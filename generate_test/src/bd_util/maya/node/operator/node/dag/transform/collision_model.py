# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.collision_model import OwnerCentroidField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class CollisionModel(Transform):
    __slots__ = ()

    NODE_TYPE = "collisionModel"

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

    resilience = DoubleField(default_value=1.0)
    res = resilience

    friction = DoubleField(default_value=0.0)
    fri = friction
