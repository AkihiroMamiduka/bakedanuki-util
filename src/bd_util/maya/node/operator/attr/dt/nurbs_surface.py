# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator


class DataNurbsSurfacePlugOperator(
    DataTypePlugOperator["DataNurbsSurfaceAttrOperator"]
):
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


class DataNurbsSurfaceAttrOperator(
    DataTypeAttrOperator[DataNurbsSurfacePlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "nurbsSurface"
    PLUG_CLS = DataNurbsSurfacePlugOperator
