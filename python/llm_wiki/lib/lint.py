"""Python port scaffold for src/lib/lint.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class LintResult:
    """Type placeholder generated from TypeScript export."""

    pass

def runSemanticLint(*args, **kwargs):
    raise PortNotImplementedError("lint.ts.runSemanticLint is not fully ported yet")

def runStructuralLint(*args, **kwargs):
    raise PortNotImplementedError("lint.ts.runStructuralLint is not fully ported yet")

__all__ = ['LintResult', 'runSemanticLint', 'runStructuralLint']
