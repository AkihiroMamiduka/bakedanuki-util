# coding: utf-8
from __future__ import annotations

import os
from itertools import product
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya

_REGISTERED_NODE_ID_START = 0x00142680
_REGISTERED_NODE_ID_END = 0x0014277F
_FOCUS_BOX_TYPE = "bdShpL_FocusBoundingBox"
_DEFORMABLE_CUBE_TYPE = "bdShpL_DeformableCube"
_CUBE_BOUNDS = (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)


def _load_bd_util_nodes(maya_cmds) -> str:
    default_path = (
        Path(__file__).resolve().parents[6]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip(
            "bdUtilNodes.mll is not built. "
            "Run scripts/build-native-maya2025.cmd first."
        )

    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    return plugin_path.stem


def _local_bounds(maya_om, node):
    selection = maya_om.MSelectionList()
    selection.add(node)
    box = maya_om.MFnDagNode(selection.getDagPath(0)).boundingBox
    return (*tuple(box.min)[:3], *tuple(box.max)[:3])


def _framed_x(maya_cmds, maya_om):
    maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
    x, _, _ = maya_cmds.xform(
        "front", query=True, worldSpace=True, translation=True
    )
    return maya_om.MDistance.uiToInternal(x)


def test_plugin_metadata_matches_runtime(maya_cmds):
    plugin_name = _load_bd_util_nodes(maya_cmds)

    assert (
        maya_cmds.pluginInfo(plugin_name, query=True, version=True)
        == bdu.__version__
    )
    assert maya_cmds.pluginInfo(
        plugin_name, query=True, apiVersion=True
    ) == str(maya_cmds.about(apiVersion=True))


def test_node_type_ids_are_unique_and_in_registered_block(maya_cmds, maya_om):
    plugin_name = _load_bd_util_nodes(maya_cmds)
    node_types = maya_cmds.pluginInfo(plugin_name, query=True, dependNode=True)

    assert len(node_types) == 161
    assert {
        "bdShpL_FocusBoundingCrossLine3Axis",
        "bdShpL_FocusBoundingCrossLine",
        "bdShpL_FocusBoundingSquare",
    }.isdisjoint(node_types)

    type_ids = [
        maya_om.MNodeClass(node_type).typeId.id() for node_type in node_types
    ]
    assert len(type_ids) == len(set(type_ids))
    assert 0x00142722 not in type_ids
    assert all(
        _REGISTERED_NODE_ID_START <= type_id <= _REGISTERED_NODE_ID_END
        for type_id in type_ids
    )


def test_fixed_cube_public_creator_and_existing_support_undo_redo(
    maya_cmds, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.with_transform.bdShpL_Cube(
        name="cube_ctrl", shape_name="cubeShape"
    )

    assert isinstance(shape, bdu.node_types.BdShpLCube)
    assert shape.modifier_manager is mod
    mod.do_it_dag()

    assert transform.full_path == "|cube_ctrl"
    assert shape.full_path == "|cube_ctrl|cubeShape"
    assert maya_cmds.nodeType(shape.full_path) == "bdShpL_Cube"
    assert bdu.node_types.resolve("bdShpL_Cube") is type(shape)
    existing = bd_nodes.existing.bdShpL_Cube(shape.full_path)
    assert isinstance(existing, bdu.node_types.BdShpLCube)
    assert existing.m_obj == shape.m_obj
    assert existing.visibility.get() is True

    mod.undo_it()
    assert not maya_cmds.objExists("cube_ctrl")
    mod.redo_it()
    assert shape.full_path == "|cube_ctrl|cubeShape"
    assert maya_cmds.objExists(shape.full_path)


def test_deformable_cube_public_type_and_matrix_input(
    maya_cmds, maya_om, new_scene
):
    """配布ノードの型、作成・取得 API、行列入力の既定値を確認する。"""
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.with_transform.bdShpL_DeformableCube(
        name="control", shape_name="deformableCubeShape"
    )
    fixed = bd_nodes.create.bdShpL_Cube(
        parent=transform, name="fixedCubeShape"
    )
    mod.do_it_dag()

    assert maya_om.MNodeClass(_DEFORMABLE_CUBE_TYPE).typeId.id() == 0x00142723
    assert maya_cmds.getClassification(_DEFORMABLE_CUBE_TYPE) == [
        f"drawdb/subscene/{_DEFORMABLE_CUBE_TYPE}"
    ]
    assert type(shape) is bdu.node_types.BdShpLDeformableCube
    assert bdu.node_types.resolve(_DEFORMABLE_CUBE_TYPE) is type(shape)
    assert (
        bd_nodes.existing.bdShpL_DeformableCube(shape.full_path).m_obj
        == shape.m_obj
    )
    assert set(maya_cmds.listAttr(shape.full_path)) - set(
        maya_cmds.listAttr(fixed.full_path)
    ) == {"shapeDeformMatrix"}
    assert _local_bounds(maya_om, shape.full_path) == _CUBE_BOUNDS
    assert (
        maya_cmds.attributeQuery(
            "shapeDeformMatrix", node=shape.full_path, shortName=True
        )
        == "sdm"
    )
    plug = f"{shape.full_path}.sdm"
    assert maya_cmds.getAttr(plug, type=True) == "matrix"
    assert maya_cmds.getAttr(plug) == list(maya_om.MMatrix())
    assert not maya_cmds.getAttr(plug, keyable=True)
    assert not maya_cmds.getAttr(plug, channelBox=True)
    for flag in ("storable", "connectable", "writable"):
        assert maya_cmds.attributeQuery(
            "shapeDeformMatrix", node=shape.full_path, **{flag: True}
        )
    assert not maya_cmds.attributeQuery(
        "shapeBaseSpace1stAxisPlus", node=shape.full_path, connectable=True
    )

    matrix = maya_om.MTransformationMatrix()
    matrix.setTranslation(
        maya_om.MVector(2.0, 0.0, 0.0), maya_om.MSpace.kTransform
    )
    edit_mod = bdu.ModifierManager()
    edit_nodes = bdu.Nodes(modifier_manager=edit_mod)
    edit_shape = edit_nodes.existing.bdShpL_DeformableCube(shape.full_path)
    edit_shape.shapeDeformMatrix.set(matrix.asMatrix())
    edit_mod.do_it_dg()
    assert _local_bounds(maya_om, shape.full_path) == (
        1.5,
        -0.5,
        -0.5,
        2.5,
        0.5,
        0.5,
    )
    edit_mod.undo_it()
    assert _local_bounds(maya_om, shape.full_path) == _CUBE_BOUNDS


def test_deformable_cube_affine_bounds_duplicate_and_save(
    maya_cmds, maya_om, new_scene, tmp_path
):
    """軸・寸法の後に行列を適用し、複製と保存でも同じ境界を復元する。"""
    _load_bd_util_nodes(maya_cmds)
    parent = maya_cmds.createNode("joint", name="deformCtrl")
    shape = maya_cmds.createNode(
        _DEFORMABLE_CUBE_TYPE, parent=parent, name="deformShape"
    )
    maya_cmds.setAttr(f"{parent}.jointOrient", 23, 17, 11)
    parent_matrix = maya_cmds.getAttr(f"{parent}.worldMatrix[0]")
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 1)
    maya_cmds.setAttr(
        f"{shape}.shapeBaseSpace1stAxisPlus",
        maya_om.MDistance.internalToUI(1.25),
    )
    matrix = maya_om.MMatrix(
        (
            (-2.0, 0.5, 0.25, 0.0),
            (1.5, 3.0, -0.5, 0.0),
            (0.25, -0.5, 0.75, 0.0),
            (4.0, -5.0, 6.0, 1.0),
        )
    )
    maya_cmds.setAttr(f"{shape}.sdm", *list(matrix), type="matrix")
    points = [
        maya_om.MPoint(*point) * matrix
        for point in product((-0.5, 0.5), (-0.5, 0.5), (-0.5, 1.25))
    ]
    expected = tuple(
        extreme(point[axis] for point in points)
        for extreme in (min, max)
        for axis in range(3)
    )
    assert _local_bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{parent}.worldMatrix[0]") == parent_matrix

    (duplicate,) = maya_cmds.duplicate(parent, name="duplicateCtrl")
    (duplicate_shape,) = maya_cmds.listRelatives(
        duplicate, shapes=True, fullPath=True
    )
    assert _local_bounds(maya_om, duplicate_shape) == pytest.approx(expected)

    path = tmp_path / "deformable_cube.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _local_bounds(maya_om, f"|{parent}|{shape}") == pytest.approx(
        expected
    )
    assert _local_bounds(maya_om, duplicate_shape) == pytest.approx(expected)


def test_deformable_cube_connected_matrix_follows_time_and_disconnects(
    maya_cmds, maya_om, new_scene
):
    """接続中は現在値を読み、切断後は保持値を使って形状を更新する。"""
    _load_bd_util_nodes(maya_cmds)
    shape = maya_cmds.createNode(_DEFORMABLE_CUBE_TYPE)
    driver = maya_cmds.createNode("transform")
    maya_cmds.setKeyframe(driver, attribute="scaleX", time=1, value=1)
    maya_cmds.setKeyframe(driver, attribute="scaleX", time=12, value=5)
    source, destination = f"{driver}.matrix", f"{shape}.shapeDeformMatrix"
    maya_cmds.connectAttr(source, destination)
    for frame, half_width in ((1, 0.5), (12, 2.5), (1, 0.5), (12, 2.5)):
        maya_cmds.currentTime(frame)
        assert _local_bounds(maya_om, shape) == pytest.approx(
            (-half_width, -0.5, -0.5, half_width, 0.5, 0.5)
        )
    maya_cmds.disconnectAttr(source, destination)
    maya_cmds.currentTime(1)
    assert _local_bounds(maya_om, shape) == pytest.approx(
        (-2.5, -0.5, -0.5, 2.5, 0.5, 0.5)
    )
    maya_cmds.setAttr(destination, *list(maya_om.MMatrix()), type="matrix")
    assert _local_bounds(maya_om, shape) == _CUBE_BOUNDS


def test_focus_shape_public_type_and_static_attributes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.with_transform.bdShpL_FocusBoundingBox(
        name="control", shape_name="focusShape"
    )
    bd_nodes.create.bdShpL_Cube(parent=transform, name="cubeShape")
    mod.do_it_dag()

    assert maya_om.MNodeClass(_FOCUS_BOX_TYPE).typeId.id() == 0x00142721
    assert type(shape) is bdu.node_types.BdShpLFocusBoundingBox
    assert bdu.node_types.resolve(_FOCUS_BOX_TYPE) is type(shape)
    existing = bd_nodes.existing.bdShpL_FocusBoundingBox(shape.full_path)
    assert existing.m_obj == shape.m_obj
    assert existing.visibility.get() is True
    assert existing.showShape.get() is False
    for name in ("shapeTransformMatrix", "stm"):
        assert not maya_cmds.attributeQuery(
            name, node=shape.full_path, exists=True
        )
        assert not hasattr(type(existing), name)

    attrs: list[tuple[str, str, str, bool | float]] = [
        ("showShape", "ss", "bool", False)
    ]
    half_unit = maya_om.MDistance.internalToUI(0.5)
    attrs.extend(
        (
            f"shapeBaseSpace{axis}{side}",
            f"sbs{axis.lower()}{letter}",
            "doubleLinear",
            half_unit,
        )
        for axis in "XYZ"
        for side, letter in (("Plus", "p"), ("Minus", "m"))
    )
    locator = maya_cmds.createNode("locator")
    assert set(maya_cmds.listAttr(shape.full_path)) - set(
        maya_cmds.listAttr(locator)
    ) == {name for name, *_ in attrs}
    for name, short, kind, default in attrs:
        plug = f"{shape.full_path}.{name}"
        assert (
            maya_cmds.attributeQuery(
                name, node=shape.full_path, shortName=True
            )
            == short
        )
        assert maya_cmds.getAttr(plug, type=True) == kind
        assert maya_cmds.getAttr(
            f"{shape.full_path}.{short}"
        ) == pytest.approx(default)
        assert not maya_cmds.getAttr(plug, keyable=True)
        assert maya_cmds.getAttr(plug, channelBox=True)
        assert not maya_cmds.attributeQuery(
            name, node=shape.full_path, connectable=True
        )
        assert maya_cmds.attributeQuery(
            name, node=shape.full_path, storable=True
        )


def test_focus_shape_static_bounds_survive_scene_round_trip(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE, parent=ctrl)
    (focus,) = maya_cmds.ls(focus, long=True)
    expected = (-0.5, -0.5, -0.5, 2.25, 0.5, 0.5)
    maya_cmds.setAttr(
        f"{focus}.shapeBaseSpaceXPlus", maya_om.MDistance.internalToUI(2.25)
    )
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)

    scene_path = tmp_path / "focus_static.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{focus}.showShape")
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)


def test_focus_shape_frames_follow_keyed_parent_at_current_time(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE, parent=ctrl)
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXMinus", to_ui(-1.25))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXPlus", to_ui(2.25))
    original = _local_bounds(maya_om, focus)
    maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    frames_and_offsets = ((1, 3.0), (10, 13.0))
    for frame, offset in frames_and_offsets:
        maya_cmds.setKeyframe(
            ctrl,
            attribute="translateX",
            time=frame,
            value=to_ui(offset),
        )
    maya_cmds.select(ctrl)

    for visible in (False, True):
        maya_cmds.setAttr(f"{focus}.showShape", visible)
        for frame, offset in (*frames_and_offsets, *frames_and_offsets):
            maya_cmds.currentTime(frame)
            assert _framed_x(maya_cmds, maya_om) == pytest.approx(
                offset + 1.75
            )
            assert _local_bounds(maya_om, focus) == pytest.approx(original)


def test_focus_shape_bounds_stay_independent_of_preview_and_sibling(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE, parent=ctrl)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)

    assert _local_bounds(maya_om, focus) == pytest.approx(_CUBE_BOUNDS)
    for attr, value in (
        ("shapeBaseSpaceXPlus", 7.0),
        ("shapeBaseSpaceXMinus", -9.0),
        ("shapeBaseSpaceYPlus", 0.0),
        ("shapeBaseSpaceYMinus", 0.0),
        ("shapeBaseSpaceZPlus", 2.75),
        ("shapeBaseSpaceZMinus", 1.25),
    ):
        maya_cmds.setAttr(
            f"{focus}.{attr}", maya_om.MDistance.internalToUI(value)
        )
    assert _local_bounds(maya_om, focus) == pytest.approx(
        (7.0, 0.0, -1.25, 9.0, 0.0, 2.75)
    )
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceYMinus", to_ui(-2.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceYPlus", to_ui(5.0))
    expected = (7.0, 2.0, -1.25, 9.0, 5.0, 2.75)
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)
    assert _local_bounds(maya_om, body) == pytest.approx(_CUBE_BOUNDS)

    (duplicate,) = maya_cmds.duplicate(ctrl, name="copy")
    duplicated_focus, _ = maya_cmds.listRelatives(
        duplicate, shapes=True, fullPath=True
    )
    assert _local_bounds(maya_om, duplicated_focus) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{duplicated_focus}.showShape")


def test_focus_shape_rejects_incoming_connections_and_keys(
    maya_cmds, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE)
    source = maya_cmds.createNode("network")
    for attribute, kind in (
        ("showShape", "bool"),
        ("shapeBaseSpaceXMinus", "doubleLinear"),
    ):
        maya_cmds.addAttr(source, longName=attribute, attributeType=kind)
        destination = f"{focus}.{attribute}"
        with pytest.raises(RuntimeError):
            maya_cmds.connectAttr(f"{source}.{attribute}", destination)
        assert not maya_cmds.connectionInfo(destination, isDestination=True)
        assert maya_cmds.setKeyframe(focus, attribute=attribute, time=1) == 0
        assert (
            maya_cmds.keyframe(destination, query=True, keyframeCount=True)
            == 0
        )


def test_fixed_shape_channel_box_and_focus_override_defaults(
    maya_cmds, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    cube = maya_cmds.createNode("bdShpL_Cube")
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE)
    locator = maya_cmds.createNode("locator")

    for attribute in ("localPosition", "localScale"):
        for axis in "XYZ":
            name = f"{attribute}{axis}"
            for shape in (cube, focus):
                plug = f"{shape}.{name}"
                assert not maya_cmds.getAttr(plug, channelBox=True)
                assert not maya_cmds.getAttr(plug, keyable=True)
            assert maya_cmds.getAttr(f"{locator}.{name}", channelBox=True)

    focus_override = f"{focus}.overrideEnabled"
    assert maya_cmds.getAttr(focus_override, lock=True)
    with pytest.raises(RuntimeError):
        maya_cmds.setAttr(focus_override, True)
    assert not maya_cmds.getAttr(focus_override)

    for shape in (cube, locator):
        assert not maya_cmds.getAttr(f"{shape}.overrideEnabled", lock=True)


def test_focus_shape_frames_first_visible_sibling(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(_FOCUS_BOX_TYPE, parent=ctrl)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{ctrl}.translateX", to_ui(3.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXMinus", to_ui(-9.5))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXPlus", to_ui(10.5))
    maya_cmds.select(ctrl)

    assert _framed_x(maya_cmds, maya_om) == pytest.approx(13.0)
    maya_cmds.reorder(body, front=True)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(3.0)
    maya_cmds.reorder(focus, front=True)
    maya_cmds.setAttr(f"{focus}.visibility", False)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(3.0)
    maya_cmds.setAttr(f"{focus}.visibility", True)
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(13.0)

    maya_cmds.setAttr(f"{focus}.showShape", False)
    maya_cmds.setAttr(f"{focus}.overrideVisibility", False)
    maya_cmds.setAttr(f"{focus}.overrideEnabled", lock=False)
    maya_cmds.setAttr(f"{focus}.overrideEnabled", True)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(13.0)


@pytest.mark.parametrize(
    ("extension", "file_type"),
    (("ma", "mayaAscii"), ("mb", "mayaBinary")),
)
def test_registered_nodes_round_trip(
    maya_cmds,
    maya_om,
    new_scene,
    tmp_path,
    extension,
    file_type,
):
    plugin_name = _load_bd_util_nodes(maya_cmds)
    node_types = maya_cmds.pluginInfo(plugin_name, query=True, dependNode=True)
    expected_nodes = {}
    for index, node_type in enumerate(node_types):
        node_name = maya_cmds.createNode(
            node_type, name=f"bd_round_trip_{index:03d}"
        )
        expected_nodes[node_name] = (
            node_type,
            maya_om.MNodeClass(node_type).typeId.id(),
        )

    scene_path = tmp_path / f"bd_util_nodes.{extension}"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type=file_type, force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    for node_name, (node_type, type_id) in expected_nodes.items():
        assert maya_cmds.nodeType(node_name) == node_type

        selection = maya_om.MSelectionList()
        selection.add(node_name)
        node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
        assert node_fn.typeId.id() == type_id
