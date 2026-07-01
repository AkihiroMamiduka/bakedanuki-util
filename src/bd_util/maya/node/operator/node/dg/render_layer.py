# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.render_layer import (
    AdjustmentsField,
    OutAdjustmentsField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
    RenderInfoField,
    RenderPassInfoField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class RenderLayer(DG):
    __slots__ = ()

    NODE_TYPE = "renderLayer"

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    outSize = OutSizeField()
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField()
    fha = fileHasAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    global_ = BoolField(long_name="global", short_name="g")
    g = global_

    renderInfo = RenderInfoField()
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    renderable = renderInfo.renderable
    rndr = renderable
    drawColor = renderInfo.drawColor
    c = drawColor

    layerParent = ShortField()
    rlp = layerParent

    layerChildren = ShortField(multi=True)
    rlc = layerChildren

    renderPassInfo = RenderPassInfoField()
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

    renderPass = MessageField()
    rps = renderPass

    passContributionMap = MessageField()
    pcm = passContributionMap

    imageRendered = BoolField()
    ird = imageRendered

    recycleImage = BoolField()
    rci = recycleImage

    imageName = DataStringField()
    img = imageName

    displayOrder = ShortField()
    do = displayOrder

    psdBlendMode = ShortField()
    bm = psdBlendMode

    psdAlphaChannel = ShortField()
    ac = psdAlphaChannel

    precompTemplate = DataStringField()
    tpc = precompTemplate

    isDefaultPrecompTemplateOverride = BoolField()
    idpo = isDefaultPrecompTemplateOverride
