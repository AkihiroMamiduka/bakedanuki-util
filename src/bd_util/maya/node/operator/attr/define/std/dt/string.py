# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from ._core import (
    DataTypeAttrOperator,
    DataTypePlugOperator,
    DataTypeField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DataStringPlugOperator(DataTypePlugOperator["DataStringAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        return self.plug.asString()

    # set
    def set(self, value: str):
        self._node._dg_mod.newPlugValueString(self.plug, value)

    def set_direct(self, value: str):
        self.plug.setString(value)

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

        # デフォルト値
        if self._oprt_attr.default_value:
            self.set_direct(self._oprt_attr.default_value)


class DataStringAttrOperator(DataTypeAttrOperator[DataStringPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "string"


class DataStringField(
    DataTypeField[DataStringAttrOperator, DataStringPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataStringAttrOperator
    PLUG_CLS = DataStringPlugOperator
