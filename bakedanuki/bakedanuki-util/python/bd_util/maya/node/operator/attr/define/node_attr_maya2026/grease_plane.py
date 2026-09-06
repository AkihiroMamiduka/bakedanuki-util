# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
    Short2CompoundBaseAttrOperator,
    Short2CompoundBasePlugOperator,
    Short2CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class OutputImageDimensionsPlugOperator(
    Long3CompoundBasePlugOperator["OutputImageDimensionsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputImageWidth", "oiw"),
        ("outputImageHeight", "oih"),
        ("outputImageFrames", "oif"),
    )

    outputImageWidth = LongField(default_value=0, writable=False)
    oiw = outputImageWidth

    outputImageHeight = LongField(default_value=0, writable=False)
    oih = outputImageHeight

    outputImageFrames = LongField(default_value=0, writable=False)
    oif = outputImageFrames


class OutputImageDimensionsAttrOperator(
    Long3CompoundBaseAttrOperator[OutputImageDimensionsPlugOperator]
):
    __slots__ = ()

    outputImageWidth = LongField(default_value=0, writable=False)
    oiw = outputImageWidth

    outputImageHeight = LongField(default_value=0, writable=False)
    oih = outputImageHeight

    outputImageFrames = LongField(default_value=0, writable=False)
    oif = outputImageFrames


class OutputImageDimensionsField(
    Long3CompoundBaseField[
        OutputImageDimensionsAttrOperator, OutputImageDimensionsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputImageDimensionsAttrOperator
    PLUG_CLS = OutputImageDimensionsPlugOperator

    outputImageWidth = LongField(default_value=0, writable=False)
    oiw = outputImageWidth

    outputImageHeight = LongField(default_value=0, writable=False)
    oih = outputImageHeight

    outputImageFrames = LongField(default_value=0, writable=False)
    oif = outputImageFrames


class CoveragePlugOperator(
    Short2CompoundBasePlugOperator["CoverageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageX", "cvx"),
        ("coverageY", "cvy"),
    )

    coverageX = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvx = coverageX

    coverageY = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvy = coverageY


class CoverageAttrOperator(
    Short2CompoundBaseAttrOperator[CoveragePlugOperator]
):
    __slots__ = ()

    coverageX = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvx = coverageX

    coverageY = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvy = coverageY


class CoverageField(
    Short2CompoundBaseField[CoverageAttrOperator, CoveragePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoverageAttrOperator
    PLUG_CLS = CoveragePlugOperator

    coverageX = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvx = coverageX

    coverageY = ShortField(default_value=-1, min_value=1, max_value=32767)
    cvy = coverageY


class CoverageOriginPlugOperator(
    Short2CompoundBasePlugOperator["CoverageOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("coverageOriginX", "cox"),
        ("coverageOriginY", "coy"),
    )

    coverageOriginX = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    cox = coverageOriginX

    coverageOriginY = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    coy = coverageOriginY


class CoverageOriginAttrOperator(
    Short2CompoundBaseAttrOperator[CoverageOriginPlugOperator]
):
    __slots__ = ()

    coverageOriginX = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    cox = coverageOriginX

    coverageOriginY = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    coy = coverageOriginY


class CoverageOriginField(
    Short2CompoundBaseField[
        CoverageOriginAttrOperator, CoverageOriginPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CoverageOriginAttrOperator
    PLUG_CLS = CoverageOriginPlugOperator

    coverageOriginX = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    cox = coverageOriginX

    coverageOriginY = ShortField(
        default_value=0, min_value=-32767, max_value=32767
    )
    coy = coverageOriginY


class ColorGainPlugOperator(
    Float3CompoundBasePlugOperator["ColorGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGainR", "cgr"),
        ("colorGainG", "cgg"),
        ("colorGainB", "cgb"),
    )

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    cgb = colorGainB


class ColorOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ColorOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorOffsetR", "cor"),
        ("colorOffsetG", "cog"),
        ("colorOffsetB", "cob"),
    )

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cob = colorOffsetB


class SizePlugOperator(Double2CompoundBasePlugOperator["SizeAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sizeX", "sx"),
        ("sizeY", "sy"),
    )

    sizeX = DoubleField(default_value=1.4173200000000001, min_value=0.0)
    sx = sizeX

    sizeY = DoubleField(default_value=0.94488, min_value=0.0)
    sy = sizeY


class SizeAttrOperator(Double2CompoundBaseAttrOperator[SizePlugOperator]):
    __slots__ = ()

    sizeX = DoubleField(default_value=1.4173200000000001, min_value=0.0)
    sx = sizeX

    sizeY = DoubleField(default_value=0.94488, min_value=0.0)
    sy = sizeY


class SizeField(Double2CompoundBaseField[SizeAttrOperator, SizePlugOperator]):
    __slots__ = ()

    ATTR_CLS = SizeAttrOperator
    PLUG_CLS = SizePlugOperator

    sizeX = DoubleField(default_value=1.4173200000000001, min_value=0.0)
    sx = sizeX

    sizeY = DoubleField(default_value=0.94488, min_value=0.0)
    sy = sizeY


class OffsetPlugOperator(
    Double2CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
    )

    offsetX = DoubleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleField(default_value=0.0)
    oy = offsetY


class OffsetAttrOperator(Double2CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetX = DoubleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleField(default_value=0.0)
    oy = offsetY


class OffsetField(
    Double2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = DoubleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleField(default_value=0.0)
    oy = offsetY


class ImageCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ImageCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageCenterX", "icx"),
        ("imageCenterY", "icy"),
        ("imageCenterZ", "icz"),
    )

    imageCenterX = DoubleLinearField(default_value=0.0)
    icx = imageCenterX

    imageCenterY = DoubleLinearField(default_value=0.0)
    icy = imageCenterY

    imageCenterZ = DoubleLinearField(default_value=0.0)
    icz = imageCenterZ


class ImageCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ImageCenterPlugOperator]
):
    __slots__ = ()

    imageCenterX = DoubleLinearField(default_value=0.0)
    icx = imageCenterX

    imageCenterY = DoubleLinearField(default_value=0.0)
    icy = imageCenterY

    imageCenterZ = DoubleLinearField(default_value=0.0)
    icz = imageCenterZ


class ImageCenterField(
    DoubleLinear3CompoundBaseField[
        ImageCenterAttrOperator, ImageCenterPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ImageCenterAttrOperator
    PLUG_CLS = ImageCenterPlugOperator

    imageCenterX = DoubleLinearField(default_value=0.0)
    icx = imageCenterX

    imageCenterY = DoubleLinearField(default_value=0.0)
    icy = imageCenterY

    imageCenterZ = DoubleLinearField(default_value=0.0)
    icz = imageCenterZ


class RenderPlaneTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RenderPlaneTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("renderPlaneTranslateX", "rptx"),
        ("renderPlaneTranslateY", "rpty"),
        ("renderPlaneTranslateZ", "rptz"),
    )

    renderPlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptx = renderPlaneTranslateX

    renderPlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rpty = renderPlaneTranslateY

    renderPlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptz = renderPlaneTranslateZ


class RenderPlaneTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RenderPlaneTranslatePlugOperator]
):
    __slots__ = ()

    renderPlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptx = renderPlaneTranslateX

    renderPlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rpty = renderPlaneTranslateY

    renderPlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptz = renderPlaneTranslateZ


class RenderPlaneTranslateField(
    DoubleLinear3CompoundBaseField[
        RenderPlaneTranslateAttrOperator, RenderPlaneTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RenderPlaneTranslateAttrOperator
    PLUG_CLS = RenderPlaneTranslatePlugOperator

    renderPlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptx = renderPlaneTranslateX

    renderPlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rpty = renderPlaneTranslateY

    renderPlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    rptz = renderPlaneTranslateZ


class SourcePlaneTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["SourcePlaneTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourcePlaneTranslateX", "sptx"),
        ("sourcePlaneTranslateY", "spty"),
        ("sourcePlaneTranslateZ", "sptz"),
    )

    sourcePlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptx = sourcePlaneTranslateX

    sourcePlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    spty = sourcePlaneTranslateY

    sourcePlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptz = sourcePlaneTranslateZ


class SourcePlaneTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[SourcePlaneTranslatePlugOperator]
):
    __slots__ = ()

    sourcePlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptx = sourcePlaneTranslateX

    sourcePlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    spty = sourcePlaneTranslateY

    sourcePlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptz = sourcePlaneTranslateZ


class SourcePlaneTranslateField(
    DoubleLinear3CompoundBaseField[
        SourcePlaneTranslateAttrOperator, SourcePlaneTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SourcePlaneTranslateAttrOperator
    PLUG_CLS = SourcePlaneTranslatePlugOperator

    sourcePlaneTranslateX = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptx = sourcePlaneTranslateX

    sourcePlaneTranslateY = DoubleLinearField(
        default_value=0.0, writable=False
    )
    spty = sourcePlaneTranslateY

    sourcePlaneTranslateZ = DoubleLinearField(
        default_value=0.0, writable=False
    )
    sptz = sourcePlaneTranslateZ


class RenderPlaneRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RenderPlaneRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("renderPlaneRotateX", "rprx"),
        ("renderPlaneRotateY", "rpry"),
        ("renderPlaneRotateZ", "rprz"),
    )

    renderPlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rprx = renderPlaneRotateX

    renderPlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rpry = renderPlaneRotateY

    renderPlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rprz = renderPlaneRotateZ


class RenderPlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RenderPlaneRotatePlugOperator]
):
    __slots__ = ()

    renderPlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rprx = renderPlaneRotateX

    renderPlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rpry = renderPlaneRotateY

    renderPlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rprz = renderPlaneRotateZ


class RenderPlaneRotateField(
    DoubleAngle3CompoundBaseField[
        RenderPlaneRotateAttrOperator, RenderPlaneRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RenderPlaneRotateAttrOperator
    PLUG_CLS = RenderPlaneRotatePlugOperator

    renderPlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    rprx = renderPlaneRotateX

    renderPlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    rpry = renderPlaneRotateY

    renderPlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rprz = renderPlaneRotateZ


class SourcePlaneRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["SourcePlaneRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourcePlaneRotateX", "sprx"),
        ("sourcePlaneRotateY", "spry"),
        ("sourcePlaneRotateZ", "sprz"),
    )

    sourcePlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    sprx = sourcePlaneRotateX

    sourcePlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    spry = sourcePlaneRotateY

    sourcePlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    sprz = sourcePlaneRotateZ


class SourcePlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[SourcePlaneRotatePlugOperator]
):
    __slots__ = ()

    sourcePlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    sprx = sourcePlaneRotateX

    sourcePlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    spry = sourcePlaneRotateY

    sourcePlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    sprz = sourcePlaneRotateZ


class SourcePlaneRotateField(
    DoubleAngle3CompoundBaseField[
        SourcePlaneRotateAttrOperator, SourcePlaneRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SourcePlaneRotateAttrOperator
    PLUG_CLS = SourcePlaneRotatePlugOperator

    sourcePlaneRotateX = DoubleAngleField(default_value=0.0, writable=False)
    sprx = sourcePlaneRotateX

    sourcePlaneRotateY = DoubleAngleField(default_value=0.0, writable=False)
    spry = sourcePlaneRotateY

    sourcePlaneRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    sprz = sourcePlaneRotateZ


class RenderPlaneScalePlugOperator(
    Double3CompoundBasePlugOperator["RenderPlaneScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("renderPlaneScaleX", "rpsx"),
        ("renderPlaneScaleY", "rpsy"),
        ("renderPlaneScaleZ", "rpsz"),
    )

    renderPlaneScaleX = DoubleField(default_value=1.0, writable=False)
    rpsx = renderPlaneScaleX

    renderPlaneScaleY = DoubleField(default_value=1.0, writable=False)
    rpsy = renderPlaneScaleY

    renderPlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    rpsz = renderPlaneScaleZ


class RenderPlaneScaleAttrOperator(
    Double3CompoundBaseAttrOperator[RenderPlaneScalePlugOperator]
):
    __slots__ = ()

    renderPlaneScaleX = DoubleField(default_value=1.0, writable=False)
    rpsx = renderPlaneScaleX

    renderPlaneScaleY = DoubleField(default_value=1.0, writable=False)
    rpsy = renderPlaneScaleY

    renderPlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    rpsz = renderPlaneScaleZ


class RenderPlaneScaleField(
    Double3CompoundBaseField[
        RenderPlaneScaleAttrOperator, RenderPlaneScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RenderPlaneScaleAttrOperator
    PLUG_CLS = RenderPlaneScalePlugOperator

    renderPlaneScaleX = DoubleField(default_value=1.0, writable=False)
    rpsx = renderPlaneScaleX

    renderPlaneScaleY = DoubleField(default_value=1.0, writable=False)
    rpsy = renderPlaneScaleY

    renderPlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    rpsz = renderPlaneScaleZ


class SourcePlaneScalePlugOperator(
    Double3CompoundBasePlugOperator["SourcePlaneScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourcePlaneScaleX", "spsx"),
        ("sourcePlaneScaleY", "spsy"),
        ("sourcePlaneScaleZ", "spsz"),
    )

    sourcePlaneScaleX = DoubleField(default_value=1.0, writable=False)
    spsx = sourcePlaneScaleX

    sourcePlaneScaleY = DoubleField(default_value=1.0, writable=False)
    spsy = sourcePlaneScaleY

    sourcePlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    spsz = sourcePlaneScaleZ


class SourcePlaneScaleAttrOperator(
    Double3CompoundBaseAttrOperator[SourcePlaneScalePlugOperator]
):
    __slots__ = ()

    sourcePlaneScaleX = DoubleField(default_value=1.0, writable=False)
    spsx = sourcePlaneScaleX

    sourcePlaneScaleY = DoubleField(default_value=1.0, writable=False)
    spsy = sourcePlaneScaleY

    sourcePlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    spsz = sourcePlaneScaleZ


class SourcePlaneScaleField(
    Double3CompoundBaseField[
        SourcePlaneScaleAttrOperator, SourcePlaneScalePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SourcePlaneScaleAttrOperator
    PLUG_CLS = SourcePlaneScalePlugOperator

    sourcePlaneScaleX = DoubleField(default_value=1.0, writable=False)
    spsx = sourcePlaneScaleX

    sourcePlaneScaleY = DoubleField(default_value=1.0, writable=False)
    spsy = sourcePlaneScaleY

    sourcePlaneScaleZ = DoubleField(default_value=1.0, writable=False)
    spsz = sourcePlaneScaleZ


class AiOffscreenColorPlugOperator(
    Float3CompoundBasePlugOperator["AiOffscreenColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aiOffscreenColorR", "ai_offrscreen_colorr"),
        ("aiOffscreenColorG", "ai_offrscreen_colorg"),
        ("aiOffscreenColorB", "ai_offrscreen_colorb"),
    )

    aiOffscreenColorR = FloatField(default_value=0.0)
    ai_offrscreen_colorr = aiOffscreenColorR

    aiOffscreenColorG = FloatField(default_value=0.0)
    ai_offrscreen_colorg = aiOffscreenColorG

    aiOffscreenColorB = FloatField(default_value=0.0)
    ai_offrscreen_colorb = aiOffscreenColorB


class AiOffscreenColorAttrOperator(
    Float3CompoundBaseAttrOperator[AiOffscreenColorPlugOperator]
):
    __slots__ = ()

    aiOffscreenColorR = FloatField(default_value=0.0)
    ai_offrscreen_colorr = aiOffscreenColorR

    aiOffscreenColorG = FloatField(default_value=0.0)
    ai_offrscreen_colorg = aiOffscreenColorG

    aiOffscreenColorB = FloatField(default_value=0.0)
    ai_offrscreen_colorb = aiOffscreenColorB


class AiOffscreenColorField(
    Float3CompoundBaseField[
        AiOffscreenColorAttrOperator, AiOffscreenColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiOffscreenColorAttrOperator
    PLUG_CLS = AiOffscreenColorPlugOperator

    aiOffscreenColorR = FloatField(default_value=0.0)
    ai_offrscreen_colorr = aiOffscreenColorR

    aiOffscreenColorG = FloatField(default_value=0.0)
    ai_offrscreen_colorg = aiOffscreenColorG

    aiOffscreenColorB = FloatField(default_value=0.0)
    ai_offrscreen_colorb = aiOffscreenColorB
