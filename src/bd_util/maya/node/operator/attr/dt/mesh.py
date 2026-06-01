# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator


class DataMeshPlugOperator(DataTypePlugOperator["DataMeshAttrOperator"]):
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


class DataMeshAttrOperator(DataTypeAttrOperator[DataMeshPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "mesh"
    PLUG_CLS = DataMeshPlugOperator
