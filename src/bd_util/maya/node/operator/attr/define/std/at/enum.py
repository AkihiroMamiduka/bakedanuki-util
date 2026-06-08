# coding: utf-8
from __future__ import annotations

from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class EnumPlugOperator(PlugOperator["EnumAttrOperator"]):
    __slots__ = ("_fn_enum",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._fn_enum: om.MFnEnumAttribute | None = None

    # get
    def get(self) -> int:
        return self.plug.asShort()

    def _get_fn_enum(self) -> om.MFnEnumAttribute:
        # MFnEnumAttribute をキャッシュする
        if self._fn_enum is None:
            self._fn_enum = om.MFnEnumAttribute(self.plug.attribute())
        return self._fn_enum

    # name
    def name_by_index(self, index: int) -> str:
        return self._oprt_attr.NAME_MAP[index]

    def enum_full_name(self) -> str:
        return self._oprt_attr.enum_full_name()

    # index
    def index_by_name(self, name: str) -> int:
        return self._oprt_attr.index_by_name(name)

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueShort(self.plug, value)


class EnumAttrOperator(AttrOperator[EnumPlugOperator]):
    __slots__ = ("_index_by_name_dict",)

    ATTR_TYPE = "enum"

    NAME_MAP: dict[int, str] | None = None

    def __init__(
        self,
        **kwargs: Any,
    ):
        kwargs["enum_name"] = self.enum_full_name()
        super().__init__(**kwargs)

        self._index_by_name_dict: dict[str, int] = {}

    # name
    # def _name_dict(self) -> dict[int, str]:
    #     return {}

    def name_by_index(self, index: int) -> str:
        return self.NAME_MAP[index]

    def enum_full_name(self) -> str:
        return ":".join(
            [f"{name}={index}" for index, name in self.NAME_MAP.items()]
        )

    # index
    def index_by_name(self, name: str) -> int:
        # name_dict を反転させた dict をキャッシュして使用する
        if not self._index_by_name_dict:
            self._index_by_name_dict = {v: k for k, v in self.NAME_MAP.items()}
        return self._index_by_name_dict[name]

    # add
    def add_attr(self, node_name: str):
        fn_node = super().add_attr(node_name)
        if fn_node is None:
            return

        fn_attr = om.MFnEnumAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )
        fn_node.addAttribute(attr_obj)

        # enum_name からフィールドを追加
        if self.enum is not None:
            for member in self.enum:
                fn_attr.addField(member.label, int(member))


class EnumField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)
