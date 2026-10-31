"""立体Wideの帯、開口、球面の交差色をViewport 2.0で確認する。"""

from __future__ import annotations

import math

import pytest

from test_controller_shape_viewport import (
    _aim_at_origin,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
    _rgb_near_world,
)

pytestmark = pytest.mark.maya


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _pick_world(cmds, panel, point):
    from maya import utils
    from maya.api import OpenMaya as om
    from maya.api import OpenMayaUI as omui

    cmds.select(clear=True)
    cmds.setFocus(panel)
    utils.processIdleEvents()
    view = omui.M3dView.getM3dViewFromModelPanel(panel)
    x, y, visible = view.worldToView(om.MPoint(*point))
    assert visible
    om.MGlobal.selectFromScreen(
        x - 2,
        y - 2,
        x + 2,
        y + 2,
        om.MGlobal.kReplaceList,
        om.MGlobal.kSurfaceSelectMethod,
    )
    return bool(cmds.ls(selection=True))


_DIAGONAL = 0.5 / math.sqrt(3)
_CIRCLE_DIAGONAL = 0.5 / math.sqrt(2)
_SURFACE_CASES = (
    ("Cube", (0, 0, 4), (0, 0, 0.5), (0.45, 0, 0.5)),
    ("ColorCube", (0, 0, 4), (0, 0, 0.5), (0.45, 0, 0.5)),
    ("ColorCornerCube", (0, 0, 4), (0, 0, 0.5), (0.45, 0, 0.5)),
    ("Octahedron", (4, 4, 4), (1 / 6, 1 / 6, 1 / 6), (0.24, 0.24, 0.02)),
    ("OctahedronArrow", (4, 4, 4), (1 / 6, 1 / 6, 1 / 6), (0.24, 0.24, 0.02)),
    (
        "Sphere",
        (4, 4, 4),
        (_DIAGONAL, _DIAGONAL, _DIAGONAL),
        (_CIRCLE_DIAGONAL, _CIRCLE_DIAGONAL, 0),
    ),
    (
        "ColorSphere",
        (4, 4, 4),
        (_DIAGONAL, _DIAGONAL, _DIAGONAL),
        (_CIRCLE_DIAGONAL, _CIRCLE_DIAGONAL, 0),
    ),
    ("Cylinder", (4, 0, 0), (0.5, 0, 0), (0.5, 0.45, 0)),
    ("Pyramid", (-4, 0, 0), (-0.5, 0.25, 0.1), (-0.5, 0.45, 0)),
    ("Cone", (-4, 0, 0), (-0.5, 0.2, 0.2), (-0.5, 0.45, 0)),
)


@pytest.mark.parametrize("preset,position,hole,band", _SURFACE_CASES)
def test_wide_solid_fills_only_the_band_and_leaves_the_hole_unselectable(
    maya_cmds, new_scene, tmp_path, preset, position, hole, band
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, _, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, position)
        pixels = _capture_view(panel, tmp_path / "surface_band.png")
        assert max(_rgb_near_world(panel, pixels, band)) > 180, (preset, band)
        assert _brightness_near_world(panel, pixels, hole) < 120, (
            preset,
            hole,
        )
        assert _pick_world(maya_cmds, panel, band), (
            preset,
            "帯面を選択できない",
        )
        assert not _pick_world(maya_cmds, panel, hole), (
            preset,
            "開口で選択された",
        )


@pytest.mark.parametrize(
    "preset,band,hole",
    (
        ("Cube", (0.45, 0, -0.5), (0, 0, -0.5)),
        (
            "Sphere",
            (0, 0.2, -math.sqrt(0.21)),
            (_DIAGONAL, _DIAGONAL, -_DIAGONAL),
        ),
    ),
)
def test_wide_surface_bands_are_visible_from_outside_and_inside(
    maya_cmds, new_scene, tmp_path, preset, band, hole
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, _, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (0, 0, -4))
        outside = _capture_view(panel, tmp_path / "outside_band.png")
        assert _brightness_near_world(panel, outside, band) > 600
        maya_cmds.setAttr(f"{camera_shape}.orthographic", False)
        maya_cmds.setAttr(f"{camera_shape}.focalLength", 8)
        maya_cmds.setAttr(f"{camera}.translate", 0, 0, 0)
        maya_cmds.setAttr(f"{camera}.rotate", 0, 0, 0)
        inside = _capture_view(panel, tmp_path / "inside_band.png")
        assert _brightness_near_world(panel, inside, band) > 600
        assert _brightness_near_world(panel, inside, hole) < 120


@pytest.mark.parametrize("preset", ("Sphere", "ColorSphere"))
def test_wide_sphere_draws_only_union_boundaries_without_center_or_join_lines(
    maya_cmds, new_scene, tmp_path, preset
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds, preset, shapeWide=True, shapeWideWidth=0.2, shapeFill=False
    ) as (_, _, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, 4, 0)
        maya_cmds.setAttr(f"{camera}.rotate", -90, 0, 0)
        pixels = _capture_view(panel, tmp_path / "sphere_union_outline.png")
        half_band = 0.5 * math.sin(0.2)
        outer = (half_band, math.sqrt(0.25 - half_band**2 - 0.3**2), 0.3)
        former_center = (0, 0.4, 0.3)
        hidden_join = (half_band, math.sqrt(0.25 - half_band**2), 0)
        assert max(_rgb_near_world(panel, pixels, outer)) > 180
        assert _brightness_near_world(panel, pixels, former_center) < 120
        assert _brightness_near_world(panel, pixels, hidden_join) < 120


def _assert_sphere_palette_matches_rgb_override(
    cmds, shape, panel, output, colored_pixels, samples
):
    actual = [
        _rgb_near_world(panel, colored_pixels, point) for point, _ in samples
    ]
    cmds.setAttr(f"{shape}.shape", 15)
    for index, ((point, expected), color) in enumerate(zip(samples, actual)):
        cmds.setAttr(f"{shape}.overrideColorRGB", *expected)
        reference = _capture_view(panel, output / f"rgb_reference_{index}.png")
        target = _rgb_near_world(panel, reference, point)
        assert max(target) > 100, (point, expected, target)
        assert color == pytest.approx(target, abs=4), (
            point,
            expected,
            color,
            target,
        )


def test_color_sphere_bands_use_axis_colors_and_mixed_overlap_fill(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "ColorSphere",
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 4, 4))
        pixels = _capture_view(panel, tmp_path / "sphere_axis_bands.png")
        samples = []
        for axis in range(3):
            point = [_CIRCLE_DIAGONAL] * 3
            point[axis] = 0
            color = [0.0] * 3
            color[axis] = 1.0
            samples.append((point, color))
        samples.extend(
            (
                ((0.5, 0, 0), (0, 0.75, 0.75)),
                ((0, 0.5, 0), (0.75, 0, 0.75)),
                ((0, 0, 0.5), (0.75, 0.75, 0)),
            )
        )
        _assert_sphere_palette_matches_rgb_override(
            maya_cmds, shape, panel, tmp_path, pixels, samples
        )


def test_color_sphere_three_band_overlap_uses_the_neutral_mix(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "ColorSphere",
        shapeWide=True,
        shapeWideWidth=0.8,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 4, 4))
        pixels = _capture_view(panel, tmp_path / "sphere_three_band_mix.png")
        samples = (
            ((_DIAGONAL, _DIAGONAL, _DIAGONAL), (0.75, 0.75, 0.75)),
            ((0.5, 0, 0), (0, 0.75, 0.75)),
            ((0, 0.5, 0), (0.75, 0, 0.75)),
            ((0, 0, 0.5), (0.75, 0.75, 0)),
        )
        _assert_sphere_palette_matches_rgb_override(
            maya_cmds, shape, panel, tmp_path, pixels, samples
        )


@pytest.mark.parametrize("mode", ("template_fill", "selected"))
def test_color_sphere_mixes_keep_template_fill_and_selection_priority(
    maya_cmds, new_scene, tmp_path, mode
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "ColorSphere",
        shapeWide=True,
        shapeWideWidth=0.8,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (transform, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 4, 4))
        if mode == "template_fill":
            maya_cmds.setAttr(f"{shape}.shapeTemplateFill", True)
        else:
            maya_cmds.modelEditor(
                panel, edit=True, selectionHiliteDisplay=True
            )
            maya_cmds.select(transform, replace=True)
        colored = _capture_view(panel, tmp_path / f"mixed_{mode}.png")
        # 混色も単色Sphereと同じ本体Template色または選択色へ上書きする。
        maya_cmds.setAttr(f"{shape}.shape", 15)
        plain = _capture_view(panel, tmp_path / f"plain_{mode}.png")
        for point in (
            (_DIAGONAL, _DIAGONAL, _DIAGONAL),
            (0.5, 0, 0),
            (0, 0.5, 0),
            (0, 0, 0.5),
        ):
            actual = _rgb_near_world(panel, colored, point)
            assert max(actual) > 50, (mode, point, actual)
            assert actual == _rgb_near_world(panel, plain, point), (
                mode,
                point,
                actual,
            )


@pytest.mark.parametrize("preset", ("Cube", "Sphere", "Cylinder"))
def test_zero_width_solid_has_normal_lines_without_body_fill(
    maya_cmds, new_scene, tmp_path, preset
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0,
        shapeFill=True,
        shapeFillTransparency=0,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 3, 4))
        wide = _capture_view(panel, tmp_path / "zero_width.png")
        maya_cmds.setAttr(f"{shape}.shapeWide", False)
        maya_cmds.setAttr(f"{shape}.shapeFill", False)
        ordinary = _capture_view(panel, tmp_path / "ordinary_lines.png")
        assert wide == ordinary


@pytest.mark.parametrize("preset", ("Sphere", "ColorSphere"))
def test_fully_covered_sphere_has_no_internal_lines_and_unfilled_fallback(
    maya_cmds, new_scene, tmp_path, preset
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.8,
        shapeFill=True,
        shapeFillTransparency=0.5,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 3, 4))
        with_lines = _capture_view(panel, tmp_path / "covered.png")
        maya_cmds.setAttr(f"{shape}.shapeLineTransparency", 1)
        without_lines = _capture_view(panel, tmp_path / "covered_no_lines.png")
        assert with_lines == without_lines, "全球面の帯に内部線が残っている"
        maya_cmds.setAttr(f"{shape}.shapeFill", False)
        maya_cmds.setAttr(f"{shape}.shapeLineTransparency", 0)
        fallback = _capture_view(panel, tmp_path / "fallback.png")
        maya_cmds.setAttr(f"{shape}.shapeWide", False)
        ordinary = _capture_view(panel, tmp_path / "normal_sphere.png")
        assert fallback == ordinary


@pytest.mark.parametrize("preset", ("Cylinder", "Cone"))
def test_wide_curved_sides_have_open_panels_between_rim_and_generator_bands(
    maya_cmds, new_scene, tmp_path, preset
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, _, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (0, 4, 4))
        side = (0, _CIRCLE_DIAGONAL, _CIRCLE_DIAGONAL)
        band = (0, math.sqrt(0.25 - 0.04**2), 0.04)
        if preset == "Cone":
            side = (0, 0.25 / math.sqrt(2), 0.25 / math.sqrt(2))
            band = (0, math.sqrt(0.25**2 - 0.02**2), 0.02)
        pixels = _capture_view(panel, tmp_path / "curved_side_opening.png")
        assert _brightness_near_world(panel, pixels, side) < 120
        assert _brightness_near_world(panel, pixels, band) > 600


@pytest.mark.parametrize("filled", (False, True))
def test_wide_cylinder_hides_original_generators_but_keeps_rims_and_band_edges(
    maya_cmds, new_scene, tmp_path, filled
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Cylinder",
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=filled,
        shapeFillTransparency=0.85,
    ) as (_, shape, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, 4, 0)
        maya_cmds.setAttr(f"{camera}.rotate", -90, 0, 0)
        pixels = _capture_view(
            panel, tmp_path / "cylinder_without_generators.png"
        )
        center = (0, 0.5, 0)
        brightness = _brightness_near_world(panel, pixels, center)
        if filled:
            assert 100 < brightness < 550, brightness
        else:
            assert brightness < 120, brightness
        edge = (0, 0.5 * math.cos(0.2), 0.5 * math.sin(0.2))
        assert _brightness_near_world(panel, pixels, edge) > 600
        assert _brightness_near_world(panel, pixels, (0.5, 0.4, 0.3)) > 600
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0)
        zero = _capture_view(panel, tmp_path / "cylinder_zero_width_lines.png")
        assert _brightness_near_world(panel, zero, center) > 600


def test_wide_gear_fills_both_outline_bands_without_filling_the_gap_or_center(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Gear",
        shapeWide=True,
        shapeWideWidth=0.05,
        shapeFill=True,
        shapeFillTransparency=0,
        shapeLineTransparency=1,
    ) as (_, _, camera, _, panel):
        maya_cmds.setAttr(f"{camera}.translate", 0, 4, 0)
        maya_cmds.setAttr(f"{camera}.rotate", -90, 0, 0)
        pixels = _capture_view(panel, tmp_path / "gear_outline_bands.png")
        for point in ((0.1375, 0, 0), (0.49, 0, 0)):
            assert _brightness_near_world(panel, pixels, point) > 600, point
            assert _pick_world(maya_cmds, panel, point), point
        for point in ((0.25, 0, 0), (0, 0, 0)):
            assert _brightness_near_world(panel, pixels, point) < 120, point
            assert not _pick_world(maya_cmds, panel, point), point


@pytest.mark.parametrize("preset", ("Sphere", "ColorSphere", "Cube"))
@pytest.mark.parametrize("transparency", (0, 0.5))
@pytest.mark.parametrize("draw_on_top", (False, True))
def test_fully_transparent_lines_do_not_cut_wide_fill(
    maya_cmds, new_scene, tmp_path, preset, transparency, draw_on_top
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeFill=True,
        shapeFillTransparency=transparency,
        shapeLineTransparency=1,
        shapeDrawOnTop=draw_on_top,
    ) as (_, shape, camera, _, panel):
        _aim_at_origin(maya_cmds, camera, (4, 4, 4))
        normal = _capture_view(panel, tmp_path / "transparent_lines.png")
        maya_cmds.setAttr(f"{shape}.shapeLineWidth", 5)
        assert normal == _capture_view(
            panel, tmp_path / "wide_transparent_lines.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
        assert normal == _capture_view(
            panel, tmp_path / "template_transparent_lines.png"
        )
