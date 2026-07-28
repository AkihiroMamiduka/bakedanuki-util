# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
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

    scaleAmount0 = FloatField(default_value=1.0)

    scaleAmount1 = FloatField(default_value=1.0)

    scaleAmount2 = FloatField(default_value=1.0)


class ScaleAmountAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleAmountPlugOperator]
):
    __slots__ = ()

    scaleAmount0 = FloatField(default_value=1.0)

    scaleAmount1 = FloatField(default_value=1.0)

    scaleAmount2 = FloatField(default_value=1.0)


class ScaleAmountField(
    Float3CompoundBaseField[ScaleAmountAttrOperator, ScaleAmountPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAmountAttrOperator
    PLUG_CLS = ScaleAmountPlugOperator

    scaleAmount0 = FloatField(default_value=1.0)

    scaleAmount1 = FloatField(default_value=1.0)

    scaleAmount2 = FloatField(default_value=1.0)


class RotationAmountPlugOperator(
    Float3CompoundBasePlugOperator["RotationAmountAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationAmount0", "rotationAmount0"),
        ("rotationAmount1", "rotationAmount1"),
        ("rotationAmount2", "rotationAmount2"),
    )

    rotationAmount0 = FloatField(default_value=0.0)

    rotationAmount1 = FloatField(default_value=0.0)

    rotationAmount2 = FloatField(default_value=0.0)


class RotationAmountAttrOperator(
    Float3CompoundBaseAttrOperator[RotationAmountPlugOperator]
):
    __slots__ = ()

    rotationAmount0 = FloatField(default_value=0.0)

    rotationAmount1 = FloatField(default_value=0.0)

    rotationAmount2 = FloatField(default_value=0.0)


class RotationAmountField(
    Float3CompoundBaseField[
        RotationAmountAttrOperator, RotationAmountPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationAmountAttrOperator
    PLUG_CLS = RotationAmountPlugOperator

    rotationAmount0 = FloatField(default_value=0.0)

    rotationAmount1 = FloatField(default_value=0.0)

    rotationAmount2 = FloatField(default_value=0.0)


class PositionAmountPlugOperator(
    Float3CompoundBasePlugOperator["PositionAmountAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionAmount0", "positionAmount0"),
        ("positionAmount1", "positionAmount1"),
        ("positionAmount2", "positionAmount2"),
    )

    positionAmount0 = FloatField(default_value=0.0)

    positionAmount1 = FloatField(default_value=0.0)

    positionAmount2 = FloatField(default_value=0.0)


class PositionAmountAttrOperator(
    Float3CompoundBaseAttrOperator[PositionAmountPlugOperator]
):
    __slots__ = ()

    positionAmount0 = FloatField(default_value=0.0)

    positionAmount1 = FloatField(default_value=0.0)

    positionAmount2 = FloatField(default_value=0.0)


class PositionAmountField(
    Float3CompoundBaseField[
        PositionAmountAttrOperator, PositionAmountPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PositionAmountAttrOperator
    PLUG_CLS = PositionAmountPlugOperator

    positionAmount0 = FloatField(default_value=0.0)

    positionAmount1 = FloatField(default_value=0.0)

    positionAmount2 = FloatField(default_value=0.0)


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[
        FalloffObjectAttrOperator, FalloffObjectPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField(default_value=0.0)
    fallObjx = falloffObjectX

    falloffObjectY = FloatField(default_value=0.0)
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField(default_value=0.0)
    fallObjz = falloffObjectZ
