# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

ENDPOINTS = (
    (-0.5, 0.5),
    (-0.5, 2.0),
    (1.0, 2.0),
    (-2.0, -1.0),
    (2.0, 1.0),
    (-0.1, 0.05),
    (0.2, -0.2),
    (0.2, 0.2),
    (1e-8, 2e-8),
)


def _body_points(preset, swapped, limits):
    axis = int(swapped)
    minus, plus = limits[axis]
    direction = 1 if plus >= minus else -1
    joint = minus
    if preset == "ArrowPlanar":
        radius = abs(limits[2][1] - limits[2][0]) / 2
        tip = minus + direction * max(abs(plus - minus), 1.5 * radius)
        rear = minus - direction * radius / 2
        vertices = (
            (tip, 0, 0),
            (joint, 0, -0.5),
            (rear, 0, -0.25),
            (joint, 0, 0),
            (rear, 0, 0.25),
            (joint, 0, 0.5),
        )
    else:
        radius = (
            abs(limits[1 - axis][1] - limits[1 - axis][0])
            + abs(limits[2][1] - limits[2][0])
        ) / 4
        vertices = (
            (minus - direction * radius, 0, 0),
            (minus + direction * max(abs(plus - minus), radius), 0, 0),
            (joint, -0.5, 0),
            (joint, 0.5, 0),
            (joint, 0, -0.5),
            (joint, 0, 0.5),
        )
    points = []
    for longitudinal, height, width in vertices:
        point = [(low + high) / 2 for low, high in limits]
        point[axis] = longitudinal
        other = 1 - axis
        point[other] += height * (limits[other][1] - limits[other][0])
        point[2] += width * (limits[2][1] - limits[2][0])
        points.append(tuple(point))
    return points


def _point_bounds(points):
    return tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))


@pytest.mark.parametrize("preset", ("ArrowPlanar", "DiamondArrowSpatial"))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("minus,plus", ENDPOINTS)
def test_arrow_body_keeps_its_rear_section_and_uses_exact_endpoint_coordinates(
    maya_cmds, maya_om, new_scene, preset, swapped, filled, minus, plus
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedRearBody",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeGuideLine=True,
    )
    limits = [(-2.0, 2.0), (1.0, 4.0), (-0.8, 1.2)]
    limits[int(swapped)] = (minus, plus)
    _set_base_space(maya_cmds, shape, limits)
    points = _body_points(preset, swapped, limits)
    assert _bounds(maya_om, shape) == pytest.approx(
        _point_bounds(points), abs=1e-9
    )
    # 断面の位置も確認できる姿勢へ回し、単なる端点のAABB一致にしない。
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    rotation = maya_om.MEulerRotation(
        *(math.radians(value) for value in angles)
    ).asMatrix()
    posed = []
    for point in points:
        value = maya_om.MPoint(*point) * rotation
        posed.append((value.x, value.y, value.z))
    assert _bounds(maya_om, shape) == pytest.approx(
        _point_bounds(posed), abs=1e-9
    )


@pytest.mark.parametrize("preset", ("ArrowPlanar", "DiamondArrowSpatial"))
@pytest.mark.parametrize("fin", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_disabled_part_controls_are_retained_without_deforming_arrow_bodies_or_fins(
    maya_cmds, maya_om, new_scene, preset, fin, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "independentArrowBody",
        preset,
        shapeFin=fin,
        shapeFill=filled,
        shapeGuideLine=True,
        shapePart=False,
    )
    _set_base_space(maya_cmds, shape, ((1, 3), (-0.5, 0.5), (-1.5, 1.5)))
    maya_cmds.setAttr(f"{shape}.shapeRotate", 17, -29, 37)
    expected = _bounds(maya_om, shape)
    values = {
        "shapePartShape": 10,
        "shapePartType": 2,
        "shapePartOffset": -4.0,
        "shapePartSize": -7.0,
        "shapePartPrimarySizeScale": 3.0,
        "shapePartOtherSizeScale": -2.0,
        "shapePartLengthScale": 0.0,
        "shapePartWidthScale": 0.0,
        "shapePartHeightScale": 0.0,
        "shapePartTemplate": True,
    }
    for attribute, value in values.items():
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    for attribute, value in values.items():
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
            value
        )
    # 有効な寸法でPartを表示してから戻しても、本体の固定長とFinは変えない。
    active_sizes = {
        "shapePartSize": 1.7,
        "shapePartLengthScale": 1.3,
        "shapePartWidthScale": 0.8,
        "shapePartHeightScale": 1.2,
    }
    for attribute, value in active_sizes.items():
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    values.update(active_sizes)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    assert _bounds(maya_om, shape) != pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapePart", False)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    for attribute, value in values.items():
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
            value
        )


@pytest.mark.parametrize("preset", ("ArrowPlanar", "DiamondArrowSpatial"))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("fin_type", (0, 1))
def test_arrow_fins_follow_new_body_coordinates_and_keep_their_height(
    maya_cmds, maya_om, new_scene, preset, swapped, fin_type
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedRearFin",
        preset,
        shapeAxisSwap=swapped,
        shapeFin=True,
        shapeFinType=fin_type,
        shapeFinHeight=1.7,
    )
    limits = [(-1, 1), (-1, 1), (-2, 2)]
    limits[int(swapped)] = (1, 3)
    _set_base_space(maya_cmds, shape, limits)
    expected = list(_point_bounds(_body_points(preset, swapped, limits)))
    expected[4 if not swapped else 3] = 1.7
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("ArrowPlanar", "DiamondArrowSpatial"))
def test_fixed_rear_length_is_a_scene_distance_in_centimeters(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    old_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        shape = _controller(maya_cmds, "millimeterRear", preset)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", -10)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 11)
        expected = _point_bounds(
            _body_points(preset, False, ((1, 1.1), (-0.5, 0.5), (-0.5, 0.5)))
        )
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    finally:
        maya_cmds.currentUnit(linear=old_unit)


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_wide_arrow_keeps_the_finished_plane_offset_and_width_on_a_collapsed_axis(
    maya_cmds, maya_om, new_scene, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "flatWideArrow",
        "ArrowPlanar",
        shapeAxisSwap=swapped,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=filled,
    )
    limits = [(2, 4), (2, 4), (1.5, 1.5)]
    limits[int(swapped)] = (1, 3)
    _set_base_space(maya_cmds, shape, limits)
    expected = (3, 1, 1.4, 3, 3, 1.6) if swapped else (1, 3, 1.4, 3, 3, 1.6)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "tip,body_width,band_width",
    (
        (1.6, 1, 0.05),
        (1.7, 1, 0.05),
        (3, 1, 0.05),
        (10, 1, 0.05),
        (3, 0.2, 0.12),
        (10, 1e-6, 0.05),
        (10, 1, 1e-6),
        (-0.4, 0.002, 0.1),
    ),
)
@pytest.mark.parametrize("reversed", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_wide_arrow_tip_keeps_the_exact_sharp_offset_intersection(
    maya_cmds,
    maya_om,
    new_scene,
    tip,
    body_width,
    band_width,
    reversed,
    swapped,
    filled,
):
    _load_bd_util_nodes(maya_cmds)
    minus = 0.5 if reversed else -0.5
    plus = -tip if reversed else tip
    direction = 1 if plus >= minus else -1
    joint = minus
    half_body = body_width / 2
    rear = minus - direction * half_body / 2
    half_band = band_width / 2
    extension = half_band * math.hypot(plus - joint, half_body) / half_body
    expected_tip = plus + math.copysign(extension, plus - joint)
    # 他の角のbevel範囲と離し、先端の交点そのものをAABBで検証する。
    reach = 4 * half_band
    positive = plus > joint
    assert (
        expected_tip > max(minus, joint) + reach
        if positive
        else expected_tip < min(minus, joint) - reach
    )
    shape = _controller(
        maya_cmds,
        "sharpWideArrow",
        "ArrowPlanar",
        shapeAxisSwap=swapped,
        shapeWide=True,
        shapeWideWidth=band_width,
        shapeFill=filled,
    )
    limits = [(2, 4), (2, 4), (4.5 - half_body, 4.5 + half_body)]
    axis = int(swapped)
    limits[axis] = (minus, plus)
    _set_base_space(maya_cmds, shape, limits)
    actual = _bounds(maya_om, shape)
    assert actual[axis + (3 if positive else 0)] == pytest.approx(
        expected_tip, rel=1e-8, abs=1e-9
    )
    assert all(math.isfinite(value) for value in actual)
    # 内側の穴が潰れても、先端と反対へ巨大な突起を生成しない。
    if positive:
        assert actual[axis] >= min(rear, joint) - reach - 1e-9
    else:
        assert actual[axis + 3] <= max(rear, joint) + reach + 1e-9
    assert actual[2] >= limits[2][0] - reach - 1e-9
    assert actual[5] <= limits[2][1] + reach + 1e-9
    normal = 1 - axis
    assert (actual[normal], actual[normal + 3]) == pytest.approx(
        (3, 3), abs=1e-9
    )


@pytest.mark.parametrize(
    "body_width,band_width,tip",
    (
        (0, 0.05, 3),
        (1, 0, 3),
        (0, 0, 3),
        (1, 0.05, -0.5),
        (1e-12, 0.05, -0.5),
        (1e-10, 0.05, -0.5),
        (1, 1e-13, 10),
    ),
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_degenerate_wide_arrow_tips_keep_finite_geometry(
    maya_cmds, maya_om, new_scene, body_width, band_width, tip, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "degenerateSharpArrow",
        "ArrowPlanar",
        shapeAxisSwap=swapped,
        shapeWide=True,
        shapeWideWidth=band_width,
        shapeFill=filled,
    )
    limits = [(-0.5, 0.5), (-0.5, 0.5), (-body_width / 2, body_width / 2)]
    limits[int(swapped)] = (-0.5, tip)
    _set_base_space(maya_cmds, shape, limits)
    actual = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in actual)
    body = _point_bounds(_body_points("ArrowPlanar", swapped, limits))
    if body_width == 1e-12 and tip == -0.5:
        # 母体全体が輪郭の同一点判定より小さい場合は描画要素を持たない。
        assert actual == pytest.approx((0,) * 6, abs=1e-12)
        return
    reach = 4 * band_width / 2 + 1e-9
    for axis in range(3):
        assert body[axis] - reach <= actual[axis] <= body[axis + 3] + reach
        assert body[axis] - reach <= actual[axis + 3] <= body[axis + 3] + reach


@pytest.mark.parametrize("swapped", (False, True))
def test_sharp_wide_arrow_tip_still_ignores_part_controls(
    maya_cmds, maya_om, new_scene, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "independentSharpTip",
        "ArrowPlanar",
        shapeAxisSwap=swapped,
        shapeWide=True,
    )
    limits = [(-0.5, 0.5), (-0.5, 0.5), (-0.5, 0.5)]
    limits[int(swapped)] = (-0.5, 10)
    _set_base_space(maya_cmds, shape, limits)
    expected = _bounds(maya_om, shape)
    for attribute, value in (
        ("shapePartOffset", -100),
        ("shapePartLengthScale", 0),
        ("shapePartWidthScale", 0),
        ("shapePartHeightScale", -8),
        ("shapePartSize", 0),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == value
