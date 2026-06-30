# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.svg_to_poly import (
    AnimationPositionField,
    AnimationRotationField,
    AnimationScaleField,
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
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class SvgToPoly(DG):
    __slots__ = ()

    NODE_TYPE = "svgToPoly"

    outputMesh = DataMeshField()

    vertsPerChar = DataDoubleArrayField()

    holeInfo = TypedField()

    numberOfShells = LongField()

    solidsPerCharacter = DataDoubleArrayField()

    characterBoundingBoxesMax = DataVectorArrayField()

    characterBoundingBoxesMin = DataVectorArrayField()

    pathNames = DataStringArrayField()

    pathNamesFromPaste = DataStringArrayField()

    shellPositions = DataVectorArrayField()

    errorIndicator = BoolField()

    legacy2018 = BoolField()

    svgFilepath = DataStringField()

    svgPaste = DataStringField()

    svgMode = SvgModeEnumField()

    curveResolution = LongField()

    enableDistanceFilter = BoolField()

    pointDistanceFilter = FloatField()

    removeColinear = BoolField()

    displayVertexColours = BoolField()

    colinearAngle = FloatField()

    zOffset = FloatField()

    vectorMessages = VectorMessagesField()
    svgMessages = vectorMessages
    animationMessage = vectorMessages.animationMessage
    extrudeMessage = vectorMessages.extrudeMessage
    transformMessage = vectorMessages.transformMessage
    remeshMessage = vectorMessages.remeshMessage
    adjustMessage = vectorMessages.adjustMessage

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

    svgSize = FloatField()

    deformableType = BoolField()

    maxDivisions = LongField()

    maxEdgeLength = FloatField()

    useArtboard = BoolField()
