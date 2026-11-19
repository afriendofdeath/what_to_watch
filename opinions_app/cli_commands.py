"""Пользовательские команды Flask CLI."""

import csv

import click

from opinions_app import app, db
from opinions_app.models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Загрузить мнения из файла opinions.csv в базу данных."""
    with open('opinions.csv', encoding='utf-8') as opinions_file:
        reader = csv.DictReader(opinions_file)
        counter = 0
        for row in reader:
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено мнений: {counter}')
