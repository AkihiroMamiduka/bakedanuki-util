# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...define.std.at.short3 import (
    Short3AttrOperator,
    Short3PlugOperator,
    Short3Field,
)

A = TypeVar("A", bound="Short3AttrOperator")

P = TypeVar("P", bound="Short3PlugOperator")


class ExtraShort3Field(Short3Field[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Short3AttrOperator)
    PLUG_CLS = cast(Type[P], Short3PlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
