# coding: utf-8
"""選択ノードと既存scalar属性をsceneへ書き込まずに調べる。"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from typing import Literal, TypeAlias, cast

from maya import cmds
from maya.api import OpenMaya as om

from .._identity import ObjectIdentityIndex, PlugIdentitySet
from ._attribute_lookup import attribute_path, find_attribute_plug

ScalarAttributeKind: TypeAlias = Literal[
    "bool",
    "byte",
    "short",
    "long",
    "number",
    "distance",
    "angle",
    "enum",
    "string",
]
ScalarAttributeDisplayFilter: TypeAlias = Literal[
    "all", "visible", "keyable", "channel_box", "hidden"
]
_DISPLAY_FILTERS = ("all", "visible", "keyable", "channel_box", "hidden")

__all__ = [
    "ScalarAttributeKind",
    "ScalarAttributeDisplayFilter",
    "ScalarAttributeInfo",
    "ScalarAttributeTypeInfo",
    "matches_scalar_attribute_display_filter",
    "filter_scalar_attribute_paths",
    "selected_node_names",
    "node_display_name",
    "inspect_scalar_attributes",
    "inspect_scalar_attributes_by_type",
    "inspect_scalar_attribute_types",
]


@dataclass(frozen=True)
class ScalarAttributeInfo:
    """対象の scalar 型属性の名前・型・表示フラグ。

    Attributes:
        name: Maya の属性名。
        path: 親属性を含む正式な属性パス。
        nice_name: UI に表示する属性名。
        kind: 編集できる scalar 値の種類。
        keyable: キー設定できるか。
        channel_box: Channel Box に表示するか。
    """

    name: str
    path: str
    nice_name: str
    kind: ScalarAttributeKind
    keyable: bool
    channel_box: bool


@dataclass(frozen=True)
class ScalarAttributeTypeInfo:
    """操作対象の照合に使う正式な属性パスとscalar型。"""

    path: str
    kind: ScalarAttributeKind


def matches_scalar_attribute_display_filter(
    attribute: ScalarAttributeInfo,
    display_filter: ScalarAttributeDisplayFilter,
) -> bool:
    """属性が指定した表示条件に合うか判定する。

    Args:
        attribute: 判定する属性情報。
        display_filter: ``all``、``visible``、``keyable``、
            ``channel_box``、``hidden`` のいずれか。

    Returns:
        条件に合う場合は True。keyable を Channel Box より優先する。
    """
    if not isinstance(cast(object, attribute), ScalarAttributeInfo):
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
    """入力順を維持し、表示条件に合う属性パスを返す。

    Args:
        attributes: 対象の scalar 属性情報。
        display_filter: 適用する表示条件。

    Returns:
        条件に合う属性の正式パス。
    """
    if not isinstance(cast(object, attributes), Sequence) or isinstance(
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


def selected_node_names(*, limit: int | None = None) -> tuple[str, ...]:
    """選択順で重複のないノード名を返す。コンポーネントとプラグは除く。

    `limit`を指定した場合は、その数のノードを見つけた時点で走査を終える。

    Args:
        limit: 取得するノードの上限。`None`なら選択全体を調べる。

    Raises:
        ValueError: `limit`が1未満の場合。
    """
    if limit is not None and limit < 1:
        raise ValueError("limitには1以上を指定してください")
    selection = om.MGlobal.getActiveSelectionList()
    iterator = om.MItSelectionList(selection)
    names: list[str] = []
    nodes = ObjectIdentityIndex()

    # DAG インスタンスは同じノードとして扱い、最初の選択パスを残す。
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
        if nodes.index(node) == len(names):
            names.append(name)
            if limit is not None and len(names) == limit:
                break
        iterator.next()
    return tuple(names)


def _node_selection(node_name: object) -> om.MSelectionList:
    """`node_name` に完全一致する既存ノードの選択リストを作る。"""
    if not isinstance(node_name, str):
        raise TypeError("node_nameにはstrを指定してください")
    if not node_name or any(char in node_name for char in ".*?[]"):
        raise ValueError("node_nameには単一の既存node名を指定してください")
    selection = om.MSelectionList()
    try:
        selection.add(node_name)
        if selection.length() != 1:
            raise ValueError(f"nodeを一意に解決できません: {node_name}")
    except RuntimeError as error:
        raise ValueError(f"nodeを一意に解決できません: {node_name}") from error
    return selection


def node_display_name(node_name: str) -> str:
    """一意なDAGパスは短名で、曖昧なパスはフルパスで表示する。

    Args:
        node_name: 一意に解決できる既存ノード名。DAGインスタンスは表示したいパスを指定する。

    Returns:
        DAGの名前とパスが一意ならnamespace付き短名、同名やinstanceならフルパス。
        DGノードはノード名。

    Raises:
        TypeError: `node_name`が文字列でない場合。
        ValueError: `node_name`が単一の既存ノードを示さない場合。
    """
    selection = _node_selection(node_name)
    node_object = selection.getDependNode(0)
    if not node_object.hasFn(om.MFn.kDagNode):
        return cast(str, om.MFnDependencyNode(node_object).name())
    dag_path = selection.getDagPath(0)
    dag_node = om.MFnDagNode(dag_path)
    if dag_node.hasUniqueName() and not dag_path.isInstanced():
        return cast(str, dag_node.name())
    return cast(str, dag_path.fullPathName())


def _node_function(node_name: object) -> om.MFnDependencyNode:
    """`node_name` に完全一致する既存ノードだけを解決する。"""
    return om.MFnDependencyNode(_node_selection(node_name).getDependNode(0))


def _scalar_kind(plug: om.MPlug) -> ScalarAttributeKind | None:
    """配列配下を除くbool・数値・enum・typed stringを分類する。"""
    if plug.isCompound:
        return None
    ancestor = plug
    while True:
        if ancestor.isArray or ancestor.isElement:
            return None
        if not ancestor.isChild:
            break
        ancestor = ancestor.parent()
    return _scalar_attribute_kind(plug.attribute())


def _scalar_attribute_kind(
    attribute: om.MObject,
) -> ScalarAttributeKind | None:
    """属性オブジェクトから、対応するscalar値種別を分類する。"""
    if attribute.hasFn(om.MFn.kEnumAttribute):
        return "enum"
    if attribute.hasFn(om.MFn.kNumericAttribute):
        numeric_type = om.MFnNumericAttribute(attribute).numericType()
        if numeric_type == om.MFnNumericData.kBoolean:
            return "bool"
        if numeric_type == om.MFnNumericData.kByte:
            return "byte"
        if numeric_type == om.MFnNumericData.kShort:
            return "short"
        if numeric_type == om.MFnNumericData.kLong:
            return "long"
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
    elif attribute.hasFn(om.MFn.kTypedAttribute):
        if om.MFnTypedAttribute(attribute).attrType() == om.MFnData.kString:
            return "string"
    return None


def _require_attribute_paths(value: object) -> tuple[str, ...]:
    """単一文字列を除いた、属性pathの列を検証する。"""
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError("pathsには文字列のSequenceを指定してください")
    result: list[str] = []
    for path in cast(Sequence[object], value):
        if not isinstance(path, str):
            raise TypeError("pathsには文字列のSequenceを指定してください")
        result.append(path)
    return tuple(result)


def inspect_scalar_attributes_by_type(
    node_type: str,
) -> tuple[ScalarAttributeInfo, ...]:
    """ノードを作らず、型の標準scalar属性と既定の表示フラグを返す。

    Args:
        node_type: Mayaに登録済みのノード型名。抽象型も指定できる。

    Returns:
        型の属性順で並ぶ正式path・表示名・値種別・既定表示フラグ。
        個別ノードの追加属性や表示フラグの変更は含まない。

    Raises:
        TypeError: `node_type`が文字列でない場合。
        ValueError: `node_type`が空、または未登録の場合。
    """
    if not isinstance(cast(object, node_type), str):
        raise TypeError("node_typeにはstrを指定してください")
    if not node_type:
        raise ValueError("登録済みのノード型名を指定してください")
    try:
        node_class = om.MNodeClass(node_type)
        attribute_count = node_class.attributeCount
    except RuntimeError as error:
        raise ValueError(f"未登録のノード型です: {node_type}") from error

    # 実plugを作らずに親階層を調べ、配列配下と非対応型を除外する
    result: list[ScalarAttributeInfo] = []
    for index in range(attribute_count):
        attribute = node_class.attribute(index)
        kind = _scalar_attribute_kind(attribute)
        if kind is None:
            continue
        fn_attribute = om.MFnAttribute(attribute)
        names: list[str] = []
        ancestor = attribute
        while not ancestor.isNull():
            fn_ancestor = om.MFnAttribute(ancestor)
            if fn_ancestor.array:
                break
            names.append(cast(str, fn_ancestor.name))
            ancestor = fn_ancestor.parent
        else:
            name = cast(str, fn_attribute.name)
            path = ".".join(reversed(names))
            if len(names) == 1 and not fn_attribute.enforcingUniqueName:
                path = "." + path
            nice_name = cast(
                str, cmds.attributeQuery(name, type=node_type, niceName=True)
            )
            result.append(
                ScalarAttributeInfo(
                    name=name,
                    path=path,
                    nice_name=nice_name,
                    kind=kind,
                    keyable=bool(fn_attribute.keyable),
                    channel_box=bool(fn_attribute.channelBox),
                )
            )
    return tuple(result)


def _scalar_plugs(
    node_name: str, paths: Sequence[str] | None
) -> Iterator[tuple[om.MPlug, ScalarAttributeKind]]:
    """表示情報を読まず、正式pathの解決と対応型の分類を共有する。"""
    if paths is not None:
        paths = _require_attribute_paths(paths)
    node = _node_function(node_name)
    if paths is None:
        plugs = [
            node.findPlug(node.attribute(index), False)
            for index in range(node.attributeCount())
        ]
    else:
        plugs: list[om.MPlug] = []
        seen = PlugIdentitySet()
        for path in paths:
            try:
                plug = find_attribute_plug(node, path)
            except AttributeError:
                continue
            if seen.add(plug):
                plugs.append(plug)

    # 親が非表示でも子のkeyable状態は独立しているため、leaf単位で分類する
    for plug in plugs:
        kind = _scalar_kind(plug)
        if kind is not None:
            yield plug, kind


def inspect_scalar_attribute_types(
    node_name: str,
    *,
    paths: Sequence[str] | None = None,
) -> tuple[ScalarAttributeTypeInfo, ...]:
    """表示名・表示フラグを読まず、対応scalarの正式パスと型を返す。

    `paths`の解決・順序・重複排除と例外は`inspect_scalar_attributes`と同じ。
    値、enum定義、書込み可否の検証は行わず、操作側のBindingへ委譲する。

    Args:
        node_name: 一意に解決できる既存ノード名。
        paths: 属性名または相対path。`None`なら全属性を属性順で調べる。

    Returns:
        存在しない属性・非対応型を除いた、正式パスと型の情報。

    Raises:
        TypeError: `paths`が文字列のSequenceでない場合。
        ValueError: nodeまたは属性が曖昧か、不正なpathの場合。
    """
    return tuple(
        ScalarAttributeTypeInfo(attribute_path(plug), kind)
        for plug, kind in _scalar_plugs(node_name, paths)
    )


def inspect_scalar_attributes(
    node_name: str,
    *,
    paths: Sequence[str] | None = None,
) -> tuple[ScalarAttributeInfo, ...]:
    """既存ノードの対応する scalar 型属性を属性順に返す。

    Args:
        node_name: 一意に解決できる既存ノード名。
        paths: 調べる属性名または相対path。指定時は入力順で重複を除き、
            存在しない属性・非対応型を除外する。別名は受け付けない。
            `None`なら全属性を属性順で調べる。

    Returns:
        表示フラグでは絞り込まない属性情報のタプル。

    Raises:
        TypeError: `paths`が文字列のSequenceでない場合。
        ValueError: nodeまたは属性を一意に解決できないか、不正なpathの場合。
    """
    result: list[ScalarAttributeInfo] = []
    for plug, kind in _scalar_plugs(node_name, paths):
        attribute = plug.attribute()
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
