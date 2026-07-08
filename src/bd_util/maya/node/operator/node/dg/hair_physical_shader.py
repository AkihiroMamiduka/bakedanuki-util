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

    rootColorD = RootColorDField(default_value=(0.2070000022649765, 0.1379999965429306, 0.0689999982714653))
    rcD = rootColorD
    rootColorDR = rootColorD.rootColorDR
    rcDr = rootColorDR
    rootColorDG = rootColorD.rootColorDG
    rcDg = rootColorDG
    rootColorDB = rootColorD.rootColorDB
    rcDb = rootColorDB

    tipColorD = TipColorDField(default_value=(0.2070000022649765, 0.1379999965429306, 0.0689999982714653))
    tcD = tipColorD
    tipColorDR = tipColorD.tipColorDR
    tcDr = tipColorDR
    tipColorDG = tipColorD.tipColorDG
    tcDg = tipColorDG
    tipColorDB = tipColorD.tipColorDB
    tcDb = tipColorDB

    intensityD = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    iD = intensityD

    transparency = TransparencyField(default_value=(0.0, 0.0, 0.0))
    trans = transparency
    transparencyR = transparency.transparencyR
    transr = transparencyR
    transparencyG = transparency.transparencyG
    transg = transparencyG
    transparencyB = transparency.transparencyB
    transb = transparencyB

    ambientColor = AmbientColorField(default_value=(0.0, 0.0, 0.0))
    ac = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField(default_value=(0.0, 0.0, 0.0))
    incand = incandescence
    incandescenceR = incandescence.incandescenceR
    incandr = incandescenceR
    incandescenceG = incandescence.incandescenceG
    incandg = incandescenceG
    incandescenceB = incandescence.incandescenceB
    incandb = incandescenceB

    colorR = ColorRField(default_value=(1.0, 1.0, 1.0))
    cR = colorR
    colorRR = colorR.colorRR
    cRr = colorRR
    colorRG = colorR.colorRG
    cRg = colorRG
    colorRB = colorR.colorRB
    cRb = colorRB

    intensityR = FloatField(default_value=0.550000011920929, soft_min_value=0.0, soft_max_value=1.0)
    iR = intensityR

    longitudinalShiftR = FloatField(default_value=3.0, soft_min_value=-10.0, soft_max_value=10.0)
    lsR = longitudinalShiftR

    longitudinalWidthR = FloatField(default_value=3.5, soft_min_value=0.0, soft_max_value=10.0)
    lwR = longitudinalWidthR

    colorTT = ColorTTField(default_value=(1.0, 1.0, 1.0))
    cTT = colorTT
    colorTTR = colorTT.colorTTR
    cTTr = colorTTR
    colorTTG = colorTT.colorTTG
    cTTg = colorTTG
    colorTTB = colorTT.colorTTB
    cTTb = colorTTB

    intensityTT = FloatField(default_value=0.15000000596046448, soft_min_value=0.0, soft_max_value=1.0)
    iTT = intensityTT

    longitudinalShiftTT = FloatField(default_value=3.0, soft_min_value=-10.0, soft_max_value=10.0)
    lsTT = longitudinalShiftTT

    longitudinalWidthTT = FloatField(default_value=10.0, soft_min_value=5.0, soft_max_value=10.0)
    lwTT = longitudinalWidthTT

    azimuthalWidthTT = FloatField(default_value=10.0, soft_min_value=5.0, soft_max_value=15.0)
    awTT = azimuthalWidthTT

    colorTRT = ColorTRTField(default_value=(0.7250000238418579, 0.3179999887943268, 0.11400000005960464))
    cTRT = colorTRT
    colorTRTR = colorTRT.colorTRTR
    cTRTr = colorTRTR
    colorTRTG = colorTRT.colorTRTG
    cTRTg = colorTRTG
    colorTRTB = colorTRT.colorTRTB
    cTRTb = colorTRTB

    intensityTRT = FloatField(default_value=0.15000000596046448, soft_min_value=0.0, soft_max_value=1.0)
    iTRT = intensityTRT

    longitudinalShiftTRT = FloatField(default_value=3.0, soft_min_value=-10.0, soft_max_value=10.0)
    lsTRT = longitudinalShiftTRT

    longitudinalWidthTRT = FloatField(default_value=15.0, soft_min_value=0.0, soft_max_value=20.0)
    lwTRT = longitudinalWidthTRT

    colorG = ColorGField(default_value=(0.7250000238418579, 0.3179999887943268, 0.11400000005960464))
    cG = colorG
    colorGR = colorG.colorGR
    cGr = colorGR
    colorGG = colorG.colorGG
    cGg = colorGG
    colorGB = colorG.colorGB
    cGb = colorGB

    intensityG = FloatField(default_value=0.15000000596046448, soft_min_value=0.0, soft_max_value=1.0)
    iG = intensityG

    azimuthalShiftG = FloatField(default_value=30.0, soft_min_value=25.0, soft_max_value=45.0)
    asG = azimuthalShiftG

    azimuthalWidthG = FloatField(default_value=15.0, soft_min_value=0.0, soft_max_value=25.0)
    awG = azimuthalWidthG

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    colorD = ColorDField(default_value=(0.2070000022649765, 0.1379999965429306, 0.0689999982714653))
    cD = colorD
    colorDR = colorD.colorDR
    cDr = colorDR
    colorDG = colorD.colorDG
    cDg = colorDG
    colorDB = colorD.colorDB
    cDb = colorDB

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiKdInd = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0, category="arnold")
    ai_kd_ind = aiKdInd
