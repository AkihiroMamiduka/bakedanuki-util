# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.geo_connector import (
    ComponentCentroidField,
    ComponentCentroidLocalField,
    IdMappingField,
    OwnerCentroidField,
    OwnerCentroidLocalField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class _GeneratedGeoConnector(DG):
    __slots__ = ()

    NODE_TYPE = "geoConnector"

    currentTime = TimeField(default_value=0.0)
    ct = currentTime

    prevTime = TimeField(default_value=0.0, writable=False)
    pt = prevTime

    deltaTime = TimeField(default_value=0.0, writable=False)
    dlt = deltaTime

    owner = MessageField()
    own = owner

    inputGeometryMsg = MessageField()
    igm = inputGeometryMsg

    localGeometry = GenericField()
    lge = localGeometry

    worldMatrix = DataMatrixField()
    wm = worldMatrix

    ownerPositions = DataVectorArrayField(writable=False)
    pos = ownerPositions

    preOwnerPositions = DataVectorArrayField(writable=False)
    pop = preOwnerPositions

    ownerVelocities = DataVectorArrayField(writable=False)
    vel = ownerVelocities

    ownerMasses = DataDoubleArrayField(writable=False)
    mas = ownerMasses

    idMapping = IdMappingField(writable=False)
    idm = idMapping
    sortedId = idMapping.sortedId
    sid = sortedId
    idIndex = idMapping.idIndex
    idix = idIndex

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    ownerCentroid = OwnerCentroidField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocd = ownerCentroid
    ownerCentroidX = ownerCentroid.ownerCentroidX
    ocx = ownerCentroidX
    ownerCentroidY = ownerCentroid.ownerCentroidY
    ocy = ownerCentroidY
    ownerCentroidZ = ownerCentroid.ownerCentroidZ
    ocz = ownerCentroidZ

    ownerCentroidLocal = OwnerCentroidLocalField(default_value=(0.0, 0.0, 0.0), writable=False)
    ocl = ownerCentroidLocal
    ownerCentroidLocalX = ownerCentroidLocal.ownerCentroidLocalX
    olcx = ownerCentroidLocalX
    ownerCentroidLocalY = ownerCentroidLocal.ownerCentroidLocalY
    ocly = ownerCentroidLocalY
    ownerCentroidLocalZ = ownerCentroidLocal.ownerCentroidLocalZ
    oclz = ownerCentroidLocalZ

    groupId = LongField(multi=True, default_value=-1)
    gri = groupId

    componentPositions = DataVectorArrayField(multi=True, writable=False)
    cpp = componentPositions

    preComponentPositions = DataVectorArrayField(multi=True, writable=False)
    pcp = preComponentPositions

    componentVelocities = DataVectorArrayField(multi=True, writable=False)
    cpv = componentVelocities

    componentCentroid = ComponentCentroidField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    cpc = componentCentroid

    componentCentroidLocal = ComponentCentroidLocalField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    ccl = componentCentroidLocal

    sweptGeometry = TypedField(writable=False)
    swg = sweptGeometry

    localSweptGeometry = TypedField(writable=False)
    lsg = localSweptGeometry

    ratePPIn = DoubleField(multi=True, default_value=0.0)
    rpi = ratePPIn

    ratePPOut = DataDoubleArrayField(writable=False)
    rpo = ratePPOut

    matrixModified = BoolField(default_value=False, writable=False)
    mtm = matrixModified

    geometryModified = LongField(default_value=0, writable=False)
    gmd = geometryModified

    tessellationFactor = LongField(default_value=200, min_value=1, soft_min_value=1, soft_max_value=1000)
    tf = tessellationFactor

    uvSetName = DataStringField()
    guv = uvSetName

    resilience = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    res = resilience

    friction = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fri = friction

    offset = DoubleField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    off = offset
