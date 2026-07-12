# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.point_on_poly_constraint import (
    ConstraintRotateField,
    ConstraintRotatePivotField,
    ConstraintRotateTranslateField,
    ConstraintTranslateField,
    OffsetRotateField,
    OffsetTranslateField,
    RestRotateField,
    RestTranslateField,
    TargetField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.dt.matrix import DataMatrixField


class ConstraintRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class ConstraintRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class ConstraintRotateOrderEnumField(
    EnumField[ConstraintRotateOrderEnumAttrOperator, ConstraintRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateOrderEnumAttrOperator
    PLUG_CLS = ConstraintRotateOrderEnumPlugOperator


class PointOnPolyConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "pointOnPolyConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    targetU = DoubleField()
    tu = targetU

    targetV = DoubleField()
    tv = targetV

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    constraintRotatePivot = ConstraintRotatePivotField(default_value=(0.0, 0.0, 0.0))
    crp = constraintRotatePivot
    constraintRotatePivotX = constraintRotatePivot.constraintRotatePivotX
    crpx = constraintRotatePivotX
    constraintRotatePivotY = constraintRotatePivot.constraintRotatePivotY
    crpy = constraintRotatePivotY
    constraintRotatePivotZ = constraintRotatePivot.constraintRotatePivotZ
    crpz = constraintRotatePivotZ

    constraintRotateTranslate = ConstraintRotateTranslateField(default_value=(0.0, 0.0, 0.0))
    crt = constraintRotateTranslate
    constraintRotateTranslateX = constraintRotateTranslate.constraintRotateTranslateX
    crtx = constraintRotateTranslateX
    constraintRotateTranslateY = constraintRotateTranslate.constraintRotateTranslateY
    crty = constraintRotateTranslateY
    constraintRotateTranslateZ = constraintRotateTranslate.constraintRotateTranslateZ
    crtz = constraintRotateTranslateZ

    offsetTranslate = OffsetTranslateField(default_value=(0.0, 0.0, 0.0))
    ot = offsetTranslate
    offsetTranslateX = offsetTranslate.offsetTranslateX
    otx = offsetTranslateX
    offsetTranslateY = offsetTranslate.offsetTranslateY
    oty = offsetTranslateY
    offsetTranslateZ = offsetTranslate.offsetTranslateZ
    otz = offsetTranslateZ

    offsetRotate = OffsetRotateField(default_value=(0.0, 0.0, 0.0))
    or_ = offsetRotate
    offsetRotateX = offsetRotate.offsetRotateX
    orx = offsetRotateX
    offsetRotateY = offsetRotate.offsetRotateY
    ory = offsetRotateY
    offsetRotateZ = offsetRotate.offsetRotateZ
    orz = offsetRotateZ

    constraintTranslate = ConstraintTranslateField(default_value=(0.0, 0.0, 0.0), writable=False)
    ct = constraintTranslate
    constraintTranslateX = constraintTranslate.constraintTranslateX
    ctx = constraintTranslateX
    constraintTranslateY = constraintTranslate.constraintTranslateY
    cty = constraintTranslateY
    constraintTranslateZ = constraintTranslate.constraintTranslateZ
    ctz = constraintTranslateZ

    constraintRotate = ConstraintRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0)
    cro = constraintRotateOrder

    restTranslate = RestTranslateField(default_value=(0.0, 0.0, 0.0))
    rst = restTranslate
    restTranslateX = restTranslate.restTranslateX
    rtx = restTranslateX
    restTranslateY = restTranslate.restTranslateY
    rty = restTranslateY
    restTranslateZ = restTranslate.restTranslateZ
    rtz = restTranslateZ

    restRotate = RestRotateField(default_value=(0.0, 0.0, 0.0))
    rsrr = restRotate
    restRotateX = restRotate.restRotateX
    rrx = restRotateX
    restRotateY = restRotate.restRotateY
    rry = restRotateY
    restRotateZ = restRotate.restRotateZ
    rrz = restRotateZ
