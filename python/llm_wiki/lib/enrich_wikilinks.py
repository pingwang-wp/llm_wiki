"""Python port scaffold for src/lib/enrich-wikilinks.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def enrichWithWikilinks(*args, **kwargs):
    raise PortNotImplementedError("enrich-wikilinks.ts.enrichWithWikilinks is not fully ported yet")

__all__ = ['enrichWithWikilinks']
