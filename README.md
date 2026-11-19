# what_to_watch

Flask-приложение со случайными мнениями о фильмах.

## Установка и запуск (Windows / Git Bash)

Перейдите в каталог проекта и создайте виртуальное окружение:

```bash
python -m venv venv
source venv/Scripts/activate
```

Установите зависимости:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Скопируйте `.env.example` в `.env` (если `.env` ещё не создан) и задайте собственное значение `SECRET_KEY`.

Примените миграции и запустите приложение:

```bash
flask db upgrade
flask run
```

Откройте http://127.0.0.1:5000/.

## Загрузка мнений

Если база данных ещё не содержит мнений, выполните:

```bash
flask load_opinions
```

Команда читает `opinions.csv` из корневого каталога проекта.

## Структура

- `opinions_app/` — пакет приложения: модели, формы, маршруты, обработчики ошибок и CLI-команды.
- `settings.py` — конфигурация Flask.
- `.env` — локальные переменные окружения (не добавляется в Git).
- `migrations/` — миграции базы данных.
- `backup/opinions_app.py` — резервная копия исходного монолитного модуля.
