"""Python port scaffold for src/lib/utils.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def cn(*args, **kwargs):
    raise PortNotImplementedError("utils.ts.cn is not fully ported yet")

__all__ = ['cn']
