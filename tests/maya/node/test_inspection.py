# coding: utf-8
"""既存nodeの調査が表示用情報だけを返すことを検証する。"""

from dataclasses import FrozenInstanceError
from typing import cast

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.node.inspection import (
    ScalarAttributeDisplayFilter,
    filter_scalar_attribute_paths,
    inspect_scalar_attributes,
    matches_scalar_attribute_display_filter,
    selected_node_names,
)
from bd_util.maya.ui import resolve_bool_plug, resolve_float_plug


def test_inspection_reports_leaf_flags_types_names_and_limits_scope(
    new_scene,
) -> None:
    """非表示親の子も列挙し、対応型だけに範囲を限定する。"""
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="enabled", attributeType="bool")
    cmds.addAttr(
        node, longName="amount", niceName="Amount Label", attributeType="float"
    )
    cmds.addAttr(node, longName="integer", attributeType="long", keyable=True)
    cmds.addAttr(
        node, longName="timeValue", attributeType="time", keyable=True
    )
    cmds.addAttr(node, longName="values", attributeType="double", multi=True)
    cmds.addAttr(
        node,
        longName="records",
        attributeType="compound",
        numberOfChildren=1,
        multi=True,
    )
    cmds.addAttr(
        node, longName="recordValue", attributeType="bool", parent="records"
    )
    cmds.setAttr(node + ".amount", channelBox=True)
    infos = inspect_scalar_attributes(node)
    by_name = {info.name: info for info in infos}
    assert by_name["translateX"].kind == "distance"
    assert by_name["rotateX"].kind == "angle"
    assert by_name["scaleX"].kind == "number"
    assert by_name["visibility"].kind == "bool"
    assert by_name["rotateOrder"].kind == "enum"
    assert by_name["translateX"].keyable
    assert not by_name["translateX"].channel_box
    assert by_name["translateX"].path == "translate.translateX"
    assert by_name["amount"].nice_name == "Amount Label"
    assert by_name["amount"].channel_box
    assert not by_name["enabled"].keyable
    assert not by_name["enabled"].channel_box
    assert (
        not {"translate", "integer", "timeValue", "values", "recordValue"}
        & by_name.keys()
    )
    with pytest.raises(FrozenInstanceError):
        by_name["amount"].name = "changed"


def test_enum_inspection_reports_scalars_and_omits_arrays(new_scene) -> None:
    """enumの表示フラグとcompound子を返し、配列配下は列挙しない。"""
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="mode", attributeType="enum", enumName="A:B")
    cmds.setAttr(node + ".mode", channelBox=True)
    for name, multi in (("group", False), ("records", True)):
        cmds.addAttr(
            node,
            longName=name,
            attributeType="compound",
            numberOfChildren=1,
            multi=multi,
        )
        cmds.addAttr(
            node,
            longName=name + "Mode",
            parent=name,
            attributeType="enum",
            enumName="A:B",
            keyable=True,
        )
    cmds.addAttr(
        node,
        longName="modes",
        attributeType="enum",
        enumName="A:B",
        multi=True,
    )
    infos = {info.path: info for info in inspect_scalar_attributes(node)}
    assert infos["mode"].kind == "enum"
    assert infos["mode"].channel_box and not infos["mode"].keyable
    assert infos["group.groupMode"].kind == "enum"
    assert infos["group.groupMode"].keyable
    assert {"modes", "records.recordsMode"}.isdisjoint(infos)


def test_display_filter_classifies_scalar_attribute_paths(new_scene) -> None:
    """Keyableを優先し、既存の五つの表示条件で正式pathを抽出する。"""
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="keyed", attributeType="double", keyable=True)
    cmds.addAttr(node, longName="shown", attributeType="double")
    cmds.addAttr(node, longName="hidden", attributeType="double")
    cmds.setAttr(node + ".shown", channelBox=True)
    attributes = tuple(
        attribute
        for attribute in inspect_scalar_attributes(node)
        if attribute.path in {"keyed", "shown", "hidden"}
    )

    assert filter_scalar_attribute_paths(attributes, "all") == (
        "keyed",
        "shown",
        "hidden",
    )
    assert filter_scalar_attribute_paths(attributes, "visible") == (
        "keyed",
        "shown",
    )
    assert filter_scalar_attribute_paths(attributes, "keyable") == ("keyed",)
    assert filter_scalar_attribute_paths(attributes, "channel_box") == (
        "shown",
    )
    assert filter_scalar_attribute_paths(attributes, "hidden") == ("hidden",)
    assert matches_scalar_attribute_display_filter(attributes[0], "keyable")
    with pytest.raises(ValueError, match="未対応"):
        filter_scalar_attribute_paths(
            attributes, cast(ScalarAttributeDisplayFilter, "invalid")
        )
    with pytest.raises(TypeError, match="Sequence"):
        filter_scalar_attribute_paths("keyed", "all")


def test_inspection_and_selection_do_not_change_scene_or_undo(
    new_scene,
) -> None:
    """調査によってnode・選択・変更状態・Undo履歴を変更しない。"""
    node = cmds.createNode("transform")
    cmds.select(node)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    cmds.file(modified=False)
    before_nodes = cmds.ls(long=True)
    before_selection = cmds.ls(selection=True, long=True)
    inspect_scalar_attributes(node)
    assert selected_node_names() == ("|" + node,)
    assert cmds.ls(long=True) == before_nodes
    assert cmds.ls(selection=True, long=True) == before_selection
    assert not cmds.file(query=True, modified=True)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_selection_preserves_object_order_and_omits_components_and_plugs(
    new_scene,
) -> None:
    """選択objectだけを入力順に返し、tracking設定を維持する。"""
    first = cmds.createNode("transform", name="zSelected")
    last = cmds.createNode("multiplyDivide", name="aSelected")
    mesh = cmds.polyCube()[0]
    tracking = cmds.selectPref(query=True, trackSelectionOrder=True)
    selection = om.MSelectionList()
    selection.add(first)
    selection.add(mesh + ".vtx[0]")
    selection.add(first + ".visibility")
    selection.add(last)
    om.MGlobal.setActiveSelectionList(selection)
    assert selected_node_names() == ("|" + first, last)
    assert cmds.selectPref(query=True, trackSelectionOrder=True) == tracking


def test_selection_deduplicates_dag_instances_by_node(new_scene) -> None:
    """同じDAG nodeの別instanceは最初に選択されたpathへまとめる。"""
    original = cmds.polyCube()[0]
    instance = cmds.instance(original)[0]
    original_shape = cmds.listRelatives(original, shapes=True, fullPath=True)[
        0
    ]
    instance_shape = cmds.listRelatives(instance, shapes=True, fullPath=True)[
        0
    ]
    cmds.select([original_shape, instance_shape], replace=True)
    assert selected_node_names() == (original_shape,)


def test_resolvers_accept_long_short_and_full_compound_paths(
    new_scene,
) -> None:
    """親pathを使った解決でも同じscalar plugを返す。"""
    node = cmds.createNode("transform")
    cmds.addAttr(
        node,
        longName="options",
        shortName="opts",
        attributeType="compound",
        numberOfChildren=1,
    )
    cmds.addAttr(
        node,
        longName="enabled",
        shortName="ena",
        attributeType="bool",
        parent="options",
    )
    for name in (
        "enabled",
        "ena",
        "options.enabled",
        "opts.ena",
        ".options.ena",
    ):
        assert (
            resolve_bool_plug(node, name).plug
            == resolve_bool_plug(node, "enabled").plug
        )
    for name in (
        "translateX",
        "tx",
        "translate.translateX",
        "t.tx",
        ".t.translateX",
    ):
        assert (
            resolve_float_plug(node, name).plug
            == resolve_float_plug(node, "tx").plug
        )
    info = next(
        item
        for item in inspect_scalar_attributes(node)
        if item.name == "enabled"
    )
    assert info.path == "options.enabled"
    assert (
        resolve_bool_plug(node, info.path).plug
        == resolve_bool_plug(node, "enabled").plug
    )


@pytest.mark.parametrize(
    "name,error",
    [
        ("axisAlias", AttributeError),
        ("translate.axisAlias", AttributeError),
        ("rotationAlias.translateX", AttributeError),
        ("rotate.translateX", AttributeError),
        ("missing.translateX", AttributeError),
        (".translateX", AttributeError),
        ("translate.translate.translateX", AttributeError),
        ("translateX.child", AttributeError),
        ("translate..translateX", ValueError),
        ("translateX.", ValueError),
        ("translateX[0]", ValueError),
        ("translate*", ValueError),
        ("translate?", ValueError),
    ],
)
def test_resolvers_reject_aliases_and_incorrect_parent_paths(
    new_scene, name: str, error: type[Exception]
) -> None:
    """一意なleafを直接取得できても、aliasや不完全な親pathは受理しない。"""
    node = cmds.createNode("transform")
    cmds.aliasAttr("axisAlias", node + ".translateX")
    cmds.aliasAttr("rotationAlias", node + ".translate")
    with pytest.raises(error):
        resolve_float_plug(node, name)


def test_non_unique_leaf_requires_canonical_path(new_scene) -> None:
    """同じleaf名が異なる親と最上位にある場合も別々のplugを解決する。"""
    node = cmds.createNode("hierarchyTestNode4")
    envelopes = [
        info
        for info in inspect_scalar_attributes(node)
        if info.name == "envelope"
    ]
    assert [info.path for info in envelopes] == [
        ".envelope",
        "kitA.envelope",
        "kitB.envelope",
    ]
    with pytest.raises(ValueError, match="曖昧"):
        resolve_float_plug(node, "envelope")
    plugs = [resolve_float_plug(node, info.path).plug for info in envelopes]
    assert len({plug.name() for plug in plugs}) == 3
    assert not plugs[0].isChild
    assert om.MFnAttribute(plugs[1].parent().attribute()).name == "kitA"
    assert om.MFnAttribute(plugs[2].parent().attribute()).name == "kitB"


@pytest.mark.parametrize("node_name", ["", "missing", "*", "node.attr"])
def test_inspection_rejects_non_node_inputs(new_scene, node_name: str) -> None:
    """存在しないnodeやpatternを黙って読み替えない。"""
    with pytest.raises(ValueError):
        inspect_scalar_attributes(node_name)
