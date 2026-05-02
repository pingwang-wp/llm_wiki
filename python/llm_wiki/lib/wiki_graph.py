"""Python port scaffold for src/lib/wiki-graph.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class CommunityInfo:
    """Type placeholder generated from TypeScript export."""

    pass

class GraphEdge:
    """Type placeholder generated from TypeScript export."""

    pass

class GraphNode:
    """Type placeholder generated from TypeScript export."""

    pass

def buildWikiGraph(*args, **kwargs):
    raise PortNotImplementedError("wiki-graph.ts.buildWikiGraph is not fully ported yet")

__all__ = ['CommunityInfo', 'GraphEdge', 'GraphNode', 'buildWikiGraph']
