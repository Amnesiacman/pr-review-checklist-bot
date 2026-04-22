import json
from pathlib import Path

from pr_review_checklist_bot.cli import main


def test_cli_json(tmp_path: Path, capsys):
    changed = tmp_path / "changed.txt"
    changed.write_text("src/api/routes.py\n", encoding="utf-8")
    code = main(["--changed-files", str(changed), "--format", "json"])
    payload = json.loads(capsys.readouterr().out)
    assert code == 0
    assert payload["total_files"] == 1


def test_cli_output_file(tmp_path: Path):
    changed = tmp_path / "changed.txt"
    out = tmp_path / "checklist.md"
    changed.write_text("app/auth.py\n", encoding="utf-8")
    code = main(["--changed-files", str(changed), "--output", str(out)])
    assert code == 0
    assert out.exists()
