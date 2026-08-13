# coding: utf-8
from __future__ import annotations

from typing import Any, Callable

# maya
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

ValueConverter = Callable[[Any], Any]
TangentTypeValue = int | str | None


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


def _identity(value: Any) -> Any:
    return value


def _to_tangent_type(tangent_type: TangentTypeValue) -> int:
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


class KeyframeManager:
    tangent = TangentType

    __slots__ = (
        "_plug",
        "_plug_name",
        "_value_converter",
        "_value_reader",
        "_anim_curve_obj",
    )

    def __init__(
        self,
        plug: om.MPlug,
        plug_name: str | None = None,
        value_converter: ValueConverter | None = None,
        value_reader: ValueConverter | None = None,
    ):
        self._plug = plug
        self._plug_name = plug_name or str(plug)
        self._value_converter = value_converter or _identity
        self._value_reader = value_reader or _identity
        self._anim_curve_obj: om.MObject | None = None

    @property
    def plug(self) -> om.MPlug:
        return self._plug

    @property
    def plug_name(self) -> str:
        return self._plug_name

    # anim_curve
    #   delete
    def delete_anim_curve(self) -> bool:
        anim_curve_obj = self._get_anim_curve_obj()
        if anim_curve_obj is None:
            return False

        self._disconnect_anim_curve_outputs(anim_curve_obj)

        modifier = om.MDGModifier()
        modifier.deleteNode(anim_curve_obj)
        modifier.doIt()
        self._anim_curve_obj = None
        return True

    #   get
    def _get_anim_curve_obj(self) -> om.MObject | None:
        anim_curve_obj = self._cached_anim_curve_obj()
        if anim_curve_obj is not None:
            return anim_curve_obj

        anim_curve_obj = self._find_upstream_anim_curve_obj()
        if anim_curve_obj is not None:
            self._anim_curve_obj = anim_curve_obj
            return anim_curve_obj
        return None

    def _get_anim_curve_fn(self) -> oma.MFnAnimCurve | None:
        anim_curve_obj = self._get_anim_curve_obj()
        if anim_curve_obj is None:
            return None

        fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        self._validate_time_input_anim_curve(fn_anim_curve)
        return fn_anim_curve

    def _get_or_create_anim_curve_fn(self) -> oma.MFnAnimCurve:
        anim_curve_obj = self._get_or_create_anim_curve_obj()
        fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        self._validate_time_input_anim_curve(fn_anim_curve)
        return fn_anim_curve

    def _get_or_create_anim_curve_obj(self) -> om.MObject:
        anim_curve_obj = self._get_anim_curve_obj()
        if anim_curve_obj is not None:
            return anim_curve_obj

        if self.plug.isDestination:
            raise RuntimeError(
                f"{self.plug_name} is already connected, "
                "but no upstream time-input animCurve was found."
            )

        anim_curve_obj = self._create_anim_curve_obj()
        self._anim_curve_obj = anim_curve_obj
        return anim_curve_obj

    def _cached_anim_curve_obj(self) -> om.MObject | None:
        anim_curve_obj = self._anim_curve_obj
        if anim_curve_obj is None or anim_curve_obj.isNull():
            return None
        try:
            fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        except RuntimeError:
            self._anim_curve_obj = None
            return None
        if not fn_anim_curve.isTimeInput:
            return None
        return anim_curve_obj

    def _validate_time_input_anim_curve(
        self,
        fn_anim_curve: oma.MFnAnimCurve,
    ):
        if not fn_anim_curve.isTimeInput:
            raise RuntimeError(
                f"{fn_anim_curve.name()} is not a time-input animCurve."
            )

    #   find
    def _find_upstream_anim_curve_obj(self) -> om.MObject | None:
        try:
            iter_graph = om.MItDependencyGraph(
                self.plug,
                om.MFn.kAnimCurve,
                om.MItDependencyGraph.kUpstream,
                om.MItDependencyGraph.kDepthFirst,
                om.MItDependencyGraph.kNodeLevel,
                om.MItDependencyGraph.kDependsOn,
            )
        except RuntimeError:
            return None

        while not iter_graph.isDone():
            anim_curve_obj = iter_graph.currentNode()
            try:
                fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
            except RuntimeError:
                iter_graph.next()
                continue
            if fn_anim_curve.isTimeInput:
                return anim_curve_obj
            iter_graph.next()
        return None

    #   create
    def _create_anim_curve_obj(self) -> om.MObject:
        if not om.MFnAttribute(self.plug.attribute()).writable:
            raise RuntimeError(f"{self.plug_name} is not writable.")

        fn_anim_curve = oma.MFnAnimCurve()
        anim_curve_type = fn_anim_curve.timedAnimCurveTypeForPlug(self.plug)
        if anim_curve_type == oma.MFnAnimCurve.kAnimCurveUnknown:
            raise RuntimeError(
                f"Cannot determine timed animCurve type for {self.plug_name}."
            )

        modifier = om.MDGModifier()
        anim_curve_obj = fn_anim_curve.create(
            self.plug,
            anim_curve_type,
            modifier,
        )
        modifier.doIt()
        return anim_curve_obj

    #   disconnect
    def _disconnect_anim_curve_outputs(self, anim_curve_obj: om.MObject):
        try:
            output_plug = om.MFnDependencyNode(anim_curve_obj).findPlug(
                "output",
                False,
            )
        except RuntimeError:
            return

        destination_plugs = output_plug.connectedTo(False, True)
        if not destination_plugs:
            return

        modifier = om.MDGModifier()
        for destination_plug in destination_plugs:
            modifier.disconnect(output_plug, destination_plug)
        modifier.doIt()

    # keyframe
    #   query
    def has_anim_curve(self) -> bool:
        return self._get_anim_curve_obj() is not None

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

    def values(self) -> list[Any]:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return []

        return [
            self._value_reader(fn_anim_curve.evaluate(fn_anim_curve.input(i)))
            for i in range(fn_anim_curve.numKeys)
        ]

    def has_key(self, frame: float) -> bool:
        return self._find_key_index(frame) is not None

    #   set
    def set_direct(
        self,
        value: Any,
        frame: float,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ):
        fn_anim_curve = self._get_or_create_anim_curve_fn()

        fn_anim_curve.addKey(
            om.MTime(frame, om.MTime.uiUnit()),
            self._value_converter(value),
            _to_tangent_type(in_tangent_type),
            _to_tangent_type(out_tangent_type),
        )

    def set_tangent(
        self,
        frame: float,
        in_tangent_type: TangentTypeValue = None,
        out_tangent_type: TangentTypeValue = None,
    ) -> bool:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return False

        index = self._find_key_index(frame, fn_anim_curve)
        if index is None:
            return False

        if in_tangent_type is not None:
            fn_anim_curve.setInTangentType(
                index,
                _to_tangent_type(in_tangent_type),
            )
        if out_tangent_type is not None:
            fn_anim_curve.setOutTangentType(
                index,
                _to_tangent_type(out_tangent_type),
            )
        return True

    #   insert
    def insert_direct(self, frame: float, breakdown: bool = False) -> int:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            raise RuntimeError(
                f"{self.plug_name} has no upstream time-input animCurve "
                "to insert a key."
            )

        return fn_anim_curve.insertKey(
            om.MTime(frame, om.MTime.uiUnit()),
            breakdown,
        )

    #   delete
    def delete_key(self, frame: float) -> bool:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return False

        index = self._find_key_index(frame, fn_anim_curve)
        if index is None:
            return False

        fn_anim_curve.remove(index)
        return True

    def delete_keys(
        self,
        start_frame: float | None = None,
        end_frame: float | None = None,
    ) -> int:
        fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return 0

        if (
            start_frame is not None
            and end_frame is not None
            and start_frame > end_frame
        ):
            raise ValueError(
                "start_frame must be less than or equal to end_frame."
            )

        indices = [
            i
            for i in range(fn_anim_curve.numKeys)
            if self._is_frame_in_range(
                self._key_frame(fn_anim_curve, i),
                start_frame,
                end_frame,
            )
        ]
        for index in reversed(indices):
            fn_anim_curve.remove(index)
        return len(indices)

    def _find_key_index(
        self,
        frame: float,
        fn_anim_curve: oma.MFnAnimCurve | None = None,
    ) -> int | None:
        if fn_anim_curve is None:
            fn_anim_curve = self._get_anim_curve_fn()
        if fn_anim_curve is None:
            return None

        return fn_anim_curve.find(om.MTime(frame, om.MTime.uiUnit()))

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
