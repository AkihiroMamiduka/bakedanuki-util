# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataLatticePlug(DataTypePlug["DataLatticeAttr"]):
    __slots__ = ()


class DataLatticeAttr(DataTypeAttr[DataLatticePlug]):
    __slots__ = ()

    DATA_TYPE = "lattice"
    PLUG_CLS = DataLatticePlug
