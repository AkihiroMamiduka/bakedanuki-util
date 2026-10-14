# coding: utf-8
"""Maya整数属性の型固有範囲とhard limitの検証。"""

from __future__ import annotations

from maya.api import OpenMaya as om

from ....ui import IntPresentation
from ....ui.binding.int._validation import require_int
from .int_plug_resolver import (
    IntPlugKind,
    MayaIntPlug,
    int_plug_kind,
    require_int_plug,
)

_TYPE_LIMITS: dict[IntPlugKind, tuple[int, int]] = {
    "byte": (0, 255),
    "short": (-(2**15), 2**15 - 1),
    "long": (-(2**31), 2**31 - 1),
}


def _maya_integer_bound(value: object, name: str) -> int:
    """Mayaがfloatで返す整数属性の境界を、精度検証後にintへ戻す。"""
    if type(value) is float:
        if not value.is_integer():
            raise ValueError(f"{name}は整数でなければなりません")
        return require_int(int(value), name)
    return require_int(value, name)


class IntPlugValue:
    """Maya整数Plugを精度変換せずMVVMの公開値へ橋渡しする。"""

    def __init__(self, plug: MayaIntPlug) -> None:
        """属性型を検証し、現在のMaya plugを保持する。"""
        operator = require_int_plug(plug)
        self.plug = operator.plug
        self.kind: IntPlugKind = int_plug_kind(self.plug)

    def read(self) -> int:
        """byteを符号反転させず、現在の実値を整数で返す。"""
        return require_int(self.plug.asInt())

    def to_ui(self, value: int) -> int:
        """復旧値を含め、暗黙変換せず32-bit整数として検証する。"""
        return require_int(value)

    def validate(self, value: int) -> int:
        """型固有範囲と現在のhard limitを変更前に検証する。"""
        value = self.to_ui(value)
        presentation = self.presentation
        if presentation.minimum is not None and value < presentation.minimum:
            raise ValueError("valueはMaya属性の下限未満です")
        if presentation.maximum is not None and value > presentation.maximum:
            raise ValueError("valueはMaya属性の上限を超えています")
        return value

    @property
    def presentation(self) -> IntPresentation:
        """型固有範囲とMaya属性のhard limitの共通部分を返す。"""
        lower, upper = _TYPE_LIMITS[self.kind]
        attribute = om.MFnNumericAttribute(self.plug.attribute())
        if attribute.hasMin():
            lower = max(
                lower, _maya_integer_bound(attribute.getMin(), "minimum")
            )
        if attribute.hasMax():
            upper = min(
                upper, _maya_integer_bound(attribute.getMax(), "maximum")
            )
        return IntPresentation(minimum=lower, maximum=upper)
