"""Python port scaffold for src/lib/ingest-cache.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def checkIngestCache(*args, **kwargs):
    raise PortNotImplementedError("ingest-cache.ts.checkIngestCache is not fully ported yet")

def removeFromIngestCache(*args, **kwargs):
    raise PortNotImplementedError("ingest-cache.ts.removeFromIngestCache is not fully ported yet")

def saveIngestCache(*args, **kwargs):
    raise PortNotImplementedError("ingest-cache.ts.saveIngestCache is not fully ported yet")

__all__ = ['checkIngestCache', 'removeFromIngestCache', 'saveIngestCache']
