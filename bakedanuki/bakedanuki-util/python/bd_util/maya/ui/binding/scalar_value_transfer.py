# coding: utf-8
"""Maya scalar値を型付きsnapshotとして搬送し、同じ属性pathへ適用する。"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeAlias, cast

from ....ui import EnumDefinition, EnumItem, JsonClipboard
from ...node.inspection import (
    ScalarAttributeInfo,
    ScalarAttributeKind,
    inspect_scalar_attributes,
)
from ._enum_plug_value import EnumPlugValue
from ._float_plug_value import FloatPlugValue
from .bool_plug_resolver import resolve_bool_plug
from .enum_definition import read_enum_definition
from .enum_plug_resolver import resolve_enum_plug
from .float_plug_resolver import resolve_float_plug
from .plugs_binding import (
    MayaBoolPlugsBinding,
    MayaEnumPlugsBinding,
    MayaFloatPlugsBinding,
)
from .plugs_value_edits import (
    MayaBoolValueEdit,
    MayaEnumValueEdit,
    MayaFloatValueEdit,
    MayaPlugsValueEdit,
    apply_plugs_values,
)

__all__ = [
    "MayaScalarValue",
    "MayaScalarValueSnapshot",
    "MayaNodeValueSnapshot",
    "MayaScalarValueTransfer",
    "MayaScalarPasteResult",
    "MayaScalarValueClipboard",
    "capture_scalar_node_values",
    "capture_all_scalar_node_values",
    "encode_scalar_value_transfer",
    "decode_scalar_value_transfer",
    "apply_scalar_value_transfer",
    "apply_scalar_value_transfer_to_paths",
    "apply_scalar_value_to_paths",
]

MayaScalarValue: TypeAlias = bool | float | int
_ScalarBinding: TypeAlias = (
    MayaBoolPlugsBinding | MayaFloatPlugsBinding | MayaEnumPlugsBinding
)

_FORMAT = "bd_util.maya.scalar_values"
_VERSION = 1
_KINDS: tuple[ScalarAttributeKind, ...] = (
    "bool",
    "number",
    "distance",
    "angle",
    "enum",
)
_MAX_NODES = 64
_MAX_VALUES = 10_000
_MAX_ENUM_ITEMS = 2048
_MAX_PATH_LENGTH = 1024
_MAX_ENUM_NAME_LENGTH = 256
_CLIPBOARD = JsonClipboard(
    "application/vnd.bakedanuki.maya-scalar-values+json",
    "BAKEDANUKI_MAYA_SCALAR_VALUES/1\n",
)


def _require_path(value: object) -> str:
    """配列要素を含まないnode相対の正式属性pathを検証する。"""
    if not isinstance(value, str):
        raise TypeError("pathにはstrを指定してください")
    if (
        not value
        or len(value) > _MAX_PATH_LENGTH
        or value.startswith(".")
        or value.endswith(".")
        or ".." in value
        or "\x00" in value
        or "[" in value
        or "]" in value
    ):
        raise ValueError("pathには有効なscalar属性pathを指定してください")
    return value


def _require_kind(value: object) -> ScalarAttributeKind:
    """対応するscalar属性種別だけを受け付ける。"""
    if value not in _KINDS:
        raise ValueError(f"未対応のscalar属性種別です: {value}")
    return cast(ScalarAttributeKind, value)


@dataclass(frozen=True)
class MayaScalarValueSnapshot:
    """node相対path、値型、公開単位の未丸め値とenum定義。"""

    path: str
    kind: ScalarAttributeKind
    value: MayaScalarValue
    enum_definition: EnumDefinition | None = None

    def __post_init__(self) -> None:
        """暗黙の数値変換を避け、kindと値の対応を固定する。"""
        _require_path(self.path)
        kind = _require_kind(self.kind)
        if kind == "bool":
            if type(self.value) is not bool:
                raise TypeError(
                    "bool snapshotのvalueにはboolを指定してください"
                )
        elif kind == "enum":
            if not isinstance(self.value, int) or isinstance(self.value, bool):
                raise TypeError(
                    "enum snapshotのvalueにはintを指定してください"
                )
            if not isinstance(self.enum_definition, EnumDefinition):
                raise TypeError("enum snapshotにはenum_definitionが必要です")
            if len(self.enum_definition.items) > _MAX_ENUM_ITEMS:
                raise ValueError(
                    f"enum項目は{_MAX_ENUM_ITEMS}件以下にしてください"
                )
            if any(
                len(item.name) > _MAX_ENUM_NAME_LENGTH
                for item in self.enum_definition.items
            ):
                raise ValueError("enum項目名が長すぎます")
            if self.enum_definition.item_for_value(self.value) is None:
                raise ValueError("enum snapshotのvalueが定義されていません")
        else:
            if type(self.value) is not float:
                raise TypeError(
                    "数値snapshotのvalueにはfloatを指定してください"
                )
            if not math.isfinite(self.value):
                raise ValueError("数値snapshotには有限値を指定してください")
        if kind != "enum" and self.enum_definition is not None:
            raise ValueError("enum以外にenum_definitionは指定できません")


@dataclass(frozen=True)
class MayaNodeValueSnapshot:
    """一つの基準nodeから同時に取得した順序付きscalar値。"""

    values: tuple[MayaScalarValueSnapshot, ...]

    def __post_init__(self) -> None:
        """空・過大・重複した属性集合を拒否する。"""
        if not isinstance(self.values, tuple):
            raise TypeError("valuesにはtupleを指定してください")
        if not self.values:
            raise ValueError("valuesには一つ以上のsnapshotが必要です")
        if len(self.values) > _MAX_VALUES:
            raise ValueError(f"valuesは{_MAX_VALUES}件以下にしてください")
        paths: set[str] = set()
        for value in self.values:
            if not isinstance(value, MayaScalarValueSnapshot):
                raise TypeError(
                    "valuesにはMayaScalarValueSnapshotを指定してください"
                )
            if value.path in paths:
                raise ValueError(
                    f"同じ属性pathを複数回指定できません: {value.path}"
                )
            paths.add(value.path)


@dataclass(frozen=True)
class MayaScalarValueTransfer:
    """将来の複数コピー元も表現できるscalar値の搬送単位。"""

    nodes: tuple[MayaNodeValueSnapshot, ...]

    def __post_init__(self) -> None:
        """node snapshotの型と件数を検証する。"""
        if not isinstance(self.nodes, tuple):
            raise TypeError("nodesにはtupleを指定してください")
        if not self.nodes or len(self.nodes) > _MAX_NODES:
            raise ValueError(f"nodesは1件以上{_MAX_NODES}件以下にしてください")
        if any(
            not isinstance(node, MayaNodeValueSnapshot) for node in self.nodes
        ):
            raise TypeError("nodesにはMayaNodeValueSnapshotを指定してください")
        if sum(len(node.values) for node in self.nodes) > _MAX_VALUES:
            raise ValueError(f"全valuesは{_MAX_VALUES}件以下にしてください")


@dataclass(frozen=True)
class MayaScalarPasteResult:
    """同path貼り付けの変更有無、適用候補数、対象外理由。"""

    changed: bool
    eligible_count: int
    excluded: tuple[str, ...]


class MayaScalarValueClipboard:
    """Maya scalar値の搬送schemaをOSクリップボードへ読み書きする。"""

    def contains(self) -> bool:
        """対応MIMEまたは専用markerが現在のclipboardにあるか返す。"""
        return _CLIPBOARD.contains()

    def write(self, transfer: MayaScalarValueTransfer) -> None:
        """検証済みtransferをversion付きJSONとしてOSへ保存する。"""
        _CLIPBOARD.write(encode_scalar_value_transfer(transfer))

    def read(self) -> MayaScalarValueTransfer:
        """OS上の外部入力をschema検証して型付きtransferへ変換する。"""
        return decode_scalar_value_transfer(_CLIPBOARD.read())


def capture_scalar_node_values(
    node_name: str, attributes: Sequence[ScalarAttributeInfo]
) -> MayaNodeValueSnapshot:
    """一つのnodeから指定scalar属性の公開単位値をsnapshotへ複製する。"""
    if not isinstance(node_name, str) or not node_name:
        raise ValueError("node_nameには空でないstrを指定してください")
    snapshots: list[MayaScalarValueSnapshot] = []
    for attribute in attributes:
        if not isinstance(attribute, ScalarAttributeInfo):
            raise TypeError(
                "attributesにはScalarAttributeInfoを指定してください"
            )
        if attribute.kind == "bool":
            value: MayaScalarValue = resolve_bool_plug(
                node_name, attribute.path
            ).get()
            definition = None
        elif attribute.kind == "enum":
            enum_value = EnumPlugValue(
                resolve_enum_plug(node_name, attribute.path).plug
            )
            value = enum_value.read()
            definition = enum_value.definition
        else:
            value = FloatPlugValue(
                resolve_float_plug(node_name, attribute.path).plug
            ).read()
            definition = None
        snapshots.append(
            MayaScalarValueSnapshot(
                attribute.path,
                attribute.kind,
                value,
                enum_definition=definition,
            )
        )
    return MayaNodeValueSnapshot(tuple(snapshots))


def capture_all_scalar_node_values(node_name: str) -> MayaNodeValueSnapshot:
    """一つのnodeから対応する全scalar属性値をsnapshotへ複製する。"""
    return capture_scalar_node_values(
        node_name, inspect_scalar_attributes(node_name)
    )


def encode_scalar_value_transfer(
    transfer: MayaScalarValueTransfer,
) -> dict[str, object]:
    """型付きtransferをJSON互換のversion 1 documentへ変換する。"""
    if not isinstance(transfer, MayaScalarValueTransfer):
        raise TypeError(
            "transferにはMayaScalarValueTransferを指定してください"
        )
    nodes: list[object] = []
    for node in transfer.nodes:
        values: list[object] = []
        for snapshot in node.values:
            item: dict[str, object] = {
                "path": snapshot.path,
                "kind": snapshot.kind,
                "value": snapshot.value,
            }
            if snapshot.enum_definition is not None:
                item["enum_items"] = [
                    {"value": enum_item.value, "name": enum_item.name}
                    for enum_item in snapshot.enum_definition.items
                ]
            values.append(item)
        nodes.append({"values": values})
    return {"format": _FORMAT, "version": _VERSION, "nodes": nodes}


def _require_mapping(value: object, name: str) -> dict[str, object]:
    """JSON objectをstr keyのdictとして受け付ける。"""
    if not isinstance(value, dict) or any(
        not isinstance(key, str) for key in value
    ):
        raise TypeError(f"{name}にはJSON objectを指定してください")
    return cast(dict[str, object], value)


def _require_keys(
    value: dict[str, object],
    required: set[str],
    optional: set[str] | frozenset[str] = frozenset(),
) -> None:
    """schemaの不足keyと未知keyを同時に拒否する。"""
    missing = required - value.keys()
    unknown = value.keys() - required - optional
    if missing:
        raise ValueError("不足しているkey: " + ", ".join(sorted(missing)))
    if unknown:
        raise ValueError("未対応のkey: " + ", ".join(sorted(unknown)))


def _require_list(value: object, name: str) -> list[object]:
    """JSON arrayだけを受け付け、tupleなどの暗黙変換を避ける。"""
    if not isinstance(value, list):
        raise TypeError(f"{name}にはJSON arrayを指定してください")
    return cast(list[object], value)


def _decode_enum_definition(value: object) -> EnumDefinition:
    """個数と文字列長を制限してenum定義を復元する。"""
    raw_items = _require_list(value, "enum_items")
    if len(raw_items) > _MAX_ENUM_ITEMS:
        raise ValueError(f"enum_itemsは{_MAX_ENUM_ITEMS}件以下にしてください")
    items: list[EnumItem] = []
    for raw_item in raw_items:
        item = _require_mapping(raw_item, "enum item")
        _require_keys(item, {"value", "name"})
        enum_value = item["value"]
        name = item["name"]
        if not isinstance(enum_value, int) or isinstance(enum_value, bool):
            raise TypeError("enum itemのvalueにはintを指定してください")
        if (
            not isinstance(name, str)
            or not name
            or len(name) > _MAX_ENUM_NAME_LENGTH
        ):
            raise ValueError("enum itemのnameが不正です")
        items.append(EnumItem(enum_value, name))
    return EnumDefinition(tuple(items))


def _decode_snapshot(value: object) -> MayaScalarValueSnapshot:
    """一つのJSON値をkindに対応するsnapshotへ変換する。"""
    item = _require_mapping(value, "value item")
    _require_keys(item, {"path", "kind", "value"}, {"enum_items"})
    path = _require_path(item["path"])
    kind = _require_kind(item["kind"])
    raw_value = item["value"]
    definition = None
    if kind == "bool":
        if type(raw_value) is not bool:
            raise TypeError("bool valueにはboolを指定してください")
        parsed_value: MayaScalarValue = raw_value
    elif kind == "enum":
        if not isinstance(raw_value, int) or isinstance(raw_value, bool):
            raise TypeError("enum valueにはintを指定してください")
        if "enum_items" not in item:
            raise ValueError("enum valueにはenum_itemsが必要です")
        parsed_value = raw_value
        definition = _decode_enum_definition(item["enum_items"])
    else:
        if not isinstance(raw_value, (int, float)) or isinstance(
            raw_value, bool
        ):
            raise TypeError("numeric valueには数値を指定してください")
        parsed_value = float(raw_value)
        if not math.isfinite(parsed_value):
            raise ValueError("numeric valueには有限値を指定してください")
    if kind != "enum" and "enum_items" in item:
        raise ValueError("enum以外にenum_itemsは指定できません")
    return MayaScalarValueSnapshot(
        path, kind, parsed_value, enum_definition=definition
    )


def decode_scalar_value_transfer(document: object) -> MayaScalarValueTransfer:
    """外部JSON documentを完全検証してversion 1 transferへ変換する。"""
    root = _require_mapping(document, "document")
    _require_keys(root, {"format", "version", "nodes"})
    if root["format"] != _FORMAT:
        raise ValueError("対応していないclipboard形式です")
    version = root["version"]
    if not isinstance(version, int) or isinstance(version, bool):
        raise TypeError("clipboard schema versionにはintを指定してください")
    if version != _VERSION:
        raise ValueError("対応していないclipboard schema versionです")
    raw_nodes = _require_list(root["nodes"], "nodes")
    if not raw_nodes or len(raw_nodes) > _MAX_NODES:
        raise ValueError(f"nodesは1件以上{_MAX_NODES}件以下にしてください")
    nodes: list[MayaNodeValueSnapshot] = []
    total = 0
    for raw_node in raw_nodes:
        node = _require_mapping(raw_node, "node")
        _require_keys(node, {"values"})
        raw_values = _require_list(node["values"], "values")
        total += len(raw_values)
        if total > _MAX_VALUES:
            raise ValueError(f"全valuesは{_MAX_VALUES}件以下にしてください")
        nodes.append(
            MayaNodeValueSnapshot(
                tuple(_decode_snapshot(item) for item in raw_values)
            )
        )
    return MayaScalarValueTransfer(tuple(nodes))


def _create_edit(
    node_name: str, snapshot: MayaScalarValueSnapshot
) -> tuple[MayaPlugsValueEdit, _ScalarBinding]:
    """一つのtarget plugを監視するBindingと型付き入力を生成する。"""
    if snapshot.kind == "bool":
        bool_binding = MayaBoolPlugsBinding(
            [resolve_bool_plug(node_name, snapshot.path)]
        )
        return (
            MayaBoolValueEdit(bool_binding, cast(bool, snapshot.value)),
            bool_binding,
        )
    if snapshot.kind == "enum":
        enum_plug = resolve_enum_plug(node_name, snapshot.path)
        definition = snapshot.enum_definition
        if definition is None or not definition.matches(
            read_enum_definition(enum_plug)
        ):
            raise ValueError("enum定義（整数値と項目名）が異なります")
        if definition.item_for_value(cast(int, snapshot.value)) is None:
            raise ValueError("コピー元のenum値が定義されていません")
        enum_binding = MayaEnumPlugsBinding([enum_plug])
        return (
            MayaEnumValueEdit(enum_binding, cast(int, snapshot.value)),
            enum_binding,
        )
    float_binding = MayaFloatPlugsBinding(
        [resolve_float_plug(node_name, snapshot.path)]
    )
    return (
        MayaFloatValueEdit(float_binding, cast(float, snapshot.value)),
        float_binding,
    )


def apply_scalar_value_transfer(
    node_names: Sequence[str], transfer: MayaScalarValueTransfer
) -> MayaScalarPasteResult:
    """一つのsource snapshotを全target nodeの同pathへ一Undoで適用する。"""
    if not isinstance(transfer, MayaScalarValueTransfer):
        raise TypeError(
            "transferにはMayaScalarValueTransferを指定してください"
        )
    if len(transfer.nodes) != 1:
        raise ValueError("現在は一つのコピー元nodeだけ貼り付けられます")
    targets = tuple(node_names)
    if not targets:
        raise ValueError(
            "node_namesには一つ以上のtarget nodeを指定してください"
        )
    if any(not isinstance(name, str) or not name for name in targets):
        raise ValueError("node_namesには空でないstrを指定してください")
    if len(set(targets)) != len(targets):
        raise ValueError("同じtarget nodeを複数回指定できません")

    # 属性構成を先に固定し、行位置ではなく正式pathとkindだけで対応させる
    target_attributes = {
        node_name: {
            attribute.path: attribute
            for attribute in inspect_scalar_attributes(node_name)
        }
        for node_name in targets
    }
    edits: list[MayaPlugsValueEdit] = []
    bindings: list[_ScalarBinding] = []
    excluded: list[str] = []
    try:
        for snapshot in transfer.nodes[0].values:
            for node_name in targets:
                attribute = target_attributes[node_name].get(snapshot.path)
                plug_name = f"{node_name}.{snapshot.path}"
                if attribute is None:
                    excluded.append(f"{plug_name}: 対応する属性なし")
                    continue
                if attribute.kind != snapshot.kind:
                    excluded.append(f"{plug_name}: 型・単位が異なる")
                    continue
                try:
                    edit, binding = _create_edit(node_name, snapshot)
                except (TypeError, ValueError) as error:
                    excluded.append(f"{plug_name}: {error}")
                    continue
                state = binding.target_states[0]
                if not state.is_writable:
                    excluded.append(
                        f"{plug_name}: {state.reason or '値を編集できません'}"
                    )
                    binding.dispose()
                    binding.deleteLater()
                    continue
                edits.append(edit)
                bindings.append(binding)
        changed = apply_plugs_values(edits)
        return MayaScalarPasteResult(changed, len(edits), tuple(excluded))
    finally:
        for binding in bindings:
            binding.dispose()
            binding.deleteLater()


def _require_target_paths(target_paths: Sequence[str]) -> tuple[str, ...]:
    """重複のない一つ以上の貼り付け先pathを検証する。"""
    if isinstance(target_paths, str):
        raise TypeError("target_pathsにはstrのsequenceを指定してください")
    paths = tuple(_require_path(path) for path in target_paths)
    if not paths:
        raise ValueError("target_pathsには一つ以上の属性pathが必要です")
    if len(paths) > _MAX_VALUES:
        raise ValueError(f"target_pathsは{_MAX_VALUES}件以下にしてください")
    if len(set(paths)) != len(paths):
        raise ValueError("同じtarget pathを複数回指定できません")
    return paths


def apply_scalar_value_transfer_to_paths(
    node_names: Sequence[str],
    target_paths: Sequence[str],
    transfer: MayaScalarValueTransfer,
) -> MayaScalarPasteResult:
    """搬送値のうち指定した同一pathだけを全target nodeへ適用する。"""
    if not isinstance(transfer, MayaScalarValueTransfer):
        raise TypeError(
            "transferにはMayaScalarValueTransferを指定してください"
        )
    if len(transfer.nodes) != 1:
        raise ValueError("現在は一つのコピー元nodeだけ貼り付けられます")
    paths = _require_target_paths(target_paths)
    targets = tuple(node_names)
    if not targets:
        raise ValueError(
            "node_namesには一つ以上のtarget nodeを指定してください"
        )
    if any(not isinstance(name, str) or not name for name in targets):
        raise ValueError("node_namesには空でないstrを指定してください")
    if len(set(targets)) != len(targets):
        raise ValueError("同じtarget nodeを複数回指定できません")

    # 選択pathとの共通部分だけを保持し、clipboardにない選択先も結果へ残す
    values_by_path = {
        snapshot.path: snapshot for snapshot in transfer.nodes[0].values
    }
    selected_values = tuple(
        values_by_path[path] for path in paths if path in values_by_path
    )
    excluded = tuple(
        f"{node_name}.{path}: コピーされた値なし"
        for path in paths
        if path not in values_by_path
        for node_name in targets
    )
    if not selected_values:
        return MayaScalarPasteResult(False, 0, excluded)
    result = apply_scalar_value_transfer(
        targets,
        MayaScalarValueTransfer((MayaNodeValueSnapshot(selected_values),)),
    )
    return MayaScalarPasteResult(
        result.changed,
        result.eligible_count,
        result.excluded + excluded,
    )


def apply_scalar_value_to_paths(
    node_names: Sequence[str],
    target_paths: Sequence[str],
    transfer: MayaScalarValueTransfer,
) -> MayaScalarPasteResult:
    """一つの搬送値を全target nodeの指定pathへ一Undoで適用する。"""
    if not isinstance(transfer, MayaScalarValueTransfer):
        raise TypeError(
            "transferにはMayaScalarValueTransferを指定してください"
        )
    if len(transfer.nodes) != 1 or len(transfer.nodes[0].values) != 1:
        raise ValueError(
            "異なる複数属性へ貼り付けるには一つの属性値が必要です"
        )
    paths = _require_target_paths(target_paths)

    # 搬送値の型と実値を保ち、明示された正式pathだけへ展開する
    source = transfer.nodes[0].values[0]
    expanded = MayaNodeValueSnapshot(
        tuple(
            MayaScalarValueSnapshot(
                path,
                source.kind,
                source.value,
                enum_definition=source.enum_definition,
            )
            for path in paths
        )
    )
    return apply_scalar_value_transfer(
        node_names,
        MayaScalarValueTransfer((expanded,)),
    )
