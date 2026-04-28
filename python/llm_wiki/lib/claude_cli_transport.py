"""Python port scaffold for src/lib/claude-cli-transport.ts."""

from __future__ import annotations


class PortNotImplementedError(NotImplementedError):
    """Raised when a TypeScript module has not been fully ported yet."""


def createClaudeCodeStreamParser(*args, **kwargs):
    raise PortNotImplementedError("claude-cli-transport.ts.createClaudeCodeStreamParser is not fully ported yet")

def streamClaudeCodeCli(*args, **kwargs):
    raise PortNotImplementedError("claude-cli-transport.ts.streamClaudeCodeCli is not fully ported yet")

__all__ = ['createClaudeCodeStreamParser', 'streamClaudeCodeCli']
