# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shell_deformer import (
    AnimationPositionField,
    AnimationRotationField,
    AnimationScaleField,
    EnvelopeWeightsListField,
    FunctionField,
    GroupingField,
    InputField,
    TranslateInPPField,
    WeightListField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class AnimationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CHARACTER = 1
    WORD = 2
    LINE = 3


class AnimationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CHARACTER = 1
    WORD = 2
    LINE = 3

    NAME_MAP = {
        CHARACTER: "Character",
        WORD: "Word",
        LINE: "Line",
    }


class AnimationModeEnumField(
    EnumField[AnimationModeEnumAttrOperator, AnimationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationModeEnumAttrOperator
    PLUG_CLS = AnimationModeEnumPlugOperator


class ShellDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "shellDeformer"

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

    triggeredByMASH = BoolField()

    inputPoints = TypedField()

    rotationPivotPointsPP = DataVectorArrayField()

    scalePivotPointsPP = DataVectorArrayField()

    time = TimeField()
    ti = time

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP

    enableAnimation = BoolField()

    randomDelay = BoolField()

    reverseOrder = BoolField()

    animationPosition = AnimationPositionField()
    animationPositionX = animationPosition.animationPositionX
    animationPositionY = animationPosition.animationPositionY
    animationPositionZ = animationPosition.animationPositionZ

    animationRotation = AnimationRotationField()
    animationRotationX = animationRotation.animationRotationX
    animationRotationY = animationRotation.animationRotationY
    animationRotationZ = animationRotation.animationRotationZ

    animationScale = AnimationScaleField()
    animationScaleX = animationScale.animationScaleX
    animationScaleY = animationScale.animationScaleY
    animationScaleZ = animationScale.animationScaleZ

    enablePivotDisplay = BoolField()

    xPivotLocation = FloatField()

    yPivotLocation = FloatField()

    zPivotLocation = FloatField()

    localXRotationPivot = BoolField()

    localYRotationPivot = BoolField()

    localZRotationPivot = BoolField()

    localYScalePivot = BoolField()

    localXScalePivot = BoolField()

    localZScalePivot = BoolField()

    randomSeed = LongField()

    offsetFrames = FloatField()

    animationMode = AnimationModeEnumField()

    vertsPerChar = DataDoubleArrayField()

    vertexGroupIds = TypedField()

    legacy2018 = BoolField()
