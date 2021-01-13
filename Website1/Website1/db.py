import sqlite3

import click
from flask import g, current_app
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES)

        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('sql/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.commit()


@click.command('init-table')
@with_appcontext
def init_tables():
    db = get_db()
    with current_app.open_resource('sql/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.commit()
        click.echo('Tables are created')


@click.command('sample-data')
@with_appcontext
def sample_data():
    db = get_db()
    with current_app.open_resource('sql/sample_data.sql') as f:
        db.executescript(f.read().decode('utf8'))
        db.commit()
        click.echo('Data are inserted')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_tables)
    app.cli.add_command(sample_data)
