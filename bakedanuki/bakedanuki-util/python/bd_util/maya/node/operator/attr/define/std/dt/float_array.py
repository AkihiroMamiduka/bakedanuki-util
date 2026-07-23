# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataFloatArrayPlugOperator(
    DataArrayBasePlugOperator["DataFloatArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        return self._get_array_values(om.MFnFloatArrayData)

    # set
    def set_direct(self, values: list[float]):
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            values (list[float]): セットする値のリスト
        """
        self._set_values(om.MFnFloatArrayData, om.MFloatArray, values)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kFloatArray)


class DataFloatArrayAttrOperator(
    DataArrayBaseAttrOperator[DataFloatArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "floatArray"


class DataFloatArrayField(
    DataArrayBaseField[DataFloatArrayAttrOperator, DataFloatArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataFloatArrayAttrOperator
    PLUG_CLS = DataFloatArrayPlugOperator
