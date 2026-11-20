"""Cube の形状調整・アニメーション・保存を本体と研究用 DLL で共通検証する。"""

from __future__ import annotations

import os
from itertools import product
from pathlib import Path

import pytest
from maya import cmds
from maya.api import OpenMaya as om

pytestmark = pytest.mark.maya

AXES = ("1st", "2nd", "3rd")
AXIS_VECTORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ATTRIBUTE_SPECS = (
    ("shape1stAxis", "s1a", "enum", 0),
    ("shape2ndAxis", "s2a", "enum", 2),
    *(
        (
            f"shapeBaseSpace{axis}Axis{side}",
            f"sbsp{number}{suffix}",
            "doubleLinear",
            0.5,
        )
        for number, axis in enumerate(AXES, 1)
        for side, suffix in (("Minus", "m"), ("Plus", "p"))
    ),
)
ASYMMETRIC_LIMITS = ((1.0, 3.0), (-2.0, 4.0), (5.0, 7.0))
DEFAULT_LIMITS = ((-0.5, 0.5),) * 3
ANIMATION_MATRIX_ATTR = "shapeTransformMatrix"
RESEARCH_SHAPE_MATRIX = bool(
    os.environ.get("BD_FIXED_CUBE_PLUGIN_PATH")
    and os.environ.get("BD_FIXED_CUBE_EXPECT_SHAPE_MATRIX") == "1"
)
requires_shape_matrix = pytest.mark.skipif(
    not RESEARCH_SHAPE_MATRIX, reason="行列入力を含む研究用 DLL の契約"
)
AFFINE_MATRIX = (
    (-2.0, 0.5, 0.25, 0.0),
    (1.5, 3.0, -0.5, 0.0),
    (0.25, -0.5, 0.75, 0.0),
    (4.0, -5.0, 6.0, 1.0),
)


@pytest.fixture(scope="module")
def cube_plugin():
    """通常は本体を読み込み、研究ランナー指定時は既存の DLL を検証する。"""
    research_path = os.environ.get("BD_FIXED_CUBE_PLUGIN_PATH")
    if research_path:
        plugin_path = Path(research_path).resolve(strict=True)
        plugin_name = os.environ.get(
            "BD_FIXED_CUBE_PLUGIN_NAME", plugin_path.stem
        )
        assert cmds.pluginInfo(plugin_name, query=True, loaded=True)
    else:
        version = int(cmds.about(apiVersion=True)) // 10000
        default_path = (
            Path(__file__).resolve().parents[7]
            / "bakedanuki/bakedanuki-util/plug-ins"
            / f"maya{version}"
            / "bdUtilNodes.mll"
        )
        plugin_path = Path(
            os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
        ).resolve(strict=True)
        cmds.loadPlugin(str(plugin_path), quiet=True)
        plugin_name = plugin_path.stem
    assert (
        Path(cmds.pluginInfo(plugin_name, query=True, path=True)).resolve()
        == plugin_path
    )
    assert (
        int(cmds.pluginInfo(plugin_name, query=True, apiVersion=True)) // 10000
        == int(cmds.about(apiVersion=True)) // 10000
    )
    assert "bdShpL_Cube" in (
        cmds.pluginInfo(plugin_name, query=True, dependNode=True) or []
    )
    prefix = (
        "subscene"
        if plugin_path.stem.startswith("bdShpCubeSubScene")
        else "geometry"
    )
    return plugin_name, prefix


@pytest.fixture(autouse=True)
def scene(cube_plugin):
    """空のシーンと一定の単位で実行し、変更した設定を元へ戻す。"""
    linear = cmds.currentUnit(query=True, linear=True)
    angle = cmds.currentUnit(query=True, angle=True)
    undo = cmds.undoInfo(query=True, state=True)
    cmds.file(new=True, force=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    try:
        yield
    finally:
        cmds.file(new=True, force=True)
        cmds.currentUnit(linear=linear, angle=angle)
        cmds.undoInfo(state=undo)


def _create_cube(parent_type="transform", name="control"):
    """指定した親の直下へ固定 Cube を作成する。"""
    parent = cmds.createNode(parent_type, name=name)
    shape = cmds.createNode("bdShpL_Cube", parent=parent, name=name + "Shape")
    return parent, shape


def _dag_path(name):
    """名前に対応する DAG path を返す。"""
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getDagPath(0)


def _bounds(shape):
    """描画せずにローカル境界を内部単位の cm で取得する。"""
    bounds = om.MFnDagNode(_dag_path(shape)).boundingBox
    return (*tuple(bounds.min)[:3], *tuple(bounds.max)[:3])


def _set_base_space(shape, limits):
    """各軸の端座標を符号付き方向距離へ変換して直接設定する。"""
    for axis, (minus, plus) in zip(AXES, limits):
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus", -minus)
        cmds.setAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus", plus)


def _expected_points(first, second, limits):
    """直交する2軸と外積の第3軸から期待する8端点を求める。"""
    first_vector = om.MVector(AXIS_VECTORS[first])
    second_vector = om.MVector(AXIS_VECTORS[second])
    third_vector = first_vector ^ second_vector
    assert third_vector.length() == 1
    return [
        om.MPoint(first_vector * x + second_vector * y + third_vector * z)
        for x, y, z in product(*limits)
    ]


def _expected_bounds(first, second, limits, matrix=None):
    """期待する8端点を包含する境界を返す。"""
    bounds = om.MBoundingBox()
    for point in _expected_points(first, second, limits):
        bounds.expand(point if matrix is None else point * matrix)
    return (*tuple(bounds.min)[:3], *tuple(bounds.max)[:3])


def test_identity_and_attributes():
    """固有 ID と各属性の型・既定値・編集仕様を検証する。"""
    _, shape = _create_cube()
    fn = om.MFnDependencyNode(_dag_path(shape).node())
    assert fn.typeId.id() == 0x00142720
    assert cmds.nodeType(shape) == "bdShpL_Cube"
    assert not (cmds.listAttr(shape, userDefined=True) or [])
    standard_locator = cmds.createNode("locator")
    attributes = {name for name, *_ in ATTRIBUTE_SPECS}
    if RESEARCH_SHAPE_MATRIX:
        attributes.add(ANIMATION_MATRIX_ATTR)
    else:
        for name in (ANIMATION_MATRIX_ATTR, "stm"):
            assert not cmds.attributeQuery(name, node=shape, exists=True)
    assert (
        set(cmds.listAttr(shape)).difference(cmds.listAttr(standard_locator))
        == attributes
    )
    for name, short_name, kind, default in ATTRIBUTE_SPECS:
        plug = f"{shape}.{name}"
        assert (
            cmds.attributeQuery(name, node=shape, shortName=True) == short_name
        )
        assert cmds.getAttr(plug, type=True) == kind
        assert cmds.getAttr(plug) == pytest.approx(default)
        assert cmds.getAttr(f"{shape}.{short_name}") == pytest.approx(default)
        assert not cmds.getAttr(plug, keyable=True)
        assert cmds.getAttr(plug, channelBox=True)
        assert not cmds.attributeQuery(name, node=shape, connectable=True)
        assert cmds.attributeQuery(name, node=shape, storable=True)
        if kind == "enum":
            enum = om.MFnEnumAttribute(fn.attribute(name))
            assert [enum.fieldName(value) for value in range(6)] == [
                "+X",
                "-X",
                "+Y",
                "-Y",
                "+Z",
                "-Z",
            ]
    for name in ("shape", "shapeFill", "shapeSize"):
        assert not cmds.attributeQuery(name, node=shape, exists=True)


@requires_shape_matrix
def test_animation_matrix_attribute():
    """行列型・短縮名・単位行列の既定値と入力仕様を検証する。"""
    _, shape = _create_cube()
    plug = f"{shape}.{ANIMATION_MATRIX_ATTR}"
    assert cmds.getAttr(plug, type=True) == "matrix"
    assert (
        cmds.attributeQuery(
            ANIMATION_MATRIX_ATTR, node=shape, attributeType=True
        )
        == "typed"
    )
    assert (
        cmds.attributeQuery(ANIMATION_MATRIX_ATTR, node=shape, shortName=True)
        == "stm"
    )
    assert not cmds.getAttr(plug, keyable=True)
    assert not cmds.getAttr(plug, channelBox=True)
    for flag in ("connectable", "storable", "writable"):
        assert cmds.attributeQuery(
            ANIMATION_MATRIX_ATTR, node=shape, **{flag: True}
        )
    fn = om.MFnDependencyNode(_dag_path(shape).node())
    data = om.MFnMatrixData(fn.findPlug("stm", False).asMObject())
    assert list(data.matrix()) == pytest.approx(list(om.MMatrix()))


@pytest.mark.parametrize(
    "first,second",
    [
        (first, second)
        for first, second in product(range(6), repeat=2)
        if first // 2 != second // 2
    ],
)
def test_all_orthogonal_axis_pairs(first, second):
    """24通りの軸指定で非対称寸法の方向と第3軸の符号を検証する。"""
    _, shape = _create_cube()
    cmds.setAttr(shape + ".shape1stAxis", first)
    cmds.setAttr(shape + ".shape2ndAxis", second)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(first, second, ASYMMETRIC_LIMITS)
    )


@pytest.mark.parametrize(
    "first,second",
    [
        (first, second)
        for first, second in product(range(6), repeat=2)
        if first // 2 == second // 2
    ],
)
def test_collinear_axes_use_controller_fallback(first, second):
    """第1軸がY系なら+Z、それ以外なら+Yを第2軸に採用する。"""
    _, shape = _create_cube()
    cmds.setAttr(shape + ".shape1stAxis", first)
    cmds.setAttr(shape + ".shape2ndAxis", second)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    fallback_second = (2, 2, 4, 4, 2, 2)[first]
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(first, fallback_second, ASYMMETRIC_LIMITS)
    )
    assert cmds.getAttr(shape + ".shape2ndAxis") == second


@pytest.mark.parametrize(
    "limits",
    [
        ASYMMETRIC_LIMITS,
        ((2, -3), (4, -5), (6, -7)),
        ((2, 2), (-1, -1), (0, 0)),
        ((0, 2), (-3, 0), (0, 0)),
        ((3, 1), (4, -2), (7, 5)),
    ],
    ids=["asymmetric", "negative_distances", "collapsed", "zero", "reversed"],
)
def test_signed_base_space_endpoints(limits):
    """負値・ゼロ・端の反転を切り詰めず、実際の端点の境界を返す。"""
    _, shape = _create_cube()
    _set_base_space(shape, limits)
    assert _bounds(shape) == pytest.approx(_expected_bounds(0, 2, limits))
    for axis, (minus, plus) in zip(AXES, limits):
        assert cmds.getAttr(f"{shape}.shapeBaseSpace{axis}AxisMinus") == -minus
        assert cmds.getAttr(f"{shape}.shapeBaseSpace{axis}AxisPlus") == plus


@pytest.mark.parametrize("unit,centimeters", [("mm", 0.1), ("m", 100.0)])
def test_base_space_uses_distance_units(unit, centimeters):
    """作成時と編集時の表示単位を変えても、内部の距離と境界を保つ。"""
    cmds.currentUnit(linear=unit)
    _, shape = _create_cube()
    assert _bounds(shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    for name, _, kind, _ in ATTRIBUTE_SPECS:
        if kind == "doubleLinear":
            assert cmds.getAttr(f"{shape}.{name}") == pytest.approx(
                0.5 / centimeters
            )
    cmds.setAttr(shape + ".shapeBaseSpace1stAxisPlus", 2.0)
    expected = (-0.5, -0.5, -0.5, 2.0 * centimeters, 0.5, 0.5)
    assert _bounds(shape) == pytest.approx(expected)
    cmds.currentUnit(linear="cm")
    assert cmds.getAttr(shape + ".shapeBaseSpace1stAxisPlus") == pytest.approx(
        2.0 * centimeters
    )
    assert _bounds(shape) == pytest.approx(expected)


@requires_shape_matrix
def test_direct_animation_matrix_updates_local_bounds_and_undo():
    """軸と寸法の適用後に行列を掛け、親の姿勢を保つ。"""
    parent, shape = _create_cube()
    cmds.setAttr(f"{parent}.translate", 3.0, -4.0, 5.0)
    cmds.setAttr(f"{parent}.rotate", 17.0, -29.0, 23.0)
    original_parent_matrix = list(_dag_path(shape).inclusiveMatrix())
    cmds.setAttr(f"{shape}.shape1stAxis", 4)
    cmds.setAttr(f"{shape}.shape2ndAxis", 1)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    original = _bounds(shape)

    matrix = om.MMatrix(AFFINE_MATRIX)
    cmds.setAttr(f"{shape}.stm", *list(matrix), type="matrix")
    transformed = _expected_bounds(4, 1, ASYMMETRIC_LIMITS, matrix)
    assert _bounds(shape) == pytest.approx(transformed)
    assert list(_dag_path(shape).inclusiveMatrix()) == original_parent_matrix

    cmds.undo()
    assert _bounds(shape) == pytest.approx(original)
    cmds.redo()
    assert _bounds(shape) == pytest.approx(transformed)

    cmds.setAttr(f"{shape}.shape2ndAxis", 3)
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(4, 3, ASYMMETRIC_LIMITS, matrix)
    )


@requires_shape_matrix
def test_connected_animation_matrix_tracks_time_and_disconnect():
    """上流キーの移動・回転と、接続解除時の保持を検証する。"""
    _, shape = _create_cube()
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(0, 2, DEFAULT_LIMITS)
    )
    driver = cmds.createNode("composeMatrix")
    source = f"{driver}.outputMatrix"
    destination = f"{shape}.{ANIMATION_MATRIX_ATTR}"
    cmds.setAttr(f"{driver}.inputScale", -2.0, 3.0, 0.5)
    cmds.setAttr(f"{driver}.inputShear", 0.25, -0.4, 0.15)
    cmds.setKeyframe(driver, attribute="inputTranslateX", time=1, value=1.0)
    cmds.setKeyframe(driver, attribute="inputTranslateX", time=10, value=5.0)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=1, value=0.0)
    cmds.setKeyframe(driver, attribute="inputRotateZ", time=10, value=45.0)
    original_time = cmds.currentTime(query=True)
    try:
        cmds.connectAttr(source, destination)
        bounds_at_frames = []
        for frame in (1, 10, 1, 10):
            cmds.currentTime(frame)
            actual = _bounds(shape)
            current = om.MMatrix(cmds.getAttr(source))
            assert actual == pytest.approx(
                _expected_bounds(0, 2, DEFAULT_LIMITS, current)
            )
            bounds_at_frames.append(actual)
        assert bounds_at_frames[0] != pytest.approx(bounds_at_frames[1])

        cmds.setAttr(f"{shape}.shape1stAxis", 5)
        _set_base_space(shape, ASYMMETRIC_LIMITS)
        expected = _expected_bounds(5, 2, ASYMMETRIC_LIMITS, current)
        assert _bounds(shape) == pytest.approx(expected)

        cmds.disconnectAttr(source, destination)
        cmds.currentTime(1)
        assert not cmds.connectionInfo(destination, isDestination=True)
        assert cmds.getAttr(destination) == pytest.approx(list(current))
        assert _bounds(shape) == pytest.approx(expected)

        cmds.setAttr(destination, *list(om.MMatrix()), type="matrix")
        assert _bounds(shape) == pytest.approx(
            _expected_bounds(5, 2, ASYMMETRIC_LIMITS)
        )
    finally:
        cmds.currentTime(original_time)


def test_bounds_refresh_while_hidden_without_drawing():
    """境界を一度取得した後、非表示中に編集しても古い境界を残さない。"""
    parent, shape = _create_cube()
    assert _bounds(shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    cmds.setAttr(parent + ".visibility", False)
    cmds.setAttr(shape + ".visibility", False)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(0, 2, ASYMMETRIC_LIMITS)
    )
    cmds.setAttr(shape + ".shape1stAxis", 5)
    cmds.setAttr(shape + ".shape2ndAxis", 0)
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(5, 0, ASYMMETRIC_LIMITS)
    )
    _set_base_space(shape, DEFAULT_LIMITS)
    assert _bounds(shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)


@pytest.mark.parametrize("attribute", [name for name, *_ in ATTRIBUTE_SPECS])
def test_shape_settings_reject_incoming_connections_and_keys(attribute):
    """8属性の入力接続とキーを拒否し、形状調整を直接編集に限定する。"""
    _, shape = _create_cube()
    _, source = _create_cube(name="source")
    plug = f"{shape}.{attribute}"
    with pytest.raises(RuntimeError):
        cmds.connectAttr(f"{source}.{attribute}", plug, force=True)
    assert not cmds.connectionInfo(plug, isDestination=True)
    assert cmds.setKeyframe(shape, attribute=attribute, time=1) == 0
    assert cmds.keyframe(plug, query=True, keyframeCount=True) == 0
    assert not cmds.listConnections(plug, source=True, destination=False)


@pytest.mark.parametrize(
    "attribute", ["shape1stAxis", "shapeBaseSpace3rdAxisMinus"]
)
def test_modifier_cannot_bypass_incoming_connection_restriction(attribute):
    """`MDGModifier` からも軸と距離の入力接続を拒否する。"""
    _, shape = _create_cube()
    _, source = _create_cube(name="source")
    destination_fn = om.MFnDependencyNode(_dag_path(shape).node())
    source_fn = om.MFnDependencyNode(_dag_path(source).node())
    modifier = om.MDGModifier()
    with pytest.raises(RuntimeError):
        modifier.connect(
            source_fn.findPlug(attribute, False),
            destination_fn.findPlug(attribute, False),
        )
        modifier.doIt()
    assert not cmds.connectionInfo(f"{shape}.{attribute}", isDestination=True)


def test_shape_settings_can_drive_other_nodes():
    """全8属性を読み出す出力接続は許可し、直接編集した値を伝える。"""
    _, shape = _create_cube()
    target = cmds.createNode("network")
    for name, _, kind, _ in ATTRIBUTE_SPECS:
        cmds.addAttr(
            target,
            longName=name,
            attributeType="long" if kind == "enum" else "doubleLinear",
        )
        cmds.connectAttr(f"{shape}.{name}", f"{target}.{name}")
        value = 5 if kind == "enum" else 2.25
        cmds.setAttr(f"{shape}.{name}", value)
        assert cmds.getAttr(f"{target}.{name}") == pytest.approx(value)


def test_draw_classification_matches_override(cube_plugin):
    """描画方式に対応する分類でノードを登録する。"""
    _, prefix = cube_plugin
    assert cmds.getClassification("bdShpL_Cube") == [
        f"drawdb/{prefix}/bdShpL_Cube"
    ]


@pytest.mark.parametrize("parent_type", ["transform", "joint"])
@pytest.mark.parametrize("adjusted", [False, True])
def test_parent_matrix_and_local_bounds(parent_type, adjusted):
    """形状調整と、pivot・shear・jointOrient を含む親階層を分離する。"""
    group = cmds.createNode("transform", name="group")
    parent, shape = _create_cube(parent_type)
    cmds.parent(parent, group, relative=True)
    cmds.setAttr(group + ".translate", 2, -3, 4)
    cmds.setAttr(group + ".rotate", 11, 22, 33)
    cmds.setAttr(group + ".scale", 1.3, 0.7, 2)
    cmds.setAttr(parent + ".translate", 1, 2, 3)
    cmds.setAttr(parent + ".rotate", 31, -17, 54)
    cmds.setAttr(parent + ".rotateAxis", 7, 19, -13)
    cmds.setAttr(parent + ".scale", -1.2, 0.8, 1.7)
    cmds.setAttr(parent + ".rotateOrder", 4)
    cmds.setAttr(
        parent + ".offsetParentMatrix",
        *list(
            om.MMatrix([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0.3, -0.2, 0.4, 1])
        ),
        type="matrix",
    )
    if parent_type == "joint":
        cmds.setAttr(parent + ".jointOrient", 23, 34, -12)
    else:
        cmds.setAttr(parent + ".shear", 0.25, -0.17, 0.3)
        cmds.setAttr(parent + ".rotatePivot", 0.7, -0.4, 0.2)
        cmds.setAttr(parent + ".scalePivot", -0.3, 0.2, 0.5)
    first, second = (4, 1) if adjusted else (0, 2)
    limits = ASYMMETRIC_LIMITS if adjusted else DEFAULT_LIMITS
    cmds.setAttr(shape + ".shape1stAxis", first)
    cmds.setAttr(shape + ".shape2ndAxis", second)
    _set_base_space(shape, limits)
    path = _dag_path(shape)
    assert _bounds(shape) == pytest.approx(
        _expected_bounds(first, second, limits)
    )
    matrix = path.inclusiveMatrix()
    expected = om.MBoundingBox()
    for point in _expected_points(first, second, limits):
        expected.expand(point * matrix)
    assert cmds.exactWorldBoundingBox(shape) == pytest.approx(
        (*tuple(expected.min)[:3], *tuple(expected.max)[:3])
    )


@pytest.mark.parametrize(
    "uses_matrix",
    [
        pytest.param(False, id="static"),
        pytest.param(True, marks=requires_shape_matrix, id="matrix"),
    ],
)
def test_duplicate_delete_undo(uses_matrix):
    """調整値の複製・複製先の独立編集と、削除後の Undo / Redo を検証する。"""
    parent, shape = _create_cube()
    cmds.setAttr(shape + ".shape1stAxis", 5)
    cmds.setAttr(shape + ".shape2ndAxis", 0)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    if uses_matrix:
        cmds.setAttr(
            f"{shape}.stm", *list(om.MMatrix(AFFINE_MATRIX)), type="matrix"
        )
    original = _bounds(shape)
    duplicate = cmds.duplicate(parent)[0]
    duplicate_shape = cmds.listRelatives(duplicate, shapes=True)[0]
    assert cmds.nodeType(duplicate_shape) == "bdShpL_Cube"
    if uses_matrix:
        assert cmds.getAttr(f"{duplicate_shape}.stm") == cmds.getAttr(
            f"{shape}.stm"
        )
    assert _bounds(duplicate_shape) == pytest.approx(original)
    for name, *_ in ATTRIBUTE_SPECS:
        assert cmds.getAttr(f"{duplicate_shape}.{name}") == cmds.getAttr(
            f"{shape}.{name}"
        )
    cmds.setAttr(duplicate_shape + ".shapeBaseSpace1stAxisPlus", 8)
    assert _bounds(duplicate_shape) != pytest.approx(original)
    assert _bounds(shape) == pytest.approx(original)
    cmds.delete(parent)
    assert not cmds.objExists(shape)
    cmds.undo()
    assert cmds.objExists(shape)
    assert _bounds(shape) == pytest.approx(original)
    cmds.redo()
    assert not cmds.objExists(shape)


def test_direct_edit_undo_redo_updates_cached_bounds():
    """直接編集の Undo / Redo で8属性と取得済み境界を復元する。"""
    _, shape = _create_cube()
    original = _bounds(shape)
    cmds.undoInfo(openChunk=True)
    try:
        cmds.setAttr(shape + ".shape1stAxis", 4)
        cmds.setAttr(shape + ".shape2ndAxis", 1)
        _set_base_space(shape, ASYMMETRIC_LIMITS)
    finally:
        cmds.undoInfo(closeChunk=True)
    adjusted = _expected_bounds(4, 1, ASYMMETRIC_LIMITS)
    assert _bounds(shape) == pytest.approx(adjusted)
    cmds.undo()
    assert _bounds(shape) == pytest.approx(original)
    for name, _, _, default in ATTRIBUTE_SPECS:
        assert cmds.getAttr(f"{shape}.{name}") == pytest.approx(default)
    cmds.redo()
    assert _bounds(shape) == pytest.approx(adjusted)


@pytest.mark.parametrize(
    "extension,file_type", [("ma", "mayaAscii"), ("mb", "mayaBinary")]
)
@pytest.mark.parametrize(
    "uses_matrix",
    [
        pytest.param(False, id="static"),
        pytest.param(True, marks=requires_shape_matrix, id="matrix"),
    ],
)
def test_save_reload(tmp_path, extension, file_type, uses_matrix):
    """再読込後も形状属性、境界、親変換を保持する。"""
    parent, shape = _create_cube()
    cmds.setAttr(parent + ".shearXY", 0.4)
    cmds.setAttr(shape + ".shape1stAxis", 5)
    cmds.setAttr(shape + ".shape2ndAxis", 1)
    _set_base_space(shape, ASYMMETRIC_LIMITS)
    matrix = om.MMatrix(AFFINE_MATRIX) if uses_matrix else None
    if matrix is not None:
        cmds.setAttr(f"{shape}.stm", *list(matrix), type="matrix")
    expected = _expected_bounds(5, 1, ASYMMETRIC_LIMITS, matrix)
    assert _bounds(shape) == pytest.approx(expected)
    values = {
        name: cmds.getAttr(f"{shape}.{name}") for name, *_ in ATTRIBUTE_SPECS
    }
    scene_path = tmp_path / f"fixed_cube.{extension}"
    cmds.file(rename=str(scene_path))
    cmds.file(save=True, type=file_type)
    cmds.file(new=True, force=True)
    cmds.file(str(scene_path), open=True, force=True)
    assert cmds.nodeType(shape) == "bdShpL_Cube"
    assert cmds.getAttr(parent + ".shearXY") == pytest.approx(0.4)
    assert _bounds(shape) == pytest.approx(expected)
    if matrix is not None:
        assert cmds.getAttr(f"{shape}.stm") == pytest.approx(list(matrix))
    for name, value in values.items():
        assert cmds.getAttr(f"{shape}.{name}") == pytest.approx(value)


def test_node_operator_edits_use_modifier_history(monkeypatch):
    """公開型と属性・短縮名から調整し、modifier の履歴で復元する。"""
    package_path = (
        Path(__file__).resolve().parents[7]
        / "bakedanuki/bakedanuki-util/python"
    )
    monkeypatch.syspath_prepend(str(package_path))
    import bd_util as bdu

    _, name = _create_cube()
    original = _bounds(name)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    shape = bd_nodes.existing.bdShpL_Cube(name)
    assert isinstance(shape, bdu.node_types.BdShpLCube)
    assert not hasattr(type(shape), ANIMATION_MATRIX_ATTR)
    assert not hasattr(type(shape), "stm")
    shape.shape1stAxis.set(4)
    shape.s2a.set(1)
    shape.shapeBaseSpace1stAxisMinus.set(-1)
    shape.sbsp1p.set(3)
    shape.shapeBaseSpace2ndAxisMinus.set(2)
    shape.sbsp2p.set(4)
    shape.shapeBaseSpace3rdAxisMinus.set(-5)
    shape.sbsp3p.set(7)
    assert _bounds(name) == pytest.approx(original)
    mod.do_it_dg()
    adjusted = _expected_bounds(4, 1, ASYMMETRIC_LIMITS)
    assert _bounds(name) == pytest.approx(adjusted)
    assert shape.s1a.get() == 4
    assert shape.shape2ndAxis.get() == 1
    assert shape.shapeBaseSpace1stAxisPlus.get() == pytest.approx(3)
    mod.undo_it()
    assert _bounds(name) == pytest.approx(original)
    mod.redo_it()
    assert _bounds(name) == pytest.approx(adjusted)
