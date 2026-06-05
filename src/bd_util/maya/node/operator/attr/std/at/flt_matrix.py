# coding: utf-8
# maya
from maya.api import OpenMaya as om

# self
from ..._core import AttrOperator, PlugOperator, AttributeField


class FltMatrixPlugOperator(PlugOperator["FltMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MFloatMatrix:
        return om.MFnFloatMatrixData(self.plug.asMObject()).matrix()

    # set
    def set(self, value: om.MFloatMatrix):
        matrix_obj = om.MFnFloatMatrixData().create(value)
        self._node._dg_mod.newPlugValue(self.plug, matrix_obj)


class FltMatrixAttrOperator(AttrOperator[FltMatrixPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "fltMatrix"


class FltMatrixField(
    AttributeField[FltMatrixAttrOperator, FltMatrixPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FltMatrixAttrOperator
    PLUG_CLS = FltMatrixPlugOperator
