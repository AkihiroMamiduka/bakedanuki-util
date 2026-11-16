# coding: utf-8
from __future__ import annotations

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_shape import (
    _bounds,
    _load_bd_util_nodes,
    _set_custom_bounds,
)

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "coordinates,expected",
    (
        ((1, -2, 4, 3, 4, 7), (1, -2, 4, 3, 4, 7)),
        ((3, 4, 7, 1, -2, 4), (1, -2, 4, 3, 4, 7)),
        ((2, 3, 4, 2, 3, 4), (2, 3, 4, 2, 3, 4)),
        ((2, -1, 5, 2, 7, 8), (2, -1, 5, 2, 7, 8)),
    ),
)
def test_custom_endpoint_order_and_zero_dimensions_are_defined(
    maya_cmds, maya_om, new_scene, coordinates, expected
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "customCoordinates", "Cube", boundsMode=2)
    _set_custom_bounds(maya_cmds, shape, coordinates)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    for axis, minus, plus in zip("XYZ", coordinates[:3], coordinates[3:]):
        assert (
            maya_cmds.getAttr(f"{shape}.customBoundsBaseSpace{axis}Minus")
            == -minus
        )
        assert (
            maya_cmds.getAttr(f"{shape}.customBoundsBaseSpace{axis}Plus")
            == plus
        )


def test_custom_box_uses_shared_matrix_and_parent_transform_with_fixed_local_axes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "customMatrix", "ColorCube", boundsMode=2)
    transform = maya_cmds.listRelatives(shape, parent=True, fullPath=True)[0]
    _set_custom_bounds(maya_cmds, shape, (1, -2, 5, 3, 4, 7))
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 100, 200, 300)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 5)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 0)
    maya_cmds.setAttr(f"{shape}.shapeSize", 5)
    matrix = (1, 0.5, 0, 0, 0, 2, 0, 0, 0, 0, -1, 0, 3, 4, 5, 1)
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix, type="matrix"
    )
    assert _bounds(maya_om, shape) == pytest.approx((4, 0.5, -2, 6, 13.5, 0))
    maya_cmds.setAttr(f"{transform}.rotateZ", 90)
    maya_cmds.setAttr(f"{transform}.translate", 10, 20, 30)
    assert maya_cmds.xform(
        transform, query=True, boundingBox=True, worldSpace=True
    ) == pytest.approx((-3.5, 24, 28, 9.5, 26, 30), abs=1e-9)


def test_custom_endpoint_connections_are_ignored_outside_custom_and_survive_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "customConnected", "Cube")
    driver = maya_cmds.createNode("network", name="customBoundsDriver")
    for axis in "XYZ":
        for side, first, last in (("Minus", 0.5, -2), ("Plus", 0.5, 5)):
            attribute = f"{axis}{side}"
            maya_cmds.addAttr(
                driver,
                longName=attribute,
                attributeType="doubleLinear",
                keyable=True,
            )
            maya_cmds.connectAttr(
                f"{driver}.{attribute}",
                f"{shape}.customBoundsBaseSpace{attribute}",
            )
            maya_cmds.setKeyframe(
                driver, attribute=attribute, time=1, value=first
            )
            maya_cmds.setKeyframe(
                driver, attribute=attribute, time=2, value=last
            )
    for mode in (0, 1):
        maya_cmds.setAttr(f"{shape}.boundsMode", mode)
        maya_cmds.currentTime(2)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.5,) * 3 + (0.5,) * 3
        )
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx((2,) * 3 + (5,) * 3)
    scene = tmp_path / "custom_bounds_coordinates.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    maya_cmds.currentTime(2)
    assert _bounds(maya_om, shape) == pytest.approx((2,) * 3 + (5,) * 3)
    for axis in "XYZ":
        for side in ("Minus", "Plus"):
            attribute = f"{axis}{side}"
            assert maya_cmds.isConnected(
                f"{driver}.{attribute}",
                f"{shape}.customBoundsBaseSpace{attribute}",
            )


def test_custom_coordinate_distances_follow_scene_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        shape = _controller(maya_cmds, "customUnits", "Cube", boundsMode=2)
        _set_custom_bounds(maya_cmds, shape, (10, -20, 30, 20, 40, 50))
        expected = (1, -2, 3, 2, 4, 5)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        maya_cmds.currentUnit(linear="cm")
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.customBoundsBaseSpaceXMinus") == -1
    finally:
        maya_cmds.currentUnit(linear=previous)
