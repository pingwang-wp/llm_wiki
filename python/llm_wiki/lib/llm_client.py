"""Python port scaffold for src/lib/llm-client.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class StreamCallbacks:
    """Type placeholder generated from TypeScript export."""

    pass

def streamChat(*args, **kwargs):
    raise PortNotImplementedError("llm-client.ts.streamChat is not fully ported yet")

__all__ = ['StreamCallbacks', 'streamChat']
