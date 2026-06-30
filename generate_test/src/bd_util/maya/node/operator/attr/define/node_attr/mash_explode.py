# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class PivotPointsPlugOperator(
    CompoundPlugOperator["PivotPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pivotX"),
        ("pivotY", "pivotY"),
        ("pivotZ", "pivotZ"),
    )

    pivotX = FloatField()

    pivotY = FloatField()

    pivotZ = FloatField()


class PivotPointsAttrOperator(
    CompoundAttrOperator[PivotPointsPlugOperator]
):
    __slots__ = ()

    pivotX = FloatField()

    pivotY = FloatField()

    pivotZ = FloatField()


class PivotPointsField(
    CompoundField[PivotPointsAttrOperator, PivotPointsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotPointsAttrOperator
    PLUG_CLS = PivotPointsPlugOperator

    pivotX = FloatField()

    pivotY = FloatField()

    pivotZ = FloatField()


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "positionInPP"),
        ("scaleInPP", "scaleInPP"),
        ("rotationInPP", "rotationInPP"),
    )

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()
