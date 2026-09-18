# coding: utf-8
from __future__ import annotations

import math
from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Callable, Literal, overload

# maya
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import (
    _keyframe_command,
    _keyframe_discovery,
    _keyframe_move,
    _keyframe_reduce,
    _keyframe_scale,
    _keyframe_snapshot,
    _keyframe_target,
    _keyframe_value,
)
from ._keyframe_discovery import CurveNode
from .keyframe_data import AnimCurveData, KeyData

if TYPE_CHECKING:
    from ..._versioned_accessors import (  # pyright: ignore[reportMissingModuleSource]
        AnimLayerNode,
    )
    from ._keyframe_discovery import AnimCurveNode

ValueConverter = Callable[[Any], Any]
TangentTypeName = Literal[
    "auto",
    "clamped",
    "fast",
    "flat",
    "linear",
    "plateau",
    "slow",
    "spline",
    "step",
    "stepnext",
]
TangentTypeValue = TangentTypeName | int | None
_KeyValue = float | om.MAngle | om.MDistance | om.MTime
_CapturedKey = tuple[om.MTime, _KeyValue]


class TangentType:
    auto = oma.MFnAnimCurve.kTangentAuto
    clamped = oma.MFnAnimCurve.kTangentClamped
    fast = oma.MFnAnimCurve.kTangentFast
    flat = oma.MFnAnimCurve.kTangentFlat
    linear = oma.MFnAnimCurve.kTangentLinear
    plateau = oma.MFnAnimCurve.kTangentPlateau
    slow = oma.MFnAnimCurve.kTangentSlow
    spline = oma.MFnAnimCurve.kTangentSmooth
    step = oma.MFnAnimCurve.kTangentStep
    stepnext = oma.MFnAnimCurve.kTangentStepNext


_TANGENT_TYPE_MAP = {
    "auto": TangentType.auto,
    "clamped": TangentType.clamped,
    "fast": TangentType.fast,
    "flat": TangentType.flat,
    "linear": TangentType.linear,
    "plateau": TangentType.plateau,
    "slow": TangentType.slow,
    "spline": TangentType.spline,
    "step": TangentType.step,
    "stepnext": TangentType.stepnext,
}
_VALID_TANGENT_TYPES = set(_TANGENT_TYPE_MAP.values()) | {
    oma.MFnAnimCurve.kTangentGlobal,
}
_TANGENT_TYPE_NAMES = {
    value: name for name, value in _TANGENT_TYPE_MAP.items()
}


def _identity(value: Any) -> Any:
    return value


def _to_tangent_type(tangent_type: int | str | None) -> int:
    if tangent_type is None:
        return oma.MFnAnimCurve.kTangentGlobal

    if isinstance(tangent_type, str):
        tangent_type = tangent_type.lower()
        result = _TANGENT_TYPE_MAP.get(tangent_type)
        if result is not None:
            return result

    else:
        if tangent_type in _VALID_TANGENT_TYPES:
            return tangent_type

    valid_types = ", ".join(sorted(_TANGENT_TYPE_MAP))
    raise ValueError(
        f"Unsupported tangent type: {tangent_type!r}. "
        f"Expected one of: {valid_types}."
    )


def _add_keys(
    curve: oma.MFnAnimCurve,
    keys: tuple[_CapturedKey, ...],
    in_type: int,
    out_type: int,
    change: oma.MAnimCurveChange,
) -> None:
    for time, value in keys:
        if isinstance(value, om.MAngle):
            value = value.asRadians()
        elif isinstance(value, om.MDistance):
            value = value.asCentimeters()
        # addKey also updates breakdown and tangent locks on existing keys.
        curve.addKey(time, value, in_type, out_type, change)


class _KeyframeOperations(ABC):
    tangent = TangentType

    __slots__ = ("_target", "_modifier_manager")

    def __init__(
        self,
        target: _keyframe_target.Target,
        modifier_manager: ModifierManager | None,
    ) -> None:
        self._target = target
        self._modifier_manager = modifier_manager

    @abstractmethod
    def _validate_set_target(self, method: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def _key_value(
        self, value: float, time_unit: int | None = None
    ) -> _KeyValue:
        raise NotImplementedError

    @abstractmethod
    def _queue_set_keys(
        self,
        manager: ModifierManager,
        keys: tuple[_CapturedKey, ...],
        in_type: int,
        out_type: int,
    ) -> None:
        raise NotImplementedError

    def values(self) -> list[float]:
        """カーブ自身の値をdegree / cm / unitlessで取得する。"""
        return [value for _, value in self.get_keys()]

    def get_curve_data(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        include_boundaries: bool = True,
    ) -> AnimCurveData | None:
        """カーブ情報を取得する。既定で指定境界を補完し、区間の形状を保つ。

        範囲省略時は全体を取得する。対象カーブがなければNone。元のカーブは変更しない。
        境界補完では連続接線をfixedにし、weightedと時間単位を保持する。
        Falseなら範囲内の既存キーだけを取得し、接線の種類を維持する。
        """
        if type(include_boundaries) is not bool:
            raise TypeError("include_boundaries must be a bool.")
        start = (
            self._key_time(start_frame) if start_frame is not None else None
        )
        end = self._key_time(end_frame) if end_frame is not None else None
        if start is not None and end is not None and start > end:
            raise ValueError(
                "start_frame must be less than or equal to end_frame."
            )
        return _keyframe_snapshot.capture_curve(
            self._target, start, end, include_boundaries=include_boundaries
        )

    def get_weighted(self) -> bool | None:
        """対象カーブのweightedを取得する。カーブがなければNone。"""
        curve = _keyframe_snapshot.resolve_curve(self._target)
        return None if curve is None else bool(curve.isWeighted)

    def set_weighted(self, weighted: bool) -> None:
        """カーブ全体のweighted変更を予約する。対象がなければ実行時に失敗する。"""
        manager = self._require_modifier_manager()
        _keyframe_snapshot.queue_weighted(manager, self._target, weighted)

    def set_curve_data(self, data: AnimCurveData) -> None:
        """全キー・weighted・infinityの置換を予約する。保存時の時間単位を使用。

        未接続属性・登録済みlayerで対象カーブがなければ作成する。
        layerの作成や属性登録は行わない。
        """
        manager = self._require_modifier_manager()
        _keyframe_snapshot.queue_restore(
            manager, self._target, data, replace=True
        )

    def get_key_data(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        include_boundaries: bool = True,
    ) -> list[KeyData]:
        """区間のキー情報を取得する。既定で指定境界を補完し、元カーブは変更しない。

        include_boundaries=Falseなら既存キーだけを返す。カーブ無し・空カーブは[]。
        weightedと時間単位も保持する場合はget_curve_data()を使用する。
        """
        data = self.get_curve_data(
            start_frame, end_frame, include_boundaries=include_boundaries
        )
        return [] if data is None else list(data.keys)

    def set_key_data(
        self,
        keys: Iterable[KeyData],
        *,
        seconds_per_frame: float | None = None,
    ) -> None:
        """指定キーの情報を上書き予約する。既存カーブのweightedは維持する。

        frameは既定で呼び出し時のUI時間単位。保存データから使う場合は
        AnimCurveDataのseconds_per_frameを明示する。新規カーブはnonweighted。
        未接続属性・登録済みlayerでカーブがなければ作成し、仮キーは残さない。
        キーは時刻の昇順・重複なしで渡す。infinityと他のキーは置換しないが、
        autoなどの接線は前後のキー変更によりMayaが再計算する。
        nonweightedへの適用では接線の重みが失われる。
        入力を再検証して独立コピーし、予約後の編集は実行内容へ反映しない。
        """
        manager = self._require_modifier_manager()
        rate = (
            om.MTime(1.0, om.MTime.uiUnit()).asUnits(om.MTime.kSeconds)
            if seconds_per_frame is None
            else seconds_per_frame
        )
        data = AnimCurveData(
            curve_type=_keyframe_snapshot.curve_type_for_target(self._target),
            seconds_per_frame=rate,
            weighted=False,
            pre_infinity="constant",
            post_infinity="constant",
            keys=tuple(keys),
        )
        if data.keys:
            _keyframe_snapshot.queue_restore(
                manager, self._target, data, replace=False
            )

    def delete_anim_curve(self) -> None:
        """対象カーブ全体の削除を予約する。明示指定では全接続先に影響する。"""
        manager = self._require_modifier_manager()
        anim_curve_obj: om.MObject | None = None

        def disconnect_curve(modifier: om.MDGModifier) -> None:
            nonlocal anim_curve_obj
            curve = self._get_anim_curve_fn(write=True)
            if curve is None:
                return
            anim_curve_obj = curve.object()
            for source, destination in _keyframe_target.deletion_connections(
                curve
            ):
                modifier.disconnect(source, destination)

        def delete_curve(modifier: om.MDGModifier) -> None:
            if anim_curve_obj is not None:
                modifier.deleteNode(anim_curve_obj)

        # deleteNodeは予約時にも接続先を調べるため、切断の実行後に予約する。
        manager.queue_dg_modifier(disconnect_curve)
        manager.queue_dg_modifier(delete_curve)

    def _get_anim_curve_fn(
        self, *, write: bool = False
    ) -> oma.MFnAnimCurve | None:
        return _keyframe_target.resolve_curve(self._target, write=write)

    def has_anim_curve(self) -> bool:
        return self._get_anim_curve_fn() is not None

    def key_count(self) -> int:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return 0
        return fn_anim_curve.numKeys

    def frames(self) -> list[float]:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return []

        return [
            self._key_frame(fn_anim_curve, i)
            for i in range(fn_anim_curve.numKeys)
        ]

    def get_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
    ) -> list[tuple[float, float]]:
        """対象の時間入力カーブから、実在キーを時刻順に取得する。

        範囲は両端を含み、Noneの端は制限しない。frameとtime値は現在の
        UI時間単位、angle値はdegree、linear値はcentimeter。
        保留中の変更は実行せず、constraintやlayerの合成結果も評価しない。
        """
        time_unit = om.MTime.uiUnit()
        start_time = (
            self._key_time(start_frame) if start_frame is not None else None
        )
        end_time = self._key_time(end_frame) if end_frame is not None else None
        if (
            start_time is not None
            and end_time is not None
            and start_time > end_time
        ):
            raise ValueError(
                "start_frame must be less than or equal to end_frame."
            )
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None or not fn_anim_curve.numKeys:
            return []

        start_index = 0
        end_index = fn_anim_curve.numKeys
        if start_time is not None:
            start_index = fn_anim_curve.findClosest(start_time)
            if fn_anim_curve.input(start_index) < start_time:
                start_index += 1
        if end_time is not None:
            end_index = fn_anim_curve.findClosest(end_time)
            if fn_anim_curve.input(end_index) <= end_time:
                end_index += 1

        curve_type = fn_anim_curve.animCurveType
        keys: list[tuple[float, float]] = []
        for index in range(start_index, end_index):
            time = fn_anim_curve.input(index)
            value = (
                fn_anim_curve.evaluate(time)
                if curve_type == oma.MFnAnimCurve.kAnimCurveTT
                else fn_anim_curve.value(index)
            )
            if isinstance(value, om.MTime):
                value = value.asUnits(time_unit)
            elif curve_type == oma.MFnAnimCurve.kAnimCurveTA:
                value = math.degrees(value)
            keys.append((time.asUnits(time_unit), float(value)))
        return keys

    def has_key(self, frame: float) -> bool:
        return self._find_key_index(frame) is not None

    def set_key(
        self,
        value: float,
        frame: float,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """キー設定をModifierManagerへ予約する。

        Args:
            value: 角度はdegree、距離はcentimeter、time属性は予約時の
                Maya UI時間単位。それ以外はscalar値。
            frame: 予約時のMaya UI時間単位で指定する時刻。
            in_tangent_type: 入力側tangent。NoneはMayaの既定値。
            out_tangent_type: 出力側tangent。NoneはMayaの既定値。

        Notes:
            do_it_dg()で実行し、managerのundo / redo対象になる。
            属性経由の対象は、ベースまたはanim_layer()で指定したレイヤー。
            属性経由では必要に応じてcmds.setKeyframeへ委譲する。
            カーブ明示指定では、カーブ自身の値をAPIで編集する。
            キーを設定できなかった場合は実行時にRuntimeErrorを送出する。
        """
        manager = self._require_modifier_manager()

        value = float(value)
        frame = float(frame)
        if not math.isfinite(value) or not math.isfinite(frame):
            raise ValueError("Keyframe value and frame must be finite.")
        in_type = _to_tangent_type(in_tangent_type)
        out_type = _to_tangent_type(out_tangent_type)
        self._validate_set_target("set_key")

        time = om.MTime(frame, om.MTime.uiUnit())
        key_value = self._key_value(value)
        self._queue_set_keys(manager, ((time, key_value),), in_type, out_type)

    def set_keys(
        self,
        keys: Iterable[tuple[float, float]],
        *,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """複数キーの設定をまとめて予約する。単位はset_key()と同じ。

        keysは(frame, value)のペアを渡す。全入力を呼び出し時に
        捕捉・検証し、入力順で設定する。同じ時刻は後の値で上書きする。
        tangent引数は全キー共通で、keysが空なら何も予約しない。
        """
        manager = self._require_modifier_manager()
        time_unit = om.MTime.uiUnit()
        in_type = _to_tangent_type(in_tangent_type)
        out_type = _to_tangent_type(out_tangent_type)
        self._validate_set_target("set_keys")
        if isinstance(keys, (str, bytes)):
            raise TypeError(
                "keys must be an iterable of (frame, value) pairs."
            )
        captured_keys: list[_CapturedKey] = []
        for key in keys:
            if isinstance(key, (str, bytes)):
                raise TypeError("Each key must be a (frame, value) pair.")
            frame, value = key
            frame = float(frame)
            value = float(value)
            if not math.isfinite(frame) or not math.isfinite(value):
                raise ValueError("Keyframe frames and values must be finite.")
            captured_keys.append(
                (om.MTime(frame, time_unit), self._key_value(value, time_unit))
            )
        if not captured_keys:
            return
        self._queue_set_keys(manager, tuple(captured_keys), in_type, out_type)

    def set_tangent(
        self,
        frame: float,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """tangent変更を予約する。実行時にキーがなければ何もしない。"""
        manager = self._require_modifier_manager()
        time = self._key_time(frame)
        in_type = (
            _to_tangent_type(in_tangent_type)
            if in_tangent_type is not None
            else None
        )
        out_type = (
            _to_tangent_type(out_tangent_type)
            if out_tangent_type is not None
            else None
        )

        def set_key_tangent(change: oma.MAnimCurveChange) -> None:
            fn_anim_curve = self._get_anim_curve_fn(write=True)
            if fn_anim_curve is None:
                return
            index = fn_anim_curve.find(time)
            if index is None:
                return
            if in_type is not None:
                fn_anim_curve.setInTangentType(index, in_type, change)
            if out_type is not None:
                fn_anim_curve.setOutTangentType(index, out_type, change)

        manager.queue_anim_curve_change(set_key_tangent)

    def insert_key(self, frame: float, breakdown: bool = False) -> None:
        """カーブ形状を保つキー挿入を予約する。カーブがなければ実行時に失敗する。"""
        manager = self._require_modifier_manager()
        time = self._key_time(frame)

        def insert_key(change: oma.MAnimCurveChange) -> None:
            fn_anim_curve = self._get_anim_curve_fn(write=True)
            if fn_anim_curve is None:
                raise RuntimeError(
                    "The target has no channel animCurve to insert a key."
                )
            fn_anim_curve.insertKey(time, breakdown, change)

        manager.queue_anim_curve_change(insert_key)

    def delete_key(self, frame: float) -> None:
        """キー削除を予約する。キーがなければ何もせず、空のカーブは残す。"""
        manager = self._require_modifier_manager()
        time = self._key_time(frame)

        def remove_key(change: oma.MAnimCurveChange) -> None:
            fn_anim_curve = self._get_anim_curve_fn(write=True)
            if fn_anim_curve is None:
                return
            index = fn_anim_curve.find(time)
            if index is not None:
                fn_anim_curve.remove(index, change)

        manager.queue_anim_curve_change(remove_key)

    def delete_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
    ) -> None:
        """両端を含む範囲のキー削除を予約する。省略した端は制限しない。"""
        manager = self._require_modifier_manager()
        start_time = (
            self._key_time(start_frame).asUnits(om.MTime.kSeconds)
            if start_frame is not None
            else None
        )
        end_time = (
            self._key_time(end_frame).asUnits(om.MTime.kSeconds)
            if end_frame is not None
            else None
        )
        if (
            start_time is not None
            and end_time is not None
            and start_time > end_time
        ):
            raise ValueError(
                "start_frame must be less than or equal to end_frame."
            )

        def remove_keys(change: oma.MAnimCurveChange) -> None:
            fn_anim_curve = self._get_anim_curve_fn(write=True)
            if fn_anim_curve is None:
                return
            for index in reversed(range(fn_anim_curve.numKeys)):
                if self._is_frame_in_range(
                    fn_anim_curve.input(index).asUnits(om.MTime.kSeconds),
                    start_time,
                    end_time,
                ):
                    fn_anim_curve.remove(index, change)

        manager.queue_anim_curve_change(remove_keys)

    @overload
    def move_frame(
        self,
        frame: float,
        *,
        offset: float,
        to: None = None,
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def move_frame(
        self,
        frame: float,
        *,
        offset: None = None,
        to: float,
        insert_missing: bool = False,
    ) -> None: ...

    def move_frame(
        self,
        frame: float,
        *,
        offset: float | None = None,
        to: float | None = None,
        insert_missing: bool = False,
    ) -> None:
        """指定時刻のキー移動を予約する。offset / toは一方だけ。

        時刻と移動量は予約時のUI時間単位。移動先の既存キーは置換する。
        insert_missing=Trueなら、欠けた元キーを形状を保って挿入してから移す。
        カーブ・キーなしは何もしない。移動量0では挿入も行わない。
        """
        frame = float(frame)
        _keyframe_move.queue_move(
            self._require_modifier_manager(),
            self._target,
            frame,
            frame,
            offset_frames=offset,
            to_start_frame=to,
            to_end_frame=None,
            insert_missing=insert_missing,
        )

    @overload
    def move_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        offset: float,
        to_start: None = None,
        to_end: None = None,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def move_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        offset: None = None,
        to_start: float,
        to_end: None = None,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def move_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        offset: None = None,
        to_start: None = None,
        to_end: float,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    def move_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        offset: float | None = None,
        to_start: float | None = None,
        to_end: float | None = None,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None:
        """両端を含むキー範囲の移動を予約する。移動方法は1つだけ指定。

        None側は無制限、両端省略は全体。絶対移動は指定境界を基準とし、
        その側がNoneなら元範囲の最初/最後のキーを使う。移動先の対象外キーは置換。
        insert_missing=Trueは明示した境界だけを補う。空カーブや移動量0は変更しない。
        時刻は予約時のUI時間単位で捕捉し、対象とキーは初回実行時に解決する。
        補間指定時は移動前の時刻からウェイトを求め、範囲外の既存キーにも移動量を配分。
        interpolate_start < start_frame、end_frame < interpolate_endを指定する。
        補間端の静止キーを含む対象同士の衝突・順序逆転は拒否する。手動接線は維持する。
        insert_missing=Trueなら明示した補間境界も補い、自動samplingはしない。
        """
        _keyframe_move.queue_move(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            offset_frames=offset,
            to_start_frame=to_start,
            to_end_frame=to_end,
            interpolate_start=interpolate_start,
            interpolate_end=interpolate_end,
            interpolation=interpolation,
            insert_missing=insert_missing,
        )

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: float,
        duration: None = None,
        offset: float | None = None,
        to_start: None = None,
        to_end: None = None,
        pivot: float | None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: None = None,
        duration: float,
        offset: float | None = None,
        to_start: None = None,
        to_end: None = None,
        pivot: float | None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: float,
        duration: None = None,
        offset: None = None,
        to_start: float | None,
        to_end: None = None,
        pivot: None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: None = None,
        duration: float,
        offset: None = None,
        to_start: float | None,
        to_end: None = None,
        pivot: None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: float,
        duration: None = None,
        offset: None = None,
        to_start: None = None,
        to_end: float | None,
        pivot: None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: None = None,
        duration: float,
        offset: None = None,
        to_start: None = None,
        to_end: float | None,
        pivot: None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    @overload
    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: None = None,
        duration: None = None,
        offset: None = None,
        to_start: float,
        to_end: float,
        pivot: None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None: ...

    def scale_frames(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: float | None = None,
        duration: float | None = None,
        offset: float | None = None,
        to_start: float | None = None,
        to_end: float | None = None,
        pivot: float | None = None,
        mode: Literal["replace_range", "merge"] = "replace_range",
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None:
        """両端を含むキー範囲の時間拡縮を予約する。戻り値はNone。

        正の倍率・長さ・移動先の両端指定のいずれかを指定する。
        明示境界を基準とし、None側は対象キーの端を使う。接線Xも拡縮し、値は保持する。
        pivotは拡縮の基準時刻。配置先の境界とは併用不可。offsetは拡縮後に加える。
        ピボットにキーは補わない。省略時は主区間の開始を基準にする。
        既定は配置先区間の置換。mergeは同時刻だけを上書きする。元キーは残さない。
        補間区間の既存キーは元時刻で重み付けし、時刻と接線Xの拡縮を弱める。
        置換区間と拡縮基準は主区間だけで決める。対象キーの衝突・順序逆転はエラー。
        insert_missing=Trueは最大4つの明示境界を補う。恒等変換・空カーブは変更しない。
        フレーム引数は予約時のUI時間単位で捕捉し、対象キーは初回実行時に解決する。
        """
        _keyframe_scale.queue_scale(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            time_scale=scale,
            duration_frames=duration,
            pivot_frame=pivot,
            offset_frames=offset,
            to_start_frame=to_start,
            to_end_frame=to_end,
            mode=mode,
            interpolate_start=interpolate_start,
            interpolate_end=interpolate_end,
            interpolation=interpolation,
            insert_missing=insert_missing,
        )

    def set_value(
        self,
        frame: float,
        *,
        value: float,
        insert_missing: bool = False,
    ) -> None:
        """指定時刻の既存キーの値変更を予約する。手動接線は維持する。

        値は対象カーブ自身のdegree / cm / unitless / 予約時UI時間単位。
        insert_missing=Trueなら指定時刻を補う。未作成・空カーブは変更しない。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            frame,
            frame,
            operation="set",
            amount=value,
            insert_missing=insert_missing,
            single=True,
        )

    def set_values(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        value: float,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None:
        """範囲内の既存キーを同じ値へ変更する予約。手動接線は維持する。

        None側は無制限。補間指定時は外側の既存キーも元の値から指定値へ重み付けする。
        interpolate_start < start_frame、end_frame < interpolate_endを指定する。
        interpolationはキーごとの影響度であり、キー間の形状を保証しない。
        insert_missing=Trueは明示した最大4境界だけを補い、自動samplingはしない。
        値は対象カーブ自身のdegree / cm / unitless / 予約時UI時間単位。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            operation="set",
            amount=value,
            interpolate_start=interpolate_start,
            interpolate_end=interpolate_end,
            interpolation=interpolation,
            insert_missing=insert_missing,
        )

    def add_value(
        self,
        frame: float,
        *,
        offset: float,
        insert_missing: bool = False,
    ) -> None:
        """指定時刻の既存キーへ値を加算する予約。手動接線は維持する。

        単位はset_valueと同じ。offset=0では境界挿入も行わない。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            frame,
            frame,
            operation="add",
            amount=offset,
            insert_missing=insert_missing,
            single=True,
        )

    def add_values(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        offset: float,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None:
        """範囲内の既存キーへ値を加算する予約。手動接線は維持する。

        補間指定時は外側の既存キーへもoffset * 影響度を加算する。
        範囲・単位・補間・境界挿入はset_valuesと同じ。加算量0は挿入もしない。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            operation="add",
            amount=offset,
            interpolate_start=interpolate_start,
            interpolate_end=interpolate_end,
            interpolation=interpolation,
            insert_missing=insert_missing,
        )

    def scale_value(
        self,
        frame: float,
        *,
        scale: float,
        pivot: float = 0,
        insert_missing: bool = False,
    ) -> None:
        """指定時刻の既存キーをpivot基準で値方向へ拡縮する予約。

        接線Yも拡縮し、nonweighted接線は正規化する。0・負の倍率にも対応。
        pivotの単位はset_valueと同じ。倍率1では境界挿入も行わない。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            frame,
            frame,
            operation="scale",
            amount=scale,
            pivot_value=pivot,
            insert_missing=insert_missing,
            single=True,
        )

    def scale_values(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        scale: float,
        pivot: float = 0,
        interpolate_start: float | None = None,
        interpolate_end: float | None = None,
        interpolation: Literal["linear", "smoothstep"] = "smoothstep",
        insert_missing: bool = False,
    ) -> None:
        """範囲内の既存キーをpivot基準で値方向へ拡縮する予約。

        実効倍率は1 + 影響度 * (scale - 1)。接線Yも同じ倍率で拡縮し、
        nonweighted接線は正規化する。接線型・lock・breakdownは維持する。
        範囲・単位・補間・境界挿入はset_valuesと同じ。倍率1は挿入もしない。
        """
        _keyframe_value.queue_value(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            operation="scale",
            amount=scale,
            pivot_value=pivot,
            interpolate_start=interpolate_start,
            interpolate_end=interpolate_end,
            interpolation=interpolation,
            insert_missing=insert_missing,
        )

    def reduce_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        tolerance: float,
        preserve_breakdowns: bool = True,
    ) -> None:
        """元カーブとの値の誤差内でキーを削減する予約。戻り値はNone。

        範囲は両端包含、None側は無制限。範囲内の最初・最後と、既定ではbreakdownを残す。
        toleranceはdegree / cm / unitlessの非負数。キー間も比較し、判定できない候補は残す。
        残るキーの時刻・値・手動接線を保持し、auto等の再計算も誤差判定に含める。
        TA / TL / TUに対応。対象解決・編集は初回実行時、範囲の時間単位は予約時に捕捉する。
        """
        _keyframe_reduce.queue_reduce(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
            tolerance,
            preserve_breakdowns,
        )

    def _require_modifier_manager(self) -> ModifierManager:
        if self._modifier_manager is None:
            raise RuntimeError(
                "KeyframeManager mutation requires a ModifierManager."
            )
        return self._modifier_manager

    @staticmethod
    def _key_time(frame: float) -> om.MTime:
        frame = float(frame)
        if not math.isfinite(frame):
            raise ValueError("Keyframe frame must be finite.")
        return om.MTime(frame, om.MTime.uiUnit())

    def _find_key_index(
        self,
        frame: float,
        fn_anim_curve: oma.MFnAnimCurve | None = None,
    ) -> int | None:
        if fn_anim_curve is None:
            fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return None

        return fn_anim_curve.find(self._key_time(frame))

    def _key_frame(
        self,
        fn_anim_curve: oma.MFnAnimCurve,
        index: int,
    ) -> float:
        return fn_anim_curve.input(index).asUnits(om.MTime.uiUnit())

    def _is_frame_in_range(
        self,
        frame: float,
        start_frame: float | None,
        end_frame: float | None,
    ) -> bool:
        if start_frame is not None and frame < start_frame:
            return False
        if end_frame is not None and frame > end_frame:
            return False
        return True


class KeyframeManager(_KeyframeOperations):
    """属性に対するキー設定とカーブ操作。レイヤー未指定時はベースを扱う。"""

    __slots__ = ("_plug", "_plug_name", "_value_reader")

    def __init__(
        self,
        plug: om.MPlug,
        plug_name: str | None = None,
        value_reader: ValueConverter | None = None,
        *,
        modifier_manager: ModifierManager | None = None,
    ):
        super().__init__(plug, modifier_manager)
        self._plug = plug
        self._plug_name = plug_name or str(plug)
        self._value_reader = value_reader or _identity

    @property
    def plug(self) -> om.MPlug:
        return self._plug

    @property
    def plug_name(self) -> str:
        return self._plug_name

    def anim_layer(self, name: str | AnimLayerNode) -> KeyframeManager:
        """指定レイヤー用の操作入口を返す。元の入口とmanagerは共有する。

        既存名または作成待ちを含むAnimLayerを保持し、所属・接続・lockは取得時と実行時に検査する。
        キー設定はMayaの値解決、取得・詳細復元はレイヤーの生カーブを扱う。
        """
        from ..node._core import NodeOperator

        target = _keyframe_target.LayerTarget(
            self.plug, name.m_obj if isinstance(name, NodeOperator) else name
        )
        result = KeyframeManager(
            self.plug,
            self._plug_name,
            self._value_reader,
            modifier_manager=self._modifier_manager,
        )
        result._target = target
        return result

    @overload
    def find_anim_curves(
        self, *, filter_type: None = None
    ) -> tuple[AnimCurveNode, ...]: ...

    @overload
    def find_anim_curves(
        self, *, filter_type: type[CurveNode]
    ) -> tuple[CurveNode, ...]: ...

    def find_anim_curves(
        self, *, filter_type: object = None
    ) -> tuple[AnimCurveNode, ...]:
        """上流の候補をnode名順で返す。各経路の最初のカーブで探索を止める。

        Mayaの依存関係に従うため、別軸やblend weightも候補に含み得る。
        filter_typeは返却型だけを絞り込み、探索の停止位置は変えない。
        """
        return _keyframe_discovery.find_anim_curves(
            self.plug, self._modifier_manager, filter_type
        )

    def values(self) -> list[Any]:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return []

        return [
            self._value_reader(fn_anim_curve.evaluate(fn_anim_curve.input(i)))
            for i in range(fn_anim_curve.numKeys)
        ]

    def _validate_set_target(self, method: str) -> None:
        plug = self.plug
        if plug.isArray or plug.isCompound:
            raise TypeError(
                f"KeyframeManager.{method}() requires a scalar plug."
            )
        if not om.MFnAttribute(plug.attribute()).writable:
            raise RuntimeError(f"{self.plug_name} is not writable.")

    def _queue_set_keys(
        self,
        manager: ModifierManager,
        keys: tuple[_CapturedKey, ...],
        in_type: int,
        out_type: int,
    ) -> None:
        plug = self.plug
        layer_target = (
            self._target
            if isinstance(self._target, _keyframe_target.LayerTarget)
            else None
        )
        fn_anim_curve: oma.MFnAnimCurve | None = None
        api_start = 0
        in_name = _TANGENT_TYPE_NAMES.get(in_type)
        out_name = _TANGENT_TYPE_NAMES.get(out_type)

        def queue_command_key(
            modifier: om.MDGModifier, key: _CapturedKey
        ) -> None:
            time, key_value = key

            _keyframe_command.queue_key(
                modifier,
                plug,
                time,
                key_value,
                layer=layer_target,
                in_tangent_type=in_name,
                out_tangent_type=out_name,
            )

        def prepare_first_key(modifier: om.MDGModifier) -> None:
            nonlocal fn_anim_curve
            fn_anim_curve = self._api_set_curve(in_type)
            if fn_anim_curve is None:
                queue_command_key(modifier, keys[0])

        def prepare_remaining_keys(modifier: om.MDGModifier) -> None:
            nonlocal fn_anim_curve, api_start
            if fn_anim_curve is not None:
                return
            api_start = 1
            fn_anim_curve = self._api_set_curve(in_type)
            if fn_anim_curve is None:
                for key in keys[1:]:
                    queue_command_key(modifier, key)

        def set_api_keys(change: oma.MAnimCurveChange) -> None:
            if fn_anim_curve is None:
                return
            _add_keys(
                fn_anim_curve, keys[api_start:], in_type, out_type, change
            )

        manager.queue_dg_modifier(prepare_first_key)
        if len(keys) > 1:
            manager.queue_dg_modifier(prepare_remaining_keys)
        manager.queue_anim_curve_change(set_api_keys)

    def _api_set_curve(self, in_type: int) -> oma.MFnAnimCurve | None:
        """cmdsと同じ編集ができる単純な直接接続だけを、実行時に解決する。"""
        if isinstance(self._target, _keyframe_target.LayerTarget):
            return None
        plug = self.plug
        if plug.isLocked or in_type in (
            TangentType.step,
            TangentType.stepnext,
        ):
            return None
        attribute = plug.attribute()
        if attribute.hasFn(om.MFn.kNumericAttribute):
            if (
                om.MFnNumericAttribute(attribute).numericType()
                == om.MFnNumericData.kBoolean
            ):
                return None
        elif attribute.hasFn(om.MFn.kUnitAttribute):
            if (
                om.MFnUnitAttribute(attribute).unitType()
                == om.MFnUnitAttribute.kTime
            ):
                return None
        else:
            return None
        try:
            fn_anim_curve = _keyframe_target.direct_curve(plug)
        except RuntimeError:
            # Direct curve queries reject unsupported graphs; plug assignment
            # delegates their target selection and value resolution to Maya.
            return None
        if fn_anim_curve is None:
            return None
        source = fn_anim_curve.findPlug("output", False)
        if (
            fn_anim_curve.isLocked
            or fn_anim_curve.isFromReferencedFile
            or source.isLocked
            or fn_anim_curve.findPlug("keyTimeValue", False).isLocked
        ):
            return None
        node = om.MFnDependencyNode(plug.node())
        if node.isLocked or node.isFromReferencedFile:
            return None
        return fn_anim_curve

    def _key_value(
        self, value: float, time_unit: int | None = None
    ) -> _KeyValue:
        attribute = self.plug.attribute()
        if attribute.hasFn(om.MFn.kUnitAttribute):
            unit_type = om.MFnUnitAttribute(attribute).unitType()
            if unit_type == om.MFnUnitAttribute.kAngle:
                return om.MAngle(value, om.MAngle.kDegrees)
            if unit_type == om.MFnUnitAttribute.kDistance:
                return om.MDistance(value, om.MDistance.kCentimeters)
            if unit_type == om.MFnUnitAttribute.kTime:
                return om.MTime(
                    value,
                    om.MTime.uiUnit() if time_unit is None else time_unit,
                )
        return value


class CurveKeyframeManager(_KeyframeOperations):
    """明示したTA / TL / TUカーブ自身を操作する。

    時刻はカーブの入力時間、値はdegree / cm / unitless。
    接続先やlayerで合成される最終値への変換は行わない。
    対象はノード同一性で保持し、削除・未実行の作成はquery時に拒否する。
    """

    __slots__ = ()

    def __init__(
        self,
        curve: om.MObject,
        *,
        modifier_manager: ModifierManager | None = None,
    ) -> None:
        super().__init__(_keyframe_target.CurveTarget(curve), modifier_manager)

    def _validate_set_target(self, method: str) -> None:
        _keyframe_snapshot.curve_type_for_target(self._target)

    def _key_value(
        self, value: float, time_unit: int | None = None
    ) -> _KeyValue:
        if (
            _keyframe_snapshot.curve_type_for_target(self._target)
            == "animCurveTA"
        ):
            return om.MAngle(value, om.MAngle.kDegrees)
        return value

    def _queue_set_keys(
        self,
        manager: ModifierManager,
        keys: tuple[_CapturedKey, ...],
        in_type: int,
        out_type: int,
    ) -> None:
        if in_type in (TangentType.step, TangentType.stepnext):
            raise ValueError(
                "step / stepnext are supported only for outgoing tangents."
            )

        def edit(change: oma.MAnimCurveChange) -> None:
            curve = self._get_anim_curve_fn(write=True)
            if curve is None:
                raise RuntimeError("The explicit animCurve is not available.")
            _add_keys(curve, keys, in_type, out_type, change)

        manager.queue_anim_curve_change(edit)

    def get_curve_data(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        include_boundaries: bool = True,
    ) -> AnimCurveData:
        data = super().get_curve_data(
            start_frame, end_frame, include_boundaries=include_boundaries
        )
        if data is None:
            raise RuntimeError("The explicit animCurve is not available.")
        return data

    def get_weighted(self) -> bool:
        weighted = super().get_weighted()
        if weighted is None:
            raise RuntimeError("The explicit animCurve is not available.")
        return weighted
