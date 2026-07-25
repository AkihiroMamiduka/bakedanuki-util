# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.volume_fog import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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


class _GeneratedVolumeFog(DG):
    __slots__ = ()

    NODE_TYPE = "volumeFog"

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0))
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    pointWorld = PointWorldField(default_value=(0.0, 0.0, 0.0))
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    farPointWorld = FarPointWorldField(default_value=(1.0, 1.0, 1.0))
    fw = farPointWorld
    farPointWorldX = farPointWorld.farPointWorldX
    fwx = farPointWorldX
    farPointWorldY = farPointWorld.farPointWorldY
    fwy = farPointWorldY
    farPointWorldZ = farPointWorld.farPointWorldZ
    fwz = farPointWorldZ

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    farPointObj = FarPointObjField(default_value=(1.0, 1.0, 1.0))
    fo = farPointObj
    farPointObjectX = farPointObj.farPointObjectX
    fox = farPointObjectX
    farPointObjectY = farPointObj.farPointObjectY
    foy = farPointObjectY
    farPointObjectZ = farPointObj.farPointObjectZ
    foz = farPointObjectZ

    matrixWorldToEye = FltMatrixField(readable=False)
    wte = matrixWorldToEye

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    color = ColorField(default_value=(0.8999999761581421, 0.8999999761581421, 0.8999999761581421))
    cl = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    colorRampInput = ColorRampInputEnumField(default_value=0)
    cri = colorRampInput

    colorRamp = ColorRampField(multi=True)
    crm = colorRamp

    colorRamp_ColorR = FloatField()
    crmcr = colorRamp_ColorR

    colorRamp_ColorG = FloatField()
    crmcg = colorRamp_ColorG

    colorRamp_ColorB = FloatField()
    crmcb = colorRamp_ColorB

    transparency = TransparencyField(default_value=(0.5, 0.5, 0.5))
    t = transparency
    transparencyR = transparency.transparencyR
    tr = transparencyR
    transparencyG = transparency.transparencyG
    tg = transparencyG
    transparencyB = transparency.transparencyB
    tb = transparencyB

    incandescence = IncandescenceField(default_value=(0.0, 0.0, 0.0))
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    density = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    dns = density

    densityMode = DensityModeEnumField(default_value=1)
    dmd = densityMode

    dropoffShape = DropoffShapeEnumField(default_value=0)
    dos = dropoffShape

    edgeDropoff = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    edr = edgeDropoff

    axialDropoff = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    axd = axialDropoff

    dropoffMethod = DropoffMethodEnumField(default_value=0)
    drm = dropoffMethod

    dropoffSubtract = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    drs = dropoffSubtract

    illuminated = BoolField(default_value=False)
    il = illuminated

    lightScatter = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    lsc = lightScatter

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outMatteOpacity = OutMatteOpacityField(default_value=(1.0, 1.0, 1.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
