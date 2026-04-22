# pr-review-checklist-bot

`pr-review-checklist-bot` автоматически формирует чеклист ревью по измененным файлам.

## Что умеет v0.1

- принимает список changed files (один путь на строку)
- выявляет риск-зоны: миграции, auth/security, API, конфиги, отсутствие тестов/доков
- генерирует чеклист в `markdown` или `json`
- может записывать результат в файл (`--output`)

## Использование

```bash
python3 -m pip install -e .
pr-review-checklist-bot --changed-files ./changed-files.txt --format markdown
```

Пример `changed-files.txt`:

```text
src/api/routes.py
app/auth/service.py
db/migrations/002_add_index.sql
```
