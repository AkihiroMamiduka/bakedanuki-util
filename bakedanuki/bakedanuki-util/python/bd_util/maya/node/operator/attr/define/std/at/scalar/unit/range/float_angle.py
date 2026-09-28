# coding: utf-8

from maya.api import OpenMaya as om

from ._base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


class FloatAnglePlugOperator(
    UnitRangeBasePlugOperator["FloatAngleAttrOperator"]
):
    """`floatAngle` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> float:
        """floatAngleプラグの現在値をdegree単位で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMAngle().asDegrees()

    def set(self, value: float) -> None:
        """floatAngleプラグへdegree値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する角度。単位はdegree。
        """
        angle = om.MAngle(value, om.MAngle.kDegrees)
        self._node.modifier_manager.dg_mod.newPlugValueMAngle(self.plug, angle)

    def _from_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kRadians).asDegrees()

    def add_attr(self):
        """floatAngle 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnUnitAttribute.kAngle)


class FloatAngleAttrOperator(
    UnitRangeBaseAttrOperator[FloatAnglePlugOperator]
):
    """`floatAngle` 属性の定義を保持する。"""

    __slots__ = ()

    ATTR_TYPE = "floatAngle"


class FloatAngleField(
    UnitRangeBaseField[FloatAngleAttrOperator, FloatAnglePlugOperator]
):
    """`floatAngle` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = FloatAngleAttrOperator
    PLUG_CLS = FloatAnglePlugOperator
