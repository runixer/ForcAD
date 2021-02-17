import click

from cli import utils


@click.command(help='Validate config structure')
@click.option(
    '--full',
    is_flag=True,
    help='Check full config (generated by setup command).',
)
def validate(full: bool):
    if full:
        utils.load_config()
    else:
        utils.load_basic_config()
