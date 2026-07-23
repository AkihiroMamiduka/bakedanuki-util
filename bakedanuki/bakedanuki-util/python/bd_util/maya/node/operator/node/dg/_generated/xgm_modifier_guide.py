# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_modifier_guide import (
    MagnitudeScaleField,
    RegionMapField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.typed import TypedField


class _GeneratedXgmModifierGuide(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierGuide"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    inGuideData = TypedField()
    igd = inGuideData

    mask = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    magnitude = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    ms = magnitudeScale

    blend = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    bl = blend

    useRegionMap = BoolField(default_value=False)
    urm = useRegionMap

    regionMask = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    rm = regionMask

    regionMap = RegionMapField(default_value=(1.0, 1.0, 1.0))
    rmp = regionMap
    regionMapR = regionMap.regionMapR
    rmpr = regionMapR
    regionMapG = regionMap.regionMapG
    rmpg = regionMapG
    regionMapB = regionMap.regionMapB
    rmpb = regionMapB

    previewColor = BoolField(default_value=False)
    pc = previewColor
