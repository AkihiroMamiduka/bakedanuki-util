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
    _keyframe_bake,
    _keyframe_command,
    _keyframe_delete,
    _keyframe_discovery,
    _keyframe_move,
    _keyframe_reduce,
    _keyframe_scale,
    _keyframe_snapshot,
    _keyframe_tangent,
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
TangentTypeName = _keyframe_tangent.TangentTypeName
TangentTypeValue = _keyframe_tangent.TangentTypeValue
_KeyValue = float | om.MAngle | om.MDistance | om.MTime
_CapturedKey = tuple[om.MTime, _KeyValue]

TangentType = _keyframe_tangent.TangentType


def _identity(value: Any) -> Any:
    return value


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
        # addKey は既存キーの breakdown と接線 lock も更新する。
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
        """実在キーの値を時刻順に返す。

        Returns:
            角度は degree、距離は cm、時間は現在の UI 時間単位での値。
        """
        return [value for _, value in self.get_keys()]

    def get_curve_data(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        include_boundaries: bool = True,
    ) -> AnimCurveData | None:
        """元のカーブを変更せず、指定区間のカーブ情報を取得する。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            include_boundaries: 範囲境界のキーを補完して形状を保つか。
                False では既存キーのみ取得する。

        Returns:
            weighted・時間単位を含むカーブ情報。対象がなければ None。

        Raises:
            TypeError: ``include_boundaries`` が bool ではない場合。
            ValueError: 開始時刻が終了時刻より後の場合。
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
        """対象カーブの weighted 設定を返す。カーブがなければ None。"""
        curve = _keyframe_snapshot.resolve_curve(self._target)
        return None if curve is None else bool(curve.isWeighted)

    def set_weighted(self, weighted: bool) -> None:
        """カーブ全体の weighted 設定変更を予約する。

        対象カーブがなければ実行時に失敗する。

        Args:
            weighted: weighted tangent を有効にするか。
        """
        manager = self._require_modifier_manager()
        _keyframe_snapshot.queue_weighted(manager, self._target, weighted)

    def set_curve_data(self, data: AnimCurveData) -> None:
        """全キー・weighted・infinity の置換を予約する。

        属性・レイヤー対象でカーブがなければ作成する。
        レイヤー作成や属性登録は行わない。

        Args:
            data: 復元するカーブ情報。保存時の時間単位を使用する。
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
        """元のカーブを変更せず、指定区間のキー情報を取得する。

        weighted と時間単位も必要なら ``get_curve_data()`` を使う。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            include_boundaries: 範囲境界のキーを補完するか。

        Returns:
            キー情報のリスト。属性・レイヤー対象でカーブがない場合や
            キーがない場合は空リスト。

        Raises:
            RuntimeError: カーブを直接指定した対象でカーブが消失した場合。
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
        """指定キーの上書きを予約し、既存カーブの weighted を維持する。

        属性・レイヤー対象でカーブがなければ作成する。
        既存の他のキーと infinity は維持するが、
        auto 接線は Maya が再計算する。

        Args:
            keys: 時刻の昇順で重複しない KeyData。入力は予約時にコピーする。
            seconds_per_frame: 保存データの 1 frame あたりの秒数。
                None では予約時の UI 時間単位を使う。
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
        """対象カーブ全体の削除を予約する。

        カーブを明示指定した場合は、全接続先に影響する。
        """
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
        """対象のアニメーションカーブが存在するか。"""
        return self._get_anim_curve_fn() is not None

    def key_count(self) -> int:
        """対象カーブの実在キー数を返す。カーブがなければ 0。"""
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return 0
        return fn_anim_curve.numKeys

    def frames(self) -> list[float]:
        """実在キーの時刻を現在の UI 時間単位で返す。"""
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
        """対象カーブの実在キーを時刻順に取得する。

        予約中の変更やレイヤー合成結果は評価しない。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。

        Returns:
            ``(時刻, 値)`` のリスト。時刻・時間値は UI 時間単位、
            角度は degree、距離は cm。カーブがなければ空リスト。

        Raises:
            ValueError: 開始時刻が終了時刻より後の場合。
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
        """指定時刻に実在キーがあるか。

        Args:
            frame: 現在の UI 時間単位で指定する時刻。
        """
        return self._find_key_index(frame) is not None

    def set_key(
        self,
        value: float,
        frame: float,
        *,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """キー設定を ModifierManager へ予約する。

        ``do_it_dg()`` で実行する。属性では指定レイヤーの値解決を使い、
        カーブ明示指定ではカーブ自身の値を編集する。

        Args:
            value: 角度はdegree、距離はcentimeter、time属性は予約時の
                Maya UI時間単位。それ以外はscalar値。
            frame: 予約時のMaya UI時間単位で指定する時刻。
            tangent_type: 入出力両側の共通tangent。
            in_tangent_type: 入力側tangent。NoneはMayaの既定値。
            out_tangent_type: 出力側tangent。NoneはMayaの既定値。

        Raises:
            ValueError: 値または時刻が有限数でない場合。
            RuntimeError: 実行時にキーを設定できなかった場合。
        """
        manager = self._require_modifier_manager()

        value = float(value)
        frame = float(frame)
        if not math.isfinite(value) or not math.isfinite(frame):
            raise ValueError("Keyframe value and frame must be finite.")
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type,
            in_tangent_type,
            out_tangent_type,
            default_in=oma.MFnAnimCurve.kTangentGlobal,
            default_out=oma.MFnAnimCurve.kTangentGlobal,
        )
        assert in_type is not None and out_type is not None
        self._validate_set_target("set_key")

        time = om.MTime(frame, om.MTime.uiUnit())
        key_value = self._key_value(value)
        self._queue_set_keys(manager, ((time, key_value),), in_type, out_type)

    def set_keys(
        self,
        keys: Iterable[tuple[float, float]],
        *,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """複数キーの設定をまとめて予約する。

        入力は呼び出し時に確定する。空の iterable では何も予約しない。

        Args:
            keys: ``(frame, value)`` の iterable。単位は ``set_key()`` と同じ。
                同じ時刻は後の値で上書きする。
            tangent_type: 全キーの入出力共通の接線型。
            in_tangent_type: 入力側の接線型。
            out_tangent_type: 出力側の接線型。
        """
        manager = self._require_modifier_manager()
        time_unit = om.MTime.uiUnit()
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type,
            in_tangent_type,
            out_tangent_type,
            default_in=oma.MFnAnimCurve.kTangentGlobal,
            default_out=oma.MFnAnimCurve.kTangentGlobal,
        )
        assert in_type is not None and out_type is not None
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
        *,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """指定時刻の既存キーの接線型変更を予約する。

        対象キーがなければ何もしない。

        Args:
            frame: 現在の UI 時間単位で指定する時刻。
            tangent_type: 入出力共通の接線型。
            in_tangent_type: 入力側の接線型。None は変更しない。
            out_tangent_type: 出力側の接線型。None は変更しない。
        """
        self.set_tangents(
            frame,
            frame,
            tangent_type=tangent_type,
            in_tangent_type=in_tangent_type,
            out_tangent_type=out_tangent_type,
        )

    def set_tangents(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        tangent_type: TangentTypeValue = None,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> None:
        """両端を含む範囲の既存キーの接線型変更を予約する。

        境界キーは追加せず、対象キーがなければ何もしない。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            tangent_type: 入出力共通の接線型。
            in_tangent_type: 入力側の接線型。None は変更しない。
            out_tangent_type: 出力側の接線型。None は変更しない。
        """
        manager = self._require_modifier_manager()
        start_time, end_time = _keyframe_tangent.capture_range(
            start_frame, end_frame
        )
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        if in_type is None and out_type is None:
            return

        def set_key_tangents(change: oma.MAnimCurveChange) -> None:
            fn_anim_curve = self._get_anim_curve_fn(write=True)
            if fn_anim_curve is None:
                return
            indices = [
                index
                for index in range(fn_anim_curve.numKeys)
                if self._is_frame_in_range(
                    fn_anim_curve.input(index).asUnits(om.MTime.kSeconds),
                    start_time,
                    end_time,
                )
            ]
            if not indices:
                return
            _keyframe_tangent.apply(
                fn_anim_curve, tuple(indices), in_type, out_type, change
            )

        manager.queue_anim_curve_change(set_key_tangents)

    def set_tangent_lock(
        self,
        frame: float,
        *,
        tangents_locked: bool | None = None,
        weights_locked: bool | None = None,
    ) -> None:
        """指定時刻の既存キーの接線 lock 変更を予約する。

        Args:
            frame: 現在の UI 時間単位で指定する時刻。
            tangents_locked: 接線 lock の状態。None は変更しない。
            weights_locked: weight lock の状態。None は変更しない。
        """
        self.set_tangent_locks(
            frame,
            frame,
            tangents_locked=tangents_locked,
            weights_locked=weights_locked,
        )

    def set_tangent_locks(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        tangents_locked: bool | None = None,
        weights_locked: bool | None = None,
    ) -> None:
        """両端を含む範囲の既存キーの接線 lock 変更を予約する。

        境界キーは追加せず、weighted 設定と接線形状は維持する。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            tangents_locked: 接線 lock の状態。None は変更しない。
            weights_locked: weight lock の状態。None は変更しない。
        """
        manager = self._require_modifier_manager()
        start, end = _keyframe_tangent.capture_range(start_frame, end_frame)
        tangent_lock, weight_lock = _keyframe_tangent.capture_locks(
            tangents_locked, weights_locked
        )
        if tangent_lock is None and weight_lock is None:
            return

        _keyframe_tangent.queue_locks(
            manager,
            lambda: (self._target,),
            start,
            end,
            tangent_lock,
            weight_lock,
        )

    def insert_key(self, frame: float, breakdown: bool = False) -> None:
        """カーブ形状を保つキー挿入を予約する。

        カーブがなければ実行時に失敗する。

        Args:
            frame: 現在の UI 時間単位で指定する時刻。
            breakdown: 挿入キーを breakdown にするか。
        """
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
        """指定時刻のキー削除を予約する。

        キーがなければ何もしない。空のカーブは残す。

        Args:
            frame: 現在の UI 時間単位で指定する時刻。
        """
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
        """両端を含む範囲のキー削除を予約する。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
        """
        _keyframe_delete.queue_delete(
            self._require_modifier_manager(),
            self._target,
            start_frame,
            end_frame,
        )

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
        """指定時刻のキー移動を予約する。

        移動先の既存キーは置換する。移動量 0 や空カーブでは変更しない。

        Args:
            frame: 元キーの時刻。予約時の UI 時間単位。
            offset: 相対移動量。to と同時には指定できない。
            to: 移動先の時刻。offset と同時には指定できない。
            insert_missing: 元キーがなければ形状を保って挿入するか。
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
        """両端を含むキー範囲の移動を予約する。

        時刻は予約時の UI 時間単位。移動先の対象外キーは置換する。
        手動接線は維持し、キーの順序逆転は拒否する。

        Args:
            start_frame: 元範囲の開始。None は制限しない。
            end_frame: 元範囲の終了。None は制限しない。
            offset: 相対移動量。to_start / to_end と同時指定不可。
            to_start: 開始境界の移動先。未指定境界には最初のキーを使う。
            to_end: 終了境界の移動先。未指定境界には最後のキーを使う。
            interpolate_start: 移動量を徐々に増やす外側の開始時刻。
            interpolate_end: 移動量を徐々に減らす外側の終了時刻。
            interpolation: 影響度の補間方法。
            insert_missing: 明示した境界キーを補うか。
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
        """両端を含むキー範囲を時間方向に拡縮する。

        時刻は予約時の UI 時間単位。値は維持し、接線 X を拡縮する。
        キーの衝突・順序逆転は拒否する。

        Args:
            start_frame: 元範囲の開始。None では最初の対象キーを使う。
            end_frame: 元範囲の終了。None では最後の対象キーを使う。
            scale: 正の時間倍率。duration との併用は不可。
            duration: 拡縮後の長さ。scale との併用は不可。
            offset: 拡縮後に加える時刻の移動量。
            to_start: 配置先の開始時刻。pivot との併用は不可。
            to_end: 配置先の終了時刻。pivot との併用は不可。
            pivot: 拡縮の基準時刻。省略時は元範囲の開始。
            mode: ``replace_range`` は配置先区間を置換し、``merge`` は
                同時刻のキーだけを上書きする。
            interpolate_start: 影響度を徐々に増やす外側の開始時刻。
            interpolate_end: 影響度を徐々に減らす外側の終了時刻。
            interpolation: 影響度の補間方法。
            insert_missing: 明示した境界キーを補うか。
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
        """指定時刻のキーの値変更を予約する。

        手動接線は維持する。空カーブでは変更しない。

        Args:
            frame: 変更する時刻。予約時の UI 時間単位。
            value: 新しい値。角度は degree、距離は cm、時間は UI 時間単位。
            insert_missing: 対象時刻のキーがなければ補うか。
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
        """範囲内の既存キーを指定値へ変更する予約を行う。

        手動接線は維持する。補間はキーごとの影響度に適用する。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            value: 新しい値。角度は degree、距離は cm、時間は UI 時間単位。
            interpolate_start: 影響度を徐々に増やす外側の開始時刻。
            interpolate_end: 影響度を徐々に減らす外側の終了時刻。
            interpolation: 影響度の補間方法。
            insert_missing: 明示した境界キーを補うか。
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
        """指定時刻の既存キーに値を加算する。

        手動接線は維持する。offset が 0 の場合は挿入もしない。

        Args:
            frame: 変更する時刻。予約時の UI 時間単位。
            offset: 加算量。単位は ``set_value()`` と同じ。
            insert_missing: 対象時刻のキーがなければ補うか。
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
        """範囲内の既存キーに値を加算する。

        手動接線は維持する。offset が 0 の場合は挿入もしない。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            offset: 加算量。単位は ``set_value()`` と同じ。
            interpolate_start: 影響度を徐々に増やす外側の開始時刻。
            interpolate_end: 影響度を徐々に減らす外側の終了時刻。
            interpolation: 影響度の補間方法。
            insert_missing: 明示した境界キーを補うか。
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
        """指定時刻のキーを pivot 基準で値方向に拡縮する。

        scale が 1 の場合は挿入もしない。

        Args:
            frame: 変更する時刻。予約時の UI 時間単位。
            scale: 値と接線 Y に適用する倍率。0 や負数にも対応。
            pivot: 値の拡縮基準。単位は ``set_value()`` と同じ。
            insert_missing: 対象時刻のキーがなければ補うか。
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
        """範囲内の既存キーを pivot 基準で値方向に拡縮する。

        接線型・lock・breakdown は維持する。scale が 1 なら変更しない。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            scale: 値と接線 Y に適用する倍率。
            pivot: 値の拡縮基準。単位は ``set_value()`` と同じ。
            interpolate_start: 影響度を徐々に増やす外側の開始時刻。
            interpolate_end: 影響度を徐々に減らす外側の終了時刻。
            interpolation: 影響度の補間方法。
            insert_missing: 明示した境界キーを補うか。
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
        """元カーブとの値の誤差内でキーを削減する。

        範囲の最初と最後のキーは残す。対象解決と編集は初回実行時。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            tolerance: 許容誤差。角度は degree、距離は cm の非負数。
            preserve_breakdowns: breakdown キーを残すか。
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
        """属性と操作を予約する先を設定する。

        Args:
            plug: 操作対象の scalar MPlug。
            plug_name: 表示・コマンド用の属性パス。省略時は plug から作る。
            value_reader: カーブ値を属性値へ変換する関数。
            modifier_manager: 編集を予約する先。None では読み取り専用。
        """
        super().__init__(plug, modifier_manager)
        self._plug = plug
        self._plug_name = plug_name or str(plug)
        self._value_reader = value_reader or _identity

    @property
    def plug(self) -> om.MPlug:
        """操作対象の MPlug。"""
        return self._plug

    @property
    def plug_name(self) -> str:
        """操作対象の ``node.attr`` 形式の名前。"""
        return self._plug_name

    def anim_layer(self, name: str | AnimLayerNode) -> KeyframeManager:
        """指定レイヤーに対する操作入口を返す。

        レイヤーの所属・接続・lock は取得時と実行時に検査する。

        Args:
            name: レイヤー名または作成待ちを含む AnimLayer ノード。

        Returns:
            同じ ModifierManager を使うレイヤー用 KeyframeManager。
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
        """上流にあるアニメーションカーブをノード名順で返す。

        別軸や blend weight のカーブも候補に含まれる。

        Args:
            filter_type: 返すカーブのノードクラス。探索範囲は変えない。

        Returns:
            各接続経路で最初に見つかったカーブのタプル。
        """
        return _keyframe_discovery.find_anim_curves(
            self.plug, self._modifier_manager, filter_type
        )

    def bake(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
        *,
        sample_by: float = 1.0,
        tangent_type: TangentTypeValue = "auto",
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
        discrete_tangent_type: TangentTypeValue = None,
    ) -> None:
        """評価済み入力を等間隔に採取してキーへ置き換える。

        範囲の両端を採取する。上流ノードと他のレイヤーは維持する。
        各時刻を独立に評価するため履歴依存の simulation は対象外。

        Args:
            start_frame: 開始時刻。None は呼び出し時の再生範囲の開始。
            end_frame: 終了時刻。None は呼び出し時の再生範囲の終了。
            sample_by: 採取間隔。UI 時間単位で指定する。
            tangent_type: 入出力共通の接線型。
            in_tangent_type: 入力側の接線型。
            out_tangent_type: 出力側の接線型。
            discrete_tangent_type: 離散値用の接線型。
        """
        manager = self._require_modifier_manager()
        self._validate_set_target("bake")
        _keyframe_snapshot.curve_type_for_target(self._target)
        frames, rate = _keyframe_bake.capture_grid(
            start_frame, end_frame, sample_by
        )
        in_type, out_type = _keyframe_tangent.resolve_tangent_types(
            tangent_type, in_tangent_type, out_tangent_type
        )
        discrete_type = (
            _keyframe_tangent.to_tangent_type(discrete_tangent_type)
            if discrete_tangent_type is not None
            else None
        )
        _keyframe_bake.queue_bake(
            manager,
            self._target,
            self.plug,
            frames,
            rate,
            in_type=in_type,
            out_type=out_type,
            discrete_type=discrete_type,
        )

    def values(self) -> list[Any]:
        """対象カーブの実在キーの評価値を時刻順に返す。"""
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
        in_name = _keyframe_tangent.command_tangent_name(in_type)
        out_name = _keyframe_tangent.command_tangent_name(out_type)

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
            # 直接カーブを取得できない構成では、対象と値の解決を Maya に委ねる。
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
    """明示した TA / TL / TU カーブ自身を操作する。

    時刻はカーブ入力時間、値は degree / cm / unitless。
    接続先やレイヤーで合成される最終値は扱わない。
    """

    __slots__ = ()

    def __init__(
        self,
        curve: om.MObject,
        *,
        modifier_manager: ModifierManager | None = None,
    ) -> None:
        """明示したアニメーションカーブの操作入口を作る。

        Args:
            curve: TA / TL / TU カーブの MObject。
            modifier_manager: 編集を予約する先。None では読み取り専用。
        """
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
        """明示したカーブから指定範囲の情報を取得する。

        Args:
            start_frame: 範囲の開始。None は制限しない。
            end_frame: 範囲の終了。None は制限しない。
            include_boundaries: 境界キーを補完して形状を保つか。

        Returns:
            カーブのキー・接線・時間単位を含むデータ。

        Raises:
            RuntimeError: 指定カーブが利用できない場合。
        """
        data = super().get_curve_data(
            start_frame, end_frame, include_boundaries=include_boundaries
        )
        if data is None:
            raise RuntimeError("The explicit animCurve is not available.")
        return data

    def get_weighted(self) -> bool:
        """明示したカーブの weighted 設定を返す。

        Raises:
            RuntimeError: 指定カーブが利用できない場合。
        """
        weighted = super().get_weighted()
        if weighted is None:
            raise RuntimeError("The explicit animCurve is not available.")
        return weighted
