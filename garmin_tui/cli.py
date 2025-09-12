import os

import click

from garmin_tui.core import auth


@click.group()
@click.version_option()
def cli():
    ""


@cli.command(name="login")
def login():
    "Login"
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    auth.init_api(email, password)
