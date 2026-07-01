# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
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


class InRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InRootTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRootTranslateX", "rtix"),
        ("inRootTranslateY", "rtiy"),
        ("inRootTranslateZ", "rtiz"),
    )

    inRootTranslateX = DoubleLinearField()
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField()
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField()
    rtiz = inRootTranslateZ


class InRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InRootTranslatePlugOperator]
):
    __slots__ = ()

    inRootTranslateX = DoubleLinearField()
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField()
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField()
    rtiz = inRootTranslateZ


class InRootTranslateField(
    DoubleLinear3CompoundBaseField[InRootTranslateAttrOperator, InRootTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRootTranslateAttrOperator
    PLUG_CLS = InRootTranslatePlugOperator

    inRootTranslateX = DoubleLinearField()
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField()
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField()
    rtiz = inRootTranslateZ


class InRootRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InRootRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRootRotateX", "rrix"),
        ("inRootRotateY", "rriy"),
        ("inRootRotateZ", "rriz"),
    )

    inRootRotateX = DoubleAngleField()
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField()
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField()
    rriz = inRootRotateZ


class InRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InRootRotatePlugOperator]
):
    __slots__ = ()

    inRootRotateX = DoubleAngleField()
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField()
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField()
    rriz = inRootRotateZ


class InRootRotateField(
    DoubleAngle3CompoundBaseField[InRootRotateAttrOperator, InRootRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InRootRotateAttrOperator
    PLUG_CLS = InRootRotatePlugOperator

    inRootRotateX = DoubleAngleField()
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField()
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField()
    rriz = inRootRotateZ


class RootJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RootJointOrientAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rootJointOrientX", "rjox"),
        ("rootJointOrientY", "rjoy"),
        ("rootJointOrientZ", "rjoz"),
    )

    rootJointOrientX = DoubleAngleField()
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField()
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField()
    rjoz = rootJointOrientZ


class RootJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RootJointOrientPlugOperator]
):
    __slots__ = ()

    rootJointOrientX = DoubleAngleField()
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField()
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField()
    rjoz = rootJointOrientZ


class RootJointOrientField(
    DoubleAngle3CompoundBaseField[RootJointOrientAttrOperator, RootJointOrientPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RootJointOrientAttrOperator
    PLUG_CLS = RootJointOrientPlugOperator

    rootJointOrientX = DoubleAngleField()
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField()
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField()
    rjoz = rootJointOrientZ


class OffsetRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OffsetRootTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetRootTranslateX", "rtfx"),
        ("offsetRootTranslateY", "rtfy"),
        ("offsetRootTranslateZ", "rtfz"),
    )

    offsetRootTranslateX = DoubleLinearField()
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField()
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField()
    rtfz = offsetRootTranslateZ


class OffsetRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetRootTranslatePlugOperator]
):
    __slots__ = ()

    offsetRootTranslateX = DoubleLinearField()
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField()
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField()
    rtfz = offsetRootTranslateZ


class OffsetRootTranslateField(
    DoubleLinear3CompoundBaseField[OffsetRootTranslateAttrOperator, OffsetRootTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootTranslateAttrOperator
    PLUG_CLS = OffsetRootTranslatePlugOperator

    offsetRootTranslateX = DoubleLinearField()
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField()
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField()
    rtfz = offsetRootTranslateZ


class InitialOffsetRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InitialOffsetRootTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialOffsetRootTranslateX", "itfx"),
        ("initialOffsetRootTranslateY", "itfy"),
        ("initialOffsetRootTranslateZ", "itfz"),
    )

    initialOffsetRootTranslateX = DoubleLinearField()
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField()
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField()
    itfz = initialOffsetRootTranslateZ


class InitialOffsetRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InitialOffsetRootTranslatePlugOperator]
):
    __slots__ = ()

    initialOffsetRootTranslateX = DoubleLinearField()
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField()
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField()
    itfz = initialOffsetRootTranslateZ


class InitialOffsetRootTranslateField(
    DoubleLinear3CompoundBaseField[InitialOffsetRootTranslateAttrOperator, InitialOffsetRootTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialOffsetRootTranslateAttrOperator
    PLUG_CLS = InitialOffsetRootTranslatePlugOperator

    initialOffsetRootTranslateX = DoubleLinearField()
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField()
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField()
    itfz = initialOffsetRootTranslateZ


class RotateControlScalePlugOperator(
    Double3CompoundBasePlugOperator["RotateControlScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateControlScaleX", "rcsx"),
        ("rotateControlScaleY", "rcsy"),
        ("rotateControlScaleZ", "rcsz"),
    )

    rotateControlScaleX = DoubleField()
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField()
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField()
    rcsz = rotateControlScaleZ


class RotateControlScaleAttrOperator(
    Double3CompoundBaseAttrOperator[RotateControlScalePlugOperator]
):
    __slots__ = ()

    rotateControlScaleX = DoubleField()
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField()
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField()
    rcsz = rotateControlScaleZ


class RotateControlScaleField(
    Double3CompoundBaseField[RotateControlScaleAttrOperator, RotateControlScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateControlScaleAttrOperator
    PLUG_CLS = RotateControlScalePlugOperator

    rotateControlScaleX = DoubleField()
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField()
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField()
    rcsz = rotateControlScaleZ


class OffsetRootRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OffsetRootRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetRootRotateX", "rrfx"),
        ("offsetRootRotateY", "rrfy"),
        ("offsetRootRotateZ", "rrfz"),
    )

    offsetRootRotateX = DoubleAngleField()
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField()
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField()
    rrfz = offsetRootRotateZ


class OffsetRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OffsetRootRotatePlugOperator]
):
    __slots__ = ()

    offsetRootRotateX = DoubleAngleField()
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField()
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField()
    rrfz = offsetRootRotateZ


class OffsetRootRotateField(
    DoubleAngle3CompoundBaseField[OffsetRootRotateAttrOperator, OffsetRootRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootRotateAttrOperator
    PLUG_CLS = OffsetRootRotatePlugOperator

    offsetRootRotateX = DoubleAngleField()
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField()
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField()
    rrfz = offsetRootRotateZ


class OffsetRootRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OffsetRootRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetRootRotatePivotX", "rppfx"),
        ("offsetRootRotatePivotY", "rppfy"),
        ("offsetRootRotatePivotZ", "rppfz"),
    )

    offsetRootRotatePivotX = DoubleLinearField()
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField()
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField()
    rppfz = offsetRootRotatePivotZ


class OffsetRootRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetRootRotatePivotPlugOperator]
):
    __slots__ = ()

    offsetRootRotatePivotX = DoubleLinearField()
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField()
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField()
    rppfz = offsetRootRotatePivotZ


class OffsetRootRotatePivotField(
    DoubleLinear3CompoundBaseField[OffsetRootRotatePivotAttrOperator, OffsetRootRotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootRotatePivotAttrOperator
    PLUG_CLS = OffsetRootRotatePivotPlugOperator

    offsetRootRotatePivotX = DoubleLinearField()
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField()
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField()
    rppfz = offsetRootRotatePivotZ


class OutRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutRootTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRootTranslateX", "rtox"),
        ("outRootTranslateY", "rtoy"),
        ("outRootTranslateZ", "rtoz"),
    )

    outRootTranslateX = DoubleLinearField()
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField()
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField()
    rtoz = outRootTranslateZ


class OutRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutRootTranslatePlugOperator]
):
    __slots__ = ()

    outRootTranslateX = DoubleLinearField()
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField()
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField()
    rtoz = outRootTranslateZ


class OutRootTranslateField(
    DoubleLinear3CompoundBaseField[OutRootTranslateAttrOperator, OutRootTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRootTranslateAttrOperator
    PLUG_CLS = OutRootTranslatePlugOperator

    outRootTranslateX = DoubleLinearField()
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField()
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField()
    rtoz = outRootTranslateZ


class OutRootRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutRootRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outRootRotateX", "rrox"),
        ("outRootRotateY", "rroy"),
        ("outRootRotateZ", "rroz"),
    )

    outRootRotateX = DoubleAngleField()
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField()
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField()
    rroz = outRootRotateZ


class OutRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutRootRotatePlugOperator]
):
    __slots__ = ()

    outRootRotateX = DoubleAngleField()
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField()
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField()
    rroz = outRootRotateZ


class OutRootRotateField(
    DoubleAngle3CompoundBaseField[OutRootRotateAttrOperator, OutRootRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutRootRotateAttrOperator
    PLUG_CLS = OutRootRotatePlugOperator

    outRootRotateX = DoubleAngleField()
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField()
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField()
    rroz = outRootRotateZ
