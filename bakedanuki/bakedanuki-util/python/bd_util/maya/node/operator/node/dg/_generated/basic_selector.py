# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class TypeFilterEnumPlugOperator(EnumPlugOperator["TypeFilterEnumAttrOperator"]):
    __slots__ = ()

    ALL = 0
    TRANSFORMS = 1
    SHAPES = 2
    SHADERS = 3
    LIGHTS = 4
    SETS = 5
    CUSTOM = 8
    GEOMETRY_GENERATORS = 10
    SHADING_ENGINES = 11
    LIGHTS_AND_TRANSFORMS = 12


class TypeFilterEnumAttrOperator(EnumAttrOperator[TypeFilterEnumPlugOperator]):
    __slots__ = ()

    ALL = 0
    TRANSFORMS = 1
    SHAPES = 2
    SHADERS = 3
    LIGHTS = 4
    SETS = 5
    CUSTOM = 8
    GEOMETRY_GENERATORS = 10
    SHADING_ENGINES = 11
    LIGHTS_AND_TRANSFORMS = 12

    NAME_MAP = {
        ALL: "All",
        TRANSFORMS: "Transforms",
        SHAPES: "Shapes",
        SHADERS: "Shaders",
        LIGHTS: "Lights",
        SETS: "Sets",
        CUSTOM: "Custom",
        GEOMETRY_GENERATORS: "Geometry Generators",
        SHADING_ENGINES: "Shading engines",
        LIGHTS_AND_TRANSFORMS: "Lights and Transforms",
    }


class TypeFilterEnumField(
    EnumField[TypeFilterEnumAttrOperator, TypeFilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeFilterEnumAttrOperator
    PLUG_CLS = TypeFilterEnumPlugOperator


class GeneratedBasicSelector(DG):
    __slots__ = ()

    NODE_TYPE = "basicSelector"

    input = LongField(default_value=0)
    in_ = input

    output = LongField(default_value=0)
    out = output

    collection = MessageField(writable=False)
    c = collection

    pattern = DataStringField()
    pat = pattern

    previousPattern = DataStringField()
    ppa = previousPattern

    staticSelection = DataStringField()
    ssl = staticSelection

    typeFilter = TypeFilterEnumField(default_value=1)
    tf = typeFilter

    customFilterValue = DataStringField()
    cfv = customFilterValue

    includeHierarchy = BoolField(default_value=True)
    ih = includeHierarchy
