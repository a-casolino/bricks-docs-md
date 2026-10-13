#!/usr/bin/env python3
"""Scrape the Bricks Builder Academy (academy.bricksbuilder.io) into one Markdown file.

The site is built with Starlight (Astro). Page URLs come from the sitemap, the
order follows the sidebar navigation. The output file is only rewritten when the
documentation content actually changed, so a daily run produces a commit only
when Bricks updates its docs.
"""

import argparse
import hashlib
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse
from urllib import robotparser

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter

BASE = "https://academy.bricksbuilder.io/"
SITEMAP_INDEX = urljoin(BASE, "sitemap-index.xml")
USER_AGENT = "bricks-docs-md/1.0 (+https://github.com/a-casolino/bricks-docs-md)"
DELAY_SECONDS = 1.0  # polite crawl rate: at most one request per second
SKIP_PATHS = {"/privacy/", "/404/"}
HASH_MARKER = "<!-- content-sha256: {} -->"

session = requests.Session()
session.headers["User-Agent"] = USER_AGENT
_last_request = 0.0


def fetch(url: str) -> requests.Response:
    global _last_request
    for attempt in range(4):
        wait = DELAY_SECONDS - (time.monotonic() - _last_request)
        if wait > 0:
            time.sleep(wait)
        _last_request = time.monotonic()
        try:
            resp = session.get(url, timeout=30)
            if resp.status_code < 500 and resp.status_code != 429:
                return resp
        except requests.RequestException as exc:
            print(f"  ! {url}: {exc}", file=sys.stderr)
        time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"Could not fetch {url}")


def normalize(url: str) -> str:
    p = urlparse(urljoin(BASE, url))
    path = p.path if p.path.endswith("/") else p.path + "/"
    return f"https://{p.netloc}{path}"


def sitemap_urls() -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    index = ET.fromstring(fetch(SITEMAP_INDEX).content)
    for loc in index.findall("sm:sitemap/sm:loc", ns):
        sm = ET.fromstring(fetch(loc.text.strip()).content)
        urls += [normalize(u.text.strip()) for u in sm.findall("sm:url/sm:loc", ns)]
    return [u for u in dict.fromkeys(urls) if urlparse(u).path not in SKIP_PATHS]


def sidebar_links(soup: BeautifulSoup) -> list[str]:
    nav = soup.select_one("nav.sidebar, #starlight__sidebar, .sidebar-content")
    if not nav:
        return []
    links = []
    for a in nav.select("a[href]"):
        href = a["href"]
        if href.startswith(("http", "//")) and not href.startswith(BASE):
            continue
        links.append(normalize(href))
    return links


# ---------------------------------------------------------------- HTML cleanup

def clean_content(root: Tag, page_url: str) -> None:
    """Rewrite Starlight-specific markup into plain HTML markdownify handles well."""
    # Heading anchor links ("Section titled ...")
    for el in root.select(".sl-anchor-link, .sl-anchor-icon"):
        el.decompose()
    for wrapper in root.select(".sl-heading-wrapper"):
        wrapper.unwrap()

    # Expressive Code blocks: one div per line, title in a figcaption
    for ec in root.select(".expressive-code"):
        pre_src = ec.find("pre")
        if not pre_src:
            ec.decompose()
            continue
        lang = pre_src.get("data-language", "")
        lines = pre_src.select(".ec-line")
        if lines:
            code_text = "\n".join(
                (ln.select_one(".code") or ln).get_text() for ln in lines
            )
        else:
            code_text = pre_src.get_text()
        title_el = ec.select_one("figcaption .title")
        title = title_el.get_text(strip=True) if title_el else ""
        new = BeautifulSoup("", "html.parser")
        frag = []
        if title:
            p = new.new_tag("p")
            em = new.new_tag("em")
            em.string = title
            p.append(em)
            frag.append(p)
        pre = new.new_tag("pre")
        code = new.new_tag("code")
        if lang and lang != "plaintext":
            code["class"] = [f"language-{lang}"]
        code.string = code_text.rstrip("\n")
        pre.append(code)
        frag.append(pre)
        for f in frag:
            ec.insert_before(f)
        ec.decompose()

    # Asides (note / tip / caution / danger) -> blockquote with bold title
    for aside in root.select("aside.starlight-aside, aside"):
        title_el = aside.select_one(".starlight-aside__title")
        title = title_el.get_text(" ", strip=True) if title_el else ""
        if title_el:
            title_el.decompose()
        body = aside.select_one(".starlight-aside__content") or aside
        bq = BeautifulSoup("", "html.parser").new_tag("blockquote")
        if title:
            tmp = BeautifulSoup(f"<p><strong>{title}</strong></p>", "html.parser")
            bq.append(tmp.p)
        for child in list(body.children):
            bq.append(child.extract())
        aside.replace_with(bq)

    # Tabs -> one bold label per panel
    for tabs in root.select("starlight-tabs"):
        labels = [t.get_text(" ", strip=True) for t in tabs.select('[role="tab"]')]
        panels = tabs.select('[role="tabpanel"]')
        container = BeautifulSoup("<div></div>", "html.parser").div
        for i, panel in enumerate(panels):
            label = labels[i] if i < len(labels) else f"Tab {i + 1}"
            container.append(BeautifulSoup(f"<p><strong>{label}</strong></p>", "html.parser").p)
            for child in list(panel.children):
                container.append(child.extract())
        tabs.replace_with(container)

    # Embedded videos / iframes -> link
    for iframe in root.select("iframe[src]"):
        src = urljoin(page_url, iframe["src"])
        title = iframe.get("title") or "Embedded video"
        iframe.replace_with(BeautifulSoup(f'<p><a href="{src}">{title}</a></p>', "html.parser").p)
    for el in root.select("lite-youtube, [data-youtube-id]"):
        vid = el.get("videoid") or el.get("data-youtube-id")
        if vid:
            el.replace_with(BeautifulSoup(
                f'<p><a href="https://www.youtube.com/watch?v={vid}">Video</a></p>', "html.parser").p)

    for el in root.select("script, style, noscript, svg, button, .sr-only, starlight-file-tree button"):
        el.decompose()

    # Absolute links and images
    for a in root.select("a[href]"):
        a["href"] = urljoin(page_url, a["href"])
    for img in root.select("img"):
        src = img.get("src") or img.get("data-src")
        if src:
            img["src"] = urljoin(page_url, src)


class Converter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags=None, **kw):
        code = el.find("code")
        lang = ""
        if code and code.get("class"):
            for c in code["class"]:
                if c.startswith("language-"):
                    lang = c[len("language-"):]
        body = (code or el).get_text()
        fence = "````" if "```" in body else "```"
        return f"\n\n{fence}{lang}\n{body}\n{fence}\n\n"


def to_markdown(html_el: Tag) -> str:
    md = Converter(heading_style="ATX", bullets="-", strip=["span"]).convert_soup(html_el)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def parse_page(url: str, html: str) -> tuple[str, str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    nav = sidebar_links(soup)
    h1 = soup.select_one("main h1, h1#_top, h1")
    title = h1.get_text(" ", strip=True) if h1 else url
    content = soup.select_one(".sl-markdown-content") or soup.select_one("main")
    if content is None:
        return title, "", nav
    clean_content(content, url)
    return title, to_markdown(content), nav


# ---------------------------------------------------------------- main

def section_of(url: str) -> str:
    parts = [p for p in urlparse(url).path.split("/") if p]
    return parts[0] if parts else ""


def build(output: Path) -> bool:
    rp = robotparser.RobotFileParser(urljoin(BASE, "robots.txt"))
    rp.read()

    urls = sitemap_urls()
    print(f"{len(urls)} URLs in sitemap", file=sys.stderr)
    if not urls:
        raise RuntimeError("Empty sitemap, aborting so the existing file is kept")

    pages: dict[str, tuple[str, str]] = {}
    order: list[str] = []
    # Section index pages first: their sidebar defines the reading order.
    urls.sort(key=lambda u: len([p for p in urlparse(u).path.split("/") if p]))
    for i, url in enumerate(urls, 1):
        if not rp.can_fetch(USER_AGENT, url):
            print(f"  - robots.txt disallows {url}", file=sys.stderr)
            continue
        resp = fetch(url)
        if resp.status_code != 200 or "text/html" not in resp.headers.get("content-type", ""):
            print(f"  ! {resp.status_code} {url}", file=sys.stderr)
            continue
        title, md, nav = parse_page(url, resp.text)
        pages[url] = (title, md)
        for link in nav:
            if link not in order:
                order.append(link)
        print(f"[{i}/{len(urls)}] {title}", file=sys.stderr)

    if len(pages) < max(5, len(urls) // 2):
        raise RuntimeError(f"Only {len(pages)} of {len(urls)} pages fetched, aborting")

    ordered = [u for u in order if u in pages] + sorted(u for u in pages if u not in order)
    # Keep pages of the same top-level section together.
    sections = list(dict.fromkeys(section_of(u) for u in ordered))
    ordered.sort(key=lambda u: sections.index(section_of(u)))

    toc, body = [], []
    for url in ordered:
        title, md = pages[url]
        depth = max(0, len([p for p in urlparse(url).path.split("/") if p]) - 1)
        anchor = re.sub(r"[^a-z0-9]+", "-", urlparse(url).path.lower()).strip("-") or "home"
        toc.append(f"{'  ' * depth}- [{title}](#{anchor})")
        body.append(f'<a id="{anchor}"></a>\n\n# {title}\n\nSource: {url}\n\n{md}\n')

    content = "## Table of contents\n\n" + "\n".join(toc) + "\n\n---\n\n" + "\n---\n\n".join(body)
    digest = hashlib.sha256(content.encode()).hexdigest()

    if output.exists() and HASH_MARKER.format(digest) in output.read_text(encoding="utf-8"):
        print("No changes in the documentation.", file=sys.stderr)
        return False

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = (
        "# Bricks Builder Documentation\n\n"
        f"Unofficial Markdown export of {BASE} ({len(ordered)} pages). "
        f"Content last changed on {now}.\n\n"
        f"{HASH_MARKER.format(digest)}\n\n"
    )
    output.write_text(header + content, encoding="utf-8")
    print(f"Wrote {output} ({len(ordered)} pages).", file=sys.stderr)
    return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", default="bricks-docs.md", type=Path)
    args = ap.parse_args()
    build(args.output)
