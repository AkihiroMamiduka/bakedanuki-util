# coding: utf-8

from typing import TypeVar, Type, cast

# self
from ....define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)

A = TypeVar("A", bound="EnumAttrOperator")

P = TypeVar("P", bound="EnumPlugOperator")


class ExtraEnumField(EnumField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
