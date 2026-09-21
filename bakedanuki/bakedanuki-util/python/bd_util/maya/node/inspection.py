# coding: utf-8
"""選択ノードと既存scalar属性をsceneへ書き込まずに調べる。"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal, TypeAlias, cast

from maya import cmds
from maya.api import OpenMaya as om

from ._attribute_lookup import attribute_path

ScalarAttributeKind: TypeAlias = Literal[
    "bool", "number", "distance", "angle", "enum"
]
ScalarAttributeDisplayFilter: TypeAlias = Literal[
    "all", "visible", "keyable", "channel_box", "hidden"
]
_DISPLAY_FILTERS = ("all", "visible", "keyable", "channel_box", "hidden")

__all__ = [
    "ScalarAttributeKind",
    "ScalarAttributeDisplayFilter",
    "ScalarAttributeInfo",
    "matches_scalar_attribute_display_filter",
    "filter_scalar_attribute_paths",
    "selected_node_names",
    "inspect_scalar_attributes",
]


@dataclass(frozen=True)
class ScalarAttributeInfo:
    """単一値編集に利用できる既存属性の名前・型・表示フラグ。"""

    name: str
    path: str
    nice_name: str
    kind: ScalarAttributeKind
    keyable: bool
    channel_box: bool


def matches_scalar_attribute_display_filter(
    attribute: ScalarAttributeInfo,
    display_filter: ScalarAttributeDisplayFilter,
) -> bool:
    """Keyableを優先する三状態分類で、属性が表示条件に合うか返す。"""
    if not isinstance(attribute, ScalarAttributeInfo):
        raise TypeError("attributeにはScalarAttributeInfoを指定してください")
    if display_filter not in _DISPLAY_FILTERS:
        raise ValueError("未対応の属性表示フィルターです")
    if display_filter == "all":
        return True
    if display_filter == "visible":
        return attribute.keyable or attribute.channel_box
    if display_filter == "keyable":
        return attribute.keyable
    if display_filter == "channel_box":
        return not attribute.keyable and attribute.channel_box
    return not attribute.keyable and not attribute.channel_box


def filter_scalar_attribute_paths(
    attributes: Sequence[ScalarAttributeInfo],
    display_filter: ScalarAttributeDisplayFilter,
) -> tuple[str, ...]:
    """入力順を維持し、表示条件に合うscalar属性の正式pathを返す。"""
    if not isinstance(attributes, Sequence) or isinstance(
        attributes, (str, bytes)
    ):
        raise TypeError(
            "attributesにはScalarAttributeInfoのSequenceを指定してください"
        )
    if display_filter not in _DISPLAY_FILTERS:
        raise ValueError("未対応の属性表示フィルターです")
    return tuple(
        attribute.path
        for attribute in attributes
        if matches_scalar_attribute_display_filter(attribute, display_filter)
    )


def selected_node_names() -> tuple[str, ...]:
    """現在の選択順で重複のないobject名を返し、componentとplugを除く。"""
    selection = om.MGlobal.getActiveSelectionList()
    iterator = om.MItSelectionList(selection)
    names: list[str] = []
    nodes: list[om.MObject] = []

    # DAG instanceは同じnodeとして扱い、最初の選択pathを残す
    while not iterator.isDone():
        item_type = iterator.itemType()
        if item_type == om.MItSelectionList.kDagSelectionItem:
            dag_path, component = iterator.getComponent()
            if not component.isNull():
                iterator.next()
                continue
            node = dag_path.node()
            name = cast(str, dag_path.fullPathName())
        elif item_type == om.MItSelectionList.kDNselectionItem:
            node = iterator.getDependNode()
            name = cast(str, om.MFnDependencyNode(node).name())
        else:
            iterator.next()
            continue
        if not any(node == previous for previous in nodes):
            nodes.append(node)
            names.append(name)
        iterator.next()
    return tuple(names)


def _node_function(node_name: object) -> om.MFnDependencyNode:
    """完全一致する既存node名だけを解決する。"""
    if not isinstance(node_name, str):
        raise TypeError("node_nameにはstrを指定してください")
    if not node_name or any(char in node_name for char in ".*?[]"):
        raise ValueError("node_nameには単一の既存node名を指定してください")
    selection = om.MSelectionList()
    try:
        selection.add(node_name)
        return om.MFnDependencyNode(selection.getDependNode(0))
    except RuntimeError as error:
        raise ValueError(f"nodeを一意に解決できません: {node_name}") from error


def _scalar_kind(plug: om.MPlug) -> ScalarAttributeKind | None:
    """配列配下を除くbool・float/double・距離・角度・enumを分類する。"""
    if plug.isCompound:
        return None
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            return None
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()
    attribute = plug.attribute()
    if attribute.hasFn(om.MFn.kEnumAttribute):
        return "enum"
    if attribute.hasFn(om.MFn.kNumericAttribute):
        numeric_type = om.MFnNumericAttribute(attribute).numericType()
        if numeric_type == om.MFnNumericData.kBoolean:
            return "bool"
        if numeric_type in (
            om.MFnNumericData.kFloat,
            om.MFnNumericData.kDouble,
        ):
            return "number"
    elif attribute.hasFn(om.MFn.kUnitAttribute):
        unit_type = om.MFnUnitAttribute(attribute).unitType()
        if unit_type == om.MFnUnitAttribute.kDistance:
            return "distance"
        if unit_type == om.MFnUnitAttribute.kAngle:
            return "angle"
    return None


def inspect_scalar_attributes(
    node_name: str,
) -> tuple[ScalarAttributeInfo, ...]:
    """既存nodeの属性順で対応scalarを返し、表示フラグによる除外は行わない。"""
    node = _node_function(node_name)
    result: list[ScalarAttributeInfo] = []

    # 親が非表示でも子のkeyable状態は独立しているため全属性を検査する
    for index in range(node.attributeCount()):
        attribute = node.attribute(index)
        plug = node.findPlug(attribute, False)
        kind = _scalar_kind(plug)
        if kind is None:
            continue
        path = attribute_path(plug)
        nice_name = cmds.attributeName(
            f"{node_name}.{path.removeprefix('.')}", nice=True
        )
        result.append(
            ScalarAttributeInfo(
                name=cast(str, om.MFnAttribute(attribute).name),
                path=path,
                nice_name=nice_name,
                kind=kind,
                keyable=bool(plug.isKeyable),
                channel_box=bool(plug.isChannelBox),
            )
        )
    return tuple(result)
