"""Python port scaffold for src/lib/persist.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def loadChatHistory(*args, **kwargs):
    raise PortNotImplementedError("persist.ts.loadChatHistory is not fully ported yet")

def loadReviewItems(*args, **kwargs):
    raise PortNotImplementedError("persist.ts.loadReviewItems is not fully ported yet")

def saveChatHistory(*args, **kwargs):
    raise PortNotImplementedError("persist.ts.saveChatHistory is not fully ported yet")

def saveReviewItems(*args, **kwargs):
    raise PortNotImplementedError("persist.ts.saveReviewItems is not fully ported yet")

__all__ = ['loadChatHistory', 'loadReviewItems', 'saveChatHistory', 'saveReviewItems']
