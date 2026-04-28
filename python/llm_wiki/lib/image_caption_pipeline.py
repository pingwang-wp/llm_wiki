"""Python port scaffold for src/lib/image-caption-pipeline.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class CaptionPipelineOptions:
    """Type placeholder generated from TypeScript export."""

    pass

class CaptionPipelineResult:
    """Type placeholder generated from TypeScript export."""

    pass

__test = None  # TODO: port from image-caption-pipeline.ts

def captionMarkdownImages(*args, **kwargs):
    raise PortNotImplementedError("image-caption-pipeline.ts.captionMarkdownImages is not fully ported yet")

def loadCaptionCache(*args, **kwargs):
    raise PortNotImplementedError("image-caption-pipeline.ts.loadCaptionCache is not fully ported yet")

__all__ = ['CaptionPipelineOptions', 'CaptionPipelineResult', '__test', 'captionMarkdownImages', 'loadCaptionCache']
