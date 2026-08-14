# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
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


class MColourAttrOperator(Float3CompoundBaseAttrOperator[MColourPlugOperator]):
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


class AxillaryInPPPlugOperator(
    CompoundPlugOperator["AxillaryInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorInPP", "colorInPP"),
        ("uvTileInPP", "uvTileInPP"),
        ("frameInPP", "frameInPP"),
        ("isAnimatedInPP", "isAnimatedInPP"),
        ("velocityInPP", "velocityInPP"),
        ("velocityVecInPP", "velocityVecInPP"),
        ("angularVelocityInPP", "angularVelocityInPP"),
        ("angularVelocityVecInPP", "angularVelocityVecInPP"),
        ("calculatedStrength", "calculatedStrength"),
    )

    colorInPP = DataVectorArrayField()

    uvTileInPP = DataVectorArrayField()

    frameInPP = DataDoubleArrayField()

    isAnimatedInPP = TypedField()

    velocityInPP = DataDoubleArrayField()

    velocityVecInPP = DataVectorArrayField()

    angularVelocityInPP = DataDoubleArrayField()

    angularVelocityVecInPP = DataVectorArrayField()

    calculatedStrength = DataVectorArrayField()


class AxillaryInPPAttrOperator(CompoundAttrOperator[AxillaryInPPPlugOperator]):
    __slots__ = ()

    colorInPP = DataVectorArrayField()

    uvTileInPP = DataVectorArrayField()

    frameInPP = DataDoubleArrayField()

    isAnimatedInPP = TypedField()

    velocityInPP = DataDoubleArrayField()

    velocityVecInPP = DataVectorArrayField()

    angularVelocityInPP = DataDoubleArrayField()

    angularVelocityVecInPP = DataVectorArrayField()

    calculatedStrength = DataVectorArrayField()


class AxillaryInPPField(
    CompoundField[AxillaryInPPAttrOperator, AxillaryInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxillaryInPPAttrOperator
    PLUG_CLS = AxillaryInPPPlugOperator

    colorInPP = DataVectorArrayField()

    uvTileInPP = DataVectorArrayField()

    frameInPP = DataDoubleArrayField()

    isAnimatedInPP = TypedField()

    velocityInPP = DataDoubleArrayField()

    velocityVecInPP = DataVectorArrayField()

    angularVelocityInPP = DataDoubleArrayField()

    angularVelocityVecInPP = DataVectorArrayField()

    calculatedStrength = DataVectorArrayField()


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


class AxillaryOutPPPlugOperator(
    CompoundPlugOperator["AxillaryOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorOutPP", "colorOutPP"),
        ("uvTileOutPP", "uvTileOutPP"),
        ("frameOutPP", "frameOutPP"),
        ("isAnimatedOutPP", "isAnimatedOutPP"),
        ("velocityOutPP", "velocityOutPP"),
        ("velocityVecOutPP", "velocityVecOutPP"),
        ("angularVelocityOutPP", "angularVelocityOutPP"),
        ("angularVelocityVecOutPP", "angularVelocityVecOutPP"),
    )

    colorOutPP = DataVectorArrayField()

    uvTileOutPP = DataVectorArrayField()

    frameOutPP = DataDoubleArrayField()

    isAnimatedOutPP = TypedField()

    velocityOutPP = DataDoubleArrayField()

    velocityVecOutPP = DataVectorArrayField()

    angularVelocityOutPP = DataDoubleArrayField()

    angularVelocityVecOutPP = DataVectorArrayField()


class AxillaryOutPPAttrOperator(
    CompoundAttrOperator[AxillaryOutPPPlugOperator]
):
    __slots__ = ()

    colorOutPP = DataVectorArrayField()

    uvTileOutPP = DataVectorArrayField()

    frameOutPP = DataDoubleArrayField()

    isAnimatedOutPP = TypedField()

    velocityOutPP = DataDoubleArrayField()

    velocityVecOutPP = DataVectorArrayField()

    angularVelocityOutPP = DataDoubleArrayField()

    angularVelocityVecOutPP = DataVectorArrayField()


class AxillaryOutPPField(
    CompoundField[AxillaryOutPPAttrOperator, AxillaryOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxillaryOutPPAttrOperator
    PLUG_CLS = AxillaryOutPPPlugOperator

    colorOutPP = DataVectorArrayField()

    uvTileOutPP = DataVectorArrayField()

    frameOutPP = DataDoubleArrayField()

    isAnimatedOutPP = TypedField()

    velocityOutPP = DataDoubleArrayField()

    velocityVecOutPP = DataVectorArrayField()

    angularVelocityOutPP = DataDoubleArrayField()

    angularVelocityVecOutPP = DataVectorArrayField()
