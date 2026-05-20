# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttr, DataTypePlug


class DataLatticePlug(DataTypePlug["DataLatticeAttr"]):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "DataLatticePlug does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "DataLatticePlug does not support set operation"
        )


class DataLatticeAttr(DataTypeAttr[DataLatticePlug]):
    __slots__ = ()

    DATA_TYPE = "lattice"
    PLUG_CLS = DataLatticePlug
