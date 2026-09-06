# coding: utf-8
from .._core import Transform
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.long import LongField


class SetupMethodEnumPlugOperator(
    EnumPlugOperator["SetupMethodEnumAttrOperator"]
):
    __slots__ = ()

    CYCLEFREE = 0
    NATIVE = 1


class SetupMethodEnumAttrOperator(
    EnumAttrOperator[SetupMethodEnumPlugOperator]
):
    __slots__ = ()

    CYCLEFREE = 0
    NATIVE = 1

    NAME_MAP = {
        CYCLEFREE: "cycleFree",
        NATIVE: "native",
    }


class SetupMethodEnumField(
    EnumField[SetupMethodEnumAttrOperator, SetupMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SetupMethodEnumAttrOperator
    PLUG_CLS = SetupMethodEnumPlugOperator


class GeneratedBifrostRiggingContainer(Transform):
    __slots__ = ()

    NODE_TYPE = "bifrostRiggingContainer"

    autoUpdate = BoolField(default_value=False)
    aud = autoUpdate

    setupMethod = SetupMethodEnumField(default_value=0)
    sm = setupMethod

    createControls = BoolField(default_value=True)
    cc = createControls

    createJoints = BoolField(default_value=True)
    cj = createJoints

    flattenControls = BoolField(default_value=False)
    fc = flattenControls

    flattenJoints = BoolField(default_value=False)
    fj = flattenJoints

    graphNodes = MessageField(multi=True, readable=False)
    gn = graphNodes

    setupHashes = LongField(multi=True, default_value=0)
    shs = setupHashes
