# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField


class TweaksPlugOperator(
    CompoundPlugOperator["TweaksAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweak", "t"),
        ("enable", "e"),
        ("lock", "l"),
        ("strength", "s"),
        ("ownerId", "oi"),
        ("uiName", "uin"),
        ("uiGroup", "uig"),
        ("uiOrder", "uio"),
    )

    tweak = TypedField()
    t = tweak

    enable = BoolField()
    e = enable

    lock = BoolField()
    l = lock

    strength = FloatField()
    s = strength

    ownerId = LongField()
    oi = ownerId

    uiName = DataStringField()
    uin = uiName

    uiGroup = DataStringField()
    uig = uiGroup

    uiOrder = LongField()
    uio = uiOrder


class TweaksAttrOperator(
    CompoundAttrOperator[TweaksPlugOperator]
):
    __slots__ = ()

    tweak = TypedField()
    t = tweak

    enable = BoolField()
    e = enable

    lock = BoolField()
    l = lock

    strength = FloatField()
    s = strength

    ownerId = LongField()
    oi = ownerId

    uiName = DataStringField()
    uin = uiName

    uiGroup = DataStringField()
    uig = uiGroup

    uiOrder = LongField()
    uio = uiOrder


class TweaksField(
    CompoundField[TweaksAttrOperator, TweaksPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweaksAttrOperator
    PLUG_CLS = TweaksPlugOperator


class TweakGroupsPlugOperator(
    CompoundPlugOperator["TweakGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweakGroupEnable", "tge"),
        ("tweakGroupOwnerId", "tgi"),
        ("tweakGroupUIName", "tgn"),
        ("tweakGroupUIOrder", "tgo"),
    )

    tweakGroupEnable = BoolField()
    tge = tweakGroupEnable

    tweakGroupOwnerId = LongField()
    tgi = tweakGroupOwnerId

    tweakGroupUIName = DataStringField()
    tgn = tweakGroupUIName

    tweakGroupUIOrder = LongField()
    tgo = tweakGroupUIOrder


class TweakGroupsAttrOperator(
    CompoundAttrOperator[TweakGroupsPlugOperator]
):
    __slots__ = ()

    tweakGroupEnable = BoolField()
    tge = tweakGroupEnable

    tweakGroupOwnerId = LongField()
    tgi = tweakGroupOwnerId

    tweakGroupUIName = DataStringField()
    tgn = tweakGroupUIName

    tweakGroupUIOrder = LongField()
    tgo = tweakGroupUIOrder


class TweakGroupsField(
    CompoundField[TweakGroupsAttrOperator, TweakGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweakGroupsAttrOperator
    PLUG_CLS = TweakGroupsPlugOperator
