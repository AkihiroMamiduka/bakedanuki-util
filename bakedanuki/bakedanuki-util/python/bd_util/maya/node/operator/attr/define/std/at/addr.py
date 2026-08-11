# coding: utf-8
from typing import Any

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class AddrPlugOperator(PlugOperator["AddrAttrOperator"]):
    __slots__ = ("_data_handle",)

    _REQUIRED_CMDS_ADD_ATTR: bool = True

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._data_handle = None

    # get
    def get(self) -> int:
        return self._get_data_handle().asAddr()

    def _get_data_handle(self):
        # MDataHandle をキャッシュする
        if self._data_handle is None:
            self._data_handle = self.plug.asMDataHandle()

        return self._data_handle

    # set
    def set(self, value: int):
        """
        MDataHandle を使用して、値をセットする

        MPlug に直接セットする方法しかない為、undo 対応ができない点に注意。
        """

        data_handle = self._get_data_handle()

        # MDataHandle に値をセットし、plug に反映させる
        data_handle.setAddr(value)
        self.plug.setMDataHandle(data_handle)

    def add_attr(self, **kwargs):
        raise TypeError(
            "{}{}".format(
                "addr 属性は api.OpenMaya ではアトリビュートを作成できない為、 addAttr() できません。",
                "その為、 cmds_add_attr() を使用してください。",
            )
        )


class AddrAttrOperator(AttrOperator[AddrPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "addr"


class AddrField(AttributeField[AddrAttrOperator, AddrPlugOperator]):
    __slots__ = ()

    ATTR_CLS = AddrAttrOperator
    PLUG_CLS = AddrPlugOperator
