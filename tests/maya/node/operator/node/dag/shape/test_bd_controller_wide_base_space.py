# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

CURVED_PRESETS = (
    "Circle",
    "Sphere",
    "ColorSphere",
    "Cylinder",
    "Cone",
    "ArcRadial",
    "ArcAxial",
    "CrossArcRadial",
    "CrossArcAxial",
)


@pytest.mark.parametrize("preset", CURVED_PRESETS)
@pytest.mark.parametrize("scale", (0.4, 2.0, 5.0))
@pytest.mark.parametrize("filled", (False, True))
def test_curved_wide_keeps_physical_width_when_base_space_size_changes(
    maya_cmds, maya_om, new_scene, preset, scale, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeWide=True,
        shapeWideWidth=0.12,
        shapeFill=filled,
        shapeArcAngle=240,
        shapePart=True,
        shapePartShape=3,
        shapePartSize=1.2,
        shapePartOffset=0.08,
    )
    actual = _controller(maya_cmds, "physicalWide", preset, **options)
    reference = _controller(maya_cmds, "referenceWide", preset, **options)
    _set_base_space(maya_cmds, actual, ((-scale / 2, scale / 2),) * 3)
    maya_cmds.setAttr(f"{reference}.shapeSize", scale)
    maya_cmds.setAttr(f"{reference}.shapeWideWidth", 0.12 / scale)
    maya_cmds.setAttr(f"{reference}.shapePartSize", 1.2 / scale)
    maya_cmds.setAttr(f"{reference}.shapePartOffset", 0.08 / scale)
    assert _bounds(maya_om, actual) == pytest.approx(
        _bounds(maya_om, reference), abs=3e-7
    )


@pytest.mark.parametrize("preset", ("Circle", "ArcRadial", "ArcAxial"))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_ellipse_wide_uses_normal_distance_instead_of_scaled_radius(
    maya_cmds, maya_om, new_scene, preset, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "normalWidth",
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeAxisSwap=swapped,
        shapeFill=filled,
    )
    _set_base_space(maya_cmds, shape, ((-2, 2), (-1, 1), (-3, 3)))
    if preset == "ArcAxial":
        expected = (
            (-0.1, 0, -3, 0.1, 1, 3) if swapped else (0, -0.1, -3, 2, 0.1, 3)
        )
    elif preset == "ArcRadial":
        expected = (
            (0, 0, -3.1, 0, 1.1, 3.1) if swapped else (0, 0, -3.1, 2.1, 0, 3.1)
        )
    else:
        expected = (
            (0, -1.1, -3.1, 0, 1.1, 3.1)
            if swapped
            else (-2.1, 0, -3.1, 2.1, 0, 3.1)
        )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("preset", CURVED_PRESETS)
@pytest.mark.parametrize("width", (0, 0.12, 3))
def test_curved_wide_nonuniform_reflection_and_small_body_remain_finite(
    maya_cmds, maya_om, new_scene, preset, width
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "smallWide", preset, shapeWide=True, shapeWideWidth=width
    )
    _set_base_space(
        maya_cmds, shape, ((0.15, -0.15), (-0.05, 0.05), (-0.3, 0.3))
    )
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert all(math.isfinite(value) for value in _bounds(maya_om, shape))


@pytest.mark.parametrize(
    "preset",
    (
        "Circle",
        "Sphere",
        "ColorSphere",
        "Cylinder",
        "Cone",
        "ArcRadial",
        "CrossArcRadial",
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_curved_wide_template_classification_preserves_nonuniform_geometry_bounds(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "metricTemplate",
        preset,
        shapeWide=True,
        shapeWideWidth=0.14,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=0.13,
    )
    _set_base_space(maya_cmds, shape, ((-1, 1), (-1.5, 1.5), (-2, 2)))
    expected = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", 0.37)
    maya_cmds.setAttr(f"{shape}.shapeTemplateFill", True)
    maya_cmds.setAttr(f"{shape}.shapePartTemplate", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


def test_common_scale_still_scales_the_physical_wide_width(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "scaledWidth", "Circle", shapeWide=True, shapeWideWidth=0.2
    )
    _set_base_space(maya_cmds, shape, ((-2, 2), (-1, 1), (-3, 3)))
    maya_cmds.setAttr(f"{shape}.shapeSize", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-4.2, 0, -6.2, 4.2, 0, 6.2)
    )


@pytest.mark.parametrize(
    "preset",
    (
        "Line",
        "CrossLine",
        "CrossLine3Axis",
        "Cube",
        "Octahedron",
        "Pyramid",
        "Gear",
    ),
)
@pytest.mark.parametrize("scale", (0.4, 2.0, 5.0))
@pytest.mark.parametrize("filled", (False, True))
def test_straight_and_polyhedral_wide_keep_width_under_uniform_base_change(
    maya_cmds, maya_om, new_scene, preset, scale, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(shapeWide=True, shapeWideWidth=0.12, shapeFill=filled)
    actual = _controller(maya_cmds, "physicalStraightWide", preset, **options)
    reference = _controller(
        maya_cmds, "referenceStraightWide", preset, **options
    )
    _set_base_space(maya_cmds, actual, ((-scale / 2, scale / 2),) * 3)
    maya_cmds.setAttr(f"{reference}.shapeSize", scale)
    maya_cmds.setAttr(f"{reference}.shapeWideWidth", 0.12 / scale)
    assert _bounds(maya_om, actual) == pytest.approx(
        _bounds(maya_om, reference), abs=1e-8
    )


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_line_wide_tracks_body_length_and_keeps_its_width(
    maya_cmds, maya_om, new_scene, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "lineWidth",
        "Line",
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeAxisSwap=swapped,
        shapeFill=filled,
    )
    _set_base_space(maya_cmds, shape, ((1, 5), (2, 8), (3, 13)))
    expected = (3, 2, 7.9, 3, 8, 8.1) if swapped else (1, 5, 7.9, 5, 5, 8.1)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
