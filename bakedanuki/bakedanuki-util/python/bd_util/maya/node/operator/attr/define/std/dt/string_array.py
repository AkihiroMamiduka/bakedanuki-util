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
        """stringArray dataプラグの現在値を文字列リストで取得する。"""
        return self._get_array_values(om.MFnStringArrayData)

    # set
    def set_direct(self, value: list[str]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[str]): セットする値のリスト
        """
        self.plug.setMObject(om.MFnStringArrayData().create(value))

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
