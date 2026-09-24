"""レイヤーと単位を重複解決せず、Maya によるキー作成を予約する。"""

from __future__ import annotations

from typing import TypedDict

from maya import cmds
from maya.api import OpenMaya as om

from . import _keyframe_target


class _Flags(TypedDict, total=False):
    animLayer: str
    inTangentType: str
    outTangentType: str
    noResolve: bool
    insertBlend: bool


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


def queue_key(
    modifier: om.MDGModifier,
    plug: om.MPlug,
    time: om.MTime,
    value: float | om.MAngle | om.MDistance | om.MTime,
    *,
    layer: _keyframe_target.LayerTarget | None = None,
    in_tangent_type: str | None = None,
    out_tangent_type: str | None = None,
    raw: bool = False,
) -> None:
    def set_keyframe() -> None:
        plug_name = _keyframe_target.plug_path(plug)
        if not cmds.objExists(plug_name):
            raise RuntimeError(
                "Keyframe plug is not available when the queued "
                f"command executes: {plug_name!r}"
            )
        flags: _Flags = {}
        if in_tangent_type is not None:
            flags["inTangentType"] = in_tangent_type
        if out_tangent_type is not None:
            flags["outTangentType"] = out_tangent_type
        if raw:
            flags["noResolve"] = True
            flags["insertBlend"] = False
        target_layer = layer or _keyframe_target.base_layer(plug)
        if target_layer is not None:
            if layer is not None:
                _keyframe_target.layer_curve(layer, write=True)
            flags["animLayer"] = _keyframe_target.layer_name(
                target_layer, write=True
            )
        count = cmds.setKeyframe(
            plug_name,
            time=time.asUnits(om.MTime.uiUnit()),
            value=_command_value(value),
            **flags,
        )
        if not count:
            raise RuntimeError(f"No keyframe was set on {plug_name!r}.")

    # Keep one Maya mutation per callback so modifier rollback can undo it.
    modifier.pythonCommandToExecute(set_keyframe)
