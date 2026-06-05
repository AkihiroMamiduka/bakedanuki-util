# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.numeric_base import (
    DataNumericBaseAttrOperator,
    DataNumericBasePlugOperator,
    DataNumericBaseField,
)


class DataLong3PlugOperator(
    DataNumericBasePlugOperator["DataLong3AttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[int]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set(self, values: list[int]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[int]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Long, values)


class DataLong3AttrOperator(
    DataNumericBaseAttrOperator[DataLong3PlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "long3"


class DataLong3Field(
    DataNumericBaseField[DataLong3AttrOperator, DataLong3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataLong3AttrOperator
    PLUG_CLS = DataLong3PlugOperator
