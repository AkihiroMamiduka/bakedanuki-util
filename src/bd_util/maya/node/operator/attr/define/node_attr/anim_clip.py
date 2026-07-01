# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField


class WorldStartPositionPlugOperator(
    CompoundPlugOperator["WorldStartPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldStartPositionX", "wspx"),
        ("worldStartPositionY", "wspy"),
        ("worldStartPositionZ", "wspz"),
    )

    worldStartPositionX = DoubleField()
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField()
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField()
    wspz = worldStartPositionZ


class WorldStartPositionAttrOperator(
    CompoundAttrOperator[WorldStartPositionPlugOperator]
):
    __slots__ = ()

    worldStartPositionX = DoubleField()
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField()
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField()
    wspz = worldStartPositionZ


class WorldStartPositionField(
    CompoundField[WorldStartPositionAttrOperator, WorldStartPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldStartPositionAttrOperator
    PLUG_CLS = WorldStartPositionPlugOperator

    worldStartPositionX = DoubleField()
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField()
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField()
    wspz = worldStartPositionZ


class LocalStartPositionPlugOperator(
    CompoundPlugOperator["LocalStartPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localStartPositionX", "lspx"),
        ("localStartPositionY", "lspy"),
        ("localStartPositionZ", "lspz"),
    )

    localStartPositionX = DoubleField()
    lspx = localStartPositionX

    localStartPositionY = DoubleField()
    lspy = localStartPositionY

    localStartPositionZ = DoubleField()
    lspz = localStartPositionZ


class LocalStartPositionAttrOperator(
    CompoundAttrOperator[LocalStartPositionPlugOperator]
):
    __slots__ = ()

    localStartPositionX = DoubleField()
    lspx = localStartPositionX

    localStartPositionY = DoubleField()
    lspy = localStartPositionY

    localStartPositionZ = DoubleField()
    lspz = localStartPositionZ


class LocalStartPositionField(
    CompoundField[LocalStartPositionAttrOperator, LocalStartPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalStartPositionAttrOperator
    PLUG_CLS = LocalStartPositionPlugOperator

    localStartPositionX = DoubleField()
    lspx = localStartPositionX

    localStartPositionY = DoubleField()
    lspy = localStartPositionY

    localStartPositionZ = DoubleField()
    lspz = localStartPositionZ
