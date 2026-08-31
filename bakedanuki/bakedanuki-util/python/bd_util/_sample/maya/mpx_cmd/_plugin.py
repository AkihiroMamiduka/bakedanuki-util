# coding: utf-8
from __future__ import annotations

from maya import cmds

_PLUGIN_FILE_NAME = "bdUtilSampleCommands.py"
_PLUGIN_NAME = "bdUtilSampleCommands"


def ensure_sample_commands_plugin_loaded() -> None:
    """Load the shared sample commands plug-in on first facade use."""
    is_loaded: object = cmds.pluginInfo(
        _PLUGIN_NAME,
        query=True,
        loaded=True,
    )
    if not isinstance(is_loaded, bool):
        raise TypeError(
            f"Unexpected pluginInfo result for '{_PLUGIN_NAME}': "
            f"{is_loaded!r}"
        )
    if not is_loaded:
        cmds.loadPlugin(_PLUGIN_FILE_NAME, quiet=True)
