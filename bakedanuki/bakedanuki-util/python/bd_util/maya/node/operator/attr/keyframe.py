# coding: utf-8
from __future__ import annotations

import math
from typing import Any, Callable, TypedDict

# maya
from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ...modifier import ModifierManager

ValueConverter = Callable[[Any], Any]
TangentTypeValue = int | str | None


class _TangentFlags(TypedDict, total=False):
    inTangentType: str
    outTangentType: str


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
        "_value_reader",
        "_modifier_manager",
    )

    def __init__(
        self,
        plug: om.MPlug,
        plug_name: str | None = None,
        value_reader: ValueConverter | None = None,
        *,
        modifier_manager: ModifierManager | None = None,
    ):
        self._plug = plug
        self._plug_name = plug_name or str(plug)
        self._value_reader = value_reader or _identity
        self._modifier_manager = modifier_manager

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
        return True

    #   get
    def _get_anim_curve_obj(self) -> om.MObject | None:
        return self._find_upstream_anim_curve_obj()

    def _get_anim_curve_fn(self) -> oma.MFnAnimCurve | None:
        anim_curve_obj = self._get_anim_curve_obj()
        if anim_curve_obj is None:
            return None

        fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        self._validate_time_input_anim_curve(fn_anim_curve)
        return fn_anim_curve

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
    def set(
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
            対象カーブやanimation layer、blendはcmds.setKeyframeに従う。
            キーを設定できなかった場合は実行時にRuntimeErrorを送出する。
        """
        manager = self._modifier_manager
        if manager is None:
            raise RuntimeError(
                "KeyframeManager.set() requires a ModifierManager."
            )

        value = float(value)
        frame = float(frame)
        if not math.isfinite(value) or not math.isfinite(frame):
            raise ValueError("Keyframe value and frame must be finite.")
        in_type = _TANGENT_TYPE_NAMES.get(_to_tangent_type(in_tangent_type))
        out_type = _TANGENT_TYPE_NAMES.get(_to_tangent_type(out_tangent_type))
        plug = self.plug
        if plug.isArray or plug.isCompound:
            raise TypeError("KeyframeManager.set() requires a scalar plug.")
        if not om.MFnAttribute(plug.attribute()).writable:
            raise RuntimeError(f"{self.plug_name} is not writable.")

        time = om.MTime(frame, om.MTime.uiUnit())
        key_value = self._key_value(value)

        def set_keyframe() -> None:
            plug_name = plug.name()
            if not cmds.objExists(plug_name):
                raise RuntimeError(
                    "Keyframe plug is not available when the queued "
                    f"command executes: {plug_name!r}"
                )
            tangent_flags: _TangentFlags = {}
            if in_type is not None:
                tangent_flags["inTangentType"] = in_type
            if out_type is not None:
                tangent_flags["outTangentType"] = out_type
            count = cmds.setKeyframe(
                plug_name,
                time=time.asUnits(om.MTime.uiUnit()),
                value=self._command_value(key_value),
                **tangent_flags,
            )
            if not count:
                raise RuntimeError(f"No keyframe was set on {plug_name!r}.")

        manager.dg_mod.pythonCommandToExecute(set_keyframe)

    def _key_value(
        self, value: float
    ) -> float | om.MAngle | om.MDistance | om.MTime:
        attribute = self.plug.attribute()
        if attribute.hasFn(om.MFn.kUnitAttribute):
            unit_type = om.MFnUnitAttribute(attribute).unitType()
            if unit_type == om.MFnUnitAttribute.kAngle:
                return om.MAngle(value, om.MAngle.kDegrees)
            if unit_type == om.MFnUnitAttribute.kDistance:
                return om.MDistance(value, om.MDistance.kCentimeters)
            if unit_type == om.MFnUnitAttribute.kTime:
                return om.MTime(value, om.MTime.uiUnit())
        return value

    @staticmethod
    def _command_value(
        value: float | om.MAngle | om.MDistance | om.MTime,
    ) -> float:
        if isinstance(value, om.MAngle):
            return value.asUnits(om.MAngle.uiUnit())
        if isinstance(value, om.MDistance):
            return value.asUnits(om.MDistance.uiUnit())
        if isinstance(value, om.MTime):
            return value.asUnits(om.MTime.uiUnit())
        return value

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
