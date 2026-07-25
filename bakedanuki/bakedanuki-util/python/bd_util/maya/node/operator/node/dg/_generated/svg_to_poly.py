# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.svg_to_poly import (
    AnimationPositionField,
    AnimationRotationField,
    AnimationScaleField,
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
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class SvgModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FROM_FILE = 1
    COPY_SLASH_PASTE = 2


class SvgModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FROM_FILE = 1
    COPY_SLASH_PASTE = 2

    NAME_MAP = {
        FROM_FILE: "From File",
        COPY_SLASH_PASTE: "Copy/Paste",
    }


class SvgModeEnumField(
    EnumField[SvgModeEnumAttrOperator, SvgModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SvgModeEnumAttrOperator
    PLUG_CLS = SvgModeEnumPlugOperator


class _GeneratedSvgToPoly(DG):
    __slots__ = ()

    NODE_TYPE = "svgToPoly"

    outputMesh = DataMeshField()

    vertsPerChar = DataDoubleArrayField()

    holeInfo = TypedField()

    numberOfShells = LongField(default_value=0)

    solidsPerCharacter = DataDoubleArrayField()

    characterBoundingBoxesMax = DataVectorArrayField()

    characterBoundingBoxesMin = DataVectorArrayField()

    pathNames = DataStringArrayField()

    pathNamesFromPaste = DataStringArrayField()

    shellPositions = DataVectorArrayField()

    errorIndicator = BoolField(default_value=False)

    legacy2018 = BoolField(default_value=False)

    svgFilepath = DataStringField()

    svgPaste = DataStringField()

    svgMode = SvgModeEnumField(default_value=1)

    curveResolution = LongField(default_value=4, min_value=1, max_value=100, soft_max_value=10)

    enableDistanceFilter = BoolField(default_value=True)

    pointDistanceFilter = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=5.0)

    removeColinear = BoolField(default_value=False)

    displayVertexColours = BoolField(default_value=True)

    colinearAngle = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=40.0, soft_max_value=5.0)

    zOffset = FloatField(default_value=0.0010000000474974513, min_value=0.0, soft_max_value=5.0)

    vectorMessages = VectorMessagesField()
    svgMessages = vectorMessages
    animationMessage = vectorMessages.animationMessage
    extrudeMessage = vectorMessages.extrudeMessage
    transformMessage = vectorMessages.transformMessage
    remeshMessage = vectorMessages.remeshMessage
    adjustMessage = vectorMessages.adjustMessage

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

    svgSize = FloatField(default_value=10.0, min_value=0.0, soft_max_value=5.0)

    deformableType = BoolField(default_value=False)

    maxDivisions = LongField(default_value=20, min_value=1, max_value=100, soft_max_value=30)

    maxEdgeLength = FloatField(default_value=5.0, min_value=0.01, soft_min_value=0.1, soft_max_value=15.0)

    useArtboard = BoolField(default_value=False)
