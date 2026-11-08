# coding: utf-8
from __future__ import annotations

import math

import pytest

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya


def _set_cage(cmds, shape, value=2.0):
    cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlusScale2ndAxis", value)


@pytest.mark.parametrize("preset", SHAPE_NAMES)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_wide_supports_every_body_with_nonuniform_face_scales(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "cageWideBody",
        preset,
        shapeWide=True,
        shapeWideWidth=0.1,
        shapeFill=filled,
    )
    _set_cage(maya_cmds, shape)
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in box)
    assert max(box[axis + 3] - box[axis] for axis in range(3)) > 0.1


@pytest.mark.parametrize(
    "preset", ("Line", "CrossLine3Axis", "ColorCrossLine3Axis")
)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_line_width_is_built_after_mapping_the_center_axes(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "cageLineWidth",
        preset,
        shapeWide=True,
        shapeWideWidth=0.1,
        shapeFill=filled,
    )
    _set_cage(maya_cmds, shape)
    expected = (
        (-0.5, 0, -0.05, 0.5, 0, 0.05)
        if preset == "Line"
        else (-0.5, -0.75, -0.5, 0.5, 0.75, 0.5)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("preset", ("Circle", "ArcRadial", "ArcAxial"))
@pytest.mark.parametrize("filled", (False, True))
def test_cage_arc_width_follows_the_new_curve_normal_in_physical_space(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "cageCurveWidth",
        preset,
        shapeWide=True,
        shapeWideWidth=0.1,
        shapeFill=filled,
    )
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlusScale3rdAxis", 2)
    cosine = (-3 + math.sqrt(17)) / 4
    maximum = 0.5 * math.sqrt(1 - cosine * cosine) * (1.5 + 0.5 * cosine)
    if preset == "Circle":
        expected = (-0.55, 0, -maximum - 0.05, 0.55, 0, maximum + 0.05)
    elif preset == "ArcRadial":
        expected = (
            -0.05 / math.sqrt(5),
            0,
            -maximum - 0.05,
            0.55,
            0,
            maximum + 0.05,
        )
    else:
        expected = (0, -0.05, -maximum, 0.5, 0.05, maximum)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=3e-4)


@pytest.mark.parametrize(
    "preset",
    (
        "Cube",
        "ColorCornerCube",
        "Sphere",
        "Cylinder",
        "CircleArrowAxial",
        "CrossArcAxial",
    ),
)
@pytest.mark.parametrize("value", (0.0, -1.0, 0.1))
def test_cage_wide_and_corner_fields_remain_finite_when_faces_fold_or_collapse(
    maya_cmds, maya_om, new_scene, preset, value
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "foldedCageWide",
        preset,
        shapeWide=True,
        shapeWideWidth=0.3,
        shapeFill=True,
    )
    _set_cage(maya_cmds, shape, value)
    assert all(math.isfinite(value) for value in _bounds(maya_om, shape))


def test_common_size_still_scales_cage_generated_wide_geometry(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "cageCommonSize", "Cube", shapeWide=True, shapeWideWidth=0.1
    )
    _set_cage(maya_cmds, shape)
    original = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeSize", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        tuple(value * 2 for value in original), abs=1e-8
    )


@pytest.mark.parametrize("preset", ("ArcRadial", "ArcAxial"))
@pytest.mark.parametrize("filled", (False, True))
def test_cage_wide_small_radial_arc_stops_the_inner_band_at_the_center(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "smallCageArcWidth",
        preset,
        shapeWide=True,
        shapeWideWidth=0.3,
        shapeFill=filled,
    )
    for axis in ("1st", "2nd", "3rd"):
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", 0.05)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", 0.05)
    # 全体としては非線形だが、中央XZ面は半径0.075の円になる。
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale1stAxis", 2)
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace2ndAxisPlusScale3rdAxis", 2)
    expected = (
        (0, 0, -0.225, 0.225, 0, 0.225)
        if preset == "ArcRadial"
        else (0, -0.15, -0.075, 0.075, 0.15, 0.075)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)
