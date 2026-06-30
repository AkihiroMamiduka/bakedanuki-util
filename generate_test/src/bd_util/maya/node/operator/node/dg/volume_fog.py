# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.volume_fog import (
    ColorField,
    ColorRampField,
    FarPointObjField,
    FarPointWorldField,
    IncandescenceField,
    LightDataArrayField,
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    PointObjField,
    PointWorldField,
    RayDirectionField,
    TransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorRampInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    IGNORE = 0
    TRANSPARENCY = 1
    CONCENTRIC = 2
    Y_GRADIENT = 3


class ColorRampInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    IGNORE = 0
    TRANSPARENCY = 1
    CONCENTRIC = 2
    Y_GRADIENT = 3

    NAME_MAP = {
        IGNORE: "Ignore",
        TRANSPARENCY: "Transparency",
        CONCENTRIC: "Concentric",
        Y_GRADIENT: "Y Gradient",
    }


class ColorRampInputEnumField(
    EnumField[ColorRampInputEnumAttrOperator, ColorRampInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRampInputEnumAttrOperator
    PLUG_CLS = ColorRampInputEnumPlugOperator


class DensityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLDSPACE = 0
    OBJECTSPACE = 1


class DensityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLDSPACE = 0
    OBJECTSPACE = 1

    NAME_MAP = {
        WORLDSPACE: "WorldSpace",
        OBJECTSPACE: "ObjectSpace",
    }


class DensityModeEnumField(
    EnumField[DensityModeEnumAttrOperator, DensityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DensityModeEnumAttrOperator
    PLUG_CLS = DensityModeEnumPlugOperator


class DropoffShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    SPHERE = 1
    CUBE = 2
    CONE = 3
    LIGHTCONE = 4


class DropoffShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    SPHERE = 1
    CUBE = 2
    CONE = 3
    LIGHTCONE = 4

    NAME_MAP = {
        OFF: "Off",
        SPHERE: "Sphere",
        CUBE: "Cube",
        CONE: "Cone",
        LIGHTCONE: "LightCone",
    }


class DropoffShapeEnumField(
    EnumField[DropoffShapeEnumAttrOperator, DropoffShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DropoffShapeEnumAttrOperator
    PLUG_CLS = DropoffShapeEnumPlugOperator


class DropoffMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCALE_OPACITY = 0
    SUBTRACT_DENSITY = 1


class DropoffMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SCALE_OPACITY = 0
    SUBTRACT_DENSITY = 1

    NAME_MAP = {
        SCALE_OPACITY: "Scale Opacity",
        SUBTRACT_DENSITY: "Subtract Density",
    }


class DropoffMethodEnumField(
    EnumField[DropoffMethodEnumAttrOperator, DropoffMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DropoffMethodEnumAttrOperator
    PLUG_CLS = DropoffMethodEnumPlugOperator


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2

    NAME_MAP = {
        BLACK_HOLE: "Black Hole",
        SOLID_MATTE: "Solid Matte",
        OPACITY_GAIN: "Opacity Gain",
    }


class MatteOpacityModeEnumField(
    EnumField[MatteOpacityModeEnumAttrOperator, MatteOpacityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatteOpacityModeEnumAttrOperator
    PLUG_CLS = MatteOpacityModeEnumPlugOperator


class VolumeFog(DG):
    __slots__ = ()

    NODE_TYPE = "volumeFog"

    rayDirection = RayDirectionField()
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    pointWorld = PointWorldField()
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    farPointWorld = FarPointWorldField()
    fw = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fwx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fwy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fwz = farPointWorldZ

    pointObj = PointObjField()
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    farPointObj = FarPointObjField()
    fo = farPointObj
    farPointObjectX = farPointObj.farPointObjectX
    fox = farPointObjectX
    farPointObjectY = farPointObj.farPointObjectY
    foy = farPointObjectY
    farPointObjectZ = farPointObj.farPointObjectZ
    foz = farPointObjectZ

    matrixWorldToEye = FltMatrixField()
    wte = matrixWorldToEye

    lightDataArray = LightDataArrayField(multi=True)
    ltd = lightDataArray

    # TODO: lightDataArray.lightDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    color = ColorField()
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    colorRampInput = ColorRampInputEnumField()
    cri = colorRampInput

    colorRamp = ColorRampField(multi=True)
    crm = colorRamp

    # TODO: colorRamp.colorRamp_ColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: colorRamp.colorRamp_ColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: colorRamp.colorRamp_ColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    transparency = TransparencyField()
    t = transparency
    transparencyR = transparency.transparencyR
    tr = transparencyR
    transparencyG = transparency.transparencyG
    tg = transparencyG
    transparencyB = transparency.transparencyB
    tb = transparencyB

    incandescence = IncandescenceField()
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    glowIntensity = FloatField()
    gi = glowIntensity

    outGlowColor = OutGlowColorField()
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    density = FloatField()
    dns = density

    densityMode = DensityModeEnumField()
    dmd = densityMode

    dropoffShape = DropoffShapeEnumField()
    dos = dropoffShape

    edgeDropoff = FloatField()
    edr = edgeDropoff

    axialDropoff = FloatField()
    axd = axialDropoff

    dropoffMethod = DropoffMethodEnumField()
    drm = dropoffMethod

    dropoffSubtract = FloatField()
    drs = dropoffSubtract

    illuminated = BoolField()
    il = illuminated

    lightScatter = FloatField()
    lsc = lightScatter

    matteOpacityMode = MatteOpacityModeEnumField()
    mom = matteOpacityMode

    matteOpacity = FloatField()
    mog = matteOpacity

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outMatteOpacity = OutMatteOpacityField()
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
