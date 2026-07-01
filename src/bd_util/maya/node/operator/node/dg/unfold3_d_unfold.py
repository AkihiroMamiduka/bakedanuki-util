# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class Unfold3DUnfold(DG):
    __slots__ = ()

    NODE_TYPE = "Unfold3DUnfold"

    inMesh = DataMeshField()
    im = inMesh

    outMesh = DataMeshField()
    om = outMesh

    iterations = LongField()
    ite = iterations

    borderIntersection = BoolField()
    bi = borderIntersection

    triangleFlip = BoolField()
    trif = triangleFlip

    mapSize = LongField()
    msiz = mapSize

    packing = BoolField()
    pack = packing

    roomSpace = LongField()
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

    memisevereval = BoolField()
    miee = memisevereval
