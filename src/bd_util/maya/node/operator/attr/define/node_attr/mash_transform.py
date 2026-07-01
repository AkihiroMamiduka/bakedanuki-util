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


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionInPP", "positionInPP"),
        ("scaleInPP", "scaleInPP"),
        ("rotationInPP", "rotationInPP"),
        ("idInPP", "idInPP"),
        ("visibilityInPP", "visibilityInPP"),
    )

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    positionInPP = DataVectorArrayField()

    scaleInPP = DataVectorArrayField()

    rotationInPP = DataVectorArrayField()

    idInPP = DataVectorArrayField()

    visibilityInPP = DataVectorArrayField()


class TranslateOutPPPlugOperator(
    CompoundPlugOperator["TranslateOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOutPP", "positionOutPP"),
        ("scaleOutPP", "scaleOutPP"),
        ("rotationOutPP", "rotationOutPP"),
        ("idOutPP", "idOutPP"),
        ("visibilityOutPP", "visibilityOutPP"),
    )

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class TranslateOutPPAttrOperator(
    CompoundAttrOperator[TranslateOutPPPlugOperator]
):
    __slots__ = ()

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class TranslateOutPPField(
    CompoundField[TranslateOutPPAttrOperator, TranslateOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateOutPPAttrOperator
    PLUG_CLS = TranslateOutPPPlugOperator

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()

    idOutPP = DataVectorArrayField()

    visibilityOutPP = DataVectorArrayField()


class ScaleAmountPlugOperator(
    Float3CompoundBasePlugOperator["ScaleAmountAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleAmount0", "scaleAmount0"),
        ("scaleAmount1", "scaleAmount1"),
        ("scaleAmount2", "scaleAmount2"),
    )

    scaleAmount0 = FloatField()

    scaleAmount1 = FloatField()

    scaleAmount2 = FloatField()


class ScaleAmountAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleAmountPlugOperator]
):
    __slots__ = ()

    scaleAmount0 = FloatField()

    scaleAmount1 = FloatField()

    scaleAmount2 = FloatField()


class ScaleAmountField(
    Float3CompoundBaseField[ScaleAmountAttrOperator, ScaleAmountPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAmountAttrOperator
    PLUG_CLS = ScaleAmountPlugOperator

    scaleAmount0 = FloatField()

    scaleAmount1 = FloatField()

    scaleAmount2 = FloatField()


class RotationAmountPlugOperator(
    Float3CompoundBasePlugOperator["RotationAmountAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationAmount0", "rotationAmount0"),
        ("rotationAmount1", "rotationAmount1"),
        ("rotationAmount2", "rotationAmount2"),
    )

    rotationAmount0 = FloatField()

    rotationAmount1 = FloatField()

    rotationAmount2 = FloatField()


class RotationAmountAttrOperator(
    Float3CompoundBaseAttrOperator[RotationAmountPlugOperator]
):
    __slots__ = ()

    rotationAmount0 = FloatField()

    rotationAmount1 = FloatField()

    rotationAmount2 = FloatField()


class RotationAmountField(
    Float3CompoundBaseField[RotationAmountAttrOperator, RotationAmountPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationAmountAttrOperator
    PLUG_CLS = RotationAmountPlugOperator

    rotationAmount0 = FloatField()

    rotationAmount1 = FloatField()

    rotationAmount2 = FloatField()


class PositionAmountPlugOperator(
    Float3CompoundBasePlugOperator["PositionAmountAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionAmount0", "positionAmount0"),
        ("positionAmount1", "positionAmount1"),
        ("positionAmount2", "positionAmount2"),
    )

    positionAmount0 = FloatField()

    positionAmount1 = FloatField()

    positionAmount2 = FloatField()


class PositionAmountAttrOperator(
    Float3CompoundBaseAttrOperator[PositionAmountPlugOperator]
):
    __slots__ = ()

    positionAmount0 = FloatField()

    positionAmount1 = FloatField()

    positionAmount2 = FloatField()


class PositionAmountField(
    Float3CompoundBaseField[PositionAmountAttrOperator, PositionAmountPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAmountAttrOperator
    PLUG_CLS = PositionAmountPlugOperator

    positionAmount0 = FloatField()

    positionAmount1 = FloatField()

    positionAmount2 = FloatField()


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ
