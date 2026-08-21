# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.time import TimeField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
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
    Double3CompoundBaseField[
        InitialPositionAttrOperator, InitialPositionPlugOperator
    ]
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


class LastPositionPlugOperator(
    Double3CompoundBasePlugOperator["LastPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastPositionX", "lpx"),
        ("lastPositionY", "lpy"),
        ("lastPositionZ", "lpz"),
    )

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastPositionAttrOperator(
    Double3CompoundBaseAttrOperator[LastPositionPlugOperator]
):
    __slots__ = ()

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastPositionField(
    Double3CompoundBaseField[
        LastPositionAttrOperator, LastPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LastPositionAttrOperator
    PLUG_CLS = LastPositionPlugOperator

    lastPositionX = DoubleField(default_value=0.0, writable=False)
    lpx = lastPositionX

    lastPositionY = DoubleField(default_value=0.0, writable=False)
    lpy = lastPositionY

    lastPositionZ = DoubleField(default_value=0.0, writable=False)
    lpz = lastPositionZ


class LastRotationPlugOperator(
    Double3CompoundBasePlugOperator["LastRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastRotationX", "lrx"),
        ("lastRotationY", "lry"),
        ("lastRotationZ", "lrz"),
    )

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


class LastRotationAttrOperator(
    Double3CompoundBaseAttrOperator[LastRotationPlugOperator]
):
    __slots__ = ()

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


class LastRotationField(
    Double3CompoundBaseField[
        LastRotationAttrOperator, LastRotationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LastRotationAttrOperator
    PLUG_CLS = LastRotationPlugOperator

    lastRotationX = DoubleField(default_value=0.0, writable=False)
    lrx = lastRotationX

    lastRotationY = DoubleField(default_value=0.0, writable=False)
    lry = lastRotationY

    lastRotationZ = DoubleField(default_value=0.0, writable=False)
    lrz = lastRotationZ


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
    DoubleAngle3CompoundBaseField[
        InitialOrientationAttrOperator, InitialOrientationPlugOperator
    ]
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


class InitialVelocityPlugOperator(
    Double3CompoundBasePlugOperator["InitialVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialVelocityX", "ivx"),
        ("initialVelocityY", "ivy"),
        ("initialVelocityZ", "ivz"),
    )

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialVelocityAttrOperator(
    Double3CompoundBaseAttrOperator[InitialVelocityPlugOperator]
):
    __slots__ = ()

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialVelocityField(
    Double3CompoundBaseField[
        InitialVelocityAttrOperator, InitialVelocityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InitialVelocityAttrOperator
    PLUG_CLS = InitialVelocityPlugOperator

    initialVelocityX = DoubleField(default_value=0.0)
    ivx = initialVelocityX

    initialVelocityY = DoubleField(default_value=0.0)
    ivy = initialVelocityY

    initialVelocityZ = DoubleField(default_value=0.0)
    ivz = initialVelocityZ


class InitialSpinPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InitialSpinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialSpinX", "isx"),
        ("initialSpinY", "isy"),
        ("initialSpinZ", "isz"),
    )

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class InitialSpinAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InitialSpinPlugOperator]
):
    __slots__ = ()

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class InitialSpinField(
    DoubleAngle3CompoundBaseField[
        InitialSpinAttrOperator, InitialSpinPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InitialSpinAttrOperator
    PLUG_CLS = InitialSpinPlugOperator

    initialSpinX = DoubleAngleField(default_value=0.0)
    isx = initialSpinX

    initialSpinY = DoubleAngleField(default_value=0.0)
    isy = initialSpinY

    initialSpinZ = DoubleAngleField(default_value=0.0)
    isz = initialSpinZ


class CenterOfMassPlugOperator(
    Double3CompoundBasePlugOperator["CenterOfMassAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerOfMassX", "cmx"),
        ("centerOfMassY", "cmy"),
        ("centerOfMassZ", "cmz"),
    )

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class CenterOfMassAttrOperator(
    Double3CompoundBaseAttrOperator[CenterOfMassPlugOperator]
):
    __slots__ = ()

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class CenterOfMassField(
    Double3CompoundBaseField[
        CenterOfMassAttrOperator, CenterOfMassPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CenterOfMassAttrOperator
    PLUG_CLS = CenterOfMassPlugOperator

    centerOfMassX = DoubleField(default_value=0.0)
    cmx = centerOfMassX

    centerOfMassY = DoubleField(default_value=0.0)
    cmy = centerOfMassY

    centerOfMassZ = DoubleField(default_value=0.0)
    cmz = centerOfMassZ


class ImpulsePlugOperator(
    Double3CompoundBasePlugOperator["ImpulseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("impulseX", "imx"),
        ("impulseY", "imy"),
        ("impulseZ", "imz"),
    )

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulseAttrOperator(
    Double3CompoundBaseAttrOperator[ImpulsePlugOperator]
):
    __slots__ = ()

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulseField(
    Double3CompoundBaseField[ImpulseAttrOperator, ImpulsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImpulseAttrOperator
    PLUG_CLS = ImpulsePlugOperator

    impulseX = DoubleField(default_value=0.0)
    imx = impulseX

    impulseY = DoubleField(default_value=0.0)
    imy = impulseY

    impulseZ = DoubleField(default_value=0.0)
    imz = impulseZ


class ImpulsePositionPlugOperator(
    Double3CompoundBasePlugOperator["ImpulsePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("impulsePositionX", "pix"),
        ("impulsePositionY", "piy"),
        ("impulsePositionZ", "piz"),
    )

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class ImpulsePositionAttrOperator(
    Double3CompoundBaseAttrOperator[ImpulsePositionPlugOperator]
):
    __slots__ = ()

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class ImpulsePositionField(
    Double3CompoundBaseField[
        ImpulsePositionAttrOperator, ImpulsePositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ImpulsePositionAttrOperator
    PLUG_CLS = ImpulsePositionPlugOperator

    impulsePositionX = DoubleField(default_value=0.0)
    pix = impulsePositionX

    impulsePositionY = DoubleField(default_value=0.0)
    piy = impulsePositionY

    impulsePositionZ = DoubleField(default_value=0.0)
    piz = impulsePositionZ


class SpinImpulsePlugOperator(
    Double3CompoundBasePlugOperator["SpinImpulseAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spinImpulseX", "six"),
        ("spinImpulseY", "siy"),
        ("spinImpulseZ", "siz"),
    )

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class SpinImpulseAttrOperator(
    Double3CompoundBaseAttrOperator[SpinImpulsePlugOperator]
):
    __slots__ = ()

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class SpinImpulseField(
    Double3CompoundBaseField[SpinImpulseAttrOperator, SpinImpulsePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpinImpulseAttrOperator
    PLUG_CLS = SpinImpulsePlugOperator

    spinImpulseX = DoubleField(default_value=0.0)
    six = spinImpulseX

    spinImpulseY = DoubleField(default_value=0.0)
    siy = spinImpulseY

    spinImpulseZ = DoubleField(default_value=0.0)
    siz = spinImpulseZ


class VelocityPlugOperator(
    Double3CompoundBasePlugOperator["VelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("velocityX", "vx"),
        ("velocityY", "vy"),
        ("velocityZ", "vz"),
    )

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class VelocityAttrOperator(
    Double3CompoundBaseAttrOperator[VelocityPlugOperator]
):
    __slots__ = ()

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class VelocityField(
    Double3CompoundBaseField[VelocityAttrOperator, VelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VelocityAttrOperator
    PLUG_CLS = VelocityPlugOperator

    velocityX = DoubleField(default_value=0.0, writable=False)
    vx = velocityX

    velocityY = DoubleField(default_value=0.0, writable=False)
    vy = velocityY

    velocityZ = DoubleField(default_value=0.0, writable=False)
    vz = velocityZ


class SpinPlugOperator(Double3CompoundBasePlugOperator["SpinAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("spinX", "spx"),
        ("spinY", "spy"),
        ("spinZ", "spz"),
    )

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class SpinAttrOperator(Double3CompoundBaseAttrOperator[SpinPlugOperator]):
    __slots__ = ()

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class SpinField(Double3CompoundBaseField[SpinAttrOperator, SpinPlugOperator]):
    __slots__ = ()

    ATTR_CLS = SpinAttrOperator
    PLUG_CLS = SpinPlugOperator

    spinX = DoubleField(default_value=0.0, writable=False)
    spx = spinX

    spinY = DoubleField(default_value=0.0, writable=False)
    spy = spinY

    spinZ = DoubleField(default_value=0.0, writable=False)
    spz = spinZ


class ContactPositionPlugOperator(
    Double3CompoundBasePlugOperator["ContactPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("contactX", "cnx"),
        ("contactY", "cny"),
        ("contactZ", "cnz"),
    )

    contactX = DoubleField(default_value=0.0)
    cnx = contactX

    contactY = DoubleField(default_value=0.0)
    cny = contactY

    contactZ = DoubleField(default_value=0.0)
    cnz = contactZ


class ContactPositionAttrOperator(
    Double3CompoundBaseAttrOperator[ContactPositionPlugOperator]
):
    __slots__ = ()

    contactX = DoubleField(default_value=0.0)
    cnx = contactX

    contactY = DoubleField(default_value=0.0)
    cny = contactY

    contactZ = DoubleField(default_value=0.0)
    cnz = contactZ


class ContactPositionField(
    Double3CompoundBaseField[
        ContactPositionAttrOperator, ContactPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ContactPositionAttrOperator
    PLUG_CLS = ContactPositionPlugOperator


class ForcePlugOperator(Double3CompoundBasePlugOperator["ForceAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceX", "fx"),
        ("forceY", "fy"),
        ("forceZ", "fz"),
    )

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class ForceAttrOperator(Double3CompoundBaseAttrOperator[ForcePlugOperator]):
    __slots__ = ()

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class ForceField(
    Double3CompoundBaseField[ForceAttrOperator, ForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceAttrOperator
    PLUG_CLS = ForcePlugOperator

    forceX = DoubleField(default_value=0.0, writable=False)
    fx = forceX

    forceY = DoubleField(default_value=0.0, writable=False)
    fy = forceY

    forceZ = DoubleField(default_value=0.0, writable=False)
    fz = forceZ


class TorquePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["TorqueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("torqueX", "trx"),
        ("torqueY", "try"),
        ("torqueZ", "trz"),
    )

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class TorqueAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[TorquePlugOperator]
):
    __slots__ = ()

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class TorqueField(
    DoubleAngle3CompoundBaseField[TorqueAttrOperator, TorquePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TorqueAttrOperator
    PLUG_CLS = TorquePlugOperator

    torqueX = DoubleAngleField(default_value=0.0, writable=False)
    trx = torqueX

    torqueY = DoubleAngleField(default_value=0.0, writable=False)
    try_ = torqueY

    torqueZ = DoubleAngleField(default_value=0.0, writable=False)
    trz = torqueZ


class FieldDataPlugOperator(CompoundPlugOperator["FieldDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("deltaTime", "dt"),
    )

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class FieldDataAttrOperator(CompoundAttrOperator[FieldDataPlugOperator]):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField()
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField()
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField()
    fdm = fieldDataMass

    deltaTime = TimeField(default_value=0.0)
    dt = deltaTime


class GeneralForcePlugOperator(
    CompoundPlugOperator["GeneralForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputForce", "ofr"),
        ("outputTorque", "otr"),
    )

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque


class GeneralForceAttrOperator(CompoundAttrOperator[GeneralForcePlugOperator]):
    __slots__ = ()

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque


class GeneralForceField(
    CompoundField[GeneralForceAttrOperator, GeneralForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeneralForceAttrOperator
    PLUG_CLS = GeneralForcePlugOperator

    outputForce = DataVectorArrayField()
    ofr = outputForce

    outputTorque = DataVectorArrayField()
    otr = outputTorque
