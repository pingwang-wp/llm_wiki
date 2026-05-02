"""Python port scaffold for src/lib/llm-providers.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class ChatMessage:
    """Type placeholder generated from TypeScript export."""

    pass

class ContentBlock:
    """Type placeholder generated from TypeScript export."""

    pass

class RequestOverrides:
    """Type placeholder generated from TypeScript export."""

    pass

def buildAnthropicUrl(*args, **kwargs):
    raise PortNotImplementedError("llm-providers.ts.buildAnthropicUrl is not fully ported yet")

def getProviderConfig(*args, **kwargs):
    raise PortNotImplementedError("llm-providers.ts.getProviderConfig is not fully ported yet")

def parseGoogleLine(*args, **kwargs):
    raise PortNotImplementedError("llm-providers.ts.parseGoogleLine is not fully ported yet")

__all__ = ['ChatMessage', 'ContentBlock', 'RequestOverrides', 'buildAnthropicUrl', 'getProviderConfig', 'parseGoogleLine']
