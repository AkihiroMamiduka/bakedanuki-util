# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsSurfacePlug(DataTypePlug["DataNurbsSurfaceAttr"]):
    pass


class DataNurbsSurfaceAttr(DataTypeAttr[DataNurbsSurfacePlug]):
    DATA_TYPE = "nurbsSurface"
    PLUG_CLS = DataNurbsSurfacePlug
