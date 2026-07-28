# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


class SolverModeEnumPlugOperator(
    EnumPlugOperator["SolverModeEnumAttrOperator"]
):
    __slots__ = ()

    FULL_BODY = 0
    BODY_PART = 1
    SELECTION = 2


class SolverModeEnumAttrOperator(EnumAttrOperator[SolverModeEnumPlugOperator]):
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


class GeneratedHIKSolverNode(DG):
    __slots__ = ()

    NODE_TYPE = "HIKSolverNode"

    InputActive = BoolField(default_value=True)

    InputStance = BoolField(default_value=False)

    InputRelaxStance = BoolField(default_value=False)

    InputStanceMask = LongField(default_value=0)

    LowLOD = BoolField(default_value=False)

    SNS = BoolField(default_value=False)

    InputCharacterDefinition = TypedField()

    InputCharacterState = TypedField()

    InputEffectorState = TypedField()

    InputEffectorStateNoAux = TypedField()

    InputPropertySetState = TypedField()

    SolverMode = SolverModeEnumField(default_value=0)

    OutputCharacterState = TypedField()

    doubleEvalCharacterState = TypedField()
    decs = doubleEvalCharacterState
