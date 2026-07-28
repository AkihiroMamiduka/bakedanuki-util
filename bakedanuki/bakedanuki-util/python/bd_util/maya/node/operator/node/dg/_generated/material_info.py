# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.dt.string import DataStringField


class TextureFilterEnumPlugOperator(EnumPlugOperator["TextureFilterEnumAttrOperator"]):
    __slots__ = ()

    GLOBAL_SETTINGS = 1
    NEAREST_UNFILTERED = 2
    BILINEAR = 3
    MIPMAP_NEAREST = 4
    MIPMAP_LINEAR = 5
    MIPMAP_BILINEAR = 6
    MIPMAP_TRILINEAR = 7


class TextureFilterEnumAttrOperator(EnumAttrOperator[TextureFilterEnumPlugOperator]):
    __slots__ = ()

    GLOBAL_SETTINGS = 1
    NEAREST_UNFILTERED = 2
    BILINEAR = 3
    MIPMAP_NEAREST = 4
    MIPMAP_LINEAR = 5
    MIPMAP_BILINEAR = 6
    MIPMAP_TRILINEAR = 7

    NAME_MAP = {
        GLOBAL_SETTINGS: "Global Settings",
        NEAREST_UNFILTERED: "Nearest(Unfiltered)",
        BILINEAR: "Bilinear",
        MIPMAP_NEAREST: "Mipmap Nearest",
        MIPMAP_LINEAR: "Mipmap Linear",
        MIPMAP_BILINEAR: "Mipmap Bilinear",
        MIPMAP_TRILINEAR: "MipMap Trilinear",
    }


class TextureFilterEnumField(
    EnumField[TextureFilterEnumAttrOperator, TextureFilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureFilterEnumAttrOperator
    PLUG_CLS = TextureFilterEnumPlugOperator


class GeneratedMaterialInfo(DG):
    __slots__ = ()

    NODE_TYPE = "materialInfo"

    shadingGroup = MessageField()
    sg = shadingGroup

    material = MessageField()
    m = material

    texture = MessageField(multi=True, readable=False)
    t = texture

    textureName = DataStringField()
    tn = textureName

    textureChannel = MessageField()
    tc = textureChannel

    texturePlug = DataStringField(writable=False)
    tp = texturePlug

    textureFilter = TextureFilterEnumField(default_value=1)
    tmip = textureFilter
