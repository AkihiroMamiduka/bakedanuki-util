# coding: utf-8
from __future__ import annotations

import pytest


@pytest.fixture(scope="session")
def shared_util_commands_plugin():
    """正式コマンドの登録をセッション終了まで共有し、最後に解除する。"""
    cmds = pytest.importorskip("maya.cmds")
    yield
    cmds.flushUndo()
    if cmds.pluginInfo("bdUtilCommands", query=True, loaded=True):
        cmds.unloadPlugin("bdUtilCommands")
