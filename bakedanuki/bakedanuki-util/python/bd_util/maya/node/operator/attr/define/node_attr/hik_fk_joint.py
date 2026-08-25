# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class TranslateOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TranslateOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateOffsetX", "tox"),
        ("translateOffsetY", "toy"),
        ("translateOffsetZ", "toz"),
    )

    translateOffsetX = DoubleLinearField(default_value=0.0)
    tox = translateOffsetX

    translateOffsetY = DoubleLinearField(default_value=0.0)
    toy = translateOffsetY

    translateOffsetZ = DoubleLinearField(default_value=0.0)
    toz = translateOffsetZ


class TranslateOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TranslateOffsetPlugOperator]
):
    __slots__ = ()

    translateOffsetX = DoubleLinearField(default_value=0.0)
    tox = translateOffsetX

    translateOffsetY = DoubleLinearField(default_value=0.0)
    toy = translateOffsetY

    translateOffsetZ = DoubleLinearField(default_value=0.0)
    toz = translateOffsetZ


class TranslateOffsetField(
    DoubleLinear3CompoundBaseField[
        TranslateOffsetAttrOperator, TranslateOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TranslateOffsetAttrOperator
    PLUG_CLS = TranslateOffsetPlugOperator

    translateOffsetX = DoubleLinearField(default_value=0.0)
    tox = translateOffsetX

    translateOffsetY = DoubleLinearField(default_value=0.0)
    toy = translateOffsetY

    translateOffsetZ = DoubleLinearField(default_value=0.0)
    toz = translateOffsetZ


class RotateOffsetPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateOffsetX", "rox"),
        ("rotateOffsetY", "roy"),
        ("rotateOffsetZ", "roz"),
    )

    rotateOffsetX = DoubleAngleField(default_value=0.0)
    rox = rotateOffsetX

    rotateOffsetY = DoubleAngleField(default_value=0.0)
    roy = rotateOffsetY

    rotateOffsetZ = DoubleAngleField(default_value=0.0)
    roz = rotateOffsetZ


class RotateOffsetAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RotateOffsetPlugOperator]
):
    __slots__ = ()

    rotateOffsetX = DoubleAngleField(default_value=0.0)
    rox = rotateOffsetX

    rotateOffsetY = DoubleAngleField(default_value=0.0)
    roy = rotateOffsetY

    rotateOffsetZ = DoubleAngleField(default_value=0.0)
    roz = rotateOffsetZ


class RotateOffsetField(
    DoubleAngle3CompoundBaseField[
        RotateOffsetAttrOperator, RotateOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotateOffsetAttrOperator
    PLUG_CLS = RotateOffsetPlugOperator

    rotateOffsetX = DoubleAngleField(default_value=0.0)
    rox = rotateOffsetX

    rotateOffsetY = DoubleAngleField(default_value=0.0)
    roy = rotateOffsetY

    rotateOffsetZ = DoubleAngleField(default_value=0.0)
    roz = rotateOffsetZ


class ScaleOffsetPlugOperator(
    Double3CompoundBasePlugOperator["ScaleOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleOffsetX", "sox"),
        ("scaleOffsetY", "soy"),
        ("scaleOffsetZ", "soz"),
    )

    scaleOffsetX = DoubleField(default_value=1.0)
    sox = scaleOffsetX

    scaleOffsetY = DoubleField(default_value=1.0)
    soy = scaleOffsetY

    scaleOffsetZ = DoubleField(default_value=1.0)
    soz = scaleOffsetZ


class ScaleOffsetAttrOperator(
    Double3CompoundBaseAttrOperator[ScaleOffsetPlugOperator]
):
    __slots__ = ()

    scaleOffsetX = DoubleField(default_value=1.0)
    sox = scaleOffsetX

    scaleOffsetY = DoubleField(default_value=1.0)
    soy = scaleOffsetY

    scaleOffsetZ = DoubleField(default_value=1.0)
    soz = scaleOffsetZ


class ScaleOffsetField(
    Double3CompoundBaseField[ScaleOffsetAttrOperator, ScaleOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleOffsetAttrOperator
    PLUG_CLS = ScaleOffsetPlugOperator

    scaleOffsetX = DoubleField(default_value=1.0)
    sox = scaleOffsetX

    scaleOffsetY = DoubleField(default_value=1.0)
    soy = scaleOffsetY

    scaleOffsetZ = DoubleField(default_value=1.0)
    soz = scaleOffsetZ
