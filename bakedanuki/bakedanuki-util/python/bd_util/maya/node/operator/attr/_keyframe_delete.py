"""カーブや境界キーを作らず、既存キーを削除する共通処理。"""

from __future__ import annotations

from collections.abc import Callable

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_tangent, _keyframe_target

TargetResolver = Callable[[], tuple[_keyframe_target.Target, ...]]


def _indices(
    curve: oma.MFnAnimCurve,
    start: float | None,
    end: float | None,
) -> tuple[int, ...]:
    return tuple(
        index
        for index in range(curve.numKeys)
        if (
            (
                start is None
                or curve.input(index).asUnits(om.MTime.kSeconds) >= start
            )
            and (
                end is None
                or curve.input(index).asUnits(om.MTime.kSeconds) <= end
            )
        )
    )


def queue_delete(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    start_frame: float | None,
    end_frame: float | None,
) -> None:
    """既存カーブ一つを対象とするキー削除を予約する。"""
    start, end = _keyframe_tangent.capture_range(start_frame, end_frame)

    def edit(change: oma.MAnimCurveChange) -> None:
        curve = _keyframe_target.resolve_curve(target, write=True)
        if curve is None:
            return
        for index in reversed(_indices(curve, start, end)):
            curve.remove(index, change)

    manager.queue_anim_curve_change(edit)


def queue_delete_batch(
    manager: ModifierManager,
    resolve_targets: TargetResolver,
    start_frame: float | None,
    end_frame: float | None,
) -> None:
    """全対象を検証した後、削除を単一操作として予約する。"""
    start, end = _keyframe_tangent.capture_range(start_frame, end_frame)

    def prepare(work: ModifierManager) -> None:
        curves: list[oma.MFnAnimCurve] = []
        handles: set[om.MObjectHandle] = set()
        for target in resolve_targets():
            curve = _keyframe_target.resolve_curve(target, write=True)
            if curve is None:
                continue
            handle = om.MObjectHandle(curve.object())
            if handle not in handles:
                handles.add(handle)
                curves.append(curve)

        plans = tuple(
            (curve, indices)
            for curve in curves
            if (indices := _indices(curve, start, end))
        )

        def edit(change: oma.MAnimCurveChange) -> None:
            for curve, indices in plans:
                for index in reversed(indices):
                    curve.remove(index, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)
