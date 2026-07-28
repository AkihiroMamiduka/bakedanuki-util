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


class GuideInputsPlugOperator(
    Float3CompoundBasePlugOperator["GuideInputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("guideInputs0", "guideInputs0"),
        ("guideInputs1", "guideInputs1"),
        ("guideInputs2", "guideInputs2"),
    )

    guideInputs0 = FloatField(default_value=1.0, readable=False)

    guideInputs1 = FloatField(default_value=1.0, readable=False)

    guideInputs2 = FloatField(default_value=1.0, readable=False)


class GuideInputsAttrOperator(
    Float3CompoundBaseAttrOperator[GuideInputsPlugOperator]
):
    __slots__ = ()

    guideInputs0 = FloatField(default_value=1.0, readable=False)

    guideInputs1 = FloatField(default_value=1.0, readable=False)

    guideInputs2 = FloatField(default_value=1.0, readable=False)


class GuideInputsField(
    Float3CompoundBaseField[GuideInputsAttrOperator, GuideInputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GuideInputsAttrOperator
    PLUG_CLS = GuideInputsPlugOperator


class GuideScalePlugOperator(
    Float3CompoundBasePlugOperator["GuideScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("guideScale0", "guideScale0"),
        ("guideScale1", "guideScale1"),
        ("guideScale2", "guideScale2"),
    )

    guideScale0 = FloatField(default_value=1.0, readable=False)

    guideScale1 = FloatField(default_value=1.0, readable=False)

    guideScale2 = FloatField(default_value=1.0, readable=False)


class GuideScaleAttrOperator(
    Float3CompoundBaseAttrOperator[GuideScalePlugOperator]
):
    __slots__ = ()

    guideScale0 = FloatField(default_value=1.0, readable=False)

    guideScale1 = FloatField(default_value=1.0, readable=False)

    guideScale2 = FloatField(default_value=1.0, readable=False)


class GuideScaleField(
    Float3CompoundBaseField[GuideScaleAttrOperator, GuideScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GuideScaleAttrOperator
    PLUG_CLS = GuideScalePlugOperator


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


class TranslateOutPPPlugOperator(
    CompoundPlugOperator["TranslateOutPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOutPP", "positionOutPP"),
        ("scaleOutPP", "scaleOutPP"),
        ("rotationOutPP", "rotationOutPP"),
    )

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()


class TranslateOutPPAttrOperator(
    CompoundAttrOperator[TranslateOutPPPlugOperator]
):
    __slots__ = ()

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()


class TranslateOutPPField(
    CompoundField[TranslateOutPPAttrOperator, TranslateOutPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateOutPPAttrOperator
    PLUG_CLS = TranslateOutPPPlugOperator

    positionOutPP = DataVectorArrayField()

    scaleOutPP = DataVectorArrayField()

    rotationOutPP = DataVectorArrayField()
