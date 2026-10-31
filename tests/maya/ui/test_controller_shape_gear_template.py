"""Gear外周の実長に沿うTemplate区間をViewport 2.0で確認する。"""

from __future__ import annotations

import math

import pytest

from test_controller_shape_viewport import (
    _assert_template_line_partition,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
    _pick_world,
)

pytestmark = pytest.mark.maya


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _rotate_gear(point, tooth):
    angle = tooth * math.pi / 4
    x, y, z = point
    return (
        x * math.cos(angle) - z * math.sin(angle),
        y,
        x * math.sin(angle) + z * math.cos(angle),
    )


_TIP = (0.5, 0, 0)
_NEXT_ROOT = _rotate_gear((0.35, 0, -0.09), 1)
_VALLEY = tuple(
    (first + last) / 2 for first, last in zip((0.35, 0, 0.09), _NEXT_ROOT)
)
_PITCH_PATH = (
    _TIP,
    (0.5, 0, 0.0675),
    (0.35, 0, 0.09),
    _NEXT_ROOT,
    _rotate_gear((0.5, 0, -0.0675), 1),
    _rotate_gear(_TIP, 1),
)
_PITCH_LENGTHS = tuple(
    math.dist(first, last) for first, last in zip(_PITCH_PATH, _PITCH_PATH[1:])
)


def _pitch_point(tooth, parameter):
    remaining = sum(_PITCH_LENGTHS) * parameter
    for first, last, length in zip(
        _PITCH_PATH, _PITCH_PATH[1:], _PITCH_LENGTHS
    ):
        if remaining <= length:
            point = tuple(
                start + (end - start) * remaining / length
                for start, end in zip(first, last)
            )
            return _rotate_gear(point, tooth)
        remaining -= length
    return _rotate_gear(_PITCH_PATH[-1], tooth)


_AXES = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def _gear_frame(first_axis, second_axis, swapped):
    first = _AXES[first_axis]
    second = _AXES[second_axis]
    third = (
        first[1] * second[2] - first[2] * second[1],
        first[2] * second[0] - first[0] * second[2],
        first[0] * second[1] - first[1] * second[0],
    )

    def point(value):
        x, y, z = value
        if swapped:
            x, y, z = y, x, -z
        return tuple(
            x * first[index] + y * second[index] + z * third[index]
            for index in range(3)
        )

    return point, first if swapped else second, third


def _face_gear(cmds, camera, first_axis=0, second_axis=2, swapped=False):
    point, normal, up = _gear_frame(first_axis, second_axis, swapped)
    cmds.setAttr(f"{camera}.translate", *(4 * value for value in normal))
    target = cmds.createNode("transform")
    constraint = cmds.aimConstraint(
        target,
        camera,
        aimVector=(0, 0, -1),
        upVector=(0, 1, 0),
        worldUpType="vector",
        worldUpVector=up,
    )
    cmds.delete(constraint, target)
    return point


@pytest.mark.parametrize("rate", (0.7, 0.9))
def test_gear_template_eight_tip_and_valley_centers_follow_the_pitch_length(
    maya_cmds, new_scene, tmp_path, rate
):
    _require_viewport(maya_cmds)
    with _drawing_view(maya_cmds, "Gear") as (_, shape, camera, _, panel):
        _face_gear(maya_cmds, camera)
        normal = [_rotate_gear(_TIP, tooth) for tooth in range(8)]
        template = [_rotate_gear(_VALLEY, tooth) for tooth in range(8)]
        boundary = (1 - rate) / 2
        # 0.7の境界は斜辺、0.9の境界は歯先短辺にあり、角を跨いで移動する。
        for tooth in (0, 7):
            for side in (-1, 1):
                before = boundary - 0.03
                after = boundary + 0.03
                if side < 0:
                    before, after = 1 - before, 1 - after
                normal.append(_pitch_point(tooth, before))
                template.append(_pitch_point(tooth, after))
        _assert_template_line_partition(
            maya_cmds,
            shape,
            panel,
            tmp_path,
            normal,
            template,
            name=f"gear_pitch_{rate}",
            rate=rate,
        )


def test_gear_template_rate_point9_splits_both_halves_of_every_tip(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(maya_cmds, "Gear") as (_, shape, camera, _, panel):
        _face_gear(maya_cmds, camera)
        normal = [
            _rotate_gear((0.5, 0, sign * 0.012), tooth)
            for tooth in range(8)
            for sign in (-1, 1)
        ]
        template = [
            _rotate_gear((0.5, 0, sign * 0.045), tooth)
            for tooth in range(8)
            for sign in (-1, 1)
        ]
        _assert_template_line_partition(
            maya_cmds,
            shape,
            panel,
            tmp_path,
            normal,
            template,
            name="both_tip_halves",
            rate=0.9,
        )


def test_gear_template_literal_rates_and_invert_keep_the_inner_circle_rule(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(maya_cmds, "Gear") as (_, shape, camera, _, panel):
        _face_gear(maya_cmds, camera)
        inner_normal = [
            _rotate_gear((0.1375, 0, 0), tooth) for tooth in (0, 2, 4, 6)
        ]
        inner_template = [
            _rotate_gear((0.1375, 0, 0), tooth) for tooth in (1, 3, 5, 7)
        ]
        normal = [_rotate_gear(_TIP, tooth) for tooth in (0, 3, 7)]
        template = [_rotate_gear(_VALLEY, tooth) for tooth in (0, 3, 7)]
        normal += inner_normal
        template += inner_template
        all_points = normal + template
        for rate in (0, 0.7, 0.9, 1):
            for invert in (False, True):
                maya_cmds.setAttr(f"{shape}.shapeTemplateLineInvert", invert)
                if rate == 0:
                    kept, templated = all_points, []
                elif rate == 1:
                    kept, templated = [], all_points
                else:
                    kept, templated = normal, template
                if invert:
                    kept, templated = templated, kept
                _assert_template_line_partition(
                    maya_cmds,
                    shape,
                    panel,
                    tmp_path,
                    kept,
                    templated,
                    name=f"literal_{rate}_{invert}",
                    rate=rate,
                )


@pytest.mark.parametrize("width", (0, 0.05, 0.2))
def test_wide_gear_template_uses_the_original_pitch_on_remaining_boundaries(
    maya_cmds, new_scene, tmp_path, width
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds, "Gear", shapeWide=True, shapeWideWidth=width
    ) as (_, shape, camera, camera_shape, panel):
        _face_gear(maya_cmds, camera)
        if width == 0.05:
            maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 1.2)
        half_width = width / 2
        # 正常幅は内外の歯先辺、union fallbackの0.2では残る外側の歯先辺を使う。
        offsets = (0,) if width == 0 else (-half_width, half_width)
        if width >= 0.2:
            offsets = (half_width,)
        normal = []
        template = []
        for tooth in range(8):
            for offset in offsets:
                normal.append(_rotate_gear((0.5 + offset, 0, 0), tooth))
                for sign in (-1, 1):
                    template.append(
                        _rotate_gear((0.5 + offset, 0, sign * 0.04), tooth)
                    )
        valley_radius = math.hypot(_VALLEY[0], _VALLEY[2])
        inner_valley = tuple(
            value * (1 - half_width / valley_radius) for value in _VALLEY
        )
        template += [_rotate_gear(inner_valley, tooth) for tooth in range(8)]
        _assert_template_line_partition(
            maya_cmds,
            shape,
            panel,
            tmp_path,
            normal,
            template,
            name=f"wide_pitch_{width}",
            rate=0.9,
        )


@pytest.mark.parametrize(
    "swapped,first_axis,second_axis",
    ((True, 0, 2), (False, 4, 0), (True, 1, 4)),
)
def test_gear_template_pitch_follows_axis_swap_and_selected_axes(
    maya_cmds, new_scene, tmp_path, swapped, first_axis, second_axis
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Gear",
        shapeAxisSwap=swapped,
        shape1stAxis=first_axis,
        shape2ndAxis=second_axis,
    ) as (_, shape, camera, _, panel):
        point = _face_gear(maya_cmds, camera, first_axis, second_axis, swapped)
        normal = [point(_rotate_gear(_TIP, tooth)) for tooth in range(8)]
        template = [point(_rotate_gear(_VALLEY, tooth)) for tooth in range(8)]
        _assert_template_line_partition(
            maya_cmds,
            shape,
            panel,
            tmp_path,
            normal,
            template,
            name="axis_pitch",
        )


@pytest.mark.parametrize(
    "filled,template_fill",
    ((False, False), (False, True), (True, False), (True, True)),
)
def test_gear_template_lines_and_fill_keep_their_independent_selection(
    maya_cmds, new_scene, tmp_path, filled, template_fill
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Gear",
        shapeFill=filled,
        shapeFillTransparency=0,
        shapeTemplateFill=template_fill,
        shapeTemplateLine=True,
        shapeTemplateLineRate=0.7,
    ) as (_, _, camera, _, panel):
        _face_gear(maya_cmds, camera)
        pixels = _capture_view(panel, tmp_path / "gear_fill_and_lines.png")
        face = (0.25, 0, 0)
        center = (0, 0, 0)
        assert _brightness_near_world(panel, pixels, _TIP) > 600
        assert _pick_world(maya_cmds, panel, _TIP)
        assert _brightness_near_world(panel, pixels, center) < 120
        assert not _pick_world(maya_cmds, panel, center, surface=True)
        assert _pick_world(maya_cmds, panel, face, surface=True) == (
            filled and not template_fill
        )
        if filled:
            assert _brightness_near_world(panel, pixels, face) > 60
        else:
            assert _brightness_near_world(panel, pixels, face) < 120
        if not filled or template_fill:
            assert not _pick_world(maya_cmds, panel, _VALLEY)


def test_gear_template_fill_and_normal_lines_remain_occluded_by_front_geometry(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Gear",
        shapeFill=True,
        shapeFillTransparency=0,
        shapeTemplateFill=True,
        shapeTemplateLine=True,
        shapeTemplateLineRate=0.7,
        shapeDrawOnTop=False,
    ) as (_, shape, camera, _, panel):
        _face_gear(maya_cmds, camera)
        visible = _capture_view(panel, tmp_path / "gear_before_occlusion.png")
        assert _brightness_near_world(panel, visible, _TIP) > 600
        assert _brightness_near_world(panel, visible, (0.25, 0, 0)) > 60
        occluder = maya_cmds.polyPlane(
            width=1.5,
            height=1.5,
            subdivisionsX=1,
            subdivisionsY=1,
            axis=(0, 1, 0),
            constructionHistory=False,
        )[0]
        maya_cmds.setAttr(f"{occluder}.translateY", 0.2)
        maya_cmds.select(clear=True)
        occluded = _capture_view(panel, tmp_path / "gear_behind_plane.png")
        maya_cmds.setAttr(f"{shape}.visibility", False)
        plane_only = _capture_view(panel, tmp_path / "front_plane_only.png")
        assert _brightness_near_world(panel, plane_only, (0, 0.2, 0)) > 120
        assert (
            occluded == plane_only
        ), "手前のポリゴンを通してGearの面または線が見えている"
