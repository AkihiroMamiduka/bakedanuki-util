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

    from bd_util.maya.node.operator.node.dg.bd_double3_sub import BdDouble3Sub
    from bd_util.maya.node.operator.node.dg.bd_double3_sub_multi import (
        BdDouble3SubMulti,
    )

    assert BdDouble3Sub.NODE_TYPE == "bdDouble3Sub"
    assert BdDouble3Sub.input1.long_name == "input1"
    assert BdDouble3Sub.i1x.short_name == "i1x"
    assert BdDouble3Sub.input2.long_name == "input2"
    assert BdDouble3Sub.i2z.short_name == "i2z"
    assert BdDouble3Sub.output.long_name == "output"
    assert BdDouble3Sub.oz.short_name == "oz"

    assert BdDouble3SubMulti.NODE_TYPE == "bdDouble3SubMulti"
    assert BdDouble3SubMulti.input.long_name == "input"
    assert BdDouble3SubMulti.i.short_name == "i"
    assert BdDouble3SubMulti.output.long_name == "output"
    assert BdDouble3SubMulti.oz.short_name == "oz"


def test_defaults_and_fixed_component_wise_subtraction(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Sub()
    multi = nodes.create.bdDouble3SubMulti()
    fixed.input1.set((10.0, 20.0, 30.0))
    fixed.input2.set((1.0, 5.0, 7.0))
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDouble3Sub1"
    assert multi.name == "bdDouble3SubMulti1"
    assert fixed.output.get().as_tuple() == pytest.approx((9.0, 15.0, 23.0))
    assert multi.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))


@pytest.mark.parametrize(
    ("node_type", "input_values"),
    [
        (
            "bdDouble3Sub",
            (
                ("input1", (10.0, 20.0, 30.0)),
                ("input2", (1.0, 5.0, 7.0)),
            ),
        ),
        (
            "bdDouble3SubMulti",
            (
                ("input[2]", (10.0, 20.0, 30.0)),
                ("input[7]", (1.0, 5.0, 7.0)),
            ),
        ),
    ],
)
@pytest.mark.parametrize(
    ("output_child", "expected"),
    [("outputX", 9.0), ("outputY", 15.0), ("outputZ", 23.0)],
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
    node = nodes.create.bdDouble3SubMulti(name="sub")
    node.input[20].set((1.0, 2.0, 3.0))
    node.input[2].set((20.0, 30.0, 40.0))
    node.input[9].set((3.0, 5.0, 7.0))
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((16.0, 23.0, 30.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((2.0, 3.0, 4.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((1.0, 2.0, 3.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[20]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDouble3Sub")
        maya_cmds.setAttr(f"{fixed}.input1", 10.0, 20.0, 30.0, type="double3")
        maya_cmds.setAttr(f"{fixed}.input2", 1.0, 5.0, 7.0, type="double3")
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (9.0, 15.0, 23.0)
        )

        maya_cmds.setAttr(f"{fixed}.input2Y", 8.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (9.0, 12.0, 23.0)
        )

        multi = maya_cmds.createNode("bdDouble3SubMulti")
        maya_cmds.setAttr(f"{multi}.input[20]", 1.0, 2.0, 3.0, type="double3")
        maya_cmds.setAttr(
            f"{multi}.input[2]", 20.0, 30.0, 40.0, type="double3"
        )
        maya_cmds.setAttr(f"{multi}.input[9]", 3.0, 5.0, 7.0, type="double3")
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (16.0, 23.0, 30.0)
        )

        maya_cmds.setAttr(f"{multi}.input[9].inputY", 10.0)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (16.0, 18.0, 30.0)
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
            "bdDouble3Sub",
            (
                "input1X",
                "input1Y",
                "input1Z",
                "input2X",
                "input2Y",
                "input2Z",
            ),
        ),
        ("bdDouble3SubMulti", ("inputX", "inputY", "inputZ")),
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

    from bd_util.maya.node.operator.node.dg.bd_double3_sub import BdDouble3Sub
    from bd_util.maya.node.operator.node.dg.bd_double3_sub_multi import (
        BdDouble3SubMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Sub(name="fixed")
    multi = nodes.create.bdDouble3SubMulti(name="multi")
    fixed.input1.set((10.0, 20.0, 30.0))
    fixed.input2.set((1.0, 5.0, 7.0))
    fixed.output.connect(multi.input[2])
    multi.input[7].set((1.0, 2.0, 3.0))
    modifier_manager.do_it_dg()

    assert multi.output.get().as_tuple() == pytest.approx((8.0, 13.0, 20.0))
    assert isinstance(nodes.existing.bdDouble3Sub(fixed.name), BdDouble3Sub)
    assert isinstance(
        nodes.existing.bdDouble3SubMulti(multi.name),
        BdDouble3SubMulti,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Sub(name="fixed")
    multi = nodes.create.bdDouble3SubMulti(name="multi")
    fixed.input1.set((10.0, 20.0, 30.0))
    fixed.input2.set((1.0, 5.0, 7.0))
    multi.input[20].set((1.0, 2.0, 3.0))
    multi.input[2].set((20.0, 30.0, 40.0))
    multi.input[9].set((3.0, 5.0, 7.0))
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0007F00A
    assert multi_fn.typeId.id() == 0x0007F009

    scene_path = tmp_path / "bd_double3_sub.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert existing_nodes.existing.bdDouble3Sub(
        "fixed"
    ).output.get().as_tuple() == pytest.approx((9.0, 15.0, 23.0))
    assert existing_nodes.existing.bdDouble3SubMulti(
        "multi"
    ).output.get().as_tuple() == pytest.approx((16.0, 23.0, 30.0))
