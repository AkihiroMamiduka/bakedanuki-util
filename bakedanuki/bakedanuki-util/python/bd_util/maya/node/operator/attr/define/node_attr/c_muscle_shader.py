# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    PLANAR = 0
    CYLINDRICAL = 1
    CURVES = 2


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    PLANAR = 0
    CYLINDRICAL = 1
    CURVES = 2

    NAME_MAP = {
        PLANAR: "planar",
        CYLINDRICAL: "cylindrical",
        CURVES: "curves",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class PushModeEnumPlugOperator(EnumPlugOperator["PushModeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 0
    GIZMO = 1


class PushModeEnumAttrOperator(EnumAttrOperator[PushModeEnumPlugOperator]):
    __slots__ = ()

    NORMAL = 0
    GIZMO = 1

    NAME_MAP = {
        NORMAL: "normal",
        GIZMO: "gizmo",
    }


class PushModeEnumField(
    EnumField[PushModeEnumAttrOperator, PushModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PushModeEnumAttrOperator
    PLUG_CLS = PushModeEnumPlugOperator


class CombineModeEnumPlugOperator(EnumPlugOperator["CombineModeEnumAttrOperator"]):
    __slots__ = ()

    MAX = 0
    ADD = 1


class CombineModeEnumAttrOperator(EnumAttrOperator[CombineModeEnumPlugOperator]):
    __slots__ = ()

    MAX = 0
    ADD = 1

    NAME_MAP = {
        MAX: "max",
        ADD: "add",
    }


class CombineModeEnumField(
    EnumField[CombineModeEnumAttrOperator, CombineModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CombineModeEnumAttrOperator
    PLUG_CLS = CombineModeEnumPlugOperator


class PointWorldPlugOperator(
    Float3CompoundBasePlugOperator["PointWorldAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointWorldX", "pwx"),
        ("pointWorldY", "pwy"),
        ("pointWorldZ", "pwz"),
    )

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldAttrOperator(
    Float3CompoundBaseAttrOperator[PointWorldPlugOperator]
):
    __slots__ = ()

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class PointWorldField(
    Float3CompoundBaseField[PointWorldAttrOperator, PointWorldPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointWorldAttrOperator
    PLUG_CLS = PointWorldPlugOperator

    pointWorldX = FloatField(default_value=0.0)
    pwx = pointWorldX

    pointWorldY = FloatField(default_value=0.0)
    pwy = pointWorldY

    pointWorldZ = FloatField(default_value=0.0)
    pwz = pointWorldZ


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "u"),
        ("vCoord", "v"),
    )

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class VertexUvOnePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvOneAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvOneU", "t1u"),
        ("vertexUvOneV", "t1v"),
    )

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvOnePlugOperator]
):
    __slots__ = ()

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvOneField(
    Float2CompoundBaseField[VertexUvOneAttrOperator, VertexUvOnePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvOneAttrOperator
    PLUG_CLS = VertexUvOnePlugOperator

    vertexUvOneU = FloatField(default_value=0.0)
    t1u = vertexUvOneU

    vertexUvOneV = FloatField(default_value=0.0)
    t1v = vertexUvOneV


class VertexUvTwoPlugOperator(
    Float2CompoundBasePlugOperator["VertexUvTwoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvTwoU", "t2u"),
        ("vertexUvTwoV", "t2v"),
    )

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvTwoPlugOperator]
):
    __slots__ = ()

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvTwoField(
    Float2CompoundBaseField[VertexUvTwoAttrOperator, VertexUvTwoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvTwoAttrOperator
    PLUG_CLS = VertexUvTwoPlugOperator

    vertexUvTwoU = FloatField(default_value=0.0)
    t2u = vertexUvTwoU

    vertexUvTwoV = FloatField(default_value=0.0)
    t2v = vertexUvTwoV


class VertexUvThreePlugOperator(
    Float2CompoundBasePlugOperator["VertexUvThreeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vertexUvThreeU", "t3u"),
        ("vertexUvThreeV", "t3v"),
    )

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeAttrOperator(
    Float2CompoundBaseAttrOperator[VertexUvThreePlugOperator]
):
    __slots__ = ()

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class VertexUvThreeField(
    Float2CompoundBaseField[VertexUvThreeAttrOperator, VertexUvThreePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexUvThreeAttrOperator
    PLUG_CLS = VertexUvThreePlugOperator

    vertexUvThreeU = FloatField(default_value=0.0)
    t3u = vertexUvThreeU

    vertexUvThreeV = FloatField(default_value=0.0)
    t3v = vertexUvThreeV


class ImagePlugOperator(
    Float3CompoundBasePlugOperator["ImageAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imageR", "ir"),
        ("imageG", "ig"),
        ("imageB", "ib"),
    )

    imageR = FloatField(default_value=0.0)
    ir = imageR

    imageG = FloatField(default_value=0.0)
    ig = imageG

    imageB = FloatField(default_value=0.0)
    ib = imageB


class ImageAttrOperator(
    Float3CompoundBaseAttrOperator[ImagePlugOperator]
):
    __slots__ = ()

    imageR = FloatField(default_value=0.0)
    ir = imageR

    imageG = FloatField(default_value=0.0)
    ig = imageG

    imageB = FloatField(default_value=0.0)
    ib = imageB


class ImageField(
    Float3CompoundBaseField[ImageAttrOperator, ImagePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageAttrOperator
    PLUG_CLS = ImagePlugOperator

    imageR = FloatField(default_value=0.0)
    ir = imageR

    imageG = FloatField(default_value=0.0)
    ig = imageG

    imageB = FloatField(default_value=0.0)
    ib = imageB


class DispDataPlugOperator(
    CompoundPlugOperator["DispDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("muscleMatrix", "mm"),
        ("curves", "crv"),
        ("mode", "md"),
        ("length", "len"),
        ("sizeRadius", "siz"),
        ("amplitude", "amp"),
        ("falloff", "fal"),
        ("pushMode", "pmd"),
        ("combineMode", "cmd"),
        ("shader", "sha"),
    )

    muscleMatrix = MatrixField()
    mm = muscleMatrix

    curves = GenericField(multi=True)
    crv = curves

    mode = ModeEnumField(default_value=0)
    md = mode

    length = FloatField(default_value=1.0)
    len = length

    sizeRadius = FloatField(default_value=0.5)
    siz = sizeRadius

    amplitude = FloatField(default_value=0.10000000149011612)
    amp = amplitude

    falloff = FloatField(default_value=0.5)
    fal = falloff

    pushMode = PushModeEnumField(default_value=0)
    pmd = pushMode

    combineMode = CombineModeEnumField(default_value=0)
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataAttrOperator(
    CompoundAttrOperator[DispDataPlugOperator]
):
    __slots__ = ()

    muscleMatrix = MatrixField()
    mm = muscleMatrix

    curves = GenericField(multi=True)
    crv = curves

    mode = ModeEnumField(default_value=0)
    md = mode

    length = FloatField(default_value=1.0)
    len = length

    sizeRadius = FloatField(default_value=0.5)
    siz = sizeRadius

    amplitude = FloatField(default_value=0.10000000149011612)
    amp = amplitude

    falloff = FloatField(default_value=0.5)
    fal = falloff

    pushMode = PushModeEnumField(default_value=0)
    pmd = pushMode

    combineMode = CombineModeEnumField(default_value=0)
    cmd = combineMode

    shader = MessageField()
    sha = shader


class DispDataField(
    CompoundField[DispDataAttrOperator, DispDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DispDataAttrOperator
    PLUG_CLS = DispDataPlugOperator

    muscleMatrix = MatrixField()
    mm = muscleMatrix

    curves = GenericField(multi=True)
    crv = curves

    mode = ModeEnumField(default_value=0)
    md = mode

    length = FloatField(default_value=1.0)
    len = length

    sizeRadius = FloatField(default_value=0.5)
    siz = sizeRadius

    amplitude = FloatField(default_value=0.10000000149011612)
    amp = amplitude

    falloff = FloatField(default_value=0.5)
    fal = falloff

    pushMode = PushModeEnumField(default_value=0)
    pmd = pushMode

    combineMode = CombineModeEnumField(default_value=0)
    cmd = combineMode

    shader = MessageField()
    sha = shader
