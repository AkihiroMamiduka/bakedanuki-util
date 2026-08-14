# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataReflectanceRGBPlugOperator(
    DataNumericBasePlugOperator["DataReflectanceRGBAttrOperator", float]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set_direct(self, value: list[float]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[float]): x, y, z の値のリスト
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
