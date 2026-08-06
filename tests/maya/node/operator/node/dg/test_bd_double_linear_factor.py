# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


NODE_TYPE_IDS = {
    "bdDblL_Multiply": 0x0007F05F,
    "bdDblL_MultiplyMulti": 0x0007F060,
    "bdDblL3_Multiply": 0x0007F061,
    "bdDblL3_MultiplyMulti": 0x0007F062,
    "bdDblL_Divide": 0x0007F063,
    "bdDblL_DivideMulti": 0x0007F064,
    "bdDblL3_Divide": 0x0007F065,
    "bdDblL3_DivideMulti": 0x0007F066,
}


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


def _set_value(maya_cmds, plug: str, value) -> None:
    if isinstance(value, tuple):
        maya_cmds.setAttr(plug, *value, type="double3")
        return
    maya_cmds.setAttr(plug, value)


def _get_value(maya_cmds, plug: str, is_compound: bool):
    value = maya_cmds.getAttr(plug)
    return value[0] if is_compound else value


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_node_types_ids_and_attribute_contracts(
    maya_cmds,
    maya_om,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == NODE_TYPE_IDS[node_type]
    is_compound = node_type.startswith("bdDblL3_")
    is_multi = node_type.endswith("Multi")
    factor_plug = "factor[0]" if is_multi else "factor"

    if is_compound:
        assert maya_cmds.getAttr(f"{node}.input", type=True) == "double3"
        assert (
            maya_cmds.getAttr(f"{node}.{factor_plug}", type=True) == "double3"
        )
        assert maya_cmds.getAttr(f"{node}.output", type=True) == "double3"
        for axis in "XYZ":
            assert (
                maya_cmds.getAttr(f"{node}.input{axis}", type=True)
                == "doubleLinear"
            )
            factor_child = (
                f"{factor_plug}.factor{axis}" if is_multi else f"factor{axis}"
            )
            assert (
                maya_cmds.getAttr(f"{node}.{factor_child}", type=True)
                == "double"
            )
            assert (
                maya_cmds.getAttr(f"{node}.output{axis}", type=True)
                == "doubleLinear"
            )
    else:
        assert maya_cmds.getAttr(f"{node}.input", type=True) == (
            "doubleLinear"
        )
        assert (
            maya_cmds.getAttr(f"{node}.{factor_plug}", type=True) == "double"
        )
        assert maya_cmds.getAttr(f"{node}.output", type=True) == (
            "doubleLinear"
        )

    assert maya_cmds.attributeQuery("factor", node=node, multi=True) is (
        is_multi
    )


@pytest.mark.parametrize("node_type", sorted(NODE_TYPE_IDS))
def test_defaults_are_zero_input_unit_factor_and_zero_output(
    maya_cmds,
    node_type,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    is_compound = node_type.startswith("bdDblL3_")
    is_multi = node_type.endswith("Multi")
    zero = (0.0, 0.0, 0.0) if is_compound else 0.0

    assert _get_value(maya_cmds, f"{node}.input", is_compound) == (
        pytest.approx(zero)
    )
    assert _get_value(maya_cmds, f"{node}.output", is_compound) == (
        pytest.approx(zero)
    )

    if is_multi:
        assert maya_cmds.getAttr(f"{node}.factor", multiIndices=True) in (
            None,
            [],
        )
    else:
        identity = (1.0, 1.0, 1.0) if is_compound else 1.0
        assert _get_value(maya_cmds, f"{node}.factor", is_compound) == (
            pytest.approx(identity)
        )


@pytest.mark.parametrize(
    ("node_type", "input_value", "factor", "expected"),
    (
        ("bdDblL_Multiply", -2.5, 4.0, -10.0),
        ("bdDblL_Divide", 24.0, 4.0, 6.0),
        (
            "bdDblL3_Multiply",
            (2.0, 3.0, 4.0),
            (-0.5, 10.0, 2.0),
            (-1.0, 30.0, 8.0),
        ),
        (
            "bdDblL3_Divide",
            (12.0, 20.0, 30.0),
            (3.0, 4.0, 5.0),
            (4.0, 5.0, 6.0),
        ),
    ),
)
def test_fixed_nodes_apply_factor_component_wise(
    maya_cmds,
    node_type,
    input_value,
    factor,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    _set_value(maya_cmds, f"{node}.input", input_value)
    _set_value(maya_cmds, f"{node}.factor", factor)

    assert _get_value(
        maya_cmds,
        f"{node}.output",
        isinstance(expected, tuple),
    ) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("node_type", "input_value", "factors", "expected", "after_remove"),
    (
        (
            "bdDblL_MultiplyMulti",
            2.0,
            ((20, 0.5), (2, -3.0), (9, 4.0)),
            -12.0,
            -3.0,
        ),
        (
            "bdDblL_DivideMulti",
            120.0,
            ((20, 2.0), (2, 3.0), (9, 5.0)),
            4.0,
            20.0,
        ),
        (
            "bdDblL3_MultiplyMulti",
            (2.0, 3.0, 4.0),
            (
                (20, (0.5, 2.0, -1.0)),
                (2, (5.0, 6.0, 7.0)),
                (9, (2.0, 0.5, 1.0)),
            ),
            (10.0, 18.0, -28.0),
            (5.0, 36.0, -28.0),
        ),
        (
            "bdDblL3_DivideMulti",
            (120.0, 240.0, 600.0),
            (
                (20, (2.0, 4.0, 5.0)),
                (2, (3.0, 5.0, 10.0)),
                (9, (2.0, 2.0, 2.0)),
            ),
            (10.0, 6.0, 6.0),
            (20.0, 12.0, 12.0),
        ),
    ),
)
def test_multi_nodes_fold_sparse_factors_and_update_after_removal(
    maya_cmds,
    node_type,
    input_value,
    factors,
    expected,
    after_remove,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    _set_value(maya_cmds, f"{node}.input", input_value)
    for logical_index, factor in factors:
        _set_value(maya_cmds, f"{node}.factor[{logical_index}]", factor)

    is_compound = isinstance(expected, tuple)
    assert _get_value(
        maya_cmds, f"{node}.output", is_compound
    ) == pytest.approx(expected)

    maya_cmds.removeMultiInstance(f"{node}.factor[9]", b=True)
    assert _get_value(
        maya_cmds, f"{node}.output", is_compound
    ) == pytest.approx(after_remove)

    for logical_index, _ in factors:
        if logical_index != 9:
            maya_cmds.removeMultiInstance(
                f"{node}.factor[{logical_index}]", b=True
            )
    assert _get_value(
        maya_cmds, f"{node}.output", is_compound
    ) == pytest.approx(input_value)


@pytest.mark.parametrize(
    ("node_type", "input_value", "factor", "expected"),
    (
        ("bdDblL_Divide", 1.0, 0.0, 1.0e9),
        ("bdDblL_Divide", 1.0, -5.0e-10, -1.0e9),
        (
            "bdDblL3_Divide",
            (1.0, 2.0, 3.0),
            (0.0, 5.0e-10, -5.0e-10),
            (1.0e9, 2.0e9, -3.0e9),
        ),
    ),
)
def test_divide_clamps_small_factors_with_sign(
    maya_cmds,
    node_type,
    input_value,
    factor,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    _set_value(maya_cmds, f"{node}.input", input_value)
    _set_value(maya_cmds, f"{node}.factor", factor)
    assert _get_value(
        maya_cmds,
        f"{node}.output",
        isinstance(expected, tuple),
    ) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("node_type", "factor"),
    (
        ("bdDblL_DivideMulti", 0.0),
        ("bdDblL3_DivideMulti", (0.0, 5.0e-10, -5.0e-10)),
    ),
)
def test_divide_multi_clamps_each_factor(maya_cmds, node_type, factor):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    is_compound = isinstance(factor, tuple)
    input_value = (1.0, 2.0, 3.0) if is_compound else 1.0
    expected = (1.0e9, 2.0e9, -3.0e9) if is_compound else 1.0e9
    _set_value(maya_cmds, f"{node}.input", input_value)
    _set_value(maya_cmds, f"{node}.factor[4]", factor)

    assert _get_value(
        maya_cmds, f"{node}.output", is_compound
    ) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("node_type", "operation"),
    (
        ("bdDblL3_Multiply", "multiply"),
        ("bdDblL3_Divide", "divide"),
        ("bdDblL3_MultiplyMulti", "multiply"),
        ("bdDblL3_DivideMulti", "divide"),
    ),
)
@pytest.mark.parametrize(
    ("output_child", "axis", "expected_multiply", "expected_divide"),
    (
        ("outputX", 0, 10.0, 0.4),
        ("outputY", 1, 18.0, 0.5),
        ("outputZ", 2, 28.0, 4.0 / 7.0),
    ),
)
def test_compound_output_children_can_be_requested_directly(
    maya_cmds,
    node_type,
    operation,
    output_child,
    axis,
    expected_multiply,
    expected_divide,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(node_type)
    _set_value(maya_cmds, f"{node}.input", (2.0, 3.0, 4.0))
    factor_plug = "factor[3]" if node_type.endswith("Multi") else "factor"
    _set_value(maya_cmds, f"{node}.{factor_plug}", (5.0, 6.0, 7.0))
    expected = (
        expected_multiply if operation == "multiply" else expected_divide
    )

    assert maya_cmds.getAttr(f"{node}.{output_child}") == pytest.approx(
        expected
    )
    assert _get_value(maya_cmds, f"{node}.output", True)[axis] == (
        pytest.approx(expected)
    )


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_parent_child_and_sparse_dirty_updates_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdDblL3_DivideMulti")
        _set_value(maya_cmds, f"{node}.input", (120.0, 240.0, 600.0))
        _set_value(maya_cmds, f"{node}.factor[2]", (3.0, 5.0, 10.0))
        _set_value(maya_cmds, f"{node}.factor[9]", (2.0, 4.0, 5.0))
        assert _get_value(maya_cmds, f"{node}.output", True) == (
            pytest.approx((20.0, 12.0, 12.0))
        )

        maya_cmds.setAttr(f"{node}.factor[2].factorY", 0.0)
        assert maya_cmds.getAttr(f"{node}.outputY") == pytest.approx(6.0e10)

        maya_cmds.setAttr(f"{node}.inputZ", 300.0)
        assert maya_cmds.getAttr(f"{node}.outputZ") == pytest.approx(6.0)

        maya_cmds.removeMultiInstance(f"{node}.factor[9]", b=True)
        assert _get_value(maya_cmds, f"{node}.output", True) == (
            pytest.approx((40.0, 2.4e11, 30.0))
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_translate_and_scale_connect_without_unit_conversion(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    scalar_source = maya_cmds.createNode("transform")
    scalar_target = maya_cmds.createNode("transform")
    scalar = maya_cmds.createNode("bdDblL_Multiply")
    maya_cmds.setAttr(f"{scalar_source}.translateX", 3.0)
    maya_cmds.setAttr(f"{scalar_source}.scaleX", 4.0)
    maya_cmds.connectAttr(f"{scalar_source}.translateX", f"{scalar}.input")
    maya_cmds.connectAttr(f"{scalar_source}.scaleX", f"{scalar}.factor")
    maya_cmds.connectAttr(f"{scalar}.output", f"{scalar_target}.translateX")
    assert maya_cmds.getAttr(f"{scalar_target}.translateX") == (
        pytest.approx(12.0)
    )

    compound_source = maya_cmds.createNode("transform")
    compound_target = maya_cmds.createNode("transform")
    compound = maya_cmds.createNode("bdDblL3_Divide")
    _set_value(maya_cmds, f"{compound_source}.translate", (12.0, 20.0, 30.0))
    _set_value(maya_cmds, f"{compound_source}.scale", (3.0, 4.0, 5.0))
    maya_cmds.connectAttr(f"{compound_source}.translate", f"{compound}.input")
    maya_cmds.connectAttr(f"{compound_source}.scale", f"{compound}.factor")
    maya_cmds.connectAttr(f"{compound}.output", f"{compound_target}.translate")
    assert _get_value(
        maya_cmds, f"{compound_target}.translate", True
    ) == pytest.approx((4.0, 5.0, 6.0))

    assert not maya_cmds.ls(type="unitConversion")


def test_linear_display_unit_preserves_internal_distance(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="cm")
        node = maya_cmds.createNode("bdDblL3_Multiply")
        _set_value(maya_cmds, f"{node}.input", (2.0, 3.0, 4.0))
        _set_value(maya_cmds, f"{node}.factor", (5.0, 6.0, 7.0))
        assert _get_value(maya_cmds, f"{node}.output", True) == (
            pytest.approx((10.0, 18.0, 28.0))
        )

        maya_cmds.currentUnit(linear="m")
        assert _get_value(maya_cmds, f"{node}.output", True) == (
            pytest.approx((0.1, 0.18, 0.28))
        )

        selection = maya_om.MSelectionList()
        selection.add(f"{node}.outputZ")
        assert selection.getPlug(0).asMDistance().asCentimeters() == (
            pytest.approx(28.0)
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_node_operator_creation_and_existing_accessors(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_l3_divide_multi import (
        BdDblL3DivideMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_l_multiply import (
        BdDblLMultiply,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = nodes.create.bdDblL_Multiply(name="fixed")
    multi = nodes.create.bdDblL3_DivideMulti(name="multi")
    fixed.input.set(3.0)
    fixed.factor.set(4.0)
    multi.input.set((120.0, 240.0, 600.0))
    multi.factor[2].set((3.0, 5.0, 10.0))
    multi.factor[9].set((2.0, 4.0, 5.0))
    modifier_manager.do_it_dg()

    assert isinstance(fixed, BdDblLMultiply)
    assert isinstance(multi, BdDblL3DivideMulti)
    assert fixed.output.get() == pytest.approx(12.0)
    assert multi.factor[2].factorX.get() == pytest.approx(3.0)
    assert multi.output.get().as_tuple() == pytest.approx((20.0, 12.0, 12.0))
    assert isinstance(nodes.existing.bdDblL_Multiply("fixed"), BdDblLMultiply)
    assert isinstance(
        nodes.existing.bdDblL3_DivideMulti("multi"),
        BdDblL3DivideMulti,
    )


def test_factor_nodes_survive_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    scalar = nodes.create.bdDblL_Divide(name="scalar")
    compound = nodes.create.bdDblL3_MultiplyMulti(name="compound")
    scalar.input.set(24.0)
    scalar.factor.set(4.0)
    compound.input.set((2.0, 3.0, 4.0))
    compound.factor[2].set((5.0, 6.0, 7.0))
    compound.factor[9].set((0.5, 2.0, -1.0))
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_double_linear_factor.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    assert reloaded.existing.bdDblL_Divide(
        "scalar"
    ).output.get() == pytest.approx(6.0)
    assert reloaded.existing.bdDblL3_MultiplyMulti(
        "compound"
    ).output.get().as_tuple() == pytest.approx((5.0, 36.0, -28.0))
