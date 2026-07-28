# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
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


class InputPlugOperator(CompoundPlugOperator["InputAttrOperator"]):
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


class InputAttrOperator(CompoundAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputGeometry = TypedField()
    ig = inputGeometry

    groupId = LongField(default_value=0)
    gi = groupId

    componentTagExpression = DataStringField()
    gtg = componentTagExpression


class InputField(CompoundField[InputAttrOperator, InputPlugOperator]):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator


class EnvelopeWeightsListPlugOperator(
    CompoundPlugOperator["EnvelopeWeightsListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("envelopeWeights", "owt"),)

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListAttrOperator(
    CompoundAttrOperator[EnvelopeWeightsListPlugOperator]
):
    __slots__ = ()

    envelopeWeights = FloatField(multi=True, default_value=1.0, writable=False)
    owt = envelopeWeights


class EnvelopeWeightsListField(
    CompoundField[
        EnvelopeWeightsListAttrOperator, EnvelopeWeightsListPlugOperator
    ]
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


class WeightListPlugOperator(CompoundPlugOperator["WeightListAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (("weights", "wl.w"),)

    weights = FloatField(multi=True, default_value=1.0)


class WeightListAttrOperator(CompoundAttrOperator[WeightListPlugOperator]):
    __slots__ = ()

    weights = FloatField(multi=True, default_value=1.0)


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class InputTargetPlugOperator(CompoundPlugOperator["InputTargetAttrOperator"]):
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

    inputTargetGroup = CompoundField(multi=True)
    itg = inputTargetGroup

    baseWeights = FloatField(multi=True, default_value=1.0)
    bw = baseWeights

    normalizationGroup = CompoundField(multi=True, default_value=(0.0, 1.0))
    ng = normalizationGroup

    paintTargetWeights = FloatField(multi=True, default_value=1.0)
    pwt = paintTargetWeights

    paintTargetIndex = LongField(default_value=0)
    pti = paintTargetIndex

    sculptTargetIndex = LongField(default_value=-1)
    sti = sculptTargetIndex

    sculptInbetweenWeight = DoubleField(default_value=-1.0)
    siw = sculptInbetweenWeight

    sculptTargetTweaks = CompoundField()
    stt = sculptTargetTweaks

    deformMatrix = TypedField()
    dmx = deformMatrix

    deformMatrixModified = BoolField(default_value=False)
    dmxm = deformMatrixModified


class InputTargetAttrOperator(CompoundAttrOperator[InputTargetPlugOperator]):
    __slots__ = ()

    inputTargetGroup = CompoundField(multi=True)
    itg = inputTargetGroup

    baseWeights = FloatField(multi=True, default_value=1.0)
    bw = baseWeights

    normalizationGroup = CompoundField(multi=True, default_value=(0.0, 1.0))
    ng = normalizationGroup

    paintTargetWeights = FloatField(multi=True, default_value=1.0)
    pwt = paintTargetWeights

    paintTargetIndex = LongField(default_value=0)
    pti = paintTargetIndex

    sculptTargetIndex = LongField(default_value=-1)
    sti = sculptTargetIndex

    sculptInbetweenWeight = DoubleField(default_value=-1.0)
    siw = sculptInbetweenWeight

    sculptTargetTweaks = CompoundField()
    stt = sculptTargetTweaks

    deformMatrix = TypedField()
    dmx = deformMatrix

    deformMatrixModified = BoolField(default_value=False)
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

    baseOriginX = DoubleLinearField(default_value=0.0)
    bx = baseOriginX

    baseOriginY = DoubleLinearField(default_value=0.0)
    by = baseOriginY

    baseOriginZ = DoubleLinearField(default_value=0.0)
    bz = baseOriginZ


class BaseOriginAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[BaseOriginPlugOperator]
):
    __slots__ = ()

    baseOriginX = DoubleLinearField(default_value=0.0)
    bx = baseOriginX

    baseOriginY = DoubleLinearField(default_value=0.0)
    by = baseOriginY

    baseOriginZ = DoubleLinearField(default_value=0.0)
    bz = baseOriginZ


class BaseOriginField(
    DoubleLinear3CompoundBaseField[
        BaseOriginAttrOperator, BaseOriginPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BaseOriginAttrOperator
    PLUG_CLS = BaseOriginPlugOperator

    baseOriginX = DoubleLinearField(default_value=0.0)
    bx = baseOriginX

    baseOriginY = DoubleLinearField(default_value=0.0)
    by = baseOriginY

    baseOriginZ = DoubleLinearField(default_value=0.0)
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

    targetOriginX = DoubleLinearField(default_value=0.0)
    tx = targetOriginX

    targetOriginY = DoubleLinearField(default_value=0.0)
    ty = targetOriginY

    targetOriginZ = DoubleLinearField(default_value=0.0)
    tz = targetOriginZ


class TargetOriginAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TargetOriginPlugOperator]
):
    __slots__ = ()

    targetOriginX = DoubleLinearField(default_value=0.0)
    tx = targetOriginX

    targetOriginY = DoubleLinearField(default_value=0.0)
    ty = targetOriginY

    targetOriginZ = DoubleLinearField(default_value=0.0)
    tz = targetOriginZ


class TargetOriginField(
    DoubleLinear3CompoundBaseField[
        TargetOriginAttrOperator, TargetOriginPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TargetOriginAttrOperator
    PLUG_CLS = TargetOriginPlugOperator

    targetOriginX = DoubleLinearField(default_value=0.0)
    tx = targetOriginX

    targetOriginY = DoubleLinearField(default_value=0.0)
    ty = targetOriginY

    targetOriginZ = DoubleLinearField(default_value=0.0)
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

    offsetX = DoubleLinearField(default_value=0.0)
    ofx = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    ofy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
    ofz = offsetZ


class OffsetDeformerAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OffsetDeformerPlugOperator]
):
    __slots__ = ()

    offsetX = DoubleLinearField(default_value=0.0)
    ofx = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    ofy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
    ofz = offsetZ


class OffsetDeformerField(
    DoubleLinear3CompoundBaseField[
        OffsetDeformerAttrOperator, OffsetDeformerPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OffsetDeformerAttrOperator
    PLUG_CLS = OffsetDeformerPlugOperator

    offsetX = DoubleLinearField(default_value=0.0)
    ofx = offsetX

    offsetY = DoubleLinearField(default_value=0.0)
    ofy = offsetY

    offsetZ = DoubleLinearField(default_value=0.0)
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

    parentIndex = LongField(default_value=0)
    pnid = parentIndex

    directoryName = DataStringField()
    dtn = directoryName

    directoryVisibility = BoolField(default_value=True)
    dvs = directoryVisibility

    directoryParentVisibility = BoolField(default_value=True)
    dpvs = directoryParentVisibility

    directoryWeight = FloatField(
        default_value=1.0,
        min_value=-10.0,
        max_value=10.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    dwgh = directoryWeight


class TargetDirectoryAttrOperator(
    CompoundAttrOperator[TargetDirectoryPlugOperator]
):
    __slots__ = ()

    childIndices = TypedField()
    cid = childIndices

    parentIndex = LongField(default_value=0)
    pnid = parentIndex

    directoryName = DataStringField()
    dtn = directoryName

    directoryVisibility = BoolField(default_value=True)
    dvs = directoryVisibility

    directoryParentVisibility = BoolField(default_value=True)
    dpvs = directoryParentVisibility

    directoryWeight = FloatField(
        default_value=1.0,
        min_value=-10.0,
        max_value=10.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
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
    CHILD_ATTR_NAMES = (("inbetweenInfo", "ibi"),)

    inbetweenInfo = CompoundField(multi=True)
    ibi = inbetweenInfo


class InbetweenInfoGroupAttrOperator(
    CompoundAttrOperator[InbetweenInfoGroupPlugOperator]
):
    __slots__ = ()

    inbetweenInfo = CompoundField(multi=True)
    ibi = inbetweenInfo


class InbetweenInfoGroupField(
    CompoundField[
        InbetweenInfoGroupAttrOperator, InbetweenInfoGroupPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InbetweenInfoGroupAttrOperator
    PLUG_CLS = InbetweenInfoGroupPlugOperator
