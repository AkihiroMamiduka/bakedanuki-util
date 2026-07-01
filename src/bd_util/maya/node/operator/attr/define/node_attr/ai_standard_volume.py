# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class ScatterColorPlugOperator(
    Float3CompoundBasePlugOperator["ScatterColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scatterColorR", "scatter_colorr"),
        ("scatterColorG", "scatter_colorg"),
        ("scatterColorB", "scatter_colorb"),
    )

    scatterColorR = FloatField()
    scatter_colorr = scatterColorR

    scatterColorG = FloatField()
    scatter_colorg = scatterColorG

    scatterColorB = FloatField()
    scatter_colorb = scatterColorB


class ScatterColorAttrOperator(
    Float3CompoundBaseAttrOperator[ScatterColorPlugOperator]
):
    __slots__ = ()

    scatterColorR = FloatField()
    scatter_colorr = scatterColorR

    scatterColorG = FloatField()
    scatter_colorg = scatterColorG

    scatterColorB = FloatField()
    scatter_colorb = scatterColorB


class ScatterColorField(
    Float3CompoundBaseField[ScatterColorAttrOperator, ScatterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatterColorAttrOperator
    PLUG_CLS = ScatterColorPlugOperator

    scatterColorR = FloatField()
    scatter_colorr = scatterColorR

    scatterColorG = FloatField()
    scatter_colorg = scatterColorG

    scatterColorB = FloatField()
    scatter_colorb = scatterColorB


class TransparentPlugOperator(
    Float3CompoundBasePlugOperator["TransparentAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparentR", "transparentr"),
        ("transparentG", "transparentg"),
        ("transparentB", "transparentb"),
    )

    transparentR = FloatField()
    transparentr = transparentR

    transparentG = FloatField()
    transparentg = transparentG

    transparentB = FloatField()
    transparentb = transparentB


class TransparentAttrOperator(
    Float3CompoundBaseAttrOperator[TransparentPlugOperator]
):
    __slots__ = ()

    transparentR = FloatField()
    transparentr = transparentR

    transparentG = FloatField()
    transparentg = transparentG

    transparentB = FloatField()
    transparentb = transparentB


class TransparentField(
    Float3CompoundBaseField[TransparentAttrOperator, TransparentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparentAttrOperator
    PLUG_CLS = TransparentPlugOperator

    transparentR = FloatField()
    transparentr = transparentR

    transparentG = FloatField()
    transparentg = transparentG

    transparentB = FloatField()
    transparentb = transparentB


class EmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["EmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emissionColorR", "emission_colorr"),
        ("emissionColorG", "emission_colorg"),
        ("emissionColorB", "emission_colorb"),
    )

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[EmissionColorAttrOperator, EmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField()
    emission_colorr = emissionColorR

    emissionColorG = FloatField()
    emission_colorg = emissionColorG

    emissionColorB = FloatField()
    emission_colorb = emissionColorB


class DisplacementPlugOperator(
    Float3CompoundBasePlugOperator["DisplacementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("displacementX", "displacementx"),
        ("displacementY", "displacementy"),
        ("displacementZ", "displacementz"),
    )

    displacementX = FloatField()
    displacementx = displacementX

    displacementY = FloatField()
    displacementy = displacementY

    displacementZ = FloatField()
    displacementz = displacementZ


class DisplacementAttrOperator(
    Float3CompoundBaseAttrOperator[DisplacementPlugOperator]
):
    __slots__ = ()

    displacementX = FloatField()
    displacementx = displacementX

    displacementY = FloatField()
    displacementy = displacementY

    displacementZ = FloatField()
    displacementz = displacementZ


class DisplacementField(
    Float3CompoundBaseField[DisplacementAttrOperator, DisplacementPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementAttrOperator
    PLUG_CLS = DisplacementPlugOperator

    displacementX = FloatField()
    displacementx = displacementX

    displacementY = FloatField()
    displacementy = displacementY

    displacementZ = FloatField()
    displacementz = displacementZ
