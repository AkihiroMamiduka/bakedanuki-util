# coding: utf-8
from __future__ import annotations

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataLatticePlugOperator(DataTypePlugOperator["DataLatticeAttrOperator"]):
    __slots__ = ()

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kLattice)


class DataLatticeAttrOperator(DataTypeAttrOperator[DataLatticePlugOperator]):
    __slots__ = ()

    DATA_TYPE = "lattice"


class DataLatticeField(
    DataTypeField[DataLatticeAttrOperator, DataLatticePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataLatticeAttrOperator
    PLUG_CLS = DataLatticePlugOperator
