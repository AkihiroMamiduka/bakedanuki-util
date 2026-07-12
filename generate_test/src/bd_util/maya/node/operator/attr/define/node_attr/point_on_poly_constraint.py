# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.mesh import DataMeshField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2 import Double2Field
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetMesh", "tm"),
        ("targetUVSetName", "tnm"),
        ("targetUV", "tuv"),
        ("targetUseNormal", "tun"),
        ("targetWeight", "tw"),
    )

    targetMesh = DataMeshField()
    tm = targetMesh

    targetUVSetName = DataStringField()
    tnm = targetUVSetName

    targetUV = Double2Field(default_value=(0.0, 0.0))
    tuv = targetUV

    targetUseNormal = BoolField(default_value=True)
    tun = targetUseNormal

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetMesh = DataMeshField()
    tm = targetMesh

    targetUVSetName = DataStringField()
    tnm = targetUVSetName

    targetUV = Double2Field(default_value=(0.0, 0.0))
    tuv = targetUV

    targetUseNormal = BoolField(default_value=True)
    tun = targetUseNormal

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class ConstraintRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotatePivotX", "crpx"),
        ("constraintRotatePivotY", "crpy"),
        ("constraintRotatePivotZ", "crpz"),
    )

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotField(
    DoubleLinear3CompoundBaseField[ConstraintRotatePivotAttrOperator, ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotatePivotAttrOperator
    PLUG_CLS = ConstraintRotatePivotPlugOperator

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotateTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateTranslateX", "crtx"),
        ("constraintRotateTranslateY", "crty"),
        ("constraintRotateTranslateZ", "crtz"),
    )

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintRotateTranslateAttrOperator, ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateTranslateAttrOperator
    PLUG_CLS = ConstraintRotateTranslatePlugOperator

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class OffsetTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OffsetTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetTranslateX", "otx"),
        ("offsetTranslateY", "oty"),
        ("offsetTranslateZ", "otz"),
    )

    offsetTranslateX = DoubleLinearField(default_value=0.0)
    otx = offsetTranslateX

    offsetTranslateY = DoubleLinearField(default_value=0.0)
    oty = offsetTranslateY

    offsetTranslateZ = DoubleLinearField(default_value=0.0)
    otz = offsetTranslateZ


class OffsetTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetTranslatePlugOperator]
):
    __slots__ = ()

    offsetTranslateX = DoubleLinearField(default_value=0.0)
    otx = offsetTranslateX

    offsetTranslateY = DoubleLinearField(default_value=0.0)
    oty = offsetTranslateY

    offsetTranslateZ = DoubleLinearField(default_value=0.0)
    otz = offsetTranslateZ


class OffsetTranslateField(
    DoubleLinear3CompoundBaseField[OffsetTranslateAttrOperator, OffsetTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetTranslateAttrOperator
    PLUG_CLS = OffsetTranslatePlugOperator

    offsetTranslateX = DoubleLinearField(default_value=0.0)
    otx = offsetTranslateX

    offsetTranslateY = DoubleLinearField(default_value=0.0)
    oty = offsetTranslateY

    offsetTranslateZ = DoubleLinearField(default_value=0.0)
    otz = offsetTranslateZ


class OffsetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OffsetRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetRotateX", "orx"),
        ("offsetRotateY", "ory"),
        ("offsetRotateZ", "orz"),
    )

    offsetRotateX = DoubleAngleField(default_value=0.0)
    orx = offsetRotateX

    offsetRotateY = DoubleAngleField(default_value=0.0)
    ory = offsetRotateY

    offsetRotateZ = DoubleAngleField(default_value=0.0)
    orz = offsetRotateZ


class OffsetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OffsetRotatePlugOperator]
):
    __slots__ = ()

    offsetRotateX = DoubleAngleField(default_value=0.0)
    orx = offsetRotateX

    offsetRotateY = DoubleAngleField(default_value=0.0)
    ory = offsetRotateY

    offsetRotateZ = DoubleAngleField(default_value=0.0)
    orz = offsetRotateZ


class OffsetRotateField(
    DoubleAngle3CompoundBaseField[OffsetRotateAttrOperator, OffsetRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetRotateAttrOperator
    PLUG_CLS = OffsetRotatePlugOperator

    offsetRotateX = DoubleAngleField(default_value=0.0)
    orx = offsetRotateX

    offsetRotateY = DoubleAngleField(default_value=0.0)
    ory = offsetRotateY

    offsetRotateZ = DoubleAngleField(default_value=0.0)
    orz = offsetRotateZ


class ConstraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslateX", "ctx"),
        ("constraintTranslateY", "cty"),
        ("constraintTranslateZ", "ctz"),
    )

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTranslateAttrOperator
    PLUG_CLS = ConstraintTranslatePlugOperator

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateX", "crx"),
        ("constraintRotateY", "cry"),
        ("constraintRotateZ", "crz"),
    )

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintRotatePlugOperator]
):
    __slots__ = ()

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateField(
    DoubleAngle3CompoundBaseField[ConstraintRotateAttrOperator, ConstraintRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateAttrOperator
    PLUG_CLS = ConstraintRotatePlugOperator

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class RestTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RestTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restTranslateX", "rtx"),
        ("restTranslateY", "rty"),
        ("restTranslateZ", "rtz"),
    )

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RestTranslatePlugOperator]
):
    __slots__ = ()

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateField(
    DoubleLinear3CompoundBaseField[RestTranslateAttrOperator, RestTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestTranslateAttrOperator
    PLUG_CLS = RestTranslatePlugOperator

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RestRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restRotateX", "rrx"),
        ("restRotateY", "rry"),
        ("restRotateZ", "rrz"),
    )

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RestRotatePlugOperator]
):
    __slots__ = ()

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateField(
    DoubleAngle3CompoundBaseField[RestRotateAttrOperator, RestRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestRotateAttrOperator
    PLUG_CLS = RestRotatePlugOperator

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ
