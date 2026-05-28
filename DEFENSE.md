# Защита лабораторной работы 11

## Что показать

В проекте создана простая веб-страница с формой заявки. Для неё написаны 4 UI-теста на Selenium. GitHub Actions автоматически запускает тесты при изменениях и публикует сайт на GitHub Pages после успешной проверки ветки `main`.

## Основные файлы

- `index.html` - веб-страница.
- `style.css` - оформление.
- `script.js` - логика формы.
- `tests/index_test.py` - UI-тесты.
- `.github/workflows/ci.yml` - CI/CD pipeline.

## Локальная проверка

```bash
pip install pytest selenium
python -m pytest -v tests
```

Ожидаемый результат:

```text
4 passed
```

## Сценарий работы с ветками

Если репозиторий ещё не привязан к GitHub:

```bash
git remote add origin https://github.com/<username>/<repo>.git
```

Отправить ветки:

```bash
git checkout main
git push -u origin main

git checkout dev
git push -u origin dev

git checkout fix
git push -u origin fix
```

## Pull Request сценарий

1. На GitHub открыть Pull Request из `fix` в `dev`.
2. Показать, что GitHub Actions запустил тесты.
3. Если тесты зелёные, выполнить merge в `dev`.
4. Открыть Pull Request из `dev` в `main`.
5. Дождаться зелёного результата CI.
6. Выполнить merge в `main`.
7. После push в `main` показать job `deploy` и опубликованный сайт GitHub Pages.

## Как показать падение тестов

Для демонстрации неуспешного CI можно временно сломать один тест в ветке `fix`:

```python
assert heading.text == "Неверный заголовок"
```

После push GitHub Actions покажет красный статус. Затем нужно вернуть правильный текст и отправить исправление:

```python
assert heading.text == "Заявка на консультацию"
```

## Что сказать преподавателю

Я создал отдельный git-репозиторий с простой веб-страницей. Для страницы написаны Selenium UI-тесты. GitHub Actions запускает тесты на каждый push и pull request. Деплой на GitHub Pages вынесен в отдельную job, которая зависит от тестов и запускается только для ветки `main`, поэтому сайт публикуется только после успешного CI.
