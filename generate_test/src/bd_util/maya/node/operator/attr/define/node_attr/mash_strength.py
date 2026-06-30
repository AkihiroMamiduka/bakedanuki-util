# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class PositionStrengthPlugOperator(
    Float3CompoundBasePlugOperator["PositionStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionStrength0", "positionStrength0"),
        ("positionStrength1", "positionStrength1"),
        ("positionStrength2", "positionStrength2"),
    )

    positionStrength0 = FloatField()

    positionStrength1 = FloatField()

    positionStrength2 = FloatField()


class PositionStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[PositionStrengthPlugOperator]
):
    __slots__ = ()

    positionStrength0 = FloatField()

    positionStrength1 = FloatField()

    positionStrength2 = FloatField()


class PositionStrengthField(
    Float3CompoundBaseField[PositionStrengthAttrOperator, PositionStrengthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionStrengthAttrOperator
    PLUG_CLS = PositionStrengthPlugOperator

    positionStrength0 = FloatField()

    positionStrength1 = FloatField()

    positionStrength2 = FloatField()


class RotationStrengthPlugOperator(
    Float3CompoundBasePlugOperator["RotationStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationStrength0", "rotationStrength0"),
        ("rotationStrength1", "rotationStrength1"),
        ("rotationStrength2", "rotationStrength2"),
    )

    rotationStrength0 = FloatField()

    rotationStrength1 = FloatField()

    rotationStrength2 = FloatField()


class RotationStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[RotationStrengthPlugOperator]
):
    __slots__ = ()

    rotationStrength0 = FloatField()

    rotationStrength1 = FloatField()

    rotationStrength2 = FloatField()


class RotationStrengthField(
    Float3CompoundBaseField[RotationStrengthAttrOperator, RotationStrengthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationStrengthAttrOperator
    PLUG_CLS = RotationStrengthPlugOperator

    rotationStrength0 = FloatField()

    rotationStrength1 = FloatField()

    rotationStrength2 = FloatField()


class ScaleStrengthPlugOperator(
    Float3CompoundBasePlugOperator["ScaleStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleStrength0", "scaleStrength0"),
        ("scaleStrength1", "scaleStrength1"),
        ("scaleStrength2", "scaleStrength2"),
    )

    scaleStrength0 = FloatField()

    scaleStrength1 = FloatField()

    scaleStrength2 = FloatField()


class ScaleStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleStrengthPlugOperator]
):
    __slots__ = ()

    scaleStrength0 = FloatField()

    scaleStrength1 = FloatField()

    scaleStrength2 = FloatField()


class ScaleStrengthField(
    Float3CompoundBaseField[ScaleStrengthAttrOperator, ScaleStrengthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleStrengthAttrOperator
    PLUG_CLS = ScaleStrengthPlugOperator

    scaleStrength0 = FloatField()

    scaleStrength1 = FloatField()

    scaleStrength2 = FloatField()


class PositionStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["PositionStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionStrengthMapR", "positionStrengthMapr"),
        ("positionStrengthMapG", "positionStrengthMapg"),
        ("positionStrengthMapB", "positionStrengthMapb"),
    )

    positionStrengthMapR = FloatField()
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField()
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField()
    positionStrengthMapb = positionStrengthMapB


class PositionStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[PositionStrengthMapPlugOperator]
):
    __slots__ = ()

    positionStrengthMapR = FloatField()
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField()
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField()
    positionStrengthMapb = positionStrengthMapB


class PositionStrengthMapField(
    Float3CompoundBaseField[PositionStrengthMapAttrOperator, PositionStrengthMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionStrengthMapAttrOperator
    PLUG_CLS = PositionStrengthMapPlugOperator

    positionStrengthMapR = FloatField()
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField()
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField()
    positionStrengthMapb = positionStrengthMapB


class RotationStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["RotationStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationStrengthMapR", "rotationStrengthMapr"),
        ("rotationStrengthMapG", "rotationStrengthMapg"),
        ("rotationStrengthMapB", "rotationStrengthMapb"),
    )

    rotationStrengthMapR = FloatField()
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField()
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField()
    rotationStrengthMapb = rotationStrengthMapB


class RotationStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[RotationStrengthMapPlugOperator]
):
    __slots__ = ()

    rotationStrengthMapR = FloatField()
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField()
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField()
    rotationStrengthMapb = rotationStrengthMapB


class RotationStrengthMapField(
    Float3CompoundBaseField[RotationStrengthMapAttrOperator, RotationStrengthMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationStrengthMapAttrOperator
    PLUG_CLS = RotationStrengthMapPlugOperator

    rotationStrengthMapR = FloatField()
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField()
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField()
    rotationStrengthMapb = rotationStrengthMapB


class ScaleStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["ScaleStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleStrengthMapR", "scaleStrengthMapr"),
        ("scaleStrengthMapG", "scaleStrengthMapg"),
        ("scaleStrengthMapB", "scaleStrengthMapb"),
    )

    scaleStrengthMapR = FloatField()
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField()
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField()
    scaleStrengthMapb = scaleStrengthMapB


class ScaleStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleStrengthMapPlugOperator]
):
    __slots__ = ()

    scaleStrengthMapR = FloatField()
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField()
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField()
    scaleStrengthMapb = scaleStrengthMapB


class ScaleStrengthMapField(
    Float3CompoundBaseField[ScaleStrengthMapAttrOperator, ScaleStrengthMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleStrengthMapAttrOperator
    PLUG_CLS = ScaleStrengthMapPlugOperator

    scaleStrengthMapR = FloatField()
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField()
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField()
    scaleStrengthMapb = scaleStrengthMapB
