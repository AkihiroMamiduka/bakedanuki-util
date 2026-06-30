# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.material_x_material import (
    OutSurfaceField,
    OutVolumeField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class MaterialXMaterial(DG):
    __slots__ = ()

    NODE_TYPE = "materialXMaterial"

    manager = MessageField()
    mgr = manager

    document = DataStringField()
    doc = document

    element = DataStringField()
    el = element

    outSurface = OutSurfaceField()
    os = outSurface
    outSurfaceR = outSurface.outSurfaceR
    osr = outSurfaceR
    outSurfaceG = outSurface.outSurfaceG
    osg = outSurfaceG
    outSurfaceB = outSurface.outSurfaceB
    osb = outSurfaceB

    outVolume = OutVolumeField()
    ov = outVolume
    outVolumeR = outVolume.outVolumeR
    ovr = outVolumeR
    outVolumeG = outVolume.outVolumeG
    ovg = outVolumeG
    outVolumeB = outVolume.outVolumeB
    ovb = outVolumeB

    outDisplacement = FloatField()
    od = outDisplacement
