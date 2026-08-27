# coding: utf-8
from __future__ import annotations

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataNurbsCurvePlugOperator(
    DataTypePlugOperator["DataNurbsCurveAttrOperator"]
):
    __slots__ = ()

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
