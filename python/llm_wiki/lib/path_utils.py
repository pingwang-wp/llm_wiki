"""Python port scaffold for src/lib/path-utils.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def getFileName(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.getFileName is not fully ported yet")

def getFileStem(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.getFileStem is not fully ported yet")

def getRelativePath(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.getRelativePath is not fully ported yet")

def isAbsolutePath(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.isAbsolutePath is not fully ported yet")

def joinPath(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.joinPath is not fully ported yet")

def normalizePath(*args, **kwargs):
    raise PortNotImplementedError("path-utils.ts.normalizePath is not fully ported yet")

__all__ = ['getFileName', 'getFileStem', 'getRelativePath', 'isAbsolutePath', 'joinPath', 'normalizePath']
