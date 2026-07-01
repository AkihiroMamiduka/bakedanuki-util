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


class CentreOfSymmetryPlugOperator(
    Float3CompoundBasePlugOperator["CentreOfSymmetryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centreOfSymmetry0", "centreOfSymmetry0"),
        ("centreOfSymmetry1", "centreOfSymmetry1"),
        ("centreOfSymmetry2", "centreOfSymmetry2"),
    )

    centreOfSymmetry0 = FloatField()

    centreOfSymmetry1 = FloatField()

    centreOfSymmetry2 = FloatField()


class CentreOfSymmetryAttrOperator(
    Float3CompoundBaseAttrOperator[CentreOfSymmetryPlugOperator]
):
    __slots__ = ()

    centreOfSymmetry0 = FloatField()

    centreOfSymmetry1 = FloatField()

    centreOfSymmetry2 = FloatField()


class CentreOfSymmetryField(
    Float3CompoundBaseField[CentreOfSymmetryAttrOperator, CentreOfSymmetryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CentreOfSymmetryAttrOperator
    PLUG_CLS = CentreOfSymmetryPlugOperator

    centreOfSymmetry0 = FloatField()

    centreOfSymmetry1 = FloatField()

    centreOfSymmetry2 = FloatField()


class ReflectionVectorPlugOperator(
    Float3CompoundBasePlugOperator["ReflectionVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reflectionVector0", "reflectionVector0"),
        ("reflectionVector1", "reflectionVector1"),
        ("reflectionVector2", "reflectionVector2"),
    )

    reflectionVector0 = FloatField()

    reflectionVector1 = FloatField()

    reflectionVector2 = FloatField()


class ReflectionVectorAttrOperator(
    Float3CompoundBaseAttrOperator[ReflectionVectorPlugOperator]
):
    __slots__ = ()

    reflectionVector0 = FloatField()

    reflectionVector1 = FloatField()

    reflectionVector2 = FloatField()


class ReflectionVectorField(
    Float3CompoundBaseField[ReflectionVectorAttrOperator, ReflectionVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReflectionVectorAttrOperator
    PLUG_CLS = ReflectionVectorPlugOperator

    reflectionVector0 = FloatField()

    reflectionVector1 = FloatField()

    reflectionVector2 = FloatField()


class OffsetPositionPlugOperator(
    Float3CompoundBasePlugOperator["OffsetPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetPosition0", "offsetPosition0"),
        ("offsetPosition1", "offsetPosition1"),
        ("offsetPosition2", "offsetPosition2"),
    )

    offsetPosition0 = FloatField()

    offsetPosition1 = FloatField()

    offsetPosition2 = FloatField()


class OffsetPositionAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPositionPlugOperator]
):
    __slots__ = ()

    offsetPosition0 = FloatField()

    offsetPosition1 = FloatField()

    offsetPosition2 = FloatField()


class OffsetPositionField(
    Float3CompoundBaseField[OffsetPositionAttrOperator, OffsetPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetPositionAttrOperator
    PLUG_CLS = OffsetPositionPlugOperator

    offsetPosition0 = FloatField()

    offsetPosition1 = FloatField()

    offsetPosition2 = FloatField()


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
