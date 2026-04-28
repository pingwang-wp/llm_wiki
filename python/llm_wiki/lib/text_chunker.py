"""Python port scaffold for src/lib/text-chunker.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class Chunk:
    """Type placeholder generated from TypeScript export."""

    pass

class ChunkingOptions:
    """Type placeholder generated from TypeScript export."""

    pass

def chunkMarkdown(*args, **kwargs):
    raise PortNotImplementedError("text-chunker.ts.chunkMarkdown is not fully ported yet")

def stripFrontmatter(*args, **kwargs):
    raise PortNotImplementedError("text-chunker.ts.stripFrontmatter is not fully ported yet")

__all__ = ['Chunk', 'ChunkingOptions', 'chunkMarkdown', 'stripFrontmatter']
