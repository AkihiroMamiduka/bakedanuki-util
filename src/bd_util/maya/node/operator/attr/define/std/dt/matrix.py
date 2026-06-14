# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DataMatrixPlugOperator(DataTypePlugOperator["DataMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MMatrix:
        return self.plug.asMDataHandle().asMatrix()

    # set
    def set(self, value: om.MMatrix):
        matrix = om.MMatrix(value)
        matrix_obj = om.MFnMatrixData().create(matrix)
        self._node._dg_mod.newPlugValue(self.plug, matrix_obj)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kMatrix)


class DataMatrixAttrOperator(DataTypeAttrOperator[DataMatrixPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "matrix"


class DataMatrixField(
    DataTypeField[DataMatrixAttrOperator, DataMatrixPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataMatrixAttrOperator
    PLUG_CLS = DataMatrixPlugOperator
