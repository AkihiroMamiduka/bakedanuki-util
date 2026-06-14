# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class DataTypePlugOperator(PlugOperator[A]):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ファンクションを作成
        self._fn_attr = om.MFnTypedAttribute()

    # add
    def _add_attr_base(self, mfn_data_type: int):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # アトリビュートを作成
        attr_obj = self._fn_attr.create(
            self.long_name,
            self.short_name,
            mfn_data_type,
        )

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)

        # # デフォルト値
        # if self._oprt_attr.default_value:
        #     self.set_direct(self._oprt_attr.default_value)


class DataTypeAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class DataTypeField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataTypeAttrOperator)
    PLUG_CLS = cast(Type[P], DataTypePlugOperator)
