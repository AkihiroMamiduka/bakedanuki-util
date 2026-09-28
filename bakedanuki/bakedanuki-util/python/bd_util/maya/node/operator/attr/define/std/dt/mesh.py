# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataMeshPlugOperator(DataTypePlugOperator["DataMeshAttrOperator"]):
    """`mesh` データプラグを扱う。"""

    __slots__ = ()

    def add_attr(self):
        """mesh data 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kMesh)


class DataMeshAttrOperator(DataTypeAttrOperator[DataMeshPlugOperator]):
    """`mesh` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "mesh"


class DataMeshField(DataTypeField[DataMeshAttrOperator, DataMeshPlugOperator]):
    """`mesh` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataMeshAttrOperator
    PLUG_CLS = DataMeshPlugOperator
