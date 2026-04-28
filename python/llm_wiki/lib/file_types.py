"""Python port scaffold for src/lib/file-types.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class FileCategory:
    """Type placeholder generated from TypeScript export."""

    pass

def getCodeLanguage(*args, **kwargs):
    raise PortNotImplementedError("file-types.ts.getCodeLanguage is not fully ported yet")

def getFileCategory(*args, **kwargs):
    raise PortNotImplementedError("file-types.ts.getFileCategory is not fully ported yet")

def isBinary(*args, **kwargs):
    raise PortNotImplementedError("file-types.ts.isBinary is not fully ported yet")

def isTextReadable(*args, **kwargs):
    raise PortNotImplementedError("file-types.ts.isTextReadable is not fully ported yet")

__all__ = ['FileCategory', 'getCodeLanguage', 'getFileCategory', 'isBinary', 'isTextReadable']
