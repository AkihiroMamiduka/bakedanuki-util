# coding: utf-8
# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class MessagePlugOperator(PlugOperator["MessageAttrOperator"]):
    __slots__ = ()

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnMessageAttribute()
        self._fn_attr = fn_attr

        # アトリビュートを作成
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class MessageAttrOperator(AttrOperator[MessagePlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "message"


class MessageField(AttributeField[MessageAttrOperator, MessagePlugOperator]):
    __slots__ = ()

    ATTR_CLS = MessageAttrOperator
    PLUG_CLS = MessagePlugOperator
