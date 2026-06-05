# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataNurbsCurvePlugOperator(
    DataTypePlugOperator["DataNurbsCurveAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "DataNurbsCurvePlugOperator does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "DataNurbsCurvePlugOperator does not support set operation"
        )


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
