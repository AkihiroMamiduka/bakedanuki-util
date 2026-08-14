# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.material_facade import OutColorField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.dt.string import DataStringField


class GeneratedMaterialFacade(DG):
    __slots__ = ()

    NODE_TYPE = "materialFacade"

    sharedLibName = DataStringField()
    sln = sharedLibName

    connection = MessageField()
    c = connection

    uiName = DataStringField()
    uin = uiName

    keyWords = DataStringField()
    kwds = keyWords

    uiScript = DataStringField()
    uis = uiScript

    uniqueID = DataStringField()
    uid = uniqueID

    hardwareProxy = MessageField()
    hp = hardwareProxy

    proxyInitProc = DataStringField()
    pip = proxyInitProc

    outColor = OutColorField(
        default_value=(1.0, 0.6000000238418579, 0.4000000059604645)
    )
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB
