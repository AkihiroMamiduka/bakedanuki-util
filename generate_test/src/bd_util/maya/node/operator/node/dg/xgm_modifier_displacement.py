# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_displacement import VectorDisplacementField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class CoordsysEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MUDBOX_XZY = 0
    MAYA_XYZ = 1


class CoordsysEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MUDBOX_XZY = 0
    MAYA_XYZ = 1

    NAME_MAP = {
        MUDBOX_XZY: "Mudbox (XZY)",
        MAYA_XYZ: "Maya (XYZ)",
    }


class CoordsysEnumField(
    EnumField[CoordsysEnumAttrOperator, CoordsysEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordsysEnumAttrOperator
    PLUG_CLS = CoordsysEnumPlugOperator


class XgmModifierDisplacement(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierDisplacement"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    displacement = FloatField()
    dis = displacement

    vectorDisplacement = VectorDisplacementField()
    vdis = vectorDisplacement
    vectorDisplacement0 = vectorDisplacement.vectorDisplacement0
    vdis0 = vectorDisplacement0
    vectorDisplacement1 = vectorDisplacement.vectorDisplacement1
    vdis1 = vectorDisplacement1
    vectorDisplacement2 = vectorDisplacement.vectorDisplacement2
    vdis2 = vectorDisplacement2

    coordsys = CoordsysEnumField()
    cds = coordsys

    scale = FloatField()
    scl = scale

    base = FloatField()
    bs = base

    offset = FloatField()
    os = offset

    bump = FloatField()
    bp = bump

    tweak = TypedField()
    t = tweak
