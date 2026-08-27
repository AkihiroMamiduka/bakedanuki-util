# coding: utf-8
from __future__ import annotations

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataMeshPlugOperator(DataTypePlugOperator["DataMeshAttrOperator"]):
    __slots__ = ()

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kMesh)


class DataMeshAttrOperator(DataTypeAttrOperator[DataMeshPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "mesh"


class DataMeshField(DataTypeField[DataMeshAttrOperator, DataMeshPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DataMeshAttrOperator
    PLUG_CLS = DataMeshPlugOperator
