# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ._core import (
    DataTypeAttrOperator,
    DataTypePlugOperator,
    DataTypeField,
)


class DataStringPlugOperator(DataTypePlugOperator["DataStringAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asString()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueString(self.plug, value)

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnTypedAttribute()

        # アトリビュートを作成
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            om.MFnData.kString,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class DataStringAttrOperator(DataTypeAttrOperator[DataStringPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "string"


class DataStringField(
    DataTypeField[DataStringAttrOperator, DataStringPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataStringAttrOperator
    PLUG_CLS = DataStringPlugOperator
