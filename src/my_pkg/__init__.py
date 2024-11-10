"""A package for doing great things!"""

# Read version from installed package
from importlib.metadata import version

__version__ = version("my_pkg")
__author__ = "MountainGod2"
__license__ = "MIT"
__description__ = "A package for doing great things!"


# Public objects of the package (if any)
__all__: list[str] = []
"""list: List of public objects of the my-pkg package."""
