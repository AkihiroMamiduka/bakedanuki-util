# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField


class LinkPlugOperator(CompoundPlugOperator["LinkAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("light", "llnk"),
        ("object", "olnk"),
    )

    light = MessageField()
    llnk = light

    object = MessageField()
    olnk = object


class LinkAttrOperator(CompoundAttrOperator[LinkPlugOperator]):
    __slots__ = ()

    light = MessageField()
    llnk = light

    object = MessageField()
    olnk = object


class LinkField(CompoundField[LinkAttrOperator, LinkPlugOperator]):
    __slots__ = ()

    ATTR_CLS = LinkAttrOperator
    PLUG_CLS = LinkPlugOperator


class IgnorePlugOperator(CompoundPlugOperator["IgnoreAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lightIgnored", "lign"),
        ("objectIgnored", "oign"),
    )

    lightIgnored = MessageField()
    lign = lightIgnored

    objectIgnored = MessageField()
    oign = objectIgnored


class IgnoreAttrOperator(CompoundAttrOperator[IgnorePlugOperator]):
    __slots__ = ()

    lightIgnored = MessageField()
    lign = lightIgnored

    objectIgnored = MessageField()
    oign = objectIgnored


class IgnoreField(CompoundField[IgnoreAttrOperator, IgnorePlugOperator]):
    __slots__ = ()

    ATTR_CLS = IgnoreAttrOperator
    PLUG_CLS = IgnorePlugOperator


class ShadowLinkPlugOperator(CompoundPlugOperator["ShadowLinkAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowLight", "sllk"),
        ("shadowObject", "solk"),
    )

    shadowLight = MessageField()
    sllk = shadowLight

    shadowObject = MessageField()
    solk = shadowObject


class ShadowLinkAttrOperator(CompoundAttrOperator[ShadowLinkPlugOperator]):
    __slots__ = ()

    shadowLight = MessageField()
    sllk = shadowLight

    shadowObject = MessageField()
    solk = shadowObject


class ShadowLinkField(
    CompoundField[ShadowLinkAttrOperator, ShadowLinkPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowLinkAttrOperator
    PLUG_CLS = ShadowLinkPlugOperator


class ShadowIgnorePlugOperator(
    CompoundPlugOperator["ShadowIgnoreAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowLightIgnored", "slig"),
        ("shadowObjectIgnored", "soig"),
    )

    shadowLightIgnored = MessageField()
    slig = shadowLightIgnored

    shadowObjectIgnored = MessageField()
    soig = shadowObjectIgnored


class ShadowIgnoreAttrOperator(CompoundAttrOperator[ShadowIgnorePlugOperator]):
    __slots__ = ()

    shadowLightIgnored = MessageField()
    slig = shadowLightIgnored

    shadowObjectIgnored = MessageField()
    soig = shadowObjectIgnored


class ShadowIgnoreField(
    CompoundField[ShadowIgnoreAttrOperator, ShadowIgnorePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowIgnoreAttrOperator
    PLUG_CLS = ShadowIgnorePlugOperator
