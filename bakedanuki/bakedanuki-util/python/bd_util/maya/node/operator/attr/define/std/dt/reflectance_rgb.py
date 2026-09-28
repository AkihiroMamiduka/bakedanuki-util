# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataReflectanceRGBPlugOperator(
    DataNumericBasePlugOperator["DataReflectanceRGBAttrOperator", float]
):
    __slots__ = ()

    def get(self) -> list[float]:
        """reflectanceRGB dataプラグの現在値をfloatリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    def set_direct(self, value: list[float]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Float, value)


class DataReflectanceRGBAttrOperator(
    DataNumericBaseAttrOperator[DataReflectanceRGBPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "reflectanceRGB"


class DataReflectanceRGBField(
    DataNumericBaseField[
        DataReflectanceRGBAttrOperator, DataReflectanceRGBPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataReflectanceRGBAttrOperator
    PLUG_CLS = DataReflectanceRGBPlugOperator
