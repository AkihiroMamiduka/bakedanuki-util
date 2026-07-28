# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InputTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputTranslateX", "itx"),
        ("inputTranslateY", "ity"),
        ("inputTranslateZ", "itz"),
    )

    inputTranslateX = DoubleLinearField(default_value=0.0)
    itx = inputTranslateX

    inputTranslateY = DoubleLinearField(default_value=0.0)
    ity = inputTranslateY

    inputTranslateZ = DoubleLinearField(default_value=0.0)
    itz = inputTranslateZ


class InputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputTranslatePlugOperator]
):
    __slots__ = ()

    inputTranslateX = DoubleLinearField(default_value=0.0)
    itx = inputTranslateX

    inputTranslateY = DoubleLinearField(default_value=0.0)
    ity = inputTranslateY

    inputTranslateZ = DoubleLinearField(default_value=0.0)
    itz = inputTranslateZ


class InputTranslateField(
    DoubleLinear3CompoundBaseField[
        InputTranslateAttrOperator, InputTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputTranslateAttrOperator
    PLUG_CLS = InputTranslatePlugOperator

    inputTranslateX = DoubleLinearField(default_value=0.0)
    itx = inputTranslateX

    inputTranslateY = DoubleLinearField(default_value=0.0)
    ity = inputTranslateY

    inputTranslateZ = DoubleLinearField(default_value=0.0)
    itz = inputTranslateZ


class InputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputRotateX", "irx"),
        ("inputRotateY", "iry"),
        ("inputRotateZ", "irz"),
    )

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputRotatePlugOperator]
):
    __slots__ = ()

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateField(
    DoubleAngle3CompoundBaseField[
        InputRotateAttrOperator, InputRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputRotateAttrOperator
    PLUG_CLS = InputRotatePlugOperator

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputScalePlugOperator(
    Double3CompoundBasePlugOperator["InputScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputScaleX", "isx"),
        ("inputScaleY", "isy"),
        ("inputScaleZ", "isz"),
    )

    inputScaleX = DoubleField(default_value=1.0)
    isx = inputScaleX

    inputScaleY = DoubleField(default_value=1.0)
    isy = inputScaleY

    inputScaleZ = DoubleField(default_value=1.0)
    isz = inputScaleZ


class InputScaleAttrOperator(
    Double3CompoundBaseAttrOperator[InputScalePlugOperator]
):
    __slots__ = ()

    inputScaleX = DoubleField(default_value=1.0)
    isx = inputScaleX

    inputScaleY = DoubleField(default_value=1.0)
    isy = inputScaleY

    inputScaleZ = DoubleField(default_value=1.0)
    isz = inputScaleZ


class InputScaleField(
    Double3CompoundBaseField[InputScaleAttrOperator, InputScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputScaleAttrOperator
    PLUG_CLS = InputScalePlugOperator

    inputScaleX = DoubleField(default_value=1.0)
    isx = inputScaleX

    inputScaleY = DoubleField(default_value=1.0)
    isy = inputScaleY

    inputScaleZ = DoubleField(default_value=1.0)
    isz = inputScaleZ


class InputShearPlugOperator(
    Double3CompoundBasePlugOperator["InputShearAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputShearX", "ishx"),
        ("inputShearY", "ishy"),
        ("inputShearZ", "ishz"),
    )

    inputShearX = DoubleField(default_value=0.0)
    ishx = inputShearX

    inputShearY = DoubleField(default_value=0.0)
    ishy = inputShearY

    inputShearZ = DoubleField(default_value=0.0)
    ishz = inputShearZ


class InputShearAttrOperator(
    Double3CompoundBaseAttrOperator[InputShearPlugOperator]
):
    __slots__ = ()

    inputShearX = DoubleField(default_value=0.0)
    ishx = inputShearX

    inputShearY = DoubleField(default_value=0.0)
    ishy = inputShearY

    inputShearZ = DoubleField(default_value=0.0)
    ishz = inputShearZ


class InputShearField(
    Double3CompoundBaseField[InputShearAttrOperator, InputShearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputShearAttrOperator
    PLUG_CLS = InputShearPlugOperator

    inputShearX = DoubleField(default_value=0.0)
    ishx = inputShearX

    inputShearY = DoubleField(default_value=0.0)
    ishy = inputShearY

    inputShearZ = DoubleField(default_value=0.0)
    ishz = inputShearZ


class InputQuatPlugOperator(
    QuatCompoundBasePlugOperator["InputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqwx"),
        ("inputQuatY", "iqwy"),
        ("inputQuatZ", "iqwz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField(default_value=0.0)
    iqwx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqwy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqwz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField(default_value=0.0)
    iqwx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqwy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqwz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatField(
    QuatCompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField(default_value=0.0)
    iqwx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqwy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqwz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW
