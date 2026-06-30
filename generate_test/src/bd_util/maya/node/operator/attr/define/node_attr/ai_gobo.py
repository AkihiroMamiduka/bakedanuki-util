# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class SlidemapPlugOperator(
    Float3CompoundBasePlugOperator["SlidemapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("slidemapR", "slidemapr"),
        ("slidemapG", "slidemapg"),
        ("slidemapB", "slidemapb"),
    )

    slidemapR = FloatField()
    slidemapr = slidemapR

    slidemapG = FloatField()
    slidemapg = slidemapG

    slidemapB = FloatField()
    slidemapb = slidemapB


class SlidemapAttrOperator(
    Float3CompoundBaseAttrOperator[SlidemapPlugOperator]
):
    __slots__ = ()

    slidemapR = FloatField()
    slidemapr = slidemapR

    slidemapG = FloatField()
    slidemapg = slidemapG

    slidemapB = FloatField()
    slidemapb = slidemapB


class SlidemapField(
    Float3CompoundBaseField[SlidemapAttrOperator, SlidemapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SlidemapAttrOperator
    PLUG_CLS = SlidemapPlugOperator

    slidemapR = FloatField()
    slidemapr = slidemapR

    slidemapG = FloatField()
    slidemapg = slidemapG

    slidemapB = FloatField()
    slidemapb = slidemapB


class OffsetPlugOperator(
    Float2CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
    )

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY


class OffsetAttrOperator(
    Float2CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY
