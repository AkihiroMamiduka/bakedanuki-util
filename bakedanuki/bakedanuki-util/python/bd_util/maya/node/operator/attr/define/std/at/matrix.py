# coding: utf-8

from maya.api import OpenMaya as om

from .......transform.matrix.transform_matrix import (
    MatrixSequence,
    TransformMatrix,
)
from ...._core import AttrOperator, PlugOperator, AttributeField


class MatrixPlugOperator(PlugOperator["MatrixAttrOperator"]):
    """Maya の `matrix` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> TransformMatrix:
        """matrix プラグの現在値を `TransformMatrix` として取得する。"""
        return TransformMatrix(self.plug)

    def set(
        self,
        value: (
            TransformMatrix
            | om.MMatrix
            | om.MTransformationMatrix
            | MatrixSequence
        ),
    ) -> None:
        """matrix プラグへ行列値を `ModifierManager` 経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する `TransformMatrix`、`MMatrix`、
                `MTransformationMatrix`、flat 16要素、または4行4列の
                matrix sequence。
        """
        matrix = TransformMatrix(value).matrix
        mat_obj = om.MFnMatrixData().create(matrix)
        self._node.modifier_manager.dg_mod.newPlugValue(self.plug, mat_obj)

    def add_attr(self):
        """matrix 属性がなければ、ノードへ即時追加する。"""
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
    """Maya の `matrix` 属性定義を表す。"""

    __slots__ = ()

    ATTR_TYPE = "matrix"


class MatrixField(AttributeField[MatrixAttrOperator, MatrixPlugOperator]):
    """ノードクラスに `matrix` 属性を定義する。"""

    __slots__ = ()

    ATTR_CLS = MatrixAttrOperator
    PLUG_CLS = MatrixPlugOperator
