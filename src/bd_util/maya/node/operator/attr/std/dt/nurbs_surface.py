# coding: utf-8
from __future__ import annotations

from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField


class DataNurbsSurfacePlugOperator(
    DataTypePlugOperator["DataNurbsSurfaceAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self):
        raise NotImplementedError(
            "DataNurbsSurfacePlugOperator does not support get operation"
        )

    # set
    def set(self, value):
        raise NotImplementedError(
            "DataNurbsSurfacePlugOperator does not support set operation"
        )


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
