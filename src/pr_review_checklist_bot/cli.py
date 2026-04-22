import argparse
import json
from pathlib import Path

from pr_review_checklist_bot.rules import build_checklist, load_changed_files, render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pr-review-checklist-bot",
        description="Generate PR review checklist from changed files",
    )
    parser.add_argument("--changed-files", required=True, help="Path to newline-separated changed files")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", help="Optional output file path")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    files = load_changed_files(Path(args.changed_files))
    report = build_checklist(files)
    text = (
        json.dumps(report, ensure_ascii=True, indent=2)
        if args.format == "json"
        else render_markdown(report)
    )
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0

