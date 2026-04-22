from pathlib import Path

from pr_review_checklist_bot.rules import build_checklist, load_changed_files


def test_load_changed_files(tmp_path: Path):
    p = tmp_path / "changed.txt"
    p.write_text("src/api/routes.py\nREADME.md\n", encoding="utf-8")
    files = load_changed_files(p)
    assert files == ["src/api/routes.py", "README.md"]


def test_build_checklist_detects_high_risk():
    report = build_checklist(["app/auth/service.py", "db/migrations/001_init.sql"])
    ids = {i["id"] for i in report["checklist"]}
    assert "security-review" in ids
    assert "db-migrations" in ids
