"""Python port scaffold for src/lib/review-utils.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def normalizeReviewTitle(*args, **kwargs):
    raise PortNotImplementedError("review-utils.ts.normalizeReviewTitle is not fully ported yet")

__all__ = ['normalizeReviewTitle']
