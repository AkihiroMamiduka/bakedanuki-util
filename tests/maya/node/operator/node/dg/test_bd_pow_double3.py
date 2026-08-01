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


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_pow_double3_pair import (
        BdPowDouble3Pair,
    )
    from bd_util.maya.node.operator.node.dg.bd_pow_double3_multi import (
        BdPowDouble3Multi,
    )

    assert BdPowDouble3Pair.NODE_TYPE == "bdPowDouble3Pair"
    assert BdPowDouble3Pair.input1.long_name == "input1"
    assert BdPowDouble3Pair.i1x.short_name == "i1x"
    assert BdPowDouble3Pair.input2.long_name == "input2"
    assert BdPowDouble3Pair.i2z.short_name == "i2z"
    assert BdPowDouble3Pair.output.long_name == "output"
    assert BdPowDouble3Pair.oz.short_name == "oz"

    assert BdPowDouble3Multi.NODE_TYPE == "bdPowDouble3Multi"
    assert BdPowDouble3Multi.input.long_name == "input"
    assert BdPowDouble3Multi.i.short_name == "i"
    assert BdPowDouble3Multi.output.long_name == "output"
    assert BdPowDouble3Multi.oz.short_name == "oz"


def test_defaults_and_fixed_component_wise_power(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdPowDouble3Pair()
    multi = nodes.create.bdPowDouble3Multi()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdPowDouble3Pair1"
    assert multi.name == "bdPowDouble3Multi1"
    assert fixed.input1.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert fixed.input2.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert fixed.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert multi.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))

    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((3.0, 2.0, 0.5))
    modifier_manager.do_it_dg()
    assert fixed.output.get().as_tuple() == pytest.approx((8.0, 9.0, 2.0))


def test_fixed_clamps_small_bases_per_negative_exponent_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdPowDouble3Pair")
    maya_cmds.setAttr(
        f"{node}.input1",
        0.0,
        0.0,
        -5.0e-10,
        type="double3",
    )
    maya_cmds.setAttr(
        f"{node}.input2",
        -1.0,
        2.0,
        -1.0,
        type="double3",
    )

    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (1.0e9, 0.0, -1.0e9)
    )


def test_negative_base_with_non_integer_exponent_returns_nan(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdPowDouble3Pair")
    maya_cmds.setAttr(f"{node}.input1", -4.0, 4.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{node}.input2", 0.5, 0.5, 0.5, type="double3")
    output = maya_cmds.getAttr(f"{node}.output")[0]
    assert math.isnan(output[0])
    assert output[1:] == pytest.approx((2.0, 2.0))


@pytest.mark.parametrize(
    ("node_type", "input_values"),
    [
        (
            "bdPowDouble3Pair",
            (
                ("input1", (2.0, 3.0, 4.0)),
                ("input2", (3.0, 2.0, 0.5)),
            ),
        ),
        (
            "bdPowDouble3Multi",
            (
                ("input[2]", (2.0, 3.0, 4.0)),
                ("input[7]", (3.0, 2.0, 0.5)),
            ),
        ),
    ],
)
@pytest.mark.parametrize(
    ("output_child", "expected"),
    [("outputX", 8.0), ("outputY", 9.0), ("outputZ", 2.0)],
)
def test_output_children_can_be_requested_directly(
    maya_cmds,
    node_type,
    input_values,
    output_child,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    for input_name, value in input_values:
        maya_cmds.setAttr(f"{node}.{input_name}", *value, type="double3")

    assert maya_cmds.getAttr(f"{node}.{output_child}") == pytest.approx(
        expected
    )


def test_multi_uses_logical_index_order_and_defined_edge_cases(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdPowDouble3Multi(name="pow")
    node.input[20].set((2.0, 2.0, 2.0))
    node.input[2].set((2.0, 3.0, 4.0))
    node.input[9].set((3.0, 2.0, 0.5))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((64.0, 81.0, 4.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((9.0, 4.0, 0.25))

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((2.0, 2.0, 2.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_multi_clamps_current_bases_per_negative_exponent_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdPowDouble3Multi")
    maya_cmds.setAttr(f"{node}.input[2]", 0.0, 0.0, -5.0e-10, type="double3")
    maya_cmds.setAttr(f"{node}.input[9]", -1.0, 2.0, -1.0, type="double3")

    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (1.0e9, 0.0, -1.0e9)
    )


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdPowDouble3Pair")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{fixed}.input2", 3.0, 2.0, 0.5, type="double3")
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (8.0, 9.0, 2.0)
        )

        maya_cmds.setAttr(f"{fixed}.input2Y", -1.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (8.0, 1.0 / 3.0, 2.0)
        )

        maya_cmds.setAttr(f"{fixed}.input1Y", 0.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (8.0, 1.0e9, 2.0)
        )

        multi = maya_cmds.createNode("bdPowDouble3Multi")
        maya_cmds.setAttr(f"{multi}.input[20]", 2.0, 2.0, 2.0, type="double3")
        maya_cmds.setAttr(f"{multi}.input[2]", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0, 2.0, 0.5, type="double3")
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (64.0, 81.0, 4.0)
        )

        maya_cmds.setAttr(f"{multi}.input[9].inputY", 1.0)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (64.0, 9.0, 4.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_child_input_dependencies_cover_the_output_compound(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    for node_type, input_children in (
        (
            "bdPowDouble3Pair",
            (
                "input1X",
                "input1Y",
                "input1Z",
                "input2X",
                "input2Y",
                "input2Z",
            ),
        ),
        ("bdPowDouble3Multi", ("inputX", "inputY", "inputZ")),
    ):
        node = maya_cmds.createNode(node_type)
        selection = maya_om.MSelectionList()
        selection.add(node)
        node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

        for input_child in input_children:
            affected = node_fn.getAffectedAttributes(
                node_fn.attribute(input_child)
            )
            affected_names = {
                maya_om.MFnAttribute(attribute).name for attribute in affected
            }
            assert affected_names == {
                "output",
                "outputX",
                "outputY",
                "outputZ",
            }


def test_connection_and_existing_node_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_pow_double3_pair import (
        BdPowDouble3Pair,
    )
    from bd_util.maya.node.operator.node.dg.bd_pow_double3_multi import (
        BdPowDouble3Multi,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdPowDouble3Pair(name="fixed")
    multi = nodes.create.bdPowDouble3Multi(name="multi")
    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((3.0, 2.0, 0.5))
    fixed.output.connect(multi.input[2])
    multi.input[7].set((2.0, 0.5, 3.0))
    modifier_manager.do_it_dg()

    assert multi.output.get().as_tuple() == pytest.approx((64.0, 3.0, 8.0))
    assert isinstance(
        nodes.existing.bdPowDouble3Pair(fixed.name), BdPowDouble3Pair
    )
    assert isinstance(
        nodes.existing.bdPowDouble3Multi(multi.name),
        BdPowDouble3Multi,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdPowDouble3Pair(name="fixed")
    multi = nodes.create.bdPowDouble3Multi(name="multi")
    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((3.0, 2.0, 0.5))
    multi.input[20].set((2.0, 2.0, 2.0))
    multi.input[2].set((2.0, 3.0, 4.0))
    multi.input[9].set((3.0, 2.0, 0.5))
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0007F012
    assert multi_fn.typeId.id() == 0x0007F011

    scene_path = tmp_path / "bd_pow_double3_pair.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdPowDouble3Pair(
        "fixed"
    ).output.get().as_tuple() == pytest.approx((8.0, 9.0, 2.0))
    assert existing_nodes.existing.bdPowDouble3Multi(
        "multi"
    ).output.get().as_tuple() == pytest.approx((64.0, 81.0, 4.0))
