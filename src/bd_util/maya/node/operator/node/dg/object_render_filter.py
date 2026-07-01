# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField


class FilterClassEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2


class FilterClassEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2

    NAME_MAP = {
        OTHER: "other",
        BUILTIN: "builtIn",
        USER: "user",
    }


class FilterClassEnumField(
    EnumField[FilterClassEnumAttrOperator, FilterClassEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterClassEnumAttrOperator
    PLUG_CLS = FilterClassEnumPlugOperator


class ObjectRenderFilter(DG):
    __slots__ = ()

    NODE_TYPE = "objectRenderFilter"

    child = BoolField()
    ch = child

    invert = BoolField()
    inv = invert

    inputList = TypedField()
    in_ = inputList

    outputList = TypedField()
    out = outputList

    annotation = DataStringField()
    an = annotation

    category = DataStringArrayField()
    cat = category

    disable = BoolField()
    dis = disable

    filterClass = FilterClassEnumField()
    fcls = filterClass

    shaders = BoolField()
    shad = shaders

    textures = BoolField()
    txtr = textures

    textures2D = BoolField()
    tx2d = textures2D

    textures3D = BoolField()
    tx3d = textures3D

    lights = BoolField()
    lght = lights

    exclusiveLights = BoolField()
    exlt = exclusiveLights

    nonExclusiveLights = BoolField()
    nxlt = nonExclusiveLights

    postProcess = BoolField()
    post = postProcess

    utility = BoolField()
    util = utility

    rendering = BoolField()
    ren = rendering

    renderableObjectSets = BoolField()
    ros = renderableObjectSets

    lightSets = BoolField()
    ls = lightSets
