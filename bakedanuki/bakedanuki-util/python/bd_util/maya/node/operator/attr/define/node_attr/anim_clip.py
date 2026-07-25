# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField


class WorldStartPositionPlugOperator(
    CompoundPlugOperator["WorldStartPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldStartPositionX", "wspx"),
        ("worldStartPositionY", "wspy"),
        ("worldStartPositionZ", "wspz"),
    )

    worldStartPositionX = DoubleField(default_value=0.0)
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField(default_value=0.0)
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField(default_value=0.0)
    wspz = worldStartPositionZ


class WorldStartPositionAttrOperator(
    CompoundAttrOperator[WorldStartPositionPlugOperator]
):
    __slots__ = ()

    worldStartPositionX = DoubleField(default_value=0.0)
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField(default_value=0.0)
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField(default_value=0.0)
    wspz = worldStartPositionZ


class WorldStartPositionField(
    CompoundField[WorldStartPositionAttrOperator, WorldStartPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldStartPositionAttrOperator
    PLUG_CLS = WorldStartPositionPlugOperator

    worldStartPositionX = DoubleField(default_value=0.0)
    wspx = worldStartPositionX

    worldStartPositionY = DoubleField(default_value=0.0)
    wspy = worldStartPositionY

    worldStartPositionZ = DoubleField(default_value=0.0)
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

    localStartPositionX = DoubleField(default_value=0.0)
    lspx = localStartPositionX

    localStartPositionY = DoubleField(default_value=0.0)
    lspy = localStartPositionY

    localStartPositionZ = DoubleField(default_value=0.0)
    lspz = localStartPositionZ


class LocalStartPositionAttrOperator(
    CompoundAttrOperator[LocalStartPositionPlugOperator]
):
    __slots__ = ()

    localStartPositionX = DoubleField(default_value=0.0)
    lspx = localStartPositionX

    localStartPositionY = DoubleField(default_value=0.0)
    lspy = localStartPositionY

    localStartPositionZ = DoubleField(default_value=0.0)
    lspz = localStartPositionZ


class LocalStartPositionField(
    CompoundField[LocalStartPositionAttrOperator, LocalStartPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalStartPositionAttrOperator
    PLUG_CLS = LocalStartPositionPlugOperator

    localStartPositionX = DoubleField(default_value=0.0)
    lspx = localStartPositionX

    localStartPositionY = DoubleField(default_value=0.0)
    lspy = localStartPositionY

    localStartPositionZ = DoubleField(default_value=0.0)
    lspz = localStartPositionZ
