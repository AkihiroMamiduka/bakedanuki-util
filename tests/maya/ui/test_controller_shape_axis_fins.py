"""直線を保つ面変形と、軸を示すFin・GuideをViewport 2.0で確認する。"""

from __future__ import annotations

import math

import pytest

from test_controller_shape_viewport import (
    _aim_at_origin,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
)

pytestmark = pytest.mark.maya


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _point(point, swapped):
    x, y, z = point
    return (y, x, -z) if swapped else point


def _camera(cmds, camera, camera_shape, swapped, planar=False):
    target = _point((0.35, 0.3, 0), swapped)
    if planar:
        cmds.setAttr(
            f"{camera}.translate", *((4, 0, 0) if swapped else (0, 4, 0))
        )
        cmds.setAttr(
            f"{camera}.rotate", *((0, 90, 0) if swapped else (-90, 0, 0))
        )
    else:
        cmds.setAttr(f"{camera}.translate", target[0], target[1], 4)
        cmds.setAttr(f"{camera}.rotate", 0, 0, 0)
    cmds.setAttr(
        f"{camera_shape}.orthographicWidth", 3.4 if not planar else 2.5
    )


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("template", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_triangle_face_scale_keeps_edges_straight_with_fill_and_template(
    maya_cmds, new_scene, tmp_path, swapped, template, filled
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFillTransparency=0,
        shapeTemplateLine=template,
        shapeTemplateLineRate=0.5,
        **{f"shapeBaseSpace{axis}AxisPlusScale3rdAxis": 2},
    ) as (_, _, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped, planar=True)
        image = _capture_view(panel, tmp_path / "straight_triangle.png")
        for fraction in (0.2, 0.5, 0.8):
            along = -0.37 + 0.87 * fraction
            transverse = 0.565 * (1 - fraction)
            for sign in (-1, 1):
                point = _point((along, 0, sign * transverse), swapped)
                assert _brightness_near_world(panel, image, point) > 150
        for sign in (-1, 1):
            curved = _point((0.065, 0, sign * 0.39125), swapped)
            assert _brightness_near_world(panel, image, curved) < 120


@pytest.mark.parametrize("swapped", (False, True))
def test_triangle_wide_band_follows_the_straight_deformed_edge(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeAxisSwap=swapped,
        shapeWide=True,
        shapeWideWidth=0.08,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
        **{f"shapeBaseSpace{axis}AxisPlusScale3rdAxis": 2},
    ) as (_, _, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped, planar=True)
        image = _capture_view(panel, tmp_path / "straight_triangle_wide.png")
        for sign in (-1, 1):
            assert (
                _brightness_near_world(
                    panel, image, _point((0.065, 0, sign * 0.2825), swapped)
                )
                > 600
            )
            assert (
                _brightness_near_world(
                    panel, image, _point((0.065, 0, sign * 0.39125), swapped)
                )
                < 120
            )


@pytest.mark.parametrize(
    "preset",
    ("SquareArrowAxial", "DiamondArrowAxial", "CircleArrowAxial"),
)
@pytest.mark.parametrize("swapped", (False, True))
def test_axial_guides_start_at_the_minus_base_center(
    maya_cmds, new_scene, tmp_path, preset, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        preset,
        shapeAxisSwap=swapped,
        shapeDrawOnTop=True,
        **{
            f"shapeBaseSpace{axis}AxisMinus": 0.5,
            f"shapeBaseSpace{axis}AxisPlus": 1.5,
        },
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _point((4, 3, 5), swapped))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.4)
        plain = _capture_view(panel, tmp_path / "axial_plain.png")
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        guided = _capture_view(panel, tmp_path / "axial_minus_guides.png")
        sample = _point((-0.5, 0.23, 0), swapped)
        assert _brightness_near_world(panel, plain, sample) < 180
        assert _brightness_near_world(panel, guided, sample) > 600
        assert (
            _brightness_near_world(
                panel, guided, _point((0.5, 0.12, 0), swapped)
            )
            < 180
        )


@pytest.mark.parametrize("swapped", (False, True))
def test_arrow_planar_fin_rises_from_the_minus_notch(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        "ArrowPlanar",
        shapeAxisSwap=swapped,
        shapeFin=True,
        shapeFinHeight=0.6,
        **{
            f"shapeBaseSpace{axis}AxisMinus": 0.5,
            f"shapeBaseSpace{axis}AxisPlus": 1.5,
        },
    ) as (_, _, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped)
        image = _capture_view(panel, tmp_path / "fin_minus_notch.png")
        assert (
            _brightness_near_world(
                panel, image, _point((-0.5, 0.3, 0), swapped)
            )
            > 600
        )
        assert (
            _brightness_near_world(
                panel, image, _point((-0.75, 0.3, 0), swapped)
            )
            < 120
        )


@pytest.mark.parametrize(
    "preset",
    (
        "SquareArrowAxial",
        "DiamondArrowAxial",
        "CircleArrowAxial",
        "ArrowSpatial",
        "SquareArrowSpatial",
    ),
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("deformed", (False, True))
def test_standard_arrow_fin_top_remains_parallel_to_the_main_axis(
    maya_cmds, new_scene, tmp_path, preset, swapped, deformed
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    lateral = "1st" if swapped else "2nd"
    options = {
        f"shapeBaseSpace{axis}AxisMinus": 0.5,
        f"shapeBaseSpace{axis}AxisPlus": 1.5,
    }
    if deformed:
        options[f"shapeBaseSpace{axis}AxisMinusScale{lateral}Axis"] = 1.6
    with _drawing_view(
        maya_cmds,
        preset,
        shapeAxisSwap=swapped,
        shapeFinHeight=0.25,
        shapeDrawOnTop=True,
        **options,
    ) as (_, shape, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped)
        plain = _capture_view(panel, tmp_path / "standard_fin_off.png")
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        shown = _capture_view(panel, tmp_path / "standard_fin_on.png")
        for along in (-0.1, 0.2):
            sample = _point((along, 0.25, 0), swapped)
            assert _brightness_near_world(panel, plain, sample) < 180
            assert _brightness_near_world(panel, shown, sample) > 600


@pytest.mark.parametrize("swapped", (False, True))
def test_arrow_spatial_keeps_the_downward_standard_fin_edge(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    with _drawing_view(
        maya_cmds,
        "ArrowSpatial",
        shapeAxisSwap=swapped,
        shapeFinHeight=0.1,
        **{
            f"shapeBaseSpace{axis}AxisMinus": 0.5,
            f"shapeBaseSpace{axis}AxisPlus": 1.5,
        },
    ) as (_, shape, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped)
        sample = _point((-0.75, 0.18, 0), swapped)
        plain = _capture_view(panel, tmp_path / "downward_fin_off.png")
        assert _brightness_near_world(panel, plain, sample) < 180
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        shown = _capture_view(panel, tmp_path / "downward_fin_on.png")
        assert _brightness_near_world(panel, shown, sample) > 600


@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_minus_face_scale_leaves_the_plus_cap_unchanged(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    lateral = "1st" if swapped else "2nd"
    with _drawing_view(maya_cmds, "Capsule", shapeAxisSwap=swapped) as (
        _,
        shape,
        camera,
        camera_shape,
        panel,
    ):
        _camera(maya_cmds, camera, camera_shape, swapped, planar=True)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.5)
        before = _capture_view(panel, tmp_path / "capsule_equal_caps.png")
        for component in (lateral, "3rd"):
            maya_cmds.setAttr(
                f"{shape}.shapeBaseSpace{axis}AxisMinusScale{component}Axis", 2
            )
        after = _capture_view(panel, tmp_path / "capsule_larger_minus_cap.png")
        for angle in (math.pi / 8, math.pi / 4, 3 * math.pi / 8):
            plus = _point(
                (0.5 + 0.5 * math.cos(angle), 0, 0.5 * math.sin(angle)),
                swapped,
            )
            assert _brightness_near_world(panel, before, plus) > 600
            assert _brightness_near_world(panel, after, plus) > 600
        minus = _point((-0.5 - math.sqrt(0.5), 0, math.sqrt(0.5)), swapped)
        assert _brightness_near_world(panel, before, minus) < 120
        assert _brightness_near_world(panel, after, minus) > 600


@pytest.mark.parametrize("preset", ("CrossLine3Axis", "ColorCrossLine3Axis"))
@pytest.mark.parametrize("swapped", (False, True))
def test_wide_three_axis_standard_fin_keeps_its_center_height_and_parallel_top(
    maya_cmds, new_scene, tmp_path, preset, swapped
):
    _require_viewport(maya_cmds)
    axis = "2nd" if swapped else "1st"
    lateral = "1st" if swapped else "2nd"
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeAxisSwap=swapped,
        shapeFinHeight=1.2,
        **{f"shapeBaseSpace{axis}AxisPlusScale{lateral}Axis": 2},
    ) as (_, shape, camera, camera_shape, panel):
        _camera(maya_cmds, camera, camera_shape, swapped)
        before = _capture_view(panel, tmp_path / "wide_cross_without_fin.png")
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        after = _capture_view(panel, tmp_path / "wide_cross_parallel_fin.png")
        for along in (-0.3, 0.3):
            sample = _point((along, 1.2, 0), swapped)
            assert _brightness_near_world(panel, before, sample) < 180
            assert _brightness_near_world(panel, after, sample) > 600
        assert (
            _brightness_near_world(
                panel, after, _point((0.3, 1.4, 0), swapped)
            )
            < 180
        )


def test_fin_height_and_width_control_the_visible_geometry_independently(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds, "Cube", shapeFinHeight=0.4, shapeFinWidthScale=0.7
    ) as (_, shape, camera, camera_shape, panel):
        assert not maya_cmds.attributeQuery(
            "shapeFinSize", node=shape, exists=True
        )
        assert not maya_cmds.attributeQuery("sfns", node=shape, exists=True)
        maya_cmds.setAttr(f"{camera}.translate", 0, 0.6, 4)
        maya_cmds.setAttr(f"{camera}.rotate", 0, 0, 0)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.5)
        body = _capture_view(panel, tmp_path / "fin_controls_body.png")
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        initial = _capture_view(panel, tmp_path / "fin_controls_initial.png")
        for point in ((0.1, 0.9, 0), (-0.35, 0.7, 0)):
            assert _brightness_near_world(panel, initial, point) > 600
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.8)
        taller = _capture_view(panel, tmp_path / "fin_controls_taller.png")
        for point in ((0.1, 1.3, 0), (-0.35, 0.7, 0)):
            assert _brightness_near_world(panel, taller, point) > 600
        assert _brightness_near_world(panel, taller, (0.1, 0.9, 0)) < 120
        maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 1.4)
        wider = _capture_view(panel, tmp_path / "fin_controls_wider.png")
        for point in ((0.55, 1.3, 0), (0.7, 0.9, 0)):
            assert _brightness_near_world(panel, wider, point) > 600
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
        assert _capture_view(panel, tmp_path / "fin_controls_zero.png") == body


def test_default_shape_bounds_frame_the_visible_position_and_offset_line(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(maya_cmds, "Cube", shapeTranslateX=3) as (
        transform,
        shape,
        camera,
        camera_shape,
        panel,
    ):
        assert maya_cmds.getAttr(f"{shape}.boundsMode") == 0
        maya_cmds.setAttr(f"{camera}.translate", 0, 0, 4)
        maya_cmds.setAttr(f"{camera}.rotate", 0, 0, 0)
        maya_cmds.select(transform, replace=True)
        maya_cmds.viewFit(camera_shape, animate=False, noChildren=True)
        assert maya_cmds.xform(
            camera, query=True, translation=True, worldSpace=True
        )[0] == pytest.approx(3, abs=1e-6)
        _capture_view(panel, tmp_path / "default_shape_focus.png")
        maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
        maya_cmds.viewFit(camera_shape, animate=False, noChildren=True)
        assert maya_cmds.xform(
            camera, query=True, translation=True, worldSpace=True
        )[0] == pytest.approx(1.75, abs=1e-6)
        _capture_view(panel, tmp_path / "default_offset_line_focus.png")
        maya_cmds.setAttr(f"{shape}.boundsMode", 1)
        maya_cmds.viewFit(camera_shape, animate=False, noChildren=True)
        assert maya_cmds.xform(
            camera, query=True, translation=True, worldSpace=True
        )[0] == pytest.approx(0, abs=1e-6)
