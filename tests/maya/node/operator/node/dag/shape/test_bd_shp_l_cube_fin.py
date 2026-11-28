"""両 CustomCube の Fin の寸法・変形・静的属性・履歴を本番 DLL で検証する。"""

from __future__ import annotations

import os
from itertools import product
from pathlib import Path

import pytest
from maya import cmds
from maya.api import OpenMaya as om

import bd_util as bdu

pytestmark = pytest.mark.maya
NODE_TYPES = ("bdCtrlShpL_Cube", "bdCtrlShpL_DeformableCube")
SPECS = (
    ("shapeFin", "sfn", "bool", False),
    ("shapeFinType", "sfnt", "enum", 0),
    ("shapeFinHeight", "sfnh", "doubleLinear", 0.5),
    ("shapeFinWidthScale", "sfnws", "double", 1.0),
)
DEFAULT = ((-0.5, 0.5),) * 3
AFFINE = om.MMatrix(
    (
        (-2, 0.5, 0.25, 0),
        (1.5, 3, -0.5, 0),
        (0.25, -0.5, 0.75, 0),
        (4, -5, 6, 1),
    )
)
AXIS_VECTORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
CASES = (
    (
        "standard",
        0,
        0.5,
        1,
        DEFAULT,
        ((-0.5, 0.5, 0), (-0.5, 1, 0), (0.5, 1, 0), (0.5, 0.5, 0)),
    ),
    (
        "tapered",
        1,
        0.5,
        1,
        DEFAULT,
        ((-0.5, 0.5, 0), (-0.5, 1, 0), (0.5, 0.5, 0)),
    ),
    (
        "wide_standard",
        0,
        0.5,
        2,
        DEFAULT,
        ((-1, 0.5, 0), (-1, 1, 0), (1, 1, 0), (1, 0.5, 0)),
    ),
    (
        "wide_tapered",
        1,
        0.5,
        2,
        DEFAULT,
        ((-0.5, 0.5, 0), (-1, 1, 0), (1, 0.5, 0), (0.5, 0.5, 0)),
    ),
    (
        "negative_width",
        1,
        0.5,
        -2,
        DEFAULT,
        ((0.5, 0.5, 0), (1, 1, 0), (-1, 0.5, 0), (-0.5, 0.5, 0)),
    ),
    (
        "negative_height",
        0,
        -2,
        1,
        DEFAULT,
        ((-0.5, 0.5, 0), (-0.5, -1.5, 0), (0.5, -1.5, 0), (0.5, 0.5, 0)),
    ),
    (
        "negative_height_tapered",
        1,
        -2,
        1,
        DEFAULT,
        ((-0.5, 0.5, 0), (-0.5, -1.5, 0), (0.5, 0.5, 0)),
    ),
    ("zero_width", 0, 0.75, 0, DEFAULT, ((0, 0.5, 0), (0, 1.25, 0))),
    ("zero_height", 1, 0, 3, DEFAULT, ()),
    (
        "asymmetric",
        1,
        1.25,
        2,
        ((1, 3), (-2, 4), (5, 7)),
        ((1, 4, 6), (0, 5.25, 6), (4, 4, 6), (3, 4, 6)),
    ),
    (
        "reversed",
        1,
        1.25,
        1,
        ((3, 1), (4, -2), (7, 5)),
        ((3, -2, 6), (3, -3.25, 6), (1, -2, 6)),
    ),
    (
        "flat_height",
        0,
        1.25,
        1,
        ((-2, 4), (3, 3), (-1, 1)),
        ((-2, 3, 0), (-2, 4.25, 0), (4, 4.25, 0), (4, 3, 0)),
    ),
    (
        "flat_width",
        1,
        0.75,
        2,
        ((2, 2), (-1, 1), (-1, 1)),
        ((2, 1, 0), (2, 1.75, 0)),
    ),
    ("point", 0, 1, 1, ((2, 2), (3, 3), (4, 4)), ((2, 3, 4), (2, 4, 4))),
)


@pytest.fixture(autouse=True)
def fin_scene(new_scene):
    """本番 DLL と cm 単位の空シーンを使用する。"""
    version = int(cmds.about(apiVersion=True)) // 10000
    default = (
        Path(__file__).resolve().parents[7]
        / f"bakedanuki/bakedanuki-util/plug-ins/maya{version}/bdUtilNodes.mll"
    )
    path = Path(os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default)).resolve(
        strict=True
    )
    cmds.loadPlugin(str(path), quiet=True)
    linear = cmds.currentUnit(query=True, linear=True)
    cmds.currentUnit(linear="cm")
    try:
        yield
    finally:
        cmds.currentUnit(linear=linear)


def _create(node_type):
    """型に対応する親とシェイプの完全パスを返す。"""
    parent = cmds.createNode("transform", name="finControl")
    shape = cmds.createNode(node_type, parent=parent, name="finShape")
    return cmds.ls(parent, long=True)[0], cmds.ls(shape, long=True)[0]


def _fn(shape):
    """シェイプの DAG 関数セットを取得する。"""
    return om.MFnDagNode(om.MSelectionList().add(shape).getDagPath(0))


def _bounds(shape):
    """ローカル境界を返す。"""
    box = _fn(shape).boundingBox
    return (*tuple(box.min)[:3], *tuple(box.max)[:3])


def _expected(limits, fin_points, axes=(0, 2), matrix=None):
    """独立に列挙した本体端点と Fin 端点を姿勢・行列へ適用する。"""
    first, second = (om.MVector(AXIS_VECTORS[index]) for index in axes)
    third = first ^ second
    box = om.MBoundingBox()
    for x, y, z in [*product(*limits), *fin_points]:
        point = om.MPoint(first * x + second * y + third * z)
        box.expand(point if matrix is None else point * matrix)
    return (*tuple(box.min)[:3], *tuple(box.max)[:3])


def _set_case(shape, case):
    """基準空間と Fin の設定値を直接編集する。"""
    _, kind, height, width, limits, _ = case
    for axis, endpoints in zip(("1st", "2nd", "3rd"), limits):
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", -endpoints[0])
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", endpoints[1])
    for name, value in (("sfnt", kind), ("sfnh", height), ("sfnws", width)):
        cmds.setAttr(f"{shape}.{name}", value)


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_fin_static_attribute_contract(node_type):
    """4属性の型・短縮名・既定値・接続とキーの拒否を確認する。"""
    _, shape = _create(node_type)
    source = cmds.createNode("network", name="finValues")
    target = cmds.createNode("network", name="finReadback")
    for name, short, kind, default in SPECS:
        plug = f"{shape}.{name}"
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short
        assert cmds.getAttr(plug, type=True) == kind
        assert cmds.getAttr(plug) == pytest.approx(default)
        assert not cmds.getAttr(plug, keyable=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        assert cmds.attributeQuery(name, node=shape, storable=True)
        attr_type = "long" if kind == "enum" else kind
        cmds.addAttr(source, longName=name, attributeType=attr_type)
        cmds.addAttr(target, longName=name, attributeType=attr_type)
        with pytest.raises(RuntimeError):
            cmds.connectAttr(f"{source}.{name}", plug)
        source_fn = om.MFnDependencyNode(
            om.MSelectionList().add(source).getDependNode(0)
        )
        modifier = om.MDGModifier()
        with pytest.raises(RuntimeError):
            modifier.connect(
                source_fn.findPlug(name, False),
                _fn(shape).findPlug(name, False),
            )
            modifier.doIt()
        assert not cmds.connectionInfo(plug, isDestination=True)
        assert cmds.setKeyframe(shape, attribute=name, time=1) == 0
        cmds.connectAttr(plug, f"{target}.{name}")
        value = {
            "bool": True,
            "enum": 1,
            "doubleLinear": -1.25,
            "double": -2.0,
        }[kind]
        cmds.setAttr(f"{shape}.{short}", value)
        assert cmds.getAttr(f"{target}.{name}") == pytest.approx(value)
    assert cmds.attributeQuery("shapeFinType", node=shape, listEnum=True) == [
        "Standard:Tapered"
    ]
    assert not cmds.attributeQuery("shapeFinTemplate", node=shape, exists=True)


@pytest.mark.parametrize("case", CASES, ids=[case[0] for case in CASES])
@pytest.mark.parametrize(
    "node_type,deformed",
    ((NODE_TYPES[0], False), (NODE_TYPES[1], False), (NODE_TYPES[1], True)),
)
def test_fin_vertices_bounds_and_guide_combinations(case, node_type, deformed):
    """反転・縮退と affine 変形後の端点、および4種類の ON/OFF を検証する。"""
    _, shape = _create(node_type)
    _set_case(shape, case)
    axes = (4, 1) if deformed else (0, 2)
    matrix = AFFINE if deformed else None
    cmds.setAttr(shape + ".s1a", axes[0])
    cmds.setAttr(shape + ".s2a", axes[1])
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *list(matrix), type="matrix")
    for fin, guide in (
        (False, False),
        (False, True),
        (True, False),
        (True, True),
        (False, False),
        (True, True),
    ):
        cmds.setAttr(shape + ".sfn", fin)
        cmds.setAttr(shape + ".sgl", guide)
        assert _bounds(shape) == pytest.approx(
            _expected(case[4], case[5] if fin else (), axes, matrix), abs=1e-7
        )
    assert cmds.getAttr(shape + ".sfnt") == case[1]
    assert cmds.getAttr(shape + ".sfnh") == pytest.approx(case[2])
    assert cmds.getAttr(shape + ".sfnws") == pytest.approx(case[3])


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "axes", ((0, 2), (1, 2), (0, 3), (5, 0), (3, 5), (4, 1))
)
def test_fin_signed_axes(node_type, axes):
    """符号付き主軸と補助軸へ非対称 Fin の向きが追従する。"""
    _, shape = _create(node_type)
    case = CASES[9]
    _set_case(shape, case)
    cmds.setAttr(shape + ".s1a", axes[0])
    cmds.setAttr(shape + ".s2a", axes[1])
    cmds.setAttr(shape + ".sfn", True)
    assert _bounds(shape) == pytest.approx(_expected(case[4], case[5], axes))


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_fin_height_uses_scene_distance_units(node_type):
    """高さだけが距離単位へ追従し、幅倍率は単位から独立する。"""
    _, shape = _create(node_type)
    cmds.currentUnit(linear="mm")
    assert cmds.getAttr(shape + ".sfnh") == pytest.approx(5)
    cmds.setAttr(shape + ".sfn", True)
    cmds.setAttr(shape + ".sfnh", 10)
    assert cmds.getAttr(shape + ".sfnws") == 1
    assert _bounds(shape) == pytest.approx((-0.5, -0.5, -0.5, 0.5, 1.5, 0.5))


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "extension,file_type", (("ma", "mayaAscii"), ("mb", "mayaBinary"))
)
def test_fin_hidden_edit_undo_duplicate_save(
    node_type, extension, file_type, tmp_path
):
    """非表示中の更新、編集履歴、独立した複製、保存復元を検証する。"""
    parent, shape = _create(node_type)
    original = _bounds(shape)
    cmds.setAttr(parent + ".visibility", False)
    cmds.undoInfo(openChunk=True)
    try:
        _set_case(shape, CASES[4])
        cmds.setAttr(shape + ".sfn", True)
        cmds.setAttr(shape + ".sgl", True)
    finally:
        cmds.undoInfo(closeChunk=True)
    expected = _expected(DEFAULT, CASES[4][5])
    assert _bounds(shape) == pytest.approx(expected)
    cmds.undo()
    assert _bounds(shape) == pytest.approx(original)
    assert cmds.getAttr(shape + ".sfn") is False
    cmds.redo()
    assert _bounds(shape) == pytest.approx(expected)
    copy_parent = cmds.duplicate(parent, returnRootsOnly=True)[0]
    copied = cmds.listRelatives(copy_parent, shapes=True, fullPath=True)[0]
    assert _bounds(copied) == pytest.approx(expected)
    for name, *_ in SPECS:
        assert cmds.getAttr(f"{copied}.{name}") == cmds.getAttr(
            f"{shape}.{name}"
        )
    cmds.setAttr(copied + ".sfn", False)
    assert _bounds(copied) == pytest.approx(original)
    assert _bounds(shape) == pytest.approx(expected)
    filename = tmp_path / ("cube_fin." + extension)
    cmds.file(rename=str(filename))
    cmds.file(save=True, type=file_type, force=True)
    cmds.file(new=True, force=True)
    cmds.file(str(filename), open=True, force=True)
    assert _bounds(shape) == pytest.approx(expected)
    assert cmds.getAttr(shape + ".sfn") is True
    assert cmds.getAttr(shape + ".sfnt") == 1
    assert cmds.getAttr(shape + ".sfnws") == -2
    assert cmds.getAttr(shape + ".sgl") is True
    assert _bounds(copied) == pytest.approx(original)
    assert cmds.getAttr(copied + ".sfn") is False


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_fin_node_operator_modifiers(node_type):
    """公開型の属性と短縮名を modifier の実行・Undo・Redo で辿る。"""
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    _, name = _create(node_type)
    if node_type == NODE_TYPES[0]:
        shape = bd_nodes.existing.bdCtrlShpL_Cube(name)
        assert isinstance(shape, bdu.node_types.BdCtrlShpLCube)
    else:
        shape = bd_nodes.existing.bdCtrlShpL_DeformableCube(name)
        assert isinstance(shape, bdu.node_types.BdCtrlShpLDeformableCube)
    shape.sfn.set(True)
    shape.sfnt.set(shape.sfnt.TAPERED)
    shape.sfnh.set(0.75)
    shape.sfnws.set(-2)
    assert shape.shapeFin.get() is False
    mod.do_it_dg()
    assert shape.shapeFin.get() is True
    assert shape.shapeFinType.get() == shape.sfnt.TAPERED
    assert shape.shapeFinHeight.get() == pytest.approx(0.75)
    assert shape.shapeFinWidthScale.get() == -2
    expected = (-1, -0.5, -0.5, 1, 1.25, 0.5)
    assert _bounds(shape.full_path) == pytest.approx(expected)
    mod.undo_it()
    assert shape.shapeFin.get() is False
    assert _bounds(shape.full_path) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    mod.redo_it()
    assert _bounds(shape.full_path) == pytest.approx(expected)


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_fin_disabled_parameter_edits_take_effect_on_enable(node_type):
    """OFF 中は本体境界を保ち、再表示で最後の寸法を反映する。"""
    _, shape = _create(node_type)
    original = _bounds(shape)
    for kind, height, width in ((0, 2, 3), (1, -2, -3), (1, 0.75, 0)):
        for name, value in (
            ("sfnt", kind),
            ("sfnh", height),
            ("sfnws", width),
        ):
            cmds.setAttr(shape + "." + name, value)
            assert _bounds(shape) == pytest.approx(original)
    cmds.setAttr(shape + ".sfn", True)
    assert _bounds(shape) == pytest.approx((-0.5, -0.5, -0.5, 0.5, 1.25, 0.5))
    cmds.setAttr(shape + ".sfn", False)
    cmds.setAttr(shape + ".sfnh", 0)
    cmds.setAttr(shape + ".sfnws", 100)
    cmds.setAttr(shape + ".sfn", True)
    assert _bounds(shape) == pytest.approx(original)


def test_fin_deform_matrix_connection_tracks_time():
    """接続行列の再生中も Fin と本体を同じ行列で変形する。"""
    _, shape = _create(NODE_TYPES[1])
    case = CASES[3]
    _set_case(shape, case)
    cmds.setAttr(shape + ".sfn", True)
    driver = cmds.createNode("composeMatrix")
    cmds.setAttr(driver + ".inputScale", -2, 3, 0.5)
    cmds.setAttr(driver + ".inputShear", 0.25, -0.4, 0.15)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=1, value=0)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=10, value=35)
    cmds.connectAttr(driver + ".outputMatrix", shape + ".sdm")
    for frame in (1, 10, 1, 10):
        cmds.currentTime(frame)
        matrix = om.MMatrix(cmds.getAttr(driver + ".outputMatrix"))
        for guide in (False, True):
            cmds.setAttr(shape + ".sgl", guide)
            assert _bounds(shape) == pytest.approx(
                _expected(DEFAULT, case[5], matrix=matrix), abs=1e-7
            )
