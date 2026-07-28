# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class JointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["JointOrientAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("jointOrientX", "jox"),
        ("jointOrientY", "joy"),
        ("jointOrientZ", "joz"),
    )

    jointOrientX = DoubleAngleField(default_value=0.0)
    jox = jointOrientX

    jointOrientY = DoubleAngleField(default_value=0.0)
    joy = jointOrientY

    jointOrientZ = DoubleAngleField(default_value=0.0)
    joz = jointOrientZ


class JointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[JointOrientPlugOperator]
):
    __slots__ = ()

    jointOrientX = DoubleAngleField(default_value=0.0)
    jox = jointOrientX

    jointOrientY = DoubleAngleField(default_value=0.0)
    joy = jointOrientY

    jointOrientZ = DoubleAngleField(default_value=0.0)
    joz = jointOrientZ


class JointOrientField(
    DoubleAngle3CompoundBaseField[
        JointOrientAttrOperator, JointOrientPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = JointOrientAttrOperator
    PLUG_CLS = JointOrientPlugOperator

    jointOrientX = DoubleAngleField(default_value=0.0)
    jox = jointOrientX

    jointOrientY = DoubleAngleField(default_value=0.0)
    joy = jointOrientY

    jointOrientZ = DoubleAngleField(default_value=0.0)
    joz = jointOrientZ


class InverseScalePlugOperator(
    Double3CompoundBasePlugOperator["InverseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inverseScaleX", "isx"),
        ("inverseScaleY", "isy"),
        ("inverseScaleZ", "isz"),
    )

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


class InverseScaleAttrOperator(
    Double3CompoundBaseAttrOperator[InverseScalePlugOperator]
):
    __slots__ = ()

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


class InverseScaleField(
    Double3CompoundBaseField[
        InverseScaleAttrOperator, InverseScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InverseScaleAttrOperator
    PLUG_CLS = InverseScalePlugOperator

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


class StiffnessPlugOperator(
    Double3CompoundBasePlugOperator["StiffnessAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("stiffnessX", "stx"),
        ("stiffnessY", "sty"),
        ("stiffnessZ", "stz"),
    )

    stiffnessX = DoubleField(default_value=0.0)
    stx = stiffnessX

    stiffnessY = DoubleField(default_value=0.0)
    sty = stiffnessY

    stiffnessZ = DoubleField(default_value=0.0)
    stz = stiffnessZ


class StiffnessAttrOperator(
    Double3CompoundBaseAttrOperator[StiffnessPlugOperator]
):
    __slots__ = ()

    stiffnessX = DoubleField(default_value=0.0)
    stx = stiffnessX

    stiffnessY = DoubleField(default_value=0.0)
    sty = stiffnessY

    stiffnessZ = DoubleField(default_value=0.0)
    stz = stiffnessZ


class StiffnessField(
    Double3CompoundBaseField[StiffnessAttrOperator, StiffnessPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StiffnessAttrOperator
    PLUG_CLS = StiffnessPlugOperator

    stiffnessX = DoubleField(default_value=0.0)
    stx = stiffnessX

    stiffnessY = DoubleField(default_value=0.0)
    sty = stiffnessY

    stiffnessZ = DoubleField(default_value=0.0)
    stz = stiffnessZ


class PreferredAnglePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["PreferredAngleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preferredAngleX", "pax"),
        ("preferredAngleY", "pay"),
        ("preferredAngleZ", "paz"),
    )

    preferredAngleX = DoubleAngleField(default_value=0.0)
    pax = preferredAngleX

    preferredAngleY = DoubleAngleField(default_value=0.0)
    pay = preferredAngleY

    preferredAngleZ = DoubleAngleField(default_value=0.0)
    paz = preferredAngleZ


class PreferredAngleAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[PreferredAnglePlugOperator]
):
    __slots__ = ()

    preferredAngleX = DoubleAngleField(default_value=0.0)
    pax = preferredAngleX

    preferredAngleY = DoubleAngleField(default_value=0.0)
    pay = preferredAngleY

    preferredAngleZ = DoubleAngleField(default_value=0.0)
    paz = preferredAngleZ


class PreferredAngleField(
    DoubleAngle3CompoundBaseField[
        PreferredAngleAttrOperator, PreferredAnglePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PreferredAngleAttrOperator
    PLUG_CLS = PreferredAnglePlugOperator

    preferredAngleX = DoubleAngleField(default_value=0.0)
    pax = preferredAngleX

    preferredAngleY = DoubleAngleField(default_value=0.0)
    pay = preferredAngleY

    preferredAngleZ = DoubleAngleField(default_value=0.0)
    paz = preferredAngleZ


class MinRotateDampRangePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["MinRotateDampRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minRotateDampRangeX", "ndx"),
        ("minRotateDampRangeY", "ndy"),
        ("minRotateDampRangeZ", "ndz"),
    )

    minRotateDampRangeX = DoubleAngleField(default_value=0.0)
    ndx = minRotateDampRangeX

    minRotateDampRangeY = DoubleAngleField(default_value=0.0)
    ndy = minRotateDampRangeY

    minRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    ndz = minRotateDampRangeZ


class MinRotateDampRangeAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MinRotateDampRangePlugOperator]
):
    __slots__ = ()

    minRotateDampRangeX = DoubleAngleField(default_value=0.0)
    ndx = minRotateDampRangeX

    minRotateDampRangeY = DoubleAngleField(default_value=0.0)
    ndy = minRotateDampRangeY

    minRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    ndz = minRotateDampRangeZ


class MinRotateDampRangeField(
    DoubleAngle3CompoundBaseField[
        MinRotateDampRangeAttrOperator, MinRotateDampRangePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MinRotateDampRangeAttrOperator
    PLUG_CLS = MinRotateDampRangePlugOperator

    minRotateDampRangeX = DoubleAngleField(default_value=0.0)
    ndx = minRotateDampRangeX

    minRotateDampRangeY = DoubleAngleField(default_value=0.0)
    ndy = minRotateDampRangeY

    minRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    ndz = minRotateDampRangeZ


class MinRotateDampStrengthPlugOperator(
    Double3CompoundBasePlugOperator["MinRotateDampStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minRotateDampStrengthX", "nstx"),
        ("minRotateDampStrengthY", "nsty"),
        ("minRotateDampStrengthZ", "nstz"),
    )

    minRotateDampStrengthX = DoubleField(default_value=0.0)
    nstx = minRotateDampStrengthX

    minRotateDampStrengthY = DoubleField(default_value=0.0)
    nsty = minRotateDampStrengthY

    minRotateDampStrengthZ = DoubleField(default_value=0.0)
    nstz = minRotateDampStrengthZ


class MinRotateDampStrengthAttrOperator(
    Double3CompoundBaseAttrOperator[MinRotateDampStrengthPlugOperator]
):
    __slots__ = ()

    minRotateDampStrengthX = DoubleField(default_value=0.0)
    nstx = minRotateDampStrengthX

    minRotateDampStrengthY = DoubleField(default_value=0.0)
    nsty = minRotateDampStrengthY

    minRotateDampStrengthZ = DoubleField(default_value=0.0)
    nstz = minRotateDampStrengthZ


class MinRotateDampStrengthField(
    Double3CompoundBaseField[
        MinRotateDampStrengthAttrOperator, MinRotateDampStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MinRotateDampStrengthAttrOperator
    PLUG_CLS = MinRotateDampStrengthPlugOperator

    minRotateDampStrengthX = DoubleField(default_value=0.0)
    nstx = minRotateDampStrengthX

    minRotateDampStrengthY = DoubleField(default_value=0.0)
    nsty = minRotateDampStrengthY

    minRotateDampStrengthZ = DoubleField(default_value=0.0)
    nstz = minRotateDampStrengthZ


class MaxRotateDampRangePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["MaxRotateDampRangeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxRotateDampRangeX", "xdx"),
        ("maxRotateDampRangeY", "xdy"),
        ("maxRotateDampRangeZ", "xdz"),
    )

    maxRotateDampRangeX = DoubleAngleField(default_value=0.0)
    xdx = maxRotateDampRangeX

    maxRotateDampRangeY = DoubleAngleField(default_value=0.0)
    xdy = maxRotateDampRangeY

    maxRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    xdz = maxRotateDampRangeZ


class MaxRotateDampRangeAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MaxRotateDampRangePlugOperator]
):
    __slots__ = ()

    maxRotateDampRangeX = DoubleAngleField(default_value=0.0)
    xdx = maxRotateDampRangeX

    maxRotateDampRangeY = DoubleAngleField(default_value=0.0)
    xdy = maxRotateDampRangeY

    maxRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    xdz = maxRotateDampRangeZ


class MaxRotateDampRangeField(
    DoubleAngle3CompoundBaseField[
        MaxRotateDampRangeAttrOperator, MaxRotateDampRangePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MaxRotateDampRangeAttrOperator
    PLUG_CLS = MaxRotateDampRangePlugOperator

    maxRotateDampRangeX = DoubleAngleField(default_value=0.0)
    xdx = maxRotateDampRangeX

    maxRotateDampRangeY = DoubleAngleField(default_value=0.0)
    xdy = maxRotateDampRangeY

    maxRotateDampRangeZ = DoubleAngleField(default_value=0.0)
    xdz = maxRotateDampRangeZ


class MaxRotateDampStrengthPlugOperator(
    Double3CompoundBasePlugOperator["MaxRotateDampStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxRotateDampStrengthX", "xstx"),
        ("maxRotateDampStrengthY", "xsty"),
        ("maxRotateDampStrengthZ", "xstz"),
    )

    maxRotateDampStrengthX = DoubleField(default_value=0.0)
    xstx = maxRotateDampStrengthX

    maxRotateDampStrengthY = DoubleField(default_value=0.0)
    xsty = maxRotateDampStrengthY

    maxRotateDampStrengthZ = DoubleField(default_value=0.0)
    xstz = maxRotateDampStrengthZ


class MaxRotateDampStrengthAttrOperator(
    Double3CompoundBaseAttrOperator[MaxRotateDampStrengthPlugOperator]
):
    __slots__ = ()

    maxRotateDampStrengthX = DoubleField(default_value=0.0)
    xstx = maxRotateDampStrengthX

    maxRotateDampStrengthY = DoubleField(default_value=0.0)
    xsty = maxRotateDampStrengthY

    maxRotateDampStrengthZ = DoubleField(default_value=0.0)
    xstz = maxRotateDampStrengthZ


class MaxRotateDampStrengthField(
    Double3CompoundBaseField[
        MaxRotateDampStrengthAttrOperator, MaxRotateDampStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MaxRotateDampStrengthAttrOperator
    PLUG_CLS = MaxRotateDampStrengthPlugOperator

    maxRotateDampStrengthX = DoubleField(default_value=0.0)
    xstx = maxRotateDampStrengthX

    maxRotateDampStrengthY = DoubleField(default_value=0.0)
    xsty = maxRotateDampStrengthY

    maxRotateDampStrengthZ = DoubleField(default_value=0.0)
    xstz = maxRotateDampStrengthZ


class BindRotationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["BindRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bindRotationX", "brx"),
        ("bindRotationY", "bry"),
        ("bindRotationZ", "brz"),
    )

    bindRotationX = DoubleAngleField(default_value=0.0)
    brx = bindRotationX

    bindRotationY = DoubleAngleField(default_value=0.0)
    bry = bindRotationY

    bindRotationZ = DoubleAngleField(default_value=0.0)
    brz = bindRotationZ


class BindRotationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[BindRotationPlugOperator]
):
    __slots__ = ()

    bindRotationX = DoubleAngleField(default_value=0.0)
    brx = bindRotationX

    bindRotationY = DoubleAngleField(default_value=0.0)
    bry = bindRotationY

    bindRotationZ = DoubleAngleField(default_value=0.0)
    brz = bindRotationZ


class BindRotationField(
    DoubleAngle3CompoundBaseField[
        BindRotationAttrOperator, BindRotationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BindRotationAttrOperator
    PLUG_CLS = BindRotationPlugOperator

    bindRotationX = DoubleAngleField(default_value=0.0)
    brx = bindRotationX

    bindRotationY = DoubleAngleField(default_value=0.0)
    bry = bindRotationY

    bindRotationZ = DoubleAngleField(default_value=0.0)
    brz = bindRotationZ


class BindJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["BindJointOrientAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bindJointOrientX", "bjx"),
        ("bindJointOrientY", "bjy"),
        ("bindJointOrientZ", "bjz"),
    )

    bindJointOrientX = DoubleAngleField(default_value=0.0)
    bjx = bindJointOrientX

    bindJointOrientY = DoubleAngleField(default_value=0.0)
    bjy = bindJointOrientY

    bindJointOrientZ = DoubleAngleField(default_value=0.0)
    bjz = bindJointOrientZ


class BindJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[BindJointOrientPlugOperator]
):
    __slots__ = ()

    bindJointOrientX = DoubleAngleField(default_value=0.0)
    bjx = bindJointOrientX

    bindJointOrientY = DoubleAngleField(default_value=0.0)
    bjy = bindJointOrientY

    bindJointOrientZ = DoubleAngleField(default_value=0.0)
    bjz = bindJointOrientZ


class BindJointOrientField(
    DoubleAngle3CompoundBaseField[
        BindJointOrientAttrOperator, BindJointOrientPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BindJointOrientAttrOperator
    PLUG_CLS = BindJointOrientPlugOperator

    bindJointOrientX = DoubleAngleField(default_value=0.0)
    bjx = bindJointOrientX

    bindJointOrientY = DoubleAngleField(default_value=0.0)
    bjy = bindJointOrientY

    bindJointOrientZ = DoubleAngleField(default_value=0.0)
    bjz = bindJointOrientZ


class BindRotateAxisPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["BindRotateAxisAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bindRotateAxisX", "brax"),
        ("bindRotateAxisY", "bray"),
        ("bindRotateAxisZ", "braz"),
    )

    bindRotateAxisX = DoubleAngleField(default_value=0.0)
    brax = bindRotateAxisX

    bindRotateAxisY = DoubleAngleField(default_value=0.0)
    bray = bindRotateAxisY

    bindRotateAxisZ = DoubleAngleField(default_value=0.0)
    braz = bindRotateAxisZ


class BindRotateAxisAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[BindRotateAxisPlugOperator]
):
    __slots__ = ()

    bindRotateAxisX = DoubleAngleField(default_value=0.0)
    brax = bindRotateAxisX

    bindRotateAxisY = DoubleAngleField(default_value=0.0)
    bray = bindRotateAxisY

    bindRotateAxisZ = DoubleAngleField(default_value=0.0)
    braz = bindRotateAxisZ


class BindRotateAxisField(
    DoubleAngle3CompoundBaseField[
        BindRotateAxisAttrOperator, BindRotateAxisPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BindRotateAxisAttrOperator
    PLUG_CLS = BindRotateAxisPlugOperator

    bindRotateAxisX = DoubleAngleField(default_value=0.0)
    brax = bindRotateAxisX

    bindRotateAxisY = DoubleAngleField(default_value=0.0)
    bray = bindRotateAxisY

    bindRotateAxisZ = DoubleAngleField(default_value=0.0)
    braz = bindRotateAxisZ


class BindScalePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["BindScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bindScaleX", "bsx"),
        ("bindScaleY", "bsy"),
        ("bindScaleZ", "bsz"),
    )

    bindScaleX = DoubleAngleField(default_value=57.29577951308232)
    bsx = bindScaleX

    bindScaleY = DoubleAngleField(default_value=57.29577951308232)
    bsy = bindScaleY

    bindScaleZ = DoubleAngleField(default_value=57.29577951308232)
    bsz = bindScaleZ


class BindScaleAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[BindScalePlugOperator]
):
    __slots__ = ()

    bindScaleX = DoubleAngleField(default_value=57.29577951308232)
    bsx = bindScaleX

    bindScaleY = DoubleAngleField(default_value=57.29577951308232)
    bsy = bindScaleY

    bindScaleZ = DoubleAngleField(default_value=57.29577951308232)
    bsz = bindScaleZ


class BindScaleField(
    DoubleAngle3CompoundBaseField[BindScaleAttrOperator, BindScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BindScaleAttrOperator
    PLUG_CLS = BindScalePlugOperator

    bindScaleX = DoubleAngleField(default_value=57.29577951308232)
    bsx = bindScaleX

    bindScaleY = DoubleAngleField(default_value=57.29577951308232)
    bsy = bindScaleY

    bindScaleZ = DoubleAngleField(default_value=57.29577951308232)
    bsz = bindScaleZ


class BindInverseScalePlugOperator(
    Double3CompoundBasePlugOperator["BindInverseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("bindInverseScaleX", "bix"),
        ("bindInverseScaleY", "biy"),
        ("bindInverseScaleZ", "biz"),
    )

    bindInverseScaleX = DoubleField(default_value=1.0)
    bix = bindInverseScaleX

    bindInverseScaleY = DoubleField(default_value=1.0)
    biy = bindInverseScaleY

    bindInverseScaleZ = DoubleField(default_value=1.0)
    biz = bindInverseScaleZ


class BindInverseScaleAttrOperator(
    Double3CompoundBaseAttrOperator[BindInverseScalePlugOperator]
):
    __slots__ = ()

    bindInverseScaleX = DoubleField(default_value=1.0)
    bix = bindInverseScaleX

    bindInverseScaleY = DoubleField(default_value=1.0)
    biy = bindInverseScaleY

    bindInverseScaleZ = DoubleField(default_value=1.0)
    biz = bindInverseScaleZ


class BindInverseScaleField(
    Double3CompoundBaseField[
        BindInverseScaleAttrOperator, BindInverseScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BindInverseScaleAttrOperator
    PLUG_CLS = BindInverseScalePlugOperator

    bindInverseScaleX = DoubleField(default_value=1.0)
    bix = bindInverseScaleX

    bindInverseScaleY = DoubleField(default_value=1.0)
    biy = bindInverseScaleY

    bindInverseScaleZ = DoubleField(default_value=1.0)
    biz = bindInverseScaleZ


class IkRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["IkRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ikRotateX", "irx"),
        ("ikRotateY", "iry"),
        ("ikRotateZ", "irz"),
    )

    ikRotateX = DoubleAngleField(default_value=0.0)
    irx = ikRotateX

    ikRotateY = DoubleAngleField(default_value=0.0)
    iry = ikRotateY

    ikRotateZ = DoubleAngleField(default_value=0.0)
    irz = ikRotateZ


class IkRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[IkRotatePlugOperator]
):
    __slots__ = ()

    ikRotateX = DoubleAngleField(default_value=0.0)
    irx = ikRotateX

    ikRotateY = DoubleAngleField(default_value=0.0)
    iry = ikRotateY

    ikRotateZ = DoubleAngleField(default_value=0.0)
    irz = ikRotateZ


class IkRotateField(
    DoubleAngle3CompoundBaseField[IkRotateAttrOperator, IkRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IkRotateAttrOperator
    PLUG_CLS = IkRotatePlugOperator

    ikRotateX = DoubleAngleField(default_value=0.0)
    irx = ikRotateX

    ikRotateY = DoubleAngleField(default_value=0.0)
    iry = ikRotateY

    ikRotateZ = DoubleAngleField(default_value=0.0)
    irz = ikRotateZ


class FkRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["FkRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fkRotateX", "frx"),
        ("fkRotateY", "fry"),
        ("fkRotateZ", "frz"),
    )

    fkRotateX = DoubleAngleField(default_value=0.0)
    frx = fkRotateX

    fkRotateY = DoubleAngleField(default_value=0.0)
    fry = fkRotateY

    fkRotateZ = DoubleAngleField(default_value=0.0)
    frz = fkRotateZ


class FkRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[FkRotatePlugOperator]
):
    __slots__ = ()

    fkRotateX = DoubleAngleField(default_value=0.0)
    frx = fkRotateX

    fkRotateY = DoubleAngleField(default_value=0.0)
    fry = fkRotateY

    fkRotateZ = DoubleAngleField(default_value=0.0)
    frz = fkRotateZ


class FkRotateField(
    DoubleAngle3CompoundBaseField[FkRotateAttrOperator, FkRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FkRotateAttrOperator
    PLUG_CLS = FkRotatePlugOperator

    fkRotateX = DoubleAngleField(default_value=0.0)
    frx = fkRotateX

    fkRotateY = DoubleAngleField(default_value=0.0)
    fry = fkRotateY

    fkRotateZ = DoubleAngleField(default_value=0.0)
    frz = fkRotateZ
