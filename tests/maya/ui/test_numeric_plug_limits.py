# coding: utf-8
"""表示情報を生成しない数値検証と、現在の範囲・単位への追従を確認する。"""

from __future__ import annotations

import math

import pytest
from maya import cmds

from bd_util.maya.ui import resolve_float_plug, resolve_int_plug
from bd_util.maya.ui.binding._float_plug_value import FloatPlugValue
from bd_util.maya.ui.binding._int_plug_value import IntPlugValue
from bd_util.maya.ui.binding.plugs_binding import _FloatCodec
from bd_util.ui import FloatPresentation, IntPresentation


@pytest.mark.parametrize(
    "attribute_type,expected",
    [
        ("double", 5.0),
        ("float", 5.0),
        ("doubleLinear", 0.05),
        ("doubleAngle", math.radians(5)),
    ],
)
def test_float_validation_reads_current_limits_without_display_metadata(
    new_scene: None,
    monkeypatch: pytest.MonkeyPatch,
    attribute_type: str,
    expected: float,
) -> None:
    """単位変換と後から変わる範囲を検証し、表示情報の生成を要求しない。"""
    del new_scene
    linear = cmds.currentUnit(query=True, linear=True)
    angle = cmds.currentUnit(query=True, angle=True)
    cmds.currentUnit(linear="cm", angle="deg")
    node = cmds.createNode("transform")
    # addAttrの角度範囲は表示単位によらずradianで受け取る
    limit = math.radians(10) if attribute_type == "doubleAngle" else 10
    cmds.addAttr(
        node,
        longName="limited",
        attributeType=attribute_type,
        minValue=-limit,
        maxValue=limit,
    )
    codec = _FloatCodec(resolve_float_plug(node, "limited"))

    def unexpected_presentation(_value: FloatPlugValue) -> FloatPresentation:
        """表示用データを組み立てる回帰を検出する。"""
        raise AssertionError("値の範囲検証で表示情報を生成しています")

    monkeypatch.setattr(
        FloatPlugValue, "presentation", property(unexpected_presentation)
    )
    try:
        cmds.currentUnit(linear="m", angle="rad")
        assert codec.validate(5.0) == pytest.approx(expected)
        with pytest.raises(ValueError, match="下限"):
            codec.validate(-11.0)
        with pytest.raises(ValueError, match="上限"):
            codec.validate(11.0)
        # 定義変更後も公開単位で比較し、以前の範囲を再利用しない
        cmds.currentUnit(linear="cm", angle="deg")
        maximum = math.radians(4) if attribute_type == "doubleAngle" else 4
        cmds.addAttr(node + ".limited", edit=True, maxValue=maximum)
        with pytest.raises(ValueError, match="上限"):
            codec.validate(5.0)
    finally:
        cmds.currentUnit(linear=linear, angle=angle)


@pytest.mark.parametrize(
    "attribute_type,minimum,maximum",
    [
        ("byte", 0, 255),
        ("short", -(2**15), 2**15 - 1),
        ("long", -(2**31), 2**31 - 1),
    ],
)
def test_integer_validation_keeps_type_bounds_without_display_metadata(
    new_scene: None,
    monkeypatch: pytest.MonkeyPatch,
    attribute_type: str,
    minimum: int,
    maximum: int,
) -> None:
    """表示生成を省いても型固有の両端と動的な範囲変更を検証する。"""
    del new_scene
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="limited", attributeType=attribute_type)
    codec = IntPlugValue(resolve_int_plug(node, "limited"))

    def unexpected_presentation(_value: IntPlugValue) -> IntPresentation:
        """表示用データを組み立てる回帰を検出する。"""
        raise AssertionError("値の範囲検証で表示情報を生成しています")

    monkeypatch.setattr(
        IntPlugValue, "presentation", property(unexpected_presentation)
    )
    assert codec.validate(minimum) == minimum
    assert codec.validate(maximum) == maximum
    with pytest.raises(ValueError):
        codec.validate(minimum - 1)
    with pytest.raises(ValueError):
        codec.validate(maximum + 1)
    cmds.addAttr(node + ".limited", edit=True, maxValue=2)
    with pytest.raises(ValueError, match="上限"):
        codec.validate(3)
