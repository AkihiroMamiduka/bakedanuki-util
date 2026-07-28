# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InColorPlugOperator(
    Float3CompoundBasePlugOperator["InColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inColorR", "_icr"),
        ("inColorG", "_icg"),
        ("inColorB", "_icb"),
    )

    inColorR = FloatField(default_value=0.30000001192092896)
    icr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    icg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
    icb = inColorB


class InColorAttrOperator(Float3CompoundBaseAttrOperator[InColorPlugOperator]):
    __slots__ = ()

    inColorR = FloatField(default_value=0.30000001192092896)
    icr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    icg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
    icb = inColorB


class InColorField(
    Float3CompoundBaseField[InColorAttrOperator, InColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InColorAttrOperator
    PLUG_CLS = InColorPlugOperator

    inColorR = FloatField(default_value=0.30000001192092896)
    icr = inColorR

    inColorG = FloatField(default_value=0.30000001192092896)
    icg = inColorG

    inColorB = FloatField(default_value=0.30000001192092896)
    icb = inColorB


class MaskPlugOperator(Float3CompoundBasePlugOperator["MaskAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maskR", "_mr"),
        ("maskG", "_mg"),
        ("maskB", "_mb"),
    )

    maskR = FloatField(default_value=0.0)
    mr = maskR

    maskG = FloatField(default_value=0.0)
    mg = maskG

    maskB = FloatField(default_value=0.0)
    mb = maskB


class MaskAttrOperator(Float3CompoundBaseAttrOperator[MaskPlugOperator]):
    __slots__ = ()

    maskR = FloatField(default_value=0.0)
    mr = maskR

    maskG = FloatField(default_value=0.0)
    mg = maskG

    maskB = FloatField(default_value=0.0)
    mb = maskB


class MaskField(Float3CompoundBaseField[MaskAttrOperator, MaskPlugOperator]):
    __slots__ = ()

    ATTR_CLS = MaskAttrOperator
    PLUG_CLS = MaskPlugOperator

    maskR = FloatField(default_value=0.0)
    mr = maskR

    maskG = FloatField(default_value=0.0)
    mg = maskG

    maskB = FloatField(default_value=0.0)
    mb = maskB


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
