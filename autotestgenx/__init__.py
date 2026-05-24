"""AutoTestGenX package root."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("autotestgenx")
except PackageNotFoundError:
    __version__ = "3.0.0"

__all__ = ["__version__"]
