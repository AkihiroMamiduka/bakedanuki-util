# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)


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

    groupId = LongField()
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputAttrOperator(
    CompoundAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField()
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

    envelopeWeights = FloatField()
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField()
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

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionAttrOperator(
    Long3CompoundBaseAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class FunctionField(
    Long3CompoundBaseField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    fchild1 = LongField()
    f1 = fchild1

    fchild2 = LongField()
    f2 = fchild2

    fchild3 = LongField()
    f3 = fchild3


class WeightListPlugOperator(
    CompoundPlugOperator["WeightListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("weights", "wl.w"),
    )

    weights = FloatField()


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()


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

    driverFalloffStart = DoubleField()
    dfos = driverFalloffStart

    driverFalloffEnd = DoubleField()
    dfoe = driverFalloffEnd

    driverDropoffRate = DoubleField()
    ddpo = driverDropoffRate

    driverFalloffRamp = CompoundField()
    dfrmp = driverFalloffRamp

    driverOverrideFalloffRamp = BoolField()
    dofrmp = driverOverrideFalloffRamp

    driverStrength = DoubleField()
    dstrn = driverStrength

    driverUseTransformAsDeformation = BoolField()
    dxad = driverUseTransformAsDeformation

    driverScaleCompensation = DoubleField()
    dscp = driverScaleCompensation

    driverSmoothNormals = LongField()
    dsnrm = driverSmoothNormals

    driverOverrideSmoothNormals = BoolField()
    dosnrm = driverOverrideSmoothNormals

    driverSpanSamples = LongField()
    dspns = driverSpanSamples

    driverSmoothInfluences = LongField()
    dsinf = driverSmoothInfluences

    driverOverrideSmoothInfluences = BoolField()
    dosinf = driverOverrideSmoothInfluences

    driverOverrideSpanSamples = BoolField()
    dospns = driverOverrideSpanSamples

    driverWrapMode = EnumField()
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

    driverFalloffStart = DoubleField()
    dfos = driverFalloffStart

    driverFalloffEnd = DoubleField()
    dfoe = driverFalloffEnd

    driverDropoffRate = DoubleField()
    ddpo = driverDropoffRate

    driverFalloffRamp = CompoundField()
    dfrmp = driverFalloffRamp

    driverOverrideFalloffRamp = BoolField()
    dofrmp = driverOverrideFalloffRamp

    driverStrength = DoubleField()
    dstrn = driverStrength

    driverUseTransformAsDeformation = BoolField()
    dxad = driverUseTransformAsDeformation

    driverScaleCompensation = DoubleField()
    dscp = driverScaleCompensation

    driverSmoothNormals = LongField()
    dsnrm = driverSmoothNormals

    driverOverrideSmoothNormals = BoolField()
    dosnrm = driverOverrideSmoothNormals

    driverSpanSamples = LongField()
    dspns = driverSpanSamples

    driverSmoothInfluences = LongField()
    dsinf = driverSmoothInfluences

    driverOverrideSmoothInfluences = BoolField()
    dosinf = driverOverrideSmoothInfluences

    driverOverrideSpanSamples = BoolField()
    dospns = driverOverrideSpanSamples

    driverWrapMode = EnumField()
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

    falloffRamp_Position = FloatField()
    frmpp = falloffRamp_Position

    falloffRamp_FloatValue = FloatField()
    frmpfv = falloffRamp_FloatValue

    falloffRamp_Interp = EnumField()
    frmpi = falloffRamp_Interp


class FalloffRampAttrOperator(
    CompoundAttrOperator[FalloffRampPlugOperator]
):
    __slots__ = ()

    falloffRamp_Position = FloatField()
    frmpp = falloffRamp_Position

    falloffRamp_FloatValue = FloatField()
    frmpfv = falloffRamp_FloatValue

    falloffRamp_Interp = EnumField()
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

    perDriverWeights = CompoundField()
    pdw = perDriverWeights


class PerDriverWeightsListAttrOperator(
    CompoundAttrOperator[PerDriverWeightsListPlugOperator]
):
    __slots__ = ()

    perDriverWeights = CompoundField()
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

    perVertexWeights = CompoundField()
    pvw = perVertexWeights


class PerVertexWeightsListAttrOperator(
    CompoundAttrOperator[PerVertexWeightsListPlugOperator]
):
    __slots__ = ()

    perVertexWeights = CompoundField()
    pvw = perVertexWeights


class PerVertexWeightsListField(
    CompoundField[PerVertexWeightsListAttrOperator, PerVertexWeightsListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PerVertexWeightsListAttrOperator
    PLUG_CLS = PerVertexWeightsListPlugOperator
