from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya

_AXIS_QUAT = (0.1, -0.2, 0.3, 0.9)


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
    maya_cmds.currentUnit(angle="degree")
    return plugin_path


def _get_angles(maya_cmds, plug: str) -> tuple[float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _normalized(value) -> tuple[float, float, float, float]:
    length = math.sqrt(sum(component * component for component in value))
    return tuple(component / length for component in value)


def _assert_same_rotation(actual, expected, tolerance=1.0e-9) -> None:
    actual = _normalized(actual)
    expected = _normalized(expected)
    dot = abs(sum(a * b for a, b in zip(actual, expected)))
    assert dot == pytest.approx(1.0, abs=tolerance)


def _create_quat_limit_network(
    maya_cmds,
    components=(100.0, 80.0, -50.0),
    order=0,
):
    source = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    limiter = maya_cmds.createNode("bdQuat_LimitBendTwist")
    maya_cmds.setAttr(f"{source}.input", *components, type="double3")
    maya_cmds.setAttr(f"{source}.axisQuat", *_AXIS_QUAT, type="double4")
    maya_cmds.setAttr(f"{source}.order", order)
    maya_cmds.setAttr(f"{limiter}.axisQuat", *_AXIS_QUAT, type="double4")
    maya_cmds.setAttr(f"{limiter}.order", order)
    maya_cmds.connectAttr(
        f"{source}.outputQuat",
        f"{limiter}.inputQuat",
    )
    return source, limiter


def test_node_ids_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    quat_node = maya_cmds.createNode("bdQuat_LimitBendTwist")
    euler_node = maya_cmds.createNode("bdEuler_LimitBendTwist")
    selection = maya_om.MSelectionList()
    selection.add(quat_node)
    selection.add(euler_node)
    quat_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    euler_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))

    assert quat_fn.typeId.id() == 0x0007F092
    assert euler_fn.typeId.id() == 0x0007F093
    for node in (quat_node, euler_node):
        assert maya_cmds.attributeQuery(
            "bendLimitMode", node=node, listEnum=True
        ) == ["Box:Ellipse"]
        assert maya_cmds.attributeQuery("order", node=node, listEnum=True) == [
            "TwistBend:BendTwist"
        ]
        assert maya_cmds.attributeQuery(
            "min", node=node, listChildren=True
        ) == ["minTwist", "minBendH", "minBendV"]
        assert maya_cmds.attributeQuery(
            "max", node=node, listChildren=True
        ) == ["maxTwist", "maxBendH", "maxBendV"]
        assert maya_cmds.attributeQuery(
            "output", node=node, listChildren=True
        ) == ["outputTwist", "outputBendH", "outputBendV"]
        assert _get_angles(maya_cmds, f"{node}.min") == pytest.approx(
            (-180.0, -180.0, -180.0)
        )
        assert _get_angles(maya_cmds, f"{node}.max") == pytest.approx(
            (180.0, 180.0, 180.0)
        )
        assert maya_cmds.getAttr(f"{node}.bendLimitMode") == 0

    assert maya_cmds.attributeQuery(
        "outputQuat", node=quat_node, listChildren=True
    ) == ["outputQuatX", "outputQuatY", "outputQuatZ", "outputQuatW"]
    assert maya_cmds.attributeQuery(
        "inputRotate", node=euler_node, listChildren=True
    ) == ["inputRotateX", "inputRotateY", "inputRotateZ"]
    assert maya_cmds.attributeQuery(
        "outputRotate", node=euler_node, listChildren=True
    ) == ["outputRotateX", "outputRotateY", "outputRotateZ"]


@pytest.mark.parametrize("order", [0, 1])
def test_default_limits_preserve_quaternion_orientation(
    maya_cmds,
    order,
):
    _load_bd_util_nodes(maya_cmds)
    source, limiter = _create_quat_limit_network(
        maya_cmds,
        components=(70.0, 45.0, -30.0),
        order=order,
    )

    _assert_same_rotation(
        _get_quat(maya_cmds, f"{limiter}.outputQuat"),
        _get_quat(maya_cmds, f"{source}.outputQuat"),
    )
    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (70.0, 45.0, -30.0)
    )


def test_box_mode_clamps_components_independently(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    _source, limiter = _create_quat_limit_network(maya_cmds)
    maya_cmds.setAttr(f"{limiter}.min", -30.0, -40.0, -20.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", 45.0, 60.0, 10.0, type="double3")

    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (45.0, 60.0, -20.0)
    )


def test_box_mode_sorts_reversed_limits(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    _source, limiter = _create_quat_limit_network(
        maya_cmds,
        components=(30.0, -50.0, 40.0),
    )
    maya_cmds.setAttr(f"{limiter}.min", 10.0, 20.0, 15.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", -10.0, -20.0, -15.0, type="double3")

    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (10.0, -20.0, 15.0)
    )


def test_ellipse_mode_projects_radially_to_asymmetric_boundary(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    _source, limiter = _create_quat_limit_network(
        maya_cmds,
        components=(70.0, 80.0, 40.0),
    )
    maya_cmds.setAttr(f"{limiter}.bendLimitMode", 1)
    maya_cmds.setAttr(f"{limiter}.min", -35.0, -60.0, -30.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", 35.0, 90.0, 45.0, type="double3")

    ratio = math.sqrt((80.0 / 90.0) ** 2 + (40.0 / 45.0) ** 2)
    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (35.0, 80.0 / ratio, 40.0 / ratio)
    )


def test_ellipse_mode_uses_negative_direction_extents(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    _source, limiter = _create_quat_limit_network(
        maya_cmds,
        components=(0.0, -80.0, 40.0),
    )
    maya_cmds.setAttr(f"{limiter}.bendLimitMode", 1)
    maya_cmds.setAttr(f"{limiter}.min", -180.0, -60.0, -30.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", 180.0, 90.0, 45.0, type="double3")

    ratio = math.sqrt((-80.0 / 60.0) ** 2 + (40.0 / 45.0) ** 2)
    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (0.0, -80.0 / ratio, 40.0 / ratio)
    )


def test_output_quat_matches_limited_components(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    _source, limiter = _create_quat_limit_network(
        maya_cmds,
        components=(-75.0, 65.0, 50.0),
        order=1,
    )
    maya_cmds.setAttr(f"{limiter}.bendLimitMode", 1)
    maya_cmds.setAttr(f"{limiter}.min", -40.0, -50.0, -35.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", 55.0, 50.0, 35.0, type="double3")

    recomposed = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{recomposed}.axisQuat", *_AXIS_QUAT, type="double4")
    maya_cmds.setAttr(f"{recomposed}.order", 1)
    maya_cmds.connectAttr(f"{limiter}.output", f"{recomposed}.input")
    _assert_same_rotation(
        _get_quat(maya_cmds, f"{limiter}.outputQuat"),
        _get_quat(maya_cmds, f"{recomposed}.outputQuat"),
    )


def test_invalid_quaternion_falls_back_before_limits(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdQuat_LimitBendTwist")
    maya_cmds.setAttr(f"{node}.inputQuat", 0.0, 0.0, 0.0, 0.0, type="double4")
    maya_cmds.setAttr(f"{node}.min", 10.0, 20.0, 30.0, type="double3")
    maya_cmds.setAttr(f"{node}.max", 10.0, 20.0, 30.0, type="double3")

    assert _get_angles(maya_cmds, f"{node}.output") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )


def test_euler_node_limits_and_recomposes_in_selected_output_order(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    source = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    limiter = maya_cmds.createNode("bdEuler_LimitBendTwist")
    recomposed = maya_cmds.createNode("bdEuler_ComposeBendTwist")

    axis_rotate = (15.0, -25.0, 40.0)
    maya_cmds.setAttr(f"{source}.input", 90.0, 70.0, -45.0, type="double3")
    maya_cmds.setAttr(f"{source}.axisRotate", *axis_rotate, type="double3")
    maya_cmds.setAttr(f"{source}.axisRotateOrder", 2)
    maya_cmds.setAttr(f"{source}.order", 1)
    maya_cmds.setAttr(f"{source}.outputRotateOrder", 4)

    maya_cmds.connectAttr(f"{source}.outputRotate", f"{limiter}.inputRotate")
    maya_cmds.setAttr(f"{limiter}.inputRotateOrder", 4)
    maya_cmds.setAttr(f"{limiter}.axisRotate", *axis_rotate, type="double3")
    maya_cmds.setAttr(f"{limiter}.axisRotateOrder", 2)
    maya_cmds.setAttr(f"{limiter}.order", 1)
    maya_cmds.setAttr(f"{limiter}.outputRotateOrder", 5)
    maya_cmds.setAttr(f"{limiter}.min", -30.0, -40.0, -20.0, type="double3")
    maya_cmds.setAttr(f"{limiter}.max", 50.0, 55.0, 25.0, type="double3")

    assert _get_angles(maya_cmds, f"{limiter}.output") == pytest.approx(
        (50.0, 55.0, -20.0)
    )

    maya_cmds.connectAttr(f"{limiter}.output", f"{recomposed}.input")
    maya_cmds.setAttr(f"{recomposed}.axisRotate", *axis_rotate, type="double3")
    maya_cmds.setAttr(f"{recomposed}.axisRotateOrder", 2)
    maya_cmds.setAttr(f"{recomposed}.order", 1)
    maya_cmds.setAttr(f"{recomposed}.outputRotateOrder", 5)
    assert _get_angles(maya_cmds, f"{limiter}.outputRotate") == pytest.approx(
        _get_angles(maya_cmds, f"{recomposed}.outputRotate")
    )


def test_node_operator_creation_and_existing_access(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_euler_limit_bend_twist import (
        BdEulerLimitBendTwist,
    )
    from bd_util.maya.node.operator.node.dg.bd_quat_limit_bend_twist import (
        BdQuatLimitBendTwist,
    )

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    quat_node = nodes.create.bdQuat_LimitBendTwist(name="quat_limit")
    euler_node = nodes.create.bdEuler_LimitBendTwist(name="euler_limit")
    quat_node.min.set((-30.0, -45.0, -60.0))
    quat_node.max.set((30.0, 45.0, 60.0))
    quat_node.bendLimitMode.set(quat_node.bendLimitMode.ELLIPSE)
    mod.do_it_dg()

    assert isinstance(quat_node, BdQuatLimitBendTwist)
    assert isinstance(euler_node, BdEulerLimitBendTwist)
    assert tuple(quat_node.min.get()) == pytest.approx((-30.0, -45.0, -60.0))
    assert tuple(quat_node.max.get()) == pytest.approx((30.0, 45.0, 60.0))
    assert quat_node.bendLimitMode.get() == quat_node.bendLimitMode.ELLIPSE
    assert isinstance(
        nodes.existing.bdQuat_LimitBendTwist(quat_node.name),
        BdQuatLimitBendTwist,
    )
    assert isinstance(
        nodes.existing.bdEuler_LimitBendTwist(euler_node.name),
        BdEulerLimitBendTwist,
    )
