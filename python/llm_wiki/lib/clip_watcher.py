"""Python port scaffold for src/lib/clip-watcher.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def startClipWatcher(*args, **kwargs):
    raise PortNotImplementedError("clip-watcher.ts.startClipWatcher is not fully ported yet")

def stopClipWatcher(*args, **kwargs):
    raise PortNotImplementedError("clip-watcher.ts.stopClipWatcher is not fully ported yet")

__all__ = ['startClipWatcher', 'stopClipWatcher']
