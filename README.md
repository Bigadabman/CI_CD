# Lab11 CI/CD

Простой учебный сайт для лабораторной работы 11: CI/CD и автоматизированное тестирование.

## Что внутри

- `index.html` - простая веб-страница с формой заявки.
- `style.css` - стили страницы.
- `script.js` - обработка отправки и очистки формы.
- `tests/` - UI-тесты Selenium + pytest (Firefox).
- `.github/workflows/ci.yml` - CI/CD pipeline для GitHub Actions.

## Локальный запуск тестов

```bash
pip install pytest selenium
python -m pytest -v tests
```

## CI/CD

Workflow `CI + Deploy Pages` выполняет:

1. Запуск UI-тестов при каждом `push` и `pull_request`.
2. Публикацию сайта на GitHub Pages только при `push` в ветку `main`.
3. Деплой выполняется только после успешного прохождения тестов.
