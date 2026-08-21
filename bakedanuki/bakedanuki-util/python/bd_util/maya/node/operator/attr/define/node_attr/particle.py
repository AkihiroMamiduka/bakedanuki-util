# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.time import TimeField
from ..std.at.typed import TypedField
from ..std.dt.double_array import DataDoubleArrayField
from ..std.dt.string import DataStringField
from ..std.dt.string_array import DataStringArrayField
from ..std.dt.vector_array import DataVectorArrayField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class CompInstObjGroups_compObjectGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroups_compObjectGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compObjectGrpCompList", "cgcl"),
        ("compObjectGroupId", "cgid"),
    )

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroups_compObjectGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGrpCompList = TypedField()
    cgcl = compObjectGrpCompList

    compObjectGroupId = LongField(default_value=0)
    cgid = compObjectGroupId


class CompInstObjGroups_compObjectGroupsField(
    CompoundField[
        CompInstObjGroups_compObjectGroupsAttrOperator,
        CompInstObjGroups_compObjectGroupsPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroups_compObjectGroupsAttrOperator
    PLUG_CLS = CompInstObjGroups_compObjectGroupsPlugOperator


class CompInstObjGroupsPlugOperator(
    CompoundPlugOperator["CompInstObjGroupsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("compObjectGroups", "cog"),)

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsAttrOperator(
    CompoundAttrOperator[CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    compObjectGroups = CompInstObjGroups_compObjectGroupsField(multi=True)
    cog = compObjectGroups


class CompInstObjGroupsField(
    CompoundField[CompInstObjGroupsAttrOperator, CompInstObjGroupsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompInstObjGroupsAttrOperator
    PLUG_CLS = CompInstObjGroupsPlugOperator


class ComponentTagsPlugOperator(
    CompoundPlugOperator["ComponentTagsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("componentTagName", "gtagnm"),
        ("componentTagContents", "gtagcmp"),
    )

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsAttrOperator(
    CompoundAttrOperator[ComponentTagsPlugOperator]
):
    __slots__ = ()

    componentTagName = DataStringField()
    gtagnm = componentTagName

    componentTagContents = TypedField()
    gtagcmp = componentTagContents


class ComponentTagsField(
    CompoundField[ComponentTagsAttrOperator, ComponentTagsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTagsAttrOperator
    PLUG_CLS = ComponentTagsPlugOperator


class CentroidPlugOperator(
    Double3CompoundBasePlugOperator["CentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centroidX", "ctdx"),
        ("centroidY", "ctdy"),
        ("centroidZ", "ctdz"),
    )

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CentroidPlugOperator]
):
    __slots__ = ()

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class CentroidField(
    Double3CompoundBaseField[CentroidAttrOperator, CentroidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CentroidAttrOperator
    PLUG_CLS = CentroidPlugOperator

    centroidX = DoubleField(default_value=0.0, writable=False)
    ctdx = centroidX

    centroidY = DoubleField(default_value=0.0, writable=False)
    ctdy = centroidY

    centroidZ = DoubleField(default_value=0.0, writable=False)
    ctdz = centroidZ


class WorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["WorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldCentroidX", "wctx"),
        ("worldCentroidY", "wcty"),
        ("worldCentroidZ", "wctz"),
    )

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[WorldCentroidPlugOperator]
):
    __slots__ = ()

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class WorldCentroidField(
    Double3CompoundBaseField[
        WorldCentroidAttrOperator, WorldCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WorldCentroidAttrOperator
    PLUG_CLS = WorldCentroidPlugOperator

    worldCentroidX = DoubleField(default_value=0.0, writable=False)
    wctx = worldCentroidX

    worldCentroidY = DoubleField(default_value=0.0, writable=False)
    wcty = worldCentroidY

    worldCentroidZ = DoubleField(default_value=0.0, writable=False)
    wctz = worldCentroidZ


class CachedWorldCentroidPlugOperator(
    Double3CompoundBasePlugOperator["CachedWorldCentroidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cachedWorldCentroidX", "cwcx"),
        ("cachedWorldCentroidY", "cwcy"),
        ("cachedWorldCentroidZ", "cwcz"),
    )

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidAttrOperator(
    Double3CompoundBaseAttrOperator[CachedWorldCentroidPlugOperator]
):
    __slots__ = ()

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class CachedWorldCentroidField(
    Double3CompoundBaseField[
        CachedWorldCentroidAttrOperator, CachedWorldCentroidPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CachedWorldCentroidAttrOperator
    PLUG_CLS = CachedWorldCentroidPlugOperator

    cachedWorldCentroidX = DoubleField(default_value=0.0, writable=False)
    cwcx = cachedWorldCentroidX

    cachedWorldCentroidY = DoubleField(default_value=0.0, writable=False)
    cwcy = cachedWorldCentroidY

    cachedWorldCentroidZ = DoubleField(default_value=0.0, writable=False)
    cwcz = cachedWorldCentroidZ


class IdMappingPlugOperator(CompoundPlugOperator["IdMappingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingAttrOperator(CompoundAttrOperator[IdMappingPlugOperator]):
    __slots__ = ()

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator

    sortedId = TypedField(writable=False)
    sid = sortedId

    idIndex = TypedField(writable=False)
    idix = idIndex


class RandStatePlugOperator(
    Long3CompoundBasePlugOperator["RandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("randStateX", "rstx"),
        ("randStateY", "rsty"),
        ("randStateZ", "rstz"),
    )

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateAttrOperator(
    Long3CompoundBaseAttrOperator[RandStatePlugOperator]
):
    __slots__ = ()

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class RandStateField(
    Long3CompoundBaseField[RandStateAttrOperator, RandStatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandStateAttrOperator
    PLUG_CLS = RandStatePlugOperator

    randStateX = LongField(default_value=0)
    rstx = randStateX

    randStateY = LongField(default_value=0)
    rsty = randStateY

    randStateZ = LongField(default_value=0)
    rstz = randStateZ


class FieldDataPlugOperator(CompoundPlugOperator["FieldDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fieldDataPosition", "fdp"),
        ("fieldDataVelocity", "fdv"),
        ("fieldDataMass", "fdm"),
        ("fieldDataDeltaTime", "fdt"),
    )

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataAttrOperator(CompoundAttrOperator[FieldDataPlugOperator]):
    __slots__ = ()

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class FieldDataField(
    CompoundField[FieldDataAttrOperator, FieldDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldDataAttrOperator
    PLUG_CLS = FieldDataPlugOperator

    fieldDataPosition = DataVectorArrayField(writable=False)
    fdp = fieldDataPosition

    fieldDataVelocity = DataVectorArrayField(writable=False)
    fdv = fieldDataVelocity

    fieldDataMass = DataDoubleArrayField(writable=False)
    fdm = fieldDataMass

    fieldDataDeltaTime = TimeField(default_value=0.0, writable=False)
    fdt = fieldDataDeltaTime


class EmitterDataPlugOperator(CompoundPlugOperator["EmitterDataAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("emitterDataPosition", "edp"),
        ("emitterDataVelocity", "edv"),
        ("emitterDataDeltaTime", "edt"),
    )

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataAttrOperator(CompoundAttrOperator[EmitterDataPlugOperator]):
    __slots__ = ()

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class EmitterDataField(
    CompoundField[EmitterDataAttrOperator, EmitterDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EmitterDataAttrOperator
    PLUG_CLS = EmitterDataPlugOperator

    emitterDataPosition = DataVectorArrayField(writable=False)
    edp = emitterDataPosition

    emitterDataVelocity = DataVectorArrayField(writable=False)
    edv = emitterDataVelocity

    emitterDataDeltaTime = TimeField(default_value=0.0, writable=False)
    edt = emitterDataDeltaTime


class CollisionDataPlugOperator(
    CompoundPlugOperator["CollisionDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("collisionGeometry", "cge"),
        ("collisionResilience", "crs"),
        ("collisionFriction", "cfr"),
        ("collisionOffset", "cof"),
    )

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataAttrOperator(
    CompoundAttrOperator[CollisionDataPlugOperator]
):
    __slots__ = ()

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class CollisionDataField(
    CompoundField[CollisionDataAttrOperator, CollisionDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionDataAttrOperator
    PLUG_CLS = CollisionDataPlugOperator

    collisionGeometry = TypedField(multi=True)
    cge = collisionGeometry

    collisionResilience = DoubleField(multi=True, default_value=0.0)
    crs = collisionResilience

    collisionFriction = DoubleField(multi=True, default_value=0.0)
    cfr = collisionFriction

    collisionOffset = DoubleField(multi=True, default_value=0.01)
    cof = collisionOffset


class EventRandStatePlugOperator(
    Long3CompoundBasePlugOperator["EventRandStateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("eventRandStateX", "ersx"),
        ("eventRandStateY", "ersy"),
        ("eventRandStateZ", "ersz"),
    )

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateAttrOperator(
    Long3CompoundBaseAttrOperator[EventRandStatePlugOperator]
):
    __slots__ = ()

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class EventRandStateField(
    Long3CompoundBaseField[
        EventRandStateAttrOperator, EventRandStatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EventRandStateAttrOperator
    PLUG_CLS = EventRandStatePlugOperator

    eventRandStateX = LongField(default_value=0)
    ersx = eventRandStateX

    eventRandStateY = LongField(default_value=0)
    ersy = eventRandStateY

    eventRandStateZ = LongField(default_value=0)
    ersz = eventRandStateZ


class InstanceDataPlugOperator(
    CompoundPlugOperator["InstanceDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("instanceAttributeMapping", "iam"),
        ("instancePointData", "ipd"),
    )

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataAttrOperator(CompoundAttrOperator[InstanceDataPlugOperator]):
    __slots__ = ()

    instanceAttributeMapping = DataStringArrayField()
    iam = instanceAttributeMapping

    instancePointData = TypedField()
    ipd = instancePointData


class InstanceDataField(
    CompoundField[InstanceDataAttrOperator, InstanceDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InstanceDataAttrOperator
    PLUG_CLS = InstanceDataPlugOperator
