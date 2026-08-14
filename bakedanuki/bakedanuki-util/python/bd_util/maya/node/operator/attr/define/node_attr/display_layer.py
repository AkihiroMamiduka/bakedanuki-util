# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.byte import ByteField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import Float3Field


class DisplayTypeEnumPlugOperator(
    EnumPlugOperator["DisplayTypeEnumAttrOperator"]
):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2


class DisplayTypeEnumAttrOperator(
    EnumAttrOperator[DisplayTypeEnumPlugOperator]
):
    __slots__ = ()

    NORMAL = 0
    TEMPLATE = 1
    REFERENCE = 2

    NAME_MAP = {
        NORMAL: "Normal",
        TEMPLATE: "Template",
        REFERENCE: "Reference",
    }


class DisplayTypeEnumField(
    EnumField[DisplayTypeEnumAttrOperator, DisplayTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayTypeEnumAttrOperator
    PLUG_CLS = DisplayTypeEnumPlugOperator


class LevelOfDetailEnumPlugOperator(
    EnumPlugOperator["LevelOfDetailEnumAttrOperator"]
):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1


class LevelOfDetailEnumAttrOperator(
    EnumAttrOperator[LevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    FULL = 0
    BOUNDING_BOX = 1

    NAME_MAP = {
        FULL: "Full",
        BOUNDING_BOX: "Bounding Box",
    }


class LevelOfDetailEnumField(
    EnumField[LevelOfDetailEnumAttrOperator, LevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LevelOfDetailEnumAttrOperator
    PLUG_CLS = LevelOfDetailEnumPlugOperator


class DrawInfoPlugOperator(CompoundPlugOperator["DrawInfoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displayType", "dt"),
        ("levelOfDetail", "lod"),
        ("shading", "s"),
        ("texturing", "t"),
        ("playback", "p"),
        ("enabled", "e"),
        ("visibility", "v"),
        ("hideOnPlayback", "hpb"),
        ("overrideRGBColors", "ovrgbf"),
        ("color", "c"),
        ("overrideColorRGB", "ovrgb"),
        ("overrideColorA", "ovca"),
    )

    displayType = DisplayTypeEnumField(default_value=0)
    dt = displayType

    levelOfDetail = LevelOfDetailEnumField(default_value=0)
    lod = levelOfDetail

    shading = BoolField(default_value=True)
    s = shading

    texturing = BoolField(default_value=True)
    t = texturing

    playback = BoolField(default_value=True)
    p = playback

    enabled = BoolField(default_value=True)
    e = enabled

    visibility = BoolField(default_value=True)
    v = visibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    color = ByteField(default_value=0, min_value=0, max_value=255)
    c = color

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ovca = overrideColorA


class DrawInfoAttrOperator(CompoundAttrOperator[DrawInfoPlugOperator]):
    __slots__ = ()

    displayType = DisplayTypeEnumField(default_value=0)
    dt = displayType

    levelOfDetail = LevelOfDetailEnumField(default_value=0)
    lod = levelOfDetail

    shading = BoolField(default_value=True)
    s = shading

    texturing = BoolField(default_value=True)
    t = texturing

    playback = BoolField(default_value=True)
    p = playback

    enabled = BoolField(default_value=True)
    e = enabled

    visibility = BoolField(default_value=True)
    v = visibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    color = ByteField(default_value=0, min_value=0, max_value=255)
    c = color

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ovca = overrideColorA


class DrawInfoField(CompoundField[DrawInfoAttrOperator, DrawInfoPlugOperator]):
    __slots__ = ()

    ATTR_CLS = DrawInfoAttrOperator
    PLUG_CLS = DrawInfoPlugOperator

    displayType = DisplayTypeEnumField(default_value=0)
    dt = displayType

    levelOfDetail = LevelOfDetailEnumField(default_value=0)
    lod = levelOfDetail

    shading = BoolField(default_value=True)
    s = shading

    texturing = BoolField(default_value=True)
    t = texturing

    playback = BoolField(default_value=True)
    p = playback

    enabled = BoolField(default_value=True)
    e = enabled

    visibility = BoolField(default_value=True)
    v = visibility

    hideOnPlayback = BoolField(default_value=False)
    hpb = hideOnPlayback

    overrideRGBColors = BoolField(default_value=False)
    ovrgbf = overrideRGBColors

    color = ByteField(default_value=0, min_value=0, max_value=255)
    c = color

    overrideColorRGB = Float3Field(default_value=(0.0, 0.0, 0.0))
    ovrgb = overrideColorRGB

    overrideColorA = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    ovca = overrideColorA
