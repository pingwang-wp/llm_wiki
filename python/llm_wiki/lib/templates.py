"""Python port scaffold for src/lib/templates.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class WikiTemplate:
    """Type placeholder generated from TypeScript export."""

    pass

templates = None  # TODO: port from templates.ts

def getTemplate(*args, **kwargs):
    raise PortNotImplementedError("templates.ts.getTemplate is not fully ported yet")

__all__ = ['WikiTemplate', 'getTemplate', 'templates']
