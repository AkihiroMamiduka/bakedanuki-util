# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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
    wl.w = weights


class WeightListAttrOperator(
    CompoundAttrOperator[WeightListPlugOperator]
):
    __slots__ = ()

    weights = FloatField()
    wl.w = weights


class WeightListField(
    CompoundField[WeightListAttrOperator, WeightListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WeightListAttrOperator
    PLUG_CLS = WeightListPlugOperator


class TexturePlugOperator(
    Float3CompoundBasePlugOperator["TextureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureR", "tr"),
        ("textureG", "tg"),
        ("textureB", "tb"),
    )

    textureR = FloatField()
    tr = textureR

    textureG = FloatField()
    tg = textureG

    textureB = FloatField()
    tb = textureB


class TextureAttrOperator(
    Float3CompoundBaseAttrOperator[TexturePlugOperator]
):
    __slots__ = ()

    textureR = FloatField()
    tr = textureR

    textureG = FloatField()
    tg = textureG

    textureB = FloatField()
    tb = textureB


class TextureField(
    Float3CompoundBaseField[TextureAttrOperator, TexturePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureAttrOperator
    PLUG_CLS = TexturePlugOperator

    textureR = FloatField()
    tr = textureR

    textureG = FloatField()
    tg = textureG

    textureB = FloatField()
    tb = textureB


class VectorStrengthPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["VectorStrengthAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorStrengthX", "vsx"),
        ("vectorStrengthY", "vsy"),
        ("vectorStrengthZ", "vsz"),
    )

    vectorStrengthX = DoubleLinearField()
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField()
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField()
    vsz = vectorStrengthZ


class VectorStrengthAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VectorStrengthPlugOperator]
):
    __slots__ = ()

    vectorStrengthX = DoubleLinearField()
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField()
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField()
    vsz = vectorStrengthZ


class VectorStrengthField(
    DoubleLinear3CompoundBaseField[VectorStrengthAttrOperator, VectorStrengthPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorStrengthAttrOperator
    PLUG_CLS = VectorStrengthPlugOperator

    vectorStrengthX = DoubleLinearField()
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField()
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField()
    vsz = vectorStrengthZ


class VectorOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["VectorOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vectorOffsetX", "vox"),
        ("vectorOffsetY", "voy"),
        ("vectorOffsetZ", "voz"),
    )

    vectorOffsetX = DoubleLinearField()
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField()
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField()
    voz = vectorOffsetZ


class VectorOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VectorOffsetPlugOperator]
):
    __slots__ = ()

    vectorOffsetX = DoubleLinearField()
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField()
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField()
    voz = vectorOffsetZ


class VectorOffsetField(
    DoubleLinear3CompoundBaseField[VectorOffsetAttrOperator, VectorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VectorOffsetAttrOperator
    PLUG_CLS = VectorOffsetPlugOperator

    vectorOffsetX = DoubleLinearField()
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField()
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField()
    voz = vectorOffsetZ
