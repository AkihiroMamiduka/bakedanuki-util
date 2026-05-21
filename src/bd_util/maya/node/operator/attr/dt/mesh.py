# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataMeshPlug(DataTypePlug["DataMeshAttr"]):
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


class DataMeshAttr(DataTypeAttr[DataMeshPlug]):
    __slots__ = ()

    DATA_TYPE = "mesh"
    PLUG_CLS = DataMeshPlug
