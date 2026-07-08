# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sculpt import (
    EnvelopeWeightsListField,
    FunctionField,
    InputField,
    StartPositionField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLIP = 0
    PROJECT = 1
    STRETCH = 2


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLIP = 0
    PROJECT = 1
    STRETCH = 2

    NAME_MAP = {
        FLIP: "flip",
        PROJECT: "project",
        STRETCH: "stretch",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class InsideModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RING = 0
    EVEN = 1


class InsideModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RING = 0
    EVEN = 1

    NAME_MAP = {
        RING: "ring",
        EVEN: "even",
    }


class InsideModeEnumField(
    EnumField[InsideModeEnumAttrOperator, InsideModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InsideModeEnumAttrOperator
    PLUG_CLS = InsideModeEnumPlugOperator


class DropoffTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1


class DropoffTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1

    NAME_MAP = {
        NONE: "none",
        LINEAR: "linear",
    }


class DropoffTypeEnumField(
    EnumField[DropoffTypeEnumAttrOperator, DropoffTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DropoffTypeEnumAttrOperator
    PLUG_CLS = DropoffTypeEnumPlugOperator


class Sculpt(DG):
    __slots__ = ()

    NODE_TYPE = "sculpt"

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

    sculptObjectMatrix = MatrixField()
    sm = sculptObjectMatrix

    sculptObjectGeometry = TypedField()
    sg = sculptObjectGeometry

    mode = ModeEnumField(default_value=2)
    mo = mode

    insideMode = InsideModeEnumField(default_value=1)
    im = insideMode

    maximumDisplacement = DoubleLinearField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    md = maximumDisplacement

    dropoffDistance = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    dd = dropoffDistance

    dropoffType = DropoffTypeEnumField(default_value=1)
    dt = dropoffType

    startPosition = StartPositionField(default_value=(0.0, 0.0, 0.0))
    sp = startPosition
    startPosX = startPosition.startPosX
    sx = startPosX
    startPosY = startPosition.startPosY
    sy = startPosY
    startPosZ = startPosition.startPosZ
    sz = startPosZ

    extendedEnd = BoolField(default_value=False)
    exd = extendedEnd
