# coding: utf-8
from typing import Any

from maya.api import OpenMaya as om

from .......... import logger as u_logger
from ._base import (
    NumericBaseAttrOperator,
    NumericBasePlugOperator,
    NumericBaseField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class BoolPlugOperator(NumericBasePlugOperator["BoolAttrOperator"]):
    """`bool` 属性プラグを操作する。"""

    __slots__ = ()

    def get(self) -> bool:
        """boolプラグの現在値を取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asBool()

    def set(self, value: bool) -> None:
        """boolプラグへ値をModifierManager経由で設定する。

        変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。

        Args:
            value: 設定する真偽値。
        """
        self._node.modifier_manager.dg_mod.newPlugValueBool(self.plug, value)

    def add_attr(self):
        """bool 属性がなければ、ノードへ即時追加する。"""
        self._add_attr_base(om.MFnNumericData.kBoolean)


class BoolAttrOperator(NumericBaseAttrOperator[BoolPlugOperator]):
    """`bool` 属性の定義を保持する。"""

    __slots__ = ()

    ATTR_TYPE = "bool"

    def __init__(
        self,
        *args: Any,
        default_value: bool | None = None,
        **kwargs: Any,
    ) -> None:
        # デフォルト値
        if default_value is None:
            default_value = True
        super().__init__(
            *args,
            default_value=default_value,
            **kwargs,
        )


class BoolField(NumericBaseField[BoolAttrOperator, BoolPlugOperator]):
    """`bool` 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = BoolAttrOperator
    PLUG_CLS = BoolPlugOperator
