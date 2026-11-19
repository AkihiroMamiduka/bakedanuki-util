# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya

_REGISTERED_NODE_ID_START = 0x00142680
_REGISTERED_NODE_ID_END = 0x0014277F


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

    assert len(node_types) == 160

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


def test_focus_box_public_type_and_static_attributes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.with_transform.bdShpL_FocusBoundingBox(
        name="control", shape_name="focusBox"
    )
    bd_nodes.create.bdShpL_Cube(parent=transform, name="cubeShape")
    mod.do_it_dag()

    node_type = "bdShpL_FocusBoundingBox"
    assert maya_om.MNodeClass(node_type).typeId.id() == 0x00142721
    assert type(shape) is bdu.node_types.BdShpLFocusBoundingBox
    assert bdu.node_types.resolve(node_type) is type(shape)
    existing = bd_nodes.existing.bdShpL_FocusBoundingBox(shape.full_path)
    assert existing.m_obj == shape.m_obj
    assert existing.visibility.get() is True
    assert existing.showShape.get() is False

    attrs = [("showShape", "ss", "bool", False)]
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


def test_focus_box_bounds_stay_independent_of_preview_and_sibling(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode("bdShpL_FocusBoundingBox", parent=ctrl)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)

    def bounds(node):
        selection = maya_om.MSelectionList()
        selection.add(node)
        box = maya_om.MFnDagNode(selection.getDagPath(0)).boundingBox
        return (*tuple(box.min)[:3], *tuple(box.max)[:3])

    cube_bounds = (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    assert bounds(focus) == pytest.approx(cube_bounds)
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
    expected = (7.0, 0.0, -1.25, 9.0, 0.0, 2.75)
    assert bounds(focus) == pytest.approx(expected)
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert bounds(focus) == pytest.approx(expected)
    assert bounds(body) == pytest.approx(cube_bounds)

    (duplicate,) = maya_cmds.duplicate(ctrl, name="copy")
    duplicated_focus, _ = maya_cmds.listRelatives(
        duplicate, shapes=True, fullPath=True
    )
    assert bounds(duplicated_focus) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{duplicated_focus}.showShape")


def test_fixed_shape_channel_box_and_focus_override_defaults(
    maya_cmds, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    cube = maya_cmds.createNode("bdShpL_Cube")
    focus = maya_cmds.createNode("bdShpL_FocusBoundingBox")
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


def test_focus_box_frames_first_visible_sibling(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    ctrl = maya_cmds.createNode("transform")
    focus = maya_cmds.createNode("bdShpL_FocusBoundingBox", parent=ctrl)
    body = maya_cmds.createNode("bdShpL_Cube", parent=ctrl)
    to_ui = maya_om.MDistance.internalToUI
    maya_cmds.setAttr(f"{ctrl}.translateX", to_ui(3.0))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXMinus", to_ui(-9.5))
    maya_cmds.setAttr(f"{focus}.shapeBaseSpaceXPlus", to_ui(10.5))
    maya_cmds.select(ctrl)

    def framed_x():
        maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
        x, _, _ = maya_cmds.xform(
            "front", query=True, worldSpace=True, translation=True
        )
        return maya_om.MDistance.uiToInternal(x)

    assert framed_x() == pytest.approx(13.0)
    maya_cmds.reorder(body, front=True)
    assert framed_x() == pytest.approx(3.0)
    maya_cmds.reorder(focus, front=True)
    maya_cmds.setAttr(f"{focus}.visibility", False)
    assert framed_x() == pytest.approx(3.0)
    maya_cmds.setAttr(f"{focus}.visibility", True)
    maya_cmds.setAttr(f"{focus}.showShape", True)
    assert framed_x() == pytest.approx(13.0)

    maya_cmds.setAttr(f"{focus}.showShape", False)
    maya_cmds.setAttr(f"{focus}.overrideVisibility", False)
    maya_cmds.setAttr(f"{focus}.overrideEnabled", lock=False)
    maya_cmds.setAttr(f"{focus}.overrideEnabled", True)
    assert framed_x() == pytest.approx(13.0)


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
