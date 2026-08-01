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

    from bd_util.maya.node.operator.node.dg.bd_add_double3_pair import (
        BdAddDouble3Pair,
    )
    from bd_util.maya.node.operator.node.dg.bd_add_double3_multi import (
        BdAddDouble3Multi,
    )

    assert BdAddDouble3Pair.NODE_TYPE == "bdAddDouble3Pair"
    assert BdAddDouble3Pair.input1.long_name == "input1"
    assert BdAddDouble3Pair.i1x.short_name == "i1x"
    assert BdAddDouble3Pair.input2.long_name == "input2"
    assert BdAddDouble3Pair.i2z.short_name == "i2z"
    assert BdAddDouble3Pair.output.long_name == "output"
    assert BdAddDouble3Pair.oz.short_name == "oz"

    assert BdAddDouble3Multi.NODE_TYPE == "bdAddDouble3Multi"
    assert BdAddDouble3Multi.input.long_name == "input"
    assert BdAddDouble3Multi.i.short_name == "i"
    assert BdAddDouble3Multi.output.long_name == "output"
    assert BdAddDouble3Multi.oz.short_name == "oz"


def test_defaults_return_additive_identity(modifier_manager, maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdAddDouble3Pair()
    multi = nodes.create.bdAddDouble3Multi()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdAddDouble3Pair1"
    assert multi.name == "bdAddDouble3Multi1"
    assert fixed.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))
    assert multi.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))


def test_fixed_adds_two_inputs_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdAddDouble3Pair(name="add")
    node.input1.set((2.0, 3.0, 4.0))
    node.input2.set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input1.input1X.get() == pytest.approx(2.0)
    assert node.input2.i2z.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((1.5, 13.0, 6.0))


@pytest.mark.parametrize(
    ("node_type", "input_values"),
    [
        (
            "bdAddDouble3Pair",
            (
                ("input1", (2.0, 3.0, 4.0)),
                ("input2", (5.0, 6.0, 7.0)),
            ),
        ),
        (
            "bdAddDouble3Multi",
            (
                ("input[2]", (2.0, 3.0, 4.0)),
                ("input[7]", (5.0, 6.0, 7.0)),
            ),
        ),
    ],
)
@pytest.mark.parametrize(
    ("output_child", "expected"),
    [("outputX", 7.0), ("outputY", 9.0), ("outputZ", 11.0)],
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


def test_multi_adds_sparse_elements_and_updates_after_removal(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdAddDouble3Multi(name="add")
    node.input[0].set((2.0, 3.0, 4.0))
    node.input[3].set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input[0].inputX.get() == pytest.approx(2.0)
    assert node.input[3].iz.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((1.5, 13.0, 6.0))

    maya_cmds.removeMultiInstance(f"{node.name}.input[0]", b=True)
    assert node.output.get().as_tuple() == pytest.approx((-0.5, 10.0, 2.0))


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdAddDouble3Pair")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{fixed}.input2", 5.0, 6.0, 7.0, type="double3")
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (7.0, 9.0, 11.0)
        )

        maya_cmds.setAttr(f"{fixed}.input1X", 8.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (13.0, 9.0, 11.0)
        )

        multi = maya_cmds.createNode("bdAddDouble3Multi")
        maya_cmds.setAttr(f"{multi}.input[2]", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{multi}.input[9]", 5.0, 6.0, 7.0, type="double3")
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (7.0, 9.0, 11.0)
        )

        maya_cmds.setAttr(f"{multi}.input[2].inputY", 10.0)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (7.0, 16.0, 11.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_child_input_dependencies_cover_the_output_compound(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    for node_type, input_children in (
        ("bdAddDouble3Pair", ("input1X", "input1Y", "input1Z")),
        ("bdAddDouble3Multi", ("inputX", "inputY", "inputZ")),
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


def test_fixed_output_participates_in_multi_sum(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdAddDouble3Pair(name="fixed")
    multi = nodes.create.bdAddDouble3Multi(name="multi")
    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((5.0, 6.0, 7.0))
    fixed.output.connect(multi.input[2])
    multi.input[7].set((0.5, 2.0, -1.0))
    modifier_manager.do_it_dg()

    assert multi.output.get().as_tuple() == pytest.approx((7.5, 11.0, 10.0))


def test_existing_node_accessors_return_specific_wrappers(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_add_double3_pair import (
        BdAddDouble3Pair,
    )
    from bd_util.maya.node.operator.node.dg.bd_add_double3_multi import (
        BdAddDouble3Multi,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdAddDouble3Pair(name="fixed")
    multi = nodes.create.bdAddDouble3Multi(name="multi")
    modifier_manager.do_it_dg()

    assert isinstance(
        nodes.existing.bdAddDouble3Pair(fixed.name), BdAddDouble3Pair
    )
    assert isinstance(
        nodes.existing.bdAddDouble3Multi(multi.name),
        BdAddDouble3Multi,
    )


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdAddDouble3Pair(name="fixed")
    multi = nodes.create.bdAddDouble3Multi(name="multi")
    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((5.0, 6.0, 7.0))
    multi.input[0].set((2.0, 3.0, 4.0))
    multi.input[5].set((5.0, 6.0, 7.0))
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == 0x0007F006
    assert multi_fn.typeId.id() == 0x0007F005

    scene_path = tmp_path / "bd_add_double3_pair.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    expected = (7.0, 9.0, 11.0)
    assert existing_nodes.existing.bdAddDouble3Pair(
        "fixed"
    ).output.get().as_tuple() == pytest.approx(expected)
    assert existing_nodes.existing.bdAddDouble3Multi(
        "multi"
    ).output.get().as_tuple() == pytest.approx(expected)
