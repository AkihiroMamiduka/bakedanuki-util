# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class MColourPlugOperator(
    Float3CompoundBasePlugOperator["MColourAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mColourR", "mcr"),
        ("mColourG", "mcg"),
        ("mColourB", "mcb"),
    )

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourAttrOperator(
    Float3CompoundBaseAttrOperator[MColourPlugOperator]
):
    __slots__ = ()

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class MColourField(
    Float3CompoundBaseField[MColourAttrOperator, MColourPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MColourAttrOperator
    PLUG_CLS = MColourPlugOperator

    mColourR = FloatField()
    mcr = mColourR

    mColourG = FloatField()
    mcg = mColourG

    mColourB = FloatField()
    mcb = mColourB


class FalloffObjectPlugOperator(
    Float3CompoundBasePlugOperator["FalloffObjectAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falloffObjectX", "fallObjx"),
        ("falloffObjectY", "fallObjy"),
        ("falloffObjectZ", "fallObjz"),
    )

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectAttrOperator(
    Float3CompoundBaseAttrOperator[FalloffObjectPlugOperator]
):
    __slots__ = ()

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class FalloffObjectField(
    Float3CompoundBaseField[FalloffObjectAttrOperator, FalloffObjectPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalloffObjectAttrOperator
    PLUG_CLS = FalloffObjectPlugOperator

    falloffObjectX = FloatField()
    fallObjx = falloffObjectX

    falloffObjectY = FloatField()
    fallObjy = falloffObjectY

    falloffObjectZ = FloatField()
    fallObjz = falloffObjectZ


class LowClampPlugOperator(
    Float3CompoundBasePlugOperator["LowClampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lowClamp0", "lcl0"),
        ("lowClamp1", "lcl1"),
        ("lowClamp2", "lcl2"),
    )

    lowClamp0 = FloatField()
    lcl0 = lowClamp0

    lowClamp1 = FloatField()
    lcl1 = lowClamp1

    lowClamp2 = FloatField()
    lcl2 = lowClamp2


class LowClampAttrOperator(
    Float3CompoundBaseAttrOperator[LowClampPlugOperator]
):
    __slots__ = ()

    lowClamp0 = FloatField()
    lcl0 = lowClamp0

    lowClamp1 = FloatField()
    lcl1 = lowClamp1

    lowClamp2 = FloatField()
    lcl2 = lowClamp2


class LowClampField(
    Float3CompoundBaseField[LowClampAttrOperator, LowClampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LowClampAttrOperator
    PLUG_CLS = LowClampPlugOperator

    lowClamp0 = FloatField()
    lcl0 = lowClamp0

    lowClamp1 = FloatField()
    lcl1 = lowClamp1

    lowClamp2 = FloatField()
    lcl2 = lowClamp2


class HighClampPlugOperator(
    Float3CompoundBasePlugOperator["HighClampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("highClamp0", "hcl0"),
        ("highClamp1", "hcl1"),
        ("highClamp2", "hcl2"),
    )

    highClamp0 = FloatField()
    hcl0 = highClamp0

    highClamp1 = FloatField()
    hcl1 = highClamp1

    highClamp2 = FloatField()
    hcl2 = highClamp2


class HighClampAttrOperator(
    Float3CompoundBaseAttrOperator[HighClampPlugOperator]
):
    __slots__ = ()

    highClamp0 = FloatField()
    hcl0 = highClamp0

    highClamp1 = FloatField()
    hcl1 = highClamp1

    highClamp2 = FloatField()
    hcl2 = highClamp2


class HighClampField(
    Float3CompoundBaseField[HighClampAttrOperator, HighClampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HighClampAttrOperator
    PLUG_CLS = HighClampPlugOperator

    highClamp0 = FloatField()
    hcl0 = highClamp0

    highClamp1 = FloatField()
    hcl1 = highClamp1

    highClamp2 = FloatField()
    hcl2 = highClamp2


class ReorderDistancePointPlugOperator(
    Float3CompoundBasePlugOperator["ReorderDistancePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("reorderDistancePointX", "reorderDistancePointx"),
        ("reorderDistancePointY", "reorderDistancePointy"),
        ("reorderDistancePointZ", "reorderDistancePointz"),
    )

    reorderDistancePointX = FloatField()
    reorderDistancePointx = reorderDistancePointX

    reorderDistancePointY = FloatField()
    reorderDistancePointy = reorderDistancePointY

    reorderDistancePointZ = FloatField()
    reorderDistancePointz = reorderDistancePointZ


class ReorderDistancePointAttrOperator(
    Float3CompoundBaseAttrOperator[ReorderDistancePointPlugOperator]
):
    __slots__ = ()

    reorderDistancePointX = FloatField()
    reorderDistancePointx = reorderDistancePointX

    reorderDistancePointY = FloatField()
    reorderDistancePointy = reorderDistancePointY

    reorderDistancePointZ = FloatField()
    reorderDistancePointz = reorderDistancePointZ


class ReorderDistancePointField(
    Float3CompoundBaseField[ReorderDistancePointAttrOperator, ReorderDistancePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReorderDistancePointAttrOperator
    PLUG_CLS = ReorderDistancePointPlugOperator

    reorderDistancePointX = FloatField()
    reorderDistancePointx = reorderDistancePointX

    reorderDistancePointY = FloatField()
    reorderDistancePointy = reorderDistancePointY

    reorderDistancePointZ = FloatField()
    reorderDistancePointz = reorderDistancePointZ


class OffsetsPlugOperator(
    Float3CompoundBasePlugOperator["OffsetsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsets0", "off0"),
        ("offsets1", "off1"),
        ("offsets2", "off2"),
    )

    offsets0 = FloatField()
    off0 = offsets0

    offsets1 = FloatField()
    off1 = offsets1

    offsets2 = FloatField()
    off2 = offsets2


class OffsetsAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetsPlugOperator]
):
    __slots__ = ()

    offsets0 = FloatField()
    off0 = offsets0

    offsets1 = FloatField()
    off1 = offsets1

    offsets2 = FloatField()
    off2 = offsets2


class OffsetsField(
    Float3CompoundBaseField[OffsetsAttrOperator, OffsetsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetsAttrOperator
    PLUG_CLS = OffsetsPlugOperator

    offsets0 = FloatField()
    off0 = offsets0

    offsets1 = FloatField()
    off1 = offsets1

    offsets2 = FloatField()
    off2 = offsets2


class RayDirectionPlugOperator(
    Float3CompoundBasePlugOperator["RayDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rayDirection0", "rayDirection0"),
        ("rayDirection1", "rayDirection1"),
        ("rayDirection2", "rayDirection2"),
    )

    rayDirection0 = FloatField()

    rayDirection1 = FloatField()

    rayDirection2 = FloatField()


class RayDirectionAttrOperator(
    Float3CompoundBaseAttrOperator[RayDirectionPlugOperator]
):
    __slots__ = ()

    rayDirection0 = FloatField()

    rayDirection1 = FloatField()

    rayDirection2 = FloatField()


class RayDirectionField(
    Float3CompoundBaseField[RayDirectionAttrOperator, RayDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RayDirectionAttrOperator
    PLUG_CLS = RayDirectionPlugOperator

    rayDirection0 = FloatField()

    rayDirection1 = FloatField()

    rayDirection2 = FloatField()


class OffsetInputsPlugOperator(
    CompoundPlugOperator["OffsetInputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionOffset", "positionOffset"),
        ("rotationOffset", "rotationOffset"),
        ("scaleOffset", "scaleOffset"),
    )

    positionOffset = Float3Field()

    rotationOffset = Double3Field()

    scaleOffset = Float3Field()


class OffsetInputsAttrOperator(
    CompoundAttrOperator[OffsetInputsPlugOperator]
):
    __slots__ = ()

    positionOffset = Float3Field()

    rotationOffset = Double3Field()

    scaleOffset = Float3Field()


class OffsetInputsField(
    CompoundField[OffsetInputsAttrOperator, OffsetInputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetInputsAttrOperator
    PLUG_CLS = OffsetInputsPlugOperator

    positionOffset = Float3Field()

    rotationOffset = Double3Field()

    scaleOffset = Float3Field()


class CentreOfRotationPlugOperator(
    Float3CompoundBasePlugOperator["CentreOfRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centreOfRotation0", "centreOfRotation0"),
        ("centreOfRotation1", "centreOfRotation1"),
        ("centreOfRotation2", "centreOfRotation2"),
    )

    centreOfRotation0 = FloatField()

    centreOfRotation1 = FloatField()

    centreOfRotation2 = FloatField()


class CentreOfRotationAttrOperator(
    Float3CompoundBaseAttrOperator[CentreOfRotationPlugOperator]
):
    __slots__ = ()

    centreOfRotation0 = FloatField()

    centreOfRotation1 = FloatField()

    centreOfRotation2 = FloatField()


class CentreOfRotationField(
    Float3CompoundBaseField[CentreOfRotationAttrOperator, CentreOfRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CentreOfRotationAttrOperator
    PLUG_CLS = CentreOfRotationPlugOperator

    centreOfRotation0 = FloatField()

    centreOfRotation1 = FloatField()

    centreOfRotation2 = FloatField()
