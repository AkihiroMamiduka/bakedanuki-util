"""Evaluate a channel and replace its selected raw input with sampled keys."""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_discovery, _keyframe_snapshot, _keyframe_target
from .keyframe_data import AnimCurveData, KeyData

_MAX_SAMPLES = 10_000_001


@dataclass(frozen=True, slots=True)
class _IncomingConnection:
    source: om.MPlug
    destination: om.MPlug
    child_path: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class _BakePlan:
    target: _keyframe_target.Target
    plug: om.MPlug
    samples: tuple[tuple[float, float], ...]
    data: AnimCurveData
    connection: _IncomingConnection | None
    reusable: oma.MFnAnimCurve | None


TargetResolver = Callable[
    [], tuple[tuple[_keyframe_target.Target, om.MPlug], ...]
]


def capture_grid(
    start_frame: object | None,
    end_frame: object | None,
    sample_by: object,
) -> tuple[tuple[float, ...], float]:
    """Validate call-time frame arguments and preserve their physical unit."""

    def number(value: object, name: str) -> float:
        if isinstance(value, bool) or not isinstance(value, (float, int)):
            raise TypeError(f"{name} must be a number.")
        result = float(value)
        if not math.isfinite(result):
            raise ValueError(f"{name} must be finite.")
        return result

    start = number(
        (
            cmds.playbackOptions(query=True, minTime=True)
            if start_frame is None
            else start_frame
        ),
        "start_frame",
    )
    end = number(
        (
            cmds.playbackOptions(query=True, maxTime=True)
            if end_frame is None
            else end_frame
        ),
        "end_frame",
    )
    step = number(sample_by, "sample_by")
    if start > end:
        raise ValueError(
            "start_frame must be less than or equal to end_frame."
        )
    if step <= 0:
        raise ValueError("sample_by must be positive.")
    frames = frame_grid(start, end, step)
    seconds_per_frame = om.MTime(1.0, om.MTime.uiUnit()).asUnits(
        om.MTime.kSeconds
    )
    return frames, seconds_per_frame


def frame_grid(start: float, end: float, step: float) -> tuple[float, ...]:
    span = (end - start) / step
    if not math.isfinite(span) or span > _MAX_SAMPLES - 1:
        raise ValueError(
            f"The bake sample grid exceeds {_MAX_SAMPLES:,} points."
        )
    count = math.floor(span)
    frames = [start + index * step for index in range(count + 1)]
    if frames[-1] < end:
        frames.append(end)
    else:
        frames[-1] = end
    return tuple(frames)


def _child_index(plug: om.MPlug) -> int:
    parent = plug.parent()
    for index in range(parent.numChildren()):
        if parent.child(index) == plug:
            return index
    raise RuntimeError(f"Cannot identify the compound child {plug.name()}.")


def _incoming_connection(plug: om.MPlug) -> _IncomingConnection | None:
    destination = plug
    reverse_path: list[int] = []
    while True:
        sources = destination.connectedTo(True, False)
        if sources:
            if len(sources) != 1:
                raise RuntimeError(
                    f"Expected one input connection on {destination.name()}."
                )
            return _IncomingConnection(
                sources[0], destination, tuple(reversed(reverse_path))
            )
        if not destination.isChild:
            return None
        reverse_path.append(_child_index(destination))
        destination = destination.parent()


def _check_connection(source: om.MPlug, destination: om.MPlug) -> None:
    for plug in (source, destination):
        _keyframe_target.check_editable_node(om.MFnDependencyNode(plug.node()))
        _keyframe_target.check_editable_plug(plug)


def _queue_detach(
    modifier: om.MDGModifier,
    connection: _IncomingConnection,
    child_paths: tuple[tuple[int, ...], ...],
) -> None:
    source = connection.source
    destination = connection.destination
    _check_connection(source, destination)
    modifier.disconnect(source, destination)

    def reconnect(
        source_plug: om.MPlug,
        destination_plug: om.MPlug,
        path: tuple[int, ...],
    ) -> None:
        if path in child_paths:
            return
        if not any(
            target[: len(path)] == path and len(target) > len(path)
            for target in child_paths
        ):
            _check_connection(source_plug, destination_plug)
            modifier.connect(source_plug, destination_plug)
            return
        if not source_plug.isCompound or not destination_plug.isCompound:
            raise RuntimeError(
                "Cannot preserve sibling inputs while splitting a parent connection."
            )
        if source_plug.numChildren() != destination_plug.numChildren():
            raise RuntimeError(
                "Cannot split a parent connection with different child layouts."
            )
        for index in range(destination_plug.numChildren()):
            reconnect(
                source_plug.child(index),
                destination_plug.child(index),
                path + (index,),
            )

    reconnect(source, destination, ())


def _direct_reusable_curve(
    target: _keyframe_target.Target,
    raw: om.MPlug,
    connection: _IncomingConnection | None,
) -> oma.MFnAnimCurve | None:
    if connection is None or connection.child_path:
        return None
    source = connection.source
    if (
        not source.node().hasFn(om.MFn.kAnimCurve)
        or len(source.connectedTo(False, True)) != 1
    ):
        return None
    curve = _keyframe_target.resolve_curve(target, write=True)
    if curve is None or curve.object() != source.node():
        return None
    if (
        source != curve.findPlug("output", False)
        or connection.destination != raw
    ):
        return None
    return curve


def _discrete(plug: om.MPlug) -> bool:
    attribute = plug.attribute()
    return attribute.hasFn(om.MFn.kEnumAttribute) or (
        attribute.hasFn(om.MFn.kNumericAttribute)
        and om.MFnNumericAttribute(attribute).numericType()
        in (
            om.MFnNumericData.kBoolean,
            om.MFnNumericData.kByte,
            om.MFnNumericData.kChar,
            om.MFnNumericData.kShort,
            om.MFnNumericData.kInt,
        )
    )


def _curve_data(
    target: _keyframe_target.Target,
    plug: om.MPlug,
    samples: tuple[tuple[float, float], ...],
    seconds_per_frame: float,
) -> AnimCurveData:
    out_tangent = "step" if _discrete(plug) else "linear"
    return AnimCurveData(
        curve_type=_keyframe_snapshot.curve_type_for_target(target),
        seconds_per_frame=seconds_per_frame,
        weighted=False,
        pre_infinity="constant",
        post_infinity="constant",
        keys=tuple(
            KeyData(
                frame=frame,
                value=value,
                in_tangent_type="linear",
                out_tangent_type=out_tangent,
                in_tangent_xy=(1.0, 0.0),
                out_tangent_xy=(1.0, 0.0),
                tangents_locked=False,
                weights_locked=False,
                breakdown=False,
            )
            for frame, value in samples
        ),
    )


def _sample(
    plug: om.MPlug,
    frames: tuple[float, ...],
    seconds_per_frame: float,
) -> tuple[tuple[float, float], ...]:
    from .define.std.at.scalar._base import sample_plug_values

    execution_unit = om.MTime.uiUnit()
    execution_frames = tuple(
        om.MTime(frame * seconds_per_frame, om.MTime.kSeconds).asUnits(
            execution_unit
        )
        for frame in frames
    )
    sampled = sample_plug_values(plug, frames=execution_frames)
    return tuple((frame, value) for frame, (_, value) in zip(frames, sampled))


def _connection_groups(
    plans: tuple[_BakePlan, ...],
) -> tuple[tuple[_IncomingConnection, tuple[tuple[int, ...], ...]], ...]:
    groups: dict[
        tuple[str, str], tuple[_IncomingConnection, list[tuple[int, ...]]]
    ] = {}
    for plan in plans:
        connection = plan.connection
        if connection is None or plan.reusable is not None:
            continue
        key = (
            _keyframe_target.plug_path(connection.source),
            _keyframe_target.plug_path(connection.destination),
        )
        group = groups.get(key)
        if group is None:
            groups[key] = (connection, [connection.child_path])
        elif connection.child_path not in group[1]:
            group[1].append(connection.child_path)
    return tuple(
        (connection, tuple(paths)) for connection, paths in groups.values()
    )


def queue_bakes(
    manager: ModifierManager,
    resolve_targets: TargetResolver,
    frames: tuple[float, ...],
    seconds_per_frame: float,
    *,
    include_static: bool,
    empty_error: str,
) -> None:
    """Queue one atomic, deferred bake for one or more channel targets."""

    def bake(work: ModifierManager) -> None:
        prepared: list[tuple[_keyframe_target.Target, om.MPlug, om.MPlug]] = []
        for target, plug in resolve_targets():
            raw = _keyframe_target.bake_input(target)
            if include_static or _keyframe_discovery.has_animation(raw):
                prepared.append((target, plug, raw))
        if not prepared:
            raise ValueError(empty_error)

        sampled = tuple(
            (target, plug, raw, _sample(raw, frames, seconds_per_frame))
            for target, plug, raw in prepared
        )
        plans = tuple(
            _BakePlan(
                target=target,
                plug=plug,
                samples=samples,
                data=_curve_data(target, plug, samples, seconds_per_frame),
                connection=(connection := _incoming_connection(raw)),
                reusable=_direct_reusable_curve(target, raw, connection),
            )
            for target, plug, raw, samples in sampled
        )
        groups = _connection_groups(plans)
        if groups:

            def detach(modifier: om.MDGModifier) -> None:
                for connection, child_paths in groups:
                    _queue_detach(modifier, connection, child_paths)

            work.queue_dg_modifier(detach)
        for plan in plans:
            _keyframe_snapshot.queue_restore(
                work, plan.target, plan.data, replace=True
            )

        def verify(modifier: om.MDGModifier) -> None:
            del modifier
            for plan in plans:
                actual = _sample(
                    _keyframe_target.bake_input(plan.target),
                    frames,
                    seconds_per_frame,
                )
                for (frame, expected), (_, value) in zip(plan.samples, actual):
                    slack = max(1e-10, 32 * math.ulp(expected))
                    if (
                        not math.isfinite(value)
                        or abs(value - expected) > slack
                    ):
                        raise RuntimeError(
                            "Cannot preserve baked value at "
                            f"{plan.plug.name()}, frame {frame}: "
                            f"expected {expected}, got {value}."
                        )

        work.queue_dg_modifier(verify)

    manager.queue_dg_batch(bake)


def queue_bake(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    plug: om.MPlug,
    frames: tuple[float, ...],
    seconds_per_frame: float,
) -> None:
    """Queue deferred sampling, connection replacement and value verification."""

    queue_bakes(
        manager,
        lambda: ((target, plug),),
        frames,
        seconds_per_frame,
        include_static=True,
        empty_error="The bake target is not available.",
    )
