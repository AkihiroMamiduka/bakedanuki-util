# coding: utf-8

from typing import Any, TypeVar, Type, cast, get_args, get_origin

# self
from ....define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)

A = TypeVar("A", bound="EnumAttrOperator[Any]")

P = TypeVar("P", bound="EnumPlugOperator[Any]")


class ExtraEnumField(EnumField[EnumAttrOperator[P], P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[EnumAttrOperator[P]], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, "__orig_bases__", ()):
            if get_origin(base) is ExtraEnumField:
                args = get_args(base)
                if args:
                    setattr(cls, "PLUG_CLS", args[0])
                break
