"""Python port scaffold for src/lib/greeting-detector.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def isGreeting(*args, **kwargs):
    raise PortNotImplementedError("greeting-detector.ts.isGreeting is not fully ported yet")

__all__ = ['isGreeting']
