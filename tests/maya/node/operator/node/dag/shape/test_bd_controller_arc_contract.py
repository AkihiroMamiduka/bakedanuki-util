# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

ARC_BASES = (
    "ArcRadial",
    "ArcAxial",
    "WideArcRadial",
    "WideArcAxial",
    "CrossArcRadial",
    "CrossArcAxial",
    "WideCrossArcRadial",
    "WideCrossArcAxial",
)
ARC_SHAPES = tuple(
    base + suffix for base in ARC_BASES for suffix in ("", "Swapped")
)
THIN_SHAPES = tuple(name for name in ARC_SHAPES if not name.startswith("Wide"))
WIDE_THIN_PAIRS = tuple(("Wide" + name, name) for name in THIN_SHAPES)


def _controller(maya_cmds, name, preset):
    transform = maya_cmds.createNode("transform", name=name)
    shape = maya_cmds.createNode(
        "bdControllerShape", parent=transform, name=f"{name}Shape"
    )
    names = maya_cmds.attributeQuery("shape", node=shape, listEnum=True)[
        0
    ].split(":")
    maya_cmds.setAttr(f"{shape}.shape", names.index(preset))
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)
    return shape


def _swapped_bounds(bounds):
    low_x, low_y, low_z, high_x, high_y, high_z = bounds
    return low_y, low_x, -high_z, high_y, high_x, -low_z


def _body_bounds(preset, angle):
    if angle == 0:
        return (0.0,) * 6
    cross = "CrossArc" in preset
    wide = preset.startswith("Wide")
    axial = "Axial" in preset
    radius = 0.525 if wide and not axial else 0.5
    inner = 0.475 if wide and not axial else radius
    half_angle = math.radians(angle / 2)
    minimum = (inner if angle < 180 else radius) * math.cos(half_angle)
    side = radius * math.sin(half_angle) if angle < 180 else radius
    normal = 0.025 if wide and axial else 0.0
    maximum = radius
    if cross:
        normal = side = max(normal, side)
        if wide and axial:
            maximum = math.sqrt(0.25 - 0.025**2)
            if angle == 360:
                minimum = -maximum
    expected = minimum, -normal, -side, maximum, normal, side
    return (
        _swapped_bounds(expected) if preset.endswith("Swapped") else expected
    )


@pytest.mark.parametrize("preset", ARC_SHAPES)
@pytest.mark.parametrize("filled", (False, True))
def test_arc_body_uses_public_standard_and_swapped_frames(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "arc", preset)
    maya_cmds.setAttr(f"{shape}.shapeFill", filled)
    assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == pytest.approx(180)
    assert _bounds(maya_om, shape) == pytest.approx(
        _body_bounds(preset, 180), abs=1e-9
    )
    for angle in (0, 90, 180, 360):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        assert _bounds(maya_om, shape) == pytest.approx(
            _body_bounds(preset, angle), abs=1e-9
        ), (preset, filled, angle)


@pytest.mark.parametrize("preset", THIN_SHAPES)
def test_thin_arc_fill_does_not_add_a_sector_or_use_wide_width(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "thinArc", preset)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 90)
    expected = _body_bounds(preset, 90)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        for width in (0, 0.05, 0.9, 3):
            maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
            assert maya_cmds.getAttr(f"{shape}.shapeWideWidth") == width
    # 扇形の中心点が短い円弧の範囲へ混ざらないことを確認する。
    direction = int(preset.endswith("Swapped"))
    assert _bounds(maya_om, shape)[direction] == pytest.approx(
        math.sqrt(0.125), abs=1e-9
    )
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    for part, placement in ((1, 0), (4, 2), (6, 1), (8, 2)):
        maya_cmds.setAttr(f"{shape}.shapePartShape", part)
        maya_cmds.setAttr(f"{shape}.shapePartType", placement)
        maya_cmds.setAttr(f"{shape}.shapePartSize", 1.7)
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.13)
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0)
        expected = _bounds(maya_om, shape)
        for width in (0.05, 0.9, 3):
            maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(("wide_preset", "thin_preset"), WIDE_THIN_PAIRS)
def test_zero_width_arc_matches_thin_arc_for_every_part_and_placement(
    maya_cmds, maya_om, new_scene, wide_preset, thin_preset
):
    _load_bd_util_nodes(maya_cmds)
    wide = _controller(maya_cmds, "wideArc", wide_preset)
    thin = _controller(maya_cmds, "thinArc", thin_preset)
    for shape in (wide, thin):
        for attribute, value in (
            ("shapeWideWidth", 0),
            ("shapeArcAngle", 120),
            ("shapePart", True),
            ("shapePartSize", 1.7),
            ("shapePartLengthScale", 0.8),
            ("shapePartWidthScale", 1.3),
            ("shapePartOffset", 0.13),
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", value)
        # 斜め方向の範囲でも幅方向と追加面の向きを比較する。
        maya_cmds.setAttr(f"{shape}.shapeRotate", 17, -31, 23, type="double3")
        maya_cmds.setAttr(f"{shape}.shapeScale", 1.3, -0.7, 2, type="double3")
    for filled in (False, True):
        for part in range(11):
            for placement in range(3):
                for shape in (wide, thin):
                    maya_cmds.setAttr(f"{shape}.shapeFill", filled)
                    maya_cmds.setAttr(f"{shape}.shapePartShape", part)
                    maya_cmds.setAttr(f"{shape}.shapePartType", placement)
                assert _bounds(maya_om, wide) == pytest.approx(
                    _bounds(maya_om, thin), abs=1e-9
                ), (wide_preset, part, placement, filled)
    maya_cmds.setAttr(f"{wide}.shapeWideWidth", 0.05)
    _bounds(maya_om, wide)
    maya_cmds.setAttr(f"{wide}.shapeWideWidth", 0)
    assert _bounds(maya_om, wide) == pytest.approx(
        _bounds(maya_om, thin), abs=1e-9
    )


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_radial_and_axial_parts_use_distinct_main_and_arrow3d_planes(
    maya_cmds, maya_om, new_scene, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    suffix = "Swapped" if swapped else ""
    shapes = [
        _controller(maya_cmds, direction, f"Arc{direction}{suffix}")
        for direction in ("Radial", "Axial")
    ]
    normal = 0 if swapped else 1
    for shape in shapes:
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        maya_cmds.setAttr(f"{shape}.shapePartShape", 0)
    radial_2d, axial_2d = [_bounds(maya_om, shape) for shape in shapes]
    assert (radial_2d[normal], radial_2d[normal + 3]) == pytest.approx((0, 0))
    assert (axial_2d[normal], axial_2d[normal + 3]) == pytest.approx(
        (-0.05, 0.05)
    )
    for shape in shapes:
        maya_cmds.setAttr(f"{shape}.shapePartShape", 1)
    radial_3d, axial_3d = [_bounds(maya_om, shape) for shape in shapes]
    assert (radial_3d[normal], radial_3d[normal + 3]) == pytest.approx(
        (0, 0.05)
    )
    assert (axial_3d[normal], axial_3d[normal + 3]) == pytest.approx(
        (-0.05, 0.05)
    )
    outer_side = 5 if swapped else 2
    if swapped:
        assert axial_3d[outer_side] > axial_2d[outer_side] + 0.01
    else:
        assert axial_3d[outer_side] < axial_2d[outer_side] - 0.01


@pytest.mark.parametrize("preset", ARC_BASES)
def test_arc_swapped_exchanges_the_complete_body_and_parts(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    standard = _controller(maya_cmds, "standardArc", preset)
    swapped = _controller(maya_cmds, "swappedArc", preset + "Swapped")
    for shape in (standard, swapped):
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", 240)
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0.13)
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.11)
        maya_cmds.setAttr(f"{shape}.shapePartSize", 2)
    for part, placement in ((1, 0), (3, 1), (6, 0), (10, 2)):
        for filled in (False, True):
            for shape in (standard, swapped):
                maya_cmds.setAttr(f"{shape}.shapePartShape", part)
                maya_cmds.setAttr(f"{shape}.shapePartType", placement)
                maya_cmds.setAttr(f"{shape}.shapeFill", filled)
            expected = _swapped_bounds(_bounds(maya_om, standard))
            assert _bounds(maya_om, swapped) == pytest.approx(
                expected, abs=1e-9
            )
