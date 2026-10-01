# coding: utf-8
"""Maya属性の入力接続と現在時刻のキーを読み取り専用で分類する。"""

from __future__ import annotations

from typing import Literal, TypeAlias

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

__all__ = ["MayaPlugInputState", "inspect_plug_input_state"]

MayaPlugInputState: TypeAlias = Literal[
    "unconnected",
    "keyed",
    "animated",
    "pair_blend",
    "constraint",
    "connected",
]


def _other_connection_state(plug: om.MPlug) -> MayaPlugInputState:
    """直結元のMayaノード型からブレンド・コンストレイントを分類する。"""
    source = plug.sourceWithConversion()
    if source.isNull:
        return "connected"
    node = source.node()
    if node.hasFn(om.MFn.kPairBlend):
        return "pair_blend"
    if node.hasFn(om.MFn.kConstraint):
        return "constraint"
    return "connected"


def _current_time_curve(plug: om.MPlug) -> oma.MFnAnimCurve | None:
    """属性へ直接接続された通常時刻入力のカーブだけを返す。"""
    source = plug.sourceWithConversion()
    if source.isNull or not source.node().hasFn(om.MFn.kAnimCurve):
        return None
    curve = oma.MFnAnimCurve(source.node())
    if (
        not curve.isTimeInput
        or curve.animCurveType
        not in (
            oma.MFnAnimCurve.kAnimCurveTA,
            oma.MFnAnimCurve.kAnimCurveTL,
            oma.MFnAnimCurve.kAnimCurveTU,
        )
        or source != curve.findPlug("output", False)
    ):
        return None

    # カーブの入力が通常時刻以外の値で駆動される場合は区別する
    input_plug = curve.findPlug("input", False)
    for connection in curve.getConnections():
        if not connection.isDestination:
            continue
        if connection.attribute().hasFn(om.MFn.kMessageAttribute):
            continue
        if connection != input_plug:
            return None
        driver = connection.sourceWithConversion()
        if driver.isNull:
            return None
        node = om.MFnDependencyNode(driver.node())
        if (
            node.typeName != "time"
            or om.MFnAttribute(driver.attribute()).name != "outTime"
            or node.findPlug("enableTimewarp", False).asBool()
        ):
            return None
    return curve


def _inspect_plug_input(
    plug: om.MPlug, time: om.MTime
) -> tuple[MayaPlugInputState, om.MObject | None]:
    """接続の種類と、現在キーの監視対象カーブを取得する。"""
    ancestor = plug
    while ancestor.isChild:
        ancestor = ancestor.parent()
        if ancestor.isDestination:
            return _other_connection_state(ancestor), None
    if not plug.isDestination:
        return "unconnected", None
    curve = _current_time_curve(plug)
    if curve is None:
        return _other_connection_state(plug), None
    return (
        "keyed" if curve.find(time) is not None else "animated",
        curve.object(),
    )


def inspect_plug_input_state(
    plug: om.MPlug, *, time: om.MTime | None = None
) -> MayaPlugInputState:
    """通常時刻カーブのキー有無と直結元の種類を返す。

    Args:
        plug: 調べる属性のMayaプラグ。
        time: キーを照合する時刻。`None`ならMayaの現在時刻を使用する。

    Returns:
        `keyed`は現在キーあり、`animated`は通常時間カーブのみ、
        `pair_blend`と`constraint`は直接または親compoundへの接続、
        `connected`はその他の入力接続、`unconnected`は入力接続なし。
    """
    at = oma.MAnimControl.currentTime() if time is None else time
    return _inspect_plug_input(plug, at)[0]
