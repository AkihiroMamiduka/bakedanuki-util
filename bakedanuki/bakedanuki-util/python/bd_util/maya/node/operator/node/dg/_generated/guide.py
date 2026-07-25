# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.guide import BendVectorField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField


class JointGuideAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    MAX_XYZ = 1
    X = 2
    Y = 3
    Z = 4
    NONE = 5


class JointGuideAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    MAX_XYZ = 1
    X = 2
    Y = 3
    Z = 4
    NONE = 5

    NAME_MAP = {
        AUTO: "auto",
        MAX_XYZ: "max xyz",
        X: "x",
        Y: "y",
        Z: "z",
        NONE: "none",
    }


class JointGuideAxisEnumField(
    EnumField[JointGuideAxisEnumAttrOperator, JointGuideAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = JointGuideAxisEnumAttrOperator
    PLUG_CLS = JointGuideAxisEnumPlugOperator


class _GeneratedGuide(DG):
    __slots__ = ()

    NODE_TYPE = "guide"

    jointAboveMatrix = MatrixField()
    am = jointAboveMatrix

    jointXformMatrix = DataMatrixField()
    jm = jointXformMatrix

    jointBelowMatrix = MatrixField()
    bm = jointBelowMatrix

    jointGuideAxis = JointGuideAxisEnumField(default_value=0)
    ga = jointGuideAxis

    bendVector = BendVectorField(default_value=(0.0, 0.0, 0.0), writable=False)
    bv = bendVector
    bendVectorX = bendVector.bendVectorX
    bx = bendVectorX
    bendVectorY = bendVector.bendVectorY
    by = bendVectorY
    bendVectorZ = bendVector.bendVectorZ
    bz = bendVectorZ

    bendAngle = DoubleAngleField(default_value=0.0, writable=False)
    ba = bendAngle

    bendMagnitude = DoubleLinearField(default_value=0.0, writable=False)
    mg = bendMagnitude

    rotateX = DoubleAngleField(default_value=0.0, writable=False)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0, writable=False)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0, writable=False)
    rz = rotateZ

    maxXYZ = DoubleAngleField(default_value=0.0, writable=False)
    ma = maxXYZ

    autoGuide = DoubleAngleField(default_value=0.0, writable=False)
    ag = autoGuide
