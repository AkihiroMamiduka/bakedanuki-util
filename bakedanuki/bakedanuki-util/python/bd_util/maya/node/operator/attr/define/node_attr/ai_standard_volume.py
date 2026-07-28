# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
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

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
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

    scatterColorR = FloatField(default_value=0.5)
    scatter_colorr = scatterColorR

    scatterColorG = FloatField(default_value=0.5)
    scatter_colorg = scatterColorG

    scatterColorB = FloatField(default_value=0.5)
    scatter_colorb = scatterColorB


class ScatterColorAttrOperator(
    Float3CompoundBaseAttrOperator[ScatterColorPlugOperator]
):
    __slots__ = ()

    scatterColorR = FloatField(default_value=0.5)
    scatter_colorr = scatterColorR

    scatterColorG = FloatField(default_value=0.5)
    scatter_colorg = scatterColorG

    scatterColorB = FloatField(default_value=0.5)
    scatter_colorb = scatterColorB


class ScatterColorField(
    Float3CompoundBaseField[ScatterColorAttrOperator, ScatterColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScatterColorAttrOperator
    PLUG_CLS = ScatterColorPlugOperator

    scatterColorR = FloatField(default_value=0.5)
    scatter_colorr = scatterColorR

    scatterColorG = FloatField(default_value=0.5)
    scatter_colorg = scatterColorG

    scatterColorB = FloatField(default_value=0.5)
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

    transparentR = FloatField(default_value=0.3678794503211975)
    transparentr = transparentR

    transparentG = FloatField(default_value=0.3678794503211975)
    transparentg = transparentG

    transparentB = FloatField(default_value=0.3678794503211975)
    transparentb = transparentB


class TransparentAttrOperator(
    Float3CompoundBaseAttrOperator[TransparentPlugOperator]
):
    __slots__ = ()

    transparentR = FloatField(default_value=0.3678794503211975)
    transparentr = transparentR

    transparentG = FloatField(default_value=0.3678794503211975)
    transparentg = transparentG

    transparentB = FloatField(default_value=0.3678794503211975)
    transparentb = transparentB


class TransparentField(
    Float3CompoundBaseField[TransparentAttrOperator, TransparentPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparentAttrOperator
    PLUG_CLS = TransparentPlugOperator

    transparentR = FloatField(default_value=0.3678794503211975)
    transparentr = transparentR

    transparentG = FloatField(default_value=0.3678794503211975)
    transparentg = transparentG

    transparentB = FloatField(default_value=0.3678794503211975)
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

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[EmissionColorPlugOperator]
):
    __slots__ = ()

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
    emission_colorb = emissionColorB


class EmissionColorField(
    Float3CompoundBaseField[
        EmissionColorAttrOperator, EmissionColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EmissionColorAttrOperator
    PLUG_CLS = EmissionColorPlugOperator

    emissionColorR = FloatField(default_value=1.0)
    emission_colorr = emissionColorR

    emissionColorG = FloatField(default_value=1.0)
    emission_colorg = emissionColorG

    emissionColorB = FloatField(default_value=1.0)
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

    displacementX = FloatField(default_value=0.0)
    displacementx = displacementX

    displacementY = FloatField(default_value=0.0)
    displacementy = displacementY

    displacementZ = FloatField(default_value=0.0)
    displacementz = displacementZ


class DisplacementAttrOperator(
    Float3CompoundBaseAttrOperator[DisplacementPlugOperator]
):
    __slots__ = ()

    displacementX = FloatField(default_value=0.0)
    displacementx = displacementX

    displacementY = FloatField(default_value=0.0)
    displacementy = displacementY

    displacementZ = FloatField(default_value=0.0)
    displacementz = displacementZ


class DisplacementField(
    Float3CompoundBaseField[DisplacementAttrOperator, DisplacementPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplacementAttrOperator
    PLUG_CLS = DisplacementPlugOperator

    displacementX = FloatField(default_value=0.0)
    displacementx = displacementX

    displacementY = FloatField(default_value=0.0)
    displacementy = displacementY

    displacementZ = FloatField(default_value=0.0)
    displacementz = displacementZ
