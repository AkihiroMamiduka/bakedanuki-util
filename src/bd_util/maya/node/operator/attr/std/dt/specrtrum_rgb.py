# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataSpectrumRGBPlugOperator(
    DataNumericBasePlugOperator["DataSpectrumRGBAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Float, values)


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
