# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class BlendFuncEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALPHABLEND = 0
    MULTIPLYRGB = 1
    ADD = 2
    SUBTRACT = 3
    LINEARBLEND = 4
    BILINEARBLEND = 5
    COLORCHANNEL = 6
    MULTIPLYRGBA = 7


class BlendFuncEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALPHABLEND = 0
    MULTIPLYRGB = 1
    ADD = 2
    SUBTRACT = 3
    LINEARBLEND = 4
    BILINEARBLEND = 5
    COLORCHANNEL = 6
    MULTIPLYRGBA = 7

    NAME_MAP = {
        ALPHABLEND: "AlphaBlend",
        MULTIPLYRGB: "MultiplyRGB",
        ADD: "Add",
        SUBTRACT: "Subtract",
        LINEARBLEND: "LinearBlend",
        BILINEARBLEND: "BilinearBlend",
        COLORCHANNEL: "ColorChannel",
        MULTIPLYRGBA: "MultiplyRGBA",
    }


class BlendFuncEnumField(
    EnumField[BlendFuncEnumAttrOperator, BlendFuncEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendFuncEnumAttrOperator
    PLUG_CLS = BlendFuncEnumPlugOperator


class BlendColorSets(DG):
    __slots__ = ()

    NODE_TYPE = "blendColorSets"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    baseColorName = DataStringField()
    bcn = baseColorName

    srcColorName = DataStringField()
    src = srcColorName

    dstColorName = DataStringField()
    dst = dstColorName

    blendFunc = BlendFuncEnumField()
    bfn = blendFunc

    blendWeightA = FloatField()
    bwa = blendWeightA

    blendWeightB = FloatField()
    bwb = blendWeightB

    blendWeightC = FloatField()
    bwc = blendWeightC

    blendWeightD = FloatField()
    bwd = blendWeightD
