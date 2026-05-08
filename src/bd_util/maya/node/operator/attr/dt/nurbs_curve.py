# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsCurvePlug(DataTypePlug["DataNurbsCurveAttr"]):
    pass


class DataNurbsCurveAttr(DataTypeAttr[DataNurbsCurvePlug]):
    DATA_TYPE = "nurbsCurve"
    PLUG_CLS = DataNurbsCurvePlug
