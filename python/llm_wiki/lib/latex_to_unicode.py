"""Python port scaffold for src/lib/latex-to-unicode.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def convertLatexToUnicode(*args, **kwargs):
    raise PortNotImplementedError("latex-to-unicode.ts.convertLatexToUnicode is not fully ported yet")

__all__ = ['convertLatexToUnicode']
