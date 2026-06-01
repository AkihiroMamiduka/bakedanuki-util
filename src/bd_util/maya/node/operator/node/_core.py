# coding: utf-8
from __future__ import annotations
from typing import Self

# maya
import maya.cmds as cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from .....py.metaclass.immutable_descriptor import ImmutableDescriptorMeta

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

DEFAULT_VALUE_AUTO_ADD_ATTR = True


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
    _attributes_map_by_long_name: dict = {}
    _attributes_map_by_short_name: dict = {}
    _extra_attributes: tuple = ()

    __slots__ = (
        "__weakref__",
        "_dg_mod",
        "_m_obj",
        "_fn_node",
        "_plug_cache",
    )

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls._init_get_extra_attrs()

    @classmethod
    def _init_get_extra_attrs(cls) -> tuple:
        """
        クラス階層からすべての extra=True 属性記述子を収集する。
        オブジェクトの同一性に基づいて重複を排除し、
        short_name エイリアス (例: mw = myWeight) が同じ属性を二度登録しないようにする。
        """
        from ..attr._core import (
            AttrOperator,
        )  # 循環インポート回避のため遅延インポート

        attributes_by_long_name = {}
        attributes_by_short_name = {}
        extra_attrs = []
        seen_ids = set()
        for klass in cls.__mro__:
            for v in vars(klass).values():
                v: AttrOperator
                obj_id = id(v)
                if obj_id not in seen_ids and any(
                    c.__name__ == "AttrOperator" for c in type(v).__mro__
                ):
                    seen_ids.add(obj_id)
                    attributes_by_long_name[v.long_name] = v
                    attributes_by_short_name[v.short_name] = v
                    if getattr(v, "extra", False):
                        extra_attrs.append(v)
        cls._attributes_map_by_long_name = attributes_by_long_name
        cls._attributes_map_by_short_name = attributes_by_short_name
        cls._extra_attributes = tuple(extra_attrs)

    def __init__(
        self,
        dg_mod: om.MDGModifier,
        name: str = None,
        m_obj: om.MObject = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ):
        if m_obj is None and name is None:
            raise ValueError("Either m_obj or name must be provided.")
        # dg_mod
        self._dg_mod = dg_mod

        # m_obj
        if m_obj is not None:
            self._m_obj = m_obj
        else:
            sel = om.MSelectionList()
            sel.add(name)
            self._m_obj = sel.getDependNode(0)

        # fn_node
        self._fn_node = om.MFnDependencyNode(self._m_obj)

        # name
        if name:
            self._dg_mod.renameNode(self._m_obj, name)

        # plug_cache
        self._plug_cache = {}

        # auto_add_attr
        if auto_add_attr:
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
        from ..attr._core import (
            _make_dynamic_plug,
            _parse_attr_segment,
        )  # 循環インポート回避のため遅延インポート

        if not isinstance(key, str):
            raise TypeError(
                f"キーの型は str でなければなりません: {type(key)}"
            )

        segments = key.split(".")
        if any(s == "" for s in segments):
            raise ValueError(
                f"アトリビュートキーに空セグメントが含まれています: '{key}'"
            )

        # 最初のセグメントを処理する（名前 + オプションのインデックス）
        attr_name, index = _parse_attr_segment(segments[0])

        plug = _make_dynamic_plug(self, attr_name, "")
        if index is not None:
            plug = plug[index]

        # 残りのセグメントを順に処理する
        for segment in segments[1:]:
            plug = plug[segment]

        return plug

    def _auto_add_extra_attrs(self):
        """
        extra=True の Attr で、対象ノードに存在しないものを addAttr() する。
        """
        for attr in self._extra_attributes:
            attr.add_attr(self.name)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @classmethod
    def create(
        cls,
        dg_mod: om.MDGModifier,
        name=None,
        auto_add_attr=DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Self:
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

        # ノード作成
        m_obj = dg_mod.createNode(cls.NODE_TYPE)
        # ノード名を変更
        if name:
            dg_mod.renameNode(m_obj, name)

        # # チャンネルボックスでのINPUTS OUTPUTSから表示を消す
        # fn_node = om.MFnDependencyNode(m_obj)
        # attr_obj = fn_node.attribute("isHistoricallyInteresting")
        # plug = om.MPlug(m_obj, attr_obj)
        # dg_mod.newPlugValueBool(plug, False)

        # インスタンス生成
        return cls(
            dg_mod,
            m_obj=m_obj,
            name=name,
            auto_add_attr=auto_add_attr,
        )

    @property
    def name(self) -> str:
        """
        ノード名を返す。

        Returns:
            str: ノード名
        """
        return self._fn_node.name()

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
        self._dg_mod.deleteNode(self._m_obj)

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
        self._dg_mod.renameNode(self._m_obj, namespace_prefix + pure_name)
