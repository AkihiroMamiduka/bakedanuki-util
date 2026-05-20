# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsSurfacePlug(DataTypePlug["DataNurbsSurfaceAttr"]):
    __slots__ = ()


class DataNurbsSurfaceAttr(DataTypeAttr[DataNurbsSurfacePlug]):
    __slots__ = ()

    DATA_TYPE = "nurbsSurface"
    PLUG_CLS = DataNurbsSurfacePlug
