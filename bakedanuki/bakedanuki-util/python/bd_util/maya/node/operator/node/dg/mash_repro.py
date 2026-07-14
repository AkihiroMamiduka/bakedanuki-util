# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_repro import InstancedGroupField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class NormalModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    SOFT_SLASH_HARD = 1
    USER_NORMALS = 2


class NormalModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    SOFT_SLASH_HARD = 1
    USER_NORMALS = 2

    NAME_MAP = {
        NONE: "None",
        SOFT_SLASH_HARD: "Soft/Hard",
        USER_NORMALS: "User Normals",
    }


class NormalModeEnumField(
    EnumField[NormalModeEnumAttrOperator, NormalModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalModeEnumAttrOperator
    PLUG_CLS = NormalModeEnumPlugOperator


class LevelOfDetailEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GEOMETRY = 0
    BOUNDINGBOX = 1


class LevelOfDetailEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GEOMETRY = 0
    BOUNDINGBOX = 1

    NAME_MAP = {
        GEOMETRY: "Geometry",
        BOUNDINGBOX: "BoundingBox",
    }


class LevelOfDetailEnumField(
    EnumField[LevelOfDetailEnumAttrOperator, LevelOfDetailEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LevelOfDetailEnumAttrOperator
    PLUG_CLS = LevelOfDetailEnumPlugOperator


class RotationOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotationOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "XYZ",
        YZX: "YZX",
        ZXY: "ZXY",
        XZY: "XZY",
        YXZ: "YXZ",
        ZYX: "ZYX",
    }


class RotationOrderEnumField(
    EnumField[RotationOrderEnumAttrOperator, RotationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationOrderEnumAttrOperator
    PLUG_CLS = RotationOrderEnumPlugOperator


class MotionBlurInstanceModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MOTION_BLUR_COMPATIBLE = 0
    CHANGING_TOPOLOGY = 1


class MotionBlurInstanceModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MOTION_BLUR_COMPATIBLE = 0
    CHANGING_TOPOLOGY = 1

    NAME_MAP = {
        MOTION_BLUR_COMPATIBLE: "Motion Blur Compatible",
        CHANGING_TOPOLOGY: "Changing Topology",
    }


class MotionBlurInstanceModeEnumField(
    EnumField[MotionBlurInstanceModeEnumAttrOperator, MotionBlurInstanceModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurInstanceModeEnumAttrOperator
    PLUG_CLS = MotionBlurInstanceModeEnumPlugOperator


class MASH_Repro(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Repro"

    numberOfObjects = LongField(default_value=0)

    loopId = LongField(default_value=0, writable=False)

    updating = BoolField(default_value=False)
    upd = updating

    finishUpdating = BoolField(default_value=False)
    fupd = finishUpdating

    meshMessage = MessageField()
    meshmessage = meshMessage

    inputPoints = TypedField()

    setNormals = BoolField(default_value=True)
    setN = setNormals

    normalMode = NormalModeEnumField(default_value=1)

    setUVs = BoolField(default_value=True)

    setColors = BoolField(default_value=False)
    setC = setColors

    useGPU = BoolField(default_value=False)
    gpu = useGPU

    levelOfDetail = LevelOfDetailEnumField(default_value=0)
    lod = levelOfDetail

    cameraMatrix = MatrixField()
    cmtx = cameraMatrix

    rotationOrder = RotationOrderEnumField(default_value=0)
    roto = rotationOrder

    instancedGroup = InstancedGroupField(multi=True)

    outMesh = DataMeshField(writable=False)
    out = outMesh

    meshMatrix = MatrixField()
    mmtx = meshMatrix

    positionAttributeName = DataStringField()
    pAttrName = positionAttributeName

    rotationAttributeName = DataStringField()
    rAttrName = rotationAttributeName

    scaleAttributeName = DataStringField()
    sAttrName = scaleAttributeName

    objectIndexAttributeName = DataStringField()
    oIdAttrName = objectIndexAttributeName

    visibilityAttributeName = DataStringField()
    visibilityAttrName = visibilityAttributeName

    colorAttributeName = DataStringField()
    colAttrName = colorAttributeName

    uvTileAttributeName = DataStringField()
    uvAttrName = uvTileAttributeName

    animatedAttributeName = DataStringField()
    animAttrName = animatedAttributeName

    frameAttributeName = DataStringField()
    frameAttrName = frameAttributeName

    motionBlurInstanceMode = MotionBlurInstanceModeEnumField(default_value=0)
    mbim = motionBlurInstanceMode
