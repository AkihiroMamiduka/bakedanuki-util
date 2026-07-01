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

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    mask = FloatField()
    mk = mask

    clump = FloatField()
    cp = clump

    clumpScale = ClumpScaleField(multi=True)
    cs = clumpScale

    clumpVolumize = BoolField()
    cvl = clumpVolumize

    clumpVariance = FloatField()
    cvr = clumpVariance

    preserveLength = FloatField()
    pl = preserveLength

    pointDensity = FloatField()
    pd = pointDensity

    pointDensityMask = FloatField()
    pdm = pointDensityMask

    pointRandomness = FloatField()
    pr = pointRandomness

    pointSeed = LongField()
    ps = pointSeed

    useInputPoints = BoolField()
    uip = useInputPoints

    inputPoints = TypedField()
    ips = inputPoints

    autoUpdate = BoolField()
    au = autoUpdate

    radiusVariance = FloatField()
    rv = radiusVariance

    updateClumpMap = BoolField()
    ucm = updateClumpMap

    mapSubdLevel = LongField()
    msl = mapSubdLevel

    useControlMap = BoolField()
    utm = useControlMap

    controlMaps = DataStringArrayField()
    cmp = controlMaps

    activeControlMap = MessageField()
    acm = activeControlMap

    customControlMap = CustomControlMapField()
    ccm = customControlMap
    customControlMapR = customControlMap.customControlMapR
    ccmr = customControlMapR
    customControlMapG = customControlMap.customControlMapG
    ccmg = customControlMapG
    customControlMapB = customControlMap.customControlMapB
    ccmb = customControlMapB

    controlMask = ControlMaskField()
    cms = controlMask
    controlMaskR = controlMask.controlMaskR
    cmsr = controlMaskR
    controlMaskG = controlMask.controlMaskG
    cmsg = controlMaskG
    controlMaskB = controlMask.controlMaskB
    cmsb = controlMaskB

    previewColor = BoolField()
    pc = previewColor

    flatness = FloatField()
    fl = flatness

    flatnessScale = FlatnessScaleField(multi=True)
    fls = flatnessScale

    offset = FloatField()
    of = offset

    offsetScale = OffsetScaleField(multi=True)
    ofs = offsetScale

    curl = FloatField()
    cu = curl

    curlScale = CurlScaleField(multi=True)
    cus = curlScale

    orient = DoubleAngleField()
    or_ = orient

    copy = FloatField()
    co = copy

    copyScale = CopyScaleField(multi=True)
    cos = copyScale

    copyVariance = FloatField()
    cov = copyVariance

    cut = FloatField()
    ct = cut

    noise = FloatField()
    no = noise

    noiseScale = NoiseScaleField(multi=True)
    nos = noiseScale

    noiseFrequency = FloatField()
    nof = noiseFrequency

    noiseCorrelation = FloatField()
    noc = noiseCorrelation

    inMeshData = TypedField()
    imd = inMeshData
