import click
from password_generator import generate_password


@click.command()
@click.option(
    "--length",
    type=int,
    default=16,
    help="Password length.",
)
@click.option(
    "--digits",
    is_flag=True,
    default=False,
    help="Add digits to the password.",
)
@click.option(
    "--special",
    is_flag=True,
    default=False,
    help="Add special characters to the password.",
)
def main(length: int, digits: bool, special: bool) -> None:
    password = generate_password(
        len_password=length,
        digits=digits,
        special_chars=special,
    )

    click.echo(password)


if __name__ == "__main__":
    main()
