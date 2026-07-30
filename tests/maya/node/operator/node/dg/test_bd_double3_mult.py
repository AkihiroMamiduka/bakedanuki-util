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

    from bd_util.maya.node.operator.node.dg.bd_double3_mult import (
        BdDouble3Mult,
    )

    assert BdDouble3Mult.NODE_TYPE == "bdDouble3Mult"
    assert BdDouble3Mult.input.long_name == "input"
    assert BdDouble3Mult.i.short_name == "i"
    assert BdDouble3Mult.output.long_name == "output"
    assert BdDouble3Mult.o.short_name == "o"
    assert BdDouble3Mult.outputZ.long_name == "outputZ"
    assert BdDouble3Mult.oz.short_name == "oz"


def test_default_name_has_an_unambiguous_maya_index(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult()
    modifier_manager.do_it_dg()

    assert node.name == "bdDouble3Mult1"


def test_empty_input_returns_multiplicative_identity(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult(name="mult")
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx((1.0, 1.0, 1.0))


def test_multiplies_existing_sparse_elements_component_wise(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult(name="mult")
    node.input[0].set((2.0, 3.0, 4.0))
    node.input[3].set((-0.5, 10.0, 2.0))
    modifier_manager.do_it_dg()

    assert node.input[0].inputX.get() == pytest.approx(2.0)
    assert node.input[3].iz.get() == pytest.approx(2.0)
    assert node.output.get().as_tuple() == pytest.approx((-1.0, 30.0, 8.0))


def test_connected_output_participates_in_downstream_product(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    source = nodes.create.bdDouble3Mult(name="source")
    target = nodes.create.bdDouble3Mult(name="target")

    source.input[0].set((2.0, 3.0, 4.0))
    source.output.connect(target.input[2])
    target.input[7].set((5.0, 6.0, 7.0))
    modifier_manager.do_it_dg()

    assert target.output.get().as_tuple() == pytest.approx((10.0, 18.0, 28.0))


def test_existing_node_accessor_returns_specific_wrapper(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_double3_mult import (
        BdDouble3Mult,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    created = nodes.create.bdDouble3Mult(name="mult")
    modifier_manager.do_it_dg()

    existing = nodes.existing.bdDouble3Mult(created.name)
    assert isinstance(existing, BdDouble3Mult)


def test_node_survives_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdDouble3Mult(name="mult")
    node.input[0].set((2.0, 3.0, 4.0))
    node.input[5].set((5.0, 6.0, 7.0))
    modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add(node.name)
    dependency_node = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert dependency_node.typeId.id() == 0x0007F001

    scene_path = tmp_path / "bd_double3_mult.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    existing = existing_nodes.existing.bdDouble3Mult("mult")
    assert existing.output.get().as_tuple() == pytest.approx(
        (10.0, 18.0, 28.0)
    )
