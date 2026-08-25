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
    def get(self) -> TransformMatrix | None:
        try:
            return TransformMatrix(self.plug)
        except ValueError:
            return None

    def _require_value(self) -> TransformMatrix:
        value = self.get()
        if value is None:
            raise ValueError(
                f"Plug does not contain a matrix value: {self.plug.name()}"
            )
        return value

    @property
    def transformation_matrix(self) -> om.MTransformationMatrix | None:
        """
        MPlug から om.MTransformationMatrix を取得する

        Returns:
            om.MTransformationMatrix | None:
                om.MTransformationMatrix 形式の値。matrix data が未設定なら None。
        """
        value = self.get()
        if value is None:
            return None
        return value.transformation_matrix

    @property
    def translate(self) -> tuple[float, float, float]:
        return self._require_value().translate

    @property
    def rotate(self) -> tuple[float, float, float]:
        return self._require_value().rotate

    def get_rotate(
        self,
        order: RotationOrder = "xyz",
    ) -> tuple[float, float, float]:
        return self._require_value().get_rotate(order=order)

    @property
    def scale(self) -> tuple[float, float, float]:
        return self._require_value().scale

    @property
    def shear(self) -> tuple[float, float, float]:
        return self._require_value().shear

    @property
    def quat(self) -> tuple[float, float, float, float]:
        return self._require_value().quat

    # set
    def set_direct(
        self,
        value: TransformMatrix | om.MMatrix | om.MTransformationMatrix,
    ) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value:
                TransformMatrix、MMatrix、または MTransformationMatrix。
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
