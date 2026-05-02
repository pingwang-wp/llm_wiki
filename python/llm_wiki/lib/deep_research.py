"""Python port scaffold for src/lib/deep-research.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def queueResearch(*args, **kwargs):
    raise PortNotImplementedError("deep-research.ts.queueResearch is not fully ported yet")

__all__ = ['queueResearch']
