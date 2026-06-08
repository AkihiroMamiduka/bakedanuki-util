# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataDouble2PlugOperator(
    DataNumericBasePlugOperator["DataDouble2AttrOperator"]
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
        self._set_data(om.MFnNumericData.k2Double, values)


class DataDouble2AttrOperator(
    DataNumericBaseAttrOperator[DataDouble2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "double2"


class DataDouble2Field(
    DataNumericBaseField[DataDouble2AttrOperator, DataDouble2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataDouble2AttrOperator
    PLUG_CLS = DataDouble2PlugOperator
