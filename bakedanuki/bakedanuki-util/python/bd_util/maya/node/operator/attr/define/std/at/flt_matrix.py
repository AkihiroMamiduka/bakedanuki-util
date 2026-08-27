# coding: utf-8
# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class FltMatrixPlugOperator(PlugOperator["FltMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MFloatMatrix:
        """fltMatrixプラグの現在値をMFloatMatrixで取得する。"""
        matrix = om.MFnMatrixData(self.plug.asMObject()).matrix()
        return om.MFloatMatrix(matrix)

    # set
    def set(self, value: om.MFloatMatrix) -> None:
        """fltMatrixプラグへMFloatMatrixをModifierManager経由で設定する。

        Args:
            value: 設定するMFloatMatrix。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        matrix_obj = om.MFnMatrixData().create(om.MMatrix(value))
        self._node.modifier_manager.dg_mod.newPlugValue(self.plug, matrix_obj)

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
            om.MFnMatrixAttribute.kFloat,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class FltMatrixAttrOperator(AttrOperator[FltMatrixPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "fltMatrix"


class FltMatrixField(
    AttributeField[FltMatrixAttrOperator, FltMatrixPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FltMatrixAttrOperator
    PLUG_CLS = FltMatrixPlugOperator
