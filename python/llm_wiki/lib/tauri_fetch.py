"""Python port scaffold for src/lib/tauri-fetch.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def getHttpFetch(*args, **kwargs):
    raise PortNotImplementedError("tauri-fetch.ts.getHttpFetch is not fully ported yet")

def isFetchNetworkError(*args, **kwargs):
    raise PortNotImplementedError("tauri-fetch.ts.isFetchNetworkError is not fully ported yet")

__all__ = ['getHttpFetch', 'isFetchNetworkError']
