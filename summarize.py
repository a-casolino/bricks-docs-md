#!/usr/bin/env python3
"""Prepend a plain-language Italian summary, written by Claude, to the change report.

Reads the report written by `scrape.py --report` (page list + per-page diffs) and
inserts an "In breve" section at the top. Needs ANTHROPIC_API_KEY; without it, or
if the API call fails, the report is left as it is so the email still goes out.
"""

import os
import sys
from pathlib import Path

import anthropic

MODEL = "claude-opus-5-5"

PROMPT = """Qui sotto c'è il resoconto delle modifiche di oggi alla documentazione ufficiale di Bricks Builder \
(il page builder per WordPress): l'elenco delle pagine cambiate e, per ciascuna, le righe tolte (-) e aggiunte (+).

Scrivi in italiano un riassunto discorsivo di cosa è cambiato, per un web designer che costruisce siti con Bricks \
e usa questa documentazione come contesto per l'IA.

- Apri con una frase che dica quanto è rilevante l'aggiornamento nel complesso.
- Poi spiega le modifiche sostanziali, raggruppate per argomento: cosa dice di nuovo la documentazione e cosa \
cambia in pratica (nuove funzioni, comportamenti chiariti, esempi aggiunti, avvertenze).
- Le modifiche minori (solo video sostituiti o aggiunti, link, refusi) citale in una frase sola, senza elencarle.
- Non inventare nulla che non sia nelle righe modificate. Se una modifica non è chiara dal diff, dillo.
- Usa Markdown semplice (paragrafi brevi ed elenchi puntati), nessun titolo. Al massimo circa 250 parole.

<resoconto>
{report}
</resoconto>"""


def main() -> None:
    path = Path(sys.argv[1])
    if not path.exists():
        return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set, skipping the summary", file=sys.stderr)
        return
    report = path.read_text(encoding="utf-8")

    client = anthropic.Anthropic()
    try:
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            output_config={"effort": "medium"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            messages=[{"role": "user", "content": PROMPT.format(report=report)}],
        )
    except anthropic.APIConnectionError as exc:
        print(f"Summary skipped, connection error: {exc}", file=sys.stderr)
        return
    except anthropic.APIStatusError as exc:
        print(f"Summary skipped, API error {exc.status_code}: {exc.message}", file=sys.stderr)
        return

    if response.stop_reason == "refusal":
        print("Summary skipped, request declined", file=sys.stderr)
        return
    summary = "".join(b.text for b in response.content if b.type == "text").strip()
    if not summary:
        return
    path.write_text(f"### In breve\n\n{summary}\n\n{report}", encoding="utf-8")
    print("Summary added to the report", file=sys.stderr)


if __name__ == "__main__":
    main()
