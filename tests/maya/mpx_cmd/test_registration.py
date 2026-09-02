# coding: utf-8
from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

from bd_util.maya.mpx_cmd import MPxCommandBase
from bd_util.maya.mpx_cmd import registration

pytestmark = pytest.mark.maya


class _CommandA(MPxCommandBase[None]):
    COMMAND_NAME = "bduTestRegistrationA"

    def parse_arguments(self, arg_database: om.MArgDatabase) -> None:
        return None

    def execute(self, params: None) -> None:
        return None


class _CommandB(_CommandA):
    COMMAND_NAME = "bduTestRegistrationB"


class _FakePluginFn:
    def __init__(
        self,
        *,
        register_failure: str | None = None,
        deregister_failure: str | None = None,
    ) -> None:
        self.register_failure = register_failure
        self.deregister_failure = deregister_failure
        self.calls: list[tuple[str, str]] = []

    def registerCommand(self, name, creator, syntax_creator) -> None:
        self.calls.append(("register", name))
        if name == self.register_failure:
            raise RuntimeError(f"register failed: {name}")

    def deregisterCommand(self, name) -> None:
        self.calls.append(("deregister", name))
        if name == self.deregister_failure:
            raise RuntimeError(f"deregister failed: {name}")


def test_register_commands_rolls_back_partial_registration(monkeypatch):
    plugin_fn = _FakePluginFn(register_failure=_CommandB.COMMAND_NAME)
    monkeypatch.setattr(registration.om, "MFnPlugin", lambda plugin: plugin_fn)

    with pytest.raises(RuntimeError, match="register failed"):
        registration.register_commands(
            om.MObject(),
            (_CommandA, _CommandB),
        )

    assert plugin_fn.calls == [
        ("register", _CommandA.COMMAND_NAME),
        ("register", _CommandB.COMMAND_NAME),
        ("deregister", _CommandA.COMMAND_NAME),
    ]


def test_deregister_commands_continues_in_reverse_order(monkeypatch):
    plugin_fn = _FakePluginFn(deregister_failure=_CommandB.COMMAND_NAME)
    monkeypatch.setattr(registration.om, "MFnPlugin", lambda plugin: plugin_fn)

    with pytest.raises(RuntimeError, match="deregister failed"):
        registration.deregister_commands(
            om.MObject(),
            (_CommandA, _CommandB),
        )

    assert plugin_fn.calls == [
        ("deregister", _CommandB.COMMAND_NAME),
        ("deregister", _CommandA.COMMAND_NAME),
    ]
