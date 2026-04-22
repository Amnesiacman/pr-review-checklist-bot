# pr-review-checklist-bot

[English version](README.md)

Генерация чеклиста ревью на основе изменённых файлов и риск-эвристик.

## Риск-сигналы

- миграции
- auth/security изменения
- API изменения
- конфиги/инфраструктура
- отсутствие изменений в тестах
- отсутствие изменений в документации

## Использование

```bash
python3 main.py --changed-files ./changed-files.txt --format markdown
python3 main.py --changed-files ./changed-files.txt --format json
python3 main.py --changed-files ./changed-files.txt --output checklist.md
```
