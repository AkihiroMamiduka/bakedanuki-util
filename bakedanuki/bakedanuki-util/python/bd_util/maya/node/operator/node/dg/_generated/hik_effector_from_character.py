# coding: utf-8
from .._core import DG
from ....attr.define.std.at.typed import TypedField


class _GeneratedHIKEffectorFromCharacter(DG):
    __slots__ = ()

    NODE_TYPE = "HIKEffectorFromCharacter"

    InputCharacterDefinition = TypedField()

    InputCharacterState = TypedField()

    InputPropertySetState = TypedField()

    OutputEffectorState = TypedField()
