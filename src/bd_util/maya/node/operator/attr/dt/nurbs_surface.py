# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataNurbsSurfacePlug(DataTypePlug["DataNurbsSurfaceAttr"]):
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


class DataNurbsSurfaceAttr(DataTypeAttr[DataNurbsSurfacePlug]):
    __slots__ = ()

    DATA_TYPE = "nurbsSurface"
    PLUG_CLS = DataNurbsSurfacePlug
