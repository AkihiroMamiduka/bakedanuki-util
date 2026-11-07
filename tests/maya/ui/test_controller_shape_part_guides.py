# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_controller_shape_viewport import (
    _aim_at_origin,
    _brightness_near_world,
    _capture_view,
    _drawing_view,
    _pick_world,
    _rgb_near_world,
)

pytestmark = pytest.mark.maya

GUIDE_BODIES = ("Diamond", "Octahedron", "OctahedronArrow")
DISPLAY_CASES = (
    (False, False, False, False),
    (True, False, True, True),
    (False, True, True, False),
    (True, True, False, True),
)


def _require_viewport(cmds):
    if cmds.about(batch=True):
        pytest.skip("実際のViewport 2.0があるMaya GUIで実行する")


def _point(direction, distance, swapped=False):
    x, y, z = (component * distance for component in direction)
    return (y, x, -z) if swapped else (x, y, z)


def _directions(preset):
    directions = ((1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1))
    if preset != "Diamond":
        directions += ((0, 1, 0), (0, -1, 0))
    return directions


def _triangle_sites():
    half_angle = math.atan2(0.87, 0.5) * 0.5
    return (
        ((0.5, 0, 0), (1, 0, 0), math.atan2(0.5, 0.87)),
        (
            (-0.37, 0, 0.5),
            (-math.sin(half_angle), 0, math.cos(half_angle)),
            half_angle,
        ),
        (
            (-0.37, 0, -0.5),
            (-math.sin(half_angle), 0, -math.cos(half_angle)),
            half_angle,
        ),
    )


def _triangle_part_point(vertex, along, distance, swapped=False):
    return _point(
        tuple(
            position + axis * distance for position, axis in zip(vertex, along)
        ),
        1,
        swapped,
    )


def _guide_camera(cmds, preset, swapped, camera, camera_shape):
    if preset in ("Triangle", "Diamond"):
        cmds.setAttr(
            f"{camera}.translate", *((4, 0, 0) if swapped else (0, 4, 0))
        )
        cmds.setAttr(
            f"{camera}.rotate", *((0, 90, 0) if swapped else (-90, 0, 0))
        )
    else:
        _aim_at_origin(cmds, camera, (3, 2, 4))
    cmds.setAttr(f"{camera_shape}.orthographicWidth", 3.2)


def _assert_added_guide(panel, before, after, point):
    previous = _brightness_near_world(panel, before, point)
    current = _brightness_near_world(panel, after, point)
    assert current > max(100, previous + 40), (point, previous, current)


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("appearance", ("smoothShaded", "wireframe"))
def test_corner_marker_survives_wireframe_parts(
    maya_cmds, new_scene, tmp_path, wide, appearance
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "ColorCornerCube",
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapeFill=appearance == "wireframe",
        shapePart=False,
        shapePartShape=6,
        shapePartOffset=4,
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, (3, 2, 4))
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.4)
        maya_cmds.modelEditor(panel, edit=True, displayAppearance=appearance)
        points = ((0.5, 0.45, 0.45), (0.45, 0.5, 0.45), (0.45, 0.45, 0.5))
        baseline = _capture_view(panel, tmp_path / "marker_without_part.png")
        expected = tuple(
            _rgb_near_world(panel, baseline, point) for point in points
        )
        for axis, color in enumerate(expected):
            assert color[axis] > 180 and all(
                color[other] < 50 for other in range(3) if other != axis
            ), (axis, color)
        for enabled in (True, False):
            maya_cmds.setAttr(f"{shape}.shapePart", enabled)
            actual = _capture_view(
                panel, tmp_path / f"marker_part_{enabled}.png"
            )
            for point, color in zip(points, expected):
                assert _rgb_near_world(panel, actual, point) == pytest.approx(
                    color, abs=8
                ), (
                    "Part切替でRGBマーカーが消える",
                    appearance,
                    enabled,
                    point,
                )


@pytest.mark.parametrize("filled,wide,swapped,template", DISPLAY_CASES)
def test_triangle_keeps_all_three_guides_with_parts(
    maya_cmds, new_scene, tmp_path, filled, wide, swapped, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeFill=filled,
        shapeFillTransparency=0.85,
        shapeDrawOnTop=True,
        shapePart=False,
        shapePartShape=6,
        shapePartType=1,
        shapePartOffset=2,
        shapeGuideLine=True,
        shapeGuideLineTemplate=template,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Triangle", swapped, camera, camera_shape)
        baseline = _capture_view(
            panel, tmp_path / "triangle_guides_without_parts.png"
        )
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
        before = _capture_view(
            panel, tmp_path / "triangle_parts_without_guides.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(
            panel, tmp_path / "triangle_guides_with_parts.png"
        )
        for vertex in ((0.5, 0, 0), (-0.37, 0, 0.5), (-0.37, 0, -0.5)):
            sample = _point(vertex, 0.55, swapped)
            _assert_added_guide(panel, before, after, sample)
            assert _rgb_near_world(panel, after, sample) == pytest.approx(
                _rgb_near_world(panel, baseline, sample), abs=8
            ), ("Part切替でTriangleのガイドが変わる", sample)


@pytest.mark.parametrize("part_shape", (0, 1))
@pytest.mark.parametrize("filled,wide,swapped,template", DISPLAY_CASES)
def test_triangle_arrow_guides_follow_the_vertex_bisectors_to_the_tips(
    maya_cmds, new_scene, tmp_path, part_shape, filled, wide, swapped, template
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeFill=filled,
        shapeFillTransparency=0.85,
        shapeDrawOnTop=True,
        shapePart=True,
        shapePartShape=part_shape,
        shapePartSize=1.4,
        shapePartLengthScale=1.6,
        shapePartWidthScale=1.2,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapeGuideLineTemplate=template,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Triangle", swapped, camera, camera_shape)
        for placement in (0, 1, 2):
            maya_cmds.setAttr(f"{shape}.shapePartType", placement)
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
            before = _capture_view(
                panel, tmp_path / f"triangle_arrow_off_{placement}.png"
            )
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
            after = _capture_view(
                panel, tmp_path / f"triangle_arrow_on_{placement}.png"
            )
            for index, (vertex, along, half_angle) in enumerate(
                _triangle_sites()
            ):
                active = placement == 1 or index == 0
                gap = _triangle_part_point(vertex, along, 0.25, swapped)
                if active:
                    # 下2頂点は原点からの放射線とは異なる角二等分線へ折れる。
                    _assert_added_guide(panel, before, after, gap)
                    for fraction in (0.55, 0.85):
                        _assert_added_guide(
                            panel,
                            before,
                            after,
                            _point(vertex, fraction, swapped),
                        )
                    tip_distance = 0.45 + 0.125 * 1.4 * 1.6
                    if wide:
                        tip_distance += 0.04 / math.sin(half_angle)
                    sample = _triangle_part_point(
                        vertex, along, tip_distance - 0.08, swapped
                    )
                    if part_shape == 0:
                        _assert_added_guide(panel, before, after, sample)
                    else:
                        assert (
                            _brightness_near_world(panel, after, sample) > 100
                        )
                    assert (
                        _brightness_near_world(
                            panel,
                            after,
                            _triangle_part_point(
                                vertex, along, tip_distance + 0.1, swapped
                            ),
                        )
                        < 120
                    )
                else:
                    assert _brightness_near_world(panel, after, gap) < 120
            sample = _triangle_part_point(
                (0.5, 0, 0), (1, 0, 0), 0.25, swapped
            )
            if filled:
                maya_cmds.setAttr(f"{shape}.shapeFill", False)
                _capture_view(
                    panel, tmp_path / f"triangle_arrow_pick_{placement}.png"
                )
            assert _pick_world(maya_cmds, panel, sample) == (not template)
            maya_cmds.select(clear=True)
            if filled:
                maya_cmds.setAttr(f"{shape}.shapeFill", True)


@pytest.mark.parametrize(
    "mode", ("part_off", "zero_primary", "zero_other", "non_arrow")
)
def test_triangle_guides_skip_absent_or_non_arrow_heads(
    maya_cmds, new_scene, tmp_path, mode
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeDrawOnTop=True,
        shapeGuideLine=True,
        shapePart=mode != "part_off",
        shapePartShape=6 if mode == "non_arrow" else 0,
        shapePartType=1,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=0 if mode == "zero_primary" else 1,
        shapePartOtherSizeScale=0 if mode == "zero_other" else 1,
    ) as (_, _, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Triangle", False, camera, camera_shape)
        image = _capture_view(panel, tmp_path / f"triangle_omitted_{mode}.png")
        for index, (vertex, along, _) in enumerate(_triangle_sites()):
            extended = (
                mode == "zero_primary"
                and index != 0
                or mode == "zero_other"
                and index == 0
            )
            brightness = _brightness_near_world(
                panel, image, _triangle_part_point(vertex, along, 0.25)
            )
            assert (brightness > 200) if extended else (brightness < 120), (
                mode,
                index,
                brightness,
            )


@pytest.mark.parametrize("length", (1, -1))
@pytest.mark.parametrize("swapped", (False, True))
def test_triangle_inward_offset_keeps_the_bent_arrow_axis_continuous(
    maya_cmds, new_scene, tmp_path, length, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Triangle",
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=0,
        shapePartType=1,
        shapePartOffset=-0.3,
        shapePartLengthScale=length,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapeDrawOnTop=True,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Triangle", swapped, camera, camera_shape)
        before = _capture_view(panel, tmp_path / "triangle_inward_off.png")
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "triangle_inward_on.png")
        for vertex, along, _ in _triangle_sites():
            # 肩から先端までを内向きにも通し、下2頂点を放射線へ置き換えない。
            sample = _triangle_part_point(
                vertex, along, -0.3 + 0.0625 * length, swapped
            )
            _assert_added_guide(panel, before, after, sample)


@pytest.mark.parametrize("preset", GUIDE_BODIES)
@pytest.mark.parametrize("part_shape", (0, 1))
@pytest.mark.parametrize("filled,wide,swapped,template", DISPLAY_CASES)
def test_vertex_arrow_guides_connect_body_roots_to_tips(
    maya_cmds,
    new_scene,
    tmp_path,
    preset,
    part_shape,
    filled,
    wide,
    swapped,
    template,
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeFill=filled,
        shapeFillTransparency=0.85,
        shapeDrawOnTop=True,
        shapePart=True,
        shapePartShape=part_shape,
        shapePartSize=1.4,
        shapePartLengthScale=1.6,
        shapePartWidthScale=1.2,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapeGuideLineTemplate=template,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, preset, swapped, camera, camera_shape)
        directions = _directions(preset)
        for placement in (0, 1):
            maya_cmds.setAttr(f"{shape}.shapePartType", placement)
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
            before = _capture_view(
                panel, tmp_path / f"vertex_guide_off_{placement}.png"
            )
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
            after = _capture_view(
                panel, tmp_path / f"vertex_guide_on_{placement}.png"
            )
            active = directions if placement == 1 else directions[:1]
            for direction in directions:
                gap = _point(direction, 0.725, swapped)
                if direction in active:
                    # 本体と矢印の肩の間を調べ、Arrow3Dの軸線による偽陽性を避ける。
                    _assert_added_guide(panel, before, after, gap)
                    body_point = _point(direction, 0.24, swapped)
                    if preset == "Diamond":
                        _assert_added_guide(panel, before, after, body_point)
                        _assert_added_guide(
                            panel,
                            before,
                            after,
                            _point(direction, 0.44, swapped),
                        )
                    else:
                        # 立体の稜線が重なる投影でも、本体内の線は維持する。
                        assert (
                            _brightness_near_world(panel, after, body_point)
                            > 100
                        )
                    if part_shape == 0:
                        # 立体の斜視ではV輪郭が先端近くへ投影されるため、肩寄りの2点を使う。
                        distances = (
                            (1.15,) if preset == "Diamond" else (1.04, 1.08)
                        )
                        for distance in distances:
                            _assert_added_guide(
                                panel,
                                before,
                                after,
                                _point(direction, distance, swapped),
                            )
                else:
                    assert _brightness_near_world(panel, after, gap) < 120, (
                        "Partのない方向へガイドが伸びる",
                        direction,
                    )
                assert (
                    _brightness_near_world(
                        panel, after, _point(direction, 1.4, swapped)
                    )
                    < 120
                ), ("ガイドがPart先端を越える", direction)
            sample = _point(directions[0], 0.725, swapped)
            if filled:
                # Partの主面を除き、延長ガイドだけの選択可否を確認する。
                maya_cmds.setAttr(f"{shape}.shapeFill", False)
                _capture_view(
                    panel, tmp_path / f"vertex_wire_pick_{placement}.png"
                )
            assert _pick_world(maya_cmds, panel, sample) == (not template), (
                "GuideLineTemplateの選択可否が異なる",
                preset,
                template,
            )
            maya_cmds.select(clear=True)
            if filled:
                maya_cmds.setAttr(f"{shape}.shapeFill", True)


@pytest.mark.parametrize("preset", GUIDE_BODIES)
@pytest.mark.parametrize(
    "mode", ("part_off", "zero_primary", "zero_other", "non_arrow")
)
def test_vertex_guides_skip_absent_or_non_arrow_heads(
    maya_cmds, new_scene, tmp_path, preset, mode
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        preset,
        shapeDrawOnTop=True,
        shapeGuideLine=True,
        shapePart=mode != "part_off",
        shapePartShape=6 if mode == "non_arrow" else 0,
        shapePartType=1,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=0 if mode == "zero_primary" else 1,
        shapePartOtherSizeScale=0 if mode == "zero_other" else 1,
    ) as (_, _, camera, camera_shape, panel):
        _guide_camera(maya_cmds, preset, False, camera, camera_shape)
        image = _capture_view(panel, tmp_path / f"omitted_guide_{mode}.png")
        for index, direction in enumerate(_directions(preset)):
            extended = (
                mode == "zero_primary"
                and index != 0
                or mode == "zero_other"
                and index == 0
            )
            brightness = _brightness_near_world(
                panel, image, _point(direction, 0.725)
            )
            assert (brightness > 200) if extended else (brightness < 120), (
                preset,
                mode,
                direction,
                brightness,
            )
        assert _brightness_near_world(panel, image, (0.24, 0, 0)) > 200


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_diamond_arrow_guides_restore_the_body_to_root_interval(
    maya_cmds, new_scene, tmp_path, filled, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Diamond",
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFillTransparency=0.85,
        shapeDrawOnTop=True,
        shapePart=True,
        shapePartShape=0,
        shapePartType=1,
        shapePartSize=2,
        shapePartOffset=0.12,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Diamond", swapped, camera, camera_shape)
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 2.4)
        before = _capture_view(
            panel, tmp_path / "large_diamond_arrow_guide_off.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(
            panel, tmp_path / "large_diamond_arrow_guide_on.png"
        )
        for index, direction in enumerate(_directions("Diamond")):
            # .44はPartの肩幅で切り取られた本体内、.54以降は根元から先端の区間。
            for distance in (0.24, 0.44, 0.54, 0.60, 0.68):
                _assert_added_guide(
                    panel, before, after, _point(direction, distance, swapped)
                )
            tip = 0.87 if index == 0 else 0.745
            if index == 0:
                _assert_added_guide(
                    panel, before, after, _point(direction, 0.82, swapped)
                )
            assert (
                _brightness_near_world(
                    panel, after, _point(direction, tip + 0.08, swapped)
                )
                < 120
            ), ("ガイドが既定の配置倍率を掛けた先端を越える", direction, tip)


@pytest.mark.parametrize("swapped", (False, True))
def test_oct_arrow_guides_keep_the_stretched_joint_origin(
    maya_cmds, new_scene, tmp_path, swapped
):
    _require_viewport(maya_cmds)
    options = {
        f"shapeBaseSpace{'2nd' if swapped else '1st'}Axis{end}": (
            -value if end == "Minus" else value
        )
        for end, value in (("Minus", 1.5), ("Plus", 3))
    }
    with _drawing_view(
        maya_cmds,
        "OctahedronArrow",
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=0,
        shapePartType=1,
        shapePartOffset=0.45,
        shapePartPrimarySizeScale=1,
        shapePartOtherSizeScale=1,
        shapeDrawOnTop=True,
        **options,
    ) as (_, shape, camera, camera_shape, panel):
        _aim_at_origin(maya_cmds, camera, _point((4, 3, 5), 1, swapped))
        maya_cmds.setAttr(
            f"{camera}.translate", *_point((5.7, 3, 5), 1, swapped)
        )
        maya_cmds.setAttr(f"{camera_shape}.orthographicWidth", 5)
        before = _capture_view(
            panel, tmp_path / "stretched_joint_guide_off.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "stretched_joint_guide_on.png")
        # 断面の稜線やPartの側線と投影が重ならない、本体内と本体外の途中点。
        for point in (
            (1.5, 0.34, 0),
            (1.5, -0.34, 0),
            (1.5, 0, 0.18),
            (1.5, 0, -0.18),
            (1.5, 0.725, 0),
            (1.5, -0.725, 0),
            (1.5, 0, 0.725),
            (1.5, 0, -0.725),
        ):
            _assert_added_guide(
                panel, before, after, _point(point, 1, swapped)
            )
        # 完成本体のbounds中点(2,0,0)から負Z頂点へ結ぶ誤った線上の点。
        wrong_origin = _point((1.75, 0, -0.25), 1, swapped)
        assert _brightness_near_world(panel, before, wrong_origin) < 120
        assert _brightness_near_world(panel, after, wrong_origin) < 120


def test_deformed_vertex_guide_keeps_its_body_segment(
    maya_cmds, new_scene, tmp_path
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Diamond",
        shapeWide=True,
        shapeWideWidth=0.08,
        shapeBaseSpace1stAxisPlusScale3rdAxis=1.6,
        shapeLineTransparency=0.5,
        shapeGuideLine=True,
        shapePartShape=0,
        shapePartOffset=0.45,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Diamond", False, camera, camera_shape)
        baseline = _capture_view(panel, tmp_path / "deformed_body_guide.png")
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        after = _capture_view(panel, tmp_path / "deformed_part_guide.png")
        for point in ((0.2, 0, 0), (0.35, 0, 0)):
            expected = _rgb_near_world(panel, baseline, point)
            assert sum(expected) > 120
            assert _rgb_near_world(panel, after, point) == pytest.approx(
                expected, abs=8
            ), ("非affine変形で元のガイドが欠けるか、二重描画される", point)
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
        before = _capture_view(
            panel, tmp_path / "deformed_part_without_guide.png"
        )
        _assert_added_guide(panel, before, after, (0.725, 0, 0))


@pytest.mark.parametrize("length", (1, -1))
@pytest.mark.parametrize("swapped", (False, True))
def test_inward_offset_keeps_the_guide_through_the_arrow_axis(
    maya_cmds, new_scene, tmp_path, length, swapped
):
    _require_viewport(maya_cmds)
    with _drawing_view(
        maya_cmds,
        "Diamond",
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=0,
        shapePartOffset=-0.3,
        shapePartLengthScale=length,
        shapeDrawOnTop=True,
    ) as (_, shape, camera, camera_shape, panel):
        _guide_camera(maya_cmds, "Diamond", swapped, camera, camera_shape)
        before = _capture_view(
            panel, tmp_path / "inward_arrow_without_guide.png"
        )
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
        after = _capture_view(panel, tmp_path / "inward_arrow_with_guide.png")
        sample = _point((1, 0, 0), 0.25 if length > 0 else 0.125, swapped)
        _assert_added_guide(panel, before, after, sample)
