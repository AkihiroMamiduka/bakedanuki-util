"""複数ノードの現在値を保存し、シーンへ復元する。"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

from maya import cmds
from maya.api import OpenMaya as om

from ...py import json_file
from ._animation_clip_capture import plug_for, saved_node_name
from ._animation_clip_restore import absolute, mapped_name
from ._attribute_lookup import attribute_path
from ._saved_node_selector import select_saved_node_names
from .animation_clip import finite_number, literal_name
from .modifier import ModifierManager
from .operator.attr import _keyframe_target
from .operator.attr.keyframe import KeyframeManager
from .operator.node._core import NodeOperator
from .operator.node.dg._anim_layer import (
    leaf_plugs,
    live_node,
    locked_plug,
    node_object,
)

if TYPE_CHECKING:
    from ._versioned_accessors import (  # pyright: ignore[reportMissingModuleSource]
        AnimLayerNode,
    )

ValueKind = Literal[
    "bool", "int", "float", "enum", "angle", "distance", "string"
]
ScalarValue = bool | int | float | str


def _record(value: object, keys: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TypeError("Expected a mapping.")
    data = cast(Mapping[str, object], value)
    if set(data) != set(keys.split()):
        raise ValueError(f"Expected fields: {keys}.")
    return data


def _items(value: object) -> list[object] | tuple[object, ...]:
    if not isinstance(value, (list, tuple)):
        raise TypeError("Expected a list or tuple.")
    return cast(list[object] | tuple[object, ...], value)


def _checked_value(kind: ValueKind, value: object) -> ScalarValue:
    if kind == "bool":
        if type(value) is not bool:
            raise TypeError("Boolean attribute value must be a bool.")
        return value
    if kind in ("int", "enum"):
        if type(value) is not int:
            raise TypeError("Integer attribute value must be an int.")
        return value
    if kind == "string":
        if not isinstance(value, str):
            raise TypeError("String attribute value must be a string.")
        return value
    return finite_number(value, "attribute value")


@dataclass(frozen=True, slots=True)
class AttributeValueData:
    """一つの末端属性の名前、値型、現在値。"""

    attribute: str
    kind: ValueKind
    value: ScalarValue

    @classmethod
    def from_dict(cls, value: object) -> AttributeValueData:
        """保存した属性値の辞書を検証する。"""
        data = _record(value, "attribute kind value")
        kind = data["kind"]
        if kind not in (
            "bool",
            "int",
            "float",
            "enum",
            "angle",
            "distance",
            "string",
        ):
            raise ValueError(f"Unsupported attribute value kind: {kind!r}.")
        return cls(
            literal_name(data["attribute"]),
            kind,
            _checked_value(kind, data["value"]),
        )


@dataclass(frozen=True, slots=True)
class NodeAttributeValues:
    """一つのノードと保存順に並ぶ属性値。"""

    name: str
    attributes: tuple[AttributeValueData, ...]

    @classmethod
    def from_dict(cls, value: object) -> NodeAttributeValues:
        """保存したノード値の辞書を検証する。"""
        data = _record(value, "name attributes")
        result = cls(
            literal_name(data["name"]),
            tuple(
                AttributeValueData.from_dict(item)
                for item in _items(data["attributes"])
            ),
        )
        names = [item.attribute for item in result.attributes]
        if len(names) != len(set(names)):
            raise ValueError("Duplicate attribute in node values.")
        return result


@dataclass(frozen=True, slots=True)
class AttributeRestoreSkip:
    """復元しなかった属性と理由。"""

    node: str
    attribute: str
    reason: str


@dataclass(slots=True)
class AttributeRestoreReport:
    """`do_it_dg()` 後に完了する復元結果。"""

    applied_count: int = 0
    skipped: tuple[AttributeRestoreSkip, ...] = ()
    complete: bool = False


def _kind(plug: om.MPlug) -> ValueKind | None:
    attribute = plug.attribute()
    if attribute.hasFn(om.MFn.kEnumAttribute):
        return "enum"
    if attribute.hasFn(om.MFn.kUnitAttribute):
        unit = om.MFnUnitAttribute(attribute).unitType()
        if unit == om.MFnUnitAttribute.kAngle:
            return "angle"
        if unit == om.MFnUnitAttribute.kDistance:
            return "distance"
        return None
    if attribute.hasFn(om.MFn.kNumericAttribute):
        numeric = om.MFnNumericAttribute(attribute).numericType()
        if numeric == om.MFnNumericData.kBoolean:
            return "bool"
        if numeric in (
            om.MFnNumericData.kByte,
            om.MFnNumericData.kChar,
            om.MFnNumericData.kShort,
            om.MFnNumericData.kInt,
        ):
            return "int"
        if numeric in (om.MFnNumericData.kFloat, om.MFnNumericData.kDouble):
            return "float"
    if (
        attribute.hasFn(om.MFn.kTypedAttribute)
        and om.MFnTypedAttribute(attribute).attrType() == om.MFnData.kString
    ):
        return "string"
    return None


def _read(plug: om.MPlug, kind: ValueKind) -> ScalarValue:
    if kind == "bool":
        return plug.asBool()
    if kind in ("int", "enum"):
        return plug.asInt()
    if kind == "angle":
        return finite_number(plug.asMAngle().asDegrees(), plug.name())
    if kind == "distance":
        return finite_number(plug.asMDistance().asCentimeters(), plug.name())
    if kind == "string":
        return plug.asString()
    return finite_number(plug.asDouble(), plug.name())


def _queue_value(
    modifier: om.MDGModifier, plug: om.MPlug, item: AttributeValueData
) -> None:
    kind, value = item.kind, item.value
    if kind == "bool":
        modifier.newPlugValueBool(plug, cast(bool, value))
    elif kind == "enum":
        modifier.newPlugValueShort(plug, cast(int, value))
    elif kind == "int":
        numeric = om.MFnNumericAttribute(plug.attribute()).numericType()
        if numeric in (om.MFnNumericData.kByte, om.MFnNumericData.kChar):
            modifier.newPlugValueChar(plug, cast(int, value))
        elif numeric == om.MFnNumericData.kShort:
            modifier.newPlugValueShort(plug, cast(int, value))
        else:
            modifier.newPlugValueInt(plug, cast(int, value))
    elif kind == "angle":
        modifier.newPlugValueMAngle(
            plug, om.MAngle(cast(float, value), om.MAngle.kDegrees)
        )
    elif kind == "distance":
        modifier.newPlugValueMDistance(
            plug, om.MDistance(cast(float, value), om.MDistance.kCentimeters)
        )
    elif kind == "string":
        modifier.newPlugValueString(plug, cast(str, value))
    else:
        if (
            om.MFnNumericAttribute(plug.attribute()).numericType()
            == om.MFnNumericData.kFloat
        ):
            modifier.newPlugValueFloat(plug, cast(float, value))
        else:
            modifier.newPlugValueDouble(plug, cast(float, value))


def _has_time_curve(plug: om.MPlug) -> bool:
    """レイヤーと通常チャンネルの既存の時間カーブだけを検出する。"""
    if plug.sourceWithConversion().isNull:
        return False
    try:
        if _keyframe_target.channel_curve(plug) is not None:
            return True
    except RuntimeError:
        pass
    iterator = om.MItDependencyNodes(om.MFn.kAnimLayer)
    while not iterator.isDone():
        layer = om.MFnDependencyNode(iterator.thisNode()).name()
        if _keyframe_target.layer_member(layer, plug):
            target = _keyframe_target.LayerTarget(plug, layer)
            if _keyframe_target.layer_curve(target) is not None:
                return True
        iterator.next()
    return False


@dataclass(frozen=True, slots=True, kw_only=True)
class AttrSnapshot:
    """シーンから独立した複数ノードの現在値。"""

    nodes: tuple[NodeAttributeValues, ...]
    schema_version: Literal[1] = 1

    def __post_init__(self) -> None:
        if type(self.schema_version) is not int or self.schema_version != 1:
            raise ValueError("Unsupported AttrSnapshot schema_version.")
        normalized = tuple(
            NodeAttributeValues.from_dict(asdict(node)) for node in self.nodes
        )
        if len({node.name for node in normalized}) != len(normalized):
            raise ValueError("Snapshot node names must be unique.")
        object.__setattr__(self, "nodes", normalized)

    def to_dict(self) -> dict[str, object]:
        """JSON 化できる辞書に変換する。"""
        return asdict(self)

    def to_json(self, *, indent: int | None = 2) -> str:
        """Unicode を維持した JSON 文字列を返す。"""
        return json.dumps(
            self.to_dict(), ensure_ascii=False, allow_nan=False, indent=indent
        )

    @classmethod
    def from_dict(cls, value: object) -> AttrSnapshot:
        """schema 1 の辞書から独立したスナップショットを復元する。"""
        data = _record(value, "nodes schema_version")
        if (
            type(data["schema_version"]) is not int
            or data["schema_version"] != 1
        ):
            raise ValueError("Unsupported AttrSnapshot schema_version.")
        return cls(
            nodes=tuple(
                NodeAttributeValues.from_dict(item)
                for item in _items(data["nodes"])
            )
        )

    @classmethod
    def from_json(cls, value: str) -> AttrSnapshot:
        """JSON 文字列を検証して読み込む。"""
        return cls.from_dict(json.loads(value))

    def save(
        self,
        path: str | PathLike[str],
        *,
        indent: int | None = 2,
        overwrite: bool = True,
        create_parents: bool = True,
    ) -> Path:
        """JSON ファイルへ即時保存する。ファイル操作は Undo 対象外。"""
        return json_file.write(
            path,
            self.from_dict(self.to_dict()).to_dict(),
            indent=indent,
            overwrite=overwrite,
            create_parents=create_parents,
        )

    @classmethod
    def load(cls, path: str | PathLike[str]) -> AttrSnapshot:
        """JSON ファイルを検証して独立した値を返す。"""
        return cls.from_dict(json_file.read(path))

    def extract(
        self,
        *,
        nodes: Iterable[NodeOperator | om.MObject | str],
    ) -> AttrSnapshot:
        """指定した保存ノードの全属性を持つ新しいスナップショットを返す。

        元データ、シーン、予約中の操作は変更しない。

        Args:
            nodes: 保存名、既存ノード、または明示名付きの作成予定ノード。
                短い名前の一致が複数ある場合は拒否する。

        Returns:
            指定順にノードを並べた独立した `AttrSnapshot`。

        Raises:
            TypeError: `nodes` がノード選択子の iterable でない場合。
            ValueError: 対象が空、重複、見つからない、曖昧、または属性値がない場合。
        """
        data = self.from_dict(self.to_dict())
        selected_names = select_saved_node_names(
            (node.name for node in data.nodes), nodes=nodes, kind="snapshot"
        )
        by_name = {node.name: node for node in data.nodes}
        selected = tuple(by_name[name] for name in selected_names)
        if not any(node.attributes for node in selected):
            raise ValueError(
                "The selected snapshot nodes contain no attributes."
            )
        return AttrSnapshot(nodes=selected, schema_version=data.schema_version)

    @classmethod
    def capture(
        cls,
        nodes: Iterable[NodeOperator | om.MObject | str],
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = True,
        include_hidden: bool = False,
    ) -> AttrSnapshot:
        """既存ノードの評価済み現在値を即時取得する。

        `include_hidden` は Channel Box に出ない属性を含める指定で、
        `MFnAttribute.hidden` とは独立する。明示した `attributes` は表示条件を無視する。
        配列は既存要素のみ、複合属性は末端を取得する。

        Args:
            nodes: 保存するノードの iterable。
            attributes: 各ノードに共通の属性名。`None` では表示条件で収集する。
            include_channel_box: 自動収集で channel box 専用属性も含めるか。
            include_hidden: 自動収集で channel box 非表示属性も含めるか。

        Returns:
            シーンから独立した値。
        """
        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        if (
            type(include_channel_box) is not bool
            or type(include_hidden) is not bool
        ):
            raise TypeError("Capture display flags must be bool.")
        if isinstance(attributes, str):
            raise TypeError("attributes must be an iterable of names.")
        selected = (
            None
            if attributes is None
            else tuple(literal_name(name) for name in attributes)
        )
        result: list[NodeAttributeValues] = []
        handles: set[om.MObjectHandle] = set()
        for value in nodes:
            node = node_object(value)
            handle = om.MObjectHandle(node)
            if handle in handles:
                raise ValueError("Duplicate source node.")
            handles.add(handle)
            fn = live_node(node)
            candidates = (
                [plug_for(node, name) for name in selected]
                if selected is not None
                else [
                    fn.findPlug(fn.attribute(i), False)
                    for i in range(fn.attributeCount())
                    if om.MFnAttribute(fn.attribute(i)).parent.isNull()
                ]
            )
            found: dict[str, AttributeValueData] = {}
            for candidate in candidates:
                for plug in leaf_plugs(candidate):
                    if selected is None and not (
                        plug.isKeyable
                        or include_channel_box
                        and plug.isChannelBox
                        or include_hidden
                        and not (plug.isKeyable or plug.isChannelBox)
                    ):
                        continue
                    kind = _kind(plug)
                    if (
                        kind is None
                        or not om.MFnAttribute(plug.attribute()).readable
                    ):
                        if selected is not None:
                            raise TypeError(
                                f"Unsupported snapshot attribute: {plug.name()}."
                            )
                        continue
                    path = attribute_path(plug)
                    found[path] = AttributeValueData(
                        path, kind, _read(plug, kind)
                    )
            result.append(
                NodeAttributeValues(
                    saved_node_name(node), tuple(found.values())
                )
            )
        if not result or not any(node.attributes for node in result):
            raise ValueError("No supported attribute values were selected.")
        return cls(nodes=tuple(result))

    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        anim_layer: AnimLayerNode | om.MObject | str | None = None,
        frame: float | None = None,
        strict: bool = False,
    ) -> AttributeRestoreReport:
        """保存値の復元を予約し、`do_it_dg()` 後に完成する結果を返す。

        入力接続のない属性は直接設定する。既存の時間カーブがある属性は
        `frame` で `anim_layer` にキーを設定する。指定なしではルートを使う。
        その他の入力接続、編集不可、型不一致、レイヤー未所属はスキップする。
        キー設定先のカーブがロックまたは参照されている場合も、その属性をスキップする。
        `strict=True` では全件の適用可否を変更前に検査してエラーにする。

        Args:
            modifier_manager: 復元と Undo を管理する先。
            targets: 保存順に対応する復元先。`namespace` と併用不可。
            namespace: 保存名の名前空間を置換。空文字では名前空間を除く。
            anim_layer: アニメーション属性のキー設定先。`None` はルート。
            frame: 予約時の Maya UI 時間単位によるキー時刻。
                `None` は予約時の UI 時刻。
            strict: スキップ対象があれば一括でエラーにするか。

        Returns:
            `do_it_dg()` 後に件数とスキップ理由が入る結果。
        """
        if not isinstance(cast(object, modifier_manager), ModifierManager):
            raise TypeError("modifier_manager must be a ModifierManager.")
        if type(strict) is not bool:
            raise TypeError("strict must be a bool.")
        if namespace is not None:
            if (
                targets is not None
                or not isinstance(cast(object, namespace), str)
                or any(c in namespace for c in "|.*?[]")
            ):
                raise ValueError(
                    "namespace must be literal and cannot accompany targets."
                )
            namespace = namespace.strip(":")
        if isinstance(targets, (str, NodeOperator, om.MObject)):
            raise TypeError("targets must be an iterable of nodes.")
        if anim_layer is not None and not isinstance(
            cast(object, anim_layer), (str, om.MObject, NodeOperator)
        ):
            raise TypeError("anim_layer must be a layer name or node.")
        time_unit = om.MTime.uiUnit()
        target_frame = finite_number(
            cmds.currentTime(query=True) if frame is None else frame, "frame"
        )
        target_time = om.MTime(target_frame, time_unit)
        data = self.from_dict(self.to_dict())
        destination = (
            tuple(
                absolute(mapped_name(node.name, namespace))
                for node in data.nodes
            )
            if targets is None
            else tuple(
                (
                    literal_name(item)
                    if isinstance(item, str)
                    else node_object(item)
                )
                for item in targets
            )
        )
        if len(destination) != len(data.nodes):
            raise ValueError(
                "targets must have the same length as the saved node list."
            )
        report = AttributeRestoreReport()

        def prepare(manager: ModifierManager) -> None:
            pending: list[tuple[om.MPlug, AttributeValueData, bool]] = []
            skipped: list[AttributeRestoreSkip] = []
            layer_name: str | None = None
            if anim_layer is not None:
                try:
                    layer_node = node_object(anim_layer)
                    if not layer_node.hasFn(om.MFn.kAnimLayer):
                        raise TypeError(
                            "anim_layer must be an animation layer."
                        )
                    layer_name = live_node(layer_node).name()
                except (RuntimeError, ValueError, TypeError):
                    if strict:
                        raise
                    layer_name = ""
            for node_data, target in zip(data.nodes, destination, strict=True):
                try:
                    node = node_object(target)
                except (RuntimeError, ValueError):
                    for item in node_data.attributes:
                        skipped.append(
                            AttributeRestoreSkip(
                                str(target), item.attribute, "missing node"
                            )
                        )
                    continue
                fn = live_node(node)
                for item in node_data.attributes:
                    reason: str | None = None
                    try:
                        plug = plug_for(node, item.attribute)
                    except (RuntimeError, ValueError):
                        reason = "missing attribute"
                    else:
                        if _kind(plug) != item.kind:
                            reason = "type mismatch"
                        elif (
                            fn.isLocked
                            or fn.isFromReferencedFile
                            or locked_plug(plug)
                            or not om.MFnAttribute(plug.attribute()).writable
                        ):
                            reason = "locked, referenced or nonwritable"
                        elif not plug.sourceWithConversion().isNull:
                            if item.kind == "string":
                                reason = "non-animation input connection"
                            else:
                                try:
                                    animated = _has_time_curve(plug)
                                except RuntimeError:
                                    animated = False
                                if not animated:
                                    reason = "non-animation input connection"
                                elif layer_name == "":
                                    reason = "missing animation layer"
                                elif (
                                    layer_name is not None
                                    and layer_name
                                    != cmds.animLayer(query=True, root=True)
                                    and not _keyframe_target.layer_member(
                                        layer_name, plug
                                    )
                                ):
                                    reason = "attribute is not a member of animation layer"
                                else:
                                    try:
                                        target_layer = (
                                            _keyframe_target.LayerTarget(
                                                plug, layer_name
                                            )
                                            if layer_name is not None
                                            else _keyframe_target.base_layer(
                                                plug
                                            )
                                        )
                                        if target_layer is not None:
                                            _keyframe_target.layer_name(
                                                target_layer, write=True
                                            )
                                    except RuntimeError:
                                        reason = (
                                            "animation layer is not editable"
                                        )
                                    else:
                                        curve = (
                                            _keyframe_target.layer_curve(
                                                target_layer
                                            )
                                            if target_layer is not None
                                            else _keyframe_target.channel_curve(
                                                plug
                                            )
                                        )
                                        if curve is not None:
                                            if curve.isFromReferencedFile:
                                                reason = "referenced animation curve"
                                            else:
                                                try:
                                                    _keyframe_target.check_key_editable_curve(
                                                        curve
                                                    )
                                                except RuntimeError:
                                                    reason = "locked animation curve"
                        if reason is None:
                            pending.append(
                                (
                                    plug,
                                    item,
                                    not plug.sourceWithConversion().isNull,
                                )
                            )
                    if reason is not None:
                        skipped.append(
                            AttributeRestoreSkip(
                                fn.name(), item.attribute, reason
                            )
                        )
            if strict and skipped:
                first = skipped[0]
                raise RuntimeError(
                    f"Cannot restore {first.node}.{first.attribute}: {first.reason}."
                )
            for plug, item, keyed in pending:
                if keyed:
                    keyframes = KeyframeManager(plug, modifier_manager=manager)
                    if layer_name is not None:
                        keyframes = keyframes.anim_layer(layer_name)
                    keyframes.set_key(
                        cast(float, item.value),
                        target_time.asUnits(om.MTime.uiUnit()),
                    )
                else:
                    _queue_value(manager.dg_mod, plug, item)

            manager.queue_dg_modifier(
                lambda modifier: _complete(
                    report, len(pending), tuple(skipped)
                )
            )

        modifier_manager.queue_dg_batch(prepare)
        return report


def _complete(
    report: AttributeRestoreReport,
    count: int,
    skipped: tuple[AttributeRestoreSkip, ...],
) -> None:
    report.applied_count = count
    report.skipped = skipped
    report.complete = True
