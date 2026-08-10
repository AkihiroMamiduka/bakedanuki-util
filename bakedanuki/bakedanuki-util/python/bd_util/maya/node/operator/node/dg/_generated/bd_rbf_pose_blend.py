# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_rbf_pose_blend import (
    BaseRotateField,
    BaseScaleField,
    BaseTranslateField,
    OutputQuatField,
    OutputRotateField,
    OutputScaleField,
    OutputTranslateField,
    PoseField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class RotateOrderEnumPlugOperator(
    EnumPlugOperator["RotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class RotateOrderEnumAttrOperator(
    EnumAttrOperator[RotateOrderEnumPlugOperator]
):
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


class BlendStatusEnumPlugOperator(
    EnumPlugOperator["BlendStatusEnumAttrOperator"]
):
    __slots__ = ()

    SUCCESS = 0
    INVALIDWEIGHT = 1
    INVALIDTRANSLATE = 2
    INVALIDROTATE = 3
    INVALIDSCALE = 4
    UNSUPPORTEDROTATEORDER = 5
    NUMERICALFAILURE = 6


class BlendStatusEnumAttrOperator(
    EnumAttrOperator[BlendStatusEnumPlugOperator]
):
    __slots__ = ()

    SUCCESS = 0
    INVALIDWEIGHT = 1
    INVALIDTRANSLATE = 2
    INVALIDROTATE = 3
    INVALIDSCALE = 4
    UNSUPPORTEDROTATEORDER = 5
    NUMERICALFAILURE = 6

    NAME_MAP = {
        SUCCESS: "Success",
        INVALIDWEIGHT: "InvalidWeight",
        INVALIDTRANSLATE: "InvalidTranslate",
        INVALIDROTATE: "InvalidRotate",
        INVALIDSCALE: "InvalidScale",
        UNSUPPORTEDROTATEORDER: "UnsupportedRotateOrder",
        NUMERICALFAILURE: "NumericalFailure",
    }


class BlendStatusEnumField(
    EnumField[BlendStatusEnumAttrOperator, BlendStatusEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendStatusEnumAttrOperator
    PLUG_CLS = BlendStatusEnumPlugOperator


class GeneratedBdRbfPoseBlend(DG):
    __slots__ = ()

    NODE_TYPE = "bdRbf_PoseBlend"

    baseTranslate = BaseTranslateField(default_value=(0.0, 0.0, 0.0))
    bt = baseTranslate
    baseTranslateX = baseTranslate.baseTranslateX
    btx = baseTranslateX
    baseTranslateY = baseTranslate.baseTranslateY
    bty = baseTranslateY
    baseTranslateZ = baseTranslate.baseTranslateZ
    btz = baseTranslateZ

    baseRotate = BaseRotateField(default_value=(0.0, 0.0, 0.0))
    br = baseRotate
    baseRotateX = baseRotate.baseRotateX
    brx = baseRotateX
    baseRotateY = baseRotate.baseRotateY
    bry = baseRotateY
    baseRotateZ = baseRotate.baseRotateZ
    brz = baseRotateZ

    baseScale = BaseScaleField(default_value=(1.0, 1.0, 1.0))
    bsc = baseScale
    baseScaleX = baseScale.baseScaleX
    bscx = baseScaleX
    baseScaleY = baseScale.baseScaleY
    bscy = baseScaleY
    baseScaleZ = baseScale.baseScaleZ
    bscz = baseScaleZ

    rotateOrder = RotateOrderEnumField(default_value=0)
    ro = rotateOrder

    pose = PoseField(multi=True)
    p = pose

    weight = DoubleField(multi=True, default_value=0.0)
    w = weight

    outputTranslate = OutputTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outputTranslate
    outputTranslateX = outputTranslate.outputTranslateX
    otx = outputTranslateX
    outputTranslateY = outputTranslate.outputTranslateY
    oty = outputTranslateY
    outputTranslateZ = outputTranslate.outputTranslateZ
    otz = outputTranslateZ

    outputRotate = OutputRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ort = outputRotate
    outputRotateX = outputRotate.outputRotateX
    orx = outputRotateX
    outputRotateY = outputRotate.outputRotateY
    ory = outputRotateY
    outputRotateZ = outputRotate.outputRotateZ
    orz = outputRotateZ

    outputQuat = OutputQuatField(
        default_value=(0.0, 0.0, 0.0, 1.0), writable=False
    )
    oq = outputQuat
    outputQuatX = outputQuat.outputQuatX
    oqx = outputQuatX
    outputQuatY = outputQuat.outputQuatY
    oqy = outputQuatY
    outputQuatZ = outputQuat.outputQuatZ
    oqz = outputQuatZ
    outputQuatW = outputQuat.outputQuatW
    oqw = outputQuatW

    outputScale = OutputScaleField(
        default_value=(1.0, 1.0, 1.0), writable=False
    )
    os = outputScale
    outputScaleX = outputScale.outputScaleX
    osx = outputScaleX
    outputScaleY = outputScale.outputScaleY
    osy = outputScaleY
    outputScaleZ = outputScale.outputScaleZ
    osz = outputScaleZ

    isValid = BoolField(default_value=True, writable=False)
    iv = isValid

    blendStatus = BlendStatusEnumField(default_value=0, writable=False)
    bst = blendStatus
