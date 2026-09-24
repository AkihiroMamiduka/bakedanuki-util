# coding: utf-8
from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)

A = TypeVar("A", bound="EnumAttrOperator[Any]")

P = TypeVar("P", bound="EnumPlugOperator[Any]")


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


class EnumPlugOperator(ScalarBasePlugOperator[A]):
    """enum プラグの番号と表示名を扱う。"""

    __slots__ = ("_fn_enum",)

    NAME_MAP: dict[int, str] | None = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._fn_enum: om.MFnEnumAttribute | None = None

    def get(self) -> int:
        """現在選択されている項目の番号を返す。"""
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.asShort()

    def _get_fn_enum(self) -> om.MFnEnumAttribute:
        # 同じ属性の定義を繰り返し問い合わせないように保持する。
        fn_enum = self._fn_enum
        if fn_enum is None:
            fn_enum = om.MFnEnumAttribute(self.plug.attribute())
            self._fn_enum = fn_enum
        return fn_enum

    @property
    def _active_name_map(self) -> dict[int, str]:
        name_map = self.NAME_MAP
        if name_map is None:
            name_map = self._oprt_attr.NAME_MAP
        return _name_map_or_raise(name_map, type(self).__name__)

    def name_by_index(self, index: int) -> str:
        """項目番号に対応する表示名を返す。

        Args:
            index: 表示名を調べる項目番号。

        Raises:
            KeyError: 番号が定義されていない場合。
        """
        return _name_by_index_from_name_map(self._active_name_map, index)

    def enum_full_name(self) -> str:
        """`名前=番号` を `:` でつないだ Maya enum 定義を返す。"""
        return _enum_full_name_from_name_map(self._active_name_map)

    def index_by_name(self, name: str) -> int:
        """表示名に対応する項目番号を返す。

        Args:
            name: 項目の表示名。

        Raises:
            KeyError: 表示名が定義されていない場合。
        """
        return _index_by_name_from_name_map(self._active_name_map, name)

    def set(self, value: int) -> None:
        """項目番号の設定を ModifierManager に予約する。

        `ModifierManager.do_it_dg()` の実行時に反映される。

        Args:
            value: 設定する項目番号。
        """
        self._node.modifier_manager.dg_mod.newPlugValueShort(self.plug, value)

    def add_attr(self):
        """属性が未作成なら、定義済みの項目を持つ enum 属性を追加する。"""
        if self.exists():
            return

        # 共通オプションを付けた属性を作り、ノードへ登録する。
        fn_attr = om.MFnEnumAttribute()
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
        )
        self._apply_mfn_attr_options(fn_attr)

        self._node.fn_node.addAttribute(attr_obj)

        # 番号と表示名の対応を enum フィールドへ反映する。
        for index, name in self._active_name_map.items():
            fn_attr.addField(name, index)


class EnumAttrOperator(ScalarBaseAttrOperator[P]):
    """enum 属性の項目番号と表示名を定義する。"""

    __slots__ = ()

    ATTR_TYPE = "enum"

    NAME_MAP: dict[int, str] | None = None

    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        if self.NAME_MAP is not None:
            kwargs["enum_name"] = self.enum_full_name()
        super().__init__(**kwargs)

    @property
    def _active_name_map(self) -> dict[int, str]:
        return _name_map_or_raise(self.NAME_MAP, type(self).__name__)

    def name_by_index(self, index: int) -> str:
        """項目番号に対応する表示名を返す。

        Args:
            index: 表示名を調べる項目番号。

        Raises:
            KeyError: 番号が定義されていない場合。
        """
        return _name_by_index_from_name_map(self._active_name_map, index)

    def enum_full_name(self) -> str:
        """`名前=番号` を `:` でつないだ Maya enum 定義を返す。

        ``NAME_MAP`` が未設定なら空文字列を返す。
        """
        if self.NAME_MAP is None:
            return ""
        return _enum_full_name_from_name_map(self.NAME_MAP)

    def index_by_name(self, name: str) -> int:
        """表示名に対応する項目番号を返す。

        Args:
            name: 項目の表示名。

        Raises:
            KeyError: 表示名が定義されていない場合。
        """
        return _index_by_name_from_name_map(self._active_name_map, name)


class EnumField(ScalarBaseField[A, P]):
    """enum 属性の定義とプラグ操作を結ぶディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], EnumAttrOperator)
    PLUG_CLS = cast(Type[P], EnumPlugOperator)
