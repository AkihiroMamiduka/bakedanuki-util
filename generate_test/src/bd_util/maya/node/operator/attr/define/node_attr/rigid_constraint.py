# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
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


class InitialPositionPlugOperator(
    Double3CompoundBasePlugOperator["InitialPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialPositionX", "ipx"),
        ("initialPositionY", "ipy"),
        ("initialPositionZ", "ipz"),
    )

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class InitialPositionAttrOperator(
    Double3CompoundBaseAttrOperator[InitialPositionPlugOperator]
):
    __slots__ = ()

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class InitialPositionField(
    Double3CompoundBaseField[InitialPositionAttrOperator, InitialPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialPositionAttrOperator
    PLUG_CLS = InitialPositionPlugOperator

    initialPositionX = DoubleField(default_value=0.0)
    ipx = initialPositionX

    initialPositionY = DoubleField(default_value=0.0)
    ipy = initialPositionY

    initialPositionZ = DoubleField(default_value=0.0)
    ipz = initialPositionZ


class VelocityPlugOperator(
    Double3CompoundBasePlugOperator["VelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityX", "vlx"),
        ("velocityY", "vly"),
        ("velocityZ", "vlz"),
    )

    velocityX = DoubleField(default_value=0.0, writable=False)
    vlx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vly = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vlz = velocityZ


class VelocityAttrOperator(
    Double3CompoundBaseAttrOperator[VelocityPlugOperator]
):
    __slots__ = ()

    velocityX = DoubleField(default_value=0.0, writable=False)
    vlx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vly = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vlz = velocityZ


class VelocityField(
    Double3CompoundBaseField[VelocityAttrOperator, VelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityAttrOperator
    PLUG_CLS = VelocityPlugOperator

    velocityX = DoubleField(default_value=0.0, writable=False)
    vlx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vly = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vlz = velocityZ


class AngularVelocityPlugOperator(
    Double3CompoundBasePlugOperator["AngularVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("angularVelocityX", "avx"),
        ("angularVelocityY", "avy"),
        ("angularVelocityZ", "avz"),
    )

    angularVelocityX = DoubleField(default_value=0.0, writable=False)
    avx = angularVelocityX

    angularVelocityY = DoubleField(default_value=0.0, writable=False)
    avy = angularVelocityY

    angularVelocityZ = DoubleField(default_value=0.0, writable=False)
    avz = angularVelocityZ


class AngularVelocityAttrOperator(
    Double3CompoundBaseAttrOperator[AngularVelocityPlugOperator]
):
    __slots__ = ()

    angularVelocityX = DoubleField(default_value=0.0, writable=False)
    avx = angularVelocityX

    angularVelocityY = DoubleField(default_value=0.0, writable=False)
    avy = angularVelocityY

    angularVelocityZ = DoubleField(default_value=0.0, writable=False)
    avz = angularVelocityZ


class AngularVelocityField(
    Double3CompoundBaseField[AngularVelocityAttrOperator, AngularVelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AngularVelocityAttrOperator
    PLUG_CLS = AngularVelocityPlugOperator

    angularVelocityX = DoubleField(default_value=0.0, writable=False)
    avx = angularVelocityX

    angularVelocityY = DoubleField(default_value=0.0, writable=False)
    avy = angularVelocityY

    angularVelocityZ = DoubleField(default_value=0.0, writable=False)
    avz = angularVelocityZ


class InitialOrientationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InitialOrientationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialOrientationX", "iox"),
        ("initialOrientationY", "ioy"),
        ("initialOrientationZ", "ioz"),
    )

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class InitialOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InitialOrientationPlugOperator]
):
    __slots__ = ()

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class InitialOrientationField(
    DoubleAngle3CompoundBaseField[InitialOrientationAttrOperator, InitialOrientationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialOrientationAttrOperator
    PLUG_CLS = InitialOrientationPlugOperator

    initialOrientationX = DoubleAngleField(default_value=0.0)
    iox = initialOrientationX

    initialOrientationY = DoubleAngleField(default_value=0.0)
    ioy = initialOrientationY

    initialOrientationZ = DoubleAngleField(default_value=0.0)
    ioz = initialOrientationZ


class ForcePlugOperator(
    Double3CompoundBasePlugOperator["ForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceX", "frx"),
        ("forceY", "fry"),
        ("forceZ", "frz"),
    )

    forceX = DoubleField(default_value=0.0, writable=False)
    frx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fry = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    frz = forceZ


class ForceAttrOperator(
    Double3CompoundBaseAttrOperator[ForcePlugOperator]
):
    __slots__ = ()

    forceX = DoubleField(default_value=0.0, writable=False)
    frx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fry = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    frz = forceZ


class ForceField(
    Double3CompoundBaseField[ForceAttrOperator, ForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceAttrOperator
    PLUG_CLS = ForcePlugOperator

    forceX = DoubleField(default_value=0.0, writable=False)
    frx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fry = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    frz = forceZ


class UserDefinedPositionPlugOperator(
    Double3CompoundBasePlugOperator["UserDefinedPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("userDefinedPositionX", "upx"),
        ("userDefinedPositionY", "upy"),
        ("userDefinedPositionZ", "upz"),
    )

    userDefinedPositionX = DoubleField(default_value=0.0)
    upx = userDefinedPositionX

    userDefinedPositionY = DoubleField(default_value=0.0)
    upy = userDefinedPositionY

    userDefinedPositionZ = DoubleField(default_value=0.0)
    upz = userDefinedPositionZ


class UserDefinedPositionAttrOperator(
    Double3CompoundBaseAttrOperator[UserDefinedPositionPlugOperator]
):
    __slots__ = ()

    userDefinedPositionX = DoubleField(default_value=0.0)
    upx = userDefinedPositionX

    userDefinedPositionY = DoubleField(default_value=0.0)
    upy = userDefinedPositionY

    userDefinedPositionZ = DoubleField(default_value=0.0)
    upz = userDefinedPositionZ


class UserDefinedPositionField(
    Double3CompoundBaseField[UserDefinedPositionAttrOperator, UserDefinedPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UserDefinedPositionAttrOperator
    PLUG_CLS = UserDefinedPositionPlugOperator

    userDefinedPositionX = DoubleField(default_value=0.0)
    upx = userDefinedPositionX

    userDefinedPositionY = DoubleField(default_value=0.0)
    upy = userDefinedPositionY

    userDefinedPositionZ = DoubleField(default_value=0.0)
    upz = userDefinedPositionZ
