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

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField(default_value=1.0)
    mcr = mColourR

    mColourG = FloatField(default_value=1.0)
    mcg = mColourG

    mColourB = FloatField(default_value=1.0)
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

    pivotX = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotY = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotZ = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)


class PivotPointsAttrOperator(
    CompoundAttrOperator[PivotPointsPlugOperator]
):
    __slots__ = ()

    pivotX = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotY = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotZ = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)


class PivotPointsField(
    CompoundField[PivotPointsAttrOperator, PivotPointsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotPointsAttrOperator
    PLUG_CLS = PivotPointsPlugOperator

    pivotX = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotY = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    pivotZ = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)


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
