# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def _load_bd_util_nodes(maya_cmds) -> str:
    default_path = (
        Path(__file__).resolve().parents[6]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip(
            "bdUtilNodes.mll is not built. "
            "Run scripts/build-native-maya2025.cmd first."
        )

    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    return plugin_path.stem


def test_plugin_metadata_matches_runtime(maya_cmds):
    plugin_name = _load_bd_util_nodes(maya_cmds)

    assert (
        maya_cmds.pluginInfo(plugin_name, query=True, version=True)
        == bdu.__version__
    )
    assert maya_cmds.pluginInfo(
        plugin_name, query=True, apiVersion=True
    ) == str(maya_cmds.about(apiVersion=True))
