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

    rootColorDR = FloatField()
    rcDr = rootColorDR

    rootColorDG = FloatField()
    rcDg = rootColorDG

    rootColorDB = FloatField()
    rcDb = rootColorDB


class RootColorDAttrOperator(
    Float3CompoundBaseAttrOperator[RootColorDPlugOperator]
):
    __slots__ = ()

    rootColorDR = FloatField()
    rcDr = rootColorDR

    rootColorDG = FloatField()
    rcDg = rootColorDG

    rootColorDB = FloatField()
    rcDb = rootColorDB


class RootColorDField(
    Float3CompoundBaseField[RootColorDAttrOperator, RootColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RootColorDAttrOperator
    PLUG_CLS = RootColorDPlugOperator

    rootColorDR = FloatField()
    rcDr = rootColorDR

    rootColorDG = FloatField()
    rcDg = rootColorDG

    rootColorDB = FloatField()
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

    tipColorDR = FloatField()
    tcDr = tipColorDR

    tipColorDG = FloatField()
    tcDg = tipColorDG

    tipColorDB = FloatField()
    tcDb = tipColorDB


class TipColorDAttrOperator(
    Float3CompoundBaseAttrOperator[TipColorDPlugOperator]
):
    __slots__ = ()

    tipColorDR = FloatField()
    tcDr = tipColorDR

    tipColorDG = FloatField()
    tcDg = tipColorDG

    tipColorDB = FloatField()
    tcDb = tipColorDB


class TipColorDField(
    Float3CompoundBaseField[TipColorDAttrOperator, TipColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TipColorDAttrOperator
    PLUG_CLS = TipColorDPlugOperator

    tipColorDR = FloatField()
    tcDr = tipColorDR

    tipColorDG = FloatField()
    tcDg = tipColorDG

    tipColorDB = FloatField()
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

    transparencyR = FloatField()
    transr = transparencyR

    transparencyG = FloatField()
    transg = transparencyG

    transparencyB = FloatField()
    transb = transparencyB


class TransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[TransparencyPlugOperator]
):
    __slots__ = ()

    transparencyR = FloatField()
    transr = transparencyR

    transparencyG = FloatField()
    transg = transparencyG

    transparencyB = FloatField()
    transb = transparencyB


class TransparencyField(
    Float3CompoundBaseField[TransparencyAttrOperator, TransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAttrOperator
    PLUG_CLS = TransparencyPlugOperator

    transparencyR = FloatField()
    transr = transparencyR

    transparencyG = FloatField()
    transg = transparencyG

    transparencyB = FloatField()
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

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorAttrOperator(
    Float3CompoundBaseAttrOperator[AmbientColorPlugOperator]
):
    __slots__ = ()

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
    acb = ambientColorB


class AmbientColorField(
    Float3CompoundBaseField[AmbientColorAttrOperator, AmbientColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AmbientColorAttrOperator
    PLUG_CLS = AmbientColorPlugOperator

    ambientColorR = FloatField()
    acr = ambientColorR

    ambientColorG = FloatField()
    acg = ambientColorG

    ambientColorB = FloatField()
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

    incandescenceR = FloatField()
    incandr = incandescenceR

    incandescenceG = FloatField()
    incandg = incandescenceG

    incandescenceB = FloatField()
    incandb = incandescenceB


class IncandescenceAttrOperator(
    Float3CompoundBaseAttrOperator[IncandescencePlugOperator]
):
    __slots__ = ()

    incandescenceR = FloatField()
    incandr = incandescenceR

    incandescenceG = FloatField()
    incandg = incandescenceG

    incandescenceB = FloatField()
    incandb = incandescenceB


class IncandescenceField(
    Float3CompoundBaseField[IncandescenceAttrOperator, IncandescencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceAttrOperator
    PLUG_CLS = IncandescencePlugOperator

    incandescenceR = FloatField()
    incandr = incandescenceR

    incandescenceG = FloatField()
    incandg = incandescenceG

    incandescenceB = FloatField()
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

    colorRR = FloatField()
    cRr = colorRR

    colorRG = FloatField()
    cRg = colorRG

    colorRB = FloatField()
    cRb = colorRB


class ColorRAttrOperator(
    Float3CompoundBaseAttrOperator[ColorRPlugOperator]
):
    __slots__ = ()

    colorRR = FloatField()
    cRr = colorRR

    colorRG = FloatField()
    cRg = colorRG

    colorRB = FloatField()
    cRb = colorRB


class ColorRField(
    Float3CompoundBaseField[ColorRAttrOperator, ColorRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRAttrOperator
    PLUG_CLS = ColorRPlugOperator

    colorRR = FloatField()
    cRr = colorRR

    colorRG = FloatField()
    cRg = colorRG

    colorRB = FloatField()
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

    colorTTR = FloatField()
    cTTr = colorTTR

    colorTTG = FloatField()
    cTTg = colorTTG

    colorTTB = FloatField()
    cTTb = colorTTB


class ColorTTAttrOperator(
    Float3CompoundBaseAttrOperator[ColorTTPlugOperator]
):
    __slots__ = ()

    colorTTR = FloatField()
    cTTr = colorTTR

    colorTTG = FloatField()
    cTTg = colorTTG

    colorTTB = FloatField()
    cTTb = colorTTB


class ColorTTField(
    Float3CompoundBaseField[ColorTTAttrOperator, ColorTTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorTTAttrOperator
    PLUG_CLS = ColorTTPlugOperator

    colorTTR = FloatField()
    cTTr = colorTTR

    colorTTG = FloatField()
    cTTg = colorTTG

    colorTTB = FloatField()
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

    colorTRTR = FloatField()
    cTRTr = colorTRTR

    colorTRTG = FloatField()
    cTRTg = colorTRTG

    colorTRTB = FloatField()
    cTRTb = colorTRTB


class ColorTRTAttrOperator(
    Float3CompoundBaseAttrOperator[ColorTRTPlugOperator]
):
    __slots__ = ()

    colorTRTR = FloatField()
    cTRTr = colorTRTR

    colorTRTG = FloatField()
    cTRTg = colorTRTG

    colorTRTB = FloatField()
    cTRTb = colorTRTB


class ColorTRTField(
    Float3CompoundBaseField[ColorTRTAttrOperator, ColorTRTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorTRTAttrOperator
    PLUG_CLS = ColorTRTPlugOperator

    colorTRTR = FloatField()
    cTRTr = colorTRTR

    colorTRTG = FloatField()
    cTRTg = colorTRTG

    colorTRTB = FloatField()
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

    colorGR = FloatField()
    cGr = colorGR

    colorGG = FloatField()
    cGg = colorGG

    colorGB = FloatField()
    cGb = colorGB


class ColorGAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGPlugOperator]
):
    __slots__ = ()

    colorGR = FloatField()
    cGr = colorGR

    colorGG = FloatField()
    cGg = colorGG

    colorGB = FloatField()
    cGb = colorGB


class ColorGField(
    Float3CompoundBaseField[ColorGAttrOperator, ColorGPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGAttrOperator
    PLUG_CLS = ColorGPlugOperator

    colorGR = FloatField()
    cGr = colorGR

    colorGG = FloatField()
    cGg = colorGG

    colorGB = FloatField()
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

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
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

    colorDR = FloatField()
    cDr = colorDR

    colorDG = FloatField()
    cDg = colorDG

    colorDB = FloatField()
    cDb = colorDB


class ColorDAttrOperator(
    Float3CompoundBaseAttrOperator[ColorDPlugOperator]
):
    __slots__ = ()

    colorDR = FloatField()
    cDr = colorDR

    colorDG = FloatField()
    cDg = colorDG

    colorDB = FloatField()
    cDb = colorDB


class ColorDField(
    Float3CompoundBaseField[ColorDAttrOperator, ColorDPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorDAttrOperator
    PLUG_CLS = ColorDPlugOperator

    colorDR = FloatField()
    cDr = colorDR

    colorDG = FloatField()
    cDg = colorDG

    colorDB = FloatField()
    cDb = colorDB
