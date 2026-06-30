# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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


class OutputTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTranslateX", "otx"),
        ("outputTranslateY", "oty"),
        ("outputTranslateZ", "otz"),
    )

    outputTranslateX = DoubleLinearField()
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField()
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField()
    otz = outputTranslateZ


class OutputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputTranslatePlugOperator]
):
    __slots__ = ()

    outputTranslateX = DoubleLinearField()
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField()
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField()
    otz = outputTranslateZ


class OutputTranslateField(
    DoubleLinear3CompoundBaseField[OutputTranslateAttrOperator, OutputTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputTranslateAttrOperator
    PLUG_CLS = OutputTranslatePlugOperator

    outputTranslateX = DoubleLinearField()
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField()
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField()
    otz = outputTranslateZ


class OutputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputRotateX", "orx"),
        ("outputRotateY", "ory"),
        ("outputRotateZ", "orz"),
    )

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[OutputRotateAttrOperator, OutputRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ


class OutputScalePlugOperator(
    Double3CompoundBasePlugOperator["OutputScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputScaleX", "osx"),
        ("outputScaleY", "osy"),
        ("outputScaleZ", "osz"),
    )

    outputScaleX = DoubleField()
    osx = outputScaleX

    outputScaleY = DoubleField()
    osy = outputScaleY

    outputScaleZ = DoubleField()
    osz = outputScaleZ


class OutputScaleAttrOperator(
    Double3CompoundBaseAttrOperator[OutputScalePlugOperator]
):
    __slots__ = ()

    outputScaleX = DoubleField()
    osx = outputScaleX

    outputScaleY = DoubleField()
    osy = outputScaleY

    outputScaleZ = DoubleField()
    osz = outputScaleZ


class OutputScaleField(
    Double3CompoundBaseField[OutputScaleAttrOperator, OutputScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputScaleAttrOperator
    PLUG_CLS = OutputScalePlugOperator

    outputScaleX = DoubleField()
    osx = outputScaleX

    outputScaleY = DoubleField()
    osy = outputScaleY

    outputScaleZ = DoubleField()
    osz = outputScaleZ


class OutputShearPlugOperator(
    Double3CompoundBasePlugOperator["OutputShearAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputShearX", "oshx"),
        ("outputShearY", "oshy"),
        ("outputShearZ", "oshz"),
    )

    outputShearX = DoubleField()
    oshx = outputShearX

    outputShearY = DoubleField()
    oshy = outputShearY

    outputShearZ = DoubleField()
    oshz = outputShearZ


class OutputShearAttrOperator(
    Double3CompoundBaseAttrOperator[OutputShearPlugOperator]
):
    __slots__ = ()

    outputShearX = DoubleField()
    oshx = outputShearX

    outputShearY = DoubleField()
    oshy = outputShearY

    outputShearZ = DoubleField()
    oshz = outputShearZ


class OutputShearField(
    Double3CompoundBaseField[OutputShearAttrOperator, OutputShearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputShearAttrOperator
    PLUG_CLS = OutputShearPlugOperator

    outputShearX = DoubleField()
    oshx = outputShearX

    outputShearY = DoubleField()
    oshy = outputShearY

    outputShearZ = DoubleField()
    oshz = outputShearZ


class OutputQuatPlugOperator(
    QuatCompoundBasePlugOperator["OutputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputQuatX", "oqx"),
        ("outputQuatY", "oqy"),
        ("outputQuatZ", "oqz"),
        ("outputQuatW", "oqw"),
    )

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW


class OutputQuatField(
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField()
    oqx = outputQuatX

    outputQuatY = DoubleField()
    oqy = outputQuatY

    outputQuatZ = DoubleField()
    oqz = outputQuatZ

    outputQuatW = DoubleField()
    oqw = outputQuatW
