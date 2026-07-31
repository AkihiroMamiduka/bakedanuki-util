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

    from bd_util.maya.node.operator.node.dg.bd_double3_mult import (
        BdDouble3Mult,
    )

    assert BdDouble3Mult.NODE_TYPE == "bdDouble3Mult"
    assert BdDouble3Mult.input1.long_name == "input1"
    assert BdDouble3Mult.i1.short_name == "i1"
    assert BdDouble3Mult.input1X.long_name == "input1X"
    assert BdDouble3Mult.i1x.short_name == "i1x"
    assert BdDouble3Mult.input2.long_name == "input2"
    assert BdDouble3Mult.i2.short_name == "i2"
    assert BdDouble3Mult.input2Z.long_name == "input2Z"
    assert BdDouble3Mult.i2z.short_name == "i2z"
    assert BdDouble3Mult.output.long_name == "output"
    assert BdDouble3Mult.oz.short_name == "oz"


def test_multi_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_double3_mult_multi import (
        BdDouble3MultMulti,
    )

    assert BdDouble3MultMulti.NODE_TYPE == "bdDouble3MultMulti"
    assert BdDouble3MultMulti.input.long_name == "input"
    assert BdDouble3MultMulti.i.short_name == "i"
    assert BdDouble3MultMulti.output.long_name == "output"
    assert BdDouble3MultMulti.oz.short_name == "oz"


def test_default_names_have_unambiguous_maya_indices(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Mult()
    multi = nodes.create.bdDouble3MultMulti()
    modifier_manager.do_it_dg()

    assert fixed.name == "bdDouble3Mult1"
    assert multi.name == "bdDouble3MultMulti1"


def test_fixed_defaults_return_multiplicative_identity(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult(name="mult")
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_fixed_multiplies_two_inputs_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult(name="mult")
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
    node = nodes.create.bdDouble3Mult(name="mult")
    node.input1.input1X.set(2.0)
    node.input1.i1y.set(3.0)
    node.input1.input1Z.set(4.0)
    node.input2.i2x.set(5.0)
    node.input2.input2Y.set(6.0)
    node.input2.i2z.set(7.0)
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((10.0, 18.0, 28.0))


def test_multi_empty_input_returns_multiplicative_identity(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3MultMulti(name="mult")
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_multi_multiplies_existing_sparse_elements_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3MultMulti(name="mult")
    node.input[0].set((2.0, 3.0, 4.0))
    node.input[3].set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input[0].inputX.get() == pytest.approx(2.0)
    assert node.input[3].iz.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((-1.0, 30.0, 8.0))


def test_fixed_output_participates_in_multi_product(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Mult(name="fixed")
    multi = nodes.create.bdDouble3MultMulti(name="multi")

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

    from bd_util.maya.node.operator.node.dg.bd_double3_mult import (
        BdDouble3Mult,
    )
    from bd_util.maya.node.operator.node.dg.bd_double3_mult_multi import (
        BdDouble3MultMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Mult(name="fixed")
    multi = nodes.create.bdDouble3MultMulti(name="multi")
    modifier_manager.do_it_dg()

    existing_fixed = nodes.existing.bdDouble3Mult(fixed.name)
    existing_multi = nodes.existing.bdDouble3MultMulti(multi.name)
    assert isinstance(existing_fixed, BdDouble3Mult)
    assert isinstance(existing_multi, BdDouble3MultMulti)


def test_both_nodes_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDouble3Mult(name="fixed")
    multi = nodes.create.bdDouble3MultMulti(name="multi")
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
    assert fixed_fn.typeId.id() == 0x0007F002
    assert multi_fn.typeId.id() == 0x0007F001

    scene_path = tmp_path / "bd_double3_mult.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    existing_fixed = existing_nodes.existing.bdDouble3Mult("fixed")
    existing_multi = existing_nodes.existing.bdDouble3MultMulti("multi")
    expected = (10.0, 18.0, 28.0)
    assert existing_fixed.output.get().as_tuple() == pytest.approx(expected)
    assert existing_multi.output.get().as_tuple() == pytest.approx(expected)
