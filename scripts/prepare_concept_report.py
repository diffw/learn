#!/usr/bin/env python3

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_text).strip("-").lower()
    return slug or "concept"


def next_report_path(root: Path, slug: str, report_date: str) -> Path:
    reports_dir = root / "concepts" / slug / "reports"
    base_name = f"{report_date}-deep-dive"
    candidate = reports_dir / f"{base_name}.md"
    if not candidate.exists():
        return candidate

    version = 2
    while True:
        candidate = reports_dir / f"{base_name}-v{version}.md"
        if not candidate.exists():
            return candidate
        version += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve the canonical output path for a concept deep-dive report."
    )
    parser.add_argument("--concept", required=True, help="Concept name, e.g. Honest Agent")
    parser.add_argument("--root", default=".", help="Project root path")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Report date in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create the parent report directory if it does not exist",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print structured JSON instead of only the report path",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = slugify(args.concept)
    report_path = next_report_path(root, slug, args.date)

    if args.create:
        report_path.parent.mkdir(parents=True, exist_ok=True)

    if args.json:
        payload = {
            "concept": args.concept,
            "slug": slug,
            "root": str(root),
            "report_dir": str(report_path.parent),
            "report_path": str(report_path),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(report_path)


if __name__ == "__main__":
    main()
