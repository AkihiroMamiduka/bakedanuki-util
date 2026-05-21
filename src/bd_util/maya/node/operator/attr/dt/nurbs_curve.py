# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsCurvePlug(DataTypePlug["DataNurbsCurveAttr"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "DataMeshPlug does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "DataMeshPlug does not support set operation"
        )


class DataNurbsCurveAttr(DataTypeAttr[DataNurbsCurvePlug]):
    __slots__ = ()

    DATA_TYPE = "nurbsCurve"
    PLUG_CLS = DataNurbsCurvePlug
