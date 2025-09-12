import os

import click
from uniplot import plot

from garmin_tui.core import auth, get, utils


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


@cli.command(name="bb")
def body_battery():
    "Display body battery"
    r = get.body_battery()

    plot(
        ys=utils.extract_key_as_list(r, "charged"),
        xs=utils.extract_key_as_list(r, "date"),
        title="Body Battery",
        lines=True,
        height=5,
        width=70,
    )
