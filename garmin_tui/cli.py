import click


@click.group()
@click.version_option()
def cli():
    ""


@cli.command(name="foo")
def foo():
    "Foo"
    print("foo")
