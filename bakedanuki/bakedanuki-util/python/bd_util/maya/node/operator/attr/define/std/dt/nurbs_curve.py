# coding: utf-8
from __future__ import annotations

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField
from ........py.error import UnsupportedOperationError


class DataNurbsCurvePlugOperator(
    DataTypePlugOperator["DataNurbsCurveAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self):
        raise UnsupportedOperationError(
            f"{self.__class__.__name__} does not support get operation"
        )

    # set
    def set_direct(self, value: object):
        raise UnsupportedOperationError(
            f"{self.__class__.__name__} does not support set_direct operation"
        )

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kNurbsCurve)


class DataNurbsCurveAttrOperator(
    DataTypeAttrOperator[DataNurbsCurvePlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "nurbsCurve"


class DataNurbsCurveField(
    DataTypeField[DataNurbsCurveAttrOperator, DataNurbsCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataNurbsCurveAttrOperator
    PLUG_CLS = DataNurbsCurvePlugOperator
