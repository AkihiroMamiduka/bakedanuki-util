# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataStringArrayPlugOperator(
    DataArrayBasePlugOperator["DataStringArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[str]:
        return self._get_array_values(om.MFnStringArrayData)

    # set
    def set(self, values: list[str]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[str]): セットする値のリスト
        """
        self._set_values(om.MFnStringArrayData, om.MStringArray, values)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kStringArray)


class DataStringArrayAttrOperator(
    DataArrayBaseAttrOperator[DataStringArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "stringArray"


class DataStringArrayField(
    DataArrayBaseField[
        DataStringArrayAttrOperator, DataStringArrayPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataStringArrayAttrOperator
    PLUG_CLS = DataStringArrayPlugOperator
