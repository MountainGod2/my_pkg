"""Tests for my_pkg."""

from my_pkg.my_pkg import hello


def test_my_pkg() -> None:
    """Test main function."""
    assert hello() == "Hello, world!"
