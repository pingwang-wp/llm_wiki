"""Python port scaffold for src/lib/embedding.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class PageSearchResult:
    """Type placeholder generated from TypeScript export."""

    pass

def dropLegacyVectorTable(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.dropLegacyVectorTable is not fully ported yet")

def embedAllPages(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.embedAllPages is not fully ported yet")

def embedPage(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.embedPage is not fully ported yet")

def fetchEmbedding(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.fetchEmbedding is not fully ported yet")

def getEmbeddingCount(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.getEmbeddingCount is not fully ported yet")

def getLastEmbeddingError(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.getLastEmbeddingError is not fully ported yet")

def legacyVectorRowCount(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.legacyVectorRowCount is not fully ported yet")

def looksLikeOversizeError(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.looksLikeOversizeError is not fully ported yet")

def removePageEmbedding(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.removePageEmbedding is not fully ported yet")

def searchByEmbedding(*args, **kwargs):
    raise PortNotImplementedError("embedding.ts.searchByEmbedding is not fully ported yet")

__all__ = ['PageSearchResult', 'dropLegacyVectorTable', 'embedAllPages', 'embedPage', 'fetchEmbedding', 'getEmbeddingCount', 'getLastEmbeddingError', 'legacyVectorRowCount', 'looksLikeOversizeError', 'removePageEmbedding', 'searchByEmbedding']
