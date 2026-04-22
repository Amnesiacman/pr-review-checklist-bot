# pr-review-checklist-bot

[Русская версия](README.ru.md)

Generate review checklist from changed files and risk heuristics.

## Risk signals

- migrations
- auth/security changes
- API changes
- config/infrastructure changes
- missing tests updates
- missing docs updates

## Usage

```bash
python3 main.py --changed-files ./changed-files.txt --format markdown
python3 main.py --changed-files ./changed-files.txt --format json
python3 main.py --changed-files ./changed-files.txt --output checklist.md
```
