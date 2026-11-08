# coding: utf-8
from __future__ import annotations

import itertools
import math

import pytest

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller, _union_bounds
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_cage_geometry import _set_faces
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

ARROW_FAMILY = SHAPE_NAMES[21:]
NEW_BODIES = (
    "SquareArrowPlanar",
    "CircleArrowPlanar",
    "DiamondArrowAxial",
    "ArrowSpatial",
)


def _limits(main, swapped, transverse=(1.4, 0.6)):
    axis = int(swapped)
    result = [(-0.5, 0.5)] * 3
    result[axis] = main
    for component, span in zip((1 - axis, 2), transverse):
        result[component] = (0.3 - span / 2, 0.3 + span / 2)
    return result


def _frame(preset, limits, swapped):
    axis = int(swapped)
    minus, plus = limits[axis]
    direction = 1 if plus >= minus else -1
    center = [(low + high) / 2 for low, high in limits]
    center[axis] = minus
    radii = [abs(high - low) / 2 for low, high in limits]
    radius = (
        radii[2]
        if preset.endswith("Planar")
        else (radii[1 - axis] + radii[2]) / 2
    )
    front = minus + direction * max(
        abs(plus - minus),
        radius * (1.5 if preset in ("ArrowPlanar", "ArrowSpatial") else 1),
    )
    rear = minus - direction * radius * (
        0.5 if preset in ("ArrowPlanar", "ArrowSpatial") else 1
    )
    return axis, center, radii, radius, direction, rear, front


def _family_bounds(preset, limits, swapped):
    axis, center, radii, _, _, rear, front = _frame(preset, limits, swapped)
    if preset.endswith("Axial"):
        rear, front = limits[axis]
    result = [min(low, high) for low, high in limits] + [
        max(low, high) for low, high in limits
    ]
    result[axis], result[axis + 3] = min(rear, front), max(rear, front)
    if preset.endswith("Planar"):
        result[1 - axis] = result[4 - axis] = center[1 - axis]
    return tuple(result)


def _vertices(preset, limits, swapped):
    axis, center, radii, radius, direction, rear, front = _frame(
        preset, limits, swapped
    )
    points = []
    if preset == "ArrowSpatial":
        for component in (1 - axis, 2):
            for along, across in (
                (front, 0),
                (center[axis], -radii[component]),
                (rear, -radii[component] / 2),
                (center[axis], 0),
                (rear, radii[component] / 2),
                (center[axis], radii[component]),
            ):
                point = center.copy()
                point[axis] = along
                point[component] += across
                points.append(point)
    elif preset == "SquareArrowPlanar":
        for along, across in itertools.product(
            (rear, center[axis] + direction * radius), limits[2]
        ):
            point = center.copy()
            point[axis], point[2] = along, across
            points.append(point)
        point = center.copy()
        point[axis] = front
        points.append(point)
    elif preset == "DiamondArrowAxial":
        point = center.copy()
        point[axis] = limits[axis][1]
        points.append(point)
        for component in (1 - axis, 2):
            for sign in (-1, 1):
                point = center.copy()
                point[component] += sign * radii[component]
                points.append(point)
    return points


def _sites(preset, limits, swapped):
    axis, center, radii, _, direction, rear, front = _frame(
        preset, limits, swapped
    )
    tip = center.copy()
    tip[axis] = limits[axis][1] if preset.endswith("Axial") else front
    result = [
        (tip, tuple(direction if index == axis else 0 for index in range(3)))
    ]
    if preset.endswith("Axial"):
        return result
    if preset != "ArrowSpatial":
        point = center.copy()
        point[axis] = rear
        result.append(
            (
                point,
                tuple(
                    -direction if index == axis else 0 for index in range(3)
                ),
            )
        )
    for component in ((1 - axis, 2) if preset == "ArrowSpatial" else (2,)):
        for sign in (-1, 1):
            point = center.copy()
            point[component] += sign * radii[component]
            result.append(
                (
                    point,
                    tuple(
                        sign if index == component else 0 for index in range(3)
                    ),
                )
            )
    return result


@pytest.mark.parametrize("preset", ARROW_FAMILY)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((0.2, 2), (0.2, 0.3), (1, -1), (0.2, 0.2)))
@pytest.mark.parametrize("transverse", ((1.4, 0.6), (0, 1.2)))
def test_arrow_family_body_bounds_follow_planar_axial_and_spatial_contracts(
    maya_cmds, maya_om, new_scene, preset, swapped, main, transverse
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "familyBody", preset, shapeAxisSwap=swapped)
    limits = _limits(main, swapped, transverse)
    _set_base_space(maya_cmds, shape, limits)
    expected = _family_bounds(preset, limits, swapped)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((0.2, 2), (0.2, 0.3), (1, -1)))
def test_new_arrow_family_rotated_bounds_use_independent_vertices_or_circle_support(
    maya_cmds, maya_om, new_scene, preset, swapped, main
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "familyRotatedBody",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits(main, swapped)
    _set_base_space(maya_cmds, shape, limits)
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    rotation = maya_om.MEulerRotation(
        *(math.radians(value) for value in angles)
    ).asMatrix()
    if preset == "CircleArrowPlanar":
        axis, center, _, radius, _, _, front = _frame(preset, limits, swapped)
        tip = center.copy()
        tip[axis] = front
        posed_center, posed_tip = (
            maya_om.MPoint(*center) * rotation,
            maya_om.MPoint(*tip) * rotation,
        )
        along = (
            maya_om.MVector(*(int(index == axis) for index in range(3)))
            * rotation
        )
        side = maya_om.MVector(0, 0, 1) * rotation
        extent = [
            radius * math.hypot(along[index], side[index])
            for index in range(3)
        ]
        expected = tuple(
            min(posed_center[index] - extent[index], posed_tip[index])
            for index in range(3)
        ) + tuple(
            max(posed_center[index] + extent[index], posed_tip[index])
            for index in range(3)
        )
    else:
        points = [
            maya_om.MPoint(*point) * rotation
            for point in _vertices(preset, limits, swapped)
        ]
        expected = tuple(
            min(point[index] for point in points) for index in range(3)
        ) + tuple(max(point[index] for point in points) for index in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(
        expected, abs=0.005 if preset == "CircleArrowPlanar" else 1e-9
    )


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("placement", (0, 1, 2))
@pytest.mark.parametrize("main", ((0.2, 2), (0.2, 0.3)))
def test_new_arrow_family_parts_use_four_one_or_five_independent_sites(
    maya_cmds, maya_om, new_scene, preset, swapped, placement, main
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "familyPartSites",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
        shapePart=True,
        shapePartShape=6,
        shapePartType=placement,
        shapePartOffset=3,
        shapePartPrimarySizeScale=1.4,
        shapePartOtherSizeScale=0.6,
    )
    limits = _limits(main, swapped)
    _set_base_space(maya_cmds, shape, limits)
    sites = _sites(preset, limits, swapped)
    assert (
        len(sites)
        == {
            "SquareArrowPlanar": 4,
            "CircleArrowPlanar": 4,
            "DiamondArrowAxial": 1,
            "ArrowSpatial": 5,
        }[preset]
    )
    if placement != 1:
        sites = sites[:1]
    boxes = [_family_bounds(preset, limits, swapped)]
    for index, (point, along) in enumerate(sites):
        scale = (1.4 if index == 0 else 0.6) if placement == 1 else 1
        center = [
            point[component] + 3 * along[component] for component in range(3)
        ]
        boxes.append(
            tuple(value - 0.05 * scale for value in center)
            + tuple(value + 0.05 * scale for value in center)
        )
    assert _bounds(maya_om, shape) == pytest.approx(
        _union_bounds(boxes), abs=1e-9
    )


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("wide", (False, True))
def test_new_arrow_family_supports_all_part_profiles_and_restores_body_options(
    maya_cmds, maya_om, new_scene, preset, part, wide
):
    _load_bd_util_nodes(maya_cmds)
    swapped = bool(part % 2)
    shape = _controller(
        maya_cmds,
        "familyPartProfiles",
        preset,
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapePartShape=part,
        shapePartType=1,
        shapePartOffset=3,
    )
    _set_base_space(maya_cmds, shape, _limits((-0.2, 2), swapped))
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        body = _bounds(maya_om, shape)
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        decorated = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in decorated)
        assert decorated != pytest.approx(body)
        for attribute in (
            "shapeGuideLine",
            "shapeGuideLineTemplate",
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", True)
            assert _bounds(maya_om, shape) == pytest.approx(
                decorated, abs=1e-9
            )
        for attribute in (
            "shapeGuideLine",
            "shapeGuideLineTemplate",
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", False)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
def test_new_arrow_family_face_scale_changes_cage_without_changing_base_radius(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "familyCageRadius",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits((0.2, 0.3), swapped)
    _set_base_space(maya_cmds, shape, limits)
    expected = _family_bounds(preset, limits, swapped)
    for scales in (
        {(axis, "Plus", 2): 2.4},
        {(axis, "Minus", 2): 0},
        {(axis, "Minus", 1 - axis): -1.8},
    ):
        _set_faces(maya_cmds, shape, scales)
        actual = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in actual)
        assert (actual[axis], actual[axis + 3]) == pytest.approx(
            (expected[axis], expected[axis + 3]), abs=1e-9
        )


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
def test_new_arrow_family_zero_transverse_radius_keeps_reversed_part_dimensions(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "zeroRadiusFamilyPart",
        preset,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=2,
    )
    limits = _limits((1, -1), swapped, (0, 0))
    _set_base_space(maya_cmds, shape, limits)
    part = tuple(
        -3.05 if component == axis else 0.25 for component in range(3)
    ) + tuple(-2.95 if component == axis else 0.35 for component in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(
        _union_bounds([_family_bounds(preset, limits, swapped), part]),
        abs=1e-9,
    )


@pytest.mark.parametrize("preset", NEW_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
def test_new_arrow_family_zero_radius_wide_preserves_the_shifted_main_segment(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "zeroRadiusWideFamily",
        preset,
        shapeAxisSwap=swapped,
        shapeWideWidth=0.2,
    )
    _set_base_space(maya_cmds, shape, _limits((1, 3), swapped, (0, 0)))
    for wide, filled in itertools.product((False, True), repeat=2):
        maya_cmds.setAttr(f"{shape}.shapeWide", wide)
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        box = _bounds(maya_om, shape)
        assert all(math.isfinite(value) and abs(value) < 4 for value in box)
        assert (box[axis], box[axis + 3]) == pytest.approx((1, 3), abs=1e-9)
