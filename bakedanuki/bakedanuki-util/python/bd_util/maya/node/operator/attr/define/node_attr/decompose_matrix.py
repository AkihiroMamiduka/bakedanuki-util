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


class OutputTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTranslateX", "otx"),
        ("outputTranslateY", "oty"),
        ("outputTranslateZ", "otz"),
    )

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputTranslatePlugOperator]
):
    __slots__ = ()

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateField(
    DoubleLinear3CompoundBaseField[
        OutputTranslateAttrOperator, OutputTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputTranslateAttrOperator
    PLUG_CLS = OutputTranslatePlugOperator

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
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

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[
        OutputRotateAttrOperator, OutputRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
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

    outputScaleX = DoubleField(default_value=0.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=0.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=0.0, writable=False)
    osz = outputScaleZ


class OutputScaleAttrOperator(
    Double3CompoundBaseAttrOperator[OutputScalePlugOperator]
):
    __slots__ = ()

    outputScaleX = DoubleField(default_value=0.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=0.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=0.0, writable=False)
    osz = outputScaleZ


class OutputScaleField(
    Double3CompoundBaseField[OutputScaleAttrOperator, OutputScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputScaleAttrOperator
    PLUG_CLS = OutputScalePlugOperator

    outputScaleX = DoubleField(default_value=0.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=0.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=0.0, writable=False)
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

    outputShearX = DoubleField(default_value=0.0, writable=False)
    oshx = outputShearX

    outputShearY = DoubleField(default_value=0.0, writable=False)
    oshy = outputShearY

    outputShearZ = DoubleField(default_value=0.0, writable=False)
    oshz = outputShearZ


class OutputShearAttrOperator(
    Double3CompoundBaseAttrOperator[OutputShearPlugOperator]
):
    __slots__ = ()

    outputShearX = DoubleField(default_value=0.0, writable=False)
    oshx = outputShearX

    outputShearY = DoubleField(default_value=0.0, writable=False)
    oshy = outputShearY

    outputShearZ = DoubleField(default_value=0.0, writable=False)
    oshz = outputShearZ


class OutputShearField(
    Double3CompoundBaseField[OutputShearAttrOperator, OutputShearPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputShearAttrOperator
    PLUG_CLS = OutputShearPlugOperator

    outputShearX = DoubleField(default_value=0.0, writable=False)
    oshx = outputShearX

    outputShearY = DoubleField(default_value=0.0, writable=False)
    oshy = outputShearY

    outputShearZ = DoubleField(default_value=0.0, writable=False)
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

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatField(
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW
