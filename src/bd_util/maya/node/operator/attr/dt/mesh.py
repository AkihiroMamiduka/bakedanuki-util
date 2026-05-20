# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataMeshPlug(DataTypePlug["DataMeshAttr"]):
    __slots__ = ()


class DataMeshAttr(DataTypeAttr[DataMeshPlug]):
    __slots__ = ()

    DATA_TYPE = "mesh"
    PLUG_CLS = DataMeshPlug
