# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class OutputsPlugOperator(
    CompoundPlugOperator["OutputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translate", "translate"),
        ("rotate", "rotate"),
        ("scale", "scale"),
        ("id", "id"),
        ("visibility", "visibility"),
        ("color", "color"),
        ("time", "time"),
        ("velocityVector", "velocityVector"),
        ("angularVelocityVector", "angularVelocityVector"),
        ("velocity", "velocity"),
        ("angularVelocity", "angularVelocity"),
    )

    translate = Float3Field()

    rotate = Double3Field()

    scale = Float3Field()

    id = FloatField()

    visibility = LongField()

    color = Float3Field()

    time = FloatField()

    velocityVector = Float3Field()

    angularVelocityVector = Float3Field()

    velocity = FloatField()

    angularVelocity = FloatField()


class OutputsAttrOperator(
    CompoundAttrOperator[OutputsPlugOperator]
):
    __slots__ = ()

    translate = Float3Field()

    rotate = Double3Field()

    scale = Float3Field()

    id = FloatField()

    visibility = LongField()

    color = Float3Field()

    time = FloatField()

    velocityVector = Float3Field()

    angularVelocityVector = Float3Field()

    velocity = FloatField()

    angularVelocity = FloatField()


class OutputsField(
    CompoundField[OutputsAttrOperator, OutputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputsAttrOperator
    PLUG_CLS = OutputsPlugOperator
