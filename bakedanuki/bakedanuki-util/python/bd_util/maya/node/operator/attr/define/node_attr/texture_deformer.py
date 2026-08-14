# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Long3CompoundBaseAttrOperator,
    Long3CompoundBasePlugOperator,
    Long3CompoundBaseField,
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
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


class TexturePlugOperator(
    Float3CompoundBasePlugOperator["TextureAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("textureR", "tr"),
        ("textureG", "tg"),
        ("textureB", "tb"),
    )

    textureR = FloatField(default_value=0.0)
    tr = textureR

    textureG = FloatField(default_value=0.0)
    tg = textureG

    textureB = FloatField(default_value=0.0)
    tb = textureB


class TextureAttrOperator(Float3CompoundBaseAttrOperator[TexturePlugOperator]):
    __slots__ = ()

    textureR = FloatField(default_value=0.0)
    tr = textureR

    textureG = FloatField(default_value=0.0)
    tg = textureG

    textureB = FloatField(default_value=0.0)
    tb = textureB


class TextureField(
    Float3CompoundBaseField[TextureAttrOperator, TexturePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureAttrOperator
    PLUG_CLS = TexturePlugOperator

    textureR = FloatField(default_value=0.0)
    tr = textureR

    textureG = FloatField(default_value=0.0)
    tg = textureG

    textureB = FloatField(default_value=0.0)
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

    vectorStrengthX = DoubleLinearField(default_value=1.0)
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField(default_value=1.0)
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField(default_value=1.0)
    vsz = vectorStrengthZ


class VectorStrengthAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VectorStrengthPlugOperator]
):
    __slots__ = ()

    vectorStrengthX = DoubleLinearField(default_value=1.0)
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField(default_value=1.0)
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField(default_value=1.0)
    vsz = vectorStrengthZ


class VectorStrengthField(
    DoubleLinear3CompoundBaseField[
        VectorStrengthAttrOperator, VectorStrengthPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VectorStrengthAttrOperator
    PLUG_CLS = VectorStrengthPlugOperator

    vectorStrengthX = DoubleLinearField(default_value=1.0)
    vsx = vectorStrengthX

    vectorStrengthY = DoubleLinearField(default_value=1.0)
    vsy = vectorStrengthY

    vectorStrengthZ = DoubleLinearField(default_value=1.0)
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

    vectorOffsetX = DoubleLinearField(default_value=0.0)
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField(default_value=0.0)
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField(default_value=0.0)
    voz = vectorOffsetZ


class VectorOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[VectorOffsetPlugOperator]
):
    __slots__ = ()

    vectorOffsetX = DoubleLinearField(default_value=0.0)
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField(default_value=0.0)
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField(default_value=0.0)
    voz = vectorOffsetZ


class VectorOffsetField(
    DoubleLinear3CompoundBaseField[
        VectorOffsetAttrOperator, VectorOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = VectorOffsetAttrOperator
    PLUG_CLS = VectorOffsetPlugOperator

    vectorOffsetX = DoubleLinearField(default_value=0.0)
    vox = vectorOffsetX

    vectorOffsetY = DoubleLinearField(default_value=0.0)
    voy = vectorOffsetY

    vectorOffsetZ = DoubleLinearField(default_value=0.0)
    voz = vectorOffsetZ
