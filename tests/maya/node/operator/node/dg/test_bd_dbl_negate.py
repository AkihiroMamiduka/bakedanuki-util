# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def _load_bd_util_nodes(maya_cmds) -> Path:
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
    return plugin_path


def test_attributes_defaults_and_type_id(modifier_manager, maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_negate import BdDblNegate

    assert BdDblNegate.NODE_TYPE == "bdDbl_Negate"
    assert BdDblNegate.input.long_name == "input"
    assert BdDblNegate.i.short_name == "i"
    assert BdDblNegate.output.long_name == "output"
    assert BdDblNegate.o.short_name == "o"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Negate()
    modifier_manager.do_it_dg()

    assert node.input.get() == pytest.approx(0.0)
    assert node.output.get() == pytest.approx(-0.0)
    for attribute_name in ("input", "output"):
        assert not maya_cmds.attributeQuery(
            attribute_name,
            node=node.name,
            minExists=True,
        )
        assert not maya_cmds.attributeQuery(
            attribute_name,
            node=node.name,
            maxExists=True,
        )

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F02A


@pytest.mark.parametrize(
    ("input_value", "expected"),
    (
        (42.5, -42.5),
        (-42.5, 42.5),
        (float("inf"), float("-inf")),
        (float("-inf"), float("inf")),
    ),
)
def test_negates_value(maya_cmds, input_value, expected):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Negate")
    maya_cmds.setAttr(f"{node}.input", input_value)
    assert maya_cmds.getAttr(f"{node}.output") == expected


def test_nan_propagates(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Negate")
    maya_cmds.setAttr(f"{node}.input", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize(
    ("input_value", "expected_sign"),
    (
        (0.0, -1.0),
        (-0.0, 1.0),
    ),
)
def test_signed_zero_is_reversed(maya_cmds, input_value, expected_sign):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Negate")
    maya_cmds.setAttr(f"{node}.input", input_value)
    output = maya_cmds.getAttr(f"{node}.output")
    assert output == 0.0
    assert math.copysign(1.0, output) == expected_sign


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDbl_Negate")
        maya_cmds.setAttr(f"{node}.input", -4.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(4.0)

        maya_cmds.setAttr(f"{node}.input", 7.5)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(-7.5)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl_Negate(name="source_neg")
    target = nodes.create.bdDbl_Negate(name="target_neg")
    source.input.set(-3.5)
    source.output.connect(target.input)
    modifier_manager.do_it_dg()

    assert target.output.get() == pytest.approx(-3.5)
    existing = nodes.existing.bdDbl_Negate(target.name)
    assert type(existing) is type(target)

    scene_path = tmp_path / "bd_dbl_negate.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_Negate("target_neg").output.get() == (
        pytest.approx(-3.5)
    )
