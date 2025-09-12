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


@cli.command(name="sleep")
def sleep():
    "Display sleep"
    r = get.sleep()

    plot(
        ys=[
            utils.extract_key_as_list(r, "deep"),
            utils.extract_key_as_list(r, "light"),
            utils.extract_key_as_list(r, "rem"),
            utils.extract_key_as_list(r, "awake"),
        ],
        xs=[
            utils.extract_key_as_list(r, "date"),
            utils.extract_key_as_list(r, "date"),
            utils.extract_key_as_list(r, "date"),
            utils.extract_key_as_list(r, "date"),
        ],
        color=["blue", "cyan", "magenta", "yellow"],
        legend_labels=["Deep", "Light", "REM", "Awake"],
        title="Sleep",
        lines=True,
        height=8,
        width=70,
    )


@cli.command(name="stress")
def stress():
    "Display stress"
    r = get.stress()

    plot(
        ys=[
            utils.extract_key_as_list(r, "max"),
            utils.extract_key_as_list(r, "avg"),
        ],
        xs=[
            utils.extract_key_as_list(r, "date"),
            utils.extract_key_as_list(r, "date"),
        ],
        color=["#fb4f14", "#ffb347"],
        legend_labels=["Max", "Average"],
        title="Stress",
        lines=True,
        height=5,
    )
