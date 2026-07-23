# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.solidify import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    WeightListField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class AttachmentModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BORDERS = 0
    FULL = 1


class AttachmentModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BORDERS = 0
    FULL = 1

    NAME_MAP = {
        BORDERS: "Borders",
        FULL: "Full",
    }


class AttachmentModeEnumField(
    EnumField[AttachmentModeEnumAttrOperator, AttachmentModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttachmentModeEnumAttrOperator
    PLUG_CLS = AttachmentModeEnumPlugOperator


class ScaleModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    EDGE = 1
    EDGE_GLOBAL = 2


class ScaleModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    EDGE = 1
    EDGE_GLOBAL = 2

    NAME_MAP = {
        OFF: "Off",
        EDGE: "Edge",
        EDGE_GLOBAL: "Edge Global",
    }


class ScaleModeEnumField(
    EnumField[ScaleModeEnumAttrOperator, ScaleModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleModeEnumAttrOperator
    PLUG_CLS = ScaleModeEnumPlugOperator


class _GeneratedSolidify(DG):
    __slots__ = ()

    NODE_TYPE = "solidify"

    input = InputField(multi=True)
    ip = input

    weightFunction = TypedField(multi=True)
    wfl = weightFunction

    outputGeometry = TypedField(multi=True, writable=False)
    og = outputGeometry

    originalGeometry = TypedField(multi=True)
    orggeom = originalGeometry

    envelopeWeightsList = EnvelopeWeightsListField(multi=True, default_value=1.0, writable=False)
    ocw = envelopeWeightsList

    blockGPU = BoolField(default_value=False)
    bgp = blockGPU

    envelope = FloatField(default_value=1.0, min_value=-2.0, max_value=2.0, soft_min_value=0.0, soft_max_value=1.0)
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

    attachmentMode = AttachmentModeEnumField(default_value=0)
    amd = attachmentMode

    stabilizationLevel = LongField(default_value=0, min_value=0)
    stb = stabilizationLevel

    useBorderFalloff = BoolField(default_value=True)
    ubf = useBorderFalloff

    borderFalloffBlur = LongField(default_value=2, min_value=0)
    bfb = borderFalloffBlur

    islands = DataStringField()
    isl = islands

    normalScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    nsc = normalScale

    tangentPlaneScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    tsc = tangentPlaneScale

    scaleMode = ScaleModeEnumField(default_value=0)
    smd = scaleMode

    scaleEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    sen = scaleEnvelope
