# coding: utf-8
"""Maya属性の入力接続と現在時刻のキーを読み取り専用で分類する。"""

from __future__ import annotations

import math
from typing import Literal, TypeAlias

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

__all__ = ["MayaPlugInputState", "inspect_plug_input_state"]

MayaPlugInputState: TypeAlias = Literal[
    "unconnected",
    "nonkeyable",
    "keyed",
    "animated",
    "key_altered",
    "driven_key",
    "expression",
    "animation_layer",
    "animation_clip",
    "muted",
    "pair_blend",
    "constraint",
    "connected",
]


def _other_connection_state(plug: om.MPlug) -> MayaPlugInputState:
    """直結元のMayaノード型から特殊な入力接続を分類する。"""
    source = plug.sourceWithConversion()
    if source.isNull:
        return "connected"
    node = source.node()
    node_fn = om.MFnDependencyNode(node)
    if node.hasFn(om.MFn.kAnimCurve):
        if not oma.MFnAnimCurve(node).isTimeInput:
            return "driven_key"
    if node_fn.typeName == "expression":
        return "expression"
    if node_fn.typeName == "timeEditorInterpolator":
        return "animation_clip"
    if node_fn.typeName.startswith("animBlendNode"):
        for connection in node_fn.getConnections():
            if any(
                om.MFnDependencyNode(other.node()).typeName == "animLayer"
                for other in connection.connectedTo(True, True)
            ):
                return "animation_layer"
    if node.hasFn(om.MFn.kPairBlend):
        return "pair_blend"
    if node.hasFn(om.MFn.kConstraint):
        return "constraint"
    return "connected"


def _is_key_altered(
    plug: om.MPlug, curve: oma.MFnAnimCurve, time: om.MTime
) -> bool:
    """現在時刻のプラグ値がカーブの評価値から手動変更されたか判定する。"""
    if time != oma.MAnimControl.currentTime():
        return False
    try:
        actual = plug.asDouble()
    except (RuntimeError, TypeError):
        return False
    return not math.isclose(
        actual, curve.evaluate(time), rel_tol=1e-6, abs_tol=1e-6
    )


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
        return ("unconnected" if plug.isKeyable else "nonkeyable"), None
    source = plug.sourceWithConversion()
    if not source.isNull:
        source_fn = om.MFnDependencyNode(source.node())
        if source_fn.typeName == "mute":
            if source_fn.findPlug("mute", False).asBool():
                return "muted", None
            muted_input = source_fn.findPlug("input", False)
            if muted_input.isDestination:
                return _inspect_plug_input(muted_input, time)
    curve = _current_time_curve(plug)
    if curve is None:
        return _other_connection_state(plug), None
    return (
        (
            "key_altered"
            if _is_key_altered(plug, curve, time)
            else "keyed" if curve.find(time) is not None else "animated"
        ),
        curve.object(),
    )


def inspect_plug_input_state(
    plug: om.MPlug, *, time: om.MTime | None = None
) -> MayaPlugInputState:
    """通常時刻カーブのキー有無と直結元の種類、非keyableを返す。

    Args:
        plug: 調べる属性のMayaプラグ。
        time: キーを照合する時刻。`None`ならMayaの現在時刻を使用する。

    Returns:
        `key_altered`は現在値とカーブ値の差、`keyed`は現在キーあり、
        `animated`は通常時間カーブのみ。特殊な接続は元ノード別に分類し、
        入力接続のない非keyable属性は`nonkeyable`とする。
    """
    at = oma.MAnimControl.currentTime() if time is None else time
    return _inspect_plug_input(plug, at)[0]
