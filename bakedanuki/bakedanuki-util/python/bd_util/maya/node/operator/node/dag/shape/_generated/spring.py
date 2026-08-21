# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.spring import IdMappingField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.double_array import DataDoubleArrayField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class GeneratedSpring(Shape):
    __slots__ = ()

    NODE_TYPE = "spring"

    end1Weight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    f = end1Weight

    end2Weight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    t = end2Weight

    useStiffnessPS = BoolField(default_value=True)
    usps = useStiffnessPS

    useDampingPS = BoolField(default_value=True)
    udps = useDampingPS

    useRestLengthPS = BoolField(default_value=True)
    urps = useRestLengthPS

    stiffness = DoubleField(
        default_value=1.0, min_value=0.0, soft_max_value=20.0
    )
    s = stiffness

    damping = DoubleField(
        default_value=0.2, min_value=0.0, soft_max_value=20.0
    )
    d = damping

    restLength = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=20.0
    )
    r = restLength

    stiffnessPS = DataDoubleArrayField()
    sps = stiffnessPS

    dampingPS = DataDoubleArrayField()
    dps = dampingPS

    restLengthPS = DataDoubleArrayField()
    rps = restLengthPS

    objectPositions = DataVectorArrayField(multi=True)
    opos = objectPositions

    objectVelocities = DataVectorArrayField(multi=True)
    ovel = objectVelocities

    objectMass = DataDoubleArrayField(multi=True)
    omas = objectMass

    deltaTime = TimeField(multi=True, default_value=0.0)
    dt = deltaTime

    outputForce = DataVectorArrayField(multi=True, writable=False)
    of = outputForce

    validIndex = TypedField()
    vali = validIndex

    object0 = TypedField()
    obz = object0

    point0 = TypedField()
    ptz = point0

    object1 = TypedField()
    obo = object1

    point1 = TypedField()
    pto = point1

    minSprings = LongField(default_value=0)
    ms = minSprings

    manageParticleDeath = BoolField(default_value=True)
    mpd = manageParticleDeath

    idMapping = IdMappingField(multi=True)
    idm = idMapping

    count = LongField(default_value=0, writable=False)
    cnt = count

    objects = MessageField(multi=True)
    obj = objects

    objCount = LongField(default_value=0)
    obc = objCount

    lengths = DataDoubleArrayField()
    lns = lengths

    minUsed = DoubleField(default_value=0.0)
    mnu = minUsed

    maxUsed = DoubleField(default_value=0.0)
    mxu = maxUsed

    pt0Index = DataDoubleArrayField()
    pzi = pt0Index

    pt1Index = DataDoubleArrayField()
    poi = pt1Index

    obj0Index = DataDoubleArrayField()
    ozi = obj0Index

    obj1Index = DataDoubleArrayField()
    ooi = obj1Index
