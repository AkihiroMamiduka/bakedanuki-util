# coding: utf-8
from typing import Any

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    UnitRangeBaseAttrOperator,
    UnitRangeBasePlugOperator,
    UnitRangeBaseField,
)


def _float_to_angle(value: float) -> om.MAngle:
    return om.MAngle(value, om.MAngle.kDegrees)


def _float_to_radians(value: float) -> float:
    return _float_to_angle(value).asRadians()


class DoubleAnglePlugOperator(
    UnitRangeBasePlugOperator["DoubleAngleAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> float:
        """doubleAngleプラグの現在値をdegree単位で取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asMAngle().asDegrees()

    # set
    def set(self, value: float) -> None:
        """doubleAngleプラグへdegree値をModifierManager経由で設定する。

        Args:
            value: 設定する角度。単位はdegree。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueMAngle(
            self.plug, _float_to_angle(value)
        )

    def _to_anim_curve_value(self, value: float) -> float:
        return _float_to_radians(value)

    def _from_anim_curve_value(self, value: float) -> float:
        return om.MAngle(value, om.MAngle.kRadians).asDegrees()

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnUnitAttribute.kAngle)


class DoubleAngleAttrOperator(
    UnitRangeBaseAttrOperator[DoubleAnglePlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "doubleAngle"

    def __init__(
        self,
        *args: Any,
        default_value: float | None = None,
        **kwargs: Any,
    ) -> None:
        # デフォルト値
        if default_value is None:
            default_value = 0.0
        else:
            default_value = _float_to_radians(default_value)
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class DoubleAngleField(
    UnitRangeBaseField[DoubleAngleAttrOperator, DoubleAnglePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DoubleAngleAttrOperator
    PLUG_CLS = DoubleAnglePlugOperator
