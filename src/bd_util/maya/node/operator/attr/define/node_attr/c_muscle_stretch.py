# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
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


class ForceStartPlugOperator(
    Float3CompoundBasePlugOperator["ForceStartAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceStartX", "fstx"),
        ("forceStartY", "fsty"),
        ("forceStartZ", "fstz"),
    )

    forceStartX = FloatField()
    fstx = forceStartX

    forceStartY = FloatField()
    fsty = forceStartY

    forceStartZ = FloatField()
    fstz = forceStartZ


class ForceStartAttrOperator(
    Float3CompoundBaseAttrOperator[ForceStartPlugOperator]
):
    __slots__ = ()

    forceStartX = FloatField()
    fstx = forceStartX

    forceStartY = FloatField()
    fsty = forceStartY

    forceStartZ = FloatField()
    fstz = forceStartZ


class ForceStartField(
    Float3CompoundBaseField[ForceStartAttrOperator, ForceStartPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceStartAttrOperator
    PLUG_CLS = ForceStartPlugOperator


class ForceMidPlugOperator(
    Float3CompoundBasePlugOperator["ForceMidAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceMidX", "fmdx"),
        ("forceMidY", "fmdy"),
        ("forceMidZ", "fmdz"),
    )

    forceMidX = FloatField()
    fmdx = forceMidX

    forceMidY = FloatField()
    fmdy = forceMidY

    forceMidZ = FloatField()
    fmdz = forceMidZ


class ForceMidAttrOperator(
    Float3CompoundBaseAttrOperator[ForceMidPlugOperator]
):
    __slots__ = ()

    forceMidX = FloatField()
    fmdx = forceMidX

    forceMidY = FloatField()
    fmdy = forceMidY

    forceMidZ = FloatField()
    fmdz = forceMidZ


class ForceMidField(
    Float3CompoundBaseField[ForceMidAttrOperator, ForceMidPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceMidAttrOperator
    PLUG_CLS = ForceMidPlugOperator


class ForceEndPlugOperator(
    Float3CompoundBasePlugOperator["ForceEndAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("forceEndX", "fedx"),
        ("forceEndY", "fedy"),
        ("forceEndZ", "fedz"),
    )

    forceEndX = FloatField()
    fedx = forceEndX

    forceEndY = FloatField()
    fedy = forceEndY

    forceEndZ = FloatField()
    fedz = forceEndZ


class ForceEndAttrOperator(
    Float3CompoundBaseAttrOperator[ForceEndPlugOperator]
):
    __slots__ = ()

    forceEndX = FloatField()
    fedx = forceEndX

    forceEndY = FloatField()
    fedy = forceEndY

    forceEndZ = FloatField()
    fedz = forceEndZ


class ForceEndField(
    Float3CompoundBaseField[ForceEndAttrOperator, ForceEndPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceEndAttrOperator
    PLUG_CLS = ForceEndPlugOperator
