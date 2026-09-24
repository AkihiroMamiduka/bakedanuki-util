# coding: utf-8
import math
from collections.abc import Callable, Iterable
from typing import Any, TypeVar, Type, cast

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ....._channel_state import ChannelBoxStateMixin
from ....._core import AttrOperator, PlugOperator, AttributeField
from .....keyframe import KeyframeManager
from ....._keyframe_discovery import curve_objects

A = TypeVar("A", bound="ScalarBaseAttrOperator[Any]")

P = TypeVar("P", bound="ScalarBasePlugOperator[Any]")


def sample_reader(plug: om.MPlug, time_unit: int) -> Callable[[], float]:
    attribute = plug.attribute()
    if attribute.hasFn(om.MFn.kUnitAttribute):
        unit_type = om.MFnUnitAttribute(attribute).unitType()
        if unit_type == om.MFnUnitAttribute.kAngle:
            return lambda: plug.asMAngle().asDegrees()
        if unit_type == om.MFnUnitAttribute.kDistance:
            return lambda: plug.asMDistance().asCentimeters()
        if unit_type == om.MFnUnitAttribute.kTime:
            return lambda: plug.asMTime().asUnits(time_unit)
        raise TypeError("Unsupported scalar unit type.")
    if attribute.hasFn(om.MFn.kNumericAttribute) or attribute.hasFn(
        om.MFn.kEnumAttribute
    ):
        return plug.asDouble
    raise TypeError("sample_values() requires a numeric or unit plug.")


def sample_plug_values(
    plug: om.MPlug, *, frames: Iterable[float]
) -> list[tuple[float, float]]:
    """Scalar plugの時刻別評価を共通化する。現在時刻と保留中編集は変更しない。"""
    time_unit = om.MTime.uiUnit()
    if isinstance(frames, (str, bytes)):
        raise TypeError("frames must be an iterable of numbers.")
    frame_items = tuple(float(frame) for frame in frames)
    if not all(math.isfinite(frame) for frame in frame_items):
        raise ValueError("Sample frames must be finite.")
    if plug.isArray or plug.isCompound:
        raise TypeError("sample_values() requires a scalar plug.")
    read_value = sample_reader(plug, time_unit)
    if frame_items:
        outputs = [
            om.MFnDependencyNode(node).name() + ".output"
            for node in curve_objects(plug, traverse_inputs=True)
        ]
        if outputs:
            # setKeyframe can leave downstream timed-context input data stale.
            cmds.dgdirty(*outputs, propagation=True)
    samples: list[tuple[float, float]] = []
    for frame in frame_items:
        context = om.MDGContext(om.MTime(frame, time_unit))
        previous = context.makeCurrent()
        try:
            value = read_value()
        finally:
            previous.makeCurrent()
        samples.append((frame, value))
    return samples


class ScalarBasePlugOperator(ChannelBoxStateMixin, PlugOperator[A]):
    __slots__ = ()

    def _channel_box_state_plugs(self) -> tuple[om.MPlug, ...]:
        self._require_indexed_channel_box_target()
        return (self.plug,)

    @property
    def keyframe(self) -> KeyframeManager:
        return self._get_keyframe_manager()

    def sample_values(
        self, *, frames: Iterable[float]
    ) -> list[tuple[float, float]]:
        """指定時刻の評価済みscalar値を(frame, value)のリストで返す。

        入力順と重複を維持する。frameとtime値は呼び出し時のUI時間単位、
        angle値はdegree、linear値はcentimeter、その他はnumeric値。
        現在時刻を変更せず、保留中の操作も実行しない。
        各時刻を独立に評価するため、履歴依存のsimulationは対象外。
        """
        return sample_plug_values(self.plug, frames=frames)


class ScalarBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class ScalarBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ScalarBaseAttrOperator)
    PLUG_CLS = cast(Type[P], ScalarBasePlugOperator)
