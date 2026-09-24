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
    from ._versioned_accessors import (  # pyright: ignore[reportMissingModuleSource]
        AnimLayerNode,
    )
    from .modifier import ModifierManager
    from .operator.node._core import NodeOperator

LayerMode = Literal["flatten", "preserve"]
RestoreMode = Literal["merge", "replace_all", "replace_range"]


def finite_number(value: object, name: str) -> float:
    """値を有限の浮動小数点数として検証する。

    Args:
        value: 検証する数値。bool は受け付けない。
        name: エラーメッセージに使う項目名。

    Returns:
        変換後の浮動小数点数。

    Raises:
        TypeError: 値が数値でない場合。
        ValueError: 値が有限でない場合。
    """
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise TypeError(f"{name} must be a number.")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite.")
    return result


def literal_name(value: object) -> str:
    """ワイルドカードを含まない空でない名前を検証する。

    Args:
        value: 検証する名前。

    Returns:
        検証済みの文字列。

    Raises:
        ValueError: 名前が空、不正な型、またはワイルドカードを含む場合。
    """
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
    """一つの属性とレイヤーに属するアニメーションカーブ。"""

    attribute: str
    layer: str | None
    curve: AnimCurveData

    @classmethod
    def from_dict(cls, value: object) -> ChannelAnimationData:
        """属性・レイヤー・カーブを持つ辞書から復元する。"""
        data = _record(value, "attribute layer curve")
        return cls(
            literal_name(data["attribute"]),
            None if data["layer"] is None else literal_name(data["layer"]),
            AnimCurveData.from_dict(data["curve"]),
        )


@dataclass(frozen=True, slots=True)
class NodeAnimationData:
    """一つのノードの名前と属性ごとのアニメーション。"""

    name: str
    channels: tuple[ChannelAnimationData, ...]

    @classmethod
    def from_dict(cls, value: object) -> NodeAnimationData:
        """ノード名とチャンネルを持つ辞書から復元する。"""
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
    """アニメーションレイヤー設定の値と任意のアニメーションカーブ。"""

    name: str
    value: float
    curve: AnimCurveData | None

    @classmethod
    def from_dict(cls, value: object) -> LayerSettingData:
        """レイヤー設定名・値・カーブを持つ辞書から復元する。"""
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
    """アニメーションレイヤーの親子関係と設定。"""

    name: str
    parent: str | None
    settings: tuple[LayerSettingData, ...]

    @classmethod
    def from_dict(cls, value: object) -> AnimationLayerData:
        """レイヤー名・親・設定を持つ辞書から復元する。"""
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
    """シーンから独立したアニメーション保存データ。

    JSON 形式は schema 2 のみ扱う。ノード順、保存範囲、レイヤー構造を保持する。

    Attributes:
        nodes: 保存順に並ぶノードと属性カーブ。
        layers: 親が子より先に並ぶレイヤー情報。
        layer_mode: 合成値を保存する ``flatten`` または生カーブの ``preserve``。
        start_frame: 保存区間の開始。
        end_frame: 保存区間の終了。
        seconds_per_frame: 保存時の 1 frame あたりの秒数。
        root_settings: ルートレイヤーの設定。flatten では空。
        clipped: 区間を切り出して保存したか。
        sample_by: flatten 時の採取間隔。preserve 時は生カーブを保持する。
        schema_version: JSON の schema バージョン。常に 2。
    """

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
        # 保存形式と時間範囲を確定してから参照関係を検証する。
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
        # 親が子より先に現れる順序を要求する。
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
        """JSON 化できる辞書に変換する。"""
        return asdict(self)

    def to_json(self, *, indent: int | None = 2) -> str:
        """日本語を Unicode のまま保つ JSON 文字列へ変換する。

        Args:
            indent: インデント幅。None では改行を入れない。
        """
        return json.dumps(
            self.to_dict(), ensure_ascii=False, allow_nan=False, indent=indent
        )

    @classmethod
    def from_dict(cls, value: object) -> AnimationClip:
        """schema 2 の辞書を検証して独立した clip に復元する。

        Args:
            value: 保存済みの clip 辞書。

        Returns:
            検証済みの AnimationClip。

        Raises:
            TypeError: 辞書やフィールドの型が不正な場合。
            ValueError: schema、範囲、レイヤー構造などが不正な場合。
        """
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
        """JSON 文字列を検証して独立した clip に復元する。"""
        return cls.from_dict(json.loads(value))

    def save(
        self,
        path: str | PathLike[str],
        *,
        indent: int | None = 2,
        overwrite: bool = True,
        create_parents: bool = True,
    ) -> Path:
        """schema 2 の JSON ファイルへ clip を即時保存する。

        シーンと予約中の操作は変更しない。ファイル操作は Undo 対象外。

        Args:
            path: 保存先のパス。
            indent: JSON のインデント幅。
            overwrite: 既存ファイルを上書きするか。
            create_parents: 親ディレクトリを作成するか。

        Returns:
            実際の保存先 Path。
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
        """JSON ファイルを検証して独立した clip を返す。

        Args:
            path: 読み込む JSON ファイル。

        Returns:
            シーンには復元しない AnimationClip。
        """
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
        layers: Iterable[AnimLayerNode | om.MObject | str] | None = None,
        sample_by: float = 1.0,
    ) -> AnimationClip:
        """指定ノードのアニメーションを即時取得する。

        compound と既存配列は scalar 子属性へ展開する。
        予約中の modifier は実行しない。

        Args:
            nodes: 保存するノードの iterable。
            attributes: 各ノードに共通の属性名。省略時は keyable 属性。
            include_channel_box: 自動収集時に Channel Box 属性も含めるか。
            include_static: 時間変化のない属性も含めるか。
            start_frame: 保存区間の開始。None は取得したキー範囲の開始。
            end_frame: 保存区間の終了。None は取得したキー範囲の終了。
            layer_mode: 合成値の ``flatten`` またはレイヤー別の ``preserve``。
            layers: preserve 時に保存するレイヤー。None は所属レイヤー。
            sample_by: flatten 時の採取間隔。現在の UI 時間単位で指定する。

        Returns:
            シーンから独立した AnimationClip。

        Raises:
            ValueError: キー範囲を得られず、保存区間も指定されていない場合。
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
        """保存カーブのキーを削減した新しい clip を返す。

        区間の最初と最後のキー、レイヤー設定カーブは維持する。
        元の clip とシーンは変更しない。

        Args:
            start_frame: 保存時の時間単位で指定する開始。None は制限しない。
            end_frame: 保存時の時間単位で指定する終了。None は制限しない。
            tolerance: 許容する値の絶対誤差。角度は degree、距離は cm。
            preserve_breakdowns: breakdown キーを残すか。

        Returns:
            キー削減後の独立した AnimationClip。
        """
        from ._animation_clip_reduce import reduce_keys

        return reduce_keys(
            self,
            start_frame,
            end_frame,
            tolerance=tolerance,
            preserve_breakdowns=preserve_breakdowns,
        )

    def extract(
        self,
        *,
        nodes: Iterable[NodeOperator | om.MObject | str],
    ) -> AnimationClip:
        """指定した保存ノードだけを持つ新しい clip を返す。

        元の clip、シーン、予約中の操作は変更しない。

        Args:
            nodes: 保存名、既存ノード、または明示名付きの作成予定ノード。
                短い名前の一致が複数ある場合は拒否する。

        Returns:
            指定順にノードを並べた独立した AnimationClip。
        """
        from ._animation_clip_extract import extract

        return extract(self, nodes=nodes)

    def reversed(self) -> AnimationClip:
        """保存範囲を軸に全カーブの時間を反転した新しい clip を返す。

        レイヤー設定カーブも同じ軸で反転する。元の clip とシーンは変更しない。
        """
        from ._animation_clip_reverse import reversed_clip

        return reversed_clip(self)

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
        """保存したアニメーションの復元を予約する。

        保存区間は clip の時間単位、復元先時刻は予約時の UI 時間単位。
        開始・終了時刻の両方指定は時間倍率・長さ・移動量と併用できない。
        復元に失敗した場合は操作全体を戻す。

        Args:
            modifier_manager: 復元操作を予約する先。
            targets: 保存ノード順に対応する復元先。namespace とは併用不可。
            namespace: 復元先ノードに付ける名前空間。
            mode: ``merge``、``replace_all``、``replace_range`` のいずれか。
            start_frame: 保存データ内の使用区間の開始。None は保存範囲の端。
            end_frame: 保存データ内の使用区間の終了。None は保存範囲の端。
            offset_frames: 復元時刻に加える移動量。
            to_start_frame: 復元先の開始時刻。
            to_end_frame: 復元先の終了時刻。開始と両方指定すると区間を合わせる。
            time_scale: 正の時間倍率。duration_frames との併用不可。
            duration_frames: 復元区間の長さ。time_scale との併用不可。
            restore_layer_settings: 設定が異なる既存レイヤーも更新するか。
            tolerance: flatten 値の復元確認に使う許容誤差。
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
