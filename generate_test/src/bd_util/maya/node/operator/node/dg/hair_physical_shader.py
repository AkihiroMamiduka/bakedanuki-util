# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hair_physical_shader import (
    AmbientColorField,
    ColorDField,
    ColorGField,
    ColorRField,
    ColorTRTField,
    ColorTTField,
    IncandescenceField,
    OutColorField,
    RootColorDField,
    TipColorDField,
    TransparencyField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class HairPhysicalShader(DG):
    __slots__ = ()

    NODE_TYPE = "hairPhysicalShader"

    rootColorD = RootColorDField()
    rcD = rootColorD
    rootColorDR = rootColorD.rootColorDR
    rcDr = rootColorDR
    rootColorDG = rootColorD.rootColorDG
    rcDg = rootColorDG
    rootColorDB = rootColorD.rootColorDB
    rcDb = rootColorDB

    tipColorD = TipColorDField()
    tcD = tipColorD
    tipColorDR = tipColorD.tipColorDR
    tcDr = tipColorDR
    tipColorDG = tipColorD.tipColorDG
    tcDg = tipColorDG
    tipColorDB = tipColorD.tipColorDB
    tcDb = tipColorDB

    intensityD = FloatField()
    iD = intensityD

    transparency = TransparencyField()
    trans = transparency
    transparencyR = transparency.transparencyR
    transr = transparencyR
    transparencyG = transparency.transparencyG
    transg = transparencyG
    transparencyB = transparency.transparencyB
    transb = transparencyB

    ambientColor = AmbientColorField()
    ac = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField()
    incand = incandescence
    incandescenceR = incandescence.incandescenceR
    incandr = incandescenceR
    incandescenceG = incandescence.incandescenceG
    incandg = incandescenceG
    incandescenceB = incandescence.incandescenceB
    incandb = incandescenceB

    colorR = ColorRField()
    cR = colorR
    colorRR = colorR.colorRR
    cRr = colorRR
    colorRG = colorR.colorRG
    cRg = colorRG
    colorRB = colorR.colorRB
    cRb = colorRB

    intensityR = FloatField()
    iR = intensityR

    longitudinalShiftR = FloatField()
    lsR = longitudinalShiftR

    longitudinalWidthR = FloatField()
    lwR = longitudinalWidthR

    colorTT = ColorTTField()
    cTT = colorTT
    colorTTR = colorTT.colorTTR
    cTTr = colorTTR
    colorTTG = colorTT.colorTTG
    cTTg = colorTTG
    colorTTB = colorTT.colorTTB
    cTTb = colorTTB

    intensityTT = FloatField()
    iTT = intensityTT

    longitudinalShiftTT = FloatField()
    lsTT = longitudinalShiftTT

    longitudinalWidthTT = FloatField()
    lwTT = longitudinalWidthTT

    azimuthalWidthTT = FloatField()
    awTT = azimuthalWidthTT

    colorTRT = ColorTRTField()
    cTRT = colorTRT
    colorTRTR = colorTRT.colorTRTR
    cTRTr = colorTRTR
    colorTRTG = colorTRT.colorTRTG
    cTRTg = colorTRTG
    colorTRTB = colorTRT.colorTRTB
    cTRTb = colorTRTB

    intensityTRT = FloatField()
    iTRT = intensityTRT

    longitudinalShiftTRT = FloatField()
    lsTRT = longitudinalShiftTRT

    longitudinalWidthTRT = FloatField()
    lwTRT = longitudinalWidthTRT

    colorG = ColorGField()
    cG = colorG
    colorGR = colorG.colorGR
    cGr = colorGR
    colorGG = colorG.colorGG
    cGg = colorGG
    colorGB = colorG.colorGB
    cGb = colorGB

    intensityG = FloatField()
    iG = intensityG

    azimuthalShiftG = FloatField()
    asG = azimuthalShiftG

    azimuthalWidthG = FloatField()
    awG = azimuthalWidthG

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    colorD = ColorDField()
    cD = colorD
    colorDR = colorD.colorDR
    cDr = colorDR
    colorDG = colorD.colorDG
    cDg = colorDG
    colorDB = colorD.colorDB
    cDb = colorDB

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiKdInd = FloatField()
    ai_kd_ind = aiKdInd
