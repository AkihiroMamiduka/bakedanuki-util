# coding: utf-8
from __future__ import annotations

import pytest

import bd_util as bdu

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

AXES = ("1st", "2nd", "3rd")
FACE_SCALES = tuple(
    (
        normal,
        side,
        component,
        f"shapeBaseSpace{axis}Axis{side}Scale{other}Axis",
        f"sbsp{normal + 1}{'p' if side == 'Plus' else 'm'}s{component + 1}",
    )
    for normal, axis in enumerate(AXES)
    for side in ("Plus", "Minus")
    for component, other in enumerate(AXES)
    if component != normal
)
FACE_SCALE_PARENTS = tuple(
    (
        normal,
        side,
        f"shapeBaseSpace{axis}Axis{side}Scale",
        f"sbsp{normal + 1}{'p' if side == 'Plus' else 'm'}s",
        tuple(component for component in range(3) if component != normal),
        tuple(item[3] for item in FACE_SCALES if item[:2] == (normal, side)),
    )
    for normal, axis in enumerate(AXES)
    for side in ("Plus", "Minus")
)


def _face_bounds(components, values):
    bounds = [-0.5] * 3 + [0.5] * 3
    for component, value in zip(components, values):
        bounds[component] *= max(1, abs(value))
        bounds[component + 3] *= max(1, abs(value))
    return tuple(bounds)


@pytest.mark.parametrize(
    "normal,side,component,attribute,short_name", FACE_SCALES
)
def test_face_scale_children_keep_schema_and_belong_to_the_face_parent(
    maya_cmds, new_scene, normal, side, component, attribute, short_name
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "faceScaleSchema", "Cube")
    assert maya_cmds.getAttr(f"{shape}.{attribute}", type=True) == "double"
    assert maya_cmds.getAttr(f"{shape}.{attribute}") == 1.0
    assert maya_cmds.attributeQuery(
        attribute, node=shape, listDefault=True
    ) == [1.0]
    assert (
        maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
        == short_name
    )
    assert not maya_cmds.attributeQuery(attribute, node=shape, minExists=True)
    assert not maya_cmds.attributeQuery(attribute, node=shape, maxExists=True)
    for flag in ("readable", "writable", "storable"):
        assert maya_cmds.attributeQuery(attribute, node=shape, **{flag: True})
    assert not maya_cmds.attributeQuery(
        attribute, node=shape, connectable=True
    )
    assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
    assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    parent = f"shapeBaseSpace{AXES[normal]}Axis{side}Scale"
    assert maya_cmds.attributeQuery(
        attribute, node=shape, listParent=True
    ) == [parent]
    face = tuple(item[3] for item in FACE_SCALES if item[:2] == (normal, side))
    channels = maya_cmds.listAttr(shape, channelBox=True)
    start = channels.index(parent)
    assert channels[start : start + 3] == [parent, *face]
    maya_cmds.setAttr(f"{shape}.{short_name}", -1.25)
    assert maya_cmds.getAttr(f"{shape}.{attribute}") == -1.25


@pytest.mark.parametrize(
    "normal,side,parent,short_name,components,children", FACE_SCALE_PARENTS
)
def test_face_scale_parents_are_numeric_double2_with_ordered_children(
    maya_cmds,
    maya_om,
    new_scene,
    normal,
    side,
    parent,
    short_name,
    components,
    children,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "faceParentSchema", "Cube")
    assert maya_cmds.getAttr(f"{shape}.{parent}", type=True) == "double2"
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (1, 1)
    assert maya_cmds.attributeQuery(parent, node=shape, listDefault=True) == [
        1,
        1,
    ]
    assert (
        maya_cmds.attributeQuery(parent, node=shape, shortName=True)
        == short_name
    )
    assert maya_cmds.attributeQuery(
        parent, node=shape, numberOfChildren=True
    ) == [2]
    assert maya_cmds.attributeQuery(
        parent, node=shape, listChildren=True
    ) == list(children)
    assert not maya_cmds.attributeQuery(parent, node=shape, listParent=True)
    for flag in ("readable", "writable", "storable"):
        assert maya_cmds.attributeQuery(parent, node=shape, **{flag: True})
    assert not maya_cmds.attributeQuery(parent, node=shape, connectable=True)
    assert not maya_cmds.getAttr(f"{shape}.{parent}", keyable=True)
    assert maya_cmds.getAttr(f"{shape}.{parent}", channelBox=True)
    selection = maya_om.MSelectionList()
    selection.add(shape)
    plug = maya_om.MFnDependencyNode(selection.getDependNode(0)).findPlug(
        parent, False
    )
    assert (
        maya_om.MFnNumericAttribute(plug.attribute()).numericType()
        == maya_om.MFnNumericData.k2Double
    )
    assert plug.isCompound and plug.numChildren() == 2
    assert (
        tuple(
            maya_om.MFnAttribute(plug.child(i).attribute()).name
            for i in range(2)
        )
        == children
    )
    assert maya_cmds.getAttr(f"{shape}.{short_name}")[0] == (1, 1)


@pytest.mark.parametrize(
    "normal,side,parent,short_name,components,children", FACE_SCALE_PARENTS
)
@pytest.mark.parametrize("filled", (False, True))
def test_face_scale_parent_bulk_set_updates_both_children_and_invalidates_bounds(
    maya_cmds,
    maya_om,
    new_scene,
    normal,
    side,
    parent,
    short_name,
    components,
    children,
    filled,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "bulkFaceScale", "Cube", shapeFill=filled)
    assert _bounds(maya_om, shape) == (-0.5,) * 3 + (0.5,) * 3
    for pair in ((2, 3), (-2, 0.25), (0, 0), (1, 1)):
        maya_cmds.setAttr(f"{shape}.{short_name}", *pair, type="double2")
        assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == pair
        assert (
            tuple(maya_cmds.getAttr(f"{shape}.{child}") for child in children)
            == pair
        )
        assert _bounds(maya_om, shape) == pytest.approx(
            _face_bounds(components, pair), abs=1e-9
        )


@pytest.mark.parametrize(
    "normal,side,parent,short_name,components,children", FACE_SCALE_PARENTS
)
def test_face_scale_parent_api_bulk_set_supports_modifier_undo_redo(
    maya_cmds,
    maya_om,
    new_scene,
    normal,
    side,
    parent,
    short_name,
    components,
    children,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "undoFaceParent", "Cube")
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    node = bd_nodes.existing(shape)
    field = getattr(node, parent)
    field.set((2, 3))
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (1, 1)
    mod.do_it_dg()
    assert field.get() == pytest.approx((2, 3))
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (2, 3)), abs=1e-9
    )
    mod.undo_it()
    assert field.get() == pytest.approx((1, 1))
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    mod.redo_it()
    assert field.get() == pytest.approx((2, 3))
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (2, 3)), abs=1e-9
    )


@pytest.mark.parametrize(
    "normal,side,parent,short_name,components,children", FACE_SCALE_PARENTS
)
def test_face_scale_parent_and_single_child_direct_edits_both_dirty_geometry(
    maya_cmds,
    maya_om,
    new_scene,
    tmp_path,
    normal,
    side,
    parent,
    short_name,
    components,
    children,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "directFaceParent", "Cube")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(shape)
    getattr(node, parent).set(2, 3)
    mod.do_it_dg()
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (2, 3)), abs=1e-9
    )
    mod.undo_it()
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (1, 1)
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    mod.redo_it()
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (2, 3)
    maya_cmds.setAttr(f"{shape}.{parent}", 4, 0.5, type="double2")
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (4, 0.5)), abs=1e-9
    )
    getattr(node, children[0]).set(2.5)
    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (2.5, 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (2.5, 0.5)), abs=1e-9
    )
    scene = tmp_path / "direct_face_parent.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == (2.5, 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (2.5, 0.5)), abs=1e-9
    )
    maya_cmds.setAttr(f"{shape}.{parent}", 3, 4, type="double2")
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, (3, 4)), abs=1e-9
    )


@pytest.mark.parametrize(
    "normal,side,parent,short_name,components,children", FACE_SCALE_PARENTS
)
def test_face_scale_parent_and_child_direct_edits_survive_scene_reload(
    maya_cmds,
    maya_om,
    new_scene,
    tmp_path,
    normal,
    side,
    parent,
    short_name,
    components,
    children,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "directFaceParent", "Cube")
    pairs = ((0.75, 1.5), (-1.25, 2.5), (2, 0))
    for index, pair in enumerate(pairs):
        if index == 1:
            for child, value in zip(children, pair):
                maya_cmds.setAttr(f"{shape}.{child}", value)
        else:
            maya_cmds.setAttr(f"{shape}.{parent}", *pair, type="double2")
        assert maya_cmds.getAttr(f"{shape}.{short_name}")[0] == pytest.approx(
            pair
        )
        assert _bounds(maya_om, shape) == pytest.approx(
            _face_bounds(components, pair), abs=1e-9
        )
    scene = tmp_path / "face_scale_parent.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.attributeQuery(
        parent, node=shape, listChildren=True
    ) == list(children)
    assert maya_cmds.getAttr(f"{shape}.{parent}")[0] == pairs[-1]
    assert _bounds(maya_om, shape) == pytest.approx(
        _face_bounds(components, pairs[-1]), abs=1e-9
    )
    for child in children:
        assert not maya_cmds.connectionInfo(
            f"{shape}.{child}", isDestination=True
        )
        assert (
            maya_cmds.keyframe(
                f"{shape}.{child}", query=True, keyframeCount=True
            )
            == 0
        )


@pytest.mark.parametrize(
    "normal,side,component,attribute,short_name", FACE_SCALES
)
@pytest.mark.parametrize("filled", (False, True))
def test_every_face_scale_invalidates_cached_body_and_keeps_signed_values(
    maya_cmds,
    maya_om,
    new_scene,
    normal,
    side,
    component,
    attribute,
    short_name,
    filled,
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "dirtyFaceScale", "Cube", shapeFill=filled)
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    for value in (2.0, 3.0, 0.0, -2.0, 1.0):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
        expected = [-0.5] * 3 + [0.5] * 3
        expected[component] *= max(1.0, abs(value))
        expected[component + 3] *= max(1.0, abs(value))
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == value


@pytest.mark.parametrize("color", (False, True))
def test_signed_face_scale_changes_plain_shape_but_color_uses_absolute_value(
    maya_cmds, maya_om, new_scene, color
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "signedFaceScale",
        "ColorCrossLine3Axis" if color else "CrossLine3Axis",
    )
    attribute = "shapeBaseSpace2ndAxisPlusScale1stAxis"
    maya_cmds.setAttr(f"{shape}.{attribute}", -1)
    expected = (
        (-0.5,) * 3 + (0.5,) * 3 if color else (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    assert maya_cmds.getAttr(f"{shape}.{attribute}") == -1


def test_face_scales_are_unitless_when_scene_distance_units_change(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        shape = _controller(maya_cmds, "unitlessFaces", "Cube")
        for _, _, _, attribute, _ in FACE_SCALES:
            maya_cmds.setAttr(f"{shape}.{attribute}", 1.5)
        expected = (-1.125,) * 3 + (1.125,) * 3
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        for unit in ("m", "cm"):
            maya_cmds.currentUnit(linear=unit)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
            for _, _, _, attribute, _ in FACE_SCALES:
                assert maya_cmds.getAttr(f"{shape}.{attribute}") == 1.5
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_face_scale_api_direct_edits_undo_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "directFaces", "Cube")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(shape)
    for _, _, _, attribute, _ in FACE_SCALES:
        getattr(node, attribute).set(1.5)
    mod.do_it_dg()
    expected = (-1.125,) * 3 + (1.125,) * 3
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    mod.undo_it()
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    mod.redo_it()
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    for value in (0.75, 1.0, 1.5):
        for _, _, _, attribute, _ in FACE_SCALES:
            maya_cmds.setAttr(f"{shape}.{attribute}", value)
        extent = 0.5 * value * value
        assert _bounds(maya_om, shape) == pytest.approx(
            (-extent,) * 3 + (extent,) * 3, abs=1e-9
        )
    scene = tmp_path / "base_space_face_scales.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    for _, _, _, attribute, _ in FACE_SCALES:
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == 1.5
        assert not maya_cmds.listConnections(
            f"{shape}.{attribute}", source=True, destination=False
        )


def test_custom_bounds_remain_independent_of_all_face_scales(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "separateFaceBounds", "Cube", boundsMode=2)
    for _, _, _, attribute, _ in FACE_SCALES:
        maya_cmds.setAttr(f"{shape}.{attribute}", 4.0)
    maya_cmds.setAttr(f"{shape}.showBoundsPreview", True)
    assert _bounds(maya_om, shape) == pytest.approx((-0.5,) * 3 + (0.5,) * 3)
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    assert _bounds(maya_om, shape) == pytest.approx((-8.0,) * 3 + (8.0,) * 3)
