# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataLatticePlug(DataTypePlug["DataLatticeAttr"]):
    pass


class DataLatticeAttr(DataTypeAttr[DataLatticePlug]):
    DATA_TYPE = "lattice"
    PLUG_CLS = DataLatticePlug
