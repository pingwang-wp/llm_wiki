"""Python port scaffold for src/lib/search.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class ImageRef:
    """Type placeholder generated from TypeScript export."""

    pass

class SearchResult:
    """Type placeholder generated from TypeScript export."""

    pass

def searchWiki(*args, **kwargs):
    raise PortNotImplementedError("search.ts.searchWiki is not fully ported yet")

def tokenizeQuery(*args, **kwargs):
    raise PortNotImplementedError("search.ts.tokenizeQuery is not fully ported yet")

__all__ = ['ImageRef', 'SearchResult', 'searchWiki', 'tokenizeQuery']
