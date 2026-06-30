# coding: utf-8
from ._core import DG
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField


class HIKRetargeterNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKRetargeterNode"

    SNS = BoolField()

    referenceGX = MatrixField()

    InputCharacterDefinitionSrc = TypedField()

    InputCharacterDefinitionDst = TypedField()

    InputCharacterState = TypedField()

    InputSrcPropertySetState = TypedField()

    InputDstPropertySetState = TypedField()

    OutputCharacterState = TypedField()
