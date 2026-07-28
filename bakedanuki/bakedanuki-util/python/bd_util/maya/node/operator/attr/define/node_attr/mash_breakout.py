# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..custom import (
    Double3Field,
    Float3Field,
)


class OutputsPlugOperator(CompoundPlugOperator["OutputsAttrOperator"]):
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

    translate = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    rotate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    scale = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    id = FloatField(default_value=0.0, writable=False)

    visibility = LongField(default_value=0, writable=False)

    color = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    time = FloatField(default_value=0.0, writable=False)

    velocityVector = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    angularVelocityVector = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )

    velocity = FloatField(default_value=0.0)

    angularVelocity = FloatField(default_value=0.0, writable=False)


class OutputsAttrOperator(CompoundAttrOperator[OutputsPlugOperator]):
    __slots__ = ()

    translate = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    rotate = Double3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    scale = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    id = FloatField(default_value=0.0, writable=False)

    visibility = LongField(default_value=0, writable=False)

    color = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    time = FloatField(default_value=0.0, writable=False)

    velocityVector = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)

    angularVelocityVector = Float3Field(
        default_value=(0.0, 0.0, 0.0), writable=False
    )

    velocity = FloatField(default_value=0.0)

    angularVelocity = FloatField(default_value=0.0, writable=False)


class OutputsField(CompoundField[OutputsAttrOperator, OutputsPlugOperator]):
    __slots__ = ()

    ATTR_CLS = OutputsAttrOperator
    PLUG_CLS = OutputsPlugOperator
