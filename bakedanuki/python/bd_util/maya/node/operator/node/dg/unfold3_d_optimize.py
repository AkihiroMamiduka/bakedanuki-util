# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class Unfold3DOptimize(DG):
    __slots__ = ()

    NODE_TYPE = "Unfold3DOptimize"

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

    roomSpace = LongField(default_value=2)
    rspac = roomSpace

    surfangle = FloatField(default_value=1.0)
    sa = surfangle

    power = FloatField(default_value=1.0)
    pow = power

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
