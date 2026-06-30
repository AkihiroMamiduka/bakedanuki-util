# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.motion_path import (
    AllCoordinatesField,
    RotateField,
    WorldUpVectorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class RotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class RotateOrderEnumField(
    EnumField[RotateOrderEnumAttrOperator, RotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateOrderEnumAttrOperator
    PLUG_CLS = RotateOrderEnumPlugOperator


class FrontAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class FrontAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class FrontAxisEnumField(
    EnumField[FrontAxisEnumAttrOperator, FrontAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrontAxisEnumAttrOperator
    PLUG_CLS = FrontAxisEnumPlugOperator


class UpAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class UpAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class UpAxisEnumField(
    EnumField[UpAxisEnumAttrOperator, UpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpAxisEnumAttrOperator
    PLUG_CLS = UpAxisEnumPlugOperator


class WorldUpTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_ROTATION_UP = 2
    VECTOR = 3
    NORMAL = 4


class WorldUpTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_ROTATION_UP = 2
    VECTOR = 3
    NORMAL = 4

    NAME_MAP = {
        SCENE_UP: "Scene Up",
        OBJECT_UP: "Object Up",
        OBJECT_ROTATION_UP: "Object Rotation Up",
        VECTOR: "Vector",
        NORMAL: "Normal",
    }


class WorldUpTypeEnumField(
    EnumField[WorldUpTypeEnumAttrOperator, WorldUpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldUpTypeEnumAttrOperator
    PLUG_CLS = WorldUpTypeEnumPlugOperator


class MotionPath(DG):
    __slots__ = ()

    NODE_TYPE = "motionPath"

    uValue = DoubleLinearField()
    u = uValue

    frontTwist = DoubleAngleField()
    ft = frontTwist

    upTwist = DoubleAngleField()
    ut = upTwist

    sideTwist = DoubleAngleField()
    st = sideTwist

    allCoordinates = AllCoordinatesField()
    ac = allCoordinates
    xCoordinate = allCoordinates.xCoordinate
    xc = xCoordinate
    yCoordinate = allCoordinates.yCoordinate
    yc = yCoordinate
    zCoordinate = allCoordinates.zCoordinate
    zc = zCoordinate

    orientMatrix = DataMatrixField()
    om = orientMatrix

    rotate = RotateField()
    r = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    rotateOrder = RotateOrderEnumField()
    ro = rotateOrder

    flowNode = MessageField()
    fn = flowNode

    geometryPath = GenericField()
    gp = geometryPath

    positionMarkerTime = TimeField(multi=True)
    pmt = positionMarkerTime

    orientationMarkerTime = TimeField(multi=True)
    omt = orientationMarkerTime

    follow = BoolField()
    f = follow

    normal = BoolField()
    nr = normal

    inverseUp = BoolField()
    iu = inverseUp

    inverseFront = BoolField()
    if_ = inverseFront

    frontAxis = FrontAxisEnumField()
    fa = frontAxis

    upAxis = UpAxisEnumField()
    ua = upAxis

    worldUpType = WorldUpTypeEnumField()
    wut = worldUpType

    worldUpVector = WorldUpVectorField()
    wu = worldUpVector
    worldUpVectorX = worldUpVector.worldUpVectorX
    wux = worldUpVectorX
    worldUpVectorY = worldUpVector.worldUpVectorY
    wuy = worldUpVectorY
    worldUpVectorZ = worldUpVector.worldUpVectorZ
    wuz = worldUpVectorZ

    worldUpMatrix = MatrixField()
    wum = worldUpMatrix

    bank = BoolField()
    b = bank

    bankScale = DoubleField()
    bs = bankScale

    bankLimit = DoubleAngleField()
    bl = bankLimit

    fractionMode = BoolField()
    fm = fractionMode

    updateOM = BoolField()
    uom = updateOM
