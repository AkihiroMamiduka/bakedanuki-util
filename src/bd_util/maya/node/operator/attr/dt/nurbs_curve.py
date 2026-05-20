# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsCurvePlug(DataTypePlug["DataNurbsCurveAttr"]):
    __slots__ = ()


class DataNurbsCurveAttr(DataTypeAttr[DataNurbsCurvePlug]):
    __slots__ = ()

    DATA_TYPE = "nurbsCurve"
    PLUG_CLS = DataNurbsCurvePlug
