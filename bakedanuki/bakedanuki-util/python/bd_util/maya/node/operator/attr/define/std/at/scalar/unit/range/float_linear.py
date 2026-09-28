# coding: utf-8

from maya.api import OpenMaya as om

from ._base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


class FloatLinearPlugOperator(
    UnitRangeBasePlugOperator["FloatLinearAttrOperator"]
):
    """`floatLinear` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> float:
        """floatLinearプラグの現在値をcentimeter単位で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMDistance().asCentimeters()

    def set(self, value: float) -> None:
        """floatLinearプラグへcentimeter値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する距離。単位はcentimeter。
        """
        distance = om.MDistance(value, om.MDistance.kCentimeters)
        self._node.modifier_manager.dg_mod.newPlugValueMDistance(
            self.plug, distance
        )

    def add_attr(self):
        """floatLinear 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnUnitAttribute.kDistance)


class FloatLinearAttrOperator(
    UnitRangeBaseAttrOperator[FloatLinearPlugOperator]
):
    """`floatLinear` 属性の定義を保持する。"""

    __slots__ = ()

    ATTR_TYPE = "floatLinear"


class FloatLinearField(
    UnitRangeBaseField[FloatLinearAttrOperator, FloatLinearPlugOperator]
):
    """`floatLinear` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatLinearAttrOperator
    PLUG_CLS = FloatLinearPlugOperator
