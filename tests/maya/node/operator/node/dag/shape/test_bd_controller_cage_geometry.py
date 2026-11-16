# coding: utf-8
from __future__ import annotations

import itertools
import math

import pytest

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

AXES = ("1st", "2nd", "3rd")
LIMITS = ((1, 3), (-2, 4), (4, 7))
FACE_CASES = (
    {(0, "Plus", 1): 2, (0, "Plus", 2): 1.5},
    {(0, "Plus", 1): 2, (2, "Plus", 1): 3},
    {(0, "Minus", 2): 0.2, (1, "Plus", 0): 1.7, (2, "Minus", 1): 0.3},
    {(0, "Plus", 1): -2, (1, "Minus", 2): 0, (2, "Plus", 0): 1.5},
)


def _set_faces(cmds, shape, scales):
    for (normal, side, component), value in scales.items():
        cmds.setAttr(
            f"{shape}.shapeBaseSpace{AXES[normal]}Axis{side}Scale{AXES[component]}Axis",
            value,
        )


def _cage_point(point, scales, limits=LIMITS):
    center = [(minus + plus) / 2 for minus, plus in limits]
    coordinate = [
        (value - middle) / (plus - minus) if plus != minus else value - middle
        for value, middle, (minus, plus) in zip(point, center, limits)
    ]
    result = []
    for component in range(3):
        factor = 1
        for normal in range(3):
            if normal == component:
                continue
            factor *= (0.5 - coordinate[normal]) * scales.get(
                (normal, "Minus", component), 1
            ) + (0.5 + coordinate[normal]) * scales.get(
                (normal, "Plus", component), 1
            )
        result.append(
            center[component] + (point[component] - center[component]) * factor
        )
    return result


@pytest.mark.parametrize("scales", FACE_CASES)
@pytest.mark.parametrize("angles", ((0, 0, 0), (17, 31, -23), (80, -40, 12)))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_cube_shared_corners_and_common_rotation_follow_the_same_map(
    maya_cmds, maya_om, new_scene, scales, angles, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "sharedCageCorners",
        "Cube",
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shape1stAxis=0,
        shape2ndAxis=2,
    )
    _set_base_space(maya_cmds, shape, LIMITS)
    _set_faces(maya_cmds, shape, scales)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    rotation = maya_om.MEulerRotation(
        *(math.radians(value) for value in angles)
    ).asQuaternion()
    points = [
        maya_om.MVector(*_cage_point(corner, scales)).rotateBy(rotation)
        for corner in itertools.product(*LIMITS)
    ]
    expected = tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("preset", SHAPE_NAMES)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_main_shapes_remain_finite_and_common_size_applies_after_deformation(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "cageMainShape",
        preset,
        shapeFill=filled,
        shape1stAxis=0,
        shape2ndAxis=2,
    )
    _set_base_space(maya_cmds, shape, LIMITS)
    _set_faces(maya_cmds, shape, FACE_CASES[2])
    original = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in original)
    maya_cmds.setAttr(f"{shape}.shapeSize", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        tuple(2 * value for value in original), abs=1e-7
    )


# 横径由来の主軸寸法を持つ本体は、組立後の面倍率を専用テストで確認する。
@pytest.mark.parametrize(
    "preset",
    tuple(
        name
        for name in SHAPE_NAMES
        if name
        not in (
            "ArrowPlanar",
            "SquareArrowPlanar",
            "DiamondArrowPlanar",
            "CircleArrowPlanar",
            "ArrowSpatial",
            "DiamondArrowSpatial",
            "SquareArrowSpatial",
            "CircleArrowSpatial",
            "Capsule",
        )
    ),
)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("wide", (False, True))
def test_constant_opposing_face_scales_match_the_existing_base_space_path(
    maya_cmds, maya_om, new_scene, preset, filled, wide
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=filled,
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapePart=True,
        shapePartShape=6,
        shapePartType=1,
        shapePartOffset=0.1,
        shapeFin=True,
        shapeFinHeight=0.7,
        shapeGuideLine=True,
        shapeTemplateLine=True,
        shapeTemplateFill=True,
    )
    actual = _controller(maya_cmds, "constantFaceScales", preset, **options)
    reference = _controller(
        maya_cmds, "equivalentBaseSpace", preset, **options
    )
    _set_base_space(maya_cmds, actual, LIMITS)
    _set_faces(
        maya_cmds,
        actual,
        {
            (normal, side, component): factor
            for normal, component, factor in (
                (1, 0, 2),
                (0, 1, 0.7),
                (0, 2, 1.5),
            )
            for side in ("Plus", "Minus")
        },
    )
    effective = tuple(
        (
            (minus + plus) / 2 + (minus - plus) * factor / 2,
            (minus + plus) / 2 + (plus - minus) * factor / 2,
        )
        for (minus, plus), factor in zip(LIMITS, (2, 0.7, 1.5))
    )
    _set_base_space(maya_cmds, reference, effective)
    assert _bounds(maya_om, actual) == pytest.approx(
        _bounds(maya_om, reference), abs=1e-8
    )
