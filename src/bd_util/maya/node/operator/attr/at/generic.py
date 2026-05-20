# coding: utf-8
from .._core import Attr, Plug


class GenericPlug(Plug["GenericAttr"]):
    __slots__ = ("_data_handle",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._data_handle = None

    # get
    def _get_data_handle(self):
        # MDataHandle をキャッシュする
        if self._data_handle is None:
            self._data_handle = self.plug.asMDataHandle()

        return self._data_handle

    def get(self):
        raise NotImplementedError("GenericPlug does not support get operation")

    # set
    def set(self, value):
        raise NotImplementedError("GenericPlug does not support set operation")


class GenericAttr(Attr[GenericPlug]):
    __slots__ = ()

    ATTR_TYPE = "generic"
    PLUG_CLS = GenericPlug
