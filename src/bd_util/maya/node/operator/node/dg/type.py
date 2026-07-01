# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.type import (
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
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class GeneratorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    FRAME_NUMBER = 1
    SCENE_TIME = 2
    RANDOM = 6
    ANIMATED_TEXT = 8
    PYTHON = 9


class GeneratorEnumAttrOperator(EnumAttrOperator):
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


class RandomizerModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALPHANUMERIC = 0
    ALPHABETICAL = 1
    NUMERIC = 2
    INPUT_TEXT = 3


class RandomizerModeEnumAttrOperator(EnumAttrOperator):
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


class Type(DG):
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

    numberOfShells = LongField()

    fontError = DataStringField()

    textInput = DataStringField()

    currentFont = DataStringField()

    currentStyle = DataStringField()

    writingSystem = DataStringField()

    homeFolder = DataStringField()

    fontList = DataStringField()

    styleList = DataStringField()

    fontStyleList = DataStringArrayField()

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

    fontSize = FloatField()

    kerningScale = FloatField()

    spaceWidthScale = FloatField()

    tracking = FloatField()

    leadingScale = FloatField()

    curveResolution = LongField()

    alignmentMode = AlignmentModeEnumField()

    positionAdjust = PositionAdjustField()
    positionAdjust0 = positionAdjust.positionAdjust0
    positionAdjust1 = positionAdjust.positionAdjust1
    positionAdjust2 = positionAdjust.positionAdjust2

    rotationAdjust = RotationAdjustField()
    rotationAdjust0 = rotationAdjust.rotationAdjust0
    rotationAdjust1 = rotationAdjust.rotationAdjust1
    rotationAdjust2 = rotationAdjust.rotationAdjust2

    scaleAdjust = ScaleAdjustField()
    scaleAdjust0 = scaleAdjust.scaleAdjust0
    scaleAdjust1 = scaleAdjust.scaleAdjust1
    scaleAdjust2 = scaleAdjust.scaleAdjust2

    enableDistanceFilter = BoolField()

    pointDistanceFilter = FloatField()

    setParity = BoolField()

    removeColinear = BoolField()

    colinearAngle = FloatField()

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

    deformableType = BoolField()

    legacyDecomposition = BoolField()

    preTLDecompose = BoolField()

    maxDivisions = LongField()

    maxEdgeLength = FloatField()

    vectorMessages = VectorMessagesField()
    typeMessages = vectorMessages
    animationMessage = vectorMessages.animationMessage
    extrudeMessage = vectorMessages.extrudeMessage
    transformMessage = vectorMessages.transformMessage
    remeshMessage = vectorMessages.remeshMessage

    generator = GeneratorEnumField()

    countdown = LongField()

    changeRate = LongField()

    randomRange = RandomRangeField()
    randomRange0 = randomRange.randomRange0
    randomRange1 = randomRange.randomRange1

    length = LongField()

    decimalPlaces = LongField()

    randomSeed = LongField()

    percent = LongField()

    reverse = BoolField()

    random = BoolField()

    delay = FloatField()

    randomizerMode = RandomizerModeEnumField()

    time = TimeField()
    ti = time

    animatedType = DataStringField()

    pythonExpression = DataStringField()
