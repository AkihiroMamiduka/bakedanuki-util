# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class DoublePlugOperator(PlugOperator["DoubleAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> float:
        return self.plug.asDouble()

    # set
    def set(self, value: float):
        self._node._dg_mod.newPlugValueDouble(self.plug, value)

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # アトリビュートを作成
        fn_attr = om.MFnNumericAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnNumericData.kDouble,
            self._oprt_attr.default_value,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)

        # アトリビュート設定
        #   min/max
        val = self._oprt_attr.min_value
        if val is not None:
            fn_attr.setMin(val)
        val = self._oprt_attr.max_value
        if val is not None:
            fn_attr.setMax(val)
        #   soft min/max
        val = self._oprt_attr.soft_min_value
        if val is not None:
            fn_attr.setSoftMin(val)
        val = self._oprt_attr.soft_max_value
        if val is not None:
            fn_attr.setSoftMax(val)


class DoubleAttrOperator(AttrOperator[DoublePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "double"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # デフォルト値
        if self.default_value is None:
            self.default_value = 0.0


class DoubleField(AttributeField[DoubleAttrOperator, DoublePlugOperator]):
    __slots__ = ()

    ATTR_CLS = DoubleAttrOperator
    PLUG_CLS = DoublePlugOperator
