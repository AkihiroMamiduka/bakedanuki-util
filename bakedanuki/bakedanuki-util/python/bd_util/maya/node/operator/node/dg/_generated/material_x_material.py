# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.material_x_material import (
    OutSurfaceField,
    OutVolumeField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedMaterialXMaterial(DG):
    __slots__ = ()

    NODE_TYPE = "materialXMaterial"

    manager = MessageField()
    mgr = manager

    document = DataStringField()
    doc = document

    element = DataStringField()
    el = element

    outSurface = OutSurfaceField(default_value=(0.0, 0.0, 0.0), writable=False)
    os = outSurface
    outSurfaceR = outSurface.outSurfaceR
    osr = outSurfaceR
    outSurfaceG = outSurface.outSurfaceG
    osg = outSurfaceG
    outSurfaceB = outSurface.outSurfaceB
    osb = outSurfaceB

    outVolume = OutVolumeField(default_value=(0.0, 0.0, 0.0), writable=False)
    ov = outVolume
    outVolumeR = outVolume.outVolumeR
    ovr = outVolumeR
    outVolumeG = outVolume.outVolumeG
    ovg = outVolumeG
    outVolumeB = outVolume.outVolumeB
    ovb = outVolumeB

    outDisplacement = FloatField(default_value=0.0, writable=False)
    od = outDisplacement
