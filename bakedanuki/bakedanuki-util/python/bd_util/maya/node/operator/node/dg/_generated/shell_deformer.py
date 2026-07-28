# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.shell_deformer import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class AnimationModeEnumPlugOperator(EnumPlugOperator["AnimationModeEnumAttrOperator"]):
    __slots__ = ()

    CHARACTER = 1
    WORD = 2
    LINE = 3


class AnimationModeEnumAttrOperator(EnumAttrOperator[AnimationModeEnumPlugOperator]):
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


class GeneratedShellDeformer(DG):
    __slots__ = ()

    NODE_TYPE = "shellDeformer"

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

    triggeredByMASH = BoolField(default_value=False, readable=False)

    inputPoints = TypedField()

    rotationPivotPointsPP = DataVectorArrayField()

    scalePivotPointsPP = DataVectorArrayField()

    time = TimeField(default_value=1.0)
    ti = time

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP

    enableAnimation = BoolField(default_value=False)

    randomDelay = BoolField(default_value=False)

    reverseOrder = BoolField(default_value=False)

    animationPosition = AnimationPositionField(default_value=(0.0, 0.0, 0.0))
    animationPositionX = animationPosition.animationPositionX
    animationPositionY = animationPosition.animationPositionY
    animationPositionZ = animationPosition.animationPositionZ

    animationRotation = AnimationRotationField(default_value=(0.0, 0.0, 0.0))
    animationRotationX = animationRotation.animationRotationX
    animationRotationY = animationRotation.animationRotationY
    animationRotationZ = animationRotation.animationRotationZ

    animationScale = AnimationScaleField(default_value=(1.0, 1.0, 1.0))
    animationScaleX = animationScale.animationScaleX
    animationScaleY = animationScale.animationScaleY
    animationScaleZ = animationScale.animationScaleZ

    enablePivotDisplay = BoolField(default_value=False)

    xPivotLocation = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    yPivotLocation = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    zPivotLocation = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    localXRotationPivot = BoolField(default_value=True)

    localYRotationPivot = BoolField(default_value=False)

    localZRotationPivot = BoolField(default_value=True)

    localYScalePivot = BoolField(default_value=False)

    localXScalePivot = BoolField(default_value=True)

    localZScalePivot = BoolField(default_value=True)

    randomSeed = LongField(default_value=0, min_value=0, soft_max_value=100)

    offsetFrames = FloatField(default_value=50.0, soft_min_value=-100.0, soft_max_value=100.0)

    animationMode = AnimationModeEnumField(default_value=1)

    vertsPerChar = DataDoubleArrayField()

    vertexGroupIds = TypedField()

    legacy2018 = BoolField(default_value=False)
