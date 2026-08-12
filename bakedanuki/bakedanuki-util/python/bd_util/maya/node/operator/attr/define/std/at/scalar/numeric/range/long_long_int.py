# coding: utf-8
from collections.abc import Callable
from typing import Any, cast

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ...........py.error import UnsupportedOperationError
from ._base import (
    NumericRangeBaseAttrOperator,
    NumericRangeBasePlugOperator,
    NumericRangeBaseField,
)

_set_int_attr = cast(Callable[[str, int], object], cmds.setAttr)


class LongLongIntPlugOperator(
    NumericRangeBasePlugOperator["LongLongIntAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> int:
        plug = self.plug
        plug_name = plug.name()
        if not cmds.objExists(plug_name):
            return int(plug.asDouble())

        value = cmds.getAttr(plug_name)
        if not isinstance(value, int):
            raise TypeError(f"Expected int value from {plug_name}: {value!r}")
        return value

    # set
    def set(self, value: int) -> None:
        plug = self.plug

        def set_value() -> None:
            plug_name = plug.name()
            if not cmds.objExists(plug_name):
                raise RuntimeError(
                    "LongLongInt plug is not available when the queued "
                    f"set command executes: {plug_name!r}"
                )
            _set_int_attr(plug_name, value)

        self._node.modifier_manager.dg_mod.pythonCommandToExecute(set_value)

    def set_direct(self, value: int) -> None:
        plug_name = self.plug.name()
        if not cmds.objExists(plug_name):
            raise RuntimeError(
                "LongLongInt plug must exist in the scene before "
                f"set_direct() is called: {plug_name!r}"
            )
        _set_int_attr(plug_name, value)

    def set_min(self, value: int | float) -> None:
        raise UnsupportedOperationError(
            "Setting min value is not supported for LongLongInt attributes."
        )

    def set_max(self, value: int | float) -> None:
        raise UnsupportedOperationError(
            "Setting max value is not supported for LongLongInt attributes."
        )

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kInt64)


class LongLongIntAttrOperator(
    NumericRangeBaseAttrOperator[LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_TYPE = "long long int"

    def __init__(
        self,
        *args: Any,
        default_value: int | None = None,
        **kwargs: Any,
    ) -> None:
        # デフォルト値
        if default_value is None:
            default_value = 0
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class LongLongIntField(
    NumericRangeBaseField[LongLongIntAttrOperator, LongLongIntPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LongLongIntAttrOperator
    PLUG_CLS = LongLongIntPlugOperator
