"""my_pkg package."""


def hello() -> str:
    """Return a greeting."""
    return "Hello, world!"


def main() -> None:  # pragma: no cover
    """Print the greeting."""
    print(hello())  # noqa: T201


if __name__ == "__main__":  # pragma: no cover
    main()
