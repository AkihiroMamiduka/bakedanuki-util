# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField


class CycleTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HOLD = 0
    LOOP = 1
    REVERSE = 2
    BOUNCE = 3


class CycleTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HOLD = 0
    LOOP = 1
    REVERSE = 2
    BOUNCE = 3

    NAME_MAP = {
        HOLD: "Hold",
        LOOP: "Loop",
        REVERSE: "Reverse",
        BOUNCE: "Bounce",
    }


class CycleTypeEnumField(
    EnumField[CycleTypeEnumAttrOperator, CycleTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CycleTypeEnumAttrOperator
    PLUG_CLS = CycleTypeEnumPlugOperator


class AlembicNode(DG):
    __slots__ = ()

    NODE_TYPE = "AlembicNode"

    time = TimeField(default_value=0.0)
    tm = time

    abc_File = DataStringField()
    fn = abc_File

    abc_layerFiles = DataStringArrayField()
    fns = abc_layerFiles

    speed = DoubleField(default_value=1.0)
    sp = speed

    offset = DoubleField(default_value=0.0)
    of = offset

    cycleType = CycleTypeEnumField(default_value=0)
    ct = cycleType

    regexIncludeFilter = DataStringField()
    ift = regexIncludeFilter

    regexExcludeFilter = DataStringField()
    eft = regexExcludeFilter

    startFrame = DoubleField(default_value=0.0, writable=False)
    sf = startFrame

    endFrame = DoubleField(default_value=0.0, writable=False)
    ef = endFrame

    outSubDMesh = DataMeshField(multi=True, writable=False)
    osubd = outSubDMesh

    outPolyMesh = DataMeshField(multi=True, writable=False)
    opoly = outPolyMesh

    outNSurface = DataNurbsSurfaceField(multi=True, writable=False)
    ons = outNSurface

    outNCurveGrp = DataNurbsCurveField(multi=True, writable=False)
    onc = outNCurveGrp

    outLoc = DoubleField(multi=True, default_value=0.0, writable=False)
    olo = outLoc

    transOp = DoubleField(multi=True, default_value=0.0, writable=False)
    to = transOp

    outCamera = DoubleField(multi=True, default_value=0.0, writable=False)
    ocam = outCamera

    prop = GenericField(multi=True, writable=False)
    pr = prop
