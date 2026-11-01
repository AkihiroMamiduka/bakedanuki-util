# coding: utf-8
from __future__ import annotations

import itertools
import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

ARC_PRESETS = (
    "ArcRadial",
    "ArcAxial",
    "WideArcRadial",
    "WideArcAxial",
    "CrossArcRadial",
    "CrossArcAxial",
    "WideCrossArcRadial",
    "WideCrossArcAxial",
)


def _adaptive_integral(function, first, last, tolerance=1e-12):
    def refine(low, high, left, middle, right, estimate, remaining):
        center = (low + high) / 2
        quarter = function((low + center) / 2)
        three_quarters = function((center + high) / 2)
        before = (center - low) * (left + 4 * quarter + middle) / 6
        after = (high - center) * (middle + 4 * three_quarters + right) / 6
        error = before + after - estimate
        if remaining == 0 or abs(error) <= 15 * tolerance:
            return before + after + error / 15
        return refine(
            low, center, left, quarter, middle, before, remaining - 1
        ) + refine(
            center, high, middle, three_quarters, right, after, remaining - 1
        )

    left, middle, right = (
        function(first),
        function((first + last) / 2),
        function(last),
    )
    estimate = (last - first) * (left + 4 * middle + right) / 6
    return refine(first, last, left, middle, right, estimate, 20)


@pytest.mark.parametrize("preset", ARC_PRESETS)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("placement", (0, 1))
def test_uniform_base_space_matches_inverse_part_size_and_global_scale(
    maya_cmds, maya_om, new_scene, preset, part, placement
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapePart=True,
        shapePartShape=part,
        shapePartType=placement,
        shapePartSize=1.3,
        shapePartLengthScale=1.7,
        shapePartWidthScale=1.4,
        shapePartHeightScale=0.8,
        shapePartOffset=0.11,
        shapeArcAngle=120,
        shapeWideWidth=0.08,
    )
    actual = _controller(maya_cmds, "baseSpaceArc", preset, **options)
    reference = _controller(maya_cmds, "scaledArc", preset, **options)
    _set_base_space(maya_cmds, actual, ((-1, 1),) * 3)
    maya_cmds.setAttr(f"{reference}.shapeSize", 2)
    maya_cmds.setAttr(f"{reference}.shapePartSize", 0.65)
    maya_cmds.setAttr(f"{reference}.shapePartOffset", 0.055)
    maya_cmds.setAttr(f"{reference}.shapeWideWidth", 0.04)
    for swapped, filled in itertools.product((False, True), repeat=2):
        for shape in (actual, reference):
            maya_cmds.setAttr(f"{shape}.shapeAxisSwap", swapped)
            maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, actual) == pytest.approx(
            _bounds(maya_om, reference), abs=2e-7
        ), (preset, part, placement, swapped, filled)


@pytest.mark.parametrize("swapped", (False, True))
def test_axial_wrap_length_uses_the_physical_ellipse_arc_length(
    maya_cmds, maya_om, new_scene, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "ellipseLength",
        "ArcAxial",
        shapePart=True,
        shapePartShape=3,
        shapePartLengthScale=4,
        shapeAxisSwap=swapped,
    )
    _set_base_space(maya_cmds, shape, ((-1, 1), (-1, 1), (-2, 2)))
    # 半長0.2のSquareが、半径1・2の楕円の端点から同じ弧長だけ伸びる。
    low, high = 0.0, math.pi / 2
    for _ in range(48):
        angle = (low + high) / 2
        length = _adaptive_integral(
            lambda value: math.hypot(math.cos(value), 2 * math.sin(value)),
            0,
            angle,
        )
        if length < 0.2:
            low = angle
        else:
            high = angle
    extent = math.sin((low + high) / 2)
    expected = (-extent, -0.05, -2, 1, 0.05, 2)
    if swapped:
        expected = (-0.05, -extent, -2, 0.05, 1, 2)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("preset", ("ArcRadial", "ArcAxial"))
def test_small_solid_finds_a_short_contact_interval_on_a_large_arc(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    actual = _controller(
        maya_cmds,
        "largeArcContact",
        preset,
        shapePart=True,
        shapePartShape=6,
        shapePartLengthScale=2,
        shapePartWidthScale=1.4,
        shapePartHeightScale=0.8,
        shapePartOffset=-5,
        shapeArcAngle=120,
        shapeFill=True,
    )
    reference = _controller(
        maya_cmds,
        "smallArcContact",
        preset,
        shapePart=True,
        shapePartShape=6,
        shapePartSize=0.001,
        shapePartLengthScale=2,
        shapePartWidthScale=1.4,
        shapePartHeightScale=0.8,
        shapePartOffset=-0.005,
        shapeArcAngle=120,
        shapeSize=1000,
        shapeFill=True,
    )
    _set_base_space(maya_cmds, actual, ((-500, 500),) * 3)
    for shape in (actual, reference):
        maya_cmds.setAttr(f"{shape}.shapeRotateY", 30)
    assert _bounds(maya_om, actual) == pytest.approx(
        _bounds(maya_om, reference), abs=1e-7
    )


@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("swapped", (False, True))
def test_zero_base_normal_keeps_the_wide_body_and_wrapped_part_width_intact(
    maya_cmds, maya_om, new_scene, part, swapped
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapePart=True,
        shapePartShape=part,
        shapePartLengthScale=4,
        shapePartWidthScale=1.4,
        shapePartHeightScale=1.3,
        shapePartOffset=0 if part >= 6 else 0.7,
        shapeAxisSwap=swapped,
    )
    actual = _controller(
        maya_cmds, "zeroAxialWidth", "WideArcAxial", **options
    )
    reference = _controller(
        maya_cmds, "restoredNormal", "WideArcAxial", **options
    )
    limits = [(-1, 1), (-1, 1), (-2, 2)]
    limits[0 if swapped else 1] = (0, 0)
    _set_base_space(maya_cmds, actual, limits)
    limits[0 if swapped else 1] = (-0.5, 0.5)
    _set_base_space(maya_cmds, reference, limits)
    for filled in (False, True):
        for shape in (actual, reference):
            maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, actual) == pytest.approx(
            _bounds(maya_om, reference), abs=1e-8
        ), (part, swapped, filled)


@pytest.mark.parametrize("swapped", (False, True))
def test_cross_arc_keeps_wrap_on_the_plane_that_survives_a_zero_axis(
    maya_cmds, maya_om, new_scene, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "oneSurvivingPlane",
        "WideCrossArcAxial",
        shapePart=True,
        shapePartShape=3,
        shapePartLengthScale=4,
        shapePartOffset=0.7,
        shapeWideWidth=0.08,
        shapeAxisSwap=swapped,
    )
    limits = [(-1, 1), (-1, 1), (-2, 2)]
    limits[0 if swapped else 1] = (0, 0)
    _set_base_space(maya_cmds, shape, limits)
    low, high = 0.0, math.pi / 2
    for _ in range(48):
        angle = (low + high) / 2
        length = _adaptive_integral(
            lambda value: math.hypot(math.cos(value), 2 * math.sin(value)),
            0,
            angle,
        )
        if length < 0.2:
            low = angle
        else:
            high = angle
    extent = math.sin((low + high) / 2)
    apex = math.sqrt(1 - 0.08**2)
    expected = (-extent, -0.05, -2, apex, 0.05, 2)
    if swapped:
        expected = (-0.05, -extent, -2, 0.05, apex, 2)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("axial", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_solid_part_keeps_orthogonal_dimensions_at_an_oblique_ellipse_endpoint(
    maya_cmds, maya_om, new_scene, axial, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "ellipseCube",
        "ArcAxial" if axial else "ArcRadial",
        shapePart=True,
        shapePartShape=6,
        shapePartSize=1.4,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
        shapePartHeightScale=0.8,
        shapePartOffset=2,
        shapeArcAngle=120,
        shapeAxisSwap=swapped,
        shapeFill=filled,
    )
    _set_base_space(maya_cmds, shape, ((-1, 1), (-1.5, 1.5), (-2, 2)))
    radius = 1.5 if swapped else 1.0
    angle = math.pi / 6
    endpoint = (radius * math.sin(angle), 0.0, -2 * math.cos(angle))
    tangent_length = math.hypot(radius * math.cos(angle), 2 * math.sin(angle))
    along = (
        -radius * math.cos(angle) / tangent_length,
        0.0,
        -2 * math.sin(angle) / tangent_length,
    )
    normal_length = math.hypot(math.sin(angle) / radius, math.cos(angle) / 2)
    normal = (
        math.sin(angle) / radius / normal_length,
        0.0,
        -math.cos(angle) / 2 / normal_length,
    )
    side = (0.0, 1.0, 0.0) if axial else normal
    up = normal if axial else (0.0, 1.0, 0.0)
    half_sizes = (0.05 * 1.4 * 1.3, 0.05 * 1.4 * 1.7, 0.05 * 1.4 * 0.8)
    points = [
        tuple(
            endpoint[axis]
            + along[axis] * (2 + length * half_sizes[0])
            + side[axis] * width * half_sizes[1]
            + up[axis] * height * half_sizes[2]
            for axis in range(3)
        )
        for length, width, height in itertools.product((-1, 1), repeat=3)
    ]
    points.extend(
        (
            (radius * math.sin(angle), 0.0, -2 * math.cos(angle)),
            (radius * math.sin(angle), 0.0, 2 * math.cos(angle)),
            (radius, 0.0, 0.0),
        )
    )
    if swapped:
        points = [(point[1], point[0], -point[2]) for point in points]
    expected = tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)
