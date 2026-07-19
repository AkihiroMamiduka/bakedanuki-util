# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from .......transform.matrix.transform_matrix import (
    RotationOrder,
    TransformMatrix,
)
from ._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DataMatrixPlugOperator(DataTypePlugOperator["DataMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MMatrix | None:
        try:
            return self.transform_matrix.matrix
        except ValueError:
            return None

    @property
    def transform_matrix(self) -> TransformMatrix:
        """現在の plug 値を TransformMatrix のスナップショットで返す。"""
        return TransformMatrix(self.plug)

    @property
    def transformation_matrix(self) -> om.MTransformationMatrix | None:
        """
        MPlug から om.MTransformationMatrix を取得する

        Returns:
            om.MTransformationMatrix | None:
                om.MTransformationMatrix 形式の値。matrix data が未設定なら None。
        """
        matrix = self.get()
        if matrix is None:
            return None
        return om.MTransformationMatrix(matrix)

    @property
    def translate(self) -> tuple[float, float, float]:
        return self.transform_matrix.translate

    @property
    def rotate(self) -> tuple[float, float, float]:
        return self.transform_matrix.rotate

    def get_rotate(
        self,
        order: RotationOrder = "xyz",
    ) -> tuple[float, float, float]:
        return self.transform_matrix.get_rotate(order=order)

    @property
    def scale(self) -> tuple[float, float, float]:
        return self.transform_matrix.scale

    @property
    def shear(self) -> tuple[float, float, float]:
        return self.transform_matrix.shear

    @property
    def quat(self) -> tuple[float, float, float, float]:
        return self.transform_matrix.quat

    # set
    def set_direct(self, value: om.MMatrix):
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (om.MMatrix): om.MMatrix 形式の値
        """
        matrix = om.MMatrix(value)
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
