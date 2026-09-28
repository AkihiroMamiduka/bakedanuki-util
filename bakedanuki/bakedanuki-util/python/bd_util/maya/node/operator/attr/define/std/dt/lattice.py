# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataLatticePlugOperator(DataTypePlugOperator["DataLatticeAttrOperator"]):
    """`lattice` データプラグを扱う。"""

    __slots__ = ()

    def add_attr(self):
        """lattice data 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kLattice)


class DataLatticeAttrOperator(DataTypeAttrOperator[DataLatticePlugOperator]):
    """`lattice` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "lattice"


class DataLatticeField(
    DataTypeField[DataLatticeAttrOperator, DataLatticePlugOperator]
):
    """`lattice` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataLatticeAttrOperator
    PLUG_CLS = DataLatticePlugOperator
