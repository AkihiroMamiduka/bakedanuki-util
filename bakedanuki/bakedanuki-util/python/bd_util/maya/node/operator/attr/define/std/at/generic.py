# coding: utf-8

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField


class GenericPlugOperator(PlugOperator["GenericAttrOperator"]):
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

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnGenericAttribute()
        self._fn_attr = fn_attr

        # アトリビュートを作成
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class GenericAttrOperator(AttrOperator[GenericPlugOperator]):
    __slots__ = ()

    ATTR_TYPE = "generic"


class GenericField(AttributeField[GenericAttrOperator, GenericPlugOperator]):
    __slots__ = ()

    ATTR_CLS = GenericAttrOperator
    PLUG_CLS = GenericPlugOperator
