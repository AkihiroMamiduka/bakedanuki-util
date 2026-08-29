# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from .......transform.matrix.transform_matrix import (
    MatrixSequence,
    RotationOrder,
    TransformMatrix,
)
from .......value import Double3, DoubleAngle3, DoubleLinear3, Quat
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DataMatrixPlugOperator(DataTypePlugOperator["DataMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> TransformMatrix:
        """matrix dataプラグの現在値をTransformMatrixのsnapshotとして取得する。

        Raises:
            ValueError: plugがmatrix dataを保持していない場合。
        """
        return TransformMatrix(self.plug)

    @property
    def transformation_matrix(self) -> om.MTransformationMatrix:
        """
        MPlug から om.MTransformationMatrix を取得する

        Returns:
            om.MTransformationMatrix: om.MTransformationMatrix 形式の値。
        """
        return self.get().transformation_matrix

    @property
    def translate(self) -> DoubleLinear3:
        return self.get().translate

    @property
    def rotate(self) -> DoubleAngle3:
        return self.get().rotate

    def get_rotate(
        self,
        order: RotationOrder = "xyz",
    ) -> DoubleAngle3:
        return self.get().get_rotate(order=order)

    @property
    def scale(self) -> Double3:
        return self.get().scale

    @property
    def shear(self) -> Double3:
        return self.get().shear

    @property
    def quat(self) -> Quat:
        return self.get().quat

    # set
    def set_direct(
        self,
        value: (
            TransformMatrix
            | om.MMatrix
            | om.MTransformationMatrix
            | MatrixSequence
        ),
    ) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value:
                TransformMatrix、MMatrix、MTransformationMatrix、
                flat 16要素、または4行4列のmatrix sequence。
        """
        matrix = TransformMatrix(value).matrix
        matrix_obj = om.MFnMatrixData().create(matrix)
        self.plug.setMObject(matrix_obj)

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
