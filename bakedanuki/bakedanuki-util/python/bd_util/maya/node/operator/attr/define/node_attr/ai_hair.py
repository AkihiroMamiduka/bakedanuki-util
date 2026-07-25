# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
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


class RootcolorPlugOperator(
    Float3CompoundBasePlugOperator["RootcolorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rootcolorR", "rootcolorr"),
        ("rootcolorG", "rootcolorg"),
        ("rootcolorB", "rootcolorb"),
    )

    rootcolorR = FloatField(default_value=0.10000000149011612)
    rootcolorr = rootcolorR

    rootcolorG = FloatField(default_value=0.10000000149011612)
    rootcolorg = rootcolorG

    rootcolorB = FloatField(default_value=0.10000000149011612)
    rootcolorb = rootcolorB


class RootcolorAttrOperator(
    Float3CompoundBaseAttrOperator[RootcolorPlugOperator]
):
    __slots__ = ()

    rootcolorR = FloatField(default_value=0.10000000149011612)
    rootcolorr = rootcolorR

    rootcolorG = FloatField(default_value=0.10000000149011612)
    rootcolorg = rootcolorG

    rootcolorB = FloatField(default_value=0.10000000149011612)
    rootcolorb = rootcolorB


class RootcolorField(
    Float3CompoundBaseField[RootcolorAttrOperator, RootcolorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RootcolorAttrOperator
    PLUG_CLS = RootcolorPlugOperator

    rootcolorR = FloatField(default_value=0.10000000149011612)
    rootcolorr = rootcolorR

    rootcolorG = FloatField(default_value=0.10000000149011612)
    rootcolorg = rootcolorG

    rootcolorB = FloatField(default_value=0.10000000149011612)
    rootcolorb = rootcolorB


class TipcolorPlugOperator(
    Float3CompoundBasePlugOperator["TipcolorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tipcolorR", "tipcolorr"),
        ("tipcolorG", "tipcolorg"),
        ("tipcolorB", "tipcolorb"),
    )

    tipcolorR = FloatField(default_value=0.5)
    tipcolorr = tipcolorR

    tipcolorG = FloatField(default_value=0.5)
    tipcolorg = tipcolorG

    tipcolorB = FloatField(default_value=0.5)
    tipcolorb = tipcolorB


class TipcolorAttrOperator(
    Float3CompoundBaseAttrOperator[TipcolorPlugOperator]
):
    __slots__ = ()

    tipcolorR = FloatField(default_value=0.5)
    tipcolorr = tipcolorR

    tipcolorG = FloatField(default_value=0.5)
    tipcolorg = tipcolorG

    tipcolorB = FloatField(default_value=0.5)
    tipcolorb = tipcolorB


class TipcolorField(
    Float3CompoundBaseField[TipcolorAttrOperator, TipcolorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TipcolorAttrOperator
    PLUG_CLS = TipcolorPlugOperator

    tipcolorR = FloatField(default_value=0.5)
    tipcolorr = tipcolorR

    tipcolorG = FloatField(default_value=0.5)
    tipcolorg = tipcolorG

    tipcolorB = FloatField(default_value=0.5)
    tipcolorb = tipcolorB


class OpacityPlugOperator(
    Float3CompoundBasePlugOperator["OpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("opacityR", "opacityr"),
        ("opacityG", "opacityg"),
        ("opacityB", "opacityb"),
    )

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class OpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OpacityPlugOperator]
):
    __slots__ = ()

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class OpacityField(
    Float3CompoundBaseField[OpacityAttrOperator, OpacityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityAttrOperator
    PLUG_CLS = OpacityPlugOperator

    opacityR = FloatField(default_value=1.0)
    opacityr = opacityR

    opacityG = FloatField(default_value=1.0)
    opacityg = opacityG

    opacityB = FloatField(default_value=1.0)
    opacityb = opacityB


class SpecColorPlugOperator(
    Float3CompoundBasePlugOperator["SpecColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("specColorR", "spec_colorr"),
        ("specColorG", "spec_colorg"),
        ("specColorB", "spec_colorb"),
    )

    specColorR = FloatField(default_value=1.0)
    spec_colorr = specColorR

    specColorG = FloatField(default_value=1.0)
    spec_colorg = specColorG

    specColorB = FloatField(default_value=1.0)
    spec_colorb = specColorB


class SpecColorAttrOperator(
    Float3CompoundBaseAttrOperator[SpecColorPlugOperator]
):
    __slots__ = ()

    specColorR = FloatField(default_value=1.0)
    spec_colorr = specColorR

    specColorG = FloatField(default_value=1.0)
    spec_colorg = specColorG

    specColorB = FloatField(default_value=1.0)
    spec_colorb = specColorB


class SpecColorField(
    Float3CompoundBaseField[SpecColorAttrOperator, SpecColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpecColorAttrOperator
    PLUG_CLS = SpecColorPlugOperator

    specColorR = FloatField(default_value=1.0)
    spec_colorr = specColorR

    specColorG = FloatField(default_value=1.0)
    spec_colorg = specColorG

    specColorB = FloatField(default_value=1.0)
    spec_colorb = specColorB


class Spec2ColorPlugOperator(
    Float3CompoundBasePlugOperator["Spec2ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spec2ColorR", "spec2_colorr"),
        ("spec2ColorG", "spec2_colorg"),
        ("spec2ColorB", "spec2_colorb"),
    )

    spec2ColorR = FloatField(default_value=1.0)
    spec2_colorr = spec2ColorR

    spec2ColorG = FloatField(default_value=0.4000000059604645)
    spec2_colorg = spec2ColorG

    spec2ColorB = FloatField(default_value=0.10000000149011612)
    spec2_colorb = spec2ColorB


class Spec2ColorAttrOperator(
    Float3CompoundBaseAttrOperator[Spec2ColorPlugOperator]
):
    __slots__ = ()

    spec2ColorR = FloatField(default_value=1.0)
    spec2_colorr = spec2ColorR

    spec2ColorG = FloatField(default_value=0.4000000059604645)
    spec2_colorg = spec2ColorG

    spec2ColorB = FloatField(default_value=0.10000000149011612)
    spec2_colorb = spec2ColorB


class Spec2ColorField(
    Float3CompoundBaseField[Spec2ColorAttrOperator, Spec2ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spec2ColorAttrOperator
    PLUG_CLS = Spec2ColorPlugOperator

    spec2ColorR = FloatField(default_value=1.0)
    spec2_colorr = spec2ColorR

    spec2ColorG = FloatField(default_value=0.4000000059604645)
    spec2_colorg = spec2ColorG

    spec2ColorB = FloatField(default_value=0.10000000149011612)
    spec2_colorb = spec2ColorB


class TransmissionColorPlugOperator(
    Float3CompoundBasePlugOperator["TransmissionColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transmissionColorR", "transmission_colorr"),
        ("transmissionColorG", "transmission_colorg"),
        ("transmissionColorB", "transmission_colorb"),
    )

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=0.4000000059604645)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=0.10000000149011612)
    transmission_colorb = transmissionColorB


class TransmissionColorAttrOperator(
    Float3CompoundBaseAttrOperator[TransmissionColorPlugOperator]
):
    __slots__ = ()

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=0.4000000059604645)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=0.10000000149011612)
    transmission_colorb = transmissionColorB


class TransmissionColorField(
    Float3CompoundBaseField[TransmissionColorAttrOperator, TransmissionColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransmissionColorAttrOperator
    PLUG_CLS = TransmissionColorPlugOperator

    transmissionColorR = FloatField(default_value=1.0)
    transmission_colorr = transmissionColorR

    transmissionColorG = FloatField(default_value=0.4000000059604645)
    transmission_colorg = transmissionColorG

    transmissionColorB = FloatField(default_value=0.10000000149011612)
    transmission_colorb = transmissionColorB


class AiMatteColorPlugOperator(
    Float3CompoundBasePlugOperator["AiMatteColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiMatteColorR", "ai_matte_colorr"),
        ("aiMatteColorG", "ai_matte_colorg"),
        ("aiMatteColorB", "ai_matte_colorb"),
    )

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB


class AiMatteColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiMatteColorPlugOperator]
):
    __slots__ = ()

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB


class AiMatteColorField(
    Float3CompoundBaseField[AiMatteColorAttrOperator, AiMatteColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiMatteColorAttrOperator
    PLUG_CLS = AiMatteColorPlugOperator

    aiMatteColorR = FloatField(default_value=0.0)
    ai_matte_colorr = aiMatteColorR

    aiMatteColorG = FloatField(default_value=0.0)
    ai_matte_colorg = aiMatteColorG

    aiMatteColorB = FloatField(default_value=0.0)
    ai_matte_colorb = aiMatteColorB
