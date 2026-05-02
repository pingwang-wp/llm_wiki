"""Python port scaffold for src/lib/reset-project-state.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def resetProjectState(*args, **kwargs):
    raise PortNotImplementedError("reset-project-state.ts.resetProjectState is not fully ported yet")

__all__ = ['resetProjectState']
