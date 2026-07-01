# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class SolverModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FULL_BODY = 0
    BODY_PART = 1
    SELECTION = 2


class SolverModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FULL_BODY = 0
    BODY_PART = 1
    SELECTION = 2

    NAME_MAP = {
        FULL_BODY: "Full Body",
        BODY_PART: "Body Part",
        SELECTION: "Selection",
    }


class SolverModeEnumField(
    EnumField[SolverModeEnumAttrOperator, SolverModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverModeEnumAttrOperator
    PLUG_CLS = SolverModeEnumPlugOperator


class HIKSolverNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKSolverNode"

    InputActive = BoolField()

    InputStance = BoolField()

    InputRelaxStance = BoolField()

    InputStanceMask = LongField()

    LowLOD = BoolField()

    SNS = BoolField()

    InputCharacterDefinition = TypedField()

    InputCharacterState = TypedField()

    InputEffectorState = TypedField()

    InputEffectorStateNoAux = TypedField()

    InputPropertySetState = TypedField()

    SolverMode = SolverModeEnumField()

    OutputCharacterState = TypedField()

    doubleEvalCharacterState = TypedField()
    decs = doubleEvalCharacterState
