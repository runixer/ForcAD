import click

from .utils import run_docker, with_fast_option


@click.command(
    'rd',
    help='Run docker-compose command with correct compose files',
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@with_fast_option
@click.argument(
    'dc_args',
    nargs=-1,
    type=click.UNPROCESSED,
)
def run_docker_command(dc_args, **_kwargs):
    run_docker(list(dc_args))
