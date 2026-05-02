"""Python port scaffold for src/lib/project-mutex.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def __resetProjectLocksForTesting(*args, **kwargs):
    raise PortNotImplementedError("project-mutex.ts.__resetProjectLocksForTesting is not fully ported yet")

__all__ = ['__resetProjectLocksForTesting']
