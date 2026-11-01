# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya


@pytest.mark.parametrize("axis", range(3))
@pytest.mark.parametrize("span", (1e-8, 1e-12, -1e-8, -1e-12, 0.0))
@pytest.mark.parametrize("filled", (False, True))
def test_tiny_and_zero_spans_preserve_part_dimensions_and_offset(
    maya_cmds, maya_om, new_scene, axis, span, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "tinySpace",
        "Line",
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=1.0,
        shapeFill=filled,
    )
    limits = [(-0.5, 0.5)] * 3
    limits[axis] = (-span / 2, span / 2)
    _set_base_space(maya_cmds, shape, limits)
    x_span = span if axis == 0 else 1.0
    direction = -1.0 if x_span < 0 else 1.0
    center = x_span / 2 + direction
    expected = (
        min(-abs(x_span) / 2, center - 0.05),
        -0.05,
        -0.05,
        max(abs(x_span) / 2, center + 0.05),
        0.05,
        0.05,
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_collapsed_base_keeps_every_part_at_the_mapped_pivot(
    maya_cmds, maya_om, new_scene, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "collapsedSpace",
        "Line",
        shapePart=True,
        shapePartShape=part,
        shapePartOffset=1.0,
        shapePartSize=1.7,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.5,
        shapePartHeightScale=0.8,
        shapeFill=filled,
    )
    original = _bounds(maya_om, shape)
    _set_base_space(maya_cmds, shape, ((2, 2), (3, 3), (4, 4)))
    expected = (
        2,
        original[1] + 3,
        original[2] + 4,
        original[3] + 1.5,
        original[4] + 3,
        original[5] + 4,
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("Line", "LineSwapped", "Cube", "Sphere"))
@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_fin_height_survives_a_collapsed_height_axis(
    maya_cmds, maya_om, new_scene, preset, fin_type, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "collapsedFin",
        preset,
        shapeFin=True,
        shapeFinHeight=0.7,
        shapeFinType=fin_type,
        shapeFill=filled,
    )
    limits = [(1, 3), (-2, 4), (4, 7)]
    height_axis = 0 if preset == "LineSwapped" else 1
    limits[height_axis] = (2, 2)
    _set_base_space(maya_cmds, shape, limits)
    box = _bounds(maya_om, shape)
    assert box[height_axis] == pytest.approx(2, abs=1e-9)
    assert box[height_axis + 3] == pytest.approx(2.7, abs=1e-9)


@pytest.mark.parametrize("preset", ("Cube", "ColorCube"))
def test_reversed_base_coordinates_keep_color_effective_width_positive(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "reversedSpace", preset)
    _set_base_space(maya_cmds, shape, ((3, 1), (4, -2), (7, 4)))
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.7)
    box = _bounds(maya_om, shape)
    expected = (
        (1, -2, 4, 3, 4.7, 7)
        if preset == "ColorCube"
        else (1, -2.7, 4, 3, 4, 7)
    )
    assert box == pytest.approx(expected, abs=1e-9)
    assert maya_cmds.getAttr(f"{shape}.shapeBaseSpace1stAxisMinus") == 3
    assert maya_cmds.getAttr(f"{shape}.shapeBaseSpace1stAxisPlus") == 1


@pytest.mark.parametrize(
    "preset", ("ArcRadial", "ArcAxial", "CrossArcRadial", "CrossArcAxial")
)
@pytest.mark.parametrize("part", range(11))
def test_fully_collapsed_arc_parts_keep_finite_nonzero_local_dimensions(
    maya_cmds, maya_om, new_scene, preset, part
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "collapsedArc",
        preset,
        shapePart=True,
        shapePartType=1,
        shapePartShape=part,
        shapePartOffset=1.0,
        shapeFill=True,
    )
    _set_base_space(maya_cmds, shape, ((0, 0), (0, 0), (0, 0)))
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in box)
    assert max(box[i + 3] - box[i] for i in range(3)) == pytest.approx(
        0.1, abs=1e-9
    )
    assert max(abs(value) for value in box) >= 0.9
