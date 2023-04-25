"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """omniml."""


if __name__ == "__main__":
    main(prog_name="omniml")  # pragma: no cover
