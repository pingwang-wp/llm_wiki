"""Python port scaffold for src/lib/sources-merge.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def mergeSourcesIntoContent(*args, **kwargs):
    raise PortNotImplementedError("sources-merge.ts.mergeSourcesIntoContent is not fully ported yet")

def mergeSourcesLists(*args, **kwargs):
    raise PortNotImplementedError("sources-merge.ts.mergeSourcesLists is not fully ported yet")

def parseSources(*args, **kwargs):
    raise PortNotImplementedError("sources-merge.ts.parseSources is not fully ported yet")

def writeSources(*args, **kwargs):
    raise PortNotImplementedError("sources-merge.ts.writeSources is not fully ported yet")

__all__ = ['mergeSourcesIntoContent', 'mergeSourcesLists', 'parseSources', 'writeSources']
