# coding: utf-8
from __future__ import annotations

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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_divide import (
        BdDbl3Divide,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_divide_multi import (
        BdDbl3DivideMulti,
    )

    assert BdDbl3Divide.NODE_TYPE == "bdDbl3_Divide"
    assert BdDbl3Divide.input1.long_name == "input1"
    assert BdDbl3Divide.i1x.short_name == "i1x"
    assert BdDbl3Divide.input2.long_name == "input2"
    assert BdDbl3Divide.i2z.short_name == "i2z"
    assert BdDbl3Divide.output.long_name == "output"
    assert BdDbl3Divide.oz.short_name == "oz"

    assert BdDbl3DivideMulti.NODE_TYPE == "bdDbl3_DivideMulti"
    assert BdDbl3DivideMulti.input.long_name == "input"
    assert BdDbl3DivideMulti.i.short_name == "i"
    assert BdDbl3DivideMulti.output.long_name == "output"
    assert BdDbl3DivideMulti.oz.short_name == "oz"


def test_defaults_and_fixed_component_wise_division(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Divide()
    multi = nodes.create.bdDbl3_DivideMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl3_Divide1"
    assert multi.name == "bdDbl3_DivideMulti1"
    assert fixed.input1.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert fixed.input2.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert fixed.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))
    assert multi.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))

    fixed.input1.set((12.0, 20.0, 30.0))
    fixed.input2.set((3.0, 4.0, 5.0))
    modifier_manager.do_it_dg()
    assert fixed.output.get().as_tuple() == pytest.approx((4.0, 5.0, 6.0))


def test_fixed_clamps_small_divisors_per_component(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdDbl3_Divide")
    maya_cmds.setAttr(f"{node}.input1", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(
        f"{node}.input2",
        0.0,
        5.0e-10,
        -5.0e-10,
        type="double3",
    )

    assert maya_cmds.getAttr(f"{node}.output")[0] == pytest.approx(
        (1.0e9, 2.0e9, -3.0e9)
    )


@pytest.mark.parametrize(
    ("node_type", "input_values"),
    [
        (
            "bdDbl3_Divide",
            (
                ("input1", (12.0, 20.0, 30.0)),
                ("input2", (3.0, 4.0, 5.0)),
            ),
        ),
        (
            "bdDbl3_DivideMulti",
            (
                ("input[2]", (12.0, 20.0, 30.0)),
                ("input[7]", (3.0, 4.0, 5.0)),
            ),
        ),
    ],
)
@pytest.mark.parametrize(
    ("output_child", "expected"),
    [("outputX", 4.0), ("outputY", 5.0), ("outputZ", 6.0)],
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
    node = nodes.create.bdDbl3_DivideMulti(name="div")
    node.input[20].set((2.0, 4.0, 5.0))
    node.input[2].set((120.0, 240.0, 600.0))
    node.input[9].set((3.0, 5.0, 10.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((20.0, 12.0, 12.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((1.5, 1.25, 2.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((2.0, 4.0, 5.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_multi_clamps_divisors_per_component(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_DivideMulti(name="div")
    node.input[2].set((1.0, 2.0, 3.0))
    node.input[9].set((0.0, 5.0e-10, -5.0e-10))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx(
        (1.0e9, 2.0e9, -3.0e9)
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

        fixed = maya_cmds.createNode("bdDbl3_Divide")
        maya_cmds.setAttr(f"{fixed}.input1", 12.0, 20.0, 30.0, type="double3")
        maya_cmds.setAttr(f"{fixed}.input2", 3.0, 4.0, 5.0, type="double3")
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (4.0, 5.0, 6.0)
        )

        maya_cmds.setAttr(f"{fixed}.input2Y", 0.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (4.0, 2.0e10, 6.0)
        )

        multi = maya_cmds.createNode("bdDbl3_DivideMulti")
        maya_cmds.setAttr(f"{multi}.input[20]", 2.0, 4.0, 5.0, type="double3")
        maya_cmds.setAttr(
            f"{multi}.input[2]", 120.0, 240.0, 600.0, type="double3"
        )
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0, 5.0, 10.0, type="double3")
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (20.0, 12.0, 12.0)
        )

        maya_cmds.setAttr(f"{multi}.input[9].inputY", 0.0)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (20.0, 6.0e10, 12.0)
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
            "bdDbl3_Divide",
            (
                "input1X",
                "input1Y",
                "input1Z",
                "input2X",
                "input2Y",
                "input2Z",
            ),
        ),
        ("bdDbl3_DivideMulti", ("inputX", "inputY", "inputZ")),
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

    from bd_util.maya.node.operator.node.dg.bd_dbl3_divide import (
        BdDbl3Divide,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_divide_multi import (
        BdDbl3DivideMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Divide(name="fixed")
    multi = nodes.create.bdDbl3_DivideMulti(name="multi")
    fixed.input1.set((12.0, 20.0, 30.0))
    fixed.input2.set((3.0, 4.0, 5.0))
    fixed.output.connect(multi.input[2])
    multi.input[7].set((2.0, 5.0, 3.0))
    modifier_manager.do_it_dg()

    assert multi.output.get().as_tuple() == pytest.approx((2.0, 1.0, 2.0))
    assert isinstance(nodes.existing.bdDbl3_Divide(fixed.name), BdDbl3Divide)
    assert isinstance(
        nodes.existing.bdDbl3_DivideMulti(multi.name),
        BdDbl3DivideMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Divide(name="fixed")
    multi = nodes.create.bdDbl3_DivideMulti(name="multi")
    fixed.input1.set((12.0, 20.0, 30.0))
    fixed.input2.set((3.0, 4.0, 5.0))
    multi.input[20].set((2.0, 4.0, 5.0))
    multi.input[2].set((120.0, 240.0, 600.0))
    multi.input[9].set((3.0, 5.0, 10.0))
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0014268D
    assert multi_fn.typeId.id() == 0x0014268C

    scene_path = tmp_path / "bd_dbl3_divide.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDbl3_Divide(
        "fixed"
    ).output.get().as_tuple() == pytest.approx((4.0, 5.0, 6.0))
    assert existing_nodes.existing.bdDbl3_DivideMulti(
        "multi"
    ).output.get().as_tuple() == pytest.approx((20.0, 12.0, 12.0))
