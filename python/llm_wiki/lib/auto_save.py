"""Python port scaffold for src/lib/auto-save.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def setupAutoSave(*args, **kwargs):
    raise PortNotImplementedError("auto-save.ts.setupAutoSave is not fully ported yet")

__all__ = ['setupAutoSave']
