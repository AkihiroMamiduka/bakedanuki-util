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


class DataTypeAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class DataTypeField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataTypeAttrOperator)
    PLUG_CLS = cast(Type[P], DataTypePlugOperator)
