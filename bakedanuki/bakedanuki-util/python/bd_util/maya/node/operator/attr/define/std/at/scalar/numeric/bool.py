# coding: utf-8
from typing import Any

# maya
from maya.api import OpenMaya as om

# self
from .......... import logger as u_logger
from ._base import (
    NumericBaseAttrOperator,
    NumericBasePlugOperator,
    NumericBaseField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class BoolPlugOperator(NumericBasePlugOperator["BoolAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> bool:
        """boolプラグの現在値を取得する。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asBool()

    # set
    def set(self, value: bool) -> None:
        """boolプラグへ値をModifierManager経由で設定する。

        Args:
            value: 設定する真偽値。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueBool(self.plug, value)

    # add
    def add_attr(self):
        self._add_attr_base(om.MFnNumericData.kBoolean)


class BoolAttrOperator(NumericBaseAttrOperator[BoolPlugOperator]):
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
    __slots__ = ()

    ATTR_CLS = BoolAttrOperator
    PLUG_CLS = BoolPlugOperator
