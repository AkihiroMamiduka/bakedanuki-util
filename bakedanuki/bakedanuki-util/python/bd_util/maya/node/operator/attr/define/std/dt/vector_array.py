# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class DataVectorArrayPlugOperator(
    DataArrayBasePlugOperator["DataVectorArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[tuple[float, float, float]]:
        return [
            (p.x, p.y, p.z)
            for p in self._get_array_values(om.MFnVectorArrayData)
        ]

    # set
    def set_direct(
        self,
        value: list[tuple[float, float, float]],
    ) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[tuple[float, float, float]]):
                セットする値のリスト
        """
        vectors = [om.MVector(*vector) for vector in value]
        self._set_values_after_create(
            om.MFnVectorArrayData,
            om.MVectorArray,
            vectors,
        )

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kVectorArray)


class DataVectorArrayAttrOperator(
    DataArrayBaseAttrOperator[DataVectorArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "vectorArray"


class DataVectorArrayField(
    DataArrayBaseField[
        DataVectorArrayAttrOperator, DataVectorArrayPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = DataVectorArrayAttrOperator
    PLUG_CLS = DataVectorArrayPlugOperator
