"""Python port scaffold for src/lib/sweep-reviews.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def extractJsonObject(*args, **kwargs):
    raise PortNotImplementedError("sweep-reviews.ts.extractJsonObject is not fully ported yet")

def sweepResolvedReviews(*args, **kwargs):
    raise PortNotImplementedError("sweep-reviews.ts.sweepResolvedReviews is not fully ported yet")

__all__ = ['extractJsonObject', 'sweepResolvedReviews']
