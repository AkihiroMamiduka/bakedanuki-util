# coding: utf-8
from __future__ import annotations

import math

import pytest

import bd_util as bdu

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

BASE_LIMITS = ((1.0, 3.0), (-2.0, 4.0), (4.0, 7.0))
AXES = ("1st", "2nd", "3rd")


def _set_base_space(cmds, shape, limits=BASE_LIMITS):
    """物理端座標を公開属性の符号付き方向距離へ変換して設定する。"""
    for axis, (minus, plus) in zip(AXES, limits):
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", -minus)
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", plus)


def _mapped_bounds(bounds, limits=BASE_LIMITS):
    return tuple(
        minus + (bounds[start + axis] + 0.5) * (plus - minus)
        for start in (0, 3)
        for axis, (minus, plus) in enumerate(limits)
    )


@pytest.mark.parametrize("preset", ("Cube", "ColorCube"))
@pytest.mark.parametrize("swapped", (False, True))
def test_shared_signed_distance_driver_expands_shape_and_custom_bounds_symmetrically(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "sharedDirectionalDistance", preset, shapeAxisSwap=swapped
    )
    driver = maya_cmds.createNode("network", name="directionalDistanceDriver")
    maya_cmds.addAttr(
        driver,
        longName="distance",
        attributeType="doubleLinear",
        defaultValue=0.5,
        keyable=True,
    )
    for axis, custom_axis in zip(AXES, "XYZ"):
        for side in ("Minus", "Plus"):
            maya_cmds.connectAttr(
                f"{driver}.distance", f"{shape}.shapeBaseSpace{axis}Axis{side}"
            )
            maya_cmds.connectAttr(
                f"{driver}.distance",
                f"{shape}.customBoundsBaseSpace{custom_axis}{side}",
            )
    for value in (0.5, 2, -0.4, 0):
        maya_cmds.setAttr(f"{driver}.distance", value)
        expected = (-abs(value),) * 3 + (abs(value),) * 3
        for mode in (0, 2):
            maya_cmds.setAttr(f"{shape}.boundsMode", mode)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert (
            maya_cmds.getAttr(f"{shape}.shapeBaseSpace1stAxisMinus") == value
        )
        assert (
            maya_cmds.getAttr(f"{shape}.customBoundsBaseSpaceXMinus") == value
        )


@pytest.mark.parametrize(
    "preset",
    tuple(
        name
        for name in SHAPE_NAMES
        if name
        not in ("ArrowPlanar", "DiamondArrowPlanar", "DiamondArrowSpatial")
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_base_space_maps_all_body_shapes_without_normalizing_their_bounds(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "mappedBody",
        preset,
        shapeWide=False,
        shapeWideWidth=0.2,
        shapeFill=filled,
    )
    original = _bounds(maya_om, shape)
    for axis in AXES:
        for side, expected in (("Minus", 0.5), ("Plus", 0.5)):
            attribute = f"shapeBaseSpace{axis}Axis{side}"
            assert (
                maya_cmds.getAttr(f"{shape}.{attribute}", type=True)
                == "doubleLinear"
            )
            assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
                expected
            )
    _set_base_space(maya_cmds, shape)
    if preset == "Capsule":
        expected = (-1.25, -2, 4, 5.25, 4, 7)
    elif preset in ("SquareArrowSpatial", "CircleArrowSpatial"):
        # Minus=1を中心に横半径3と1.5の平均R=2.25を保ち、長さ2では錐を出さない。
        expected = (-1.25, -2, 4, 3.25, 4, 7)
    elif preset in ("SquareArrowPlanar", "CircleArrowPlanar"):
        # 平面の主軸半径は第3軸半幅1.5だけを使い、法線方向は中心1へ置く。
        expected = (-0.5, 1, 4, 3, 1, 7)
    elif preset == "ArrowSpatial":
        # 横平均半径2.25に対し、後部深さR/2・前母体長1.5Rを保つ。
        expected = (-0.125, -2, 4, 4.375, 4, 7)
    else:
        expected = _mapped_bounds(original)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_base_space_endpoints_are_coordinates_and_move_the_original_center(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "translatedCube", "Cube")
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", -1)
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1, -0.5, -0.5, 2, 0.5, 0.5), abs=1e-9
    )


@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_base_space_moves_line_part_pivots_without_scaling_local_dimensions(
    maya_cmds, maya_om, new_scene, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedPart",
        "Line",
        shapePart=True,
        shapePartShape=part,
        shapePartSize=1.3,
        shapePartLengthScale=1.7,
        shapePartWidthScale=1.8,
        shapePartHeightScale=0.8,
        shapePartOffset=1.0,
        shapeFill=filled,
    )
    original = _bounds(maya_om, shape)
    _set_base_space(maya_cmds, shape)
    expected = (
        1,
        original[1] + 1,
        original[2] + 5.5,
        original[3] + 2.5,
        original[4] + 1,
        original[5] + 5.5,
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("Cube", "Sphere", "Circle"))
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_attached_parts_keep_public_dimensions_on_a_narrow_nonuniform_body(
    maya_cmds, maya_om, new_scene, preset, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "attachedDimensions", preset, shapeFill=filled
    )
    _set_base_space(maya_cmds, shape, ((1, 3), (0.99, 1.01), (5.485, 5.515)))
    body = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    maya_cmds.setAttr(f"{shape}.shapePartShape", part)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 1.3)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 1.7)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.8)
    maya_cmds.setAttr(f"{shape}.shapePartHeightScale", 0.8)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 4)
    length, width, height = 1.3 * 1.7, 1.3 * 1.8, 1.3 * 0.8
    if part <= 1:
        extent = 0.125 * length
        half_width = (0.075 if preset == "Sphere" else 0.072) * width
        low_y = 1
        high_y = 1 + (0.0625 * height if part == 1 else 0)
    else:
        extent = (0.1 if part in (2, 9, 10) else 0.05) * length
        half_width = 0.05 * width
        low_y = 1 - (0.05 * height if part >= 6 else 0)
        high_y = 1 + (0.05 * height if part >= 6 else 0)
    expected = (
        body[0],
        min(body[1], low_y),
        min(body[2], 5.5 - half_width),
        7 + extent,
        max(body[4], high_y),
        max(body[5], 5.5 + half_width),
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "preset,first_axis",
    (("Cube", 0), ("Sphere", 0), ("ColorSphere", 4), ("ColorSphere", 5)),
)
@pytest.mark.parametrize(
    "primary,other", ((1.5, 0.25), (0, 0.5), (1, 0), (-1, -0.5))
)
def test_at_ends_offsets_and_size_scales_use_mapped_faces_and_color_primary_axis(
    maya_cmds, maya_om, new_scene, preset, first_axis, primary, other
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "mappedEnds",
        preset,
        shapePart=True,
        shapePartShape=6,
        shapePartType=1,
        shapePartSize=2,
        shapePartPrimarySizeScale=primary,
        shapePartOtherSizeScale=other,
        shapePartOffset=0.3,
        shape1stAxis=first_axis,
    )
    _set_base_space(maya_cmds, shape)
    expected = [1, -2, 4, 3, 4, 7]
    for axis in range(3):
        for sign in (-1, 1):
            representative = axis == first_axis // 2 and sign == (
                1 if first_axis % 2 == 0 else -1
            )
            size_scale = primary if representative else other
            if size_scale == 0:
                continue
            index = axis + (3 if sign > 0 else 0)
            expected[index] += sign * (0.3 + 0.1 * abs(size_scale))
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "preset", ("Square", "Circle", "WideLine", "WideCrossLine3Axis")
)
@pytest.mark.parametrize("filled", (False, True))
def test_guide_lines_follow_the_moved_body_center_and_keep_part_fin_bounds(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "movedGuideCenter",
        preset,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartSize=1.7,
        shapePartPrimarySizeScale=1.4,
        shapePartOtherSizeScale=0.6,
        shapePartOffset=0.13,
        shapeFin=True,
        shapeFinHeight=0.7,
        shapeFill=filled,
    )
    _set_base_space(maya_cmds, shape, ((1, 3), (2, 4), (5, 7)))
    expected = _bounds(maya_om, shape)
    assert all(value > 0 for value in expected)
    maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("Line", "LineSwapped", "Cube"))
@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_fin_uses_mapped_body_roots_and_width_but_preserves_its_height(
    maya_cmds, maya_om, new_scene, preset, fin_type, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedFinHeight",
        preset,
        shapeFin=True,
        shapeFinType=fin_type,
        shapeFinHeight=0.7,
        shapeFill=filled,
    )
    _set_base_space(maya_cmds, shape)
    expected = {
        "Line": (1, 1, 5.5, 3, 1.7, 5.5),
        "LineSwapped": (2, -2, 5.5, 2.7, 4, 5.5),
        "Cube": (1, -2, 4, 3, 4.7, 7),
    }[preset]
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("swapped", (False, True))
def test_base_space_axes_keep_their_meaning_after_axis_swap(
    maya_cmds, maya_om, new_scene, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "swappedSpace", "Square", shapeAxisSwap=swapped
    )
    _set_base_space(maya_cmds, shape)
    expected = (2, -2, 4, 2, 4, 7) if swapped else (1, 1, 4, 3, 1, 7)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("Cube", "ColorCube"))
def test_base_space_precedes_selected_axes_and_keeps_color_body_axes_fixed(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "selectedFrame", preset)
    _set_base_space(maya_cmds, shape)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)
    expected = (
        (1, -2, 4, 3, 4, 7) if preset == "ColorCube" else (-7, -2, 1, -4, 4, 3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_common_size_and_transform_still_scale_body_parts_and_base_center(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "commonTransform", "Line", shapePart=True, shapePartShape=6
    )
    _set_base_space(maya_cmds, shape)
    original = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeSize", 2)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 3)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 10, 20, 30)
    expected = tuple(
        value * 6 + (30, 60, 90)[index % 3]
        for index, value in enumerate(original)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("ArcRadial", "ArcAxial"))
def test_arc_part_length_is_measured_on_the_new_circle_and_width_is_preserved(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "largerArc",
        preset,
        shapePart=True,
        shapePartShape=3,
        shapePartLengthScale=4,
    )
    _set_base_space(maya_cmds, shape, ((-1, 1), (-1, 1), (-1, 1)))
    box = _bounds(maya_om, shape)
    if preset == "ArcAxial":
        assert box == pytest.approx(
            (-math.sin(0.2), -0.05, -1, 1, 0.05, 1), abs=1e-7
        )
    else:
        assert box == pytest.approx(
            (-1.05 * math.sin(0.2), 0, -1.05, 1, 0, 1), abs=1e-7
        )


@pytest.mark.parametrize("preset", ("ArcAxial", "CrossArcAxial"))
def test_axial_parts_keep_their_local_width_on_an_ellipse(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "ellipticArc",
        preset,
        shapePart=True,
        shapePartShape=3,
    )
    _set_base_space(maya_cmds, shape)
    box = _bounds(maya_om, shape)
    if preset == "ArcAxial":
        assert (box[1], box[4]) == pytest.approx((0.95, 1.05), abs=1e-9)
    assert all(math.isfinite(value) for value in box)
    maya_cmds.setAttr(f"{shape}.shapeFill", True)
    assert _bounds(maya_om, shape) == pytest.approx(box, abs=1e-9)


def test_base_space_updates_offset_line_shape_centered_and_custom_bounds(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "baseBounds", "Line")
    _set_base_space(maya_cmds, shape)
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx((0, 0, 0, 3, 1, 5.5))
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    assert _bounds(maya_om, shape) == pytest.approx((-1, 0, 0, 1, 0, 0))
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)


def test_base_space_distances_follow_scene_units_without_changing_geometry(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        shape = _controller(maya_cmds, "unitSpace", "Cube")
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", -10)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 20)
        expected = (1, -0.5, -0.5, 2, 0.5, 0.5)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        maya_cmds.currentUnit(linear="cm")
        assert maya_cmds.getAttr(
            f"{shape}.shapeBaseSpace1stAxisMinus"
        ) == pytest.approx(-1)
        assert maya_cmds.getAttr(
            f"{shape}.shapeBaseSpace1stAxisPlus"
        ) == pytest.approx(2)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_base_space_api_history_connections_animation_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "animatedSpace", "Cube")
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    node = bd_nodes.existing(shape)
    original = _bounds(maya_om, shape)
    node.shapeBaseSpace1stAxisMinus.set(-1)
    node.shapeBaseSpace1stAxisPlus.set(2)
    mod.do_it_dg()
    expected = (1, -0.5, -0.5, 2, 0.5, 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, shape) == pytest.approx(original)
    mod.redo_it()
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    driver = maya_cmds.createNode("network", name="baseSpaceDriver")
    for side in ("minus", "plus"):
        maya_cmds.addAttr(
            driver, longName=side, attributeType="doubleLinear", keyable=True
        )
    node.shapeBaseSpace1stAxisMinus.connect_from(f"{driver}.minus")
    node.shapeBaseSpace1stAxisPlus.connect_from(f"{driver}.plus")
    mod.do_it_dg()
    values = ((1, 2), (-2, 1), (3, 5))
    for time, (minus, plus) in enumerate(values, 1):
        maya_cmds.setKeyframe(f"{driver}.minus", time=time, value=-minus)
        maya_cmds.setKeyframe(f"{driver}.plus", time=time, value=plus)
    boxes = []
    for time, (minus, plus) in enumerate(values, 1):
        maya_cmds.currentTime(time)
        box = (minus, -0.5, -0.5, plus, 0.5, 0.5)
        assert _bounds(maya_om, shape) == pytest.approx(box)
        boxes.append(box)
    scene = tmp_path / "base_space.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    for time, expected in enumerate(boxes, 1):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    for side in ("Minus", "Plus"):
        assert maya_cmds.isConnected(
            f"{driver}.{side.lower()}", f"{shape}.shapeBaseSpace1stAxis{side}"
        )
