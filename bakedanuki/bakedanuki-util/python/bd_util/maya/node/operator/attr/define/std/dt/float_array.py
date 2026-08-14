# coding: utf-8
from typing import Protocol, cast

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from .base.array_base import (
    DataArrayBaseAttrOperator,
    DataArrayBasePlugOperator,
    DataArrayBaseField,
)


class _SetFloatArrayAttr(Protocol):
    def __call__(
        self,
        plug_name: str,
        value: list[float],
        *,
        type: str,
    ) -> object: ...


_set_float_array_attr = cast(_SetFloatArrayAttr, cmds.setAttr)


class DataFloatArrayPlugOperator(
    DataArrayBasePlugOperator["DataFloatArrayAttrOperator"]
):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        plug_name = self.plug.name()
        if not cmds.objExists(plug_name):
            return []

        values = cast(object, cmds.getAttr(plug_name))
        if values is None:
            return []
        if not isinstance(values, (list, tuple)):
            raise TypeError(
                f"Expected float array value from {plug_name}: {values!r}"
            )

        result: list[float] = []
        array_values = cast(list[object] | tuple[object, ...], values)
        for value in array_values:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Expected float array value from {plug_name}: {values!r}"
                )
            result.append(float(value))
        return result

    # set
    def set_direct(self, value: list[float]) -> None:
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (list[float]): セットする値のリスト
        """
        plug_name = self.plug.name()
        if not cmds.objExists(plug_name):
            raise RuntimeError(
                "FloatArray plug must exist in the scene before "
                f"set_direct() is called: {plug_name!r}"
            )
        _set_float_array_attr(plug_name, value, type="floatArray")

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnData.kFloatArray)


class DataFloatArrayAttrOperator(
    DataArrayBaseAttrOperator[DataFloatArrayPlugOperator]
):
    __slots__ = ()

    DATA_TYPE = "floatArray"


class DataFloatArrayField(
    DataArrayBaseField[DataFloatArrayAttrOperator, DataFloatArrayPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataFloatArrayAttrOperator
    PLUG_CLS = DataFloatArrayPlugOperator
