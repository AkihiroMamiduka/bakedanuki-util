# coding: utf-8

from maya.api import OpenMaya as om

from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataSpectrumRGBPlugOperator(
    DataNumericBasePlugOperator["DataSpectrumRGBAttrOperator", float]
):
    __slots__ = ()

    def get(self) -> list[float]:
        """spectrumRGB dataプラグの現在値をfloatリストで取得する。"""
        x, y, z = self._get_data()
        return [x, y, z]

    def set_direct(self, value: list[float]) -> None:
        """`MPlug` に値を直接設定する。

        `ModifierManager` の履歴には入らない。

        Args:
            value: x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Float, value)


class DataSpectrumRGBAttrOperator(
    DataNumericBaseAttrOperator[DataSpectrumRGBPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "spectrumRGB"


class DataSpectrumRGBField(
    DataNumericBaseField[
        DataSpectrumRGBAttrOperator, DataSpectrumRGBPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataSpectrumRGBAttrOperator
    PLUG_CLS = DataSpectrumRGBPlugOperator
