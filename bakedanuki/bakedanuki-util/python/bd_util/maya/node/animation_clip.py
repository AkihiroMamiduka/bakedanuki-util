"""複数ノードのアニメーションを保存する、sceneから独立したデータ。"""

from __future__ import annotations

import json
import math
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from os import PathLike
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast, overload

from ...py import json_file
from .operator.attr.keyframe_data import AnimCurveData

if TYPE_CHECKING:
    from maya.api import OpenMaya as om
    from .modifier import ModifierManager
    from .operator.node._core import NodeOperator

LayerMode = Literal["flatten", "preserve"]
RestoreMode = Literal["merge", "replace_all", "replace_range"]


def finite_number(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise TypeError(f"{name} must be a number.")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite.")
    return result


def literal_name(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value
        or any(c in value for c in "*?\x00")
    ):
        raise ValueError("Expected a nonempty, literal name.")
    return value


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


@dataclass(frozen=True, slots=True)
class ChannelAnimationData:
    attribute: str
    layer: str | None
    curve: AnimCurveData

    @classmethod
    def from_dict(cls, value: object) -> ChannelAnimationData:
        data = _record(value, "attribute layer curve")
        return cls(
            literal_name(data["attribute"]),
            None if data["layer"] is None else literal_name(data["layer"]),
            AnimCurveData.from_dict(data["curve"]),
        )


@dataclass(frozen=True, slots=True)
class NodeAnimationData:
    name: str
    channels: tuple[ChannelAnimationData, ...]

    @classmethod
    def from_dict(cls, value: object) -> NodeAnimationData:
        data = _record(value, "name channels")
        return cls(
            literal_name(data["name"]),
            tuple(
                ChannelAnimationData.from_dict(item)
                for item in _items(data["channels"])
            ),
        )


LAYER_SETTINGS = (
    "override",
    "passthrough",
    "rotationAccumulationMode",
    "scaleAccumulationMode",
    "weight",
    "mute",
    "solo",
    "lock",
)


@dataclass(frozen=True, slots=True)
class LayerSettingData:
    name: str
    value: float
    curve: AnimCurveData | None

    @classmethod
    def from_dict(cls, value: object) -> LayerSettingData:
        data = _record(value, "name value curve")
        name = literal_name(data["name"])
        if name not in LAYER_SETTINGS:
            raise ValueError(f"Unsupported layer setting: {name}.")
        return cls(
            name,
            finite_number(data["value"], name),
            (
                None
                if data["curve"] is None
                else AnimCurveData.from_dict(data["curve"])
            ),
        )


@dataclass(frozen=True, slots=True)
class AnimationLayerData:
    name: str
    parent: str | None
    settings: tuple[LayerSettingData, ...]

    @classmethod
    def from_dict(cls, value: object) -> AnimationLayerData:
        data = _record(value, "name parent settings")
        settings = tuple(
            LayerSettingData.from_dict(item)
            for item in _items(data["settings"])
        )
        if tuple(item.name for item in settings) != LAYER_SETTINGS:
            raise ValueError(
                "Layer settings must contain every supported setting in order."
            )
        return cls(
            literal_name(data["name"]),
            None if data["parent"] is None else literal_name(data["parent"]),
            settings,
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class AnimationClip:
    """保存範囲・ノード順・レイヤー構造を持つアニメーション。JSONはschema 2のみ。"""

    nodes: tuple[NodeAnimationData, ...]
    layers: tuple[AnimationLayerData, ...]
    layer_mode: LayerMode
    start_frame: float
    end_frame: float
    seconds_per_frame: float
    root_settings: tuple[LayerSettingData, ...] = ()
    clipped: bool = False
    sample_by: float = 1.0
    schema_version: Literal[2] = 2

    def __post_init__(self) -> None:
        if type(self.clipped) is not bool:
            raise TypeError("clipped must be a bool.")
        if type(self.schema_version) is not int or self.schema_version != 2:
            raise ValueError("Unsupported AnimationClip schema_version.")
        if self.layer_mode not in ("flatten", "preserve"):
            raise ValueError("layer_mode must be flatten or preserve.")
        for name in (
            "start_frame",
            "end_frame",
            "seconds_per_frame",
            "sample_by",
        ):
            object.__setattr__(
                self, name, finite_number(getattr(self, name), name)
            )
        if (
            self.start_frame > self.end_frame
            or self.seconds_per_frame <= 0
            or self.sample_by <= 0
        ):
            raise ValueError(
                "Expected an ordered finite range and positive time units/sample_by."
            )
        object.__setattr__(
            self,
            "nodes",
            tuple(
                NodeAnimationData.from_dict(asdict(node))
                for node in self.nodes
            ),
        )
        object.__setattr__(
            self,
            "layers",
            tuple(
                AnimationLayerData.from_dict(asdict(layer))
                for layer in self.layers
            ),
        )
        root_settings = tuple(
            LayerSettingData.from_dict(asdict(item))
            for item in self.root_settings
        )
        if (
            root_settings
            and tuple(item.name for item in root_settings) != LAYER_SETTINGS
        ):
            raise ValueError(
                "Root settings must contain every supported setting in order."
            )
        object.__setattr__(self, "root_settings", root_settings)
        finite_number(
            self.start_frame * self.seconds_per_frame, "start time in seconds"
        )
        finite_number(
            self.end_frame * self.seconds_per_frame, "end time in seconds"
        )
        names: set[str] = set()
        for layer in self.layers:
            if layer.name in names or (
                layer.parent is not None and layer.parent not in names
            ):
                raise ValueError(
                    "Layers must be unique and ordered parent before child."
                )
            names.add(layer.name)
        if self.layer_mode == "flatten" and (
            self.layers or self.root_settings
        ):
            raise ValueError("Flattened clips cannot contain layer structure.")
        node_names: set[str] = set()
        for node in self.nodes:
            if node.name in node_names:
                raise ValueError("Clip node names must be unique.")
            node_names.add(node.name)
            channels: set[tuple[str, str | None]] = set()
            for channel in node.channels:
                key = (channel.attribute, channel.layer)
                if key in channels or (
                    channel.layer is not None and channel.layer not in names
                ):
                    raise ValueError(
                        "Duplicate channel or missing layer definition."
                    )
                channels.add(key)
                if channel.curve.seconds_per_frame != self.seconds_per_frame:
                    raise ValueError("All curves must use the clip time unit.")
                if any(
                    not self.start_frame <= k.frame <= self.end_frame
                    for k in channel.curve.keys
                ):
                    raise ValueError(
                        "Clip keys must be inside the saved range."
                    )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

    def to_json(self, *, indent: int | None = 2) -> str:
        return json.dumps(
            self.to_dict(), ensure_ascii=False, allow_nan=False, indent=indent
        )

    @classmethod
    def from_dict(cls, value: object) -> AnimationClip:
        data = _record(
            value,
            "nodes layers root_settings clipped layer_mode start_frame end_frame seconds_per_frame sample_by schema_version",
        )
        mode = data["layer_mode"]
        if mode not in ("flatten", "preserve"):
            raise ValueError("layer_mode must be flatten or preserve.")
        if (
            type(data["schema_version"]) is not int
            or data["schema_version"] != 2
        ):
            raise ValueError("Unsupported AnimationClip schema_version.")
        if type(data["clipped"]) is not bool:
            raise TypeError("clipped must be a bool.")
        return cls(
            clipped=data["clipped"],
            nodes=tuple(
                NodeAnimationData.from_dict(item)
                for item in _items(data["nodes"])
            ),
            layers=tuple(
                AnimationLayerData.from_dict(item)
                for item in _items(data["layers"])
            ),
            root_settings=tuple(
                LayerSettingData.from_dict(item)
                for item in _items(data["root_settings"])
            ),
            layer_mode=mode,
            start_frame=finite_number(data["start_frame"], "start_frame"),
            end_frame=finite_number(data["end_frame"], "end_frame"),
            seconds_per_frame=finite_number(
                data["seconds_per_frame"], "seconds_per_frame"
            ),
            sample_by=finite_number(data["sample_by"], "sample_by"),
        )

    @classmethod
    def from_json(cls, value: str) -> AnimationClip:
        return cls.from_dict(json.loads(value))

    def save(
        self,
        path: str | PathLike[str],
        *,
        indent: int | None = 2,
        overwrite: bool = True,
        create_parents: bool = True,
    ) -> Path:
        """再検証したschema 2データをJSONファイルへ即時保存し、Pathを返す。

        既定は親フォルダを作成し、既存ファイルを上書きする。
        scene・保留中modifierは変更しない。ファイル操作はUndoの対象外。
        """
        data = self.from_dict(self.to_dict()).to_dict()
        return json_file.write(
            path,
            data,
            indent=indent,
            overwrite=overwrite,
            create_parents=create_parents,
        )

    @classmethod
    def load(cls, path: str | PathLike[str]) -> AnimationClip:
        """JSONファイルを再検証し、独立clipを返す。sceneへの復元は行わない。"""
        return cls.from_dict(json_file.read(path))

    @classmethod
    def capture(
        cls,
        nodes: Iterable[NodeOperator | om.MObject | str],
        *,
        attributes: Iterable[str] | None = None,
        include_channel_box: bool = False,
        include_static: bool = False,
        start_frame: float | None = None,
        end_frame: float | None = None,
        layer_mode: LayerMode = "flatten",
        layers: Iterable[str] | None = None,
        sample_by: float = 1.0,
    ) -> AnimationClip:
        """即時取得。既定はkeyable属性の最終値を1フレーム間隔で合成保存する。

        attributesは各nodeに共通の属性名。compoundと既存array要素はleafへ展開。
        静的な属性は既定で除外し、include_static=Trueで含める。
        キー・時間依存がある属性と、レイヤー再現に必要な静的な生値は保持する。
        layersはpreserve専用で、省略時はベースと対象属性の所属layerを保存する。
        指定layerの親は構造・設定のみ保存する。queryは保留中modifierを実行しない。
        """
        from ._animation_clip_capture import capture

        return capture(
            nodes,
            attributes=attributes,
            include_channel_box=include_channel_box,
            include_static=include_static,
            start_frame=start_frame,
            end_frame=end_frame,
            layer_mode=layer_mode,
            layers=layers,
            sample_by=sample_by,
        )

    def reduce_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        tolerance: float,
        preserve_breakdowns: bool = True,
    ) -> AnimationClip:
        """保存カーブのキーを削減した独立したclipを即時に返す。

        元clip・scene・保留中modifierは変更しない。対象は全nodeの属性チャンネルで、
        layerとrootの設定カーブは維持する。時間はclipに保存されたフレーム単位。
        両端包含、None側は無制限。範囲内の最初・最後の実在キーを残し、挿入はしない。
        toleranceは非負の絶対誤差（degree / cm / unitless）。手動接線を調整せず、
        自動接線の再計算も含めて判定する。復元先でのレイヤー合成誤差は保証しない。
        """
        from ._animation_clip_reduce import reduce_keys

        return reduce_keys(
            self,
            start_frame,
            end_frame,
            tolerance=tolerance,
            preserve_breakdowns=preserve_breakdowns,
        )

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: float | None = None,
        to_start_frame: None = None,
        to_end_frame: None = None,
        time_scale: float | None = None,
        duration_frames: None = None,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: float | None = None,
        to_start_frame: None = None,
        to_end_frame: None = None,
        time_scale: None = None,
        duration_frames: float,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: None = None,
        to_start_frame: float,
        to_end_frame: None = None,
        time_scale: float | None = None,
        duration_frames: None = None,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: None = None,
        to_start_frame: float,
        to_end_frame: None = None,
        time_scale: None = None,
        duration_frames: float,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: None = None,
        to_start_frame: None = None,
        to_end_frame: float,
        time_scale: float | None = None,
        duration_frames: None = None,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: None = None,
        to_start_frame: None = None,
        to_end_frame: float,
        time_scale: None = None,
        duration_frames: float,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    @overload
    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: None = None,
        to_start_frame: float,
        to_end_frame: float,
        time_scale: None = None,
        duration_frames: None = None,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None: ...

    def restore(
        self,
        modifier_manager: ModifierManager,
        *,
        targets: Iterable[NodeOperator | om.MObject | str] | None = None,
        namespace: str | None = None,
        mode: RestoreMode = "merge",
        start_frame: float | None = None,
        end_frame: float | None = None,
        offset_frames: float | None = None,
        to_start_frame: float | None = None,
        to_end_frame: float | None = None,
        time_scale: float | None = None,
        duration_frames: float | None = None,
        restore_layer_settings: bool = False,
        tolerance: float = 1e-6,
    ) -> None:
        """復元を予約する。targetsは保存node順、namespaceとは同時指定不可。

        合成値はベースへ逆算設定し、サンプル時刻で検証する。失敗時は全体を戻す。
        preserveは生値を復元。設定不一致の既存layerを変更する場合だけ
        restore_layer_settings=Trueを指定する。予約後のデータ編集は反映しない。
        start_frame / end_frameは保存フレーム単位の使用区間。省略側は保存区間の端。
        範囲指定時は境界補完・連続接線のfixed化後、その区間を基準に拡縮・移動する。
        保存区間外は拒否する。replace_rangeは変換後の区間、replace_allは全カーブを置換。
        復元区間を基準に全キーとlayer設定を拡縮・移動する。倍率または長さは一方だけ指定する。
        to_start_frameとto_end_frameの両方は区間合わせとなり、倍率・長さ・offsetとは併用不可。
        復元先の片側合わせとoffsetは排他。倍率は正、復元先時刻・長さは予約時のUI時間単位。
        未指定・移動量0・倍率1でも通常の復元を行う。
        """
        from ._animation_clip_restore import restore

        restore(
            self,
            modifier_manager,
            targets=targets,
            namespace=namespace,
            mode=mode,
            start_frame=start_frame,
            end_frame=end_frame,
            offset_frames=offset_frames,
            to_start_frame=to_start_frame,
            to_end_frame=to_end_frame,
            time_scale=time_scale,
            duration_frames=duration_frames,
            restore_layer_settings=restore_layer_settings,
            tolerance=tolerance,
        )
