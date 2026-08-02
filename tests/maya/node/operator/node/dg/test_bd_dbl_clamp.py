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

    from bd_util.maya.node.operator.node.dg.bd_dbl_clamp import BdDblClamp

    assert BdDblClamp.NODE_TYPE == "bdDbl_Clamp"
    assert BdDblClamp.input.long_name == "input"
    assert BdDblClamp.i.short_name == "i"
    assert BdDblClamp.minimum.long_name == "minimum"
    assert BdDblClamp.min.short_name == "min"
    assert BdDblClamp.maximum.long_name == "maximum"
    assert BdDblClamp.max.short_name == "max"
    assert BdDblClamp.output.long_name == "output"
    assert BdDblClamp.o.short_name == "o"

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl_Clamp()
    modifier_manager.do_it_dg()

    assert node.input.get() == pytest.approx(0.0)
    assert node.minimum.get() == pytest.approx(0.0)
    assert node.maximum.get() == pytest.approx(1.0)
    assert node.output.get() == pytest.approx(0.0)
    for attribute_name in ("input", "minimum", "maximum"):
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
    assert node_fn.typeId.id() == 0x0007F024


@pytest.mark.parametrize(
    ("input_value", "minimum", "maximum", "expected"),
    (
        (-5.0, 0.0, 10.0, 0.0),
        (5.0, 0.0, 10.0, 5.0),
        (15.0, 0.0, 10.0, 10.0),
        (-5.0, 10.0, 0.0, 0.0),
        (5.0, 10.0, 0.0, 5.0),
        (15.0, 10.0, 0.0, 10.0),
    ),
)
def test_clamps_with_normalized_bounds(
    maya_cmds,
    input_value,
    minimum,
    maximum,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Clamp")
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.minimum", minimum)
    maya_cmds.setAttr(f"{node}.maximum", maximum)
    assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(expected)


@pytest.mark.parametrize("nan_attribute", ("input", "minimum", "maximum"))
def test_nan_propagates_from_each_input(maya_cmds, nan_attribute):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Clamp")
    maya_cmds.setAttr(f"{node}.input", 0.5)
    maya_cmds.setAttr(f"{node}.minimum", 0.0)
    maya_cmds.setAttr(f"{node}.maximum", 1.0)
    maya_cmds.setAttr(f"{node}.{nan_attribute}", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{node}.output"))


@pytest.mark.parametrize(
    ("input_value", "minimum", "maximum", "expected"),
    (
        (3.0, float("-inf"), float("inf"), 3.0),
        (float("inf"), -5.0, 5.0, 5.0),
        (float("-inf"), -5.0, 5.0, -5.0),
        (float("inf"), float("inf"), float("-inf"), float("inf")),
    ),
)
def test_infinity_uses_normal_ordering(
    maya_cmds,
    input_value,
    minimum,
    maximum,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Clamp")
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.minimum", minimum)
    maya_cmds.setAttr(f"{node}.maximum", maximum)
    assert maya_cmds.getAttr(f"{node}.output") == expected


@pytest.mark.parametrize(
    ("input_value", "expected_sign"),
    ((-1.0, -1.0), (1.0, 1.0)),
)
def test_signed_zero_is_selected_deterministically(
    maya_cmds,
    input_value,
    expected_sign,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl_Clamp")
    maya_cmds.setAttr(f"{node}.input", input_value)
    maya_cmds.setAttr(f"{node}.minimum", -0.0)
    maya_cmds.setAttr(f"{node}.maximum", 0.0)
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
        node = maya_cmds.createNode("bdDbl_Clamp")
        maya_cmds.setAttr(f"{node}.input", 15.0)
        maya_cmds.setAttr(f"{node}.minimum", 0.0)
        maya_cmds.setAttr(f"{node}.maximum", 10.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(10.0)

        maya_cmds.setAttr(f"{node}.maximum", 20.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(15.0)

        maya_cmds.setAttr(f"{node}.minimum", 18.0)
        assert maya_cmds.getAttr(f"{node}.output") == pytest.approx(18.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_connections_existing_accessor_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDbl_Clamp(name="source_clamp")
    target = nodes.create.bdDbl_Clamp(name="target_clamp")
    source.input.set(15.0)
    source.minimum.set(0.0)
    source.maximum.set(10.0)
    source.output.connect(target.input)
    target.minimum.set(2.0)
    target.maximum.set(8.0)
    modifier_manager.do_it_dg()

    assert target.output.get() == pytest.approx(8.0)
    existing = nodes.existing.bdDbl_Clamp(target.name)
    assert type(existing) is type(target)

    scene_path = tmp_path / "bd_dbl_clamp.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDbl_Clamp("target_clamp").output.get() == (
        pytest.approx(8.0)
    )
