# coding: utf-8

from typing import TypeVar, Type, cast, get_args, get_origin

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


class ExtraEnumPlugField(ExtraEnumField[EnumAttrOperator[P], P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[EnumAttrOperator[P]], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, "__orig_bases__", ()):
            if get_origin(base) is ExtraEnumPlugField:
                args = get_args(base)
                if args:
                    cls.PLUG_CLS = args[0]
                break
