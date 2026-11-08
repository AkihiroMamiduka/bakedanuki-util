# coding: utf-8
from __future__ import annotations

import math

import pytest

from controller_shape_cases import set_preset
from test_controller_shape_viewport import (
    _aim_at_origin,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
    _pick_world,
)

pytestmark = pytest.mark.maya

ARROW_BODIES = (
    "DiamondArrowPlanar",
    "SquareArrowSpatial",
    "CircleArrowSpatial",
)
ARROW_ENUMS = {
    "ArrowPlanar": 21,
    "SquareArrowPlanar": 22,
    "DiamondArrowPlanar": 23,
    "CircleArrowPlanar": 24,
    "SquareArrowAxial": 25,
    "DiamondArrowAxial": 26,
    "CircleArrowAxial": 27,
    "ArrowSpatial": 28,
    "SquareArrowSpatial": 29,
    "DiamondArrowSpatial": 30,
    "CircleArrowSpatial": 31,
}
PLANAR_ARROWS = (
    "ArrowPlanar",
    "SquareArrowPlanar",
    "DiamondArrowPlanar",
    "CircleArrowPlanar",
)
SPATIAL_ARROWS = (
    "ArrowSpatial",
    "SquareArrowSpatial",
    "DiamondArrowSpatial",
    "CircleArrowSpatial",
)
CENTERED_ARROWS = (*PLANAR_ARROWS, *SPATIAL_ARROWS)
NEW_ARROW_SHAPES = (
    "SquareArrowPlanar",
    "CircleArrowPlanar",
    "DiamondArrowAxial",
    "ArrowSpatial",
)


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _point(point, swapped=False, reverse=False, deformed=False):
    x, y, z = point
    if deformed:
        z *= 1 + 0.6 * (x + 0.5) / 2.5
    if reverse:
        x = -x
    return (y, x, -z) if swapped else (x, y, z)


def _main_options(plus, swapped=False, reverse=False, deformed=False):
    axis = "2nd" if swapped else "1st"
    sign = -1 if reverse else 1
    options = {
        "shapeAxisSwap": swapped,
        f"shapeBaseSpace{axis}AxisMinus": 0,
        f"shapeBaseSpace{axis}AxisPlus": plus * sign,
    }
    if deformed:
        options[f"shapeBaseSpace{axis}AxisPlusScale3rdAxis"] = 1.6
    return options


def _profile_camera(cmds, camera, camera_shape, swapped, reverse=False):
    target = _point((0.75, 0, 0), swapped, reverse)
    offset = (4, 0, 0) if swapped else (0, 4, 0)
    cmds.setAttr(
        f"{camera}.translate", *(a + b for a, b in zip(target, offset))
    )
    cmds.setAttr(f"{camera}.rotate", *((0, 90, 0) if swapped else (-90, 0, 0)))
    cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.3)


def _drawing_mask(panel, pixels):
    from maya.api import OpenMayaUI as omui

    width = omui.M3dView.getM3dViewFromModelPanel(panel).portWidth()
    return {
        (index // 4 % width, index // 4 // width)
        for index in range(0, len(pixels), 4)
        if sum(pixels[index : index + 3]) > 200
    }


def _guide_axis_clearance(panel, point, swapped):
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    origin_x, origin_y, _ = view.worldToView(om.MPoint())
    point_x, point_y, _ = view.worldToView(om.MPoint(*point))
    distances = []
    for axis in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        axis_x, axis_y, _ = view.worldToView(om.MPoint(*_point(axis, swapped)))
        dx, dy = axis_x - origin_x, axis_y - origin_y
        distances.append(
            abs(dx * (point_y - origin_y) - dy * (point_x - origin_x))
            / math.hypot(dx, dy)
        )
    return min(distances)


def _assert_same_outline(panel, actual, expected):
    actual_mask = _drawing_mask(panel, actual)
    expected_mask = _drawing_mask(panel, expected)
    assert actual_mask and expected_mask
    for source, reference in (
        (actual_mask, expected_mask),
        (expected_mask, actual_mask),
    ):
        expanded = {
            (x + dx, y + dy)
            for x, y in reference
            for dx in range(-2, 3)
            for dy in range(-2, 3)
        }
        assert len(source - expanded) / len(source) < 0.02


@pytest.mark.parametrize("preset", CENTERED_ARROWS)
def test_public_default_minus_places_arrow_center_on_the_negative_half_axis(
    maya_cmds, new_scene, tmp_path, preset
):
    _require_viewport(maya_cmds)
    with _drawing_view(maya_cmds, preset, shapeBaseSpace1stAxisMinus=0.5) as (
        _,
        shape,
        camera,
        camera_shape,
        panel,
    ):
        assert maya_cmds.getAttr(f"{shape}.shapeBaseSpace1stAxisMinus") == 0.5
        assert maya_cmds.getAttr(f"{shape}.shapeBaseSpace1stAxisPlus") == 0.5
        maya_cmds.setAttr(f"{camera}.translate", -0.25, 4, 0)
        maya_cmds.setAttr(f"{camera}.rotate", -90, 0, 0)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.3)
        image = _capture_view(
            panel, tmp_path / "public_default_arrow_center.png"
        )
        arrow = preset in ("ArrowPlanar", "ArrowSpatial")
        rear = (-0.75, 0, 0.25) if arrow else (-1, 0, 0)
        for point in (rear, (-0.5, 0, 0.5), (0.5, 0, 0)):
            assert _brightness_near_world(panel, image, point) > 600, (
                preset,
                point,
            )
        for point in (((-0.87 if arrow else -1.12), 0, 0), (0.62, 0, 0)):
            assert _brightness_near_world(panel, image, point) < 120


@pytest.mark.parametrize("preset", CENTERED_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("center,sign", ((-0.4, 1), (0.7, -1)))
def test_arrow_axial_radii_follow_width_without_using_face_scales(
    maya_cmds, new_scene, tmp_path, preset, swapped, center, sign
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    lateral = "1st" if swapped else "2nd"
    planar = preset in PLANAR_ARROWS
    arrow = preset in ("ArrowPlanar", "ArrowSpatial")
    radius = 0.6 if planar else 0.5
    radius_minus = radius * 0.5 if arrow else radius
    radius_plus = radius * 1.5 if arrow else radius
    rear, front = center - radius_minus, center + radius_plus
    options = {
        "shapeAxisSwap": swapped,
        f"shapeBaseSpace{axis}AxisMinus": -center,
        f"shapeBaseSpace{axis}AxisPlus": center + 0.1,
        f"shapeBaseSpace{lateral}AxisMinus": 0.4,
        f"shapeBaseSpace{lateral}AxisPlus": 0.4,
        "shapeBaseSpace3rdAxisMinus": 0.6,
        "shapeBaseSpace3rdAxisPlus": 0.6,
        f"shapeBaseSpace{axis}AxisMinusScale{lateral}Axis": sign * 2,
        f"shapeBaseSpace{axis}AxisMinusScale3rdAxis": 0.5,
        f"shapeBaseSpace{axis}AxisPlusScale{lateral}Axis": sign * 0.5,
        f"shapeBaseSpace{axis}AxisPlusScale3rdAxis": 2,
    }
    with _drawing_view(maya_cmds, preset, **options) as (
        _,
        _,
        camera,
        camera_shape,
        panel,
    ):
        _profile_camera(maya_cmds, camera, camera_shape, swapped)
        maya_cmds.setAttr(
            f"{camera}.translate",
            *_point(((rear + front) * 0.5, 4, 0), swapped),
        )
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.2)
        image = _capture_view(
            panel, tmp_path / "independent_arrow_axial_radii.png"
        )
        # 主軸の母体寸法は横端座標だけで決め、面倍率は後段の変形へ留める。
        for along in (rear, front):
            point = _point(
                (along, 0, 0.15 if arrow and along == rear else 0), swapped
            )
            assert _brightness_near_world(panel, image, point) > 600, (
                preset,
                swapped,
                center,
                sign,
                point,
            )
        for along in (rear - 0.12, front + 0.12):
            assert (
                _brightness_near_world(
                    panel, image, _point((along, 0, 0), swapped)
                )
                < 120
            )


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_sphere_arrow_keeps_the_center_circle_without_a_tangent_circle_or_band(
    maya_cmds, new_scene, tmp_path, wide, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "CircleArrowSpatial",
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapeFill=wide,
        shapeFillTransparency=0,
        shapeLineTransparency=1 if wide else 0,
        **_main_options(2, swapped),
    ) as (_, shape, camera, camera_shape, panel):
        _profile_camera(maya_cmds, camera, camera_shape, swapped)
        center_circle = _point((0, 0, 0.25), swapped)
        tangent_circle = _point((0.125, 0, 0.25), swapped)
        for template in (False, True):
            maya_cmds.setAttr(f"{shape}.shapeTemplateLine", template)
            maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", 1)
            image = _capture_view(
                panel,
                tmp_path / f"sphere_arrow_without_join_circle_{template}.png",
            )
            assert _brightness_near_world(panel, image, center_circle) > (
                100 if template else 600
            )
            assert (
                _brightness_near_world(panel, image, tangent_circle) < 120
            ), (wide, swapped, template)
            if not wide:
                assert _pick_world(maya_cmds, panel, center_circle) == (
                    not template
                )
                maya_cmds.select(clear=True)


@pytest.mark.parametrize(
    "preset,mother,plus",
    (
        ("DiamondArrowPlanar", "Diamond", 0.5),
        ("SquareArrowSpatial", "Cube", 0.5),
        ("CircleArrowSpatial", "Sphere", 0.5),
        ("SquareArrowSpatial", "Cube", 0),
        ("CircleArrowSpatial", "Sphere", 0),
        ("SquareArrowPlanar", "Square", 0.5),
        ("SquareArrowPlanar", "Square", 0),
        ("CircleArrowPlanar", "Circle", 0.5),
        ("CircleArrowPlanar", "Circle", 0),
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_default_and_short_arrow_bodies_keep_the_complete_mother_shape(
    maya_cmds, new_scene, tmp_path, preset, mother, plus, filled
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeBaseSpace1stAxisPlus=plus,
        shapeFill=filled,
        shapeFillTransparency=0,
        shapeLineTransparency=1 if filled else 0,
    ) as (_, shape, camera, camera_shape, panel):
        assert maya_cmds.getAttr(f"{shape}.shape") == ARROW_ENUMS[preset]
        if preset in PLANAR_ARROWS:
            maya_cmds.setAttr(f"{camera}.translate", 0, 4, 0)
            maya_cmds.setAttr(f"{camera}.rotate", -90, 0, 0)
        else:
            _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        arrow = _capture_view(panel, tmp_path / "unextended_arrow.png")
        set_preset(maya_cmds, shape, mother)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", 0.5)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 0.5)
        reference = _capture_view(panel, tmp_path / "mother_shape.png")
        # Sphereの緯度軸による微小なメッシュ差を許容して、線または外殻全体を比べる。
        _assert_same_outline(panel, arrow, reference)


@pytest.mark.parametrize("preset", (*ARROW_BODIES, *NEW_ARROW_SHAPES))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("reverse", (False, True))
def test_long_arrow_profiles_keep_the_fixed_body_and_reach_the_new_tip(
    maya_cmds, new_scene, tmp_path, preset, swapped, reverse
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds, preset, **_main_options(2, swapped, reverse)
    ) as (_, _, camera, camera_shape, panel):
        _profile_camera(maya_cmds, camera, camera_shape, swapped, reverse)
        image = _capture_view(panel, tmp_path / "long_arrow_profile.png")
        if preset == "DiamondArrowPlanar":
            points = ((-0.25, 0, 0.25), (0, 0, 0.5), (1, 0, 0.25), (2, 0, 0))
            outside = (1, 0, 0.37)
        elif preset in ("SquareArrowSpatial", "SquareArrowPlanar"):
            points = (
                (-0.5, 0, 0.25),
                (-0.25, 0, 0.5),
                (0.5, 0, 0.5),
                (1.25, 0, 0.25),
                (2, 0, 0),
            )
            outside = (1.25, 0, 0.37)
        elif preset in ("CircleArrowSpatial", "CircleArrowPlanar"):
            tangent = 0.5**2 / 2
            radius = math.sqrt(0.5**2 - tangent**2)
            points = (
                (-math.sqrt(0.125), 0, math.sqrt(0.125)),
                (0, 0, 0.5),
                (tangent, 0, radius),
                ((tangent + 2) * 0.5, 0, radius * 0.5),
                (2, 0, 0),
            )
            outside = ((tangent + 2) * 0.5, 0, radius * 0.5 + 0.12)
        elif preset == "ArrowSpatial":
            points = (
                (-0.25, 0, 0.25),
                (-0.125, 0, 0.125),
                (0, 0, 0.5),
                (1, 0, 0.25),
                (2, 0, 0),
            )
            outside = (1, 0, 0.37)
        else:
            points = ((0, 0, 0.25), (0, 0, 0.5), (1, 0, 0.25), (2, 0, 0))
            outside = (1, 0, 0.37)
        for point in points:
            sample = _point(point, swapped, reverse)
            assert _brightness_near_world(panel, image, sample) > 600, (
                preset,
                swapped,
                reverse,
                sample,
            )
        rear_limit = (
            0
            if preset == "DiamondArrowAxial"
            else -0.25 if preset == "ArrowSpatial" else -0.5
        )
        for point in (outside, (2.1, 0, 0), (rear_limit - 0.12, 0, 0)):
            sample = _point(point, swapped, reverse)
            assert _brightness_near_world(panel, image, sample) < 120, (
                preset,
                swapped,
                reverse,
                sample,
            )


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
def test_long_solid_arrows_have_only_an_outward_outer_shell(
    maya_cmds, new_scene, tmp_path, preset, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
        **_main_options(2, swapped),
    ) as (_, _, camera, camera_shape, panel):
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        _aim_at_origin(maya_cmds, camera, _point((3, 2, 4), swapped))
        outside = _capture_view(panel, tmp_path / "solid_arrow_outside.png")
        for along, front in ((0, True), (1, False)):
            maya_cmds.setAttr(
                f"{camera}.translate", *_point((along, 0, 0), swapped)
            )
            if swapped:
                maya_cmds.setAttr(
                    f"{camera}.rotate", *((90, 0, 0) if front else (-90, 0, 0))
                )
            else:
                maya_cmds.setAttr(
                    f"{camera}.rotate", 0, -90 if front else 90, 0
                )
            inside = _capture_view(
                panel, tmp_path / f"solid_arrow_inside_{along}.png"
            )
            background = inside[:4]
            assert all(
                inside[index : index + 4] == background
                for index in range(0, len(inside), 4)
            ), (
                "本体または錐の内側から裏面・内部の蓋が見える",
                preset,
                swapped,
                along,
            )
            assert any(
                outside[index : index + 4] != background
                for index in range(0, len(outside), 4)
            )


def _local_part_camera(cmds, camera, camera_shape, point, direction):
    cmds.setAttr(
        f"{camera}.translate",
        *(value + axis * 0.3 for value, axis in zip(point, direction)),
    )
    axis = next(index for index, value in enumerate(direction) if value)
    sign = direction[axis]
    rotations = (
        (0, sign * 90, 0),
        (-sign * 90, 0, 0),
        (0, 0 if sign > 0 else 180, 0),
    )
    cmds.setAttr(f"{camera}.rotate", *rotations[axis])
    cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.35)
    cmds.setAttr(f"{camera_shape}.farClipPlane", 0.5)


@pytest.mark.parametrize(
    "preset", ("SquareArrowPlanar", "CircleArrowPlanar", "ArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
def test_new_planar_and_crossed_arrow_faces_are_visible_from_both_sides(
    maya_cmds, new_scene, tmp_path, preset, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
        **_main_options(2, swapped),
    ) as (_, shape, camera, camera_shape, panel):
        planes = (((0, 1, 0), (0.9, 0, 0.1)),)
        if preset == "ArrowSpatial":
            planes += (((0, 0, 1), (0.9, 0.1, 0)),)
        for index, (normal, sample) in enumerate(planes):
            for sign in (-1, 1):
                direction = _point(
                    tuple(value * sign for value in normal), swapped
                )
                center = _point((0.75, 0, 0), swapped)
                _local_part_camera(
                    maya_cmds, camera, camera_shape, center, direction
                )
                maya_cmds.setAttr(
                    f"{camera}.translate",
                    *(
                        value + axis * 4
                        for value, axis in zip(center, direction)
                    ),
                )
                maya_cmds.setAttr(f"{camera_shape}.farClipPlane", 1000)
                maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.3)
                filled = _capture_view(
                    panel, tmp_path / f"arrow_plane_fill_{index}_{sign}.png"
                )
                maya_cmds.setAttr(f"{shape}.shapeFill", False)
                empty = _capture_view(
                    panel, tmp_path / f"arrow_plane_empty_{index}_{sign}.png"
                )
                point = _point(sample, swapped)
                assert _brightness_near_world(panel, filled, point) > 600, (
                    preset,
                    swapped,
                    index,
                    sign,
                )
                assert _brightness_near_world(panel, empty, point) < 120
                maya_cmds.setAttr(f"{shape}.shapeFill", True)


@pytest.mark.parametrize(
    "wide,swapped,deformed,template",
    ((False, False, False, False), (True, True, True, True)),
)
def test_diamond_arrow_axial_keeps_body_guides_and_fin_without_part_tip_extension(
    maya_cmds, new_scene, tmp_path, wide, swapped, deformed, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "DiamondArrowAxial",
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeTemplateLine=template,
        shapeTemplateLineRate=1,
        shapeGuideLineTemplate=template,
        shapePart=True,
        shapePartShape=0,
        shapePartSize=2,
        shapePartWidthScale=1.5,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        **_main_options(2, swapped, deformed=deformed),
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _point((3, 4, 4), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.2)
        maya_cmds.setAttr(f"{camera}.translate", *_point((3.8, 4, 4), swapped))
        before = _capture_view(
            panel, tmp_path / "diamond_axial_without_guides.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(
            panel, tmp_path / "diamond_axial_with_guides.png"
        )
        candidates = tuple(
            _point((along, 0, 0), swapped)
            for along in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7)
        )
        visible = tuple(
            point
            for point in candidates
            if _brightness_near_world(panel, before, point) < 120
        )
        assert len(visible) >= 2
        for point in visible:
            previous = _brightness_near_world(panel, before, point)
            assert _brightness_near_world(panel, after, point) > max(
                100, previous + 40
            )
        assert (
            _brightness_near_world(panel, after, _point((2.2, 0, 0), swapped))
            < 120
        )
        assert _pick_world(maya_cmds, panel, visible[0]) == (not template)
        maya_cmds.select(clear=True)
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.3)
        with_fin = _capture_view(
            panel, tmp_path / "diamond_axial_with_fin.png"
        )
        assert with_fin != after
        maya_cmds.setAttr(f"{shape}.shapeFin", False)
        assert (
            _capture_view(panel, tmp_path / "diamond_axial_fin_removed.png")
            == after
        )


@pytest.mark.parametrize("preset", (*CENTERED_ARROWS, "DiamondArrowAxial"))
@pytest.mark.parametrize("swapped", (False, True))
def test_arrow_parts_keep_the_four_sides_and_rear_fixed_while_the_front_follows(
    maya_cmds, new_scene, tmp_path, preset, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
        shapePartShape=6,
        shapePartType=1,
        shapePartSize=2,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        **_main_options(0.5, swapped),
    ) as (_, shape, camera, camera_shape, panel):
        axis = "2nd" if swapped else "1st"
        for plus in (0.5, 2):
            maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", plus)
            arrow = preset in ("ArrowPlanar", "ArrowSpatial")
            axial = preset == "DiamondArrowAxial"
            front = plus if axial else max(plus, 0.75 if arrow else 0.5)
            sites = [((front, 0, 0), (1, 0, 0))]
            if not arrow and not axial:
                sites.append(((-0.5, 0, 0), (-1, 0, 0)))
            if not axial:
                sites.extend(
                    (((0, 0, 0.5), (0, 0, 1)), ((0, 0, -0.5), (0, 0, -1)))
                )
            if preset in SPATIAL_ARROWS:
                sites.extend(
                    (((0, 0.5, 0), (0, 1, 0)), ((0, -0.5, 0), (0, -1, 0)))
                )
            for index, (site, along) in enumerate(sites):
                center = _point(
                    tuple(
                        value + direction * 0.45
                        for value, direction in zip(site, along)
                    ),
                    swapped,
                )
                _local_part_camera(
                    maya_cmds,
                    camera,
                    camera_shape,
                    center,
                    _point(along, swapped),
                )
                maya_cmds.setAttr(f"{shape}.shapePart", False)
                before = _capture_view(
                    panel, tmp_path / f"part_absent_{plus}_{index}.png"
                )
                maya_cmds.setAttr(f"{shape}.shapePart", True)
                after = _capture_view(
                    panel, tmp_path / f"part_present_{plus}_{index}.png"
                )
                assert _brightness_near_world(panel, before, center) < 120
                assert _brightness_near_world(panel, after, center) > 600, (
                    preset,
                    swapped,
                    plus,
                    site,
                )


@pytest.mark.parametrize("preset", CENTERED_ARROWS)
@pytest.mark.parametrize(
    "wide,swapped,deformed,template",
    ((False, False, False, False), (True, True, True, True)),
)
def test_arrow_guides_use_the_body_center_with_wide_cage_template_and_fin(
    maya_cmds, new_scene, tmp_path, preset, wide, swapped, deformed, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeTemplateLine=template,
        shapeTemplateLineRate=1,
        shapeGuideLineTemplate=template,
        shapePart=True,
        shapePartShape=0,
        shapePartSize=2,
        shapePartWidthScale=1.5,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapePartType=1,
        shapeDrawOnTop=True,
        **_main_options(2, swapped, deformed=deformed),
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _point((3, 4, 4), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 5.8)
        before = _capture_view(panel, tmp_path / "arrow_without_guides.png")
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "arrow_with_guides.png")
        for sign in (-1, 1):
            candidates = tuple(
                _point((0, 0, sign * distance), swapped, deformed=deformed)
                for distance in (0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36)
            )
            visible = tuple(
                point
                for point in candidates
                if _brightness_near_world(panel, before, point) < 120
            )
            assert len(visible) >= 2, (
                "本体内Guideを輪郭と分離した検証点が足りない",
                preset,
                sign,
            )
            for sample in visible:
                previous = _brightness_near_world(panel, before, sample)
                assert _brightness_near_world(panel, after, sample) > max(
                    100, previous + 40
                ), (preset, sample, previous)
        sample = _point((2.2, 0, 0), swapped)
        previous = _brightness_near_world(panel, before, sample)
        assert _brightness_near_world(panel, after, sample) > max(
            100, previous + 40
        ), (preset, sample, previous)
        # 公開両端の中点(1,0,0)から側方根元への誤線を、正しい各軸Guideから8px離す。
        rear_depth = 0.25 if preset in ("ArrowPlanar", "ArrowSpatial") else 0.5
        side_root = (
            0.5 * (1 + 0.6 * rear_depth / (2 + rear_depth))
            if deformed
            else 0.5
        )
        candidates = tuple(
            _point((1 - parameter, 0, side_root * parameter), swapped)
            for parameter in (0.3, 0.35, 0.4, 0.45, 0.5)
        )
        wrong_points = tuple(
            point
            for point in candidates
            if _guide_axis_clearance(panel, point, swapped) >= 8
            and _brightness_near_world(panel, before, point) < 120
        )
        assert len(wrong_points) >= 2, (
            "誤原点線を輪郭・正しいGuideから分離した検証点が足りない",
            preset,
        )
        for sample in wrong_points:
            assert _brightness_near_world(panel, after, sample) < 120, (
                preset,
                sample,
            )
        sample = _point((2.2, 0, 0), swapped)
        assert _pick_world(maya_cmds, panel, sample) == (not template)
        maya_cmds.select(clear=True)
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.3)
        with_fin = _capture_view(panel, tmp_path / "arrow_with_fin.png")
        assert with_fin != after
        maya_cmds.setAttr(f"{shape}.shapeFin", False)
        assert (
            _capture_view(panel, tmp_path / "arrow_fin_removed.png") == after
        )


@pytest.mark.parametrize("swapped", (False, True))
def test_anisotropic_arrow_spatial_wide_planes_join_the_front_cube_without_a_gap(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    lateral = "1st" if swapped else "2nd"
    options = {
        **_main_options(2, swapped),
        f"shapeBaseSpace{lateral}AxisMinus": 1,
        f"shapeBaseSpace{lateral}AxisPlus": 1,
        "shapeBaseSpace3rdAxisMinus": 0.5,
        "shapeBaseSpace3rdAxisPlus": 0.5,
    }
    with _drawing_view(
        maya_cmds,
        "ArrowSpatial",
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
        shapePart=False,
        shapePartShape=6,
        shapePartType=0,
        shapePartSize=1,
        shapePartOffset=0,
        **options,
    ) as (_, shape, camera, camera_shape, panel):
        maya_cmds.setAttr(
            f"{camera}.translate", *_point((2.31, 0, 4), swapped)
        )
        maya_cmds.setAttr(f"{camera}.rotate", 0, 180 if swapped else 0, 0)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 0.36)
        before = _capture_view(
            panel, tmp_path / "anisotropic_front_without_cube.png"
        )
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        after = _capture_view(
            panel, tmp_path / "anisotropic_front_with_cube.png"
        )
        outer_xy = 0.1 * math.hypot(2, 1)
        outer_xz = 0.1 * math.hypot(2, 0.5) / 0.5
        cube_back = 2 + outer_xz - 0.05
        # XZ面は投影でY=0へ潰れるため、XY面上の少し外れた点で接続面を調べる。
        samples = tuple(
            _point(point, swapped)
            for sign in (-1, 1)
            for point in (
                (2.30, sign * 0.01, 0),
                (cube_back - 0.02, sign * 0.005, 0),
                (cube_back + 0.02, sign * 0.005, 0),
            )
        )
        assert 2 + outer_xy < 2.30 < cube_back
        for point in samples:
            assert _brightness_near_world(panel, before, point) < 120, (
                swapped,
                point,
            )
            assert _brightness_near_world(panel, after, point) > 600, (
                "狭いXY面の帯と共通前Partの間に隙間がある",
                swapped,
                point,
            )
        maya_cmds.setAttr(
            f"{camera}.translate", *_point((2.31, 4, 0), swapped)
        )
        maya_cmds.setAttr(
            f"{camera}.rotate", *((0, 90, 0) if swapped else (-90, 0, 0))
        )
        wider_with_part = _capture_view(
            panel, tmp_path / "anisotropic_xz_with_cube.png"
        )
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        wider_body = _capture_view(
            panel, tmp_path / "anisotropic_xz_without_cube.png"
        )
        for sign in (-1, 1):
            for point in (
                (2.30, 0, sign * 0.01),
                (cube_back - 0.02, 0, sign * 0.005),
            ):
                sample = _point(point, swapped)
                assert _brightness_near_world(panel, wider_body, sample) > 600
                assert (
                    _brightness_near_world(panel, wider_with_part, sample)
                    > 600
                ), (
                    "元から共通前端へ届くXZ面の帯が接合補正で欠ける",
                    swapped,
                    sample,
                )
