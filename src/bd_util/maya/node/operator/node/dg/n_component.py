# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.double_array import DataDoubleArrayField
from ...attr.define.std.dt.mesh import DataMeshField


class ComponentTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    POINT = 2
    EDGE = 3
    FACE = 4
    OBJECT = 6


class ComponentTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    POINT = 2
    EDGE = 3
    FACE = 4
    OBJECT = 6

    NAME_MAP = {
        NONE: "None",
        POINT: "Point",
        EDGE: "Edge",
        FACE: "Face",
        OBJECT: "Object",
    }


class ComponentTypeEnumField(
    EnumField[ComponentTypeEnumAttrOperator, ComponentTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComponentTypeEnumAttrOperator
    PLUG_CLS = ComponentTypeEnumPlugOperator


class ElementsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FROM_INDICE_LIST = 0
    BORDERS = 1
    ALL = 2


class ElementsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FROM_INDICE_LIST = 0
    BORDERS = 1
    ALL = 2

    NAME_MAP = {
        FROM_INDICE_LIST: "From Indice List",
        BORDERS: "Borders",
        ALL: "All",
    }


class ElementsEnumField(
    EnumField[ElementsEnumAttrOperator, ElementsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ElementsEnumAttrOperator
    PLUG_CLS = ElementsEnumPlugOperator


class StrengthMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class StrengthMapTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class StrengthMapTypeEnumField(
    EnumField[StrengthMapTypeEnumAttrOperator, StrengthMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StrengthMapTypeEnumAttrOperator
    PLUG_CLS = StrengthMapTypeEnumPlugOperator


class GlueStrengthMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class GlueStrengthMapTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class GlueStrengthMapTypeEnumField(
    EnumField[GlueStrengthMapTypeEnumAttrOperator, GlueStrengthMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GlueStrengthMapTypeEnumAttrOperator
    PLUG_CLS = GlueStrengthMapTypeEnumPlugOperator


class WeightMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class WeightMapTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class WeightMapTypeEnumField(
    EnumField[WeightMapTypeEnumAttrOperator, WeightMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightMapTypeEnumAttrOperator
    PLUG_CLS = WeightMapTypeEnumPlugOperator


class NComponent(DG):
    __slots__ = ()

    NODE_TYPE = "nComponent"

    surface = DataMeshField()
    srf = surface

    componentGroupId = LongField()
    cid = componentGroupId

    componentType = ComponentTypeEnumField()
    ct = componentType

    elements = ElementsEnumField()
    el = elements

    strength = DoubleField()
    stn = strength

    strengthMap = FloatField()
    stnm = strengthMap

    strengthPerVertex = DataDoubleArrayField()
    spv = strengthPerVertex

    glueStrength = DoubleField()
    gst = glueStrength

    glueStrengthMap = FloatField()
    gstm = glueStrengthMap

    glueStrengthPerVertex = DataDoubleArrayField()
    gspv = glueStrengthPerVertex

    weight = DoubleField()
    wgh = weight

    weightMap = FloatField()
    wemp = weightMap

    weightPerVertex = DataDoubleArrayField()
    wpv = weightPerVertex

    tangentStrength = DoubleField()
    tst = tangentStrength

    objectId = GenericField()
    obid = objectId

    componentIndices = LongField(multi=True)
    ci = componentIndices

    outComponent = TypedField()
    ocp = outComponent

    strengthMapType = StrengthMapTypeEnumField()
    smt = strengthMapType

    glueStrengthMapType = GlueStrengthMapTypeEnumField()
    gsmt = glueStrengthMapType

    weightMapType = WeightMapTypeEnumField()
    wmt = weightMapType
