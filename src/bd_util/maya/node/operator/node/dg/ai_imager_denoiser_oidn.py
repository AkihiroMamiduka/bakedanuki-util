# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class RenderDeviceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    CPU = 1
    GPU = 2


class RenderDeviceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    CPU = 1
    GPU = 2

    NAME_MAP = {
        AUTO: "auto",
        CPU: "cpu",
        GPU: "gpu",
    }


class RenderDeviceEnumField(
    EnumField[RenderDeviceEnumAttrOperator, RenderDeviceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderDeviceEnumAttrOperator
    PLUG_CLS = RenderDeviceEnumPlugOperator


class AiImagerDenoiserOidn(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerDenoiserOidn"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    outputSuffix = DataStringField()
    output_suffix = outputSuffix

    albedo = DataStringField()

    renderDevice = RenderDeviceEnumField(default_value=0)
    render_device = renderDevice
