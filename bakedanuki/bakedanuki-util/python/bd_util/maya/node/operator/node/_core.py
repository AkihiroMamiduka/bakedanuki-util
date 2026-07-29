# coding: utf-8
from __future__ import annotations
from typing import Any, Protocol, Self, TYPE_CHECKING

# maya
import maya.cmds as cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from .....py.metaclass.immutable_descriptor import ImmutableDescriptorMeta
from ...modifier import ModifierManager

if TYPE_CHECKING:
    from ..attr._core import AttrOperator, PlugOperator

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

DEFAULT_VALUE_AUTO_ADD_ATTR = True


class _ExtraAttributeField(Protocol):
    name: str


class IsInstance(ImmutableDescriptor):
    """
    親クラスがインスタンスかどうかの判定
    """

    __slots__ = ()

    def __get__(
        self,
        instance: object | None,
        owner: type,
    ) -> bool:
        """
        属性アクセスメソッド
        親クラスがインスタンスかどうかを返す

        Args:
            instance (object | None): インスタンス
            owner (type): 親クラス

        Returns:
            bool: 親がインスタンスかどうかの真偽値
        """
        if instance is None:
            return False
        return True


class NodeClass(ImmutableDescriptor):
    """
    ノードクラスを返す属性記述子
    """

    __slots__ = ()

    def __get__(
        self,
        instance: object | None,
        owner: type,
    ) -> om.MNodeClass:
        """
        属性アクセスメソッド
        ノードクラスを返す

        Args:
            instance (object | None): インスタンス
            owner (type): 親クラス

        Returns:
            om.MNodeClass: ノードクラス
        """
        node_class = None
        if owner.NODE_TYPE is not None:
            node_class = om.MNodeClass(owner.NODE_TYPE)
        return node_class


class NodeOperator(metaclass=ImmutableDescriptorMeta):
    NODE_TYPE = None
    node_class = NodeClass()
    is_instance = IsInstance()
    _attributes_map_by_long_name: dict[str, AttrOperator[Any]] = {}
    _attributes_map_by_short_name: dict[str, AttrOperator[Any]] = {}
    _extra_attributes: tuple[_ExtraAttributeField, ...] = ()

    __slots__ = (
        "__weakref__",
        "_modifier_manager",
        "m_obj",
        "_fn_node",
        "_plug_cache",
    )

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls._init_set_extra_attrs()

    @classmethod
    def _init_set_extra_attrs(cls):
        """
        クラス階層からすべての extra=True 属性記述子を収集する。
        オブジェクトの同一性に基づいて重複を排除し、
        short_name エイリアス (例: mw = myWeight) が同じ属性を二度登録しないようにする。
        """
        from ..attr._core import (
            AttributeField,
        )  # 循環インポート回避のため遅延インポート

        attributes_by_long_name = {}
        attributes_by_short_name = {}
        extra_attrs = []
        seen_ids = set()
        for klass in cls.__mro__:
            for v in vars(klass).values():
                v: AttributeField[Any, Any]
                obj_id = id(v)

                # 既に登録されているか、AttributeField でない場合はスキップ
                if obj_id in seen_ids or not isinstance(v, AttributeField):
                    continue

                # 初回なので登録
                seen_ids.add(obj_id)

                # class access で AttrOperator を取得してマップを構築する
                oprt_attr = v.__get__(None, cls)
                attributes_by_long_name[oprt_attr.long_name] = oprt_attr
                attributes_by_short_name[oprt_attr.short_name] = oprt_attr

                # extra=True のものは field を保持して、
                # instance access 時に PlugOperator へ解決する
                if getattr(v, "extra", False):
                    extra_attrs.append(v)

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

        # fn_node
        self._fn_node = None

        # name
        if name:
            self._dg_mod.renameNode(self.m_obj, name)

        # plug_cache
        self._plug_cache = None

        # auto_add_attr
        if auto_add_attr and self._extra_attributes:
            self._auto_add_extra_attrs()

    def __getitem__(self, key: str):
        """
        文字列キーでアトリビュートにアクセスし、Plug を返す。

        "attrName"、"attrName.subAttr"、"attrName[0].subAttr" など
        ドット区切り・インデックス指定を組み合わせた文字列から
        Plug インスタンスを取得できる。

        Args:
            key (str): アトリビュート名または "." 区切りのアトリビュートパス。
                各セグメントには "attrName" または "attrName[index]" を使用できる。

        Returns:
            Plug: 対応する Plug インスタンス

        Raises:
            AttributeError: アトリビュートが見つからない場合
            TypeError: key が str 以外の型の場合
            ValueError: キーの書式が不正な場合
        """
        return getattr(self, key)

    def __class_getitem__(cls, key: str):
        return getattr(cls, key)

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    @property
    def _dg_mod(self) -> om.MDGModifier:
        return self._modifier_manager.dg_mod

    def _auto_add_extra_attrs(self):
        """
        extra=True の Attr で、対象ノードに存在しないものを addAttr() する。
        """
        for field in self._extra_attributes:
            plug = getattr(self, field.name)
            plug: PlugOperator[Any]
            if not plug.exists():
                if plug._REQUIRED_CMDS_ADD_ATTR:
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
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

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
        """
        MFnDependencyNode を返す。

        初回アクセス時に作成し、以降はキャッシュを返す。
        """
        if self._fn_node is None:
            self._fn_node = om.MFnDependencyNode(self.m_obj)
        return self._fn_node

    @property
    def name(self) -> str:
        """
        ノード名を返す。

        Returns:
            str: ノード名
        """
        return self.fn_node.name()

    @property
    def namespace(self) -> str:
        """
        ノード名のネームスペース部分を返す。

        ネームスペースが存在しない場合は空文字列を返す。
        例: ``ns1:ns2:nodeName`` → ``"ns1:ns2"``
            ``nodeName`` → ``""``

        Returns:
            str: ネームスペース文字列
        """
        if ":" in self.name:
            return self.name.rsplit(":", 1)[0]
        return ""

    @property
    def namespace_colon(self) -> str:
        """
        ネームスペース部分をコロン付きで返す。

        ネームスペースが存在しない場合は空文字列を返す。
        例: ``ns1:ns2:nodeName`` → ``"ns1:ns2:"``
            ``nodeName`` → ``""``

        Returns:
            str: ネームスペース文字列（コロン付き）
        """
        if self.namespace:
            return f"{self.namespace}:"
        return ""

    @property
    def local_name(self) -> str:
        """
        ネームスペースを除いたノード名（ローカルネーム）を返す。

        例: ``ns1:ns2:nodeName`` → ``"nodeName"``
            ``nodeName`` → ``"nodeName"``

        Returns:
            str: ネームスペースなしのノード名
        """
        if ":" in self.name:
            return self.name.rsplit(":", 1)[1]
        return self.name

    @property
    def _cmd_access_name(self) -> str:
        """
        maya コマンドへアクセスする用のノード名を返す。
        dg ノード : name をそのまま返す
        dag ノード: ロングネームを返す（階層パスを含む）

        Returns:
            str: ノード名の文字列
        """
        return self.name

    def exists(self) -> bool:
        return cmds.objExists(self.name)

    def delete(self):
        if self.exists():
            self.delete_non_check()

    def delete_non_check(self):
        self._dg_mod.deleteNode(self.m_obj)

    def rename(
        self,
        new_name: str | None = None,
        search: str | None = None,
        replace: str = "",
        prefix: str = "",
        suffix: str = "",
    ):
        """
        ノードをリネームする。

        Maya ノード名はネームスペースを含む場合がある（例: ``ns:nodeName``）。
        ネームスペース部分はリネームの対象外とし、コロン以降のピュアな名前部分
        のみを変更する。

        Args:
            new_name (str | None): 新しいノード名（ピュアな名前）。
                指定した場合、現在のピュアな名前を置き換える。
                ``search`` / ``replace`` と同時には使用できない。
            search (str | None): 検索文字列。``replace`` と組み合わせて使用する。
                ``new_name`` と同時には使用できない。
            replace (str): 置換文字列。``search`` と組み合わせて使用する。
            prefix (str): ピュアな名前の先頭に付加する文字列。
            suffix (str): ピュアな名前の末尾に付加する文字列。

        Raises:
            ValueError: ``new_name`` と ``search`` / ``replace`` が同時に
                指定された場合。
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
            replace_str = replace if replace is not None else ""
            pure_name = pure_name.replace(search, replace_str)
        #   prefix, suffix を付加する
        pure_name = prefix + pure_name + suffix

        # リネームする
        self._dg_mod.renameNode(self.m_obj, namespace_prefix + pure_name)
