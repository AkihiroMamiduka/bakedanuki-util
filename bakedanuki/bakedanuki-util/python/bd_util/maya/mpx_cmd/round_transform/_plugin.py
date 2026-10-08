# coding: utf-8
from __future__ import annotations

from maya import cmds

_PLUGIN_NAME = "bdUtilCommands"


def ensure_util_commands_plugin_loaded() -> None:
    """正式な util コマンドプラグインを必要時に読み込む。"""
    loaded: object = cmds.pluginInfo(_PLUGIN_NAME, query=True, loaded=True)
    if not isinstance(loaded, bool):
        raise TypeError(
            f"Unexpected pluginInfo result for '{_PLUGIN_NAME}': {loaded!r}"
        )
    if not loaded:
        cmds.loadPlugin(f"{_PLUGIN_NAME}.py", quiet=True)
