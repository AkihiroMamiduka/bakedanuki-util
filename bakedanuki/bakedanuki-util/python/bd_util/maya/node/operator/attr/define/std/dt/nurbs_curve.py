# coding: utf-8
from __future__ import annotations

from maya.api import OpenMaya as om

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataNurbsCurvePlugOperator(
    DataTypePlugOperator["DataNurbsCurveAttrOperator"]
):
    """`nurbsCurve` データプラグを扱う。"""

    __slots__ = ()

    def add_attr(self):
        """NURBS curve data 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kNurbsCurve)


class DataNurbsCurveAttrOperator(
    DataTypeAttrOperator[DataNurbsCurvePlugOperator]
):
    """`nurbsCurve` データ属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "nurbsCurve"


class DataNurbsCurveField(
    DataTypeField[DataNurbsCurveAttrOperator, DataNurbsCurvePlugOperator]
):
    """`nurbsCurve` データ属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataNurbsCurveAttrOperator
    PLUG_CLS = DataNurbsCurvePlugOperator
