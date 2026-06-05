# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataMeshPlugOperator(DataTypePlugOperator["DataMeshAttrOperator"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "DataMeshPlugOperator does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "DataMeshPlugOperator does not support set operation"
        )


class DataMeshAttrOperator(DataTypeAttrOperator[DataMeshPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "mesh"


class DataMeshField(DataTypeField[DataMeshAttrOperator, DataMeshPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DataMeshAttrOperator
    PLUG_CLS = DataMeshPlugOperator
