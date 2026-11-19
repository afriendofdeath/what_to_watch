"""Настройки приложения what_to_watch."""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Конфигурация Flask-приложения."""

    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.getenv('SECRET_KEY')
