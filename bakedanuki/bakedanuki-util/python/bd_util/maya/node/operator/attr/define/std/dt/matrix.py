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
    """matrix data プラグを TransformMatrix として読み書きする。"""

    __slots__ = ()

    def get(self) -> TransformMatrix:
        """現在の行列値を TransformMatrix のスナップショットで返す。

        Raises:
            ValueError: plugがmatrix dataを保持していない場合。
        """
        return TransformMatrix(self.plug)

    @property
    def transformation_matrix(self) -> om.MTransformationMatrix:
        """現在値を Maya の変換行列で返す。"""
        return self.get().transformation_matrix

    @property
    def translate(self) -> DoubleLinear3:
        """現在の行列から取り出した移動値を返す。"""
        return self.get().translate

    @property
    def rotate(self) -> DoubleAngle3:
        """現在の行列から取り出した回転値を返す。"""
        return self.get().rotate

    def get_rotate(
        self,
        rotate_order: RotationOrder = "xyz",
    ) -> DoubleAngle3:
        """指定した回転順で行列の回転値を返す。

        Args:
            rotate_order: 回転値を表す Euler 回転順。
        """
        return self.get().get_rotate(rotate_order=rotate_order)

    @property
    def scale(self) -> Double3:
        """現在の行列から取り出したスケールを返す。"""
        return self.get().scale

    @property
    def shear(self) -> Double3:
        """現在の行列から取り出したシアーを返す。"""
        return self.get().shear

    @property
    def quat(self) -> Quat:
        """現在の行列から取り出した回転をクォータニオンで返す。"""
        return self.get().quat

    def set_direct(
        self,
        value: (
            TransformMatrix
            | om.MMatrix
            | om.MTransformationMatrix
            | MatrixSequence
        ),
    ) -> None:
        """行列を即時設定する。ModifierManager の Undo 履歴には入らない。

        Args:
            value: TransformMatrix、MMatrix、MTransformationMatrix、
                16 要素または 4 行 4 列の数列。
        """
        matrix = TransformMatrix(value).matrix
        matrix_obj = om.MFnMatrixData().create(matrix)
        self.plug.setMObject(matrix_obj)

    def add_attr(self):
        """matrix data 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnData.kMatrix)


class DataMatrixAttrOperator(DataTypeAttrOperator[DataMatrixPlugOperator]):
    """matrix data 属性の定義を保持する。"""

    __slots__ = ()

    DATA_TYPE = "matrix"


class DataMatrixField(
    DataTypeField[DataMatrixAttrOperator, DataMatrixPlugOperator]
):
    """matrix data 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = DataMatrixAttrOperator
    PLUG_CLS = DataMatrixPlugOperator
