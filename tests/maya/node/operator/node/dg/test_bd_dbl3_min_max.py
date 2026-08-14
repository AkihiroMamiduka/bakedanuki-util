# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


OPERATIONS = (
    ("Min", min, 0x0014269B, 0x0014269A),
    ("Max", max, 0x0014269F, 0x0014269E),
)


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


def _component_wise(function, *values):
    return tuple(function(components) for components in zip(*values))


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl3_max import BdDbl3Max
    from bd_util.maya.node.operator.node.dg.bd_dbl3_max_multi import (
        BdDbl3MaxMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl3_min import BdDbl3Min
    from bd_util.maya.node.operator.node.dg.bd_dbl3_min_multi import (
        BdDbl3MinMulti,
    )

    for node_cls, node_type in (
        (BdDbl3Min, "bdDbl3_Min"),
        (BdDbl3Max, "bdDbl3_Max"),
    ):
        assert node_cls.NODE_TYPE == node_type
        assert node_cls.input1.long_name == "input1"
        assert node_cls.i1x.short_name == "i1x"
        assert node_cls.input2.long_name == "input2"
        assert node_cls.i2z.short_name == "i2z"
        assert node_cls.output.long_name == "output"
        assert node_cls.oz.short_name == "oz"

    for node_cls, node_type in (
        (BdDbl3MinMulti, "bdDbl3_MinMulti"),
        (BdDbl3MaxMulti, "bdDbl3_MaxMulti"),
    ):
        assert node_cls.NODE_TYPE == node_type
        assert node_cls.input.long_name == "input"
        assert node_cls.i.short_name == "i"
        assert node_cls.output.long_name == "output"
        assert node_cls.oz.short_name == "oz"


@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_defaults_and_type_ids(
    modifier_manager,
    maya_cmds,
    maya_om,
    operation,
    function,
    fixed_type_id,
    multi_type_id,
):
    del function
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = getattr(nodes.create, f"bdDbl3_{operation}")()
    multi = getattr(nodes.create, f"bdDbl3_{operation}Multi")()
    modifier_manager.do_it_dg()

    zero = (0.0, 0.0, 0.0)
    assert fixed.input1.get().as_tuple() == pytest.approx(zero)
    assert fixed.input2.get().as_tuple() == pytest.approx(zero)
    assert fixed.output.get().as_tuple() == pytest.approx(zero)
    assert multi.output.get().as_tuple() == pytest.approx(zero)

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == fixed_type_id
    assert multi_fn.typeId.id() == multi_type_id


@pytest.mark.parametrize(
    ("operation", "values", "expected"),
    (
        (
            "Min",
            ((5.0, 10.0, 7.0), (10.0, 6.0, 12.0)),
            (5.0, 6.0, 7.0),
        ),
        (
            "Max",
            ((-5.0, -10.0, -7.0), (-10.0, -6.0, -12.0)),
            (-5.0, -6.0, -7.0),
        ),
    ),
)
def test_fixed_and_multi_do_not_include_zero_in_non_empty_comparison(
    modifier_manager,
    maya_cmds,
    operation,
    values,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = getattr(nodes.create, f"bdDbl3_{operation}")()
    multi = getattr(nodes.create, f"bdDbl3_{operation}Multi")()
    fixed.input1.set(values[0])
    fixed.input2.set(values[1])
    modifier_manager.do_it_dg()

    assert fixed.output.get().as_tuple() == pytest.approx(expected)
    assert multi.output.get().as_tuple() == pytest.approx((0.0, 0.0, 0.0))

    multi.input[2].set_direct(values[0])
    multi.input[9].set_direct(values[1])
    assert multi.output.get().as_tuple() == pytest.approx(expected)


@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_multi_handles_sparse_elements_and_removal(
    modifier_manager,
    maya_cmds,
    operation,
    function,
    fixed_type_id,
    multi_type_id,
):
    del fixed_type_id, multi_type_id
    _load_bd_util_nodes(maya_cmds)

    values = (
        (2.0, 8.0, -1.0),
        (-3.0, 5.0, 9.0),
        (0.5, 7.0, 3.0),
    )
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = getattr(nodes.create, f"bdDbl3_{operation}Multi")()
    node.input[2].set(values[0])
    node.input[9].set(values[1])
    node.input[20].set(values[2])
    modifier_manager.do_it_dg()

    assert node.output.get().as_tuple() == pytest.approx(
        _component_wise(function, *values)
    )

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get().as_tuple() == pytest.approx(
        _component_wise(function, values[0], values[2])
    )

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get().as_tuple() == pytest.approx(values[2])


@pytest.mark.parametrize("operation", ("Min", "Max"))
def test_nan_propagates_per_component(maya_cmds, operation):
    _load_bd_util_nodes(maya_cmds)

    fixed = maya_cmds.createNode(f"bdDbl3_{operation}")
    maya_cmds.setAttr(
        f"{fixed}.input1",
        1.0,
        2.0,
        float("nan"),
        type="double3",
    )
    maya_cmds.setAttr(
        f"{fixed}.input2",
        2.0,
        1.0,
        3.0,
        type="double3",
    )
    output = maya_cmds.getAttr(f"{fixed}.output")[0]
    assert output[:2] == pytest.approx(
        (1.0, 1.0) if operation == "Min" else (2.0, 2.0)
    )
    assert math.isnan(output[2])

    multi = maya_cmds.createNode(f"bdDbl3_{operation}Multi")
    maya_cmds.setAttr(
        f"{multi}.input[2]",
        1.0,
        2.0,
        3.0,
        type="double3",
    )
    maya_cmds.setAttr(f"{multi}.input[9].inputY", float("nan"))
    multi_output = maya_cmds.getAttr(f"{multi}.output")[0]
    assert math.isnan(multi_output[1])


@pytest.mark.parametrize(
    ("operation", "expected"),
    (
        ("Min", (3.0, float("-inf"), float("-inf"))),
        ("Max", (float("inf"), 3.0, float("inf"))),
    ),
)
def test_infinity_uses_component_wise_normal_ordering(
    maya_cmds,
    operation,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(f"bdDbl3_{operation}")
    maya_cmds.setAttr(
        f"{node}.input1", 3.0, 3.0, float("-inf"), type="double3"
    )
    maya_cmds.setAttr(
        f"{node}.input2",
        float("inf"),
        float("-inf"),
        float("inf"),
        type="double3",
    )
    assert maya_cmds.getAttr(f"{node}.output")[0] == expected


@pytest.mark.parametrize(
    ("operation", "expected_sign"),
    (("Min", -1.0), ("Max", 1.0)),
)
def test_signed_zero_is_selected_per_component(
    maya_cmds,
    operation,
    expected_sign,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(f"bdDbl3_{operation}")
    maya_cmds.setAttr(f"{node}.input1", 0.0, 1.0, 2.0, type="double3")
    maya_cmds.setAttr(f"{node}.input2", -0.0, 2.0, 1.0, type="double3")
    output_x = maya_cmds.getAttr(f"{node}.outputX")
    assert output_x == 0.0
    assert math.copysign(1.0, output_x) == expected_sign


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_child_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
    operation,
    function,
    fixed_type_id,
    multi_type_id,
):
    del fixed_type_id, multi_type_id
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)

        fixed = maya_cmds.createNode(f"bdDbl3_{operation}")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{fixed}.input2", 5.0, 1.0, 7.0, type="double3")
        assert maya_cmds.getAttr(f"{fixed}.output")[0] == pytest.approx(
            _component_wise(function, (2.0, 3.0, 4.0), (5.0, 1.0, 7.0))
        )

        maya_cmds.setAttr(f"{fixed}.input1X", 8.0)
        assert maya_cmds.getAttr(f"{fixed}.outputX") == pytest.approx(
            function(8.0, 5.0)
        )

        multi = maya_cmds.createNode(f"bdDbl3_{operation}Multi")
        maya_cmds.setAttr(f"{multi}.input[2]", 2.0, 3.0, 4.0, type="double3")
        maya_cmds.setAttr(f"{multi}.input[9]", 5.0, 1.0, 7.0, type="double3")
        maya_cmds.setAttr(f"{multi}.input[2].inputY", 10.0)
        assert maya_cmds.getAttr(f"{multi}.outputY") == pytest.approx(
            function(10.0, 1.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


@pytest.mark.parametrize("operation", ("Min", "Max"))
def test_child_dependencies_cover_output_compound(
    maya_cmds, maya_om, operation
):
    _load_bd_util_nodes(maya_cmds)

    for node_type, input_children in (
        (f"bdDbl3_{operation}", ("input1X", "input1Y", "input1Z")),
        (f"bdDbl3_{operation}Multi", ("inputX", "inputY", "inputZ")),
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


@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_connections_existing_accessors_and_scene_round_trip(
    modifier_manager,
    maya_cmds,
    tmp_path,
    operation,
    function,
    fixed_type_id,
    multi_type_id,
):
    del fixed_type_id, multi_type_id
    _load_bd_util_nodes(maya_cmds)

    input1 = (2.0, 3.0, 4.0)
    input2 = (5.0, 1.0, 7.0)
    extra = (0.5, 2.0, -1.0)
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = getattr(nodes.create, f"bdDbl3_{operation}")(name="fixed")
    multi = getattr(nodes.create, f"bdDbl3_{operation}Multi")(name="multi")
    fixed.input1.set(input1)
    fixed.input2.set(input2)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(extra)
    modifier_manager.do_it_dg()

    expected = _component_wise(
        function,
        _component_wise(function, input1, input2),
        extra,
    )
    assert multi.output.get().as_tuple() == pytest.approx(expected)

    existing_fixed = getattr(nodes.existing, f"bdDbl3_{operation}")(fixed.name)
    existing_multi = getattr(nodes.existing, f"bdDbl3_{operation}Multi")(
        multi.name
    )
    assert type(existing_fixed) is type(fixed)
    assert type(existing_multi) is type(multi)

    scene_path = tmp_path / f"bd_dbl3_{operation.lower()}.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    reloaded_multi = getattr(
        reloaded.existing,
        f"bdDbl3_{operation}Multi",
    )("multi")
    assert reloaded_multi.output.get().as_tuple() == pytest.approx(expected)
