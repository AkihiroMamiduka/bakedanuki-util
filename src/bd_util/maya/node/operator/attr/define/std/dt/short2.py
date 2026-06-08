# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataShort2PlugOperator(
    DataNumericBasePlugOperator["DataShort2AttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        x, y = self._get_data()
        return [x, y]

    # set
    def set(self, values: list[int]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[int]): x, y の値のリスト
        """
        self._set_data(om.MFnNumericData.k2Short, values)


class DataShort2AttrOperator(
    DataNumericBaseAttrOperator[DataShort2PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "short2"


class DataShort2Field(
    DataNumericBaseField[DataShort2AttrOperator, DataShort2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataShort2AttrOperator
    PLUG_CLS = DataShort2PlugOperator
