"""両 Cube の原点補助線と、静的変形・行列更新・履歴の契約を検証する。"""

from __future__ import annotations

from itertools import product

import pytest
from maya import cmds
from maya.api import OpenMaya as om

import bd_util as bdu

from test_bd_shp_l_cube_adjustments import (
    DEFAULT_LIMITS,
    DEFORM,
    MIXED_FACES,
    NODE_TYPES,
    STATIC_SETTINGS,
    _cage_corners,
    _point_bounds,
    _set_faces,
    _set_limits,
    _set_static,
    _static_points,
    adjustment_scene,
)
from test_bd_shp_l_cube_fin import CASES, _bounds, _create, _fn, fin_scene

pytestmark = pytest.mark.maya


def _expected(
    limits,
    settings,
    *,
    faces=None,
    fin_points=(),
    axes=(0, 2),
    matrix=None,
    enabled=True,
):
    """静的中心が非ゼロなら線を加え、本体・Finとともに行列で変換する。"""
    points = _static_points(
        [*_cage_corners(limits, faces or {}), *fin_points], settings, axes
    )
    center = tuple((minus + plus) / 2 for minus, plus in limits)
    endpoint = _static_points([center], settings, axes)[0]
    if enabled and endpoint != (0, 0, 0):
        points += [(0, 0, 0), endpoint]
    if matrix is not None:
        points = [tuple(om.MPoint(point) * matrix)[:3] for point in points]
    return _point_bounds(points)


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_offset_line_static_attribute_contract(node_type):
    """既定値・短縮名・直接編集・入力拒否・出力参照の契約を確認する。"""
    _, shape = _create(node_type)
    _, source = _create(node_type)
    plug = shape + ".shapeOffsetLine"
    assert (
        cmds.attributeQuery("shapeOffsetLine", node=shape, shortName=True)
        == "sol"
    )
    assert cmds.getAttr(plug, type=True) == "bool"
    assert cmds.getAttr(plug) is False
    assert cmds.getAttr(shape + ".sol") is False
    assert cmds.attributeQuery(
        "shapeOffsetLine", node=shape, listDefault=True
    ) == [False]
    assert not cmds.getAttr(plug, keyable=True)
    assert cmds.getAttr(plug, channelBox=True)
    assert not cmds.getAttr(plug, lock=True)
    assert not cmds.attributeQuery(
        "shapeOffsetLine", node=shape, connectable=True
    )
    for flag in ("readable", "writable", "storable"):
        assert cmds.attributeQuery(
            "shapeOffsetLine", node=shape, **{flag: True}
        )
    assert not cmds.attributeQuery(
        "shapeOffsetLineTemplate", node=shape, exists=True
    )
    with pytest.raises(RuntimeError):
        cmds.connectAttr(source + ".sol", plug)
    modifier = om.MDGModifier()
    with pytest.raises(RuntimeError):
        modifier.connect(
            _fn(source).findPlug("sol", False),
            _fn(shape).findPlug("sol", False),
        )
        modifier.doIt()
    assert cmds.setKeyframe(shape, attribute="shapeOffsetLine", time=1) == 0
    assert not cmds.listConnections(plug, source=True, destination=False)
    target = cmds.createNode("network")
    cmds.addAttr(target, longName="enabled", attributeType="bool")
    cmds.connectAttr(plug, target + ".enabled")
    cmds.setAttr(shape + ".sol", True)
    assert cmds.getAttr(target + ".enabled") is True


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "limits",
    (
        DEFAULT_LIMITS,
        ((1, 3), (-2, 4), (5, 7)),
        ((3, 1), (4, -2), (7, 5)),
        ((2, 2), (-1, 3), (4, 7)),
    ),
    ids=("default", "asymmetric", "reversed", "collapsed"),
)
def test_offset_bounds_use_static_center_and_deform_both_line_endpoints(
    node_type, limits
):
    """非線形本体と静的中心から線を構成し、両端へ同じDeformを適用する。"""
    parent, shape = _create(node_type)
    _set_limits(shape, limits)
    _set_faces(shape, MIXED_FACES)
    _set_static(shape, STATIC_SETTINGS)
    cmds.setAttr(shape + ".s1a", 4)
    cmds.setAttr(shape + ".s2a", 1)
    cmds.setAttr(parent + ".translate", 10, -20, 30)
    cmds.setAttr(parent + ".rotate", 11, 22, 33)
    parent_matrix = list(_fn(shape).dagPath().inclusiveMatrix())
    matrix = DEFORM if node_type == NODE_TYPES[1] else None
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *list(matrix), type="matrix")
    for enabled in (False, True, False, True):
        cmds.setAttr(shape + ".sol", enabled)
        assert _bounds(shape) == pytest.approx(
            _expected(
                limits,
                STATIC_SETTINGS,
                faces=MIXED_FACES,
                axes=(4, 1),
                matrix=matrix,
                enabled=enabled,
            ),
            abs=1e-6,
        )
    assert list(_fn(shape).dagPath().inclusiveMatrix()) == pytest.approx(
        parent_matrix
    )


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_offset_fin_and_guide_toggle_union(node_type):
    """Finの張り出しと原点補助線を合算し、Guideの切替では範囲を変えない。"""
    _, shape = _create(node_type)
    _, kind, height, width, limits, fin_points = CASES[9]
    _set_limits(shape, limits)
    settings = {"shapeTranslate": (7, 2, -5), "shapeRotate": (17, 29, -31)}
    _set_static(shape, settings)
    cmds.setAttr(shape + ".sfnt", kind)
    cmds.setAttr(shape + ".sfnh", height)
    cmds.setAttr(shape + ".sfnws", width)
    for fin, guide, offset in product((False, True), repeat=3):
        cmds.setAttr(shape + ".sfn", fin)
        cmds.setAttr(shape + ".sgl", guide)
        cmds.setAttr(shape + ".sol", offset)
        assert _bounds(shape) == pytest.approx(
            _expected(
                limits,
                settings,
                fin_points=fin_points if fin else (),
                enabled=offset,
            ),
            abs=1e-6,
        )


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_offset_exact_zero_and_sub_epsilon_translation(node_type):
    """原点に潰れた形状と、極小だがゼロでない移動を区別する。"""
    _, shape = _create(node_type)
    cmds.setAttr(shape + ".ss", 0)
    cmds.setAttr(shape + ".sol", True)
    assert _bounds(shape) == (0,) * 6
    for translation in (1e-14, -1e-14, 0.0):
        cmds.setAttr(shape + ".stx", translation)
        expected = (min(0, translation), 0, 0, max(0, translation), 0, 0)
        assert _bounds(shape) == pytest.approx(expected, rel=1e-6, abs=0)
        cmds.setAttr(shape + ".sol", False)
        assert _bounds(shape) == pytest.approx(
            (translation, 0, 0) * 2, rel=1e-6, abs=0
        )
        cmds.setAttr(shape + ".sol", True)


def test_deform_singular_matrix_translation_and_cancellation():
    """特異行列では線も潰し、終点が原点へ移動しても静的に作った線を保つ。"""
    _, shape = _create(NODE_TYPES[1])
    cmds.setAttr(shape + ".sol", True)
    singular = om.MMatrix(
        ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (3, -4, 5, 1))
    )
    cmds.setAttr(shape + ".sdm", *list(singular), type="matrix")
    assert _bounds(shape) == pytest.approx((3, -4, 5) * 2)
    cmds.setAttr(shape + ".sol", False)
    assert _bounds(shape) == pytest.approx((3, -4, 5) * 2)
    cmds.setAttr(shape + ".sol", True)
    cmds.setAttr(shape + ".ss", 0)
    cmds.setAttr(shape + ".st", 1, 2, 3, type="double3")
    assert _bounds(shape) == pytest.approx((3, -4, 5) * 2)
    cancel = om.MMatrix(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (-1, -2, -3, 1))
    )
    cmds.setAttr(shape + ".sdm", *list(cancel), type="matrix")
    assert _bounds(shape) == pytest.approx((-1, -2, -3, 0, 0, 0))
    cmds.setAttr(shape + ".sol", False)
    assert _bounds(shape) == (0,) * 6
    cmds.setAttr(shape + ".sol", True)
    assert _bounds(shape) == pytest.approx((-1, -2, -3, 0, 0, 0))
    cmds.setAttr(shape + ".sdm", *list(om.MMatrix()), type="matrix")
    assert _bounds(shape) == pytest.approx((0, 0, 0, 1, 2, 3))
    cmds.setAttr(shape + ".srs", 0)
    assert _bounds(shape) == (0,) * 6
    cmds.setAttr(shape + ".sdm", *list(singular), type="matrix")
    assert _bounds(shape) == pytest.approx((3, -4, 5) * 2)


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "extension,file_type", (("ma", "mayaAscii"), ("mb", "mayaBinary"))
)
def test_offset_hidden_edit_modifier_history_duplicate_and_save(
    node_type, extension, file_type, tmp_path
):
    """非表示中の遅延編集・Undo・複製と、ゼロ端点で保存したON値を復元する。"""
    parent, shape = _create(node_type)
    cmds.setAttr(shape + ".st", 3, -2, 4, type="double3")
    original = _bounds(shape)
    cmds.setAttr(parent + ".visibility", False)
    modifier = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=modifier).existing(shape)
    node.sol.set(True)
    assert node.shapeOffsetLine.get() is False
    assert _bounds(shape) == original
    modifier.do_it_dg()
    expected = _expected(DEFAULT_LIMITS, {"shapeTranslate": (3, -2, 4)})
    assert node.shapeOffsetLine.get() is True
    assert _bounds(shape) == pytest.approx(expected)
    modifier.undo_it()
    assert _bounds(shape) == original
    modifier.redo_it()
    assert _bounds(shape) == pytest.approx(expected)
    copied_parent = cmds.duplicate(parent, returnRootsOnly=True)[0]
    copied = cmds.listRelatives(copied_parent, shapes=True, fullPath=True)[0]
    assert cmds.getAttr(copied + ".sol") is True
    cmds.setAttr(copied + ".sol", False)
    assert _bounds(copied) == original
    assert _bounds(shape) == pytest.approx(expected)
    cmds.setAttr(shape + ".st", 0, 0, 0, type="double3")
    filename = tmp_path / ("cube_offset_line." + extension)
    cmds.file(rename=str(filename))
    cmds.file(save=True, type=file_type, force=True)
    cmds.file(new=True, force=True)
    cmds.file(str(filename), open=True, force=True)
    assert cmds.getAttr(shape + ".sol") is True
    assert cmds.getAttr(copied + ".sol") is False
    assert _bounds(shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    cmds.setAttr(shape + ".st", 3, -2, 4, type="double3")
    assert _bounds(shape) == pytest.approx(expected)
    assert _bounds(copied) == original


@pytest.mark.parametrize("static_offset", (0, 2))
def test_connected_deform_preserves_static_line_decision(static_offset):
    """行列だけの移動では線を作らず、既存の線は始点も一緒に移動する。"""
    _, shape = _create(NODE_TYPES[1])
    cmds.setAttr(shape + ".ss", 0)
    cmds.setAttr(shape + ".stx", static_offset)
    cmds.setAttr(shape + ".sol", True)
    driver = cmds.createNode("composeMatrix")
    cmds.setKeyframe(driver, attribute="inputTranslateZ", time=1, value=0)
    cmds.setKeyframe(driver, attribute="inputTranslateZ", time=10, value=3)
    cmds.connectAttr(driver + ".outputMatrix", shape + ".sdm")
    for frame, distance in ((1, 0), (10, 3), (1, 0), (10, 3)):
        cmds.currentTime(frame)
        assert _bounds(shape) == pytest.approx(
            (0, 0, distance, static_offset, 0, distance)
        )
        cmds.setAttr(shape + ".sol", False)
        assert _bounds(shape) == pytest.approx(
            (static_offset, 0, distance) * 2
        )
        cmds.setAttr(shape + ".sol", True)
