# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_complex_ior import (
    EdgetintField,
    KField,
    NField,
    OutColorField,
    OutTransparencyField,
    ReflectivityField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class MaterialEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CUSTOM = 0
    ALUMINIUM = 1
    COPPER = 2
    GOLD = 3
    IRON = 4
    LEAD = 5
    MAGNESIUM = 6
    MERCURY = 7
    NICKEL = 8
    PLATINUM = 9
    SILVER = 10
    SODIUM = 11


class MaterialEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CUSTOM = 0
    ALUMINIUM = 1
    COPPER = 2
    GOLD = 3
    IRON = 4
    LEAD = 5
    MAGNESIUM = 6
    MERCURY = 7
    NICKEL = 8
    PLATINUM = 9
    SILVER = 10
    SODIUM = 11

    NAME_MAP = {
        CUSTOM: "custom",
        ALUMINIUM: "aluminium",
        COPPER: "copper",
        GOLD: "gold",
        IRON: "iron",
        LEAD: "lead",
        MAGNESIUM: "magnesium",
        MERCURY: "mercury",
        NICKEL: "nickel",
        PLATINUM: "platinum",
        SILVER: "silver",
        SODIUM: "sodium",
    }


class MaterialEnumField(
    EnumField[MaterialEnumAttrOperator, MaterialEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaterialEnumAttrOperator
    PLUG_CLS = MaterialEnumPlugOperator


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ARTISTIC = 0
    PHYSICAL = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ARTISTIC = 0
    PHYSICAL = 1

    NAME_MAP = {
        ARTISTIC: "artistic",
        PHYSICAL: "physical",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class _GeneratedAiComplexIor(DG):
    __slots__ = ()

    NODE_TYPE = "aiComplexIor"

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

    material = MaterialEnumField(default_value=0)

    mode = ModeEnumField(default_value=0)

    reflectivity = ReflectivityField(default_value=(0.9259520173072815, 0.7208870053291321, 0.5041540265083313))
    reflectivityR = reflectivity.reflectivityR
    reflectivityr = reflectivityR
    reflectivityG = reflectivity.reflectivityG
    reflectivityg = reflectivityG
    reflectivityB = reflectivity.reflectivityB
    reflectivityb = reflectivityB

    edgetint = EdgetintField(default_value=(0.995523989200592, 0.957414984703064, 0.8227760195732117))
    edgetintR = edgetint.edgetintR
    edgetintr = edgetintR
    edgetintG = edgetint.edgetintG
    edgetintg = edgetintG
    edgetintB = edgetint.edgetintB
    edgetintb = edgetintB

    n = NField(default_value=(0.27105000615119934, 0.6769300103187561, 1.3164000511169434))
    nX = n.nX
    nx = nX
    nY = n.nY
    ny = nY
    nZ = n.nZ
    nz = nZ

    k = KField(default_value=(3.6092000007629395, 2.6247000694274902, 2.292099952697754))
    kX = k.kX
    kx = kX
    kY = k.kY
    ky = kY
    kZ = k.kZ
    kz = kZ
