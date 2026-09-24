"""同期した Transform の回転カーブに Euler filter を適用する。"""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_target


@dataclass(frozen=True, slots=True)
class RotationTarget:
    """一つのノードの三つの回転チャンネルと固定の回転順。"""

    name: str
    rotate_order: om.MPlug
    axes: tuple[
        _keyframe_target.Target,
        _keyframe_target.Target,
        _keyframe_target.Target,
    ]


TargetResolver = Callable[[], tuple[RotationTarget, ...]]


@dataclass(frozen=True, slots=True)
class _Plan:
    curves: tuple[oma.MFnAnimCurve, oma.MFnAnimCurve, oma.MFnAnimCurve]
    values: tuple[tuple[tuple[int, int, int], float, float, float], ...]


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


def _times(
    curve: oma.MFnAnimCurve, indices: tuple[int, ...]
) -> tuple[float, ...]:
    return tuple(
        curve.input(index).asUnits(om.MTime.kSeconds) for index in indices
    )


def _rotation_order(target: RotationTarget) -> int:
    if not target.rotate_order.sourceWithConversion().isNull:
        raise RuntimeError(
            f"Euler filter requires a static rotateOrder on {target.name}."
        )
    order = target.rotate_order.asInt()
    if order not in range(6):
        raise RuntimeError(
            f"Unsupported rotateOrder value on {target.name}: {order}."
        )
    return order


def _plan(
    target: RotationTarget,
    start: float | None,
    end: float | None,
) -> _Plan | None:
    read_curves = (
        _keyframe_target.resolve_curve(target.axes[0]),
        _keyframe_target.resolve_curve(target.axes[1]),
        _keyframe_target.resolve_curve(target.axes[2]),
    )
    indices = (
        () if read_curves[0] is None else _indices(read_curves[0], start, end),
        () if read_curves[1] is None else _indices(read_curves[1], start, end),
        () if read_curves[2] is None else _indices(read_curves[2], start, end),
    )
    if not any(indices):
        return None
    x_curve, y_curve, z_curve = read_curves
    if x_curve is None or y_curve is None or z_curve is None:
        raise RuntimeError(
            "Euler filter requires existing rotateX, rotateY and rotateZ "
            f"curves on {target.name}."
        )

    x_indices, y_indices, z_indices = indices
    times = _times(x_curve, x_indices)
    if times != _times(y_curve, y_indices) or times != _times(
        z_curve, z_indices
    ):
        raise RuntimeError(
            "Euler filter requires synchronized rotateX, rotateY and rotateZ "
            f"key times on {target.name}."
        )

    order = _rotation_order(target)
    if len(x_indices) < 2:
        return None
    if len(y_indices) < 2 or len(z_indices) < 2:
        raise RuntimeError(
            "Euler filter key synchronization changed unexpectedly."
        )

    write_curves = (
        _keyframe_target.resolve_curve(target.axes[0], write=True),
        _keyframe_target.resolve_curve(target.axes[1], write=True),
        _keyframe_target.resolve_curve(target.axes[2], write=True),
    )
    x_curve, y_curve, z_curve = write_curves
    if x_curve is None or y_curve is None or z_curve is None:
        raise RuntimeError(
            "Euler filter rotation curves disappeared during validation."
        )

    anchor = x_indices[0], y_indices[0], z_indices[0]
    previous = om.MEulerRotation(
        x_curve.value(anchor[0]),
        y_curve.value(anchor[1]),
        z_curve.value(anchor[2]),
        order,
    )
    values: list[tuple[tuple[int, int, int], float, float, float]] = []
    for x_index, y_index, z_index in zip(
        x_indices[1:], y_indices[1:], z_indices[1:]
    ):
        current = om.MEulerRotation(
            x_curve.value(x_index),
            y_curve.value(y_index),
            z_curve.value(z_index),
            order,
        )
        closest = current.closestSolution(previous)
        values.append(
            ((x_index, y_index, z_index), closest.x, closest.y, closest.z)
        )
        previous = closest
    return _Plan((x_curve, y_curve, z_curve), tuple(values))


def queue_filter(
    manager: ModifierManager,
    resolve_targets: TargetResolver,
    start: float | None,
    end: float | None,
) -> None:
    """全ノードを検証した後、Euler filter を単一操作として予約する。"""

    def prepare(work: ModifierManager) -> None:
        plans = tuple(
            plan
            for target in resolve_targets()
            if (plan := _plan(target, start, end)) is not None
        )
        if not plans:
            return

        def edit(change: oma.MAnimCurveChange) -> None:
            for plan in plans:
                x_curve, y_curve, z_curve = plan.curves
                for indices, x_value, y_value, z_value in plan.values:
                    current_values = (
                        x_curve.value(indices[0]),
                        y_curve.value(indices[1]),
                        z_curve.value(indices[2]),
                    )
                    for curve, index, current, value in zip(
                        plan.curves,
                        indices,
                        current_values,
                        (x_value, y_value, z_value),
                    ):
                        if not math.isclose(
                            current, value, rel_tol=0.0, abs_tol=1e-12
                        ):
                            curve.setValue(index, value, change)

        work.queue_anim_curve_change(edit)

    manager.queue_dg_batch(prepare)


__all__ = ("RotationTarget", "queue_filter")
