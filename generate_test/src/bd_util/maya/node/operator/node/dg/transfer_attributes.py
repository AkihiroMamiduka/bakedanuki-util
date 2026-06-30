# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.transfer_attributes import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    SearchScaleField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class TransferPositionsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class TransferPositionsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class TransferPositionsEnumField(
    EnumField[TransferPositionsEnumAttrOperator, TransferPositionsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransferPositionsEnumAttrOperator
    PLUG_CLS = TransferPositionsEnumPlugOperator


class TransferNormalsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class TransferNormalsEnumAttrOperator(EnumAttrOperator):
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


class TransferUVsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2


class TransferUVsEnumAttrOperator(EnumAttrOperator):
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


class TransferColorsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SINGLE = 1
    ALL = 2


class TransferColorsEnumAttrOperator(EnumAttrOperator):
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


class SampleSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    LOCAL = 1
    IGNORE_TRANSLATION = 2
    UV = 3
    COMPONENT = 4
    TOPOLOGY = 5


class SampleSpaceEnumAttrOperator(EnumAttrOperator):
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


class SearchMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST_ALONG_NORMAL = 0
    CLOSEST_TO_POINT = 3


class SearchMethodEnumAttrOperator(EnumAttrOperator):
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


class FlipUVsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    U = 1
    V = 2
    BOTH = 3


class FlipUVsEnumAttrOperator(EnumAttrOperator):
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


class ColorBordersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    IGNORE = 0
    PRESERVE = 1


class ColorBordersEnumAttrOperator(EnumAttrOperator):
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


class TransferAttributes(DG):
    __slots__ = ()

    NODE_TYPE = "transferAttributes"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True)
    ocw = envelopeWeightsList

    blockGPU = BoolField()
    bgp = blockGPU

    envelope = FloatField()
    en = envelope

    function = FunctionField()
    f = function
    fchild1 = function.fchild1
    f1 = fchild1
    fchild2 = function.fchild2
    f2 = fchild2
    fchild3 = function.fchild3
    f3 = fchild3

    map64BitIndices = TypedField()
    map = map64BitIndices

    weightList = WeightListField(multi=True)
    wl = weightList

    source = TypedField(multi=True)
    src = source

    transferPositions = TransferPositionsEnumField()
    pos = transferPositions

    transferNormals = TransferNormalsEnumField()
    nml = transferNormals

    transferUVs = TransferUVsEnumField()
    uvs = transferUVs

    sourceUVSet = DataStringField()
    suv = sourceUVSet

    targetUVSet = DataStringField()
    tuv = targetUVSet

    transferColors = TransferColorsEnumField()
    col = transferColors

    sourceColorSet = DataStringField()
    scs = sourceColorSet

    targetColorSet = DataStringField()
    tcs = targetColorSet

    sampleSpace = SampleSpaceEnumField()
    spa = sampleSpace

    sourceUVSpace = DataStringField()
    sus = sourceUVSpace

    targetUVSpace = DataStringField()
    tus = targetUVSpace

    searchMethod = SearchMethodEnumField()
    mtd = searchMethod

    searchDistance = DoubleField()
    dis = searchDistance

    searchTolerance = DoubleField()
    tol = searchTolerance

    searchScale = SearchScaleField()
    ss = searchScale
    searchScaleX = searchScale.searchScaleX
    ssx = searchScaleX
    searchScaleY = searchScale.searchScaleY
    ssy = searchScaleY
    searchScaleZ = searchScale.searchScaleZ
    ssz = searchScaleZ

    flipUVs = FlipUVsEnumField()
    fuv = flipUVs

    colorBorders = ColorBordersEnumField()
    clb = colorBorders

    matchCount = LongField(multi=True)
    mcn = matchCount

    matchChoice = LongField()
    mch = matchChoice
