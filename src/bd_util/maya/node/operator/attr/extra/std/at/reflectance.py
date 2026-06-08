# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ...define.std.at.reflectance import (
    ReflectanceAttrOperator,
    ReflectancePlugOperator,
    ReflectanceField,
)

A = TypeVar("A", bound="ReflectanceAttrOperator")

P = TypeVar("P", bound="ReflectancePlugOperator")


class ExtraCompoundField(ReflectanceField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], ReflectanceAttrOperator)
    PLUG_CLS = cast(Type[P], ReflectancePlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
