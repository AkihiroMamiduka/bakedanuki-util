# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
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


class InputTargetPlugOperator(
    CompoundPlugOperator["InputTargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputTargetGroup", "itg"),
        ("baseWeights", "bw"),
        ("normalizationGroup", "ng"),
        ("paintTargetWeights", "pwt"),
        ("paintTargetIndex", "pti"),
        ("sculptTargetIndex", "sti"),
        ("sculptInbetweenWeight", "siw"),
        ("sculptTargetTweaks", "stt"),
        ("deformMatrix", "dmx"),
        ("deformMatrixModified", "dmxm"),
    )

    inputTargetGroup = CompoundField()
    itg = inputTargetGroup

    baseWeights = FloatField()
    bw = baseWeights

    normalizationGroup = CompoundField()
    ng = normalizationGroup

    paintTargetWeights = FloatField()
    pwt = paintTargetWeights

    paintTargetIndex = LongField()
    pti = paintTargetIndex

    sculptTargetIndex = LongField()
    sti = sculptTargetIndex

    sculptInbetweenWeight = DoubleField()
    siw = sculptInbetweenWeight

    sculptTargetTweaks = CompoundField()
    stt = sculptTargetTweaks

    deformMatrix = TypedField()
    dmx = deformMatrix

    deformMatrixModified = BoolField()
    dmxm = deformMatrixModified


class InputTargetAttrOperator(
    CompoundAttrOperator[InputTargetPlugOperator]
):
    __slots__ = ()

    inputTargetGroup = CompoundField()
    itg = inputTargetGroup

    baseWeights = FloatField()
    bw = baseWeights

    normalizationGroup = CompoundField()
    ng = normalizationGroup

    paintTargetWeights = FloatField()
    pwt = paintTargetWeights

    paintTargetIndex = LongField()
    pti = paintTargetIndex

    sculptTargetIndex = LongField()
    sti = sculptTargetIndex

    sculptInbetweenWeight = DoubleField()
    siw = sculptInbetweenWeight

    sculptTargetTweaks = CompoundField()
    stt = sculptTargetTweaks

    deformMatrix = TypedField()
    dmx = deformMatrix

    deformMatrixModified = BoolField()
    dmxm = deformMatrixModified


class InputTargetField(
    CompoundField[InputTargetAttrOperator, InputTargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputTargetAttrOperator
    PLUG_CLS = InputTargetPlugOperator


class BaseOriginPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["BaseOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseOriginX", "bx"),
        ("baseOriginY", "by"),
        ("baseOriginZ", "bz"),
    )

    baseOriginX = DoubleLinearField()
    bx = baseOriginX

    baseOriginY = DoubleLinearField()
    by = baseOriginY

    baseOriginZ = DoubleLinearField()
    bz = baseOriginZ


class BaseOriginAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[BaseOriginPlugOperator]
):
    __slots__ = ()

    baseOriginX = DoubleLinearField()
    bx = baseOriginX

    baseOriginY = DoubleLinearField()
    by = baseOriginY

    baseOriginZ = DoubleLinearField()
    bz = baseOriginZ


class BaseOriginField(
    DoubleLinear3CompoundBaseField[BaseOriginAttrOperator, BaseOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseOriginAttrOperator
    PLUG_CLS = BaseOriginPlugOperator

    baseOriginX = DoubleLinearField()
    bx = baseOriginX

    baseOriginY = DoubleLinearField()
    by = baseOriginY

    baseOriginZ = DoubleLinearField()
    bz = baseOriginZ


class TargetOriginPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TargetOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetOriginX", "tx"),
        ("targetOriginY", "ty"),
        ("targetOriginZ", "tz"),
    )

    targetOriginX = DoubleLinearField()
    tx = targetOriginX

    targetOriginY = DoubleLinearField()
    ty = targetOriginY

    targetOriginZ = DoubleLinearField()
    tz = targetOriginZ


class TargetOriginAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TargetOriginPlugOperator]
):
    __slots__ = ()

    targetOriginX = DoubleLinearField()
    tx = targetOriginX

    targetOriginY = DoubleLinearField()
    ty = targetOriginY

    targetOriginZ = DoubleLinearField()
    tz = targetOriginZ


class TargetOriginField(
    DoubleLinear3CompoundBaseField[TargetOriginAttrOperator, TargetOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetOriginAttrOperator
    PLUG_CLS = TargetOriginPlugOperator

    targetOriginX = DoubleLinearField()
    tx = targetOriginX

    targetOriginY = DoubleLinearField()
    ty = targetOriginY

    targetOriginZ = DoubleLinearField()
    tz = targetOriginZ


class OffsetDeformerPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OffsetDeformerAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ofx"),
        ("offsetY", "ofy"),
        ("offsetZ", "ofz"),
    )

    offsetX = DoubleLinearField()
    ofx = offsetX

    offsetY = DoubleLinearField()
    ofy = offsetY

    offsetZ = DoubleLinearField()
    ofz = offsetZ


class OffsetDeformerAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetDeformerPlugOperator]
):
    __slots__ = ()

    offsetX = DoubleLinearField()
    ofx = offsetX

    offsetY = DoubleLinearField()
    ofy = offsetY

    offsetZ = DoubleLinearField()
    ofz = offsetZ


class OffsetDeformerField(
    DoubleLinear3CompoundBaseField[OffsetDeformerAttrOperator, OffsetDeformerPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetDeformerAttrOperator
    PLUG_CLS = OffsetDeformerPlugOperator

    offsetX = DoubleLinearField()
    ofx = offsetX

    offsetY = DoubleLinearField()
    ofy = offsetY

    offsetZ = DoubleLinearField()
    ofz = offsetZ


class TargetDirectoryPlugOperator(
    CompoundPlugOperator["TargetDirectoryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("childIndices", "cid"),
        ("parentIndex", "pnid"),
        ("directoryName", "dtn"),
        ("directoryVisibility", "dvs"),
        ("directoryParentVisibility", "dpvs"),
        ("directoryWeight", "dwgh"),
    )

    childIndices = TypedField()
    cid = childIndices

    parentIndex = LongField()
    pnid = parentIndex

    directoryName = DataStringField()
    dtn = directoryName

    directoryVisibility = BoolField()
    dvs = directoryVisibility

    directoryParentVisibility = BoolField()
    dpvs = directoryParentVisibility

    directoryWeight = FloatField()
    dwgh = directoryWeight


class TargetDirectoryAttrOperator(
    CompoundAttrOperator[TargetDirectoryPlugOperator]
):
    __slots__ = ()

    childIndices = TypedField()
    cid = childIndices

    parentIndex = LongField()
    pnid = parentIndex

    directoryName = DataStringField()
    dtn = directoryName

    directoryVisibility = BoolField()
    dvs = directoryVisibility

    directoryParentVisibility = BoolField()
    dpvs = directoryParentVisibility

    directoryWeight = FloatField()
    dwgh = directoryWeight


class TargetDirectoryField(
    CompoundField[TargetDirectoryAttrOperator, TargetDirectoryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetDirectoryAttrOperator
    PLUG_CLS = TargetDirectoryPlugOperator


class InbetweenInfoGroupPlugOperator(
    CompoundPlugOperator["InbetweenInfoGroupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inbetweenInfo", "ibi"),
    )

    inbetweenInfo = CompoundField()
    ibi = inbetweenInfo


class InbetweenInfoGroupAttrOperator(
    CompoundAttrOperator[InbetweenInfoGroupPlugOperator]
):
    __slots__ = ()

    inbetweenInfo = CompoundField()
    ibi = inbetweenInfo


class InbetweenInfoGroupField(
    CompoundField[InbetweenInfoGroupAttrOperator, InbetweenInfoGroupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InbetweenInfoGroupAttrOperator
    PLUG_CLS = InbetweenInfoGroupPlugOperator
