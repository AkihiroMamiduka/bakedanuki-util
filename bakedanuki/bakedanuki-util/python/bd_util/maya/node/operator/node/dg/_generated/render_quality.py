# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class EdgeAntiAliasingEnumPlugOperator(
    EnumPlugOperator["EdgeAntiAliasingEnumAttrOperator"]
):
    __slots__ = ()

    HIGHEST_QUALITY = 0
    HIGH_QUALITY = 1
    MEDIUM_QUALITY = 2
    LOW_QUALITY = 3


class EdgeAntiAliasingEnumAttrOperator(
    EnumAttrOperator[EdgeAntiAliasingEnumPlugOperator]
):
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
    EnumField[
        EdgeAntiAliasingEnumAttrOperator, EdgeAntiAliasingEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = EdgeAntiAliasingEnumAttrOperator
    PLUG_CLS = EdgeAntiAliasingEnumPlugOperator


class PixelFilterTypeEnumPlugOperator(
    EnumPlugOperator["PixelFilterTypeEnumAttrOperator"]
):
    __slots__ = ()

    BOX_FILTER = 0
    TRIANGLE_FILTER = 2
    GAUSSIAN_FILTER = 4
    QUADRATIC_B_MINUS_SPLINE_FILTER = 5
    PLUG_IN_FILTER = 1000


class PixelFilterTypeEnumAttrOperator(
    EnumAttrOperator[PixelFilterTypeEnumPlugOperator]
):
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


class GeneratedRenderQuality(DG):
    __slots__ = ()

    NODE_TYPE = "renderQuality"

    reflections = LongField(default_value=1, min_value=0, soft_max_value=10)
    rfl = reflections

    refractions = LongField(default_value=6, min_value=0, soft_max_value=10)
    rfr = refractions

    shadows = LongField(default_value=2, min_value=0, soft_max_value=10)
    sl = shadows

    rayTraceBias = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    rtb = rayTraceBias

    edgeAntiAliasing = EdgeAntiAliasingEnumField(default_value=3)
    eaa = edgeAntiAliasing

    renderSample = BoolField(default_value=False)
    rsdn = renderSample

    useMultiPixelFilter = BoolField(default_value=False)
    ufil = useMultiPixelFilter

    pixelFilterType = PixelFilterTypeEnumField(default_value=2)
    pft = pixelFilterType

    pixelFilterWidthX = FloatField(
        default_value=2.200000047683716,
        min_value=1.0,
        max_value=3.0,
        soft_max_value=3.0,
    )
    pfwx = pixelFilterWidthX

    pixelFilterWidthY = FloatField(
        default_value=2.200000047683716,
        min_value=1.0,
        max_value=3.0,
        soft_max_value=3.0,
    )
    pfwy = pixelFilterWidthY

    plugInFilterWeight = FloatField(default_value=1.0)
    pifw = plugInFilterWeight

    shadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    ss = shadingSamples

    maxShadingSamples = LongField(
        default_value=8, min_value=1, max_value=32, soft_max_value=20
    )
    mss = maxShadingSamples

    visibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = visibilitySamples

    maxVisibilitySamples = LongField(
        default_value=4, min_value=2, max_value=32, soft_max_value=20
    )
    mvm = maxVisibilitySamples

    volumeSamples = LongField(default_value=1, min_value=1, soft_max_value=20)
    vs = volumeSamples

    particleSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    pss = particleSamples

    enableRaytracing = BoolField(default_value=False)
    ert = enableRaytracing

    redThreshold = FloatField(
        default_value=0.4000000059604645, min_value=0.0, max_value=1.0
    )
    rct = redThreshold

    greenThreshold = FloatField(
        default_value=0.30000001192092896, min_value=0.0, max_value=1.0
    )
    gct = greenThreshold

    blueThreshold = FloatField(
        default_value=0.6000000238418579, min_value=0.0, max_value=1.0
    )
    bct = blueThreshold

    coverageThreshold = FloatField(
        default_value=0.125, min_value=0.0, max_value=1.0
    )
    cct = coverageThreshold
