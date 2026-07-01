# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class TranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "tx"),
        ("translateY", "ty"),
        ("translateZ", "tz"),
    )

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateField(
    DoubleLinear3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class LocalTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localTranslateX", "ltx"),
        ("localTranslateY", "lty"),
        ("localTranslateZ", "ltz"),
    )

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
    ltz = localTranslateZ


class LocalTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalTranslatePlugOperator]
):
    __slots__ = ()

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
    ltz = localTranslateZ


class LocalTranslateField(
    DoubleLinear3CompoundBaseField[LocalTranslateAttrOperator, LocalTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalTranslateAttrOperator
    PLUG_CLS = LocalTranslatePlugOperator

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
    ltz = localTranslateZ
