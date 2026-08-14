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


class InRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InRootTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inRootTranslateX", "rtix"),
        ("inRootTranslateY", "rtiy"),
        ("inRootTranslateZ", "rtiz"),
    )

    inRootTranslateX = DoubleLinearField(default_value=0.0)
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField(default_value=0.0)
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField(default_value=0.0)
    rtiz = inRootTranslateZ


class InRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InRootTranslatePlugOperator]
):
    __slots__ = ()

    inRootTranslateX = DoubleLinearField(default_value=0.0)
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField(default_value=0.0)
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField(default_value=0.0)
    rtiz = inRootTranslateZ


class InRootTranslateField(
    DoubleLinear3CompoundBaseField[
        InRootTranslateAttrOperator, InRootTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InRootTranslateAttrOperator
    PLUG_CLS = InRootTranslatePlugOperator

    inRootTranslateX = DoubleLinearField(default_value=0.0)
    rtix = inRootTranslateX

    inRootTranslateY = DoubleLinearField(default_value=0.0)
    rtiy = inRootTranslateY

    inRootTranslateZ = DoubleLinearField(default_value=0.0)
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

    inRootRotateX = DoubleAngleField(default_value=0.0)
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField(default_value=0.0)
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField(default_value=0.0)
    rriz = inRootRotateZ


class InRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InRootRotatePlugOperator]
):
    __slots__ = ()

    inRootRotateX = DoubleAngleField(default_value=0.0)
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField(default_value=0.0)
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField(default_value=0.0)
    rriz = inRootRotateZ


class InRootRotateField(
    DoubleAngle3CompoundBaseField[
        InRootRotateAttrOperator, InRootRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InRootRotateAttrOperator
    PLUG_CLS = InRootRotatePlugOperator

    inRootRotateX = DoubleAngleField(default_value=0.0)
    rrix = inRootRotateX

    inRootRotateY = DoubleAngleField(default_value=0.0)
    rriy = inRootRotateY

    inRootRotateZ = DoubleAngleField(default_value=0.0)
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

    rootJointOrientX = DoubleAngleField(default_value=0.0)
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField(default_value=0.0)
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField(default_value=0.0)
    rjoz = rootJointOrientZ


class RootJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RootJointOrientPlugOperator]
):
    __slots__ = ()

    rootJointOrientX = DoubleAngleField(default_value=0.0)
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField(default_value=0.0)
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField(default_value=0.0)
    rjoz = rootJointOrientZ


class RootJointOrientField(
    DoubleAngle3CompoundBaseField[
        RootJointOrientAttrOperator, RootJointOrientPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RootJointOrientAttrOperator
    PLUG_CLS = RootJointOrientPlugOperator

    rootJointOrientX = DoubleAngleField(default_value=0.0)
    rjox = rootJointOrientX

    rootJointOrientY = DoubleAngleField(default_value=0.0)
    rjoy = rootJointOrientY

    rootJointOrientZ = DoubleAngleField(default_value=0.0)
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

    offsetRootTranslateX = DoubleLinearField(default_value=0.0)
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField(default_value=0.0)
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField(default_value=0.0)
    rtfz = offsetRootTranslateZ


class OffsetRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetRootTranslatePlugOperator]
):
    __slots__ = ()

    offsetRootTranslateX = DoubleLinearField(default_value=0.0)
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField(default_value=0.0)
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField(default_value=0.0)
    rtfz = offsetRootTranslateZ


class OffsetRootTranslateField(
    DoubleLinear3CompoundBaseField[
        OffsetRootTranslateAttrOperator, OffsetRootTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootTranslateAttrOperator
    PLUG_CLS = OffsetRootTranslatePlugOperator

    offsetRootTranslateX = DoubleLinearField(default_value=0.0)
    rtfx = offsetRootTranslateX

    offsetRootTranslateY = DoubleLinearField(default_value=0.0)
    rtfy = offsetRootTranslateY

    offsetRootTranslateZ = DoubleLinearField(default_value=0.0)
    rtfz = offsetRootTranslateZ


class InitialOffsetRootTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "InitialOffsetRootTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialOffsetRootTranslateX", "itfx"),
        ("initialOffsetRootTranslateY", "itfy"),
        ("initialOffsetRootTranslateZ", "itfz"),
    )

    initialOffsetRootTranslateX = DoubleLinearField(default_value=0.0)
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField(default_value=0.0)
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField(default_value=0.0)
    itfz = initialOffsetRootTranslateZ


class InitialOffsetRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        InitialOffsetRootTranslatePlugOperator
    ]
):
    __slots__ = ()

    initialOffsetRootTranslateX = DoubleLinearField(default_value=0.0)
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField(default_value=0.0)
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField(default_value=0.0)
    itfz = initialOffsetRootTranslateZ


class InitialOffsetRootTranslateField(
    DoubleLinear3CompoundBaseField[
        InitialOffsetRootTranslateAttrOperator,
        InitialOffsetRootTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = InitialOffsetRootTranslateAttrOperator
    PLUG_CLS = InitialOffsetRootTranslatePlugOperator

    initialOffsetRootTranslateX = DoubleLinearField(default_value=0.0)
    itfx = initialOffsetRootTranslateX

    initialOffsetRootTranslateY = DoubleLinearField(default_value=0.0)
    itfy = initialOffsetRootTranslateY

    initialOffsetRootTranslateZ = DoubleLinearField(default_value=0.0)
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

    rotateControlScaleX = DoubleField(default_value=1.0)
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField(default_value=1.0)
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField(default_value=1.0)
    rcsz = rotateControlScaleZ


class RotateControlScaleAttrOperator(
    Double3CompoundBaseAttrOperator[RotateControlScalePlugOperator]
):
    __slots__ = ()

    rotateControlScaleX = DoubleField(default_value=1.0)
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField(default_value=1.0)
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField(default_value=1.0)
    rcsz = rotateControlScaleZ


class RotateControlScaleField(
    Double3CompoundBaseField[
        RotateControlScaleAttrOperator, RotateControlScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RotateControlScaleAttrOperator
    PLUG_CLS = RotateControlScalePlugOperator

    rotateControlScaleX = DoubleField(default_value=1.0)
    rcsx = rotateControlScaleX

    rotateControlScaleY = DoubleField(default_value=1.0)
    rcsy = rotateControlScaleY

    rotateControlScaleZ = DoubleField(default_value=1.0)
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

    offsetRootRotateX = DoubleAngleField(default_value=0.0)
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField(default_value=0.0)
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField(default_value=0.0)
    rrfz = offsetRootRotateZ


class OffsetRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OffsetRootRotatePlugOperator]
):
    __slots__ = ()

    offsetRootRotateX = DoubleAngleField(default_value=0.0)
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField(default_value=0.0)
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField(default_value=0.0)
    rrfz = offsetRootRotateZ


class OffsetRootRotateField(
    DoubleAngle3CompoundBaseField[
        OffsetRootRotateAttrOperator, OffsetRootRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootRotateAttrOperator
    PLUG_CLS = OffsetRootRotatePlugOperator

    offsetRootRotateX = DoubleAngleField(default_value=0.0)
    rrfx = offsetRootRotateX

    offsetRootRotateY = DoubleAngleField(default_value=0.0)
    rrfy = offsetRootRotateY

    offsetRootRotateZ = DoubleAngleField(default_value=0.0)
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

    offsetRootRotatePivotX = DoubleLinearField(default_value=0.0)
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField(default_value=0.0)
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField(default_value=0.0)
    rppfz = offsetRootRotatePivotZ


class OffsetRootRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetRootRotatePivotPlugOperator]
):
    __slots__ = ()

    offsetRootRotatePivotX = DoubleLinearField(default_value=0.0)
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField(default_value=0.0)
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField(default_value=0.0)
    rppfz = offsetRootRotatePivotZ


class OffsetRootRotatePivotField(
    DoubleLinear3CompoundBaseField[
        OffsetRootRotatePivotAttrOperator, OffsetRootRotatePivotPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OffsetRootRotatePivotAttrOperator
    PLUG_CLS = OffsetRootRotatePivotPlugOperator

    offsetRootRotatePivotX = DoubleLinearField(default_value=0.0)
    rppfx = offsetRootRotatePivotX

    offsetRootRotatePivotY = DoubleLinearField(default_value=0.0)
    rppfy = offsetRootRotatePivotY

    offsetRootRotatePivotZ = DoubleLinearField(default_value=0.0)
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

    outRootTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    rtoz = outRootTranslateZ


class OutRootTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutRootTranslatePlugOperator]
):
    __slots__ = ()

    outRootTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    rtoz = outRootTranslateZ


class OutRootTranslateField(
    DoubleLinear3CompoundBaseField[
        OutRootTranslateAttrOperator, OutRootTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutRootTranslateAttrOperator
    PLUG_CLS = OutRootTranslatePlugOperator

    outRootTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    rtox = outRootTranslateX

    outRootTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    rtoy = outRootTranslateY

    outRootTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
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

    outRootRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rroz = outRootRotateZ


class OutRootRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutRootRotatePlugOperator]
):
    __slots__ = ()

    outRootRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rroz = outRootRotateZ


class OutRootRotateField(
    DoubleAngle3CompoundBaseField[
        OutRootRotateAttrOperator, OutRootRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutRootRotateAttrOperator
    PLUG_CLS = OutRootRotatePlugOperator

    outRootRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rrox = outRootRotateX

    outRootRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rroy = outRootRotateY

    outRootRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rroz = outRootRotateZ
