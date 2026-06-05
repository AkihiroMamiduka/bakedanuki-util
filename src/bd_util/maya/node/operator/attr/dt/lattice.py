# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataLatticePlugOperator(DataTypePlugOperator["DataLatticeAttrOperator"]):
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


class DataLatticeAttrOperator(DataTypeAttrOperator[DataLatticePlugOperator]):
    __slots__ = ()

    DATA_TYPE = "lattice"


class LatticeField(
    DataTypeField[DataLatticeAttrOperator, DataLatticePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataLatticeAttrOperator
    PLUG_CLS = DataLatticePlugOperator
