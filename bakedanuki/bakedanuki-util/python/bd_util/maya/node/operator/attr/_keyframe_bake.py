"""Evaluate a channel and replace its selected raw input with sampled keys."""

from __future__ import annotations

import math
from dataclasses import dataclass

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager
from . import _keyframe_snapshot, _keyframe_target
from .keyframe_data import AnimCurveData, KeyData

_MAX_SAMPLES = 10_000_001


@dataclass(frozen=True, slots=True)
class _IncomingConnection:
    source: om.MPlug
    destination: om.MPlug
    child_path: tuple[int, ...]


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
    modifier: om.MDGModifier, connection: _IncomingConnection
) -> None:
    source = connection.source
    destination = connection.destination
    _check_connection(source, destination)
    modifier.disconnect(source, destination)
    for target_index in connection.child_path:
        if not source.isCompound or not destination.isCompound:
            raise RuntimeError(
                "Cannot preserve sibling inputs while splitting a parent connection."
            )
        if source.numChildren() != destination.numChildren():
            raise RuntimeError(
                "Cannot split a parent connection with different child layouts."
            )
        for index in range(destination.numChildren()):
            source_child = source.child(index)
            destination_child = destination.child(index)
            _check_connection(source_child, destination_child)
            if index != target_index:
                modifier.connect(source_child, destination_child)
        source = source.child(target_index)
        destination = destination.child(target_index)


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


def queue_bake(
    manager: ModifierManager,
    target: _keyframe_target.Target,
    plug: om.MPlug,
    frames: tuple[float, ...],
    seconds_per_frame: float,
) -> None:
    """Queue deferred sampling, connection replacement and value verification."""

    def bake(work: ModifierManager) -> None:
        raw = _keyframe_target.bake_input(target)
        samples = _sample(raw, frames, seconds_per_frame)
        data = _curve_data(target, plug, samples, seconds_per_frame)
        connection = _incoming_connection(raw)
        reusable = _direct_reusable_curve(target, raw, connection)
        if connection is not None and reusable is None:
            work.queue_dg_modifier(
                lambda modifier: _queue_detach(modifier, connection)
            )
        _keyframe_snapshot.queue_restore(work, target, data, replace=True)

        def verify(modifier: om.MDGModifier) -> None:
            del modifier
            actual = _sample(
                _keyframe_target.bake_input(target),
                frames,
                seconds_per_frame,
            )
            for (frame, expected), (_, value) in zip(samples, actual):
                slack = max(1e-10, 32 * math.ulp(expected))
                if not math.isfinite(value) or abs(value - expected) > slack:
                    raise RuntimeError(
                        f"Cannot preserve baked value at {plug.name()}, frame {frame}: "
                        f"expected {expected}, got {value}."
                    )

        work.queue_dg_modifier(verify)

    manager.queue_dg_batch(bake)
