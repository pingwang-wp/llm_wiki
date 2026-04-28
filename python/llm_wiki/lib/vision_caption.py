"""Python port scaffold for src/lib/vision-caption.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class CaptionOptions:
    """Type placeholder generated from TypeScript export."""

    pass

CAPTION_PROMPT = None  # TODO: port from vision-caption.ts

def buildCaptionPromptWithContext(*args, **kwargs):
    raise PortNotImplementedError("vision-caption.ts.buildCaptionPromptWithContext is not fully ported yet")

def captionImage(*args, **kwargs):
    raise PortNotImplementedError("vision-caption.ts.captionImage is not fully ported yet")

__all__ = ['CAPTION_PROMPT', 'CaptionOptions', 'buildCaptionPromptWithContext', 'captionImage']
