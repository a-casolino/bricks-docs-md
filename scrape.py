#!/usr/bin/env python3
"""Export the Bricks Builder Academy (academy.bricksbuilder.io) as Markdown for AI context.

The Academy publishes a machine-readable index (content-index.json) and a Markdown
alternate for every page (the page URL with a .md suffix). This script reads the
index, downloads each Markdown source, strips the Astro/Starlight-specific syntax
(frontmatter, MDX imports, components, ::: directives) and writes:

  bricks-docs.md            every page in one file
  sections/<section>.md     one file per top-level section (builder, developer, ...)
  llms.txt                  index of the files above

Pages without a Markdown alternate fall back to HTML-to-Markdown conversion.
Files are rewritten only when their content changed, so the daily GitHub Actions
run commits only when Bricks updates its docs.
"""

import argparse
import hashlib
import json
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
CONTENT_INDEX = urljoin(BASE, "content-index.json")
SITEMAP_INDEX = urljoin(BASE, "sitemap-index.xml")
USER_AGENT = "bricks-docs-md/1.0 (+https://github.com/a-casolino/bricks-docs-md)"
DELAY_SECONDS = 1.0  # polite crawl rate: at most one request per second
SKIP_PATHS = {"/privacy/", "/404/"}
HASH_MARKER = "<!-- content-sha256: {} -->"
PUBLIC_BASE = "https://raw.githubusercontent.com/a-casolino/bricks-docs-md/main/"

SECTION_TITLES = {
    "getting-started": "Getting Started",
    "builder": "Builder",
    "developer": "Developer",
    "schema": "Schema (Bricks Data Model)",
    "integrations": "Integrations",
    "woocommerce": "WooCommerce",
}

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


def path_parts(url: str) -> list[str]:
    return [p for p in urlparse(url).path.split("/") if p]


def section_of(url: str) -> str:
    parts = path_parts(url)
    if parts[:2] == ["developer", "schema"]:
        return "schema"
    return parts[0] if parts else "home"


# ---------------------------------------------------------------- page list

def index_pages() -> list[dict]:
    """Pages from content-index.json, falling back to the sitemap."""
    try:
        resp = fetch(CONTENT_INDEX)
        resp.raise_for_status()
        items = resp.json()["items"]
        pages = [
            {"url": normalize(i["url"]), "title": i.get("title"),
             "markdownUrl": i.get("markdownUrl"), "lastmod": i.get("lastmod")}
            for i in items if i.get("url")
        ]
        if pages:
            return pages
    except (requests.RequestException, ValueError, KeyError, RuntimeError) as exc:
        print(f"content-index.json unavailable ({exc}), using the sitemap", file=sys.stderr)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    index = ET.fromstring(fetch(SITEMAP_INDEX).content)
    for loc in index.findall("sm:sitemap/sm:loc", ns):
        sm = ET.fromstring(fetch(loc.text.strip()).content)
        urls += [normalize(u.text.strip()) for u in sm.findall("sm:url/sm:loc", ns)]
    return [{"url": u, "title": None, "markdownUrl": u.rstrip("/") + ".md", "lastmod": None}
            for u in dict.fromkeys(urls)]


# ---------------------------------------------------------------- Markdown source cleanup

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
DIRECTIVE_OPEN_RE = re.compile(r"^\s*(:{3,})(\w+)(?:\[(.*?)\])?\s*$")
DIRECTIVE_CLOSE_RE = re.compile(r"^\s*:{3,}\s*$")
ATTR_RE = re.compile(r'(\w+)=(?:"([^"]*)"|\'([^\']*)\'|\{["\']([^"\']*)["\']\})')
COMPONENT_LINE_RE = re.compile(r"^\s*<(/?)([A-Z]\w*)\b([^>]*?)(/?)>\s*$")
MD_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()(/[^)\s]*)")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    meta = {}
    lines = text.lstrip("\ufeff").split("\n")
    if not lines or lines[0].strip() != "---":
        return meta, text
    # Tolerate repeated opening "---" lines before the fields.
    start = 0
    while start < len(lines) and lines[start].strip() == "---":
        start += 1
    try:
        end = next(i for i in range(start, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return meta, text
    for line in lines[start:end]:
        if ":" in line and not line.startswith((" ", "\t", "-")):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, "\n".join(lines[end + 1:])


def clean_markdown(text: str) -> str:
    out: list[str] = []
    fence = None
    quote_depth = 0  # nesting level of ::: directives rendered as blockquotes
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if fence:
            out.append(("> " * quote_depth) + line if quote_depth else line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            out.append(("> " * quote_depth) + line if quote_depth else line)
            continue

        if re.match(r"^\s*(import|export)\s.+from\s+[\'\"]", line):
            continue
        d = DIRECTIVE_OPEN_RE.match(line)
        if d:
            label = d.group(3) or d.group(2).capitalize()
            out.append(("> " * quote_depth) + f"> **{label}**")
            out.append(("> " * quote_depth) + ">")
            quote_depth += 1
            continue
        if DIRECTIVE_CLOSE_RE.match(line) and quote_depth:
            quote_depth -= 1
            out.append("")
            continue

        c = COMPONENT_LINE_RE.match(line)
        if c:
            closing, name, attrs_src = c.group(1), c.group(2), c.group(3)
            attrs = {a[0]: a[1] or a[2] or a[3] for a in ATTR_RE.findall(attrs_src)}
            if not closing and name in ("TabItem", "Tab"):
                line = f"\n**{attrs.get('label', 'Tab')}**\n"
            elif not closing and name in ("LinkCard", "Card", "LinkButton") and attrs.get("href"):
                line = f"- [{attrs.get('title') or attrs.get('label') or attrs['href']}]({attrs['href']})"
            elif not closing and name in ("Card",) and attrs.get("title"):
                line = f"**{attrs['title']}**"
            elif not closing and name == "Aside":
                label = attrs.get("title") or attrs.get("type", "note").capitalize()
                out.append(("> " * quote_depth) + f"> **{label}**")
                out.append(("> " * quote_depth) + ">")
                quote_depth += 1
                continue
            elif closing and name == "Aside" and quote_depth:
                quote_depth -= 1
                out.append("")
                continue
            else:
                continue  # wrapper components (<Tabs>, <Steps>, <CardGrid>...) carry no text
        if quote_depth:
            line = ("> " * quote_depth + line).rstrip()
        out.append(line)

    md = "\n".join(out)
    md = MD_LINK_RE.sub(lambda m: m.group(1) + urljoin(BASE, m.group(2)), md)
    md = re.sub(r'(src|href)="(/[^"]*)"', lambda m: f'{m.group(1)}="{urljoin(BASE, m.group(2))}"', md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def strip_title(md: str, title: str) -> str:
    """Drop a leading "# Title" that duplicates the page title we add ourselves."""
    lines = md.split("\n")
    if lines and re.match(r"^#\s+", lines[0]) and lines[0][1:].strip().lower() == title.lower():
        return "\n".join(lines[1:]).strip()
    return md


# ---------------------------------------------------------------- HTML fallback

def sidebar_links(soup: BeautifulSoup) -> list[str]:
    nav = soup.select_one("nav.sidebar, #starlight__sidebar, .sidebar-content")
    if not nav:
        return []
    return [normalize(a["href"]) for a in nav.select("a[href]")
            if not a["href"].startswith(("http", "//")) or a["href"].startswith(BASE)]



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


# ---------------------------------------------------------------- page fetch

def get_page(page: dict) -> tuple[str, str] | None:
    url = page["url"]
    md_url = page.get("markdownUrl")
    if md_url:
        resp = fetch(md_url)
        ctype = resp.headers.get("content-type", "")
        if resp.status_code == 200 and "html" not in ctype:
            meta, body = parse_frontmatter(resp.text)
            title = meta.get("title") or page.get("title") or url
            md = strip_title(clean_markdown(body), title)
            if meta.get("description"):
                md = f"*{meta['description']}*\n\n{md}"
            return title, md
    resp = fetch(url)
    if resp.status_code != 200 or "text/html" not in resp.headers.get("content-type", ""):
        print(f"  ! {resp.status_code} {url}", file=sys.stderr)
        return None
    title, md, _ = parse_page(url, resp.text)
    return page.get("title") or title, md


def anchor_for(url: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", urlparse(url).path.lower()).strip("-") or "home"


def render(title: str, intro: str, entries: list[tuple[str, str, str]]) -> str:
    toc, body = [], []
    for url, page_title, md in entries:
        depth = max(0, len(path_parts(url)) - 1)
        toc.append(f"{'  ' * depth}- [{page_title}](#{anchor_for(url)})")
        body.append(f'<a id="{anchor_for(url)}"></a>\n\n# {page_title}\n\nSource: {url}\n\n{md}\n')
    content = "## Table of contents\n\n" + "\n".join(toc) + "\n\n---\n\n" + "\n---\n\n".join(body)
    return f"# {title}\n\n{intro}\n\n" + content


def write_if_changed(path: Path, text: str) -> bool:
    """Write text with a content hash; keep the old file (and its date) if nothing changed."""
    digest = hashlib.sha256(text.encode()).hexdigest()
    marker = HASH_MARKER.format(digest)
    if path.exists() and marker in path.read_text(encoding="utf-8"):
        return False
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    first, rest = text.split("\n", 1)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{first}\n\n{marker}\n<!-- content last changed: {now} -->\n{rest}", encoding="utf-8")
    print(f"Updated {path}", file=sys.stderr)
    return True


def build(out_dir: Path) -> bool:
    # Fetch robots.txt with our own session (urllib's default client may be blocked).
    rp = robotparser.RobotFileParser()
    robots = fetch(urljoin(BASE, "robots.txt"))
    rp.parse(robots.text.splitlines() if robots.status_code == 200 else [])

    pages = [p for p in index_pages() if urlparse(p["url"]).path not in SKIP_PATHS]
    print(f"{len(pages)} pages in the index", file=sys.stderr)
    if not pages:
        raise RuntimeError("Empty page list, aborting so the existing files are kept")

    done: list[tuple[str, str, str]] = []
    for i, page in enumerate(pages, 1):
        if not rp.can_fetch(USER_AGENT, page["url"]):
            print(f"  - robots.txt disallows {page['url']}", file=sys.stderr)
            continue
        result = get_page(page)
        if result:
            done.append((page["url"], *result))
            print(f"[{i}/{len(pages)}] {result[0]}", file=sys.stderr)

    if len(done) < max(5, int(len(pages) * 0.8)):
        raise RuntimeError(f"Only {len(done)} of {len(pages)} pages fetched, aborting")

    # Keep the index order, grouped by section in order of first appearance.
    sections = list(dict.fromkeys(section_of(u) for u, _, _ in done))
    done.sort(key=lambda e: sections.index(section_of(e[0])))

    note = (f"Unofficial Markdown export of the Bricks Builder Academy ({BASE}), "
            "refreshed daily. Content © Bricks.")
    changed = write_if_changed(
        out_dir / "bricks-docs.md",
        render("Bricks Builder Documentation", f"{note} {len(done)} pages.", done),
    )

    llms = ["# Bricks Builder Documentation (Markdown)", "",
            f"> {note}", "",
            "## Files", "",
            f"- [All pages]({PUBLIC_BASE}bricks-docs.md): the complete documentation in one file"]
    for sec in sections:
        entries = [e for e in done if section_of(e[0]) == sec]
        name = SECTION_TITLES.get(sec, sec.replace("-", " ").title())
        changed |= write_if_changed(
            out_dir / "sections" / f"{sec}.md",
            render(f"Bricks Builder Documentation: {name}", f"{note} {len(entries)} pages.", entries),
        )
        llms.append(f"- [{name}]({PUBLIC_BASE}sections/{sec}.md): {len(entries)} pages")
    llms_path = out_dir / "llms.txt"
    llms_text = "\n".join(llms) + "\n"
    if not llms_path.exists() or llms_path.read_text(encoding="utf-8") != llms_text:
        llms_path.write_text(llms_text, encoding="utf-8")
        changed = True

    print("Changes written." if changed else "No changes in the documentation.", file=sys.stderr)
    return changed


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-o", "--out-dir", default=".", type=Path)
    args = ap.parse_args()
    build(args.out_dir)
