# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2027.ai_shader_to_rgba import (
    InputField,
    OutColorField,
    OutDirectField,
    OutIndirectField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class LightGroupModeEnumPlugOperator(
    EnumPlugOperator["LightGroupModeEnumAttrOperator"]
):
    __slots__ = ()

    INCLUDE = 0
    EXCLUDE = 1


class LightGroupModeEnumAttrOperator(
    EnumAttrOperator[LightGroupModeEnumPlugOperator]
):
    __slots__ = ()

    INCLUDE = 0
    EXCLUDE = 1

    NAME_MAP = {
        INCLUDE: "include",
        EXCLUDE: "exclude",
    }


class LightGroupModeEnumField(
    EnumField[LightGroupModeEnumAttrOperator, LightGroupModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightGroupModeEnumAttrOperator
    PLUG_CLS = LightGroupModeEnumPlugOperator


class GeneratedAiShaderToRgba(DG):
    __slots__ = ()

    NODE_TYPE = "aiShaderToRgba"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outDirect = OutDirectField(default_value=(0.0, 0.0, 0.0), writable=False)
    out_direct = outDirect
    outDirectR = outDirect.outDirectR
    out_directr = outDirectR
    outDirectG = outDirect.outDirectG
    out_directg = outDirectG
    outDirectB = outDirect.outDirectB
    out_directb = outDirectB

    outIndirect = OutIndirectField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    out_indirect = outIndirect
    outIndirectR = outIndirect.outIndirectR
    out_indirectr = outIndirectR
    outIndirectG = outIndirect.outIndirectG
    out_indirectg = outIndirectG
    outIndirectB = outIndirect.outIndirectB
    out_indirectb = outIndirectB

    inputA = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    inputa = inputA

    input = InputField(default_value=(0.0, 0.0, 0.0))
    inputR = input.inputR
    inputr = inputR
    inputG = input.inputG
    inputg = inputG
    inputB = input.inputB
    inputb = inputB

    lightGroupMode = LightGroupModeEnumField(default_value=0)
    light_group_mode = lightGroupMode

    lightGroup = DataStringField()
    light_group = lightGroup
