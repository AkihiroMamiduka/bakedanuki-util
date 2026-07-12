# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class PoleVectorPlugOperator(
    Double3CompoundBasePlugOperator["PoleVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("poleVectorX", "pvx"),
        ("poleVectorY", "pvy"),
        ("poleVectorZ", "pvz"),
    )

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class PoleVectorAttrOperator(
    Double3CompoundBaseAttrOperator[PoleVectorPlugOperator]
):
    __slots__ = ()

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class PoleVectorField(
    Double3CompoundBaseField[PoleVectorAttrOperator, PoleVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoleVectorAttrOperator
    PLUG_CLS = PoleVectorPlugOperator

    poleVectorX = DoubleField(default_value=0.0)
    pvx = poleVectorX

    poleVectorY = DoubleField(default_value=0.0)
    pvy = poleVectorY

    poleVectorZ = DoubleField(default_value=1.0)
    pvz = poleVectorZ


class DWorldUpVectorPlugOperator(
    Double3CompoundBasePlugOperator["DWorldUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dWorldUpVectorX", "dwux"),
        ("dWorldUpVectorY", "dwuy"),
        ("dWorldUpVectorZ", "dwuz"),
    )

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorAttrOperator(
    Double3CompoundBaseAttrOperator[DWorldUpVectorPlugOperator]
):
    __slots__ = ()

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorField(
    Double3CompoundBaseField[DWorldUpVectorAttrOperator, DWorldUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpVectorAttrOperator
    PLUG_CLS = DWorldUpVectorPlugOperator

    dWorldUpVectorX = DoubleField(default_value=0.0)
    dwux = dWorldUpVectorX

    dWorldUpVectorY = DoubleField(default_value=1.0)
    dwuy = dWorldUpVectorY

    dWorldUpVectorZ = DoubleField(default_value=0.0)
    dwuz = dWorldUpVectorZ


class DWorldUpVectorEndPlugOperator(
    Double3CompoundBasePlugOperator["DWorldUpVectorEndAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dWorldUpVectorEndX", "dwvx"),
        ("dWorldUpVectorEndY", "dwvy"),
        ("dWorldUpVectorEndZ", "dwvz"),
    )

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DWorldUpVectorEndAttrOperator(
    Double3CompoundBaseAttrOperator[DWorldUpVectorEndPlugOperator]
):
    __slots__ = ()

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DWorldUpVectorEndField(
    Double3CompoundBaseField[DWorldUpVectorEndAttrOperator, DWorldUpVectorEndPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DWorldUpVectorEndAttrOperator
    PLUG_CLS = DWorldUpVectorEndPlugOperator

    dWorldUpVectorEndX = DoubleField(default_value=0.0)
    dwvx = dWorldUpVectorEndX

    dWorldUpVectorEndY = DoubleField(default_value=1.0)
    dwvy = dWorldUpVectorEndY

    dWorldUpVectorEndZ = DoubleField(default_value=0.0)
    dwvz = dWorldUpVectorEndZ


class DTwistStartEndPlugOperator(
    Double2CompoundBasePlugOperator["DTwistStartEndAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dTwistStart", "dtst"),
        ("dTwistEnd", "dten"),
    )

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistStartEndAttrOperator(
    Double2CompoundBaseAttrOperator[DTwistStartEndPlugOperator]
):
    __slots__ = ()

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistStartEndField(
    Double2CompoundBaseField[DTwistStartEndAttrOperator, DTwistStartEndPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistStartEndAttrOperator
    PLUG_CLS = DTwistStartEndPlugOperator

    dTwistStart = DoubleField(default_value=0.0)
    dtst = dTwistStart

    dTwistEnd = DoubleField(default_value=0.0)
    dten = dTwistEnd


class DTwistRampPlugOperator(
    Float3CompoundBasePlugOperator["DTwistRampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dTwistRampR", "dtrr"),
        ("dTwistRampG", "dtrg"),
        ("dTwistRampB", "dtrb"),
    )

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB


class DTwistRampAttrOperator(
    Float3CompoundBaseAttrOperator[DTwistRampPlugOperator]
):
    __slots__ = ()

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB


class DTwistRampField(
    Float3CompoundBaseField[DTwistRampAttrOperator, DTwistRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DTwistRampAttrOperator
    PLUG_CLS = DTwistRampPlugOperator

    dTwistRampR = FloatField(default_value=0.0)
    dtrr = dTwistRampR

    dTwistRampG = FloatField(default_value=0.0)
    dtrg = dTwistRampG

    dTwistRampB = FloatField(default_value=0.0)
    dtrb = dTwistRampB
