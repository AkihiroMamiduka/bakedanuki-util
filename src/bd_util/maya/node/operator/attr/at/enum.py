# coding: utf-8
from __future__ import annotations

from typing import Any, Generic, Self, Type, TypeVar, overload

# self
from .....attr.enum import AttributeEnum
from .._core import Attr, Plug

E = TypeVar("E", bound=AttributeEnum)


class EnumPlug(Plug["EnumAttr"], Generic[E]):
    @property
    def enum(self) -> type[E]:
        """
        EnumAttr に紐付いた AttributeEnum サブクラスを返す。

        Returns:
            type[E]: AttributeEnum サブクラス。
        """
        return self._attr._enum_cls


class EnumAttr(Attr[EnumPlug], Generic[E]):
    ATTR_TYPE = "enum"
    PLUG_CLS = EnumPlug

    @property
    def enum(self) -> type[E]:
        """
        EnumAttr に紐付いた AttributeEnum サブクラスを返す。

        Returns:
            type[E]: AttributeEnum サブクラス。
        """
        return self._enum_cls

    def __init__(
        self,
        enum_name: Type[E] | list[str] | str | None = None,
        multi: bool = False,
        extra: bool = False,
        default_value: Any = None,
        min_value: Any = None,
        max_value: Any = None,
        soft_min_value: Any = None,
        soft_max_value: Any = None,
        number_of_children: int | None = None,
        parent: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ):
        # AttributeEnum サブクラスが渡された場合は Maya enumName 文字列に変換し、
        # クラスを _enum_cls に保存する
        self._enum_cls: Type[E] | None = None
        if isinstance(enum_name, type) and issubclass(enum_name, AttributeEnum):
            self._enum_cls = enum_name
            enum_name_str: str | None = enum_name.to_enum_name()
        elif isinstance(enum_name, list):
            enum_name_str = ":".join(enum_name)
        else:
            enum_name_str = enum_name

        super().__init__(
            multi=multi,
            extra=extra,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            soft_min_value=soft_min_value,
            soft_max_value=soft_max_value,
            enum_name=enum_name_str,
            number_of_children=number_of_children,
            parent=parent,
            readable=readable,
            writable=writable,
            category=category,
        )

    @overload
    def __get__(self, instance: None, owner: type) -> Self: ...

    @overload
    def __get__(self, instance: object, owner: type) -> EnumPlug[E]: ...

    def __get__(self, instance: object | None, owner: type) -> Self | EnumPlug[E]:
        return super().__get__(instance, owner)  # type: ignore[return-value]
