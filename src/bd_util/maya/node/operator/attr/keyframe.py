# coding: utf-8
from __future__ import annotations

from typing import Any, Callable

# maya
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma


ValueConverter = Callable[[Any], Any]


def _identity(value: Any) -> Any:
    return value


class KeyframeManager:
    __slots__ = (
        "_plug",
        "_plug_name",
        "_value_converter",
        "_anim_curve_obj",
    )

    def __init__(
        self,
        plug: om.MPlug,
        plug_name: str | None = None,
        value_converter: ValueConverter | None = None,
    ):
        self._plug = plug
        self._plug_name = plug_name or str(plug)
        self._value_converter = value_converter or _identity
        self._anim_curve_obj: om.MObject | None = None

    @property
    def plug(self) -> om.MPlug:
        return self._plug

    @property
    def plug_name(self) -> str:
        return self._plug_name

    def set_direct(self, value: Any, frame: float):
        anim_curve_obj = self._get_or_create_anim_curve_obj()
        fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        if not fn_anim_curve.isTimeInput:
            raise RuntimeError(
                f"{fn_anim_curve.name()} is not a time-input animCurve."
            )

        fn_anim_curve.addKey(
            om.MTime(frame, om.MTime.uiUnit()),
            self._value_converter(value),
        )

    def insert_direct(self, frame: float, breakdown: bool = False) -> int:
        anim_curve_obj = self._get_anim_curve_obj()
        if anim_curve_obj is None:
            raise RuntimeError(
                f"{self.plug_name} has no upstream time-input animCurve "
                "to insert a key."
            )

        fn_anim_curve = oma.MFnAnimCurve(anim_curve_obj)
        if not fn_anim_curve.isTimeInput:
            raise RuntimeError(
                f"{fn_anim_curve.name()} is not a time-input animCurve."
            )

        return fn_anim_curve.insertKey(
            om.MTime(frame, om.MTime.uiUnit()),
            breakdown,
        )

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

    def _get_anim_curve_obj(self) -> om.MObject | None:
        anim_curve_obj = self._cached_anim_curve_obj()
        if anim_curve_obj is not None:
            return anim_curve_obj

        anim_curve_obj = self._find_upstream_anim_curve_obj()
        if anim_curve_obj is not None:
            self._anim_curve_obj = anim_curve_obj
            return anim_curve_obj
        return None

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
