# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_triplanar import (
    InputField,
    InputYField,
    InputZField,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    RotateField,
    ScaleField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class CoordSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2


class CoordSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 0
    OBJECT = 1
    PREF = 2

    NAME_MAP = {
        WORLD: "world",
        OBJECT: "object",
        PREF: "Pref",
    }


class CoordSpaceEnumField(
    EnumField[CoordSpaceEnumAttrOperator, CoordSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CoordSpaceEnumAttrOperator
    PLUG_CLS = CoordSpaceEnumPlugOperator


class AiTriplanar(DG):
    __slots__ = ()

    NODE_TYPE = "aiTriplanar"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField()
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    inputY = InputYField()
    input_Y = inputY
    inputYR = inputY.inputYR
    input_Yr = inputYR
    inputYG = inputY.inputYG
    input_Yg = inputYG
    inputYB = inputY.inputYB
    input_Yb = inputYB

    inputZ = InputZField()
    input_Z = inputZ
    inputZR = inputZ.inputZR
    input_Zr = inputZR
    inputZG = inputZ.inputZG
    input_Zg = inputZG
    inputZB = inputZ.inputZB
    input_Zb = inputZB

    scale = ScaleField()
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    rotate = RotateField()
    rotateX = rotate.rotateX
    rotatex = rotateX
    rotateY = rotate.rotateY
    rotatey = rotateY
    rotateZ = rotate.rotateZ
    rotatez = rotateZ

    offset = OffsetField()
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY
    offsetZ = offset.offsetZ
    offsetz = offsetZ

    coordSpace = CoordSpaceEnumField()
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    blend = FloatField()

    cell = BoolField()

    cellRotate = FloatField()
    cell_rotate = cellRotate

    cellBlend = FloatField()
    cell_blend = cellBlend

    inputPerAxis = BoolField()
    input_per_axis = inputPerAxis

    flipOnOppositeDirection = BoolField()
    flip_on_opposite_direction = flipOnOppositeDirection
