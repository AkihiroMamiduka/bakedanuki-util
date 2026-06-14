# coding: utf-8
from __future__ import annotations

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField
from ........py.error import UnsupportedOperationError


class DataNurbsSurfacePlugOperator(
    DataTypePlugOperator["DataNurbsSurfaceAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self):
        raise UnsupportedOperationError(
            f"{self.__class__.__name__} does not support get operation"
        )

    # set
    def set_direct(self, _):
        raise UnsupportedOperationError(
            f"{self.__class__.__name__} does not support set_direct operation"
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
