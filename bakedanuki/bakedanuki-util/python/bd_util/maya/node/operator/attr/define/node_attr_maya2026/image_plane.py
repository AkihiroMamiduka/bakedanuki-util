# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
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
