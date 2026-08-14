# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


OPERATIONS = (
    ("Min", min, 0x0014269D, 0x0014269C),
    ("Max", max, 0x001426A1, 0x001426A0),
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


def test_class_attribute_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_dbl_max import BdDblMax
    from bd_util.maya.node.operator.node.dg.bd_dbl_max_multi import (
        BdDblMaxMulti,
    )
    from bd_util.maya.node.operator.node.dg.bd_dbl_min import BdDblMin
    from bd_util.maya.node.operator.node.dg.bd_dbl_min_multi import (
        BdDblMinMulti,
    )

    for node_cls, node_type in (
        (BdDblMin, "bdDbl_Min"),
        (BdDblMax, "bdDbl_Max"),
    ):
        assert node_cls.NODE_TYPE == node_type
        assert node_cls.input1.long_name == "input1"
        assert node_cls.i1.short_name == "i1"
        assert node_cls.input2.long_name == "input2"
        assert node_cls.i2.short_name == "i2"
        assert node_cls.output.long_name == "output"
        assert node_cls.o.short_name == "o"

    for node_cls, node_type in (
        (BdDblMinMulti, "bdDbl_MinMulti"),
        (BdDblMaxMulti, "bdDbl_MaxMulti"),
    ):
        assert node_cls.NODE_TYPE == node_type
        assert node_cls.input.long_name == "input"
        assert node_cls.i.short_name == "i"
        assert node_cls.output.long_name == "output"
        assert node_cls.o.short_name == "o"


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
    fixed = getattr(nodes.create, f"bdDbl_{operation}")()
    multi = getattr(nodes.create, f"bdDbl_{operation}Multi")()
    modifier_manager.do_it_dg()

    assert fixed.input1.get() == pytest.approx(0.0)
    assert fixed.input2.get() == pytest.approx(0.0)
    assert fixed.output.get() == pytest.approx(0.0)
    assert multi.output.get() == pytest.approx(0.0)

    selection = maya_om.MSelectionList()
    selection.add(fixed.name)
    selection.add(multi.name)
    fixed_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    multi_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert fixed_fn.typeId.id() == fixed_type_id
    assert multi_fn.typeId.id() == multi_type_id


@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_fixed_selects_extreme_value(
    modifier_manager,
    maya_cmds,
    operation,
    function,
    fixed_type_id,
    multi_type_id,
):
    del fixed_type_id, multi_type_id
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = getattr(nodes.create, f"bdDbl_{operation}")(name="extreme")
    node.input1.set(-2.5)
    node.input2.set(4.0)
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(function(-2.5, 4.0))


@pytest.mark.parametrize(
    ("operation", "values", "expected"),
    (
        ("Min", (5.0, 10.0), 5.0),
        ("Max", (-5.0, -10.0), -5.0),
    ),
)
def test_multi_empty_returns_zero_without_biasing_non_empty_values(
    modifier_manager,
    maya_cmds,
    operation,
    values,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = getattr(nodes.create, f"bdDbl_{operation}Multi")()
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node.name}.input[2]", values[0])
    maya_cmds.setAttr(f"{node.name}.input[9]", values[1])
    assert node.output.get() == pytest.approx(expected)


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

    values = (2.0, -3.0, 0.5)
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = getattr(nodes.create, f"bdDbl_{operation}Multi")()
    node.input[2].set(values[0])
    node.input[9].set(values[1])
    node.input[20].set(values[2])
    modifier_manager.do_it_dg()

    assert node.output.get() == pytest.approx(function(values))

    maya_cmds.removeMultiInstance(f"{node.name}.input[9]", b=True)
    assert node.output.get() == pytest.approx(function(values[0], values[2]))

    maya_cmds.removeMultiInstance(f"{node.name}.input[2]", b=True)
    assert node.output.get() == pytest.approx(values[2])


@pytest.mark.parametrize("operation", ("Min", "Max"))
def test_nan_propagates_from_fixed_and_multi_inputs(maya_cmds, operation):
    _load_bd_util_nodes(maya_cmds)

    fixed = maya_cmds.createNode(f"bdDbl_{operation}")
    maya_cmds.setAttr(f"{fixed}.input1", 2.0)
    maya_cmds.setAttr(f"{fixed}.input2", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{fixed}.output"))

    multi = maya_cmds.createNode(f"bdDbl_{operation}Multi")
    maya_cmds.setAttr(f"{multi}.input[2]", 2.0)
    maya_cmds.setAttr(f"{multi}.input[9]", float("nan"))
    assert math.isnan(maya_cmds.getAttr(f"{multi}.output"))


@pytest.mark.parametrize(
    ("operation", "input2", "expected"),
    (
        ("Min", float("inf"), 3.0),
        ("Min", float("-inf"), float("-inf")),
        ("Max", float("inf"), float("inf")),
        ("Max", float("-inf"), 3.0),
    ),
)
def test_infinity_uses_normal_ordering(
    maya_cmds,
    operation,
    input2,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(f"bdDbl_{operation}")
    maya_cmds.setAttr(f"{node}.input1", 3.0)
    maya_cmds.setAttr(f"{node}.input2", input2)
    assert maya_cmds.getAttr(f"{node}.output") == expected


@pytest.mark.parametrize(
    ("operation", "expected_sign"),
    (("Min", -1.0), ("Max", 1.0)),
)
def test_signed_zero_is_selected_deterministically(
    maya_cmds,
    operation,
    expected_sign,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode(f"bdDbl_{operation}")
    maya_cmds.setAttr(f"{node}.input1", 0.0)
    maya_cmds.setAttr(f"{node}.input2", -0.0)
    output = maya_cmds.getAttr(f"{node}.output")
    assert output == 0.0
    assert math.copysign(1.0, output) == expected_sign


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
@pytest.mark.parametrize(
    ("operation", "function", "fixed_type_id", "multi_type_id"),
    OPERATIONS,
)
def test_dirty_updates_match_in_all_evaluation_modes(
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

        fixed = maya_cmds.createNode(f"bdDbl_{operation}")
        maya_cmds.setAttr(f"{fixed}.input1", 2.0)
        maya_cmds.setAttr(f"{fixed}.input2", 5.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(
            function(2.0, 5.0)
        )

        maya_cmds.setAttr(f"{fixed}.input1", -4.0)
        assert maya_cmds.getAttr(f"{fixed}.output") == pytest.approx(
            function(-4.0, 5.0)
        )

        multi = maya_cmds.createNode(f"bdDbl_{operation}Multi")
        maya_cmds.setAttr(f"{multi}.input[2]", 3.0)
        maya_cmds.setAttr(f"{multi}.input[9]", 7.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(
            function(3.0, 7.0)
        )

        maya_cmds.setAttr(f"{multi}.input[2]", 10.0)
        assert maya_cmds.getAttr(f"{multi}.output") == pytest.approx(
            function(10.0, 7.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


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

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    fixed = getattr(nodes.create, f"bdDbl_{operation}")(name="fixed")
    multi = getattr(nodes.create, f"bdDbl_{operation}Multi")(name="multi")
    fixed.input1.set(2.0)
    fixed.input2.set(5.0)
    fixed.output.connect(multi.input[2])
    multi.input[7].set(-0.5)
    modifier_manager.do_it_dg()

    expected = function(function(2.0, 5.0), -0.5)
    assert multi.output.get() == pytest.approx(expected)

    existing_fixed = getattr(nodes.existing, f"bdDbl_{operation}")(fixed.name)
    existing_multi = getattr(nodes.existing, f"bdDbl_{operation}Multi")(
        multi.name
    )
    assert type(existing_fixed) is type(fixed)
    assert type(existing_multi) is type(multi)

    scene_path = tmp_path / f"bd_dbl_{operation.lower()}.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    reloaded = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    reloaded_multi = getattr(
        reloaded.existing,
        f"bdDbl_{operation}Multi",
    )("multi")
    assert reloaded_multi.output.get() == pytest.approx(expected)
