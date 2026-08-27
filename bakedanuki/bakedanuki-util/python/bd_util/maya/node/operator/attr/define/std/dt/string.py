# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from ._core import (
    DataTypeAttrOperator,
    DataTypePlugOperator,
    DataTypeField,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class DataStringPlugOperator(DataTypePlugOperator["DataStringAttrOperator"]):
    __slots__ = ()

    # get
    def get(self) -> str:
        """string dataプラグの現在値を文字列で取得する。"""
        return self.plug.asString()

    # set
    def set(self, value: str) -> None:
        """string dataプラグへ文字列をModifierManager経由で設定する。

        Args:
            value: 設定する文字列。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        self._node.modifier_manager.dg_mod.newPlugValueString(self.plug, value)

    def set_direct(self, value: str):
        """
        MPlug に値を直接セットする
            その為、modifier.undoIt() 非対応です

        Args:
            value (str): セットする文字列
        """
        self.plug.setString(value)

    @staticmethod
    def _create_default_object(value: object) -> om.MObject:
        if not isinstance(value, str):
            raise TypeError(
                "DataString default_value must be str; "
                f"got {type(value).__name__}."
            )
        return om.MFnStringData().create(value)

    # add
    def add_attr(self):
        self._add_attr_base(
            om.MFnData.kString,
            default_object_factory=self._create_default_object,
        )


class DataStringAttrOperator(DataTypeAttrOperator[DataStringPlugOperator]):
    __slots__ = ()

    DATA_TYPE = "string"


class DataStringField(
    DataTypeField[DataStringAttrOperator, DataStringPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DataStringAttrOperator
    PLUG_CLS = DataStringPlugOperator
