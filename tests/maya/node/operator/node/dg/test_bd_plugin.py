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
_FOCUS_SQUARE_TYPE = "bdShpL_FocusBoundingSquare"
_FOCUS_NODE_TYPES = {
    _FOCUS_BOX_TYPE: (0x00142721, "BdShpLFocusBoundingBox"),
    _FOCUS_SQUARE_TYPE: (0x00142722, "BdShpLFocusBoundingSquare"),
}
_FOCUS_MATRIX_ATTR = "shapeTransformMatrix"
_AXIS_FIELDS = ("+X", "-X", "+Y", "-Y", "+Z", "-Z")
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
    }.isdisjoint(node_types)

    type_ids = [
        maya_om.MNodeClass(node_type).typeId.id() for node_type in node_types
    ]
    assert len(type_ids) == len(set(type_ids))
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


@pytest.mark.parametrize("node_type", _FOCUS_NODE_TYPES)
def test_focus_shape_public_type_and_static_attributes(
    node_type, maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    create = getattr(bd_nodes.create.with_transform, node_type)
    transform, shape = create(name="control", shape_name="focusShape")
    bd_nodes.create.bdShpL_Cube(parent=transform, name="cubeShape")
    mod.do_it_dag()

    type_id, class_name = _FOCUS_NODE_TYPES[node_type]
    assert maya_om.MNodeClass(node_type).typeId.id() == type_id
    assert type(shape) is getattr(bdu.node_types, class_name)
    assert bdu.node_types.resolve(node_type) is type(shape)
    existing = getattr(bd_nodes.existing, node_type)(shape.full_path)
    assert existing.m_obj == shape.m_obj
    assert existing.visibility.get() is True
    assert existing.showShape.get() is False

    attrs: list[tuple[str, str, str, bool | int | float]] = [
        ("showShape", "ss", "bool", False)
    ]
    half_unit = maya_om.MDistance.internalToUI(0.5)
    if node_type == _FOCUS_SQUARE_TYPE:
        attrs.extend(
            (
                ("shape1stAxis", "s1a", "enum", 0),
                ("shape2ndAxis", "s2a", "enum", 2),
            )
        )
        distance_names = (("1stAxis", "sbsp1"), ("2ndAxis", "sbsp2"))
    else:
        distance_names = (("X", "sbsx"), ("Y", "sbsy"), ("Z", "sbsz"))
    attrs.extend(
        (
            f"shapeBaseSpace{axis}{side}",
            f"{short}{letter}",
            "doubleLinear",
            half_unit,
        )
        for axis, short in distance_names
        for side, letter in (("Plus", "p"), ("Minus", "m"))
    )
    locator = maya_cmds.createNode("locator")
    assert set(maya_cmds.listAttr(shape.full_path)) - set(
        maya_cmds.listAttr(locator)
    ) == {_FOCUS_MATRIX_ATTR, *(name for name, *_ in attrs)}
    node_class = maya_om.MNodeClass(node_type)
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
        if kind == "enum":
            enum = maya_om.MFnEnumAttribute(node_class.attribute(name))
            assert tuple(enum.fieldName(i) for i in range(6)) == _AXIS_FIELDS


@pytest.mark.parametrize("node_type", _FOCUS_NODE_TYPES)
def test_focus_shape_matrix_attribute(
    node_type, maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    focus = maya_cmds.createNode(node_type)
    plug = f"{focus}.{_FOCUS_MATRIX_ATTR}"

    assert maya_cmds.getAttr(plug, type=True) == "matrix"
    assert (
        maya_cmds.attributeQuery(
            _FOCUS_MATRIX_ATTR, node=focus, attributeType=True
        )
        == "typed"
    )
    assert (
        maya_cmds.attributeQuery(
            _FOCUS_MATRIX_ATTR, node=focus, shortName=True
        )
        == "stm"
    )
    assert maya_cmds.getAttr(f"{focus}.stm") == pytest.approx(
        list(maya_om.MMatrix())
    )
    assert not maya_cmds.getAttr(plug, keyable=True)
    assert not maya_cmds.getAttr(plug, channelBox=True)
    for flag in ("connectable", "storable", "writable"):
        assert maya_cmds.attributeQuery(
            _FOCUS_MATRIX_ATTR, node=focus, **{flag: True}
        )


@pytest.mark.parametrize("node_type", _FOCUS_NODE_TYPES)
def test_focus_shape_matrix_transforms_local_corners(
    node_type, maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(node_type, parent=ctrl)
    (focus,) = maya_cmds.ls(focus, long=True)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    if node_type == _FOCUS_SQUARE_TYPE:
        maya_cmds.setAttr(f"{focus}.shape1stAxis", 1)
        maya_cmds.setAttr(f"{focus}.shape2ndAxis", 4)
        first_axis_plus = "shapeBaseSpace1stAxisPlus"
    else:
        first_axis_plus = "shapeBaseSpaceXPlus"
    maya_cmds.setAttr(
        f"{focus}.{first_axis_plus}", maya_om.MDistance.internalToUI(2.25)
    )
    original = _local_bounds(maya_om, focus)
    matrix = maya_om.MMatrix(
        (
            (0.0, -1.0, 0.5, 0.0),
            (-1.5, 0.25, 0.75, 0.0),
            (0.5, 0.4, 1.4, 0.0),
            (3.0, -2.0, 5.0, 1.0),
        )
    )
    transformed = maya_om.MBoundingBox()
    for corner in product(*zip(original[:3], original[3:], strict=True)):
        transformed.expand(maya_om.MPoint(*corner) * matrix)
    expected = (*tuple(transformed.min)[:3], *tuple(transformed.max)[:3])

    matrix_plug = f"{focus}.stm"
    maya_cmds.setAttr(matrix_plug, *list(matrix), type="matrix")
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)
    assert _local_bounds(maya_om, body) == pytest.approx(_CUBE_BOUNDS)
    maya_cmds.setAttr(matrix_plug, *list(maya_om.MMatrix()), type="matrix")
    assert _local_bounds(maya_om, focus) == pytest.approx(original)
    maya_cmds.setAttr(f"{focus}.showShape", False)
    assert _local_bounds(maya_om, focus) == pytest.approx(original)

    maya_cmds.setAttr(matrix_plug, *list(matrix), type="matrix")
    maya_cmds.setAttr(f"{focus}.showShape", True)
    (duplicate,) = maya_cmds.duplicate(ctrl)
    duplicated_focus, _ = maya_cmds.listRelatives(
        duplicate, shapes=True, fullPath=True
    )
    assert _local_bounds(maya_om, duplicated_focus) == pytest.approx(expected)
    scene_path = tmp_path / "focus_matrix.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{focus}.showShape")
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)


@pytest.mark.parametrize("node_type", _FOCUS_NODE_TYPES)
def test_focus_shape_connected_matrix_frames_at_current_time(
    node_type, maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(node_type, parent=ctrl)
    original = _local_bounds(maya_om, focus)
    maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    driver = maya_cmds.createNode("composeMatrix")
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{ctrl}.translateX", to_ui(3.0))
    frames_and_offsets = ((1, 8.0), (10, 13.0))
    for frame, offset in frames_and_offsets:
        maya_cmds.setKeyframe(
            driver,
            attribute="inputTranslateX",
            time=frame,
            value=to_ui(offset),
        )
    source = f"{driver}.outputMatrix"
    destination = f"{focus}.{_FOCUS_MATRIX_ATTR}"
    maya_cmds.connectAttr(source, destination)
    maya_cmds.select(ctrl)

    for visible in (False, True, False):
        maya_cmds.setAttr(f"{focus}.showShape", visible)
        for frame, offset in (*frames_and_offsets, *frames_and_offsets):
            maya_cmds.currentTime(frame)
            assert _framed_x(maya_cmds, maya_om) == pytest.approx(3.0 + offset)
            expected = list(original)
            expected[0] += offset
            expected[3] += offset
            assert _local_bounds(maya_om, focus) == pytest.approx(expected)

    connected_matrix = maya_cmds.getAttr(source)
    maya_cmds.disconnectAttr(source, destination)
    maya_cmds.currentTime(1)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(16.0)
    assert maya_cmds.getAttr(destination) == pytest.approx(connected_matrix)
    assert not maya_cmds.connectionInfo(destination, isDestination=True)
    maya_cmds.setAttr(destination, *list(maya_om.MMatrix()), type="matrix")
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(3.0)
    maya_cmds.connectAttr(source, destination)
    assert _framed_x(maya_cmds, maya_om) == pytest.approx(11.0)


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


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    (
        (0, 2, (1.0, -2.0, 0.0, 3.0, 4.0, 0.0)),
        (1, 4, (-3.0, 0.0, -2.0, -1.0, 0.0, 4.0)),
        (3, 1, (-4.0, -3.0, 0.0, 2.0, -1.0, 0.0)),
        (0, 1, (1.0, -2.0, 0.0, 3.0, 4.0, 0.0)),
        (3, 2, (0.0, -3.0, -2.0, 0.0, -1.0, 4.0)),
        (5, 5, (0.0, -2.0, -3.0, 0.0, 4.0, -1.0)),
    ),
)
def test_planar_focus_shape_bounds_use_oriented_axis_limits(
    first, second, expected, maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    focus = maya_cmds.createNode(_FOCUS_SQUARE_TYPE)
    assert _local_bounds(maya_om, focus) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)
    )

    maya_cmds.setAttr(f"{focus}.shape1stAxis", first)
    maya_cmds.setAttr(f"{focus}.shape2ndAxis", second)
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace1stAxisMinus", to_ui(-1.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace1stAxisPlus", to_ui(3.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace2ndAxisMinus", to_ui(2.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace2ndAxisPlus", to_ui(4.0))
    assert _local_bounds(maya_om, focus) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{focus}.shape2ndAxis") == second


def test_planar_focus_shape_degenerate_bounds_with_sibling_and_preview(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode(_FOCUS_SQUARE_TYPE, parent=ctrl)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace1stAxisMinus", 0.0)
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace1stAxisPlus", 0.0)
    assert _local_bounds(maya_om, focus) == pytest.approx(
        (0.0, -0.5, 0.0, 0.0, 0.5, 0.0)
    )

    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace2ndAxisMinus", to_ui(-2.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpace2ndAxisPlus", to_ui(2.0))
    expected = (0.0, 2.0, 0.0, 0.0, 2.0, 0.0)
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


def test_planar_focus_shape_rejects_incoming_connections(maya_cmds, new_scene):
    _load_bd_util_nodes(maya_cmds)
    focus = maya_cmds.createNode(_FOCUS_SQUARE_TYPE)
    source = maya_cmds.createNode("network")
    for attribute, options in (
        ("showShape", {"attributeType": "bool"}),
        ("shape1stAxis", {"attributeType": "enum", "enumName": "off:on"}),
        ("shapeBaseSpace1stAxisMinus", {"attributeType": "doubleLinear"}),
    ):
        maya_cmds.addAttr(source, longName=attribute, **options)
        destination = f"{focus}.{attribute}"
        with pytest.raises(RuntimeError):
            maya_cmds.connectAttr(f"{source}.{attribute}", destination)
        assert not maya_cmds.connectionInfo(destination, isDestination=True)


@pytest.mark.parametrize("node_type", _FOCUS_NODE_TYPES)
def test_fixed_shape_channel_box_and_focus_override_defaults(
    node_type, maya_cmds, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    cube = maya_cmds.createNode("bdShpL_Cube")
    focus = maya_cmds.createNode(node_type)
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
