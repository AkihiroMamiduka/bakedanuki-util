# coding: utf-8
from __future__ import annotations

import math

import pytest

from controller_shape_cases import set_preset
from test_controller_shape_viewport import (
    _aim_at_origin,
    _assert_template_line_partition,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
    _pick_world,
    _rgb_near_world,
)

pytestmark = pytest.mark.maya


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _profile_camera(cmds, camera, camera_shape, section, width):
    cmds.setAttr(
        f"{camera}.translate", *((0, 0, 4) if section == 2 else (0, 4, 0))
    )
    cmds.setAttr(
        f"{camera}.rotate", *((0, 0, 0) if section == 2 else (-90, 0, 0))
    )
    cmds.setAttr(f"{camera_shape}.orthographicWidth", width)


def _profile_point(along, radius, section):
    return (along, radius, 0) if section == 2 else (along, 0, radius)


def _bright_pixels(panel, pixels):
    from maya.api import OpenMayaUI as omui

    width = omui.M3dView.getM3dViewFromModelPanel(panel).portWidth()
    return {
        (index // 4 % width, index // 4 // width)
        for index in range(0, len(pixels), 4)
        if sum(pixels[index : index + 3]) > 200
    }


def _joint_options(swapped, deformed):
    axis = "2nd" if swapped else "1st"
    options = {
        "shapeAxisSwap": swapped,
        f"shapeBaseSpace{axis}AxisMinus": 1.2,
        f"shapeBaseSpace{axis}AxisPlus": 1.2,
    }
    if deformed:
        component = "1st" if swapped else "2nd"
        options[f"shapeBaseSpace{axis}AxisPlusScale{component}Axis"] = 1.6
    return options


def _joint_point(point, swapped=False, deformed=False):
    x, y, z = point
    if deformed:
        # R-=.5、R+=.65を含む完成外端[-1.7,1.85]で面倍率を補間する。
        y *= 1 + 0.6 * (x + 1.7) / 3.55
    return (y, x, -z) if swapped else (x, y, z)


def _circle_point(along, angle, swapped=False, deformed=False):
    return _joint_point(
        (along, 0.5 * math.cos(angle), 0.5 * math.sin(angle)),
        swapped,
        deformed,
    )


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("deformed", (False, True))
def test_capsule_cross_sections_follow_both_cap_joints_and_leave_the_middle_clear(
    maya_cmds, new_scene, tmp_path, wide, swapped, deformed
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapeFill=wide,
        shapeFillTransparency=0,
        shapeLineTransparency=1 if wide else 0,
        **_joint_options(swapped, deformed),
    ) as (_, _, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _joint_point((3, 4, 4), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.2)
        image = _capture_view(panel, tmp_path / "capsule_joint_sections.png")
        for angle in (math.pi / 4, 3 * math.pi / 8):
            for along in (-1.2, 1.2):
                point = _circle_point(along, angle, swapped, deformed)
                assert _brightness_near_world(panel, image, point) > 600, (
                    "接合円または接合部の帯がない",
                    wide,
                    swapped,
                    deformed,
                    point,
                )
            middle = _circle_point(0, angle, swapped, deformed)
            assert _brightness_near_world(panel, image, middle) < 120, (
                "廃止した中央円または中央の帯が残る",
                wide,
                swapped,
                deformed,
                middle,
            )


@pytest.mark.parametrize(
    "swapped,deformed", ((False, False), (True, False), (True, True))
)
def test_capsule_joint_circles_keep_the_circle_template_phase_and_selection(
    maya_cmds, new_scene, tmp_path, swapped, deformed
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds, "Capsule", **_joint_options(swapped, deformed)
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _joint_point((3, 4, 4), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.2)
        _assert_template_line_partition(
            maya_cmds,
            shape,
            panel,
            tmp_path,
            tuple(
                _circle_point(along, math.pi / 16, swapped, deformed)
                for along in (-1.2, 1.2)
            ),
            tuple(
                _circle_point(along, math.pi / 4, swapped, deformed)
                for along in (-1.2, 1.2)
            ),
            name="capsule_joint_circles",
            rate=0.5,
        )


@pytest.mark.parametrize("swapped", (False, True))
def test_zero_cylinder_capsule_does_not_draw_transparent_joint_circles_twice(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeAxisSwap=swapped,
        shapeLineTransparency=0.5,
        **{
            f"shapeBaseSpace{axis}AxisMinus": 0,
            f"shapeBaseSpace{axis}AxisPlus": 0,
        },
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _joint_point((3, 4, 4), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        capsule = _capture_view(
            panel, tmp_path / "transparent_zero_capsule.png"
        )
        set_preset(maya_cmds, shape, "Sphere")
        maya_cmds.setAttr(f"{shape}.shapeAxisSwap", swapped)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", 0.5)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", 0.5)
        sphere = _capture_view(panel, tmp_path / "transparent_sphere.png")
        for angle in (math.pi / 4, 3 * math.pi / 8):
            point = _circle_point(0, angle, swapped)
            reference = _rgb_near_world(panel, sphere, point)
            assert sum(reference) > 100
            assert _rgb_near_world(panel, capsule, point) == pytest.approx(
                reference, abs=8
            ), (
                "中心間0で接合円が二重描画され、Sphereより線が濃くなる",
                swapped,
                point,
            )


@pytest.mark.parametrize("length", (0, 0.6, 1, 2.4))
@pytest.mark.parametrize("section", (2, 3))
@pytest.mark.parametrize(
    "radius2,radius3", ((0.35, 0.7), (0.3, 0.3), (0.75, 0.75))
)
def test_capsule_wire_keeps_round_caps_and_independent_cross_sections(
    maya_cmds, new_scene, tmp_path, length, section, radius2, radius3
):
    _require_viewport(maya_cmds)
    cap_radius = (radius2 + radius3) * 0.5
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeBaseSpace1stAxisMinus=length * 0.5,
        shapeBaseSpace1stAxisPlus=length * 0.5,
        shapeBaseSpace2ndAxisMinus=radius2,
        shapeBaseSpace2ndAxisPlus=radius2,
        shapeBaseSpace3rdAxisMinus=radius3,
        shapeBaseSpace3rdAxisPlus=radius3,
    ) as (_, shape, camera, camera_shape, panel):
        assert maya_cmds.getAttr(f"{shape}.shape") == 20
        _profile_camera(
            maya_cmds,
            camera,
            camera_shape,
            section,
            max(length + 2 * cap_radius, 2 * max(radius2, radius3)) + 0.8,
        )
        image = _capture_view(
            panel, tmp_path / f"capsule_profile_{section}.png"
        )
        transverse = radius2 if section == 2 else radius3
        cap_center = length * 0.5
        for sign in (-1, 1):
            for angle in (
                0,
                math.pi / 8,
                math.pi / 4,
                3 * math.pi / 8,
                math.pi / 2,
            ):
                along = sign * (cap_center + cap_radius * math.cos(angle))
                radius = transverse * math.sin(angle)
                for side in (-1, 1):
                    point = _profile_point(along, side * radius, section)
                    assert _brightness_near_world(panel, image, point) > 600, (
                        length,
                        section,
                        point,
                    )
        # 横2半径の平均を主軸半径とし、同径なら縮小・拡大後も半球を保つ。
        assert (
            _brightness_near_world(
                panel, image, _profile_point(0, transverse, section)
            )
            > 600
        )
        assert (
            _brightness_near_world(
                panel,
                image,
                _profile_point(cap_center + cap_radius + 0.1, 0, section),
            )
            < 120
        )
        assert (
            _brightness_near_world(
                panel, image, _profile_point(0, transverse + 0.1, section)
            )
            < 120
        )


@pytest.mark.parametrize("filled", (False, True))
def test_zero_cylinder_capsule_matches_the_sphere_silhouette(
    maya_cmds, new_scene, tmp_path, filled
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeBaseSpace1stAxisMinus=0,
        shapeBaseSpace1stAxisPlus=0,
        shapeFill=filled,
        shapeFillTransparency=0,
        shapeLineTransparency=1 if filled else 0,
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.6)
        capsule = _bright_pixels(
            panel, _capture_view(panel, tmp_path / "zero_cylinder_capsule.png")
        )
        set_preset(maya_cmds, shape, "Sphere")
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", 0.5)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 0.5)
        sphere = _bright_pixels(
            panel, _capture_view(panel, tmp_path / "reference_sphere.png")
        )
        assert capsule and sphere
        for actual, expected in ((capsule, sphere), (sphere, capsule)):
            # 面メッシュの緯度軸による微小な輪郭差は2pxまで許容する。
            expanded = {
                (x + dx, y + dy)
                for x, y in expected
                for dx in range(-2, 3)
                for dy in range(-2, 3)
            }
            assert len(actual - expanded) / len(actual) < 0.02


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("template", (False, True))
def test_capsule_fill_switch_keeps_wireframe_and_template_selection(
    maya_cmds, new_scene, tmp_path, wide, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeBaseSpace1stAxisMinus=1.2,
        shapeBaseSpace1stAxisPlus=1.2,
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeTemplateLine=template,
        shapeTemplateFill=template,
        shapeTemplateLineRate=1,
    ) as (_, shape, camera, camera_shape, panel):
        _profile_camera(maya_cmds, camera, camera_shape, 3, 4.2)
        shaded = _capture_view(panel, tmp_path / "capsule_shaded.png")
        maya_cmds.modelEditor(panel, edit=True, displayAppearance="wireframe")
        wireframe = _capture_view(
            panel, tmp_path / "capsule_wireframe_filled.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeFill", False)
        lines = _capture_view(panel, tmp_path / "capsule_wireframe_lines.png")
        assert wireframe == lines
        assert shaded != wireframe
        boundary = (0.6, 0, 0.5)
        assert _brightness_near_world(panel, lines, boundary) > 100
        assert _pick_world(maya_cmds, panel, boundary) == (not template)


@pytest.mark.parametrize("part_shape", (0, 1))
@pytest.mark.parametrize(
    "length,wide,template", ((0.6, False, False), (2.4, True, True))
)
def test_capsule_arrow_guides_connect_the_actual_tips_at_both_ends(
    maya_cmds, new_scene, tmp_path, part_shape, length, wide, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeBaseSpace1stAxisMinus=length * 0.5,
        shapeBaseSpace1stAxisPlus=length * 0.5,
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapePart=True,
        shapePartShape=part_shape,
        shapePartSize=1.4,
        shapePartLengthScale=1.6,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapeGuideLineTemplate=template,
        shapeDrawOnTop=True,
    ) as (_, shape, camera, camera_shape, panel):
        _profile_camera(maya_cmds, camera, camera_shape, 3, length + 3.2)
        for placement in (0, 1):
            maya_cmds.setAttr(f"{shape}.shapePartType", placement)
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
            before = _capture_view(
                panel, tmp_path / f"capsule_arrow_off_{placement}.png"
            )
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
            after = _capture_view(
                panel, tmp_path / f"capsule_arrow_on_{placement}.png"
            )
            tip = length * 0.5 + 0.5 + 0.45 + 0.125 * 1.4 * 1.6
            for sign in (-1, 1):
                gap = (sign * (length * 0.5 + 0.72), 0, 0)
                if placement == 1 or sign == 1:
                    previous = _brightness_near_world(panel, before, gap)
                    assert _brightness_near_world(panel, after, gap) > max(
                        100, previous + 40
                    )
                    sample = (sign * (tip - 0.1), 0, 0)
                    assert _brightness_near_world(panel, after, sample) > 100
                else:
                    assert _brightness_near_world(panel, after, gap) < 120
                assert (
                    _brightness_near_world(
                        panel, after, (sign * (tip + 0.1), 0, 0)
                    )
                    < 120
                )
            gap = (length * 0.5 + 0.72, 0, 0)
            assert _pick_world(maya_cmds, panel, gap) == (not template)
            maya_cmds.select(clear=True)


def test_capsule_large_inward_offset_keeps_the_guide_through_the_opposite_cap(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Capsule",
        shapeBaseSpace1stAxisMinus=1.5,
        shapeBaseSpace1stAxisPlus=1.5,
        shapePart=True,
        shapePartShape=0,
        shapePartType=0,
        shapePartOffset=-4,
        shapeDrawOnTop=True,
    ) as (_, shape, camera, camera_shape, panel):
        # 斜視にして、2断面の外周線と主軸Guideの投影を分離する。
        _aim_at_origin(maya_cmds, camera, (3, 4, 4))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.8)
        before = _capture_view(
            panel, tmp_path / "capsule_inward_offset_off.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "capsule_inward_offset_on.png")
        # 根元+2から肩-2へ戻り、先端-1.875へ向かう全区間を保つ。
        for along in (-1.97, -1.5, -0.8, 0.6, 1, 1.55):
            point = (along, 0, 0)
            previous = _brightness_near_world(panel, before, point)
            assert _brightness_near_world(panel, after, point) > max(
                100, previous + 40
            ), (point, previous)
        for along in (-2.15, 2.15):
            assert _brightness_near_world(panel, after, (along, 0, 0)) < 120


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("sign", (1, -1))
def test_capsule_keeps_cap_centers_and_uses_independent_axial_cap_radii(
    maya_cmds, new_scene, tmp_path, swapped, sign
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    lateral = "1st" if swapped else "2nd"
    options = {
        "shapeAxisSwap": swapped,
        f"shapeBaseSpace{axis}AxisMinus": 1,
        f"shapeBaseSpace{axis}AxisPlus": 1.2,
        f"shapeBaseSpace{lateral}AxisMinus": 0.4,
        f"shapeBaseSpace{lateral}AxisPlus": 0.4,
        "shapeBaseSpace3rdAxisMinus": 0.6,
        "shapeBaseSpace3rdAxisPlus": 0.6,
        f"shapeBaseSpace{axis}AxisMinusScale{lateral}Axis": sign * 2,
        f"shapeBaseSpace{axis}AxisMinusScale3rdAxis": 0.5,
        f"shapeBaseSpace{axis}AxisPlusScale{lateral}Axis": sign * 0.5,
        f"shapeBaseSpace{axis}AxisPlusScale3rdAxis": 2,
    }
    with _drawing_view(maya_cmds, "Capsule", **options) as (
        _,
        _,
        camera,
        camera_shape,
        panel,
    ):
        maya_cmds.setAttr(
            f"{camera}.translate", *_joint_point((0.1, 4, 0), swapped)
        )
        maya_cmds.setAttr(
            f"{camera}.rotate", *((0, 90, 0) if swapped else (-90, 0, 0))
        )
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 4.2)
        image = _capture_view(
            panel, tmp_path / "capsule_independent_axial_cap_radii.png"
        )
        # R-=(.4*2+.6*.5)/2=.55、R+=(.4*.5+.6*2)/2=.7。
        for point in (
            (-1.55, 0, 0),
            (1.9, 0, 0),
            (-1, 0, 0.15),
            (1.2, 0, 0.15),
        ):
            assert (
                _brightness_near_world(
                    panel, image, _joint_point(point, swapped)
                )
                > 600
            ), (swapped, sign, point)
        for along in (-1.67, 2.02):
            assert (
                _brightness_near_world(
                    panel, image, _joint_point((along, 0, 0), swapped)
                )
                < 120
            )
