# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.type import (
    AnimationPositionField,
    AnimationRotationField,
    AnimationScaleField,
    GroupingField,
    ManipulatorTransformsField,
    PositionAdjustField,
    RandomRangeField,
    RotationAdjustField,
    ScaleAdjustField,
    VectorMessagesField,
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
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class AlignmentModeEnumPlugOperator(EnumPlugOperator["AlignmentModeEnumAttrOperator"]):
    __slots__ = ()

    LEFT = 1
    CENTRE = 2
    RIGHT = 3


class AlignmentModeEnumAttrOperator(EnumAttrOperator[AlignmentModeEnumPlugOperator]):
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


class GeneratorEnumPlugOperator(EnumPlugOperator["GeneratorEnumAttrOperator"]):
    __slots__ = ()

    OFF = 0
    FRAME_NUMBER = 1
    SCENE_TIME = 2
    RANDOM = 6
    ANIMATED_TEXT = 8
    PYTHON = 9


class GeneratorEnumAttrOperator(EnumAttrOperator[GeneratorEnumPlugOperator]):
    __slots__ = ()

    OFF = 0
    FRAME_NUMBER = 1
    SCENE_TIME = 2
    RANDOM = 6
    ANIMATED_TEXT = 8
    PYTHON = 9

    NAME_MAP = {
        OFF: "Off",
        FRAME_NUMBER: "Frame Number",
        SCENE_TIME: "Scene Time",
        RANDOM: "Random",
        ANIMATED_TEXT: "Animated Text",
        PYTHON: "Python",
    }


class GeneratorEnumField(
    EnumField[GeneratorEnumAttrOperator, GeneratorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeneratorEnumAttrOperator
    PLUG_CLS = GeneratorEnumPlugOperator


class RandomizerModeEnumPlugOperator(EnumPlugOperator["RandomizerModeEnumAttrOperator"]):
    __slots__ = ()

    ALPHANUMERIC = 0
    ALPHABETICAL = 1
    NUMERIC = 2
    INPUT_TEXT = 3


class RandomizerModeEnumAttrOperator(EnumAttrOperator[RandomizerModeEnumPlugOperator]):
    __slots__ = ()

    ALPHANUMERIC = 0
    ALPHABETICAL = 1
    NUMERIC = 2
    INPUT_TEXT = 3

    NAME_MAP = {
        ALPHANUMERIC: "Alphanumeric",
        ALPHABETICAL: "Alphabetical",
        NUMERIC: "Numeric",
        INPUT_TEXT: "Input Text",
    }


class RandomizerModeEnumField(
    EnumField[RandomizerModeEnumAttrOperator, RandomizerModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RandomizerModeEnumAttrOperator
    PLUG_CLS = RandomizerModeEnumPlugOperator


class GeneratedType(DG):
    __slots__ = ()

    NODE_TYPE = "type"

    grouping = GroupingField()
    solidsPerCharacter = grouping.solidsPerCharacter
    solidsPerWord = grouping.solidsPerWord
    solidsPerLine = grouping.solidsPerLine

    vertsPerChar = DataDoubleArrayField()

    characterBoundingBoxesMax = DataVectorArrayField()

    characterBoundingBoxesMin = DataVectorArrayField()

    outputMesh = DataMeshField()

    manipulatorPivots = DataVectorArrayField()

    holeInfo = TypedField()

    numberOfShells = LongField(default_value=0)

    fontError = DataStringField(writable=False)

    textInput = DataStringField()

    currentFont = DataStringField()

    currentStyle = DataStringField()

    writingSystem = DataStringField()

    homeFolder = DataStringField(writable=False)

    fontList = DataStringField(writable=False)

    styleList = DataStringField(writable=False)

    fontStyleList = DataStringArrayField(writable=False)

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

    fontSize = FloatField(default_value=20.0, soft_min_value=0.1, soft_max_value=100.0)

    kerningScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    spaceWidthScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    tracking = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)

    leadingScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)

    curveResolution = LongField(default_value=4, min_value=1, max_value=100, soft_max_value=10)

    alignmentMode = AlignmentModeEnumField(default_value=1)

    positionAdjust = PositionAdjustField(default_value=(0.0, 0.0, 0.0))
    positionAdjust0 = positionAdjust.positionAdjust0
    positionAdjust1 = positionAdjust.positionAdjust1
    positionAdjust2 = positionAdjust.positionAdjust2

    rotationAdjust = RotationAdjustField(default_value=(0.0, 0.0, 0.0))
    rotationAdjust0 = rotationAdjust.rotationAdjust0
    rotationAdjust1 = rotationAdjust.rotationAdjust1
    rotationAdjust2 = rotationAdjust.rotationAdjust2

    scaleAdjust = ScaleAdjustField(default_value=(0.0, 0.0, 0.0))
    scaleAdjust0 = scaleAdjust.scaleAdjust0
    scaleAdjust1 = scaleAdjust.scaleAdjust1
    scaleAdjust2 = scaleAdjust.scaleAdjust2

    enableDistanceFilter = BoolField(default_value=False)

    pointDistanceFilter = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=5.0)

    setParity = BoolField(default_value=False)

    removeColinear = BoolField(default_value=False)

    colinearAngle = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=40.0, soft_max_value=5.0)

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

    deformableType = BoolField(default_value=False)

    legacyDecomposition = BoolField(default_value=False)

    preTLDecompose = BoolField(default_value=False)

    maxDivisions = LongField(default_value=20, min_value=1, max_value=100, soft_max_value=30)

    maxEdgeLength = FloatField(default_value=5.0, min_value=0.01, soft_min_value=0.1, soft_max_value=15.0)

    vectorMessages = VectorMessagesField()
    typeMessages = vectorMessages
    animationMessage = vectorMessages.animationMessage
    extrudeMessage = vectorMessages.extrudeMessage
    transformMessage = vectorMessages.transformMessage
    remeshMessage = vectorMessages.remeshMessage

    generator = GeneratorEnumField(default_value=0)

    countdown = LongField(default_value=0)

    changeRate = LongField(default_value=1, min_value=1, soft_max_value=100)

    randomRange = RandomRangeField(default_value=(0, 10))
    randomRange0 = randomRange.randomRange0
    randomRange1 = randomRange.randomRange1

    length = LongField(default_value=4, min_value=0, soft_max_value=20)

    decimalPlaces = LongField(default_value=3, min_value=0, soft_max_value=10)

    randomSeed = LongField(default_value=0, min_value=1, soft_max_value=100)

    percent = LongField(default_value=0, min_value=0, soft_max_value=100)

    reverse = BoolField(default_value=False)

    random = BoolField(default_value=False)

    delay = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    randomizerMode = RandomizerModeEnumField(default_value=1)

    time = TimeField(default_value=1.0)
    ti = time

    animatedType = DataStringField()

    pythonExpression = DataStringField()
