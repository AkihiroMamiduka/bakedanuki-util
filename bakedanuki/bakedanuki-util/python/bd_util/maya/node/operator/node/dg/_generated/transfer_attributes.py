# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.transfer_attributes import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    SearchScaleField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class TransferPositionsEnumPlugOperator(
    EnumPlugOperator["TransferPositionsEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    ON = 1


class TransferPositionsEnumAttrOperator(
    EnumAttrOperator[TransferPositionsEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class TransferPositionsEnumField(
    EnumField[
        TransferPositionsEnumAttrOperator, TransferPositionsEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TransferPositionsEnumAttrOperator
    PLUG_CLS = TransferPositionsEnumPlugOperator


class TransferNormalsEnumPlugOperator(
    EnumPlugOperator["TransferNormalsEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    ON = 1


class TransferNormalsEnumAttrOperator(
    EnumAttrOperator[TransferNormalsEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class TransferNormalsEnumField(
    EnumField[TransferNormalsEnumAttrOperator, TransferNormalsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransferNormalsEnumAttrOperator
    PLUG_CLS = TransferNormalsEnumPlugOperator


class TransferUVsEnumPlugOperator(
    EnumPlugOperator["TransferUVsEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2


class TransferUVsEnumAttrOperator(
    EnumAttrOperator[TransferUVsEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2

    NAME_MAP = {
        OFF: "Off",
        SINGLE: "Single",
        ALL: "All",
    }


class TransferUVsEnumField(
    EnumField[TransferUVsEnumAttrOperator, TransferUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransferUVsEnumAttrOperator
    PLUG_CLS = TransferUVsEnumPlugOperator


class TransferColorsEnumPlugOperator(
    EnumPlugOperator["TransferColorsEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2


class TransferColorsEnumAttrOperator(
    EnumAttrOperator[TransferColorsEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2

    NAME_MAP = {
        OFF: "Off",
        SINGLE: "Single",
        ALL: "All",
    }


class TransferColorsEnumField(
    EnumField[TransferColorsEnumAttrOperator, TransferColorsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransferColorsEnumAttrOperator
    PLUG_CLS = TransferColorsEnumPlugOperator


class SampleSpaceEnumPlugOperator(
    EnumPlugOperator["SampleSpaceEnumAttrOperator"]
):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    IGNORE_TRANSLATION = 2
    UV = 3
    COMPONENT = 4
    TOPOLOGY = 5


class SampleSpaceEnumAttrOperator(
    EnumAttrOperator[SampleSpaceEnumPlugOperator]
):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    IGNORE_TRANSLATION = 2
    UV = 3
    COMPONENT = 4
    TOPOLOGY = 5

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
        IGNORE_TRANSLATION: "Ignore Translation",
        UV: "UV",
        COMPONENT: "Component",
        TOPOLOGY: "Topology",
    }


class SampleSpaceEnumField(
    EnumField[SampleSpaceEnumAttrOperator, SampleSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SampleSpaceEnumAttrOperator
    PLUG_CLS = SampleSpaceEnumPlugOperator


class SearchMethodEnumPlugOperator(
    EnumPlugOperator["SearchMethodEnumAttrOperator"]
):
    __slots__ = ()

    CLOSEST_ALONG_NORMAL = 0
    CLOSEST_TO_POINT = 3


class SearchMethodEnumAttrOperator(
    EnumAttrOperator[SearchMethodEnumPlugOperator]
):
    __slots__ = ()

    CLOSEST_ALONG_NORMAL = 0
    CLOSEST_TO_POINT = 3

    NAME_MAP = {
        CLOSEST_ALONG_NORMAL: "Closest along normal",
        CLOSEST_TO_POINT: "Closest to point",
    }


class SearchMethodEnumField(
    EnumField[SearchMethodEnumAttrOperator, SearchMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SearchMethodEnumAttrOperator
    PLUG_CLS = SearchMethodEnumPlugOperator


class FlipUVsEnumPlugOperator(EnumPlugOperator["FlipUVsEnumAttrOperator"]):
    __slots__ = ()

    OFF = 0
    U = 1
    V = 2
    BOTH = 3


class FlipUVsEnumAttrOperator(EnumAttrOperator[FlipUVsEnumPlugOperator]):
    __slots__ = ()

    OFF = 0
    U = 1
    V = 2
    BOTH = 3

    NAME_MAP = {
        OFF: "Off",
        U: "U",
        V: "V",
        BOTH: "Both",
    }


class FlipUVsEnumField(
    EnumField[FlipUVsEnumAttrOperator, FlipUVsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlipUVsEnumAttrOperator
    PLUG_CLS = FlipUVsEnumPlugOperator


class ColorBordersEnumPlugOperator(
    EnumPlugOperator["ColorBordersEnumAttrOperator"]
):
    __slots__ = ()

    IGNORE = 0
    PRESERVE = 1


class ColorBordersEnumAttrOperator(
    EnumAttrOperator[ColorBordersEnumPlugOperator]
):
    __slots__ = ()

    IGNORE = 0
    PRESERVE = 1

    NAME_MAP = {
        IGNORE: "Ignore",
        PRESERVE: "Preserve",
    }


class ColorBordersEnumField(
    EnumField[ColorBordersEnumAttrOperator, ColorBordersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorBordersEnumAttrOperator
    PLUG_CLS = ColorBordersEnumPlugOperator


class GeneratedTransferAttributes(DG):
    __slots__ = ()

    NODE_TYPE = "transferAttributes"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(
        multi=True, default_value=1.0, writable=False
    )
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(
        default_value=1.0,
        min_value=-2.0,
        max_value=2.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    en = envelope

    function = FunctionField(default_value=(0, 0, 0), readable=False)
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True, default_value=1.0)
    wl = weightList

    source = TypedField(multi=True)
    src = source

    transferPositions = TransferPositionsEnumField(default_value=0)
    pos = transferPositions

    transferNormals = TransferNormalsEnumField(default_value=0)
    nml = transferNormals

    transferUVs = TransferUVsEnumField(default_value=0)
    uvs = transferUVs

    sourceUVSet = DataStringField()
    suv = sourceUVSet

    targetUVSet = DataStringField()
    tuv = targetUVSet

    transferColors = TransferColorsEnumField(default_value=0)
    col = transferColors

    sourceColorSet = DataStringField()
    scs = sourceColorSet

    targetColorSet = DataStringField()
    tcs = targetColorSet

    sampleSpace = SampleSpaceEnumField(default_value=0)
    spa = sampleSpace

    sourceUVSpace = DataStringField()
    sus = sourceUVSpace

    targetUVSpace = DataStringField()
    tus = targetUVSpace

    searchMethod = SearchMethodEnumField(default_value=3)
    mtd = searchMethod

    searchDistance = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=5.0
    )
    dis = searchDistance

    searchTolerance = DoubleField(
        default_value=1.3, soft_min_value=1.0, soft_max_value=2.0
    )
    tol = searchTolerance

    searchScale = SearchScaleField(default_value=(1.0, 1.0, 1.0))
    ss = searchScale
    searchScaleX = searchScale.searchScaleX
    ssx = searchScaleX
    searchScaleY = searchScale.searchScaleY
    ssy = searchScaleY
    searchScaleZ = searchScale.searchScaleZ
    ssz = searchScaleZ

    flipUVs = FlipUVsEnumField(default_value=0)
    fuv = flipUVs

    colorBorders = ColorBordersEnumField(default_value=1)
    clb = colorBorders

    matchCount = LongField(multi=True, default_value=0, writable=False)
    mcn = matchCount

    matchChoice = LongField(default_value=0)
    mch = matchChoice
