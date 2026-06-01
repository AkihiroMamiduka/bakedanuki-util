# coding: utf-8
from __future__ import annotations

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttrOperator, DataTypePlugOperator


class DataReflectanceRGBPlugOperator(
    DataTypePlugOperator["DataReflectanceRGBAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        x, y, z = self._get_data()
        return [x, y, z]

    # set
    def set(self, values: list[float]):
        """
        値をセットする

        modifier.undoIt() 非対応

        Args:
            values (list[float]): x, y, z の値のリスト
        """
        self._set_data(om.MFnNumericData.k3Float, values)


class DataReflectanceRGBAttrOperator(
    DataTypeAttrOperator[DataReflectanceRGBPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "reflectanceRGB"
    PLUG_CLS = DataReflectanceRGBPlugOperator
