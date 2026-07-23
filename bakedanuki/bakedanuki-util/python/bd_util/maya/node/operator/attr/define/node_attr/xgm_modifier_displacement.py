# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class VectorDisplacementPlugOperator(
    Float3CompoundBasePlugOperator["VectorDisplacementAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorDisplacement0", "vdis0"),
        ("vectorDisplacement1", "vdis1"),
        ("vectorDisplacement2", "vdis2"),
    )

    vectorDisplacement0 = FloatField(default_value=0.0)
    vdis0 = vectorDisplacement0

    vectorDisplacement1 = FloatField(default_value=0.0)
    vdis1 = vectorDisplacement1

    vectorDisplacement2 = FloatField(default_value=0.0)
    vdis2 = vectorDisplacement2


class VectorDisplacementAttrOperator(
    Float3CompoundBaseAttrOperator[VectorDisplacementPlugOperator]
):
    __slots__ = ()

    vectorDisplacement0 = FloatField(default_value=0.0)
    vdis0 = vectorDisplacement0

    vectorDisplacement1 = FloatField(default_value=0.0)
    vdis1 = vectorDisplacement1

    vectorDisplacement2 = FloatField(default_value=0.0)
    vdis2 = vectorDisplacement2


class VectorDisplacementField(
    Float3CompoundBaseField[VectorDisplacementAttrOperator, VectorDisplacementPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorDisplacementAttrOperator
    PLUG_CLS = VectorDisplacementPlugOperator

    vectorDisplacement0 = FloatField(default_value=0.0)
    vdis0 = vectorDisplacement0

    vectorDisplacement1 = FloatField(default_value=0.0)
    vdis1 = vectorDisplacement1

    vectorDisplacement2 = FloatField(default_value=0.0)
    vdis2 = vectorDisplacement2
