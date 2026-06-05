# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .._core import AttrOperator, PlugOperator, AttributeField


class MatrixPlugOperator(PlugOperator["MatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MMatrix:
        return om.MFnMatrixData(self.plug.asMObject()).matrix()

    # set
    def set(self, value: om.MMatrix):
        mat_obj = om.MFnMatrixData().create(value)
        self._node._dg_mod.newPlugValue(self.plug, mat_obj)


class MatrixAttrOperator(AttrOperator[MatrixPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "matrix"


class MatrixField(AttributeField[MatrixAttrOperator, MatrixPlugOperator]):
    __slots__ = ()

    ATTR_CLS = MatrixAttrOperator
    PLUG_CLS = MatrixPlugOperator
