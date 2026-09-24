# coding: utf-8
from __future__ import annotations
from typing import Any, cast, ClassVar, Self, TYPE_CHECKING

# maya
import maya.cmds as cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from .....py.metaclass.immutable_descriptor import ImmutableDescriptorMeta
from ..._maya_version import require_node_type_available
from ...modifier import ModifierManager

if TYPE_CHECKING:
    from ..attr._core import AttributeField, AttrOperator, PlugOperator
    from ._keyframes import NodeKeyframeManager

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

DEFAULT_VALUE_AUTO_ADD_ATTR = True


class IsInstance(ImmutableDescriptor):
    """クラスアクセスとインスタンスアクセスを判別する記述子。"""

    __slots__ = ()

    def __get__(
        self,
        instance: object | None,
        owner: type[NodeOperator],
    ) -> bool:
        """インスタンスからアクセスされたかを返す。

        Args:
            instance: クラスアクセス時は None。
            owner: アクセス先の NodeOperator クラス。

        Returns:
            インスタンスアクセスなら True、クラスアクセスなら False。
        """
        if instance is None:
            return False
        return True


class NodeClass(ImmutableDescriptor):
    """Maya ノード型の MNodeClass を返す記述子。"""

    __slots__ = ()

    def __get__(
        self,
        instance: object | None,
        owner: type[NodeOperator],
    ) -> om.MNodeClass | None:
        """アクセス先クラスに対応する MNodeClass を返す。

        Args:
            instance: クラスアクセス時は None。
            owner: NODE_TYPE を定義する NodeOperator クラス。

        Returns:
            Maya のノードクラス。NODE_TYPE が未定義なら None。
        """
        node_type = owner.NODE_TYPE
        if node_type is None:
            return None
        return om.MNodeClass(node_type)


class NodeOperator(metaclass=ImmutableDescriptorMeta):
    """Maya ノードとその属性操作を包む共通基底クラス。"""

    NODE_TYPE: ClassVar[str | None] = None
    node_class = NodeClass()
    is_instance = IsInstance()
    _attributes_map_by_long_name: dict[str, AttrOperator[Any]] = {}
    _attributes_map_by_short_name: dict[str, AttrOperator[Any]] = {}
    _extra_attributes: tuple[AttributeField[Any, Any], ...] = ()

    __slots__ = (
        "__weakref__",
        "_modifier_manager",
        "m_obj",
        "_fn_node",
        "_pending_at_initialization",
        "_requested_name",
        "_plug_cache",
    )

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)

        cls._init_set_extra_attrs()

    @classmethod
    def _init_set_extra_attrs(cls) -> None:
        """継承階層の extra attribute を重複なく登録する。

        同一の記述子を指す短縮名エイリアスは、別の属性として扱わない。
        """
        from ..attr._core import (
            AttributeField,
        )  # 循環インポート回避のため遅延インポート

        attributes_by_long_name: dict[str, AttrOperator[Any]] = {}
        attributes_by_short_name: dict[str, AttrOperator[Any]] = {}
        extra_attrs: list[AttributeField[Any, Any]] = []
        seen_ids: set[int] = set()
        for klass in cls.__mro__:
            for value in vars(klass).values():
                if not isinstance(value, AttributeField):
                    continue
                field = cast(AttributeField[Any, Any], value)
                obj_id = id(field)
                if obj_id in seen_ids:
                    continue

                seen_ids.add(obj_id)

                # class access で AttrOperator を取得してマップを構築する
                oprt_attr = field.__get__(None, cls)
                attributes_by_long_name[oprt_attr.long_name] = oprt_attr
                attributes_by_short_name[oprt_attr.short_name] = oprt_attr

                # extra=True のものは field を保持して、
                # instance access 時に PlugOperator へ解決する
                if field.extra:
                    extra_attrs.append(field)

        cls._attributes_map_by_long_name = attributes_by_long_name
        cls._attributes_map_by_short_name = attributes_by_short_name
        cls._extra_attributes = tuple(extra_attrs)

    def __init__(
        self,
        modifier_manager: ModifierManager,
        name: str | None = None,
        m_obj: om.MObject | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> None:
        """既存または作成予定のノードを包む。

        Args:
            modifier_manager: 変更を予約する先。
            name: ノード名。m_obj と併用した場合は名前変更を予約する。
            m_obj: 対象の MObject。
            auto_add_attr: 定義済みの extra attribute を追加するか。

        Raises:
            ValueError: name と m_obj の両方が省略された場合。
        """
        if m_obj is None and name is None:
            raise ValueError("Either m_obj or name must be provided.")
        # modifier_manager
        self._modifier_manager = modifier_manager

        # m_obj
        if m_obj is not None:
            self.m_obj = m_obj
        else:
            sel = om.MSelectionList()
            sel.add(name)
            self.m_obj = sel.getDependNode(0)

        handle = om.MObjectHandle(self.m_obj)
        self._pending_at_initialization = (
            handle.isAlive() and not handle.isValid()
        )

        # fn_node
        self._fn_node = None

        # 未実行の新規 MObject は Maya 名を取得できないため、予約時の名前を
        # データ検索用の手掛かりとして保持する。
        self._requested_name: str | None = None

        # name
        if name:
            self._dg_mod.renameNode(self.m_obj, name)
            self._set_requested_name_hint(name)

        # plug_cache
        self._plug_cache: dict[str, PlugOperator[Any]] | None = None

        # auto_add_attr
        if auto_add_attr and self._extra_attributes:
            self._auto_add_extra_attrs()

    def __getitem__(self, key: str) -> PlugOperator[Any]:
        """属性パスから PlugOperator を取得する。

        Args:
            key: 属性名または ``attrName[0].subAttr`` 形式の属性パス。

        Returns:
            対応する PlugOperator。

        Raises:
            AttributeError: 属性が見つからない場合。
            TypeError: key が文字列でない場合。
            ValueError: 属性パスの書式が不正な場合。
        """
        return cast("PlugOperator[Any]", getattr(self, key))

    def __class_getitem__(cls, key: str) -> AttrOperator[Any]:
        return cast("AttrOperator[Any]", getattr(cls, key))

    @property
    def modifier_manager(self) -> ModifierManager:
        """このノードへの変更を予約する先。"""
        return self._modifier_manager

    @property
    def keyframes(self) -> NodeKeyframeManager:
        """このノードのキーフレーム操作を予約する入口。"""
        from ._keyframes import NodeKeyframeManager

        return NodeKeyframeManager(self.m_obj, self._modifier_manager)

    @classmethod
    def get_attr_operator(cls, long_name: str) -> AttrOperator[Any] | None:
        """長い属性名に対応するクラス定義を返す。

        Args:
            long_name: Maya の長い属性名。
        """
        return cls._attributes_map_by_long_name.get(long_name)

    @classmethod
    def get_extra_attribute_fields(
        cls,
    ) -> tuple[AttributeField[Any, Any], ...]:
        """自動追加対象に登録された extra attribute 定義を返す。"""
        return cls._extra_attributes

    def get_cached_plug(self, attr_path: str) -> PlugOperator[Any] | None:
        """属性パスに対応するキャッシュ済み PlugOperator を返す。"""
        plug_cache = self._plug_cache
        if plug_cache is None:
            return None
        return plug_cache.get(attr_path)

    def cache_plug(
        self,
        attr_path: str,
        plug: PlugOperator[Any],
    ) -> None:
        """属性パスに対する PlugOperator をキャッシュする。"""
        plug_cache = self._plug_cache
        if plug_cache is None:
            plug_cache = {}
            self._plug_cache = plug_cache
        plug_cache[attr_path] = plug

    @property
    def _dg_mod(self) -> om.MDGModifier:
        return self._modifier_manager.dg_mod

    def _auto_add_extra_attrs(self):
        """不足している extra attribute を対象ノードへ追加する。"""
        for field in self._extra_attributes:
            plug = getattr(self, field.name)
            plug: PlugOperator[Any]
            if not plug.exists():
                if plug.requires_cmds_add_attr:
                    plug.cmds_add_attr()
                else:
                    plug.add_attr()

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @classmethod
    def create(
        cls,
        modifier_manager: ModifierManager,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Self:
        """このクラスに対応する DG ノードの作成を予約する。

        Args:
            modifier_manager: ノード作成を予約する先。
            name: 作成するノードの名前。省略時は Maya に委ねる。
            auto_add_attr: 定義済みの extra attribute を追加するか。

        Returns:
            作成予定のノードを包むインスタンス。

        Raises:
            ValueError: クラスに NODE_TYPE が定義されていない場合。
        """
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")
        require_node_type_available(cls.NODE_TYPE)

        # ノード作成
        m_obj = modifier_manager.dg_mod.createNode(cls.NODE_TYPE)

        # インスタンス生成
        return cls(
            modifier_manager,
            m_obj=m_obj,
            name=name,
            auto_add_attr=auto_add_attr,
        )

    @property
    def fn_node(self) -> om.MFnDependencyNode:
        """対象ノードの MFnDependencyNode。初回アクセス時に作成する。"""
        if self._fn_node is None:
            self._fn_node = om.MFnDependencyNode(self.m_obj)
        return self._fn_node

    @property
    def name(self) -> str:
        """現在の Maya ノード名。"""
        return self.fn_node.name()

    @property
    def _requested_name_hint(self) -> str | None:
        """最後に予約した明示的なノード名。"""
        return self._requested_name

    @property
    def _was_pending_creation(self) -> bool:
        """作成待ちの MObject を受け取ったか。"""
        return self._pending_at_initialization

    def _set_requested_name_hint(self, name: str) -> None:
        """名前変更を予約した後のノード名を記録する。"""
        if name.startswith(":"):
            self._requested_name = name[1:]
            return
        namespace = om.MNamespace.currentNamespace().removeprefix(":")
        self._requested_name = f"{namespace}:{name}" if namespace else name

    @property
    def namespace(self) -> str:
        """ノード名の namespace 部分。なければ空文字列。"""
        if ":" in self.name:
            return self.name.rsplit(":", 1)[0]
        return ""

    @property
    def namespace_colon(self) -> str:
        """末尾のコロンを含む namespace。なければ空文字列。"""
        if self.namespace:
            return f"{self.namespace}:"
        return ""

    @property
    def local_name(self) -> str:
        """namespace を除いたノード名。"""
        if ":" in self.name:
            return self.name.rsplit(":", 1)[1]
        return self.name

    @property
    def cmd_access_name(self) -> str:
        """Maya コマンドでこのノードを指定する名前。"""
        return self.name

    def exists(self) -> bool:
        """シーンにこの名前のノードが存在するか。"""
        return cmds.objExists(self.name)

    def delete(self):
        """ノードが存在する場合、その削除を予約する。"""
        if self.exists():
            self.delete_non_check()

    def delete_non_check(self):
        """存在確認を行わず、ノードの削除を予約する。"""
        self._dg_mod.deleteNode(self.m_obj)

    def rename(
        self,
        new_name: str | None = None,
        search: str | None = None,
        replace: str = "",
        prefix: str = "",
        suffix: str = "",
    ):
        """ネームスペースを保ち、ローカル名の変更を予約する。

        Args:
            new_name: 新しいローカル名。search とは同時に指定できない。
            search: ローカル名から検索する文字列。
            replace: search に一致した箇所の置換文字列。
            prefix: ローカル名の先頭に加える文字列。
            suffix: ローカル名の末尾に加える文字列。

        Raises:
            ValueError: 指定がない場合、または new_name と search を
                同時に指定した場合。
        """
        if new_name is not None and search is not None:
            raise ValueError(
                "new_name と search/replace を同時に指定することはできません。"
            )
        elif new_name is None and search is None and not prefix and not suffix:
            raise ValueError(
                "new_name または search、もしくは prefix/suffix のいずれかを指定してください。"
            )

        # ネームスペースとピュアな名前を分離する
        # Maya のノード名は "ns1:ns2:pureName" のような形式になる
        if ":" in self.name:
            namespace, pure_name = self.name.rsplit(":", 1)
            namespace_prefix = namespace + ":"
        else:
            namespace_prefix = ""
            pure_name = self.name

        namespace_prefix = self.namespace_colon
        pure_name = self.local_name

        # ピュアな名前を変換する
        #   名前自体の変換
        if new_name is not None:
            pure_name = new_name
        elif search is not None:
            pure_name = pure_name.replace(search, replace)
        #   prefix, suffix を付加する
        pure_name = prefix + pure_name + suffix

        # リネームする
        requested_name = namespace_prefix + pure_name
        self._dg_mod.renameNode(self.m_obj, requested_name)
        self._set_requested_name_hint(requested_name)
