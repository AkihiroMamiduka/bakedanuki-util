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
    DataNumericBasePlugOperator["DataReflectanceRGBAttrOperator"]
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


class DataReflectanceRGBAttrOperator(
    DataNumericBaseAttrOperator[DataReflectanceRGBPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "reflectanceRGB"


class ReflectanceRGBField(
    DataNumericBaseField[
        DataReflectanceRGBAttrOperator, DataReflectanceRGBPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataReflectanceRGBAttrOperator
    PLUG_CLS = DataReflectanceRGBPlugOperator
