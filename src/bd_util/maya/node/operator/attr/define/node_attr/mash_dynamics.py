# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class InitialVelocityPlugOperator(
    Float3CompoundBasePlugOperator["InitialVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialVelocity0", "initialVelocity0"),
        ("initialVelocity1", "initialVelocity1"),
        ("initialVelocity2", "initialVelocity2"),
    )

    initialVelocity0 = FloatField(default_value=0.0)

    initialVelocity1 = FloatField(default_value=0.0)

    initialVelocity2 = FloatField(default_value=0.0)


class InitialVelocityAttrOperator(
    Float3CompoundBaseAttrOperator[InitialVelocityPlugOperator]
):
    __slots__ = ()

    initialVelocity0 = FloatField(default_value=0.0)

    initialVelocity1 = FloatField(default_value=0.0)

    initialVelocity2 = FloatField(default_value=0.0)


class InitialVelocityField(
    Float3CompoundBaseField[InitialVelocityAttrOperator, InitialVelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialVelocityAttrOperator
    PLUG_CLS = InitialVelocityPlugOperator

    initialVelocity0 = FloatField(default_value=0.0)

    initialVelocity1 = FloatField(default_value=0.0)

    initialVelocity2 = FloatField(default_value=0.0)


class InitialRotationalVelocityPlugOperator(
    Float3CompoundBasePlugOperator["InitialRotationalVelocityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("initialRotationalVelocity0", "initialRotationalVelocity0"),
        ("initialRotationalVelocity1", "initialRotationalVelocity1"),
        ("initialRotationalVelocity2", "initialRotationalVelocity2"),
    )

    initialRotationalVelocity0 = FloatField(default_value=0.0)

    initialRotationalVelocity1 = FloatField(default_value=0.0)

    initialRotationalVelocity2 = FloatField(default_value=0.0)


class InitialRotationalVelocityAttrOperator(
    Float3CompoundBaseAttrOperator[InitialRotationalVelocityPlugOperator]
):
    __slots__ = ()

    initialRotationalVelocity0 = FloatField(default_value=0.0)

    initialRotationalVelocity1 = FloatField(default_value=0.0)

    initialRotationalVelocity2 = FloatField(default_value=0.0)


class InitialRotationalVelocityField(
    Float3CompoundBaseField[InitialRotationalVelocityAttrOperator, InitialRotationalVelocityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialRotationalVelocityAttrOperator
    PLUG_CLS = InitialRotationalVelocityPlugOperator

    initialRotationalVelocity0 = FloatField(default_value=0.0)

    initialRotationalVelocity1 = FloatField(default_value=0.0)

    initialRotationalVelocity2 = FloatField(default_value=0.0)
