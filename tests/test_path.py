from pathlib import Path
import pytest


def getssh_directory():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"


def test_getssh(monkeypatch):

    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh_directory()
    assert x == Path("/abc/.ssh")
