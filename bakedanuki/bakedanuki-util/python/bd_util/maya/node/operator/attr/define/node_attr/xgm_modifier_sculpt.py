# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField


class TweaksPlugOperator(CompoundPlugOperator["TweaksAttrOperator"]):
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

    enable = BoolField(default_value=True)
    e = enable

    lock = BoolField(default_value=False)
    l = lock

    strength = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    s = strength

    ownerId = LongField(default_value=-1)
    oi = ownerId

    uiName = DataStringField()
    uin = uiName

    uiGroup = DataStringField()
    uig = uiGroup

    uiOrder = LongField(default_value=0)
    uio = uiOrder


class TweaksAttrOperator(CompoundAttrOperator[TweaksPlugOperator]):
    __slots__ = ()

    tweak = TypedField()
    t = tweak

    enable = BoolField(default_value=True)
    e = enable

    lock = BoolField(default_value=False)
    l = lock

    strength = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    s = strength

    ownerId = LongField(default_value=-1)
    oi = ownerId

    uiName = DataStringField()
    uin = uiName

    uiGroup = DataStringField()
    uig = uiGroup

    uiOrder = LongField(default_value=0)
    uio = uiOrder


class TweaksField(CompoundField[TweaksAttrOperator, TweaksPlugOperator]):
    __slots__ = ()

    ATTR_CLS = TweaksAttrOperator
    PLUG_CLS = TweaksPlugOperator


class TweakGroupsPlugOperator(CompoundPlugOperator["TweakGroupsAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tweakGroupEnable", "tge"),
        ("tweakGroupOwnerId", "tgi"),
        ("tweakGroupUIName", "tgn"),
        ("tweakGroupUIOrder", "tgo"),
    )

    tweakGroupEnable = BoolField(default_value=True)
    tge = tweakGroupEnable

    tweakGroupOwnerId = LongField(default_value=-1)
    tgi = tweakGroupOwnerId

    tweakGroupUIName = DataStringField()
    tgn = tweakGroupUIName

    tweakGroupUIOrder = LongField(default_value=0)
    tgo = tweakGroupUIOrder


class TweakGroupsAttrOperator(CompoundAttrOperator[TweakGroupsPlugOperator]):
    __slots__ = ()

    tweakGroupEnable = BoolField(default_value=True)
    tge = tweakGroupEnable

    tweakGroupOwnerId = LongField(default_value=-1)
    tgi = tweakGroupOwnerId

    tweakGroupUIName = DataStringField()
    tgn = tweakGroupUIName

    tweakGroupUIOrder = LongField(default_value=0)
    tgo = tweakGroupUIOrder


class TweakGroupsField(
    CompoundField[TweakGroupsAttrOperator, TweakGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TweakGroupsAttrOperator
    PLUG_CLS = TweakGroupsPlugOperator
