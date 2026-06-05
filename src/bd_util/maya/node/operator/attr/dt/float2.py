# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataFloat2PlugOperator(
    DataNumericBasePlugOperator["DataFloat2AttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y = self._get_data()
        return [x, y]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Float, values)


class DataFloat2AttrOperator(
    DataNumericBaseAttrOperator[DataFloat2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "float2"


class DataFloat2Field(
    DataNumericBaseField[DataFloat2AttrOperator, DataFloat2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataFloat2AttrOperator
    PLUG_CLS = DataFloat2PlugOperator
