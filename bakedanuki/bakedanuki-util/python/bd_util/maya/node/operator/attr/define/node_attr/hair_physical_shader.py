# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class RootColorDPlugOperator(
    Float3CompoundBasePlugOperator["RootColorDAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rootColorDR", "rcDr"),
        ("rootColorDG", "rcDg"),
        ("rootColorDB", "rcDb"),
    )

    rootColorDR = FloatField(default_value=0.2070000022649765)
    rcDr = rootColorDR

    rootColorDG = FloatField(default_value=0.1379999965429306)
    rcDg = rootColorDG

    rootColorDB = FloatField(default_value=0.0689999982714653)
    rcDb = rootColorDB


class RootColorDAttrOperator(
    Float3CompoundBaseAttrOperator[RootColorDPlugOperator]
):
    __slots__ = ()

    rootColorDR = FloatField(default_value=0.2070000022649765)
    rcDr = rootColorDR

    rootColorDG = FloatField(default_value=0.1379999965429306)
    rcDg = rootColorDG

    rootColorDB = FloatField(default_value=0.0689999982714653)
    rcDb = rootColorDB


class RootColorDField(
    Float3CompoundBaseField[RootColorDAttrOperator, RootColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RootColorDAttrOperator
    PLUG_CLS = RootColorDPlugOperator

    rootColorDR = FloatField(default_value=0.2070000022649765)
    rcDr = rootColorDR

    rootColorDG = FloatField(default_value=0.1379999965429306)
    rcDg = rootColorDG

    rootColorDB = FloatField(default_value=0.0689999982714653)
    rcDb = rootColorDB


class TipColorDPlugOperator(
    Float3CompoundBasePlugOperator["TipColorDAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tipColorDR", "tcDr"),
        ("tipColorDG", "tcDg"),
        ("tipColorDB", "tcDb"),
    )

    tipColorDR = FloatField(default_value=0.2070000022649765)
    tcDr = tipColorDR

    tipColorDG = FloatField(default_value=0.1379999965429306)
    tcDg = tipColorDG

    tipColorDB = FloatField(default_value=0.0689999982714653)
    tcDb = tipColorDB


class TipColorDAttrOperator(
    Float3CompoundBaseAttrOperator[TipColorDPlugOperator]
):
    __slots__ = ()

    tipColorDR = FloatField(default_value=0.2070000022649765)
    tcDr = tipColorDR

    tipColorDG = FloatField(default_value=0.1379999965429306)
    tcDg = tipColorDG

    tipColorDB = FloatField(default_value=0.0689999982714653)
    tcDb = tipColorDB


class TipColorDField(
    Float3CompoundBaseField[TipColorDAttrOperator, TipColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TipColorDAttrOperator
    PLUG_CLS = TipColorDPlugOperator

    tipColorDR = FloatField(default_value=0.2070000022649765)
    tcDr = tipColorDR

    tipColorDG = FloatField(default_value=0.1379999965429306)
    tcDg = tipColorDG

    tipColorDB = FloatField(default_value=0.0689999982714653)
    tcDb = tipColorDB


class TransparencyPlugOperator(
    Float3CompoundBasePlugOperator["TransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("transparencyR", "transr"),
        ("transparencyG", "transg"),
        ("transparencyB", "transb"),
    )

    transparencyR = FloatField(default_value=0.0)
    transr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    transg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    transb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField(default_value=0.0)
    transr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    transg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    transb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField(default_value=0.0)
    transr = transparencyR

    transparencyG = FloatField(default_value=0.0)
    transg = transparencyG

    transparencyB = FloatField(default_value=0.0)
    transb = transparencyB


class AmbientColorPlugOperator(
    Float3CompoundBasePlugOperator["AmbientColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ambientColorR", "acr"),
        ("ambientColorG", "acg"),
        ("ambientColorB", "acb"),
    )

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField(default_value=0.0)
    acr = ambientColorR

    ambientColorG = FloatField(default_value=0.0)
    acg = ambientColorG

    ambientColorB = FloatField(default_value=0.0)
    acb = ambientColorB


class IncandescencePlugOperator(
    Float3CompoundBasePlugOperator["IncandescenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("incandescenceR", "incandr"),
        ("incandescenceG", "incandg"),
        ("incandescenceB", "incandb"),
    )

    incandescenceR = FloatField(default_value=0.0)
    incandr = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    incandg = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    incandb = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField(default_value=0.0)
    incandr = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    incandg = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    incandb = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField(default_value=0.0)
    incandr = incandescenceR

    incandescenceG = FloatField(default_value=0.0)
    incandg = incandescenceG

    incandescenceB = FloatField(default_value=0.0)
    incandb = incandescenceB


class ColorRPlugOperator(
    Float3CompoundBasePlugOperator["ColorRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRR", "cRr"),
        ("colorRG", "cRg"),
        ("colorRB", "cRb"),
    )

    colorRR = FloatField(default_value=1.0)
    cRr = colorRR

    colorRG = FloatField(default_value=1.0)
    cRg = colorRG

    colorRB = FloatField(default_value=1.0)
    cRb = colorRB


class ColorRAttrOperator(
    Float3CompoundBaseAttrOperator[ColorRPlugOperator]
):
    __slots__ = ()

    colorRR = FloatField(default_value=1.0)
    cRr = colorRR

    colorRG = FloatField(default_value=1.0)
    cRg = colorRG

    colorRB = FloatField(default_value=1.0)
    cRb = colorRB


class ColorRField(
    Float3CompoundBaseField[ColorRAttrOperator, ColorRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRAttrOperator
    PLUG_CLS = ColorRPlugOperator

    colorRR = FloatField(default_value=1.0)
    cRr = colorRR

    colorRG = FloatField(default_value=1.0)
    cRg = colorRG

    colorRB = FloatField(default_value=1.0)
    cRb = colorRB


class ColorTTPlugOperator(
    Float3CompoundBasePlugOperator["ColorTTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorTTR", "cTTr"),
        ("colorTTG", "cTTg"),
        ("colorTTB", "cTTb"),
    )

    colorTTR = FloatField(default_value=1.0)
    cTTr = colorTTR

    colorTTG = FloatField(default_value=1.0)
    cTTg = colorTTG

    colorTTB = FloatField(default_value=1.0)
    cTTb = colorTTB


class ColorTTAttrOperator(
    Float3CompoundBaseAttrOperator[ColorTTPlugOperator]
):
    __slots__ = ()

    colorTTR = FloatField(default_value=1.0)
    cTTr = colorTTR

    colorTTG = FloatField(default_value=1.0)
    cTTg = colorTTG

    colorTTB = FloatField(default_value=1.0)
    cTTb = colorTTB


class ColorTTField(
    Float3CompoundBaseField[ColorTTAttrOperator, ColorTTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorTTAttrOperator
    PLUG_CLS = ColorTTPlugOperator

    colorTTR = FloatField(default_value=1.0)
    cTTr = colorTTR

    colorTTG = FloatField(default_value=1.0)
    cTTg = colorTTG

    colorTTB = FloatField(default_value=1.0)
    cTTb = colorTTB


class ColorTRTPlugOperator(
    Float3CompoundBasePlugOperator["ColorTRTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorTRTR", "cTRTr"),
        ("colorTRTG", "cTRTg"),
        ("colorTRTB", "cTRTb"),
    )

    colorTRTR = FloatField(default_value=0.7250000238418579)
    cTRTr = colorTRTR

    colorTRTG = FloatField(default_value=0.3179999887943268)
    cTRTg = colorTRTG

    colorTRTB = FloatField(default_value=0.11400000005960464)
    cTRTb = colorTRTB


class ColorTRTAttrOperator(
    Float3CompoundBaseAttrOperator[ColorTRTPlugOperator]
):
    __slots__ = ()

    colorTRTR = FloatField(default_value=0.7250000238418579)
    cTRTr = colorTRTR

    colorTRTG = FloatField(default_value=0.3179999887943268)
    cTRTg = colorTRTG

    colorTRTB = FloatField(default_value=0.11400000005960464)
    cTRTb = colorTRTB


class ColorTRTField(
    Float3CompoundBaseField[ColorTRTAttrOperator, ColorTRTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorTRTAttrOperator
    PLUG_CLS = ColorTRTPlugOperator

    colorTRTR = FloatField(default_value=0.7250000238418579)
    cTRTr = colorTRTR

    colorTRTG = FloatField(default_value=0.3179999887943268)
    cTRTg = colorTRTG

    colorTRTB = FloatField(default_value=0.11400000005960464)
    cTRTb = colorTRTB


class ColorGPlugOperator(
    Float3CompoundBasePlugOperator["ColorGAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGR", "cGr"),
        ("colorGG", "cGg"),
        ("colorGB", "cGb"),
    )

    colorGR = FloatField(default_value=0.7250000238418579)
    cGr = colorGR

    colorGG = FloatField(default_value=0.3179999887943268)
    cGg = colorGG

    colorGB = FloatField(default_value=0.11400000005960464)
    cGb = colorGB


class ColorGAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGPlugOperator]
):
    __slots__ = ()

    colorGR = FloatField(default_value=0.7250000238418579)
    cGr = colorGR

    colorGG = FloatField(default_value=0.3179999887943268)
    cGg = colorGG

    colorGB = FloatField(default_value=0.11400000005960464)
    cGb = colorGB


class ColorGField(
    Float3CompoundBaseField[ColorGAttrOperator, ColorGPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGAttrOperator
    PLUG_CLS = ColorGPlugOperator

    colorGR = FloatField(default_value=0.7250000238418579)
    cGr = colorGR

    colorGG = FloatField(default_value=0.3179999887943268)
    cGg = colorGG

    colorGB = FloatField(default_value=0.11400000005960464)
    cGb = colorGB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class ColorDPlugOperator(
    Float3CompoundBasePlugOperator["ColorDAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorDR", "cDr"),
        ("colorDG", "cDg"),
        ("colorDB", "cDb"),
    )

    colorDR = FloatField(default_value=0.2070000022649765)
    cDr = colorDR

    colorDG = FloatField(default_value=0.1379999965429306)
    cDg = colorDG

    colorDB = FloatField(default_value=0.0689999982714653)
    cDb = colorDB


class ColorDAttrOperator(
    Float3CompoundBaseAttrOperator[ColorDPlugOperator]
):
    __slots__ = ()

    colorDR = FloatField(default_value=0.2070000022649765)
    cDr = colorDR

    colorDG = FloatField(default_value=0.1379999965429306)
    cDg = colorDG

    colorDB = FloatField(default_value=0.0689999982714653)
    cDb = colorDB


class ColorDField(
    Float3CompoundBaseField[ColorDAttrOperator, ColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorDAttrOperator
    PLUG_CLS = ColorDPlugOperator

    colorDR = FloatField(default_value=0.2070000022649765)
    cDr = colorDR

    colorDG = FloatField(default_value=0.1379999965429306)
    cDg = colorDG

    colorDB = FloatField(default_value=0.0689999982714653)
    cDb = colorDB
