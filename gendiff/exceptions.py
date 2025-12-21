class GendiffError(Exception):
    """Base exception for all gendiff errors."""


class UnsupportedFormatError(GendiffError):
    """Raised when the input file format is not supported."""
