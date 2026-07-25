# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.matrix import MatrixField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


class DriverWrapModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFFSET = 0
    SURFACE = 1
    SNAP = 2
    RIGID = 3
    CLUSTER = 4
    GLOBAL = 100


class DriverWrapModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFFSET = 0
    SURFACE = 1
    SNAP = 2
    RIGID = 3
    CLUSTER = 4
    GLOBAL = 100

    NAME_MAP = {
        OFFSET: "Offset",
        SURFACE: "Surface",
        SNAP: "Snap",
        RIGID: "Rigid",
        CLUSTER: "Cluster",
        GLOBAL: "Global",
    }


class DriverWrapModeEnumField(
    EnumField[DriverWrapModeEnumAttrOperator, DriverWrapModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DriverWrapModeEnumAttrOperator
    PLUG_CLS = DriverWrapModeEnumPlugOperator


class FalloffRamp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FalloffRamp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class FalloffRamp_InterpEnumField(
    EnumField[FalloffRamp_InterpEnumAttrOperator, FalloffRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffRamp_InterpEnumAttrOperator
    PLUG_CLS = FalloffRamp_InterpEnumPlugOperator


class InputPlugOperator(
    CompoundPlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputGeometry", "ig"),
        ("groupId", "gi"),
        ("componentTagExpression", "gtg"),
    )

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(
    CompoundField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelopeWeights", "owt"),
    )

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EnvelopeWeightsListAttrOperator
    PLUG_CLS = EnvelopeWeightsListPlugOperator


class FunctionPlugOperator(
    Long3CompoundBasePlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("fchild1", "f1"),
        ("fchild2", "f2"),
        ("fchild3", "f3"),
    )

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField(default_value=0, readable=False)
    f1 = fchild1

    fchild2 = LongField(default_value=0, readable=False)
    f2 = fchild2

    fchild3 = LongField(default_value=0, readable=False)
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class DriversPlugOperator(
    CompoundPlugOperator["DriversAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("driverBindGeometry", "orgdrv"),
        ("driverReferenceGeometry", "refdrv"),
        ("driverGeometry", "curdrv"),
        ("driverClusterRestMatrix", "dorgcls"),
        ("driverClusterMatrix", "dcurcls"),
        ("driverFalloffStart", "dfos"),
        ("driverFalloffEnd", "dfoe"),
        ("driverDropoffRate", "ddpo"),
        ("driverFalloffRamp", "dfrmp"),
        ("driverOverrideFalloffRamp", "dofrmp"),
        ("driverStrength", "dstrn"),
        ("driverUseTransformAsDeformation", "dxad"),
        ("driverScaleCompensation", "dscp"),
        ("driverSmoothNormals", "dsnrm"),
        ("driverOverrideSmoothNormals", "dosnrm"),
        ("driverSpanSamples", "dspns"),
        ("driverSmoothInfluences", "dsinf"),
        ("driverOverrideSmoothInfluences", "dosinf"),
        ("driverOverrideSpanSamples", "dospns"),
        ("driverWrapMode", "dwmd"),
    )

    driverBindGeometry = TypedField()
    orgdrv = driverBindGeometry

    driverReferenceGeometry = TypedField()
    refdrv = driverReferenceGeometry

    driverGeometry = TypedField()
    curdrv = driverGeometry

    driverClusterRestMatrix = MatrixField()
    dorgcls = driverClusterRestMatrix

    driverClusterMatrix = MatrixField()
    dcurcls = driverClusterMatrix

    driverFalloffStart = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dfos = driverFalloffStart

    driverFalloffEnd = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dfoe = driverFalloffEnd

    driverDropoffRate = DoubleField(default_value=4.0, min_value=0.0, soft_max_value=10.0)
    ddpo = driverDropoffRate

    driverFalloffRamp = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    dfrmp = driverFalloffRamp

    driverOverrideFalloffRamp = BoolField(default_value=False)
    dofrmp = driverOverrideFalloffRamp

    driverStrength = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    dstrn = driverStrength

    driverUseTransformAsDeformation = BoolField(default_value=True)
    dxad = driverUseTransformAsDeformation

    driverScaleCompensation = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    dscp = driverScaleCompensation

    driverSmoothNormals = LongField(default_value=0, min_value=0, max_value=20)
    dsnrm = driverSmoothNormals

    driverOverrideSmoothNormals = BoolField(default_value=False)
    dosnrm = driverOverrideSmoothNormals

    driverSpanSamples = LongField(default_value=2, min_value=1, max_value=10)
    dspns = driverSpanSamples

    driverSmoothInfluences = LongField(default_value=0, min_value=0, max_value=20)
    dsinf = driverSmoothInfluences

    driverOverrideSmoothInfluences = BoolField(default_value=False)
    dosinf = driverOverrideSmoothInfluences

    driverOverrideSpanSamples = BoolField(default_value=False)
    dospns = driverOverrideSpanSamples

    driverWrapMode = DriverWrapModeEnumField(default_value=100)
    dwmd = driverWrapMode


class DriversAttrOperator(
    CompoundAttrOperator[DriversPlugOperator]
):
    __slots__ = ()

    driverBindGeometry = TypedField()
    orgdrv = driverBindGeometry

    driverReferenceGeometry = TypedField()
    refdrv = driverReferenceGeometry

    driverGeometry = TypedField()
    curdrv = driverGeometry

    driverClusterRestMatrix = MatrixField()
    dorgcls = driverClusterRestMatrix

    driverClusterMatrix = MatrixField()
    dcurcls = driverClusterMatrix

    driverFalloffStart = DoubleField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dfos = driverFalloffStart

    driverFalloffEnd = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    dfoe = driverFalloffEnd

    driverDropoffRate = DoubleField(default_value=4.0, min_value=0.0, soft_max_value=10.0)
    ddpo = driverDropoffRate

    driverFalloffRamp = CompoundField(multi=True, default_value=(0.0, 0.0, 0.0))
    dfrmp = driverFalloffRamp

    driverOverrideFalloffRamp = BoolField(default_value=False)
    dofrmp = driverOverrideFalloffRamp

    driverStrength = DoubleField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    dstrn = driverStrength

    driverUseTransformAsDeformation = BoolField(default_value=True)
    dxad = driverUseTransformAsDeformation

    driverScaleCompensation = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    dscp = driverScaleCompensation

    driverSmoothNormals = LongField(default_value=0, min_value=0, max_value=20)
    dsnrm = driverSmoothNormals

    driverOverrideSmoothNormals = BoolField(default_value=False)
    dosnrm = driverOverrideSmoothNormals

    driverSpanSamples = LongField(default_value=2, min_value=1, max_value=10)
    dspns = driverSpanSamples

    driverSmoothInfluences = LongField(default_value=0, min_value=0, max_value=20)
    dsinf = driverSmoothInfluences

    driverOverrideSmoothInfluences = BoolField(default_value=False)
    dosinf = driverOverrideSmoothInfluences

    driverOverrideSpanSamples = BoolField(default_value=False)
    dospns = driverOverrideSpanSamples

    driverWrapMode = DriverWrapModeEnumField(default_value=100)
    dwmd = driverWrapMode


class DriversField(
    CompoundField[DriversAttrOperator, DriversPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DriversAttrOperator
    PLUG_CLS = DriversPlugOperator


class FalloffRampPlugOperator(
    CompoundPlugOperator["FalloffRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffRamp_Position", "frmpp"),
        ("falloffRamp_FloatValue", "frmpfv"),
        ("falloffRamp_Interp", "frmpi"),
    )

    falloffRamp_Position = FloatField(default_value=0.0)
    frmpp = falloffRamp_Position

    falloffRamp_FloatValue = FloatField(default_value=0.0)
    frmpfv = falloffRamp_FloatValue

    falloffRamp_Interp = FalloffRamp_InterpEnumField(default_value=0)
    frmpi = falloffRamp_Interp


class FalloffRampAttrOperator(
    CompoundAttrOperator[FalloffRampPlugOperator]
):
    __slots__ = ()

    falloffRamp_Position = FloatField(default_value=0.0)
    frmpp = falloffRamp_Position

    falloffRamp_FloatValue = FloatField(default_value=0.0)
    frmpfv = falloffRamp_FloatValue

    falloffRamp_Interp = FalloffRamp_InterpEnumField(default_value=0)
    frmpi = falloffRamp_Interp


class FalloffRampField(
    CompoundField[FalloffRampAttrOperator, FalloffRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffRampAttrOperator
    PLUG_CLS = FalloffRampPlugOperator


class PerDriverWeightsListPlugOperator(
    CompoundPlugOperator["PerDriverWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("perDriverWeights", "pdw"),
    )

    perDriverWeights = CompoundField(multi=True, default_value=0.0, writable=False)
    pdw = perDriverWeights


class PerDriverWeightsListAttrOperator(
    CompoundAttrOperator[PerDriverWeightsListPlugOperator]
):
    __slots__ = ()

    perDriverWeights = CompoundField(multi=True, default_value=0.0, writable=False)
    pdw = perDriverWeights


class PerDriverWeightsListField(
    CompoundField[PerDriverWeightsListAttrOperator, PerDriverWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PerDriverWeightsListAttrOperator
    PLUG_CLS = PerDriverWeightsListPlugOperator


class PerVertexWeightsListPlugOperator(
    CompoundPlugOperator["PerVertexWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("perVertexWeights", "pvw"),
    )

    perVertexWeights = CompoundField(multi=True, default_value=0.0, writable=False)
    pvw = perVertexWeights


class PerVertexWeightsListAttrOperator(
    CompoundAttrOperator[PerVertexWeightsListPlugOperator]
):
    __slots__ = ()

    perVertexWeights = CompoundField(multi=True, default_value=0.0, writable=False)
    pvw = perVertexWeights


class PerVertexWeightsListField(
    CompoundField[PerVertexWeightsListAttrOperator, PerVertexWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PerVertexWeightsListAttrOperator
    PLUG_CLS = PerVertexWeightsListPlugOperator
