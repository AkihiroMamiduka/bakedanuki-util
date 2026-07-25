# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
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
from ..custom.at.scalar_compound.numeric_compound.long_compound.long2_compound._base import (
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
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


class RandomScalePlugOperator(
    Float2CompoundBasePlugOperator["RandomScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randomScale0", "randomScale0"),
        ("randomScale1", "randomScale1"),
    )

    randomScale0 = FloatField(default_value=1.0, min_value=0.0)

    randomScale1 = FloatField(default_value=1.0, min_value=0.0)


class RandomScaleAttrOperator(
    Float2CompoundBaseAttrOperator[RandomScalePlugOperator]
):
    __slots__ = ()

    randomScale0 = FloatField(default_value=1.0, min_value=0.0)

    randomScale1 = FloatField(default_value=1.0, min_value=0.0)


class RandomScaleField(
    Float2CompoundBaseField[RandomScaleAttrOperator, RandomScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomScaleAttrOperator
    PLUG_CLS = RandomScalePlugOperator

    randomScale0 = FloatField(default_value=1.0, min_value=0.0)

    randomScale1 = FloatField(default_value=1.0, min_value=0.0)


class RandomRotationPlugOperator(
    Float3CompoundBasePlugOperator["RandomRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randomRotation0", "randomRotation0"),
        ("randomRotation1", "randomRotation1"),
        ("randomRotation2", "randomRotation2"),
    )

    randomRotation0 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation1 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation2 = FloatField(default_value=0.0, min_value=0.0)


class RandomRotationAttrOperator(
    Float3CompoundBaseAttrOperator[RandomRotationPlugOperator]
):
    __slots__ = ()

    randomRotation0 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation1 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation2 = FloatField(default_value=0.0, min_value=0.0)


class RandomRotationField(
    Float3CompoundBaseField[RandomRotationAttrOperator, RandomRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomRotationAttrOperator
    PLUG_CLS = RandomRotationPlugOperator

    randomRotation0 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation1 = FloatField(default_value=0.0, min_value=0.0)

    randomRotation2 = FloatField(default_value=0.0, min_value=0.0)


class RandomIdPlugOperator(
    Long2CompoundBasePlugOperator["RandomIdAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randomId0", "randomId0"),
        ("randomId1", "randomId1"),
    )

    randomId0 = LongField(default_value=0, min_value=0)

    randomId1 = LongField(default_value=0, min_value=0)


class RandomIdAttrOperator(
    Long2CompoundBaseAttrOperator[RandomIdPlugOperator]
):
    __slots__ = ()

    randomId0 = LongField(default_value=0, min_value=0)

    randomId1 = LongField(default_value=0, min_value=0)


class RandomIdField(
    Long2CompoundBaseField[RandomIdAttrOperator, RandomIdPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomIdAttrOperator
    PLUG_CLS = RandomIdPlugOperator

    randomId0 = LongField(default_value=0, min_value=0)

    randomId1 = LongField(default_value=0, min_value=0)


class PositionAdjustPlugOperator(
    Double3CompoundBasePlugOperator["PositionAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionAdjust0", "positionAdjust0"),
        ("positionAdjust1", "positionAdjust1"),
        ("positionAdjust2", "positionAdjust2"),
    )

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class PositionAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[PositionAdjustPlugOperator]
):
    __slots__ = ()

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class PositionAdjustField(
    Double3CompoundBaseField[PositionAdjustAttrOperator, PositionAdjustPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAdjustAttrOperator
    PLUG_CLS = PositionAdjustPlugOperator

    positionAdjust0 = DoubleField(default_value=0.0)

    positionAdjust1 = DoubleField(default_value=0.0)

    positionAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustPlugOperator(
    Double3CompoundBasePlugOperator["RotationAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationAdjust0", "rotationAdjust0"),
        ("rotationAdjust1", "rotationAdjust1"),
        ("rotationAdjust2", "rotationAdjust2"),
    )

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[RotationAdjustPlugOperator]
):
    __slots__ = ()

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class RotationAdjustField(
    Double3CompoundBaseField[RotationAdjustAttrOperator, RotationAdjustPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationAdjustAttrOperator
    PLUG_CLS = RotationAdjustPlugOperator

    rotationAdjust0 = DoubleField(default_value=0.0)

    rotationAdjust1 = DoubleField(default_value=0.0)

    rotationAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustPlugOperator(
    Double3CompoundBasePlugOperator["ScaleAdjustAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleAdjust0", "scaleAdjust0"),
        ("scaleAdjust1", "scaleAdjust1"),
        ("scaleAdjust2", "scaleAdjust2"),
    )

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustAttrOperator(
    Double3CompoundBaseAttrOperator[ScaleAdjustPlugOperator]
):
    __slots__ = ()

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)


class ScaleAdjustField(
    Double3CompoundBaseField[ScaleAdjustAttrOperator, ScaleAdjustPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAdjustAttrOperator
    PLUG_CLS = ScaleAdjustPlugOperator

    scaleAdjust0 = DoubleField(default_value=0.0)

    scaleAdjust1 = DoubleField(default_value=0.0)

    scaleAdjust2 = DoubleField(default_value=0.0)
