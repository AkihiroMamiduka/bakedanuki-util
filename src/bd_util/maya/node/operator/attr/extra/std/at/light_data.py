# coding: utf-8
from typing import TypeVar, Type, cast

# self
from ....define.std.at.light_data import (
    LightDataAttrOperator,
    LightDataPlugOperator,
    LightDataField,
)

A = TypeVar("A", bound="LightDataAttrOperator")

P = TypeVar("P", bound="LightDataPlugOperator")


class ExtraCompoundField(LightDataField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], LightDataAttrOperator)
    PLUG_CLS = cast(Type[P], LightDataPlugOperator)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
