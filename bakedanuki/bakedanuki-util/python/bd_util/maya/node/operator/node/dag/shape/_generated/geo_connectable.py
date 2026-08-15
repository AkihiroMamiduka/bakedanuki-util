# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class GeneratedGeoConnectable(Shape):
    __slots__ = ()

    NODE_TYPE = "geoConnectable"

    connectionsToMe = MessageField(multi=True)
    ct = connectionsToMe

    auxiliariesOwned = MessageField()
    ao = auxiliariesOwned

    velocityValid = BoolField(default_value=False)
    vv = velocityValid

    doVelocity = BoolField(default_value=False)
    dv = doVelocity

    prevTime = DoubleField(default_value=0.0)
    pt = prevTime

    cachedPositions = DataVectorArrayField()
    cpo = cachedPositions

    cachedVelocities = DataVectorArrayField()
    cve = cachedVelocities

    componentPositions = BoolField(multi=True, default_value=False)
    cpp = componentPositions

    groupId = LongField(multi=True, default_value=0)
    gri = groupId

    inputGeometryMsg = MessageField()
    igm = inputGeometryMsg

    surfaceGeometry = GenericField()
    sge = surfaceGeometry

    localSurfaceGeometry = GenericField()
    lsg = localSurfaceGeometry
