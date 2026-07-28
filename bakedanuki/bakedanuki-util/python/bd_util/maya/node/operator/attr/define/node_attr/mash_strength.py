# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
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


class PositionStrengthPlugOperator(
    Float3CompoundBasePlugOperator["PositionStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionStrength0", "positionStrength0"),
        ("positionStrength1", "positionStrength1"),
        ("positionStrength2", "positionStrength2"),
    )

    positionStrength0 = FloatField(default_value=1.0)

    positionStrength1 = FloatField(default_value=1.0)

    positionStrength2 = FloatField(default_value=1.0)


class PositionStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[PositionStrengthPlugOperator]
):
    __slots__ = ()

    positionStrength0 = FloatField(default_value=1.0)

    positionStrength1 = FloatField(default_value=1.0)

    positionStrength2 = FloatField(default_value=1.0)


class PositionStrengthField(
    Float3CompoundBaseField[
        PositionStrengthAttrOperator, PositionStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PositionStrengthAttrOperator
    PLUG_CLS = PositionStrengthPlugOperator

    positionStrength0 = FloatField(default_value=1.0)

    positionStrength1 = FloatField(default_value=1.0)

    positionStrength2 = FloatField(default_value=1.0)


class RotationStrengthPlugOperator(
    Float3CompoundBasePlugOperator["RotationStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationStrength0", "rotationStrength0"),
        ("rotationStrength1", "rotationStrength1"),
        ("rotationStrength2", "rotationStrength2"),
    )

    rotationStrength0 = FloatField(default_value=1.0)

    rotationStrength1 = FloatField(default_value=1.0)

    rotationStrength2 = FloatField(default_value=1.0)


class RotationStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[RotationStrengthPlugOperator]
):
    __slots__ = ()

    rotationStrength0 = FloatField(default_value=1.0)

    rotationStrength1 = FloatField(default_value=1.0)

    rotationStrength2 = FloatField(default_value=1.0)


class RotationStrengthField(
    Float3CompoundBaseField[
        RotationStrengthAttrOperator, RotationStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationStrengthAttrOperator
    PLUG_CLS = RotationStrengthPlugOperator

    rotationStrength0 = FloatField(default_value=1.0)

    rotationStrength1 = FloatField(default_value=1.0)

    rotationStrength2 = FloatField(default_value=1.0)


class ScaleStrengthPlugOperator(
    Float3CompoundBasePlugOperator["ScaleStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleStrength0", "scaleStrength0"),
        ("scaleStrength1", "scaleStrength1"),
        ("scaleStrength2", "scaleStrength2"),
    )

    scaleStrength0 = FloatField(default_value=1.0)

    scaleStrength1 = FloatField(default_value=1.0)

    scaleStrength2 = FloatField(default_value=1.0)


class ScaleStrengthAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleStrengthPlugOperator]
):
    __slots__ = ()

    scaleStrength0 = FloatField(default_value=1.0)

    scaleStrength1 = FloatField(default_value=1.0)

    scaleStrength2 = FloatField(default_value=1.0)


class ScaleStrengthField(
    Float3CompoundBaseField[
        ScaleStrengthAttrOperator, ScaleStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ScaleStrengthAttrOperator
    PLUG_CLS = ScaleStrengthPlugOperator

    scaleStrength0 = FloatField(default_value=1.0)

    scaleStrength1 = FloatField(default_value=1.0)

    scaleStrength2 = FloatField(default_value=1.0)


class PositionStrengthMapPlugOperator(
    Float3CompoundBasePlugOperator["PositionStrengthMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionStrengthMapR", "positionStrengthMapr"),
        ("positionStrengthMapG", "positionStrengthMapg"),
        ("positionStrengthMapB", "positionStrengthMapb"),
    )

    positionStrengthMapR = FloatField(default_value=1.0)
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField(default_value=1.0)
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField(default_value=1.0)
    positionStrengthMapb = positionStrengthMapB


class PositionStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[PositionStrengthMapPlugOperator]
):
    __slots__ = ()

    positionStrengthMapR = FloatField(default_value=1.0)
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField(default_value=1.0)
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField(default_value=1.0)
    positionStrengthMapb = positionStrengthMapB


class PositionStrengthMapField(
    Float3CompoundBaseField[
        PositionStrengthMapAttrOperator, PositionStrengthMapPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PositionStrengthMapAttrOperator
    PLUG_CLS = PositionStrengthMapPlugOperator

    positionStrengthMapR = FloatField(default_value=1.0)
    positionStrengthMapr = positionStrengthMapR

    positionStrengthMapG = FloatField(default_value=1.0)
    positionStrengthMapg = positionStrengthMapG

    positionStrengthMapB = FloatField(default_value=1.0)
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

    rotationStrengthMapR = FloatField(default_value=1.0)
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField(default_value=1.0)
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField(default_value=1.0)
    rotationStrengthMapb = rotationStrengthMapB


class RotationStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[RotationStrengthMapPlugOperator]
):
    __slots__ = ()

    rotationStrengthMapR = FloatField(default_value=1.0)
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField(default_value=1.0)
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField(default_value=1.0)
    rotationStrengthMapb = rotationStrengthMapB


class RotationStrengthMapField(
    Float3CompoundBaseField[
        RotationStrengthMapAttrOperator, RotationStrengthMapPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotationStrengthMapAttrOperator
    PLUG_CLS = RotationStrengthMapPlugOperator

    rotationStrengthMapR = FloatField(default_value=1.0)
    rotationStrengthMapr = rotationStrengthMapR

    rotationStrengthMapG = FloatField(default_value=1.0)
    rotationStrengthMapg = rotationStrengthMapG

    rotationStrengthMapB = FloatField(default_value=1.0)
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

    scaleStrengthMapR = FloatField(default_value=1.0)
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField(default_value=1.0)
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField(default_value=1.0)
    scaleStrengthMapb = scaleStrengthMapB


class ScaleStrengthMapAttrOperator(
    Float3CompoundBaseAttrOperator[ScaleStrengthMapPlugOperator]
):
    __slots__ = ()

    scaleStrengthMapR = FloatField(default_value=1.0)
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField(default_value=1.0)
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField(default_value=1.0)
    scaleStrengthMapb = scaleStrengthMapB


class ScaleStrengthMapField(
    Float3CompoundBaseField[
        ScaleStrengthMapAttrOperator, ScaleStrengthMapPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ScaleStrengthMapAttrOperator
    PLUG_CLS = ScaleStrengthMapPlugOperator

    scaleStrengthMapR = FloatField(default_value=1.0)
    scaleStrengthMapr = scaleStrengthMapR

    scaleStrengthMapG = FloatField(default_value=1.0)
    scaleStrengthMapg = scaleStrengthMapG

    scaleStrengthMapB = FloatField(default_value=1.0)
    scaleStrengthMapb = scaleStrengthMapB
