# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_triplanar import (
    InputField,
    InputYField,
    InputZField,
    OffsetField,
    OutColorField,
    OutTransparencyField,
    RotateField,
    ScaleField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiTriplanar(DG):
    __slots__ = ()

    NODE_TYPE = "aiTriplanar"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input = InputField(default_value=(1.0, 1.0, 1.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    inputY = InputYField(default_value=(1.0, 1.0, 1.0))
    input_Y = inputY
    inputYR = inputY.inputYR
    input_Yr = inputYR
    inputYG = inputY.inputYG
    input_Yg = inputYG
    inputYB = inputY.inputYB
    input_Yb = inputYB

    inputZ = InputZField(default_value=(1.0, 1.0, 1.0))
    input_Z = inputZ
    inputZR = inputZ.inputZR
    input_Zr = inputZR
    inputZG = inputZ.inputZG
    input_Zg = inputZG
    inputZB = inputZ.inputZB
    input_Zb = inputZB

    scale = ScaleField(default_value=(1.0, 1.0, 1.0))
    scaleX = scale.scaleX
    scalex = scaleX
    scaleY = scale.scaleY
    scaley = scaleY
    scaleZ = scale.scaleZ
    scalez = scaleZ

    rotate = RotateField(default_value=(0.0, 0.0, 0.0))
    rotateX = rotate.rotateX
    rotatex = rotateX
    rotateY = rotate.rotateY
    rotatey = rotateY
    rotateZ = rotate.rotateZ
    rotatez = rotateZ

    offset = OffsetField(default_value=(0.0, 0.0, 0.0))
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY
    offsetZ = offset.offsetZ
    offsetz = offsetZ

    coordSpace = CoordSpaceEnumField(default_value=1)
    coord_space = coordSpace

    prefName = DataStringField()
    pref_name = prefName

    blend = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, soft_max_value=1.0)

    cell = BoolField(default_value=False)

    cellRotate = FloatField(default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    cell_rotate = cellRotate

    cellBlend = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    cell_blend = cellBlend

    inputPerAxis = BoolField(default_value=False)
    input_per_axis = inputPerAxis

    flipOnOppositeDirection = BoolField(default_value=True)
    flip_on_opposite_direction = flipOnOppositeDirection
