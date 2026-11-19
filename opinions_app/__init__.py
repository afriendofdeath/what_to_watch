"""Пакет Flask-приложения what_to_watch."""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты в конце файла регистрируют модели, маршруты, обработчики ошибок
# и пользовательские команды после создания приложения и расширений.
from opinions_app import models  # noqa: E402,F401
from opinions_app import views  # noqa: E402,F401
from opinions_app import error_handlers  # noqa: E402,F401
from opinions_app import cli_commands  # noqa: E402,F401
