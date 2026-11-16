from __future__ import annotations

import pytest

import bd_util as bdu

from test_bd_controller_shape import (
    _bounds,
    _create_controller,
    _load_bd_util_nodes,
)

pytestmark = pytest.mark.maya


STATIC_ATTRIBUTES = (
    "shape",
    "shapeAxisSwap",
    "shapeWide",
    "shapeTemplateLine",
    "shapeTemplateLineRate",
    "shapeTemplateLineInvert",
    "shapeTemplateFill",
    "shapePartTemplate",
    "shapeFinTemplate",
    "shapeWideWidth",
    "shapeArcAngle",
    "shapeFill",
    "shapePart",
    "shapePartShape",
    "shapePartType",
    "shapeFin",
    "shapeFinType",
    "shapeFinWidthScale",
    "shapeGuideLine",
    "shapeGuideLineTemplate",
    "shape1stAxis",
    "shape2ndAxis",
    "shapeRootSize",
    "shapeSize",
    "shapePartOffset",
    "shapeFinHeight",
    "shapePartLengthScale",
    "shapePartWidthScale",
    "shapePartHeightScale",
    "shapePartSize",
    "shapePartPrimarySizeScale",
    "shapePartOtherSizeScale",
    "shapeOffsetLine",
    "shapeOffsetLineTemplate",
    *(
        f"shape{prefix}{transform}{component}"
        for prefix in ("", "Axis")
        for transform in ("Translate", "Rotate", "Scale")
        for component in ("", "X", "Y", "Z")
    ),
    *(
        f"shapeBaseSpace{axis}Axis{side}{suffix}"
        for axis in ("1st", "2nd", "3rd")
        for side in ("Minus", "Plus")
        for suffix in (
            "",
            "Scale",
            *(
                f"Scale{other}Axis"
                for other in ("1st", "2nd", "3rd")
                if other != axis
            ),
        )
    ),
)


@pytest.mark.parametrize("attribute", STATIC_ATTRIBUTES)
def test_shape_settings_reject_incoming_connections_and_keys(
    maya_cmds, new_scene, attribute
):
    """形状調整の親子とも、直接編集用の属性として入力接続とキーを拒否する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _, source = _create_controller(maya_cmds, name="staticSource")
    plug = f"{shape}.{attribute}"
    assert not maya_cmds.attributeQuery(
        attribute, node=shape, connectable=True
    )
    assert not maya_cmds.getAttr(plug, keyable=True)
    assert maya_cmds.getAttr(plug, channelBox=True)
    with pytest.raises(RuntimeError):
        maya_cmds.connectAttr(f"{source}.{attribute}", plug, force=True)
    assert not maya_cmds.connectionInfo(plug, isDestination=True)
    assert maya_cmds.setKeyframe(shape, attribute=attribute, time=1) == 0
    assert maya_cmds.keyframe(plug, query=True, keyframeCount=True) == 0
    assert not maya_cmds.listConnections(plug, source=True, destination=False)


@pytest.mark.parametrize(
    "attribute",
    (
        "shape",
        "shapeFill",
        "shapeTranslate",
        "shapeRotateZ",
        "shapeBaseSpace1stAxisPlusScale",
        "shapeBaseSpace1stAxisPlusScale2ndAxis",
    ),
)
def test_modifier_connections_cannot_bypass_static_shape_contract(
    maya_cmds, maya_om, new_scene, attribute
):
    """`MDGModifier` からの入力接続でも静的契約を維持する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _, source = _create_controller(maya_cmds, name="modifierSource")
    selected = maya_om.MSelectionList()
    selected.add(shape)
    selected.add(source)
    destination_fn = maya_om.MFnDependencyNode(selected.getDependNode(0))
    source_fn = maya_om.MFnDependencyNode(selected.getDependNode(1))
    modifier = maya_om.MDGModifier()
    with pytest.raises(RuntimeError):
        modifier.connect(
            source_fn.findPlug(attribute, False),
            destination_fn.findPlug(attribute, False),
        )
        modifier.doIt()
    assert not maya_cmds.connectionInfo(
        f"{shape}.{attribute}", isDestination=True
    )


def test_static_values_can_drive_other_nodes(maya_cmds, new_scene):
    """静的調整値を読み出す出力接続は許可する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    target = maya_cmds.createNode("transform")
    maya_cmds.connectAttr(f"{shape}.shapeTranslate", f"{target}.translate")
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.5, -2, 3)
    assert maya_cmds.getAttr(f"{target}.translate")[0] == (1.5, -2, 3)
    scalar = maya_cmds.createNode("addDoubleLinear")
    maya_cmds.connectAttr(f"{shape}.shapePartOffset", f"{scalar}.input1")
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.75)
    assert maya_cmds.getAttr(f"{scalar}.output") == pytest.approx(0.75)


@pytest.mark.parametrize(
    "attribute,kind,first,last",
    (
        ("shapeLineWidth", "double", 1, 3),
        ("shapeLineTransparency", "double", 0.1, 0.8),
        ("shapeFillTransparency", "double", 0.2, 0.7),
        ("shapeDrawOnTop", "bool", 0, 1),
        ("boundsMode", "long", 0, 2),
        ("showBoundsPreview", "bool", 0, 1),
        ("customBoundsBaseSpaceXPlus", "doubleLinear", 0.5, 1.5),
    ),
)
def test_display_and_bounds_settings_keep_connected_animation(
    maya_cmds, new_scene, attribute, kind, first, last
):
    """表示とBoundsの設定は形状の静的契約から独立して動的入力を許可する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="value", attributeType=kind, keyable=True
    )
    maya_cmds.connectAttr(f"{source}.value", f"{shape}.{attribute}")
    for frame, value in ((1, first), (10, last)):
        maya_cmds.setKeyframe(
            source, attribute="value", time=frame, value=value
        )
    for frame, value in ((1, first), (10, last), (1, first)):
        maya_cmds.currentTime(frame)
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
            value
        )


def test_static_shape_edits_keep_modifier_history_and_scene_values(
    maya_cmds, maya_om, new_scene, tmp_path
):
    """焼込み済みの本体と付属物を直接再調整し、履歴と保存で保持する。"""
    _load_bd_util_nodes(maya_cmds)
    transform, name = _create_controller(maya_cmds, shape_name="Cube")
    original = _bounds(maya_om, name)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shapeFill.set(True)
    shape.shapeTranslate.set(2, -1, 0.5)
    shape.shapeRotate.set(17, 29, 43)
    shape.shapeScale.set(1.5, -2, 0.75)
    shape.shapeBaseSpace1stAxisPlusScale.set(1.25, 0.8)
    shape.shapePart.set(True)
    shape.shapeFin.set(True)
    shape.shapeGuideLine.set(True)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    assert expected != pytest.approx(original)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(original)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    maya_cmds.setKeyframe(transform, attribute="translateX", time=1, value=0)
    maya_cmds.setKeyframe(transform, attribute="translateX", time=10, value=5)
    for frame in (1, 10, 1):
        maya_cmds.currentTime(frame)
        assert _bounds(maya_om, name) == pytest.approx(expected)
    scene = tmp_path / "controller_static_shape.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shapeTranslate")[0] == (2, -1, 0.5)
    assert maya_cmds.getAttr(f"{name}.shapePart")
    assert maya_cmds.getAttr(f"{name}.shapeFin")
    assert maya_cmds.getAttr(f"{name}.shapeGuideLine")
