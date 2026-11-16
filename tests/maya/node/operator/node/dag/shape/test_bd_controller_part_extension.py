# coding: utf-8
from __future__ import annotations

import math

import pytest

import bd_util as bdu

from test_bd_controller_attachment_contract import _controller, _union_bounds
from test_bd_controller_part_size_scale import _swap_bounds
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

NEW_PART_BODIES = (
    "Triangle",
    "Diamond",
    "Octahedron",
    "Cylinder",
    "ArrowPlanar",
    "DiamondArrowSpatial",
    "SquareArrowAxial",
    "CircleArrowAxial",
    "ColorCube",
    "ColorCornerCube",
)
PLANAR_BODIES = ("Triangle", "Diamond", "ArrowPlanar")
TRIANGLE_POINTS = ((0.5, 0.0, 0.0), (-0.37, 0.0, 0.5), (-0.37, 0.0, -0.5))


def _unit(vector):
    length = math.sqrt(sum(value * value for value in vector))
    return tuple(value / length for value in vector)


def _triangle_sites(points=TRIANGLE_POINTS):
    sites = []
    for index, point in enumerate(points):
        incoming = [
            _unit(tuple(point[axis] - other[axis] for axis in range(3)))
            for other in (
                points[index - 1],
                points[(index + 1) % 3],
            )
        ]
        along = _unit(
            tuple(sum(edge[axis] for edge in incoming) for axis in range(3))
        )
        sites.append((point, along))
    return tuple(sites)


def _sites(preset):
    if preset == "Triangle":
        return _triangle_sites()
    if preset == "Diamond":
        return tuple(
            (tuple(0.5 * value for value in along), along)
            for along in ((1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1))
        )
    if preset == "ArrowPlanar":
        return (
            ((0.5, 0, 0), (1, 0, 0)),
            ((-0.5, 0, 0.5), (0, 0, 1)),
            ((-0.5, 0, -0.5), (0, 0, -1)),
        )
    if preset in ("SquareArrowAxial", "CircleArrowAxial"):
        return (((0.5, 0, 0), (1, 0, 0)),)
    if preset == "DiamondArrowSpatial":
        return (
            ((0.5, 0, 0), (1, 0, 0)),
            ((-1, 0, 0), (-1, 0, 0)),
            ((-0.5, 0.5, 0), (0, 1, 0)),
            ((-0.5, -0.5, 0), (0, -1, 0)),
            ((-0.5, 0, 0.5), (0, 0, 1)),
            ((-0.5, 0, -0.5), (0, 0, -1)),
        )
    directions = ((1, 0, 0), (-1, 0, 0))
    if preset != "Cylinder":
        directions += ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return tuple(
        (tuple(0.5 * value for value in along), along) for along in directions
    )


def _body_bounds(preset):
    if preset == "ArrowPlanar":
        return (-0.75, 0, -0.5, 0.5, 0, 0.5)
    if preset == "DiamondArrowSpatial":
        return (-1, -0.5, -0.5, 0.5, 0.5, 0.5)
    if preset == "Triangle":
        return -0.37, 0, -0.5, 0.5, 0, 0.5
    if preset in PLANAR_BODIES:
        return -0.5, 0, -0.5, 0.5, 0, 0.5
    return (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)


def _cube_part_bounds(point, along, offset):
    center = tuple(point[axis] + along[axis] * offset for axis in range(3))
    # 平面の頂点では主面を本体面へ揃え、Cubeの8頂点が占める範囲を求める。
    side = (-along[2], 0, along[0]) if along[1] == 0 else (0, 0, 1)
    up = (
        along[1] * side[2] - along[2] * side[1],
        along[2] * side[0] - along[0] * side[2],
        along[0] * side[1] - along[1] * side[0],
    )
    half = tuple(
        0.05 * (abs(along[axis]) + abs(side[axis]) + abs(up[axis]))
        for axis in range(3)
    )
    return tuple(center[axis] - half[axis] for axis in range(3)) + tuple(
        center[axis] + half[axis] for axis in range(3)
    )


@pytest.mark.parametrize("preset", NEW_PART_BODIES)
@pytest.mark.parametrize("placement", (0, 1, 2))
@pytest.mark.parametrize("swapped", (False, True))
def test_new_part_sites_match_body_vertices_and_cap_centers(
    maya_cmds, maya_om, new_scene, preset, placement, swapped
):
    """本体から離したCubeで配置点と各頂点の外向き方向を確認する。"""
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "newPartSites",
        preset,
        shapeFill=True,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartType=placement,
        shapePartOffset=2.0,
        shapePartPrimarySizeScale=1.0,
        shapePartOtherSizeScale=1.0,
    )
    sites = _sites(preset)
    if placement != 1:
        sites = sites[:1]
    expected = _union_bounds(
        [_body_bounds(preset)]
        + [_cube_part_bounds(point, along, 2.0) for point, along in sites]
    )
    if swapped:
        expected = _swap_bounds(expected)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "values,points",
    (
        (
            {
                "shapeBaseSpace1stAxisMinus": 1.0,
                "shapeBaseSpace1stAxisPlus": 2.0,
                "shapeBaseSpace3rdAxisMinus": 0.25,
                "shapeBaseSpace3rdAxisPlus": 0.75,
            },
            ((2.0, 0, 0.25), (-0.61, 0, 0.75), (-0.61, 0, -0.25)),
        ),
        (
            {
                "shapeBaseSpace1stAxisPlusScale3rdAxis": 1.8,
                "shapeBaseSpace3rdAxisPlusScale1stAxis": 1.5,
            },
            ((0.625, 0, 0), (-0.555, 0, 0.552), (-0.37, 0, -0.552)),
        ),
    ),
    ids=("nonuniform_span", "asymmetric_face_scale"),
)
@pytest.mark.parametrize("placement", (0, 1, 2))
def test_triangle_parts_bisect_the_adjusted_vertex_angles(
    maya_cmds, maya_om, new_scene, values, points, placement
):
    """非一様な調整後の頂点を使い、角の二等分線を求め直す。"""
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "adjustedTriangleParts",
        "Triangle",
        shapeFill=True,
        shapePart=True,
        shapePartShape=6,
        shapePartType=placement,
        shapePartOffset=2.0,
        shapePartPrimarySizeScale=1.0,
        shapePartOtherSizeScale=1.0,
        **values,
    )
    sites = _triangle_sites(points)
    if placement != 1:
        sites = sites[:1]
    body = tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))
    expected = _union_bounds(
        [body]
        + [_cube_part_bounds(point, along, 2.0) for point, along in sites]
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", NEW_PART_BODIES)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("wide", (False, True))
def test_new_bodies_generate_every_part_and_preserve_template_bounds(
    maya_cmds, maya_om, new_scene, preset, part, wide
):
    """各小形状が生成され、表示種別だけの切替で範囲が変わらない。"""
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "newPartKinds",
        preset,
        shapeWide=wide,
        shapePartShape=part,
        shapePartType=1,
        shapePartOffset=3.0,
        shapePartPrimarySizeScale=1.0,
        shapePartOtherSizeScale=1.0,
    )
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        body = _bounds(maya_om, shape)
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        decorated = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in decorated)
        assert decorated != pytest.approx(body)
        for attribute in (
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", True)
        assert _bounds(maya_om, shape) == pytest.approx(decorated, abs=1e-9)
        for attribute in (
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", False)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)


@pytest.mark.parametrize("preset", ("SquareArrowAxial", "CircleArrowAxial"))
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("swapped", (False, True))
def test_single_tip_at_ends_applies_only_the_primary_multiplier(
    maya_cmds, maya_om, new_scene, preset, part, swapped
):
    """先端1点でもAtEndsのPrimary倍率を使い、Other倍率は保持して無視する。"""
    _load_bd_util_nodes(maya_cmds)
    size = 1.7
    options = dict(
        shapeAxisSwap=swapped,
        shapeFill=True,
        shapePart=True,
        shapePartShape=part,
        shapePartOffset=0.7,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.8,
        shapePartHeightScale=0.8,
    )
    actual = _controller(maya_cmds, "singleTipEnds", preset, **options)
    reference = _controller(maya_cmds, "singleTipEnd", preset, **options)
    maya_cmds.setAttr(f"{actual}.shapePartType", 1)
    maya_cmds.setAttr(f"{actual}.shapePartSize", size)
    maya_cmds.setAttr(f"{reference}.shapePart", False)
    body = _bounds(maya_om, reference)
    for primary in (0.0, 0.4, 2.0, -1.0):
        maya_cmds.setAttr(f"{actual}.shapePartPrimarySizeScale", primary)
        maya_cmds.setAttr(f"{reference}.shapePart", primary != 0)
        maya_cmds.setAttr(f"{reference}.shapePartSize", size * primary)
        expected = _bounds(maya_om, reference) if primary != 0 else body
        for other in (0.0, 3.0, -2.0):
            maya_cmds.setAttr(f"{actual}.shapePartOtherSizeScale", other)
            assert _bounds(maya_om, actual) == pytest.approx(
                expected, abs=1e-9
            )
            assert (
                maya_cmds.getAttr(f"{actual}.shapePartOtherSizeScale") == other
            )


@pytest.mark.parametrize("preset", NEW_PART_BODIES)
@pytest.mark.parametrize("swapped", (False, True))
def test_zero_part_multipliers_preserve_new_wide_body_geometry(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    """両倍率0のAtEndsは、Partを無効にした独立したWide本体と一致する。"""
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeWide=True,
        shapeWideWidth=0.08,
        shapeAxisSwap=swapped,
        shapePartShape=1,
        shapePartType=1,
        shapePartOffset=0.15,
        shapePartSize=2.5,
    )
    actual = _controller(
        maya_cmds,
        "zeroPartWideBody",
        preset,
        shapePart=True,
        shapePartPrimarySizeScale=0.0,
        shapePartOtherSizeScale=0.0,
        **options,
    )
    reference = _controller(
        maya_cmds, "plainWideBody", preset, shapePart=False, **options
    )
    for filled in (False, True):
        for angles in ((0, 0, 0), (17, -29, 37)):
            for shape in (actual, reference):
                maya_cmds.setAttr(f"{shape}.shapeFill", filled)
                maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
            assert _bounds(maya_om, actual) == pytest.approx(
                _bounds(maya_om, reference), abs=1e-9
            ), (preset, swapped, filled, angles)


@pytest.mark.parametrize("preset", ("Diamond", "ColorCube"))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_wide_straight_edges_keep_their_bounds_with_a_displaced_part(
    maya_cmds, maya_om, new_scene, preset, swapped, filled
):
    """離したCube Partの周囲でも、菱形の辺や箱の面を円弧へ変えない。"""
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "straightWideBody",
        preset,
        shapeWide=True,
        shapeWideWidth=0.08,
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=6,
        shapePartType=0,
        shapePartOffset=2.0,
    )
    if preset == "Diamond":
        reach = 0.5 + math.sqrt(2) * 0.04
        expected = (-reach, -0.05, -reach, reach + 2.05, 0.05, reach)
    else:
        expected = (-0.5, -0.5, -0.5, 2.55, 0.5, 0.5)
    if swapped:
        expected = _swap_bounds(expected)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("ArrowPlanar", "DiamondArrowSpatial"))
@pytest.mark.parametrize("swapped", (False, True))
def test_arrow_part_vertices_follow_the_fixed_rear_section(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    """幅のあるPartで、伸長後の肩と中央断面が後端の固定長へ追従する。"""
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedRearParts",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
        shapePart=True,
        shapePartShape=6,
        shapePartType=1,
        shapePartWidthScale=20.0,
        shapePartHeightScale=20.0 if preset == "DiamondArrowSpatial" else 1.0,
        shapePartPrimarySizeScale=(
            0.0 if preset == "DiamondArrowSpatial" else 1.0
        ),
        shapePartOtherSizeScale=1.0,
    )
    axis = "2nd" if swapped else "1st"
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", 6.0)
    expected = (
        (-3.0, -1.0, -1.0, 6.0, 1.0, 1.0)
        if preset == "DiamondArrowSpatial"
        else (-3.0, -0.05, -1.0, 6.05, 0.05, 1.0)
    )
    if swapped:
        expected = _swap_bounds(expected)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "preset", ("Triangle", "DiamondArrowSpatial", "ColorCornerCube")
)
def test_new_part_direct_edits_undo_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, preset
):
    """新しい対象でも直接編集・履歴・再読込が描画キャッシュへ届く。"""
    _load_bd_util_nodes(maya_cmds)
    name = _controller(
        maya_cmds,
        "animatedNewParts",
        preset,
        shapePartShape=6,
        shapePartType=1,
    )
    body = _bounds(maya_om, name)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shapePart.set(True)
    shape.shapePartOffset.set(3)
    mod.do_it_dg()
    decorated = _bounds(maya_om, name)
    assert decorated != pytest.approx(body)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(body, abs=1e-9)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(decorated, abs=1e-9)
    maya_cmds.setAttr(f"{name}.shapePartOffset", 4)
    changed = _bounds(maya_om, name)
    assert changed != pytest.approx(decorated)
    maya_cmds.setAttr(f"{name}.shapePartOffset", 3)
    assert _bounds(maya_om, name) == pytest.approx(decorated, abs=1e-9)
    scene = tmp_path / "new_part_shapes.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.getAttr(f"{name}.shapePartOffset") == 3
    assert _bounds(maya_om, name) == pytest.approx(decorated, abs=1e-9)
    maya_cmds.setAttr(f"{name}.shapePartOffset", 4)
    assert _bounds(maya_om, name) == pytest.approx(changed, abs=1e-9)
