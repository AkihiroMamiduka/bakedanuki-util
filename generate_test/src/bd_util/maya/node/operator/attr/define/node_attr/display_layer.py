# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.byte import ByteField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class DrawInfoPlugOperator(
    CompoundPlugOperator["DrawInfoAttrOperator"]
):
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

    displayType = EnumField()
    dt = displayType

    levelOfDetail = EnumField()
    lod = levelOfDetail

    shading = BoolField()
    s = shading

    texturing = BoolField()
    t = texturing

    playback = BoolField()
    p = playback

    enabled = BoolField()
    e = enabled

    visibility = BoolField()
    v = visibility

    hideOnPlayback = BoolField()
    hpb = hideOnPlayback

    overrideRGBColors = BoolField()
    ovrgbf = overrideRGBColors

    color = ByteField()
    c = color

    overrideColorRGB = Float3Field()
    ovrgb = overrideColorRGB

    overrideColorA = FloatField()
    ovca = overrideColorA


class DrawInfoAttrOperator(
    CompoundAttrOperator[DrawInfoPlugOperator]
):
    __slots__ = ()

    displayType = EnumField()
    dt = displayType

    levelOfDetail = EnumField()
    lod = levelOfDetail

    shading = BoolField()
    s = shading

    texturing = BoolField()
    t = texturing

    playback = BoolField()
    p = playback

    enabled = BoolField()
    e = enabled

    visibility = BoolField()
    v = visibility

    hideOnPlayback = BoolField()
    hpb = hideOnPlayback

    overrideRGBColors = BoolField()
    ovrgbf = overrideRGBColors

    color = ByteField()
    c = color

    overrideColorRGB = Float3Field()
    ovrgb = overrideColorRGB

    overrideColorA = FloatField()
    ovca = overrideColorA


class DrawInfoField(
    CompoundField[DrawInfoAttrOperator, DrawInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawInfoAttrOperator
    PLUG_CLS = DrawInfoPlugOperator

    displayType = EnumField()
    dt = displayType

    levelOfDetail = EnumField()
    lod = levelOfDetail

    shading = BoolField()
    s = shading

    texturing = BoolField()
    t = texturing

    playback = BoolField()
    p = playback

    enabled = BoolField()
    e = enabled

    visibility = BoolField()
    v = visibility

    hideOnPlayback = BoolField()
    hpb = hideOnPlayback

    overrideRGBColors = BoolField()
    ovrgbf = overrideRGBColors

    color = ByteField()
    c = color

    overrideColorRGB = Float3Field()
    ovrgb = overrideColorRGB

    overrideColorA = FloatField()
    ovca = overrideColorA
