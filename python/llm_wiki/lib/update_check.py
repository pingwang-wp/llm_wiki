"""Python port scaffold for src/lib/update-check.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class GithubRelease:
    """Type placeholder generated from TypeScript export."""

    pass

class UpdateStatus:
    """Type placeholder generated from TypeScript export."""

    pass

UPDATE_CHECK_CACHE_MS = None  # TODO: port from update-check.ts

def checkForUpdates(*args, **kwargs):
    raise PortNotImplementedError("update-check.ts.checkForUpdates is not fully ported yet")

def fetchLatestRelease(*args, **kwargs):
    raise PortNotImplementedError("update-check.ts.fetchLatestRelease is not fully ported yet")

def isNewer(*args, **kwargs):
    raise PortNotImplementedError("update-check.ts.isNewer is not fully ported yet")

def toLatestReleaseUrl(*args, **kwargs):
    raise PortNotImplementedError("update-check.ts.toLatestReleaseUrl is not fully ported yet")

__all__ = ['GithubRelease', 'UPDATE_CHECK_CACHE_MS', 'UpdateStatus', 'checkForUpdates', 'fetchLatestRelease', 'isNewer', 'toLatestReleaseUrl']
