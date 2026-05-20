# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import DataTypeAttr, DataTypePlug


class DataMatrixPlug(DataTypePlug["DataMatrixAttr"]):
    __slots__ = ()

    # get
    def get(self) -> om.MMatrix:
        return om.MFnMatrixData(self.plug.asMObject()).matrix()

    # set
    def set(self, value: om.MMatrix):
        mat_obj = om.MFnMatrixData().create(value)
        self._node._dg_mod.newPlugValue(self.plug, mat_obj)


class DataMatrixAttr(DataTypeAttr[DataMatrixPlug]):
    __slots__ = ()

    DATA_TYPE = "matrix"
    PLUG_CLS = DataMatrixPlug
