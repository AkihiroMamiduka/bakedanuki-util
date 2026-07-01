# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.extrude import (
    DirectionField,
    PivotField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class ExtrudeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISTANCE = 0
    FLAT = 1
    TUBE = 2


class ExtrudeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISTANCE = 0
    FLAT = 1
    TUBE = 2

    NAME_MAP = {
        DISTANCE: "Distance",
        FLAT: "Flat",
        TUBE: "Tube",
    }


class ExtrudeTypeEnumField(
    EnumField[ExtrudeTypeEnumAttrOperator, ExtrudeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtrudeTypeEnumAttrOperator
    PLUG_CLS = ExtrudeTypeEnumPlugOperator


class UseComponentPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST_ENDPOINT_OF_THE_PATH = 0
    COMPONENT_PIVOT = 1
    CENTER_OF_THE_BOUNDING_BOX_OF_THE_PROFILE = 2


class UseComponentPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST_ENDPOINT_OF_THE_PATH = 0
    COMPONENT_PIVOT = 1
    CENTER_OF_THE_BOUNDING_BOX_OF_THE_PROFILE = 2

    NAME_MAP = {
        CLOSEST_ENDPOINT_OF_THE_PATH: "Closest Endpoint of the Path",
        COMPONENT_PIVOT: "Component Pivot",
        CENTER_OF_THE_BOUNDING_BOX_OF_THE_PROFILE: "Center of the Bounding Box of the Profile",
    }


class UseComponentPivotEnumField(
    EnumField[UseComponentPivotEnumAttrOperator, UseComponentPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseComponentPivotEnumAttrOperator
    PLUG_CLS = UseComponentPivotEnumPlugOperator


class Extrude(DG):
    __slots__ = ()

    NODE_TYPE = "extrude"

    profile = DataNurbsCurveField()
    pr = profile

    path = DataNurbsCurveField()
    pt = path

    extrudeType = ExtrudeTypeEnumField()
    et = extrudeType

    fixedPath = BoolField()
    fpt = fixedPath

    useComponentPivot = UseComponentPivotEnumField()
    ucp = useComponentPivot

    useProfileNormal = BoolField()
    upn = useProfileNormal

    direction = DirectionField()
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    length = DoubleLinearField()
    l = length

    pivot = PivotField()
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    rotation = DoubleAngleField()
    ro = rotation

    scale = DoubleField()
    sc = scale

    reverseSurfaceIfPathReversed = BoolField()
    rsp = reverseSurfaceIfPathReversed

    degreeAlongLength = ShortField()
    dl = degreeAlongLength

    subCurveSubSurface = BoolField()
    scs = subCurveSubSurface

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
