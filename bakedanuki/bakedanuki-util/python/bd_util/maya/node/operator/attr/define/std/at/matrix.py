# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from .......transform.matrix.transform_matrix import TransformMatrix
from ...._core import AttrOperator, PlugOperator, AttributeField


class MatrixPlugOperator(PlugOperator["MatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> TransformMatrix:
        return TransformMatrix(self.plug)

    # set
    def set(
        self,
        value: TransformMatrix | om.MMatrix | om.MTransformationMatrix,
    ) -> None:
        matrix = TransformMatrix(value).matrix
        mat_obj = om.MFnMatrixData().create(matrix)
        self._node.modifier_manager.dg_mod.newPlugValue(self.plug, mat_obj)

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnMatrixAttribute()
        self._fn_attr = fn_attr

        # アトリビュートを作成
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnMatrixAttribute.kDouble,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class MatrixAttrOperator(AttrOperator[MatrixPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "matrix"


class MatrixField(AttributeField[MatrixAttrOperator, MatrixPlugOperator]):
    __slots__ = ()

    ATTR_CLS = MatrixAttrOperator
    PLUG_CLS = MatrixPlugOperator
