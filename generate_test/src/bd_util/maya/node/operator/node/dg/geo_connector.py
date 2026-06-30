# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.geo_connector import (
    ComponentCentroidField,
    ComponentCentroidLocalField,
    IdMappingField,
    OwnerCentroidField,
    OwnerCentroidLocalField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class GeoConnector(DG):
    __slots__ = ()

    NODE_TYPE = "geoConnector"

    currentTime = TimeField()
    ct = currentTime

    prevTime = TimeField()
    pt = prevTime

    deltaTime = TimeField()
    dlt = deltaTime

    owner = MessageField()
    own = owner

    inputGeometryMsg = MessageField()
    igm = inputGeometryMsg

    localGeometry = GenericField()
    lge = localGeometry

    worldMatrix = DataMatrixField()
    wm = worldMatrix

    ownerPositions = DataVectorArrayField()
    pos = ownerPositions

    preOwnerPositions = DataVectorArrayField()
    pop = preOwnerPositions

    ownerVelocities = DataVectorArrayField()
    vel = ownerVelocities

    ownerMasses = DataDoubleArrayField()
    mas = ownerMasses

    idMapping = IdMappingField()
    idm = idMapping
    sortedId = idMapping.sortedId
    sid = sortedId
    idIndex = idMapping.idIndex
    idix = idIndex

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    ownerCentroid = OwnerCentroidField()
    ocd = ownerCentroid
    ownerCentroidX = ownerCentroid.ownerCentroidX
    ocx = ownerCentroidX
    ownerCentroidY = ownerCentroid.ownerCentroidY
    ocy = ownerCentroidY
    ownerCentroidZ = ownerCentroid.ownerCentroidZ
    ocz = ownerCentroidZ

    ownerCentroidLocal = OwnerCentroidLocalField()
    ocl = ownerCentroidLocal
    ownerCentroidLocalX = ownerCentroidLocal.ownerCentroidLocalX
    olcx = ownerCentroidLocalX
    ownerCentroidLocalY = ownerCentroidLocal.ownerCentroidLocalY
    ocly = ownerCentroidLocalY
    ownerCentroidLocalZ = ownerCentroidLocal.ownerCentroidLocalZ
    oclz = ownerCentroidLocalZ

    groupId = LongField(multi=True)
    gri = groupId

    componentPositions = DataVectorArrayField(multi=True)
    cpp = componentPositions

    preComponentPositions = DataVectorArrayField(multi=True)
    pcp = preComponentPositions

    componentVelocities = DataVectorArrayField(multi=True)
    cpv = componentVelocities

    componentCentroid = ComponentCentroidField(multi=True)
    cpc = componentCentroid

    componentCentroidLocal = ComponentCentroidLocalField(multi=True)
    ccl = componentCentroidLocal

    sweptGeometry = TypedField()
    swg = sweptGeometry

    localSweptGeometry = TypedField()
    lsg = localSweptGeometry

    ratePPIn = DoubleField(multi=True)
    rpi = ratePPIn

    ratePPOut = DataDoubleArrayField()
    rpo = ratePPOut

    matrixModified = BoolField()
    mtm = matrixModified

    geometryModified = LongField()
    gmd = geometryModified

    tessellationFactor = LongField()
    tf = tessellationFactor

    uvSetName = DataStringField()
    guv = uvSetName

    resilience = DoubleField()
    res = resilience

    friction = DoubleField()
    fri = friction

    offset = DoubleField()
    off = offset
