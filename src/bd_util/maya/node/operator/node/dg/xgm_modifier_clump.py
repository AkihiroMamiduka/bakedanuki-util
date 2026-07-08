# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_clump import (
    ClumpScaleField,
    ControlMaskField,
    CopyScaleField,
    CurlScaleField,
    CustomControlMapField,
    FlatnessScaleField,
    NoiseScaleField,
    OffsetScaleField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.string_array import DataStringArrayField


class XgmModifierClump(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierClump"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    clump = FloatField(default_value=1.0)
    cp = clump

    clumpScale = ClumpScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    cs = clumpScale

    clumpVolumize = BoolField(default_value=False)
    cvl = clumpVolumize

    clumpVariance = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    cvr = clumpVariance

    preserveLength = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    pl = preserveLength

    pointDensity = FloatField(default_value=1.0)
    pd = pointDensity

    pointDensityMask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    pdm = pointDensityMask

    pointRandomness = FloatField(default_value=1.0, min_value=0.0)
    pr = pointRandomness

    pointSeed = LongField(default_value=0, min_value=0)
    ps = pointSeed

    useInputPoints = BoolField(default_value=False)
    uip = useInputPoints

    inputPoints = TypedField(readable=False)
    ips = inputPoints

    autoUpdate = BoolField(default_value=True)
    au = autoUpdate

    radiusVariance = FloatField(default_value=0.5, min_value=0.0)
    rv = radiusVariance

    updateClumpMap = BoolField(default_value=True)
    ucm = updateClumpMap

    mapSubdLevel = LongField(default_value=3)
    msl = mapSubdLevel

    useControlMap = BoolField(default_value=False)
    utm = useControlMap

    controlMaps = DataStringArrayField()
    cmp = controlMaps

    activeControlMap = MessageField()
    acm = activeControlMap

    customControlMap = CustomControlMapField(default_value=(1.0, 1.0, 1.0))
    ccm = customControlMap
    customControlMapR = customControlMap.customControlMapR
    ccmr = customControlMapR
    customControlMapG = customControlMap.customControlMapG
    ccmg = customControlMapG
    customControlMapB = customControlMap.customControlMapB
    ccmb = customControlMapB

    controlMask = ControlMaskField(default_value=(1.0, 1.0, 1.0))
    cms = controlMask
    controlMaskR = controlMask.controlMaskR
    cmsr = controlMaskR
    controlMaskG = controlMask.controlMaskG
    cmsg = controlMaskG
    controlMaskB = controlMask.controlMaskB
    cmsb = controlMaskB

    previewColor = BoolField(default_value=False)
    pc = previewColor

    flatness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    fl = flatness

    flatnessScale = FlatnessScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    fls = flatnessScale

    offset = FloatField(default_value=0.0)
    of = offset

    offsetScale = OffsetScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    ofs = offsetScale

    curl = FloatField(default_value=0.0)
    cu = curl

    curlScale = CurlScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    cus = curlScale

    orient = DoubleAngleField(default_value=0.0, min_value=0.0, max_value=360.0)
    or_ = orient

    copy = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    co = copy

    copyScale = CopyScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    cos = copyScale

    copyVariance = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    cov = copyVariance

    cut = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    ct = cut

    noise = FloatField(default_value=0.0, min_value=0.0)
    no = noise

    noiseScale = NoiseScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    nos = noiseScale

    noiseFrequency = FloatField(default_value=0.0, min_value=0.0)
    nof = noiseFrequency

    noiseCorrelation = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    noc = noiseCorrelation

    inMeshData = TypedField(readable=False)
    imd = inMeshData
