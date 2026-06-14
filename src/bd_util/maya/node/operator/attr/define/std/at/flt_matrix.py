# coding: utf-8
# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class FltMatrixPlugOperator(PlugOperator["FltMatrixAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> om.MFloatMatrix:
        return om.MFnFloatMatrixData(self.plug.asMObject()).matrix()

    # set
    def set(self, value: om.MFloatMatrix):
        matrix_obj = om.MFnFloatMatrixData().create(value)
        self._node._dg_mod.newPlugValue(self.plug, matrix_obj)

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
