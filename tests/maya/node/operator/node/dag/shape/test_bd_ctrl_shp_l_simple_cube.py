"""軸と六面の位置を持つ Cube の公開契約・境界・履歴を検証する。"""

from __future__ import annotations

from itertools import product

import pytest
from maya import cmds
from maya.api import OpenMaya as om

import bd_util as bdu

from test_bd_shp_l_cube_fin import _bounds, _create, _fn, fin_scene

pytestmark = pytest.mark.maya
NODE_TYPES = ("bdCtrlShpL_SimpleCube", "bdCtrlShpL_DeformableSimpleCube")
ATTRIBUTES = tuple(
    (f"shapeBaseSpace{axis}Axis{side}", f"sbsp{number}{suffix}")
    for number, axis in enumerate(("1st", "2nd", "3rd"), 1)
    for side, suffix in (("Plus", "p"), ("Minus", "m"))
)
AXIS_ATTRIBUTES = (("shape1stAxis", "s1a", 0), ("shape2ndAxis", "s2a", 2))
AXIS_VECTORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DEFAULT = ((-0.5, 0.5),) * 3
ASYMMETRIC = ((1, 3), (-2, 4), (5, 7))
LIMIT_CASES = (
    pytest.param(DEFAULT, id="default"),
    pytest.param(ASYMMETRIC, id="asymmetric"),
    pytest.param(((2, -3), (4, -1), (7, -5)), id="negative-distances"),
    pytest.param(((3, 1), (-2, -4), (7, 5)), id="reversed"),
    pytest.param(((0, 0), (-2, 4), (5, 7)), id="plane"),
    pytest.param(((2, 2), (-3, -3), (-1, 4)), id="line"),
    pytest.param(((2, 2), (-3, -3), (5, 5)), id="point"),
    pytest.param(((0, 0),) * 3, id="zero"),
)
AFFINE = om.MMatrix(
    (
        (-2, 0.5, 0.25, 0),
        (1.5, 3, -0.5, 0),
        (0.25, -0.5, 0.75, 0),
        (4, -5, 6, 1),
    )
)
SINGULAR = om.MMatrix(
    ((0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (4, -5, 6, 1))
)


def _set_limits(shape, limits):
    """内部単位の面位置を、符号付き方向距離へ変換して設定する。"""
    for axis, (minus, plus) in zip(("1st", "2nd", "3rd"), limits):
        cmds.setAttr(
            f"{shape}.shapeBaseSpace{axis}AxisMinus",
            om.MDistance.internalToUI(-minus),
        )
        cmds.setAttr(
            f"{shape}.shapeBaseSpace{axis}AxisPlus",
            om.MDistance.internalToUI(plus),
        )


def _expected(limits, matrix=None, axes=(0, 2)):
    """八頂点を独立に列挙し、必要なら行列を適用して境界を求める。"""
    first, second = axes
    if first // 2 == second // 2:
        second = (2, 2, 4, 4, 2, 2)[first]
    first_vector, second_vector = (
        om.MVector(AXIS_VECTORS[index]) for index in (first, second)
    )
    third_vector = first_vector ^ second_vector
    points = [
        om.MPoint(first_vector * x + second_vector * y + third_vector * z)
        for x, y, z in product(*limits)
    ]
    if matrix is not None:
        points = [point * matrix for point in points]
    return tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))


@pytest.mark.parametrize(
    "node_type,type_id,draw_api",
    (
        (NODE_TYPES[0], 0x00142726, "geometry"),
        (NODE_TYPES[1], 0x00142727, "subscene"),
    ),
)
def test_simple_cube_identity_and_exact_attributes(
    node_type, type_id, draw_api
):
    """新規 ID と二軸・六距離の構成、編集フラグと既定単位を確認する。"""
    _, shape = _create(node_type)
    fn = _fn(shape)
    assert fn.typeId.id() == type_id
    assert cmds.nodeType(shape) == node_type
    assert cmds.getClassification(node_type) == [
        f"drawdb/{draw_api}/{node_type}"
    ]
    assert not cmds.listAttr(shape, userDefined=True)
    locator = cmds.createNode("locator")
    expected = {name for name, _ in ATTRIBUTES} | {
        name for name, _, _ in AXIS_ATTRIBUTES
    }
    if node_type == NODE_TYPES[1]:
        expected.add("shapeDeformMatrix")
    assert set(cmds.listAttr(shape)) - set(cmds.listAttr(locator)) == expected
    assert _bounds(shape) == pytest.approx(_expected(DEFAULT))
    for name, short in ATTRIBUTES:
        plug = shape + "." + name
        attribute = om.MFnUnitAttribute(fn.attribute(name))
        assert attribute.unitType() == om.MFnUnitAttribute.kDistance
        assert fn.findPlug(
            name, False
        ).asMDistance().asCentimeters() == pytest.approx(0.5)
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short
        assert cmds.getAttr(plug, type=True) == "doubleLinear"
        assert cmds.getAttr(plug) == pytest.approx(0.5)
        assert cmds.getAttr(shape + "." + short) == pytest.approx(0.5)
        assert not cmds.getAttr(plug, keyable=True)
        assert not cmds.getAttr(plug, lock=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        for flag in ("readable", "writable", "storable"):
            assert cmds.attributeQuery(name, node=shape, **{flag: True})
        assert not cmds.attributeQuery(name, node=shape, minExists=True)
        assert not cmds.attributeQuery(name, node=shape, maxExists=True)
    for name, short, default in AXIS_ATTRIBUTES:
        plug = shape + "." + name
        assert cmds.attributeQuery(name, node=shape, shortName=True) == short
        assert cmds.getAttr(plug, type=True) == "enum"
        assert cmds.getAttr(plug) == default
        assert cmds.getAttr(shape + "." + short) == default
        assert not cmds.getAttr(plug, keyable=True)
        assert not cmds.getAttr(plug, lock=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        for flag in ("readable", "writable", "storable"):
            assert cmds.attributeQuery(name, node=shape, **{flag: True})
        enum = om.MFnEnumAttribute(fn.attribute(name))
        assert [enum.fieldName(value) for value in range(6)] == [
            "+X",
            "-X",
            "+Y",
            "-Y",
            "+Z",
            "-Z",
        ]
    assert [
        name
        for name in cmds.listAttr(shape, channelBox=True)
        if name in expected
    ] == [
        *(name for name, _, _ in AXIS_ATTRIBUTES),
        *(name for name, _ in ATTRIBUTES),
    ]
    for name in (
        "shapeFin",
        "shapeGuideLine",
        "shapeOffsetLine",
        "shapeSize",
        "_",
        "shapeBaseSpaceXPlus",
        "shapeBaseSpaceXMinus",
    ):
        assert not cmds.attributeQuery(name, node=shape, exists=True)


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize("limits", LIMIT_CASES)
def test_simple_cube_signed_face_positions(node_type, limits):
    """負値・逆転・縮退を含む面位置から正確なローカル境界を得る。"""
    parent, shape = _create(node_type)
    _set_limits(shape, limits)
    expected = _expected(limits)
    assert _bounds(shape) == pytest.approx(expected)
    cmds.setAttr(parent + ".translate", 13, -7, 5)
    cmds.setAttr(parent + ".rotate", 31, -22, 17)
    cmds.setAttr(parent + ".scale", -2, 0, 3)
    assert _bounds(shape) == pytest.approx(expected)


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize("unit", ("mm", "m"))
def test_simple_cube_distance_units(node_type, unit):
    """表示単位を変えても既定サイズと内部距離が変わらない。"""
    cmds.currentUnit(linear=unit)
    _, shape = _create(node_type)
    assert cmds.getAttr(shape + ".sbsp1p") == pytest.approx(
        om.MDistance.internalToUI(0.5)
    )
    assert _bounds(shape) == pytest.approx(_expected(DEFAULT))
    _set_limits(shape, ASYMMETRIC)
    assert _bounds(shape) == pytest.approx(_expected(ASYMMETRIC))


@pytest.mark.parametrize(
    "simple_type,custom_type",
    (
        (NODE_TYPES[0], "bdCtrlShpL_Cube"),
        (NODE_TYPES[1], "bdCtrlShpL_DeformableCube"),
    ),
)
@pytest.mark.parametrize("axes", tuple(product(range(6), repeat=2)))
def test_shared_base_settings_match_custom_cube(
    simple_type, custom_type, axes
):
    """共有八属性を移すだけで符号付き軸・重複軸補正後の形状が一致する。"""
    _, simple = _create(simple_type)
    _, custom = _create(custom_type)
    limits = ((3, 1), (-2, 4), (5, -7))
    matrix = AFFINE if simple_type == NODE_TYPES[1] else None
    for shape in (simple, custom):
        cmds.setAttr(shape + ".s1a", axes[0])
        cmds.setAttr(shape + ".s2a", axes[1])
        _set_limits(shape, limits)
        if matrix is not None:
            cmds.setAttr(shape + ".sdm", *matrix, type="matrix")
        assert _bounds(shape) == pytest.approx(_expected(limits, matrix, axes))
        assert cmds.getAttr(shape + ".s2a") == axes[1]
    assert _bounds(simple) == pytest.approx(_bounds(custom))


@pytest.mark.parametrize("node_type", NODE_TYPES)
def test_simple_cube_shape_inputs_are_static(node_type):
    """直接編集と出力参照は許可し、入力接続とキーを拒否する。"""
    _, shape = _create(node_type)
    source = cmds.createNode("network")
    target = cmds.createNode("network")
    source_fn = om.MFnDependencyNode(
        om.MSelectionList().add(source).getDependNode(0)
    )
    for name, short, kind, value in (
        *((name, short, "doubleLinear", -1.25) for name, short in ATTRIBUTES),
        *((name, short, "long", 4) for name, short, _ in AXIS_ATTRIBUTES),
    ):
        cmds.addAttr(source, longName=name, attributeType=kind)
        cmds.addAttr(target, longName=name, attributeType=kind)
        plug = shape + "." + name
        with pytest.raises(RuntimeError):
            cmds.connectAttr(source + "." + name, plug)
        modifier = om.MDGModifier()
        with pytest.raises(RuntimeError):
            modifier.connect(
                source_fn.findPlug(name, False),
                _fn(shape).findPlug(name, False),
            )
            modifier.doIt()
        assert cmds.setKeyframe(shape, attribute=name, time=1) == 0
        assert not cmds.listConnections(plug, source=True, destination=False)
        cmds.connectAttr(plug, target + "." + name)
        cmds.setAttr(shape + "." + short, value)
        assert cmds.getAttr(target + "." + name) == pytest.approx(value)


@pytest.mark.parametrize("limits", LIMIT_CASES)
@pytest.mark.parametrize(
    "matrix", (AFFINE, SINGULAR), ids=("affine", "singular")
)
def test_simple_deformable_cube_exact_transformed_bounds(limits, matrix):
    """反転・せん断・特異行列は八頂点へ適用してから境界を求める。"""
    _, shape = _create(NODE_TYPES[1])
    _set_limits(shape, limits)
    cmds.setAttr(shape + ".sdm", *matrix, type="matrix")
    assert _bounds(shape) == pytest.approx(_expected(limits, matrix))
    cmds.setAttr(shape + ".sdm", *om.MMatrix(), type="matrix")
    assert _bounds(shape) == pytest.approx(_expected(limits))


def test_simple_deformable_cube_matrix_connection_and_time_updates():
    """行列の既定値・接続契約と時刻変更、距離編集、切断後を確認する。"""
    _, shape = _create(NODE_TYPES[1])
    plug = shape + ".shapeDeformMatrix"
    assert (
        cmds.attributeQuery("shapeDeformMatrix", node=shape, shortName=True)
        == "sdm"
    )
    assert cmds.getAttr(plug, type=True) == "matrix"
    assert cmds.getAttr(plug) == list(om.MMatrix())
    assert not cmds.getAttr(plug, keyable=True)
    assert not cmds.getAttr(plug, channelBox=True)
    for flag in ("readable", "writable", "storable", "connectable"):
        assert cmds.attributeQuery(
            "shapeDeformMatrix", node=shape, **{flag: True}
        )
    driver = cmds.createNode("composeMatrix")
    cmds.connectAttr(driver + ".outputMatrix", plug)
    for frame, value in ((1, 2), (10, -4)):
        cmds.setKeyframe(
            driver, attribute="inputTranslateX", time=frame, value=value
        )
    for frame in (1, 10, 1):
        cmds.currentTime(frame)
        matrix = om.MMatrix(cmds.getAttr(driver + ".outputMatrix"))
        assert _bounds(shape) == pytest.approx(_expected(DEFAULT, matrix))
    _set_limits(shape, ASYMMETRIC)
    assert _bounds(shape) == pytest.approx(_expected(ASYMMETRIC, matrix))
    cmds.disconnectAttr(driver + ".outputMatrix", plug)
    cmds.setAttr(plug, *om.MMatrix(), type="matrix")
    assert _bounds(shape) == pytest.approx(_expected(ASYMMETRIC))


@pytest.mark.parametrize("node_type", NODE_TYPES)
@pytest.mark.parametrize(
    "extension,file_type", (("ma", "mayaAscii"), ("mb", "mayaBinary"))
)
def test_simple_cube_undo_duplicate_and_scene_persistence(
    node_type, extension, file_type, tmp_path
):
    """非表示時の編集、履歴、独立した複製、再読込後の値と境界を確認する。"""
    parent, shape = _create(node_type)
    cmds.setAttr(parent + ".visibility", False)
    original = _bounds(shape)
    cmds.setAttr(shape + ".sbsp1p", 2)
    edited = _bounds(shape)
    assert edited != original
    cmds.undo()
    assert _bounds(shape) == pytest.approx(original)
    cmds.redo()
    assert _bounds(shape) == pytest.approx(edited)
    _set_limits(shape, ASYMMETRIC)
    axes = (4, 1)
    cmds.setAttr(shape + ".s1a", axes[0])
    cmds.setAttr(shape + ".s2a", axes[1])
    matrix = AFFINE if node_type == NODE_TYPES[1] else None
    if matrix is not None:
        cmds.setAttr(shape + ".sdm", *matrix, type="matrix")
    expected = _expected(ASYMMETRIC, matrix, axes)
    duplicate = cmds.duplicate(parent)[0]
    duplicate_shape = cmds.listRelatives(
        duplicate, shapes=True, fullPath=True
    )[0]
    assert cmds.nodeType(duplicate_shape) == node_type
    assert _bounds(duplicate_shape) == pytest.approx(expected)
    cmds.setAttr(duplicate_shape + ".sbsp1p", 8)
    assert _bounds(shape) == pytest.approx(expected)
    values = {
        name: cmds.getAttr(shape + "." + name)
        for name in [
            *(name for name, _ in ATTRIBUTES),
            *(name for name, _, _ in AXIS_ATTRIBUTES),
        ]
    }
    path = tmp_path / ("simple_cube." + extension)
    cmds.file(rename=str(path))
    cmds.file(save=True, type=file_type, force=True)
    cmds.file(new=True, force=True)
    cmds.file(str(path), open=True, force=True)
    assert cmds.nodeType(shape) == node_type
    assert _bounds(shape) == pytest.approx(expected)
    assert not cmds.listAttr(shape, userDefined=True)
    for name, value in values.items():
        assert cmds.getAttr(shape + "." + name) == pytest.approx(value)
    if matrix is not None:
        assert cmds.getAttr(shape + ".sdm") == pytest.approx(list(matrix))


@pytest.mark.parametrize(
    "node_type,class_name",
    (
        (NODE_TYPES[0], "BdCtrlShpLSimpleCube"),
        (NODE_TYPES[1], "BdCtrlShpLDeformableSimpleCube"),
    ),
)
def test_simple_cube_public_node_operator_and_modifier_history(
    node_type, class_name
):
    """公開型、作成・取得 API、短縮名からの遅延編集と履歴を確認する。"""
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = getattr(bd_nodes.create.with_transform, node_type)(
        name="cubeControl"
    )
    assert type(shape) is getattr(bdu.node_types, class_name)
    assert bdu.node_types.resolve(node_type) is type(shape)
    mod.do_it_dag()
    existing = getattr(bd_nodes.existing, node_type)(shape.full_path)
    assert existing.m_obj == shape.m_obj
    assert type(existing) is type(shape)
    assert type(bd_nodes.existing(shape.full_path)) is type(shape)
    shape.shapeBaseSpace1stAxisPlus.set(2)
    shape.sbsp1m.set(-1)
    assert _bounds(shape.full_path) == pytest.approx(_expected(DEFAULT))
    mod.do_it_dg()
    expected = (1, -0.5, -0.5, 2, 0.5, 0.5)
    assert _bounds(shape.full_path) == pytest.approx(expected)
    mod.undo_it()
    assert not cmds.objExists("cubeControl")
    mod.redo_it()
    assert _bounds(shape.full_path) == pytest.approx(expected)


def test_four_cube_types_keep_attribute_handles_and_matrices_independent(
    tmp_path,
):
    """四型を共存させ、別寸法・別行列が複製と保存でも混線しない。"""
    records = []
    for index, node_type in enumerate(
        (
            NODE_TYPES[0],
            "bdCtrlShpL_Cube",
            NODE_TYPES[1],
            "bdCtrlShpL_DeformableCube",
        )
    ):
        parent, shape = _create(node_type)
        assert _bounds(shape) == pytest.approx(_expected(DEFAULT))
        limits = ((index + 1, index + 3), (-2, 4), (5, 7))
        _set_limits(shape, limits)
        matrix = None
        if "Deformable" in node_type:
            driver = cmds.createNode("composeMatrix")
            cmds.setAttr(
                driver + ".inputTranslate", index * 3, -index, index + 2
            )
            cmds.setAttr(driver + ".inputScale", -index, 0.5, 2)
            cmds.connectAttr(driver + ".outputMatrix", shape + ".sdm")
            matrix = om.MMatrix(cmds.getAttr(driver + ".outputMatrix"))
        records.append((parent, shape, node_type, _expected(limits, matrix)))
    for parent, shape, node_type, expected in records:
        assert _bounds(shape) == pytest.approx(expected)
        duplicate = cmds.duplicate(parent, inputConnections=True)[0]
        duplicate_shape = cmds.listRelatives(
            duplicate, shapes=True, fullPath=True
        )[0]
        assert cmds.nodeType(duplicate_shape) == node_type
        assert _bounds(duplicate_shape) == pytest.approx(expected)
    path = tmp_path / "four_cube_types.ma"
    cmds.file(rename=str(path))
    cmds.file(save=True, type="mayaAscii", force=True)
    cmds.file(new=True, force=True)
    cmds.file(str(path), open=True, force=True)
    for _, shape, node_type, expected in records:
        assert cmds.nodeType(shape) == node_type
        assert _bounds(shape) == pytest.approx(expected)
