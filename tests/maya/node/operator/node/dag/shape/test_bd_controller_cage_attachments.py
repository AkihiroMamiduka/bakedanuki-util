"""面倍率で接合を動かし、付属物の物理寸法を維持する。"""

from __future__ import annotations

import math

import pytest

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya


def _union_bounds(first, second):
    return tuple(min(first[i], second[i]) for i in range(3)) + tuple(
        max(first[i + 3], second[i + 3]) for i in range(3)
    )


def _set_cage(cmds, shape, attribute="1stAxisPlusScale3rdAxis", value=1.8):
    cmds.setAttr(f"{shape}.shapeBaseSpace{attribute}", value)


@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("preset", ("Cube", "Cylinder"))
def test_cage_all_part_profiles_keep_dimensions_in_the_tilted_face_frame(
    maya_cmds, maya_om, new_scene, part, filled, swapped, preset
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapePart=True,
        shapePartShape=part,
        shapePartOffset=4,
        shapePartSize=1.7,
        shapePartLengthScale=1.3,
        shapePartWidthScale=0.8,
        shapePartHeightScale=1.2,
        shapeFill=filled,
        shapeAxisSwap=swapped,
    )
    actual = _controller(maya_cmds, "tiltedFace", preset, **options)
    attribute = (
        "1stAxisPlusScale2ndAxis" if swapped else "2ndAxisPlusScale1stAxis"
    )
    _set_cage(maya_cmds, actual, attribute, 2)
    # 一面だけを傾けた基準空間では、接合面の単位法線と回転角が解析的に決まる。
    reference = _controller(maya_cmds, "rigidPartReference", preset, **options)
    _set_base_space(maya_cmds, reference, ((0, 0),) * 3)
    angle = math.degrees(math.atan(0.5)) * (1 if swapped else -1)
    maya_cmds.setAttr(f"{reference}.shapeRotateZ", angle)
    maya_cmds.setAttr(
        f"{reference}.shapeTranslate{'Y' if swapped else 'X'}", 0.75
    )
    body = (
        (-0.5, -1, -0.5, 0.5, 1, 0.5)
        if swapped
        else (-1, -0.5, -0.5, 1, 0.5, 0.5)
    )
    expected = _union_bounds(body, _bounds(maya_om, reference))
    assert _bounds(maya_om, actual) == pytest.approx(expected, abs=2e-8)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_fin_height_is_measured_from_the_sloping_body_surface(
    maya_cmds, maya_om, new_scene, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    height = 1.7
    shape = _controller(
        maya_cmds,
        "slopingFin",
        "Cube",
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFin=True,
        shapeFinHeight=height,
    )
    attribute = (
        "2ndAxisPlusScale1stAxis" if swapped else "1stAxisPlusScale2ndAxis"
    )
    _set_cage(maya_cmds, shape, attribute, 2)
    normal_offset = height / math.sqrt(5)
    expected = (
        (-1, -0.5 - normal_offset, -0.5, 1 + 2 * normal_offset, 0.5, 0.5)
        if swapped
        else (-0.5 - normal_offset, -1, -0.5, 0.5, 1 + 2 * normal_offset, 0.5)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=2e-8)


@pytest.mark.parametrize("primary,other", ((1.7, 0.6), (0.0, 0.6), (1.7, 0.0)))
@pytest.mark.parametrize("filled", (False, True))
def test_cage_keeps_primary_and_other_part_sizes_and_hides_zero_sites(
    maya_cmds, maya_om, new_scene, primary, other, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "independentCageParts",
        "Line",
        shapeFill=filled,
        shapePart=True,
        shapePartShape=6,
        shapePartType=1,
        shapePartOffset=2,
        shapePartPrimarySizeScale=primary,
        shapePartOtherSizeScale=other,
    )
    _set_cage(maya_cmds, shape, "2ndAxisPlusScale1stAxis", 2)
    half_width = 0.05 * max(primary, other)
    expected = (
        -2.75 - 0.05 * other if other else -0.75,
        -half_width,
        -half_width,
        2.75 + 0.05 * primary if primary else 0.75,
        half_width,
        half_width,
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


def _curve_speed(angle):
    sine, cosine = math.sin(angle), math.cos(angle)
    return math.hypot(
        0.5 * cosine, 0.5 * sine * (1.5 + 0.5 * sine) - 0.25 * cosine**2
    )


def _curve_length(first, last, divisions=512):
    step = (last - first) / divisions
    return (
        step
        / 3
        * (
            _curve_speed(first)
            + _curve_speed(last)
            + sum(
                (4 if i % 2 else 2) * _curve_speed(first + step * i)
                for i in range(1, divisions)
            )
        )
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_wrapped_square_uses_deformed_arc_length_and_preserves_local_width(
    maya_cmds, maya_om, new_scene, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    length, width = 1.7, 0.8
    shape = _controller(
        maya_cmds,
        "metricWrappedPart",
        "ArcAxial",
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=3,
        shapePartLengthScale=length,
        shapePartWidthScale=width,
    )
    _set_cage(
        maya_cmds,
        shape,
        "2ndAxisPlusScale3rdAxis" if swapped else "1stAxisPlusScale3rdAxis",
        2,
    )
    low, high = -math.pi / 2, 0.0
    for _ in range(45):
        middle = (low + high) / 2
        if _curve_length(middle, 0) > 0.05 * length:
            low = middle
        else:
            high = middle
    expected_minimum = 0.5 * math.sin((low + high) / 2)
    box = _bounds(maya_om, shape)
    along, across = int(swapped), 1 - int(swapped)
    assert box[along] == pytest.approx(expected_minimum, abs=2e-7)
    assert (box[across], box[across + 3]) == pytest.approx(
        (-0.05 * width, 0.05 * width), abs=1e-9
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 3)
    assert _bounds(maya_om, shape) == pytest.approx(box, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_solid_arc_part_applies_offset_once_in_the_new_unit_frame(
    maya_cmds, maya_om, new_scene, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "offsetArcPart",
        "ArcAxial",
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=1,
    )
    _set_cage(
        maya_cmds,
        shape,
        "2ndAxisPlusScale3rdAxis" if swapped else "1stAxisPlusScale3rdAxis",
        2,
    )
    box = _bounds(maya_om, shape)
    along, across = int(swapped), 1 - int(swapped)
    assert box[along] == pytest.approx(-2.15 / math.sqrt(5), abs=1e-8)
    assert (box[across], box[across + 3]) == pytest.approx(
        (-0.05, 0.05), abs=1e-9
    )


@pytest.mark.parametrize("filled", (False, True))
def test_cage_cross_arc_keeps_wrapping_on_the_remaining_nondegenerate_plane(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "mixedCageArc",
        "CrossArcAxial",
        shapeFill=filled,
        shapePart=True,
        shapePartShape=3,
        shapePartType=1,
        shapePartWidthScale=1.6,
    )
    _set_base_space(maya_cmds, shape, ((-0.5, 0.5), (-0.5, 0.5), (0, 0)))
    _set_cage(maya_cmds, shape, "1stAxisPlusScale2ndAxis", 1.8)
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in box)
    assert (box[2], box[5]) == pytest.approx((-0.08, 0.08), abs=1e-9)


@pytest.mark.parametrize(
    "preset", ("Line", "WideLine", "CrossLine", "WideCrossLine3Axis")
)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_straight_body_stops_at_a_part_moved_inward(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "inwardPart",
        preset,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=-0.3,
    )
    _set_cage(maya_cmds, shape, "2ndAxisPlusScale1stAxis", 2)
    box = _bounds(maya_om, shape)
    assert box[3] == pytest.approx(0.75 - 0.3 + 0.05, abs=1e-8)
    assert all(math.isfinite(value) for value in box)


@pytest.mark.parametrize("preset", ("WideLine", "WideCrossLine"))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_wide_part_join_moves_once_with_the_base_space_center(
    maya_cmds, maya_om, new_scene, preset, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "translatedCageJoin",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=0.2,
    )
    _set_cage(maya_cmds, shape, "2ndAxisPlusScale1stAxis", 2)
    original = _bounds(maya_om, shape)
    shift = (2, 3, 4)
    _set_base_space(
        maya_cmds, shape, tuple((value - 0.5, value + 0.5) for value in shift)
    )
    expected = tuple(value + shift[i % 3] for i, value in enumerate(original))
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize(
    "preset",
    tuple(preset for preset in SHAPE_NAMES if preset != "Gear"),
)
@pytest.mark.parametrize("part", range(11))
def test_cage_every_supported_attachment_is_finite_after_rejoining(
    maya_cmds, maya_om, new_scene, preset, part
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "joinedCagePart",
        preset,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapeFill=True,
        shapePartOffset=0.17,
    )
    _set_cage(maya_cmds, shape)
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(value) and abs(value) < 100 for value in box)
    assert max(box[i + 3] - box[i] for i in range(3)) > 0.05


@pytest.mark.parametrize(
    "preset",
    (
        "Line",
        "Cube",
        "Triangle",
        "Cylinder",
        "Arrow",
        "ArcRadial",
        "CrossArcAxial",
    ),
)
@pytest.mark.parametrize("part", (0, 6, 10))
@pytest.mark.parametrize("value", (0.0, -1.5))
def test_cage_collapsed_or_reversed_frames_keep_parts_finite(
    maya_cmds, maya_om, new_scene, preset, part, value
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "singularCagePart",
        preset,
        shapePart=True,
        shapePartShape=part,
        shapePartType=1,
        shapeFill=True,
    )
    _set_cage(maya_cmds, shape, value=value)
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(item) and abs(item) < 100 for item in box)


@pytest.mark.parametrize(
    "preset",
    (
        "Cube",
        "Octahedron",
        "OctahedronArrow",
        "Sphere",
        "Cylinder",
        "Pyramid",
        "Cone",
        "Circle",
        "WideCrossLine3Axis",
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_guides_stay_within_the_finished_body_and_part_bounds(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "cageGuides",
        preset,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=0,
        shapePartType=1,
    )
    _set_cage(maya_cmds, shape)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(before, abs=1e-8)
