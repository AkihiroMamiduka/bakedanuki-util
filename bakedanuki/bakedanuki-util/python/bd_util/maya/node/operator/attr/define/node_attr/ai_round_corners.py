# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "outx"),
        ("outValueY", "outy"),
        ("outValueZ", "outz"),
    )

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField(default_value=0.0, writable=False)
    outx = outValueX

    outValueY = FloatField(default_value=0.0, writable=False)
    outy = outValueY

    outValueZ = FloatField(default_value=0.0, writable=False)
    outz = outValueZ


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


class NormalPlugOperator(Float3CompoundBasePlugOperator["NormalAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "normalCamerax"),
        ("normalY", "normalCameray"),
        ("normalZ", "normalCameraz"),
    )

    normalX = FloatField(default_value=0.0)
    normalCamerax = normalX

    normalY = FloatField(default_value=0.0)
    normalCameray = normalY

    normalZ = FloatField(default_value=0.0)
    normalCameraz = normalZ


class NormalAttrOperator(Float3CompoundBaseAttrOperator[NormalPlugOperator]):
    __slots__ = ()

    normalX = FloatField(default_value=0.0)
    normalCamerax = normalX

    normalY = FloatField(default_value=0.0)
    normalCameray = normalY

    normalZ = FloatField(default_value=0.0)
    normalCameraz = normalZ


class NormalField(
    Float3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = FloatField(default_value=0.0)
    normalCamerax = normalX

    normalY = FloatField(default_value=0.0)
    normalCameray = normalY

    normalZ = FloatField(default_value=0.0)
    normalCameraz = normalZ
