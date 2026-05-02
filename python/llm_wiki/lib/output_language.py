"""Python port scaffold for src/lib/output-language.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def buildLanguageDirective(*args, **kwargs):
    raise PortNotImplementedError("output-language.ts.buildLanguageDirective is not fully ported yet")

def buildLanguageReminder(*args, **kwargs):
    raise PortNotImplementedError("output-language.ts.buildLanguageReminder is not fully ported yet")

def getOutputLanguage(*args, **kwargs):
    raise PortNotImplementedError("output-language.ts.getOutputLanguage is not fully ported yet")

__all__ = ['buildLanguageDirective', 'buildLanguageReminder', 'getOutputLanguage']
