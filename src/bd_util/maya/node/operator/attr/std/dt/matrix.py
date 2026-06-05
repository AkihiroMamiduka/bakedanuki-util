# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ....... import logger as u_logger
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


class DataMatrixAttrOperator(DataTypeAttrOperator[DataMatrixPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "matrix"

    # add
    def add_attr(self, node_name: str):
        fn_node = super().add_attr(node_name)
        if fn_node is None:
            return

        fn_attr = om.MFnTypedAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnMatrixData.kMatrix,
        )
        fn_node.addAttribute(attr_obj)


class DataMatrixField(
    DataTypeField[DataMatrixAttrOperator, DataMatrixPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataMatrixAttrOperator
    PLUG_CLS = DataMatrixPlugOperator
