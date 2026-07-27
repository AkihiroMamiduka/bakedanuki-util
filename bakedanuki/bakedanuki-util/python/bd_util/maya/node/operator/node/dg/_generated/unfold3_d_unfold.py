# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class GeneratedUnfold3DUnfold(DG):
    __slots__ = ()

    NODE_TYPE = "Unfold3DUnfold"

    inMesh = DataMeshField()
    im = inMesh

    outMesh = DataMeshField(writable=False)
    om = outMesh

    iterations = LongField(default_value=1)
    ite = iterations

    borderIntersection = BoolField(default_value=True)
    bi = borderIntersection

    triangleFlip = BoolField(default_value=True)
    trif = triangleFlip

    mapSize = LongField(default_value=1024)
    msiz = mapSize

    packing = BoolField(default_value=True)
    pack = packing

    roomSpace = LongField(default_value=2)
    rspac = roomSpace

    meshDagPath = DataStringField()
    mdp = meshDagPath

    uvListSelected = TypedField()
    uvl = uvListSelected

    uvSetName = DataStringField()
    usn = uvSetName

    memusexported = TypedField()
    mue = memusexported

    memvsexported = TypedField()
    mve = memvsexported

    memisevereval = BoolField(default_value=False)
    miee = memisevereval
