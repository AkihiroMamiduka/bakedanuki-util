# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataMeshPlug(DataTypePlug["DataMeshAttr"]):
    pass


class DataMeshAttr(DataTypeAttr[DataMeshPlug]):
    DATA_TYPE = "mesh"
    PLUG_CLS = DataMeshPlug
