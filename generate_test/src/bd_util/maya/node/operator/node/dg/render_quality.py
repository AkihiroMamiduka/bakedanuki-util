# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class EdgeAntiAliasingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3


class EdgeAntiAliasingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3

    NAME_MAP = {
        HIGHEST_QUALITY: "Highest Quality",
        HIGH_QUALITY: "High Quality",
        MEDIUM_QUALITY: "Medium Quality",
        LOW_QUALITY: "Low Quality",
    }


class EdgeAntiAliasingEnumField(
    EnumField[EdgeAntiAliasingEnumAttrOperator, EdgeAntiAliasingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeAntiAliasingEnumAttrOperator
    PLUG_CLS = EdgeAntiAliasingEnumPlugOperator


class PixelFilterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BOX_FILTER = 0
    TRIANGLE_FILTER = 2
    GAUSSIAN_FILTER = 4
    QUADRATIC_B_MINUS_SPLINE_FILTER = 5
    PLUG_IN_FILTER = 1000


class PixelFilterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BOX_FILTER = 0
    TRIANGLE_FILTER = 2
    GAUSSIAN_FILTER = 4
    QUADRATIC_B_MINUS_SPLINE_FILTER = 5
    PLUG_IN_FILTER = 1000

    NAME_MAP = {
        BOX_FILTER: "Box Filter",
        TRIANGLE_FILTER: "Triangle Filter",
        GAUSSIAN_FILTER: "Gaussian Filter",
        QUADRATIC_B_MINUS_SPLINE_FILTER: "Quadratic B-Spline Filter",
        PLUG_IN_FILTER: "Plug in Filter",
    }


class PixelFilterTypeEnumField(
    EnumField[PixelFilterTypeEnumAttrOperator, PixelFilterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PixelFilterTypeEnumAttrOperator
    PLUG_CLS = PixelFilterTypeEnumPlugOperator


class RenderQuality(DG):
    __slots__ = ()

    NODE_TYPE = "renderQuality"

    reflections = LongField()
    rfl = reflections

    refractions = LongField()
    rfr = refractions

    shadows = LongField()
    sl = shadows

    rayTraceBias = FloatField()
    rtb = rayTraceBias

    edgeAntiAliasing = EdgeAntiAliasingEnumField()
    eaa = edgeAntiAliasing

    renderSample = BoolField()
    rsdn = renderSample

    useMultiPixelFilter = BoolField()
    ufil = useMultiPixelFilter

    pixelFilterType = PixelFilterTypeEnumField()
    pft = pixelFilterType

    pixelFilterWidthX = FloatField()
    pfwx = pixelFilterWidthX

    pixelFilterWidthY = FloatField()
    pfwy = pixelFilterWidthY

    plugInFilterWeight = FloatField()
    pifw = plugInFilterWeight

    shadingSamples = LongField()
    ss = shadingSamples

    maxShadingSamples = LongField()
    mss = maxShadingSamples

    visibilitySamples = LongField()
    mvs = visibilitySamples

    maxVisibilitySamples = LongField()
    mvm = maxVisibilitySamples

    volumeSamples = LongField()
    vs = volumeSamples

    particleSamples = LongField()
    pss = particleSamples

    enableRaytracing = BoolField()
    ert = enableRaytracing

    redThreshold = FloatField()
    rct = redThreshold

    greenThreshold = FloatField()
    gct = greenThreshold

    blueThreshold = FloatField()
    bct = blueThreshold

    coverageThreshold = FloatField()
    cct = coverageThreshold
