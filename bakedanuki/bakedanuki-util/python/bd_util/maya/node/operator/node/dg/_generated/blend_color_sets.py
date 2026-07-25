# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedBlendColorSets(DG):
    __slots__ = ()

    NODE_TYPE = "blendColorSets"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    baseColorName = DataStringField()
    bcn = baseColorName

    srcColorName = DataStringField()
    src = srcColorName

    dstColorName = DataStringField()
    dst = dstColorName

    blendFunc = BlendFuncEnumField(default_value=0)
    bfn = blendFunc

    blendWeightA = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    bwa = blendWeightA

    blendWeightB = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    bwb = blendWeightB

    blendWeightC = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    bwc = blendWeightC

    blendWeightD = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    bwd = blendWeightD
