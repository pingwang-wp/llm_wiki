"""Python port scaffold for src/lib/raw-source-resolver.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def findRawSourceForImage(*args, **kwargs):
    raise PortNotImplementedError("raw-source-resolver.ts.findRawSourceForImage is not fully ported yet")

def imageUrlToAbsolute(*args, **kwargs):
    raise PortNotImplementedError("raw-source-resolver.ts.imageUrlToAbsolute is not fully ported yet")

__all__ = ['findRawSourceForImage', 'imageUrlToAbsolute']
