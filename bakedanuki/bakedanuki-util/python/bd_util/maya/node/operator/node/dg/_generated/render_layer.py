# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.render_layer import (
    AdjustmentsField,
    OutAdjustmentsField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
    RenderInfoField,
    RenderPassInfoField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class GeneratedRenderLayer(DG):
    __slots__ = ()

    NODE_TYPE = "renderLayer"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    outSize = OutSizeField(default_value=(0.0, 0.0), writable=False)
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField(default_value=False, writable=False)
    fha = fileHasAlpha

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    global_ = BoolField(
        default_value=False, long_name="global", short_name="g"
    )
    g = global_

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    renderable = renderInfo.renderable
    rndr = renderable
    drawColor = renderInfo.drawColor
    c = drawColor

    layerParent = ShortField(default_value=0)
    rlp = layerParent

    layerChildren = ShortField(multi=True, default_value=0, readable=False)
    rlc = layerChildren

    renderPassInfo = RenderPassInfoField(
        default_value=(1.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
    )
    rp = renderPassInfo
    beauty = renderPassInfo.beauty
    b = beauty
    color = renderPassInfo.color
    cp = color
    ambient = renderPassInfo.ambient
    am = ambient
    diffuse = renderPassInfo.diffuse
    di = diffuse
    specular = renderPassInfo.specular
    sp = specular
    shadow = renderPassInfo.shadow
    s = shadow

    adjustments = AdjustmentsField(multi=True)
    adjs = adjustments

    outAdjustments = OutAdjustmentsField(multi=True)
    oajs = outAdjustments

    deferredOutAdjustments = TypedField()
    doa = deferredOutAdjustments

    deferredUndoOutAdjustments = TypedField()
    duoa = deferredUndoOutAdjustments

    shadingGroupOverride = MessageField()
    sgo = shadingGroupOverride

    attributeOverrideScript = DataStringField()
    aos = attributeOverrideScript

    renderPass = MessageField(writable=False)
    rps = renderPass

    passContributionMap = MessageField(writable=False)
    pcm = passContributionMap

    imageRendered = BoolField(default_value=False)
    ird = imageRendered

    recycleImage = BoolField(default_value=False)
    rci = recycleImage

    imageName = DataStringField()
    img = imageName

    displayOrder = ShortField(default_value=0)
    do = displayOrder

    psdBlendMode = ShortField(default_value=0)
    bm = psdBlendMode

    psdAlphaChannel = ShortField(default_value=0)
    ac = psdAlphaChannel

    precompTemplate = DataStringField()
    tpc = precompTemplate

    isDefaultPrecompTemplateOverride = BoolField(default_value=True)
    idpo = isDefaultPrecompTemplateOverride
