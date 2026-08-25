# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.volume_axis_field import (
    AxialMagnitudeField,
    CurveRadiusField,
    DirectionField,
    FalloffCurveField,
    InputDataField,
    OwnerCentroidField,
    TurbulenceFrequencyField,
    TurbulenceOffsetField,
    VolumeOffsetField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class VolumeShapeEnumPlugOperator(
    EnumPlugOperator["VolumeShapeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    CUBE = 1
    SPHERE = 2
    CYLINDER = 3
    CONE = 4
    TORUS = 5
    CURVE = 7


class VolumeShapeEnumAttrOperator(
    EnumAttrOperator[VolumeShapeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    CUBE = 1
    SPHERE = 2
    CYLINDER = 3
    CONE = 4
    TORUS = 5
    CURVE = 7

    NAME_MAP = {
        NONE: "None",
        CUBE: "Cube",
        SPHERE: "Sphere",
        CYLINDER: "Cylinder",
        CONE: "Cone",
        TORUS: "Torus",
        CURVE: "Curve",
    }


class VolumeShapeEnumField(
    EnumField[VolumeShapeEnumAttrOperator, VolumeShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeShapeEnumAttrOperator
    PLUG_CLS = VolumeShapeEnumPlugOperator


class GeneratedVolumeAxisField(Transform):
    __slots__ = ()

    NODE_TYPE = "volumeAxisField"

    owner = MessageField()
    ow = owner

    fromWhere = ShortField(default_value=0)
    fw = fromWhere

    subsetId = LongField(default_value=-1)
    sid = subsetId

    positional = BoolField(default_value=False, writable=False)
    psl = positional

    ownerCentroid = OwnerCentroidField(default_value=(0.0, 0.0, 0.0))
    ocd = ownerCentroid
    ownerCentroidX = ownerCentroid.ownerCentroidX
    ocx = ownerCentroidX
    ownerCentroidY = ownerCentroid.ownerCentroidY
    ocy = ownerCentroidY
    ownerCentroidZ = ownerCentroid.ownerCentroidZ
    ocz = ownerCentroidZ

    ownerPosData = DataVectorArrayField()
    opd = ownerPosData

    ownerVelData = DataVectorArrayField()
    ovd = ownerVelData

    magnitude = DoubleField(
        default_value=1.0, soft_min_value=-100.0, soft_max_value=100.0
    )
    mag = magnitude

    attenuation = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=5.0
    )
    att = attenuation

    maxDistance = DoubleLinearField(
        default_value=-1.0, min_value=0.0, soft_max_value=100.0
    )
    max = maxDistance

    applyPerVertex = BoolField(default_value=False)
    apv = applyPerVertex

    useMaxDistance = BoolField(default_value=False)
    umd = useMaxDistance

    inputData = InputDataField(multi=True)
    ind = inputData

    inputForce = DataVectorArrayField(multi=True)
    inf = inputForce

    outputForce = DataVectorArrayField(multi=True, writable=False)
    of = outputForce

    volumeShape = VolumeShapeEnumField(default_value=0)
    vol = volumeShape

    volumeExclusion = BoolField(default_value=False)
    vex = volumeExclusion

    trapInside = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    trin = trapInside

    trapRadius = DoubleField(
        default_value=2.0, soft_min_value=0.0, soft_max_value=10.0
    )
    trra = trapRadius

    trapEnds = BoolField(default_value=True)
    ten = trapEnds

    volumeOffset = VolumeOffsetField(default_value=(0.0, 0.0, 0.0))
    vfo = volumeOffset
    volumeOffsetX = volumeOffset.volumeOffsetX
    vox = volumeOffsetX
    volumeOffsetY = volumeOffset.volumeOffsetY
    voy = volumeOffsetY
    volumeOffsetZ = volumeOffset.volumeOffsetZ
    voz = volumeOffsetZ

    sectionRadius = DoubleLinearField(
        default_value=0.5, min_value=0.0, soft_max_value=1.0
    )
    tsr = sectionRadius

    volumeSweep = DoubleAngleField(
        default_value=360.0, min_value=0.0, max_value=360.0
    )
    vsw = volumeSweep

    inputPPData = TypedField(multi=True)
    ppda = inputPPData

    ownerPPData = TypedField()
    oppd = ownerPPData

    falloffCurve = FalloffCurveField(multi=True, default_value=(0.0, 0.0, 0))
    fc = falloffCurve

    axialMagnitude = AxialMagnitudeField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    amag = axialMagnitude

    curveRadius = CurveRadiusField(multi=True, default_value=(0.0, 0.0, 0))
    crad = curveRadius

    inputCurve = DataNurbsCurveField()
    icv = inputCurve

    invertAttenuation = BoolField(default_value=False)
    ia = invertAttenuation

    awayFromCenter = DoubleField(
        default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    afc = awayFromCenter

    awayFromAxis = DoubleField(
        default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    afa = awayFromAxis

    alongAxis = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    alx = alongAxis

    aroundAxis = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    arx = aroundAxis

    directionalSpeed = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    drs = directionalSpeed

    direction = DirectionField(
        default_value=(1.0, 0.0, 0.0),
        soft_min_value=(-10.0, -10.0, -10.0),
        soft_max_value=(10.0, 10.0, 10.0),
    )
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    displaySpeed = BoolField(default_value=True)
    dss = displaySpeed

    turbulence = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    trb = turbulence

    turbulenceSpeed = DoubleField(
        default_value=0.2, soft_min_value=0.0, soft_max_value=1.0
    )
    trs = turbulenceSpeed

    turbulenceFrequency = TurbulenceFrequencyField(
        default_value=(1.0, 1.0, 1.0),
        soft_min_value=(0.0, 0.0, 0.0),
        soft_max_value=(10.0, 10.0, 10.0),
    )
    tf = turbulenceFrequency
    turbulenceFrequencyX = turbulenceFrequency.turbulenceFrequencyX
    tfx = turbulenceFrequencyX
    turbulenceFrequencyY = turbulenceFrequency.turbulenceFrequencyY
    tfy = turbulenceFrequencyY
    turbulenceFrequencyZ = turbulenceFrequency.turbulenceFrequencyZ
    tfz = turbulenceFrequencyZ

    turbulenceOffset = TurbulenceOffsetField(
        default_value=(0.0, 0.0, 0.0),
        soft_min_value=(-10.0, -10.0, -10.0),
        soft_max_value=(10.0, 10.0, 10.0),
    )
    to = turbulenceOffset
    turbulenceOffsetX = turbulenceOffset.turbulenceOffsetX
    tox = turbulenceOffsetX
    turbulenceOffsetY = turbulenceOffset.turbulenceOffsetY
    toy = turbulenceOffsetY
    turbulenceOffsetZ = turbulenceOffset.turbulenceOffsetZ
    toz = turbulenceOffsetZ

    detailTurbulence = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dtr = detailTurbulence

    time = TimeField(default_value=0.0)
    tim = time
