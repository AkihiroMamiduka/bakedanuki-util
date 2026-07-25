# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
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


class InTranslate1PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InTranslate1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inTranslateX1", "itx1"),
        ("inTranslateY1", "ity1"),
        ("inTranslateZ1", "itz1"),
    )

    inTranslateX1 = DoubleLinearField(default_value=0.0)
    itx1 = inTranslateX1

    inTranslateY1 = DoubleLinearField(default_value=0.0)
    ity1 = inTranslateY1

    inTranslateZ1 = DoubleLinearField(default_value=0.0)
    itz1 = inTranslateZ1


class InTranslate1AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InTranslate1PlugOperator]
):
    __slots__ = ()

    inTranslateX1 = DoubleLinearField(default_value=0.0)
    itx1 = inTranslateX1

    inTranslateY1 = DoubleLinearField(default_value=0.0)
    ity1 = inTranslateY1

    inTranslateZ1 = DoubleLinearField(default_value=0.0)
    itz1 = inTranslateZ1


class InTranslate1Field(
    DoubleLinear3CompoundBaseField[InTranslate1AttrOperator, InTranslate1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InTranslate1AttrOperator
    PLUG_CLS = InTranslate1PlugOperator

    inTranslateX1 = DoubleLinearField(default_value=0.0)
    itx1 = inTranslateX1

    inTranslateY1 = DoubleLinearField(default_value=0.0)
    ity1 = inTranslateY1

    inTranslateZ1 = DoubleLinearField(default_value=0.0)
    itz1 = inTranslateZ1


class InRotate1PlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InRotate1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRotateX1", "irx1"),
        ("inRotateY1", "iry1"),
        ("inRotateZ1", "irz1"),
    )

    inRotateX1 = DoubleAngleField(default_value=0.0)
    irx1 = inRotateX1

    inRotateY1 = DoubleAngleField(default_value=0.0)
    iry1 = inRotateY1

    inRotateZ1 = DoubleAngleField(default_value=0.0)
    irz1 = inRotateZ1


class InRotate1AttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InRotate1PlugOperator]
):
    __slots__ = ()

    inRotateX1 = DoubleAngleField(default_value=0.0)
    irx1 = inRotateX1

    inRotateY1 = DoubleAngleField(default_value=0.0)
    iry1 = inRotateY1

    inRotateZ1 = DoubleAngleField(default_value=0.0)
    irz1 = inRotateZ1


class InRotate1Field(
    DoubleAngle3CompoundBaseField[InRotate1AttrOperator, InRotate1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRotate1AttrOperator
    PLUG_CLS = InRotate1PlugOperator

    inRotateX1 = DoubleAngleField(default_value=0.0)
    irx1 = inRotateX1

    inRotateY1 = DoubleAngleField(default_value=0.0)
    iry1 = inRotateY1

    inRotateZ1 = DoubleAngleField(default_value=0.0)
    irz1 = inRotateZ1


class InTranslate2PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InTranslate2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inTranslateX2", "itx2"),
        ("inTranslateY2", "ity2"),
        ("inTranslateZ2", "itz2"),
    )

    inTranslateX2 = DoubleLinearField(default_value=0.0)
    itx2 = inTranslateX2

    inTranslateY2 = DoubleLinearField(default_value=0.0)
    ity2 = inTranslateY2

    inTranslateZ2 = DoubleLinearField(default_value=0.0)
    itz2 = inTranslateZ2


class InTranslate2AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InTranslate2PlugOperator]
):
    __slots__ = ()

    inTranslateX2 = DoubleLinearField(default_value=0.0)
    itx2 = inTranslateX2

    inTranslateY2 = DoubleLinearField(default_value=0.0)
    ity2 = inTranslateY2

    inTranslateZ2 = DoubleLinearField(default_value=0.0)
    itz2 = inTranslateZ2


class InTranslate2Field(
    DoubleLinear3CompoundBaseField[InTranslate2AttrOperator, InTranslate2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InTranslate2AttrOperator
    PLUG_CLS = InTranslate2PlugOperator

    inTranslateX2 = DoubleLinearField(default_value=0.0)
    itx2 = inTranslateX2

    inTranslateY2 = DoubleLinearField(default_value=0.0)
    ity2 = inTranslateY2

    inTranslateZ2 = DoubleLinearField(default_value=0.0)
    itz2 = inTranslateZ2


class InRotate2PlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InRotate2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRotateX2", "irx2"),
        ("inRotateY2", "iry2"),
        ("inRotateZ2", "irz2"),
    )

    inRotateX2 = DoubleAngleField(default_value=0.0)
    irx2 = inRotateX2

    inRotateY2 = DoubleAngleField(default_value=0.0)
    iry2 = inRotateY2

    inRotateZ2 = DoubleAngleField(default_value=0.0)
    irz2 = inRotateZ2


class InRotate2AttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InRotate2PlugOperator]
):
    __slots__ = ()

    inRotateX2 = DoubleAngleField(default_value=0.0)
    irx2 = inRotateX2

    inRotateY2 = DoubleAngleField(default_value=0.0)
    iry2 = inRotateY2

    inRotateZ2 = DoubleAngleField(default_value=0.0)
    irz2 = inRotateZ2


class InRotate2Field(
    DoubleAngle3CompoundBaseField[InRotate2AttrOperator, InRotate2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRotate2AttrOperator
    PLUG_CLS = InRotate2PlugOperator

    inRotateX2 = DoubleAngleField(default_value=0.0)
    irx2 = inRotateX2

    inRotateY2 = DoubleAngleField(default_value=0.0)
    iry2 = inRotateY2

    inRotateZ2 = DoubleAngleField(default_value=0.0)
    irz2 = inRotateZ2


class OutTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTranslateX", "otx"),
        ("outTranslateY", "oty"),
        ("outTranslateZ", "otz"),
    )

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutTranslatePlugOperator]
):
    __slots__ = ()

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutTranslateField(
    DoubleLinear3CompoundBaseField[OutTranslateAttrOperator, OutTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTranslateAttrOperator
    PLUG_CLS = OutTranslatePlugOperator

    outTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outTranslateX

    outTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outTranslateY

    outTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outTranslateZ


class OutRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRotateX", "orx"),
        ("outRotateY", "ory"),
        ("outRotateZ", "orz"),
    )

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ


class OutRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutRotatePlugOperator]
):
    __slots__ = ()

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ


class OutRotateField(
    DoubleAngle3CompoundBaseField[OutRotateAttrOperator, OutRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRotateAttrOperator
    PLUG_CLS = OutRotatePlugOperator

    outRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outRotateX

    outRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outRotateY

    outRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outRotateZ
