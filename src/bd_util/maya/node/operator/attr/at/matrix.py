# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import Attr, Plug


class MatrixPlug(Plug["MatrixAttr"]):
    __slots__ = ()

    # get
    def get(self) -> om.MMatrix:
        return om.MFnMatrixData(self.plug.asMObject()).matrix()

    # set
    def set(self, value: om.MMatrix):
        mat_obj = om.MFnMatrixData().create(value)
        self._node._dg_mod.newPlugValue(self.plug, mat_obj)


class MatrixAttr(Attr[MatrixPlug]):
    __slots__ = ()

    ATTR_TYPE = "matrix"
    PLUG_CLS = MatrixPlug
