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


def test_fixed_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply import (
        BdDbl3Multiply,
    )

    assert BdDbl3Multiply.NODE_TYPE == "bdDbl3_Multiply"
    assert BdDbl3Multiply.input1.long_name == "input1"
    assert BdDbl3Multiply.i1.short_name == "i1"
    assert BdDbl3Multiply.input1X.long_name == "input1X"
    assert BdDbl3Multiply.i1x.short_name == "i1x"
    assert BdDbl3Multiply.input2.long_name == "input2"
    assert BdDbl3Multiply.i2.short_name == "i2"
    assert BdDbl3Multiply.input2Z.long_name == "input2Z"
    assert BdDbl3Multiply.i2z.short_name == "i2z"
    assert BdDbl3Multiply.output.long_name == "output"
    assert BdDbl3Multiply.oz.short_name == "oz"


def test_multi_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply_multi import (
        BdDbl3MultiplyMulti,
    )

    assert BdDbl3MultiplyMulti.NODE_TYPE == "bdDbl3_MultiplyMulti"
    assert BdDbl3MultiplyMulti.input.long_name == "input"
    assert BdDbl3MultiplyMulti.i.short_name == "i"
    assert BdDbl3MultiplyMulti.output.long_name == "output"
    assert BdDbl3MultiplyMulti.oz.short_name == "oz"


def test_default_names_have_unambiguous_maya_indices(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Multiply()
    multi = nodes.create.bdDbl3_MultiplyMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDbl3_Multiply1"
    assert multi.name == "bdDbl3_MultiplyMulti1"


def test_fixed_defaults_return_multiplicative_identity(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Multiply(name="mult")
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_fixed_multiplies_two_inputs_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Multiply(name="mult")
    node.input1.set((2.0, 3.0, 4.0))
    node.input2.set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input1.input1X.get() == pytest.approx(2.0)
    assert node.input2.i2z.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((-1.0, 30.0, 8.0))


def test_fixed_child_inputs_dirty_and_update_output(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_Multiply(name="mult")
    node.input1.input1X.set(2.0)
    node.input1.i1y.set(3.0)
    node.input1.input1Z.set(4.0)
    node.input2.i2x.set(5.0)
    node.input2.input2Y.set(6.0)
    node.input2.i2z.set(7.0)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((10.0, 18.0, 28.0))


@pytest.mark.parametrize(
    ("node_type", "input_values"),
    [
        (
            "bdDbl3_Multiply",
            (
                ("input1", (2.0, 3.0, 4.0)),
                ("input2", (5.0, 6.0, 7.0)),
            ),
        ),
        (
            "bdDbl3_MultiplyMulti",
            (
                ("input[2]", (2.0, 3.0, 4.0)),
                ("input[7]", (5.0, 6.0, 7.0)),
            ),
        ),
    ],
)
@pytest.mark.parametrize(
    ("output_child", "expected"),
    [
        ("outputX", 10.0),
        ("outputY", 18.0),
        ("outputZ", 28.0),
    ],
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
        maya_cmds.setAttr(
            f"{node}.{input_name}",
            *value,
            type="double3",
        )

    assert maya_cmds.getAttr(f"{node}.{output_child}") == pytest.approx(
        expected
    )


def test_multi_empty_input_returns_multiplicative_identity(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_MultiplyMulti(name="mult")
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_multi_multiplies_existing_sparse_elements_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDbl3_MultiplyMulti(name="mult")
    node.input[0].set((2.0, 3.0, 4.0))
    node.input[3].set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input[0].inputX.get() == pytest.approx(2.0)
    assert node.input[3].iz.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((-1.0, 30.0, 8.0))


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode("bdDbl3_Multiply")
        maya_cmds.setAttr(
            f"{fixed}.input1",
            2.0,
            3.0,
            4.0,
            type="double3",
        )
        maya_cmds.setAttr(
            f"{fixed}.input2",
            5.0,
            6.0,
            7.0,
            type="double3",
        )
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (10.0, 18.0, 28.0)
        )

        maya_cmds.setAttr(f"{fixed}.input1X", 8.0)
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            (40.0, 18.0, 28.0)
        )

        multi = maya_cmds.createNode("bdDbl3_MultiplyMulti")
        maya_cmds.setAttr(
            f"{multi}.input[2]",
            2.0,
            3.0,
            4.0,
            type="double3",
        )
        maya_cmds.setAttr(
            f"{multi}.input[9]",
            5.0,
            6.0,
            7.0,
            type="double3",
        )
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (10.0, 18.0, 28.0)
        )

        maya_cmds.setAttr(f"{multi}.input[2].inputY", 10.0)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (10.0, 60.0, 28.0)
        )

        maya_cmds.removeMultiInstance(f"{multi}.input[2]", b=True)
        assert maya_cmds.getAttr(f"{multi}.output")[0] == pytest.approx(
            (5.0, 6.0, 7.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_child_input_dependencies_cover_the_output_compound(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    for node_type, input_children in (
        ("bdDbl3_Multiply", ("input1X", "input1Y", "input1Z")),
        ("bdDbl3_MultiplyMulti", ("inputX", "inputY", "inputZ")),
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


def test_fixed_output_participates_in_multi_product(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Multiply(name="fixed")
    multi = nodes.create.bdDbl3_MultiplyMulti(name="multi")

    fixed.input1.set((2.0, 3.0, 4.0))
    fixed.input2.set((5.0, 6.0, 7.0))
    fixed.output.connect(multi.input[2])
    multi.input[7].set((0.5, 2.0, -1.0))
    modifier_manager.do_it_dg()

    assert multi.output.get().as_tuple() == pytest.approx((5.0, 36.0, -28.0))


def test_existing_node_accessors_return_specific_wrappers(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply import (
        BdDbl3Multiply,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_multiply_multi import (
        BdDbl3MultiplyMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Multiply(name="fixed")
    multi = nodes.create.bdDbl3_MultiplyMulti(name="multi")
    modifier_manager.do_it_dg()

    existing_fixed = nodes.existing.bdDbl3_Multiply(fixed.name)
    existing_multi = nodes.existing.bdDbl3_MultiplyMulti(multi.name)
    assert isinstance(existing_fixed, BdDbl3Multiply)
    assert isinstance(existing_multi, BdDbl3MultiplyMulti)


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDbl3_Multiply(name="fixed")
    multi = nodes.create.bdDbl3_MultiplyMulti(name="multi")
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
    assert fixed_fn.typeId.id() == 0x00142681
    assert multi_fn.typeId.id() == 0x00142680

    scene_path = tmp_path / "bd_dbl3_multiply.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    existing_fixed = existing_nodes.existing.bdDbl3_Multiply("fixed")
    existing_multi = existing_nodes.existing.bdDbl3_MultiplyMulti("multi")
    expected = (10.0, 18.0, 28.0)
    assert existing_fixed.output.get().as_tuple() == pytest.approx(expected)
    assert existing_multi.output.get().as_tuple() == pytest.approx(expected)
