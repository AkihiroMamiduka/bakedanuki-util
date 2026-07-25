# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.vector_adjust import (
    EnvelopeWeightsListField,
    FunctionField,
    GroupingField,
    InputField,
    ManipulatorTransformsField,
    WeightListField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class AlignmentModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LEFT = 1
    CENTRE = 2
    RIGHT = 3


class AlignmentModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LEFT = 1
    CENTRE = 2
    RIGHT = 3

    NAME_MAP = {
        LEFT: "Left",
        CENTRE: "Centre",
        RIGHT: "Right",
    }


class AlignmentModeEnumField(
    EnumField[AlignmentModeEnumAttrOperator, AlignmentModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlignmentModeEnumAttrOperator
    PLUG_CLS = AlignmentModeEnumPlugOperator


class _GeneratedVectorAdjust(DG):
    __slots__ = ()

    NODE_TYPE = "vectorAdjust"

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

    shellPositions = DataVectorArrayField()

    extrudeDistanceScalePP = DataDoubleArrayField()

    boundingBoxes = DataVectorArrayField()

    selectionIndexes = TypedField()

    manipulatorTransforms = ManipulatorTransformsField()
    manipulatorPositionsPP = manipulatorTransforms.manipulatorPositionsPP
    manipulatorWordPositionsPP = manipulatorTransforms.manipulatorWordPositionsPP
    manipulatorLinePositionsPP = manipulatorTransforms.manipulatorLinePositionsPP
    manipulatorRotationsPP = manipulatorTransforms.manipulatorRotationsPP
    manipulatorWordRotationsPP = manipulatorTransforms.manipulatorWordRotationsPP
    manipulatorLineRotationsPP = manipulatorTransforms.manipulatorLineRotationsPP
    manipulatorScalesPP = manipulatorTransforms.manipulatorScalesPP
    manipulatorWordScalesPP = manipulatorTransforms.manipulatorWordScalesPP
    manipulatorLineScalesPP = manipulatorTransforms.manipulatorLineScalesPP
    manipulateId = manipulatorTransforms.manipulateId
    manipulatePolygon = manipulatorTransforms.manipulatePolygon
    manipulateWord = manipulatorTransforms.manipulateWord
    manipulateLine = manipulatorTransforms.manipulateLine
    alignmentAdjustments = manipulatorTransforms.alignmentAdjustments
    manipulatorMode = manipulatorTransforms.manipulatorMode

    alignmentMode = AlignmentModeEnumField(default_value=1)

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    vertsPerChar = DataDoubleArrayField()

    vertexGroupIds = TypedField()
