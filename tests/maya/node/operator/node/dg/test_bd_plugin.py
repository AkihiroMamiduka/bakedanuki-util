# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya

_REGISTERED_NODE_ID_START = 0x00142680
_REGISTERED_NODE_ID_END = 0x0014277F


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


def test_node_type_ids_are_unique_and_in_registered_block(maya_cmds, maya_om):
    plugin_name = _load_bd_util_nodes(maya_cmds)
    node_types = maya_cmds.pluginInfo(plugin_name, query=True, dependNode=True)

    assert len(node_types) == 156

    type_ids = [
        maya_om.MNodeClass(node_type).typeId.id() for node_type in node_types
    ]
    assert len(type_ids) == len(set(type_ids))
    assert all(
        _REGISTERED_NODE_ID_START <= type_id <= _REGISTERED_NODE_ID_END
        for type_id in type_ids
    )


@pytest.mark.parametrize(
    ("extension", "file_type"),
    (("ma", "mayaAscii"), ("mb", "mayaBinary")),
)
def test_registered_nodes_round_trip(
    maya_cmds,
    maya_om,
    new_scene,
    tmp_path,
    extension,
    file_type,
):
    plugin_name = _load_bd_util_nodes(maya_cmds)
    node_types = maya_cmds.pluginInfo(plugin_name, query=True, dependNode=True)
    expected_nodes = {}
    for index, node_type in enumerate(node_types):
        node_name = maya_cmds.createNode(
            node_type, name=f"bd_round_trip_{index:03d}"
        )
        expected_nodes[node_name] = (
            node_type,
            maya_om.MNodeClass(node_type).typeId.id(),
        )

    scene_path = tmp_path / f"bd_util_nodes.{extension}"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type=file_type, force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    for node_name, (node_type, type_id) in expected_nodes.items():
        assert maya_cmds.nodeType(node_name) == node_type

        selection = maya_om.MSelectionList()
        selection.add(node_name)
        node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
        assert node_fn.typeId.id() == type_id
