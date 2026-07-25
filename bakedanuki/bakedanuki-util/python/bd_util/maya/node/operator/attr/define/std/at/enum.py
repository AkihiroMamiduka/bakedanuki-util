# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="EnumAttrOperator")

P = TypeVar("P", bound="EnumPlugOperator")


def _name_map_or_raise(
    name_map: dict[int, str] | None,
    type_name: str,
) -> dict[int, str]:
    if name_map is None:
        raise ValueError(f"{type_name}.NAME_MAP is not defined.")
    return name_map


def _name_by_index_from_name_map(
    name_map: dict[int, str],
    index: int,
) -> str:
    return name_map[index]


def _enum_full_name_from_name_map(name_map: dict[int, str]) -> str:
    return ":".join([f"{name}={index}" for index, name in name_map.items()])


def _index_by_name_from_name_map(
    name_map: dict[int, str],
    name: str,
) -> int:
    return {v: k for k, v in name_map.items()}[name]


class EnumPlugOperator(PlugOperator[A]):
    __slots__ = ("_fn_enum",)

    NAME_MAP: dict[int, str] | None = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._fn_enum: om.MFnEnumAttribute | None = None

    # get
    def get(self) -> int:
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asShort()

    def _get_fn_enum(self) -> om.MFnEnumAttribute:
        # MFnEnumAttribute をキャッシュする
        if self._fn_enum is None:
            self._fn_enum = om.MFnEnumAttribute(self.plug.attribute())
        return self._fn_enum

    @property
    def _active_name_map(self) -> dict[int, str]:
        name_map = self.NAME_MAP
        if name_map is None:
            name_map = self._oprt_attr.NAME_MAP
        return _name_map_or_raise(name_map, type(self).__name__)

    # name
    def name_by_index(self, index: int) -> str:
        return _name_by_index_from_name_map(self._active_name_map, index)

    def enum_full_name(self) -> str:
        return _enum_full_name_from_name_map(self._active_name_map)

    # index
    def index_by_name(self, name: str) -> int:
        return _index_by_name_from_name_map(self._active_name_map, name)

    # set
    def set(self, value: int):
        self._node._dg_mod.newPlugValueShort(self.plug, value)

    @property
    def keyframe(self):
        return self._get_keyframe_manager()

    # add
    def add_attr(self):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # アトリビュートを作成
        fn_attr = om.MFnEnumAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)

        # NAME_MAP からフィールドを追加
        for index, name in self._active_name_map.items():
            fn_attr.addField(name, index)


class EnumAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "enum"

    NAME_MAP: dict[int, str] | None = None

    def __init__(
        self,
        **kwargs,
    ):
        if self.NAME_MAP is not None:
            kwargs["enum_name"] = self.enum_full_name()
        super().__init__(**kwargs)

    @property
    def _active_name_map(self) -> dict[int, str]:
        return _name_map_or_raise(self.NAME_MAP, type(self).__name__)

    # name
    def name_by_index(self, index: int) -> str:
        return _name_by_index_from_name_map(self._active_name_map, index)

    def enum_full_name(self) -> str:
        if self.NAME_MAP is None:
            return ""
        return _enum_full_name_from_name_map(self.NAME_MAP)

    # index
    def index_by_name(self, name: str) -> int:
        return _index_by_name_from_name_map(self._active_name_map, name)


class EnumField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)
