# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataNurbsSurfacePlugOperator(
    DataTypePlugOperator["DataNurbsSurfaceAttrOperator"]
):
    __slots__ = ()

    def add_attr(self):
        """NURBS surface data 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kNurbsSurface)


class DataNurbsSurfaceAttrOperator(
    DataTypeAttrOperator[DataNurbsSurfacePlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "nurbsSurface"


class DataNurbsSurfaceField(
    DataTypeField[DataNurbsSurfaceAttrOperator, DataNurbsSurfacePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataNurbsSurfaceAttrOperator
    PLUG_CLS = DataNurbsSurfacePlugOperator
