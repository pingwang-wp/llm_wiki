"""Python port scaffold for src/lib/endpoint-normalizer.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class EndpointMode:
    """Type placeholder generated from TypeScript export."""

    pass

class NormalizedEndpoint:
    """Type placeholder generated from TypeScript export."""

    pass

def normalizeEndpoint(*args, **kwargs):
    raise PortNotImplementedError("endpoint-normalizer.ts.normalizeEndpoint is not fully ported yet")

__all__ = ['EndpointMode', 'NormalizedEndpoint', 'normalizeEndpoint']
