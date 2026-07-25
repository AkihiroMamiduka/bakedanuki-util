# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.extrude import (
    DirectionField,
    PivotField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class _GeneratedExtrude(DG):
    __slots__ = ()

    NODE_TYPE = "extrude"

    profile = DataNurbsCurveField()
    pr = profile

    path = DataNurbsCurveField()
    pt = path

    extrudeType = ExtrudeTypeEnumField(default_value=2)
    et = extrudeType

    fixedPath = BoolField(default_value=False)
    fpt = fixedPath

    useComponentPivot = UseComponentPivotEnumField(default_value=0)
    ucp = useComponentPivot

    useProfileNormal = BoolField(default_value=False)
    upn = useProfileNormal

    direction = DirectionField(default_value=(0.0, 1.0, 0.0))
    d = direction
    directionX = direction.directionX
    dx = directionX
    directionY = direction.directionY
    dy = directionY
    directionZ = direction.directionZ
    dz = directionZ

    length = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    l = length

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    rotation = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ro = rotation

    scale = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    sc = scale

    reverseSurfaceIfPathReversed = BoolField(default_value=False)
    rsp = reverseSurfaceIfPathReversed

    degreeAlongLength = ShortField(default_value=1)
    dl = degreeAlongLength

    subCurveSubSurface = BoolField(default_value=False)
    scs = subCurveSubSurface

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
