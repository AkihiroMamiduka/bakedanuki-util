"""両 Cube の面内倍率・静的 TRS・区画表示と更新契約を検証する。"""

from __future__ import annotations

import math
from itertools import product

import pytest
from maya import cmds
from maya.api import OpenMaya as om

import bd_util as bdu

from test_bd_shp_l_cube_fin import CASES as FIN_CASES
from test_bd_shp_l_cube_fin import _bounds, _create, _fn, fin_scene

pytestmark = pytest.mark.maya
NODE_TYPES = ("bdShpL_Cube", "bdShpL_DeformableCube")
AXES = ("1st", "2nd", "3rd")
VECTORS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DEFAULT_LIMITS = ((-0.5, 0.5),) * 3
FACE_PARENTS = tuple(
    (
        normal,
        side,
        f"shapeBaseSpace{axis}Axis{side}Scale",
        f"sbsp{normal + 1}{'p' if side == 'Plus' else 'm'}s",
        tuple(
            (component, f"shapeBaseSpace{axis}Axis{side}Scale{other}Axis")
            for component, other in enumerate(AXES)
            if component != normal
        ),
    )
    for normal, axis in enumerate(AXES)
    for side in ("Plus", "Minus")
)
FACE_CHILDREN = tuple(
    (normal, side, component, child, f"{short}{component + 1}")
    for normal, side, _, short, children in FACE_PARENTS
    for component, child in children
)
TRIPLES = (
    ("shapeTranslate", "st", "doubleLinear", 0.0),
    ("shapeRotate", "sr", "doubleAngle", 0.0),
    ("shapeScale", "ssc", "double", 1.0),
    ("shapeAxisTranslate", "sat", "doubleLinear", 0.0),
    ("shapeAxisRotate", "sar", "doubleAngle", 0.0),
    ("shapeAxisScale", "sasc", "double", 1.0),
)
SCALARS = (("shapeRootSize", "srs", 1.0), ("shapeSize", "ss", 1.0))
ADJUSTMENT_ATTRIBUTES = {
    *(parent for _, _, parent, _, _ in FACE_PARENTS),
    *(child for _, _, _, child, _ in FACE_CHILDREN),
    *(name for name, *_ in SCALARS),
    *(name + suffix for name, *_ in TRIPLES for suffix in ("", "X", "Y", "Z")),
    *("_" * index for index in range(1, 7)),
}
STATIC_SETTINGS = {
    "shapeSize": -1.25,
    "shapeAxisScale": (0.7, -1.3, 1.1),
    "shapeAxisRotate": (17.0, -29.0, 41.0),
    "shapeAxisTranslate": (0.3, -0.7, 1.1),
    "shapeScale": (-0.8, 1.4, 0.6),
    "shapeRotate": (-31.0, 23.0, 11.0),
    "shapeTranslate": (2.0, -3.0, 0.4),
    "shapeRootSize": 1.7,
}
MIXED_FACES = {
    (0, "Plus", 1): 2.0,
    (0, "Minus", 2): -0.75,
    (1, "Plus", 0): 0.4,
    (1, "Minus", 2): 1.3,
    (2, "Plus", 1): 3.0,
    (2, "Minus", 0): 0.0,
}
DEFORM = om.MMatrix(
    (
        (-1.2, 0.4, 0.1, 0),
        (0.3, 0.7, -0.2, 0),
        (0.2, -0.1, 1.4, 0),
        (4, -2, 3, 1),
    )
)


@pytest.fixture(autouse=True)
def adjustment_scene(fin_scene):
    """共通の本番シーン準備へ角度単位と Undo の復元を追加する。"""
    angle = cmds.currentUnit(query=True, angle=True)
    undo = cmds.undoInfo(query=True, state=True)
    cmds.currentUnit(angle="deg")
    cmds.undoInfo(state=True)
    try:
        yield
    finally:
        cmds.currentUnit(angle=angle)
        cmds.undoInfo(state=undo)


def _set_limits(shape, limits):
    """端座標を公開されている符号付き距離へ変換して設定する。"""
    for axis, (minus, plus) in zip(AXES, limits):
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", -minus)
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", plus)


def _set_faces(shape, faces):
    """未指定の面倍率を既定値へ戻し、指定された倍率を設定する。"""
    for normal, side, component, name, _ in FACE_CHILDREN:
        cmds.setAttr(
            f"{shape}.{name}", faces.get((normal, side, component), 1.0)
        )


def _set_static(shape, settings):
    """静的 TRS の scalar と親 compound を直接編集する。"""
    for name, value in settings.items():
        if isinstance(value, tuple):
            cmds.setAttr(f"{shape}.{name}", *value, type="double3")
        else:
            cmds.setAttr(f"{shape}.{name}", value)


def _cage_corners(limits, faces):
    """実端座標における面倍率の線形補間から8頂点を独立に算出する。"""
    center = tuple((minus + plus) / 2 for minus, plus in limits)
    result = []
    for point in product(*limits):
        weights = tuple(
            0.5 if plus == minus else (value - minus) / (plus - minus)
            for value, (minus, plus) in zip(point, limits)
        )
        vertex = []
        for component in range(3):
            factor = math.prod(
                (1 - weights[normal])
                * faces.get((normal, "Minus", component), 1)
                + weights[normal] * faces.get((normal, "Plus", component), 1)
                for normal in range(3)
                if normal != component
            )
            vertex.append(
                center[component]
                + (point[component] - center[component]) * factor
            )
        result.append(tuple(vertex))
    return result


def _rotate_xyz(point, angles):
    """Maya の Euler クラスに依存せず X、Y、Z の順に点を回転する。"""
    x, y, z = point
    rx, ry, rz = map(math.radians, angles)
    y, z = y * math.cos(rx) - z * math.sin(rx), y * math.sin(
        rx
    ) + z * math.cos(rx)
    x, z = x * math.cos(ry) + z * math.sin(ry), -x * math.sin(
        ry
    ) + z * math.cos(ry)
    return (
        x * math.cos(rz) - y * math.sin(rz),
        x * math.sin(rz) + y * math.cos(rz),
        z,
    )


def _static_points(points, settings, axes=(0, 2)):
    """内側 TRS、符号付き軸、外側 TRS、全体倍率の順を独立に適用する。"""
    first, second = (om.MVector(VECTORS[index]) for index in axes)
    third = first ^ second
    assert third.length() == 1
    result = []
    for point in points:
        scaled = tuple(
            value * settings.get("shapeSize", 1) * scale
            for value, scale in zip(
                point, settings.get("shapeAxisScale", (1, 1, 1))
            )
        )
        rotated = _rotate_xyz(
            scaled, settings.get("shapeAxisRotate", (0, 0, 0))
        )
        inner = tuple(
            value + offset
            for value, offset in zip(
                rotated, settings.get("shapeAxisTranslate", (0, 0, 0))
            )
        )
        oriented = first * inner[0] + second * inner[1] + third * inner[2]
        scaled = tuple(
            value * scale
            for value, scale in zip(
                oriented, settings.get("shapeScale", (1, 1, 1))
            )
        )
        rotated = _rotate_xyz(scaled, settings.get("shapeRotate", (0, 0, 0)))
        result.append(
            tuple(
                (value + offset) * settings.get("shapeRootSize", 1)
                for value, offset in zip(
                    rotated, settings.get("shapeTranslate", (0, 0, 0))
                )
            )
        )
    return result


def _point_bounds(points, matrix=None):
    """実頂点を変換して境界を求め、途中の AABB は変換しない。"""
    transformed = [om.MPoint(point) for point in points]
    if matrix is not None:
        transformed = [point * matrix for point in transformed]
    return tuple(
        min(point[axis] for point in transformed) for axis in range(3)
    ) + tuple(max(point[axis] for point in transformed) for axis in range(3))


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_adjustment_schema_contract(node_type):
    """面倍率と TRS の型・親子関係・既定値・単位・静的属性制約を確認する。"""
    _, shape = _create(node_type)
    specs = [
        (name, short, "double", default) for name, short, default in SCALARS
    ]
    specs += [
        (name, short, "double", 1.0) for _, _, _, name, short in FACE_CHILDREN
    ]
    for name, short, kind, default in TRIPLES:
        specs += [
            (name + axis, short + axis.lower(), kind, default)
            for axis in "XYZ"
        ]
    parents = [
        (parent, short, tuple(child for _, child in children), 1.0)
        for _, _, parent, short, children in FACE_PARENTS
    ]
    parents += [
        (name, short, tuple(name + axis for axis in "XYZ"), default)
        for name, short, _, default in TRIPLES
    ]
    for name, short, kind, default in specs:
        plug = f"{shape}.{name}"
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short
        assert cmds.getAttr(plug, type=True) == kind
        assert cmds.getAttr(plug) == pytest.approx(default)
        assert cmds.getAttr(f"{shape}.{short}") == pytest.approx(default)
        assert not cmds.attributeQuery(name, node=shape, minExists=True)
        assert not cmds.attributeQuery(name, node=shape, maxExists=True)
    for name, short, children, default in parents:
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short
        assert cmds.attributeQuery(
            name, node=shape, listChildren=True
        ) == list(children)
        assert cmds.getAttr(f"{shape}.{name}")[0] == (default,) * len(children)
        plug = _fn(shape).findPlug(name, False)
        assert om.MFnNumericAttribute(plug.attribute()).numericType() == (
            om.MFnNumericData.k2Double
            if len(children) == 2
            else om.MFnNumericData.k3Double
        )
        for child in children:
            assert cmds.attributeQuery(child, node=shape, listParent=True) == [
                name
            ]
    for name in ADJUSTMENT_ATTRIBUTES:
        if name.startswith("_"):
            continue
        plug = f"{shape}.{name}"
        assert not cmds.getAttr(plug, keyable=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.getAttr(plug, lock=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        for flag in ("readable", "writable", "storable"):
            assert cmds.attributeQuery(name, node=shape, **{flag: True})


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_six_channel_groups_and_locked_separators(node_type):
    """6区画の厳密な順序と、値を持たない区切りの表示・保存制約を確認する。"""
    _, shape = _create(node_type)
    ordered = ["_", "shape1stAxis", "shape2ndAxis", "__"]
    ordered += [
        f"shapeBaseSpace{axis}Axis{side}"
        for axis in AXES
        for side in ("Plus", "Minus")
    ]
    ordered += ["___"]
    for _, _, parent, _, children in FACE_PARENTS:
        ordered += [parent, *(child for _, child in children)]
    ordered += [
        "____",
        "shapeFin",
        "shapeFinType",
        "shapeFinHeight",
        "shapeFinWidthScale",
        "_____",
        "shapeGuideLine",
        "______",
        "shapeRootSize",
    ]
    for name, *_ in TRIPLES:
        ordered += [name, *(name + axis for axis in "XYZ")]
    ordered += ["shapeSize"]
    assert [
        name
        for name in cmds.listAttr(shape, channelBox=True)
        if name in set(ordered)
    ] == ordered
    assert not cmds.attributeQuery("_______", node=shape, exists=True)
    for index in range(1, 7):
        name = "_" * index
        plug = f"{shape}.{name}"
        assert cmds.attributeQuery(name, node=shape, shortName=True) == name
        assert cmds.attributeQuery(name, node=shape, listEnum=True) == [
            "-----------------------------------"
        ]
        assert cmds.getAttr(plug, type=True) == "enum"
        assert cmds.getAttr(plug) == 0
        assert cmds.getAttr(plug, lock=True)
        assert not cmds.getAttr(plug, keyable=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        assert not cmds.attributeQuery(name, node=shape, storable=True)
        with pytest.raises(RuntimeError):
            cmds.setAttr(plug, 1)


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize("normal,side,component,name,short", FACE_CHILDREN)
def test_each_face_child_updates_signed_rotated_bounds(
    node_type, normal, side, component, name, short
):
    """全12倍率の負値・ゼロ・復帰を、符号を区別できる回転後の境界で確認する。"""
    _, shape = _create(node_type)
    settings = {"shapeRotate": (23, -37, 19)}
    _set_static(shape, settings)
    for value in (2.0, -2.0, 0.0, 1.0):
        cmds.setAttr(f"{shape}.{short}", value)
        points = _cage_corners(
            DEFAULT_LIMITS, {(normal, side, component): value}
        )
        assert _bounds(shape) == pytest.approx(
            _point_bounds(_static_points(points, settings)), abs=1e-7
        )
        assert cmds.getAttr(f"{shape}.{name}") == value


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize("normal,side,parent,short,children", FACE_PARENTS)
def test_face_compound_and_child_edits_with_modifier_history(
    node_type, normal, side, parent, short, children
):
    """親の一括設定と子の直接設定を、遅延実行・Undo・Redo に反映する。"""
    _, shape = _create(node_type)
    modifier = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=modifier).existing(shape)
    before = _bounds(shape)
    getattr(node, short).set(-2, 3)
    assert _bounds(shape) == pytest.approx(before)
    modifier.do_it_dg()
    faces = {
        (normal, side, component): value
        for (component, _), value in zip(children, (-2, 3))
    }
    expected = _point_bounds(_cage_corners(DEFAULT_LIMITS, faces))
    assert cmds.getAttr(f"{shape}.{parent}")[0] == (-2, 3)
    assert _bounds(shape) == pytest.approx(expected)
    modifier.undo_it()
    assert _bounds(shape) == pytest.approx(before)
    modifier.redo_it()
    assert _bounds(shape) == pytest.approx(expected)
    cmds.setAttr(f"{shape}.{children[1][1]}", 4)
    faces[(normal, side, children[1][0])] = 4
    assert cmds.getAttr(f"{shape}.{parent}")[0] == (-2, 4)
    assert _bounds(shape) == pytest.approx(
        _point_bounds(_cage_corners(DEFAULT_LIMITS, faces))
    )


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "limits",
    (
        DEFAULT_LIMITS,
        ((1, 3), (-2, 4), (5, 7)),
        ((3, 1), (4, -2), (7, 5)),
        ((2, 2), (-1, 3), (4, 7)),
        ((2, 2), (-1, -1), (4, 7)),
        ((2, 2), (-1, -1), (4, 4)),
    ),
    ids=("default", "asymmetric", "reversed", "plane", "line", "point"),
)
def test_cage_static_trs_deform_order_and_exact_bounds(node_type, limits):
    """本体8頂点へ静的 TRS と Deform を適用し、親の変換と境界を分離する。"""
    parent, shape = _create(node_type)
    cmds.setAttr(parent + ".translate", 7, -5, 3)
    cmds.setAttr(parent + ".rotate", -11, 29, 13)
    cmds.setAttr(parent + ".scale", -1.2, 0.8, 1.4)
    parent_matrix = list(_fn(shape).dagPath().inclusiveMatrix())
    _set_limits(shape, limits)
    _set_faces(shape, MIXED_FACES)
    _set_static(shape, STATIC_SETTINGS)
    cmds.setAttr(shape + ".s1a", 4)
    cmds.setAttr(shape + ".s2a", 1)
    matrix = DEFORM if node_type == NODE_TYPES[1] else None
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *list(matrix), type="matrix")
    points = _static_points(
        _cage_corners(limits, MIXED_FACES), STATIC_SETTINGS, (4, 1)
    )
    expected = _point_bounds(points, matrix)
    for guide in (False, True, False):
        cmds.setAttr(shape + ".sgl", guide)
        assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
    assert list(_fn(shape).dagPath().inclusiveMatrix()) == pytest.approx(
        parent_matrix
    )


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_collapsed_normal_averages_opposing_face_scales(node_type):
    """潰れたX軸ではX両面の倍率を平均し、Y幅を1.5倍にする。"""
    _, shape = _create(node_type)
    _set_limits(shape, ((2, 2), (-1, 3), (-0.5, 0.5)))
    cmds.setAttr(shape + ".sbsp1ps2", 2)
    assert _bounds(shape) == pytest.approx((2, -2, -0.5, 2, 4, 0.5))
    cmds.setAttr(shape + ".sbsp1ms2", -2)
    assert _bounds(shape) == pytest.approx((2, 1, -0.5, 2, 1, 0.5))
    cmds.setAttr(shape + ".sbsp1ps2", -2)
    assert _bounds(shape) == pytest.approx((2, -3, -0.5, 2, 5, 0.5))


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize("attribute", tuple(STATIC_SETTINGS))
def test_static_trs_signed_zero_and_restore(node_type, attribute):
    """静的8設定の負値・ゼロと復帰が全体の計算順を保つ。"""
    _, shape = _create(node_type)
    limits = ((1, 3), (-2, 4), (5, 7))
    _set_limits(shape, limits)
    _set_faces(shape, MIXED_FACES)
    points = _cage_corners(limits, MIXED_FACES)
    triple = isinstance(STATIC_SETTINGS[attribute], tuple)
    for value in (
        (-1.7, 0, 2.3) if triple else -1.7,
        (0, 0, 0) if triple else 0,
        STATIC_SETTINGS[attribute],
    ):
        settings = dict(STATIC_SETTINGS, **{attribute: value})
        _set_static(shape, settings)
        assert _bounds(shape) == pytest.approx(
            _point_bounds(_static_points(points, settings)), abs=1e-6
        )
        actual = cmds.getAttr(f"{shape}.{attribute}")
        assert (actual[0] if triple else actual) == pytest.approx(value)


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "case",
    [FIN_CASES[index] for index in (0, 3, 4, 6, 12)],
    ids=lambda case: case[0],
)
def test_default_face_fin_receives_static_trs_before_deform(node_type, case):
    """面倍率1では従来 Fin の端点を保ち、本体と共通の TRS で変換する。"""
    _, shape = _create(node_type)
    _, kind, height, width, limits, fin_points = case
    _set_limits(shape, limits)
    _set_static(shape, STATIC_SETTINGS)
    cmds.setAttr(shape + ".sfnt", kind)
    cmds.setAttr(shape + ".sfnh", height)
    cmds.setAttr(shape + ".sfnws", width)
    cmds.setAttr(shape + ".s1a", 3)
    cmds.setAttr(shape + ".s2a", 5)
    matrix = DEFORM if node_type == NODE_TYPES[1] else None
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *list(matrix), type="matrix")
    for fin, guide in product((False, True), repeat=2):
        cmds.setAttr(shape + ".sfn", fin)
        cmds.setAttr(shape + ".sgl", guide)
        points = [*product(*limits), *(fin_points if fin else ())]
        assert _bounds(shape) == pytest.approx(
            _point_bounds(
                _static_points(points, STATIC_SETTINGS, (3, 5)), matrix
            ),
            abs=1e-6,
        )


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "limits,faces,kind,height,width,fin_points",
    (
        (
            DEFAULT_LIMITS,
            {(0, "Plus", 1): 3},
            0,
            0.75,
            1,
            ((-0.5, 0.5, 0), (-0.5, 1.25, 0), (0.5, 2.25, 0), (0.5, 1.5, 0)),
        ),
        (
            DEFAULT_LIMITS,
            {(0, "Plus", 1): 3},
            1,
            0.5,
            -1.5,
            (
                (0.5, 1.5, 0),
                (0.75 - 0.5 / math.sqrt(2), 1.75 + 0.5 / math.sqrt(2), 0),
                (-0.75, 0.25, 0),
                (-0.5, 0.5, 0),
            ),
        ),
        (
            DEFAULT_LIMITS,
            {(0, "Plus", 1): -1, (0, "Minus", 1): -1},
            0,
            2,
            1,
            ((-0.5, -0.5, 0), (-0.5, 1.5, 0), (0.5, 1.5, 0), (0.5, -0.5, 0)),
        ),
        (
            DEFAULT_LIMITS,
            {(0, "Plus", 1): -1, (0, "Minus", 1): -1},
            1,
            2,
            1,
            ((-0.5, -0.5, 0), (-0.5, -2.5, 0), (0.5, -0.5, 0)),
        ),
        (
            ((2, 2), (-0.5, 0.5), (-0.5, 0.5)),
            {(0, "Plus", 1): 3},
            1,
            0.75,
            1,
            ((2, 1, 0), (2, 1.75, 0)),
        ),
    ),
    ids=(
        "sloping_standard",
        "wide_reversed_tapered",
        "reflected_standard",
        "reflected_tapered",
        "collapsed_tangent",
    ),
)
def test_face_warp_fin_attachment_points(
    node_type, limits, faces, kind, height, width, fin_points
):
    """斜面・幅の外挿・反転・接線縮退を、手計算した Fin 端点で検証する。"""
    _, shape = _create(node_type)
    _set_limits(shape, limits)
    _set_faces(shape, faces)
    _set_static(shape, STATIC_SETTINGS)
    cmds.setAttr(shape + ".sfnt", kind)
    cmds.setAttr(shape + ".sfnh", height)
    cmds.setAttr(shape + ".sfnws", width)
    cmds.setAttr(shape + ".sfn", True)
    matrix = DEFORM if node_type == NODE_TYPES[1] else None
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *list(matrix), type="matrix")
    points = [*_cage_corners(limits, faces), *fin_points]
    expected = _point_bounds(_static_points(points, STATIC_SETTINGS), matrix)
    for guide in (False, True):
        cmds.setAttr(shape + ".sgl", guide)
        assert _bounds(shape) == pytest.approx(expected, abs=1e-6)


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_adjustment_units_are_distances_angles_and_unitless_scales(node_type):
    """移動は距離、回転は角度、面倍率とSizeは無次元として扱う。"""
    _, shape = _create(node_type)
    cmds.currentUnit(linear="mm", angle="rad")
    cmds.setAttr(shape + ".st", 10, -20, 30, type="double3")
    cmds.setAttr(shape + ".sat", -5, 15, 20, type="double3")
    cmds.setAttr(shape + ".sr", 0.2, -0.4, 0.6, type="double3")
    cmds.setAttr(shape + ".sar", -0.3, 0.5, 0.7, type="double3")
    cmds.setAttr(shape + ".sbsp1ps", -2, 3, type="double2")
    cmds.setAttr(shape + ".ss", -1.5)
    settings = {
        "shapeTranslate": (1, -2, 3),
        "shapeAxisTranslate": (-0.5, 1.5, 2),
        "shapeRotate": tuple(map(math.degrees, (0.2, -0.4, 0.6))),
        "shapeAxisRotate": tuple(map(math.degrees, (-0.3, 0.5, 0.7))),
        "shapeSize": -1.5,
    }
    points = _cage_corners(
        DEFAULT_LIMITS, {(0, "Plus", 1): -2, (0, "Plus", 2): 3}
    )
    expected = _point_bounds(_static_points(points, settings))
    assert _bounds(shape) == pytest.approx(expected, abs=1e-7)
    cmds.currentUnit(linear="cm", angle="deg")
    for name, value in settings.items():
        actual = cmds.getAttr(f"{shape}.{name}")
        assert (
            actual[0] if isinstance(value, tuple) else actual
        ) == pytest.approx(value)
    assert cmds.getAttr(shape + ".sbsp1ps")[0] == (-2, 3)
    assert _bounds(shape) == pytest.approx(expected, abs=1e-7)


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_adjustments_reject_incoming_connections_and_keys(node_type):
    """親 compound と子属性の入力接続・直接キー・modifier接続を拒否する。"""
    _, shape = _create(node_type)
    _, source = _create(node_type)
    for name in sorted(ADJUSTMENT_ATTRIBUTES):
        if name.startswith("_"):
            continue
        plug = f"{shape}.{name}"
        with pytest.raises(RuntimeError):
            cmds.connectAttr(f"{source}.{name}", plug, force=True)
        assert not cmds.connectionInfo(plug, isDestination=True)
        assert cmds.setKeyframe(shape, attribute=name, time=1) == 0
        assert not cmds.listConnections(plug, source=True, destination=False)
    for name in (
        "shapeBaseSpace1stAxisPlusScale",
        "shapeBaseSpace1stAxisPlusScale2ndAxis",
        "shapeAxisRotate",
        "shapeTranslateX",
        "shapeRootSize",
    ):
        modifier = om.MDGModifier()
        with pytest.raises(RuntimeError):
            modifier.connect(
                _fn(source).findPlug(name, False),
                _fn(shape).findPlug(name, False),
            )
            modifier.doIt()
        assert not _fn(shape).findPlug(name, False).isDestination


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "extension,file_type", (("ma", "mayaAscii"), ("mb", "mayaBinary"))
)
def test_hidden_adjustments_undo_duplicate_and_scene_reload(
    node_type, extension, file_type, tmp_path
):
    """非表示中の更新、編集履歴、独立複製と保存復元を検証する。"""
    parent, shape = _create(node_type)
    original = _bounds(shape)
    cmds.setAttr(parent + ".visibility", False)
    cmds.undoInfo(openChunk=True)
    try:
        _set_faces(shape, MIXED_FACES)
        _set_static(shape, STATIC_SETTINGS)
        cmds.setAttr(shape + ".sgl", True)
    finally:
        cmds.undoInfo(closeChunk=True)
    expected = _point_bounds(
        _static_points(
            _cage_corners(DEFAULT_LIMITS, MIXED_FACES), STATIC_SETTINGS
        )
    )
    assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
    cmds.undo()
    assert _bounds(shape) == pytest.approx(original)
    cmds.redo()
    assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
    copied_parent = cmds.duplicate(parent, returnRootsOnly=True)[0]
    copied = cmds.listRelatives(copied_parent, shapes=True, fullPath=True)[0]
    for name in ADJUSTMENT_ATTRIBUTES:
        assert cmds.getAttr(f"{copied}.{name}") == cmds.getAttr(
            f"{shape}.{name}"
        )
    cmds.setAttr(copied + ".srs", 0)
    assert _bounds(copied) == pytest.approx((0,) * 6)
    assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
    filename = tmp_path / ("cube_adjustments." + extension)
    cmds.file(rename=str(filename))
    cmds.file(save=True, type=file_type, force=True)
    cmds.file(new=True, force=True)
    cmds.file(str(filename), open=True, force=True)
    assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
    assert _bounds(copied) == pytest.approx((0,) * 6)
    for index in range(1, 7):
        assert cmds.getAttr(f"{shape}.{'_' * index}", lock=True)
    cmds.setAttr(shape + ".srs", 0)
    assert _bounds(shape) == pytest.approx((0,) * 6)


def test_deform_connection_updates_after_static_adjustments():
    """静的形状の更新後も、接続した行列だけを時間で変化させられる。"""
    _, shape = _create(NODE_TYPES[1])
    _set_faces(shape, MIXED_FACES)
    _set_static(shape, STATIC_SETTINGS)
    driver = cmds.createNode("composeMatrix")
    cmds.setAttr(driver + ".inputScale", -1.3, 0.7, 1.5)
    cmds.setAttr(driver + ".inputShear", 0.2, -0.3, 0.4)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=1, value=0)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=10, value=37)
    cmds.connectAttr(driver + ".outputMatrix", shape + ".sdm")
    for frame in (1, 10, 1):
        cmds.currentTime(frame)
        matrix = om.MMatrix(cmds.getAttr(driver + ".outputMatrix"))
        for size in (1.25, -0.7):
            cmds.setAttr(shape + ".ss", size)
            settings = dict(STATIC_SETTINGS, shapeSize=size)
            expected = _point_bounds(
                _static_points(
                    _cage_corners(DEFAULT_LIMITS, MIXED_FACES), settings
                ),
                matrix,
            )
            assert _bounds(shape) == pytest.approx(expected, abs=1e-6)
