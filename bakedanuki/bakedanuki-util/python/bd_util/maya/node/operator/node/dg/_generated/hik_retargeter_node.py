# coding: utf-8
from .._core import DG
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class _GeneratedHIKRetargeterNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKRetargeterNode"

    SNS = BoolField(default_value=False)

    referenceGX = MatrixField()

    InputCharacterDefinitionSrc = TypedField()

    InputCharacterDefinitionDst = TypedField()

    InputCharacterState = TypedField()

    InputSrcPropertySetState = TypedField()

    InputDstPropertySetState = TypedField()

    OutputCharacterState = TypedField()
