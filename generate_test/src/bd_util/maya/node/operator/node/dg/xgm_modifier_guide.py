# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_guide import (
    MagnitudeScaleField,
    RegionMapField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


class XgmModifierGuide(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierGuide"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    inGuideData = TypedField()
    igd = inGuideData

    mask = DoubleField()
    mk = mask

    magnitude = DoubleField()
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True)
    ms = magnitudeScale

    blend = DoubleField()
    bl = blend

    useRegionMap = BoolField()
    urm = useRegionMap

    regionMask = DoubleField()
    rm = regionMask

    regionMap = RegionMapField()
    rmp = regionMap
    regionMapR = regionMap.regionMapR
    rmpr = regionMapR
    regionMapG = regionMap.regionMapG
    rmpg = regionMapG
    regionMapB = regionMap.regionMapB
    rmpb = regionMapB

    previewColor = BoolField()
    pc = previewColor
