# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.motion_path import (
    AllCoordinatesField,
    RotateField,
    WorldUpVectorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField


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


class _GeneratedMotionPath(DG):
    __slots__ = ()

    NODE_TYPE = "motionPath"

    uValue = DoubleLinearField(default_value=0.0)
    u = uValue

    frontTwist = DoubleAngleField(default_value=0.0)
    ft = frontTwist

    upTwist = DoubleAngleField(default_value=0.0)
    ut = upTwist

    sideTwist = DoubleAngleField(default_value=0.0)
    st = sideTwist

    allCoordinates = AllCoordinatesField(default_value=(0.0, 0.0, 0.0), writable=False)
    ac = allCoordinates
    xCoordinate = allCoordinates.xCoordinate
    xc = xCoordinate
    yCoordinate = allCoordinates.yCoordinate
    yc = yCoordinate
    zCoordinate = allCoordinates.zCoordinate
    zc = zCoordinate

    orientMatrix = DataMatrixField(writable=False)
    om = orientMatrix

    rotate = RotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    r = rotate
    rotateX = rotate.rotateX
    rx = rotateX
    rotateY = rotate.rotateY
    ry = rotateY
    rotateZ = rotate.rotateZ
    rz = rotateZ

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    flowNode = MessageField()
    fn = flowNode

    geometryPath = GenericField()
    gp = geometryPath

    positionMarkerTime = TimeField(multi=True, default_value=0.0)
    pmt = positionMarkerTime

    orientationMarkerTime = TimeField(multi=True, default_value=0.0)
    omt = orientationMarkerTime

    follow = BoolField(default_value=False)
    f = follow

    normal = BoolField(default_value=False)
    nr = normal

    inverseUp = BoolField(default_value=False)
    iu = inverseUp

    inverseFront = BoolField(default_value=False)
    if_ = inverseFront

    frontAxis = FrontAxisEnumField(default_value=1)
    fa = frontAxis

    upAxis = UpAxisEnumField(default_value=2)
    ua = upAxis

    worldUpType = WorldUpTypeEnumField(default_value=3)
    wut = worldUpType

    worldUpVector = WorldUpVectorField(default_value=(0.0, 1.0, 0.0))
    wu = worldUpVector
    worldUpVectorX = worldUpVector.worldUpVectorX
    wux = worldUpVectorX
    worldUpVectorY = worldUpVector.worldUpVectorY
    wuy = worldUpVectorY
    worldUpVectorZ = worldUpVector.worldUpVectorZ
    wuz = worldUpVectorZ

    worldUpMatrix = MatrixField()
    wum = worldUpMatrix

    bank = BoolField(default_value=False)
    b = bank

    bankScale = DoubleField(default_value=1.0)
    bs = bankScale

    bankLimit = DoubleAngleField(default_value=90.0)
    bl = bankLimit

    fractionMode = BoolField(default_value=False)
    fm = fractionMode

    updateOM = BoolField(default_value=False)
    uom = updateOM
