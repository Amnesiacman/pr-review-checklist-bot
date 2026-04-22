from pathlib import Path


def load_changed_files(path: Path) -> list[str]:
    files = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line:
            files.append(line)
    return files


def build_checklist(files: list[str]) -> dict:
    items = []

    has_migrations = any("migrations/" in f for f in files)
    touches_auth = any(("auth" in f.lower()) or ("security" in f.lower()) for f in files)
    touches_api = any("/api/" in f or f.endswith("routes.py") for f in files)
    touches_docs = any(f.lower().endswith(".md") for f in files)
    touches_tests = any("/tests/" in f or f.startswith("tests/") for f in files)
    touches_configs = any(
        f.endswith(".yml") or f.endswith(".yaml") or "Dockerfile" in f or f.endswith(".toml")
        for f in files
    )

    if has_migrations:
        items.append(
            {
                "id": "db-migrations",
                "title": "Проверить миграции и обратную совместимость схемы",
                "severity": "high",
            }
        )
    if touches_auth:
        items.append(
            {
                "id": "security-review",
                "title": "Провести security review для auth/security изменений",
                "severity": "high",
            }
        )
    if touches_api:
        items.append(
            {
                "id": "api-contract",
                "title": "Проверить контракт API и обратную совместимость",
                "severity": "medium",
            }
        )
    if touches_configs:
        items.append(
            {
                "id": "config-impact",
                "title": "Проверить влияние конфигов/инфраструктуры на окружения",
                "severity": "medium",
            }
        )
    if not touches_tests:
        items.append(
            {
                "id": "missing-tests",
                "title": "Добавить/обновить тесты для измененного поведения",
                "severity": "high",
            }
        )
    if not touches_docs:
        items.append(
            {
                "id": "docs-update",
                "title": "Проверить необходимость обновления документации",
                "severity": "low",
            }
        )

    return {"total_files": len(files), "checklist": items}


def render_markdown(report: dict) -> str:
    lines = [
        "# PR Review Checklist",
        "",
        f"Changed files: {report['total_files']}",
        "",
    ]
    if not report["checklist"]:
        lines.append("- [x] Риск-факторов не найдено по базовым правилам.")
        return "\n".join(lines)
    for item in report["checklist"]:
        lines.append(f"- [ ] ({item['severity']}) {item['title']}")
    return "\n".join(lines)

