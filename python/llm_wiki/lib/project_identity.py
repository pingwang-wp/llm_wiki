"""Python port scaffold for src/lib/project-identity.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


class ProjectIdentity:
    """Type placeholder generated from TypeScript export."""

    pass

class ProjectRegistry:
    """Type placeholder generated from TypeScript export."""

    pass

class ProjectRegistryEntry:
    """Type placeholder generated from TypeScript export."""

    pass

def ensureProjectId(*args, **kwargs):
    raise PortNotImplementedError("project-identity.ts.ensureProjectId is not fully ported yet")

def getProjectIdByPath(*args, **kwargs):
    raise PortNotImplementedError("project-identity.ts.getProjectIdByPath is not fully ported yet")

def getProjectPathById(*args, **kwargs):
    raise PortNotImplementedError("project-identity.ts.getProjectPathById is not fully ported yet")

def loadRegistry(*args, **kwargs):
    raise PortNotImplementedError("project-identity.ts.loadRegistry is not fully ported yet")

def upsertProjectInfo(*args, **kwargs):
    raise PortNotImplementedError("project-identity.ts.upsertProjectInfo is not fully ported yet")

__all__ = ['ProjectIdentity', 'ProjectRegistry', 'ProjectRegistryEntry', 'ensureProjectId', 'getProjectIdByPath', 'getProjectPathById', 'loadRegistry', 'upsertProjectInfo']
