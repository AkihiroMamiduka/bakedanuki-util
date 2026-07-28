# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_modifier_displacement import VectorDisplacementField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField


class CoordsysEnumPlugOperator(EnumPlugOperator["CoordsysEnumAttrOperator"]):
    __slots__ = ()

    MUDBOX_XZY = 0
    MAYA_XYZ = 1


class CoordsysEnumAttrOperator(EnumAttrOperator[CoordsysEnumPlugOperator]):
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


class GeneratedXgmModifierDisplacement(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierDisplacement"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    displacement = FloatField(default_value=0.0)
    dis = displacement

    vectorDisplacement = VectorDisplacementField(default_value=(0.0, 0.0, 0.0))
    vdis = vectorDisplacement
    vectorDisplacement0 = vectorDisplacement.vectorDisplacement0
    vdis0 = vectorDisplacement0
    vectorDisplacement1 = vectorDisplacement.vectorDisplacement1
    vdis1 = vectorDisplacement1
    vectorDisplacement2 = vectorDisplacement.vectorDisplacement2
    vdis2 = vectorDisplacement2

    coordsys = CoordsysEnumField(default_value=1)
    cds = coordsys

    scale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    scl = scale

    base = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    bs = base

    offset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    os = offset

    bump = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    bp = bump

    tweak = TypedField()
    t = tweak
