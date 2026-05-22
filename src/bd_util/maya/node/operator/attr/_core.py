# coding: utf-8
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Generic, Self, Any

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from ..node._core import Node

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Plug(Generic[A], ABC):
    __slots__ = (
        "_node",
        "_attr",
        "_attr_path",
        "multi",
        "index",
        "_plug",
        "_array_plug",
        "_next_index_cache",
        "_next_index",
        "parent_plug",
    )

    def __init__(
        self,
        node: Node,
        attr: A,
        attr_path: str,
        multi: bool = False,
        index: int = None,
        parent_plug: Plug | None = None,
    ):
        # args ----------------------------------------------------------------
        self.parent_plug: Plug | None = parent_plug

        self.multi: bool = multi
        self.index: int = index

        self._node: Node = node
        self._attr: A = attr
        self._attr_path: str = self._create_attr_path(
            parent_attr_path=attr_path
        )
        # args ----------------------------------------------------------------

        # plug
        self._plug: om.MPlug | None = None
        # array plug
        self._array_plug: om.MPlug | None = None
        self._next_index_cache: dict[str, int] | None = None
        self._next_index: int | None = None

    # name
    @property
    def name(self) -> str:
        """
        自身のアトリビュート名

        Returns:
            str: 自身のアトリビュート名
        """
        name = self._attr.name
        if self.index is not None:
            name = f"{name}[{self.index}]"
        return name

    @property
    def long_name(self) -> str:
        """
        自身のロングアトリビュート名

        Returns:
            str: 自身のロングアトリビュート名
        """
        return self.name

    @property
    def short_name(self) -> str:
        """
        自身のショートアトリビュート名

        Returns:
            str: 自身のショートアトリビュート名
        """
        name = self._attr.short_name
        if self.index is not None:
            name = f"{name}[{self.index}]"
        return name

    @property
    def plug(self) -> om.MPlug:
        """
        MPlug インスタンスを取得する

        Returns:
            om.MPlug: MPlug インスタンス
        """
        # キャッシュがあればそれを返す
        if self._plug is not None:
            return self._plug

        # plug を取得する
        #   親アトリビュートがあり、index がない場合は、親の plug から自身の plug を探す
        if self.parent_plug is not None and self.index is None:
            parent_plug = self.parent_plug.plug
            plug = self._find_child_plug(parent_plug, self._attr.name)
            if plug is None:
                raise AttributeError(
                    f"'{self._attr.name}' というアトリビュートは '{parent_plug}' に存在しません"
                )
        #   それ以外は、ノードから直接 plug を探す
        else:
            plug = self._node._fn_node.findPlug(self._attr.long_name, False)

        # index があれば、elementByLogicalIndex で plug を置き換える
        if self.index is not None:
            plug = plug.elementByLogicalIndex(self.index)

        # plug をキャッシュする
        self._plug = plug

        return plug

    def _find_child_plug(
        self,
        plug: om.MPlug,
        child_name: str,
    ) -> om.MPlug | None:
        # 子を探査して、名前が一致する plug を返す
        for i in range(plug.numChildren()):
            # 子の plug を取得
            child_plug = plug.child(i)
            # 子の純粋なロングネームを取得
            p_name = child_plug.partialName(
                useLongNames=True,
                useFullAttributePath=False,
            ).split(".")[-1]
            # 名前を比較して、一致すればその plug を返す
            if p_name == child_name:
                return child_plug
        return None

    # array
    @property
    def array_plug(self) -> om.MPlug:
        # multi アトリビュートでなければ array_plug はない
        if not self.multi:
            raise AttributeError(f"{self.plug} は array_plug を持ちません")

        # index が None ならば、自身が array_plug
        if self.index is None:
            return self.plug

        # index がある場合は、array_plug を返す
        #   キャッシュがなければ、Maya に問い合わせる
        if self._array_plug is None:
            self._array_plug = self.plug.array()
        #   キャッシュを返す
        return self._array_plug

    # type
    @property
    def type(self) -> str:
        """
        アトリビュートの型

        Returns:
            str: アトリビュートの型
        """
        return self._attr.ATTR_TYPE

    # value
    @property
    def value(self) -> Any:
        """
        アトリビュートの値をゲットする

        Returns:
            Any: アトリビュートの値
        """
        return self.get()

    @value.setter
    def value(self, value: Any):
        """
        アトリビュートに値をセットする

        Args:
            value (Any): セットする値
        """
        self.set(value)

    # enum
    @property
    def enum_name(self) -> str | None:
        """
        列挙型アトリビュートの列挙名をゲットする

        Returns:
            str | None: 列挙型アトリビュートの列挙名。列挙型でない場合は None。
        """
        return self._attr.enum_name

    # [] アクセス
    def __getitem__(
        self,
        key: int | str,
    ) -> Self:
        """
        [index] 指定（int）または文字列によるサブアトリビュートアクセス（str）を行い、
        対応する Plug を返す。

        int を渡すと既存の multi アトリビュート用インデックスアクセスとして動作する。
        str を渡すと、サブアトリビュート名から動的に Plug を生成して返す。
        str には "subAttr" または "subAttr[0]" 形式を使用できる。

        Args:
            key (int | str): インデックス（int）またはサブアトリビュート名（str）

        Raises:
            AttributeError: 親アトリビュートが [index] アクセスされている場合に
                            さらに int インデックスアクセスしようとした場合
            AttributeError: 指定した文字列アトリビュートがノードに存在しない場合
            TypeError: int / str 以外の型が渡された場合

        Returns:
            Plug: 対応する Plug インスタンス
        """
        if isinstance(key, int):
            if self.name.endswith("]"):
                raise AttributeError(
                    f"{self.plug} は [{key}] アクセスができません"
                )
            plug: Self = type(self)(
                node=self._node,
                attr=self._attr,
                attr_path=self._attr._attr_path,
                multi=self._attr.multi,
                index=key,
                parent_plug=self,
            )
            return plug
        elif isinstance(key, str):
            attr_name, index = _parse_attr_segment(key)
            plug = _make_dynamic_plug(self._node, attr_name, self._attr_path)
            if index is not None:
                plug = plug[index]
            return plug
        raise TypeError(f"キーの型が不正です: {type(key)}")

    def _create_attr_path(self, parent_attr_path: str) -> str:
        """
        attr_path を作成する

        Args:
            parent_attr_path (str): 親アトリビュートの attr_path

        Returns:
            str: 自身の attr_path
        """
        # 親の attr_path がなければ、自身の名前を返す
        if not parent_attr_path:
            return self.name

        # mulit_attr の index アクセスの場合
        if self.index is not None:
            return f"{parent_attr_path}[{self.index}]"

        # attr_path を生成する
        return f"{parent_attr_path}.{self.name}"

    # str
    def __str__(self) -> str:
        return str(self.plug)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.plug}>"

    def _get_plug_from_str(self, plug_str: str) -> om.MPlug:
        """
        "node.attr" 形式の文字列を MPlug に変換する

        Args:
            plug_str (str): "node.attr" 形式の文字列

        Returns:
            om.MPlug: 変換された MPlug インスタンス
        """
        sel = om.MSelectionList()
        sel.add(plug_str)
        plug = sel.getPlug(0)
        return plug

    def _get_plug_from_strs(self, plug_str_list: list[str]) -> om.MPlug:
        """
        ["node", "attr"] 形式の文字列リストを MPlug に変換する

        Args:
            plug_str_list (list[str]): ["node", "attr"] 形式の文字列リスト

        Returns:
            om.MPlug: 変換された MPlug インスタンス
        """
        plug_str = ".".join(plug_str_list)
        return self._get_plug_from_str(plug_str)

    # get
    @abstractmethod
    def get(self) -> Any:
        """
        プラグの値を取得する: サブクラスでオーバーライドして、適切な型で値を返すようにする
        """
        pass

    # set
    @abstractmethod
    def set(self, value: Any):
        """
        プラグに値をセットする: サブクラスでオーバーライドして、適切な型の値をセットするようにする
        """
        pass

    # connect
    def _normalize_to_plug(self, obj: Plug | str | list[str]) -> om.MPlug:
        """
        渡されたオブジェクトから、 MPlug に変換し返す

        Args:
            obj (Plug | str | list[str]): 対象のオブジェクト

        Raises:
            ValueError: listで渡す際に、["node"]のようにアトリビュートが含まれていないとエラー
                        （誤）["node"]
                        （正）["node", "attr"...]
            TypeError: Plug | str | list[str] 以外が渡されればエラー

        Returns:
            om.MPlug: MPlug インスタンス
        """
        # Plug
        if any(c.__name__ == "Plug" for c in type(obj).__mro__):
            obj: Plug = obj
            return obj.plug
        # str("node.attr")
        elif isinstance(obj, str):
            return self._get_plug_from_str(obj)
        # list or tuple(["node", "attr"...])
        elif isinstance(obj, (list, tuple)):
            if len(obj) < 2:
                raise ValueError("List/Tuple must be ['node', 'attr'...]")
            return self._get_plug_from_strs(obj)

        raise TypeError(f"Unsupported connection type: {type(obj)}")

    def connect(self, other: Plug | str | list[str]):
        """
        self から other へ connect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._normalize_to_plug(self)
        dst = self._normalize_to_plug(other)

        self._node._dg_mod.connect(src, dst)

    def _get_next_index(self) -> int:
        result = 0
        # キャッシュがあればそれを返す
        if self._next_index is not None:
            result = self._next_index
            # インクリメントする
            self._next_index += 1
        # キャッシュがなければ Maya に問い合わせる
        else:
            indices = self.plug.getExistingArrayAttributeIndices()
            if indices:
                result = max(indices) + 1

        # 戻り値
        return result

    def _get_next_plug(self) -> om.MPlug:
        return self.plug.elementByLogicalIndex(self._get_next_index())

    def connect_next_index(self, other: Plug | str | list[str]):
        """
        マルチアトリビュートの最終インデックスの次へ接続する。

        初回呼び出し時に インデックスを取得。
        2回目以降はキャッシュをインクリメントする。

        このメソッド以外の方法でコネクションが追加された場合は、
        :meth:`refresh_next_index` を呼び出してキャッシュを更新すること。

        Args:
            other (Plug | str | list[str]): 接続元のオブジェクト
        """
        src = self._normalize_to_plug(other)
        dst = self._get_next_plug()

        self._node._dg_mod.connect(src, dst)

    def refresh_next_index(self):
        """
        保持しているインデックスキャッシュを破棄する。

        connect_next_index 以外の方法でマルチアトリビュートへの
        コネクションが追加・削除された場合に呼び出すことで、
        次回の connect_next_index() 実行時に正しい最終インデックスを再スキャンする。
        """
        self._next_index = None

    def disconnect(self, other: Plug | str | list[str]):
        """
        self から other へ disconnect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._normalize_to_plug(self)
        dst = self._normalize_to_plug(other)

        self._node._dg_mod.disconnect(src, dst)

    def __gt__(self, other: Plug | str | list[str]) -> Plug | str | list[str]:
        """
        self > other 演算子オーバーライド：接続

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.connect(other)
        return other

    def __lt__(self, other: Plug | str | list[str]) -> Self:
        """
        other > self 演算子のオーバーライド：接続

        Args:
            other (Plug | str | list[str]): 切断元の対象

        Returns:
            Self: self をそのまま返す
        """
        dst = self.plug
        src = self._normalize_to_plug(other)

        self._node._dg_mod.connect(src, dst)
        return self

    def __or__(self, other: Plug | str | list[str]):
        """
        self | other 演算子オーバーライド：切断

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.disconnect(other)
        return other

    def __ror__(self, other: Plug | str | list[str]):
        """
        other | self 演算子のオーバーライド：切断

        Args:
            other (Plug | str | list[str]): 切断元の対象

        Returns:
            Self: self をそのまま返す
        """
        src = self._normalize_to_plug(other)
        dst = self.plug

        self._node._dg_mod.disconnect(src, dst)

        # 切断後、キャッシュをリセットする
        if self._attr.multi:
            self.refresh_next_index()

        return self

    # connection
    @property
    def src_name(self) -> str | None:
        """
        接続元のノード名を返す

        Returns:
            str | None: 接続元ノード名。接続がなければ None。
        """
        result = cmds.listConnections(
            self.plug,
            source=True,
            destination=False,
            plugs=False,
        )
        if result:
            return result[0]
        return None

    @property
    def src_plug(self) -> str | None:
        """
        接続元の "node.attr" 形式の plug 文字列を返す

        Returns:
            str | None: 接続元の plug 文字列。接続がなければ None。
        """
        result = cmds.listConnections(
            self.plug,
            source=True,
            destination=False,
            plugs=True,
        )
        if result:
            return result[0]
        return None

    @property
    def dst_names(self) -> list[str]:
        """
        接続先のノード名一覧を返す

        Returns:
            list[str]: 接続先ノード名のリスト。接続がなければ空リスト。
        """
        result = cmds.listConnections(
            self.plug,
            source=False,
            destination=True,
            plugs=False,
        )
        return result if result else []

    @property
    def dst_plugs(self) -> list[str]:
        """
        接続先の "node.attr" 形式の plug 文字列一覧を返す

        Returns:
            list[str]: 接続先の plug 文字列のリスト。接続がなければ空リスト。
        """
        result = cmds.listConnections(
            self.plug,
            source=False,
            destination=True,
            plugs=True,
        )
        return result if result else []

    # exists
    def exists(self) -> bool:
        return self._node._fn_node.hasAttribute(self.long_name)

    # addAttr
    def add_attr(self):
        """
        このプラグが参照するアトリビュートを、対象ノードに addAttr() する。
        既に存在する場合はスキップする。
        """
        self._attr.add_attr(self._node._cmd_access_name)


def _parse_attr_segment(segment: str) -> tuple[str, int | None]:
    """
    "attrName[0]" や "attrName" 形式の文字列を、アトリビュート名とインデックスに分解する。

    Args:
        segment (str): "attrName" または "attrName[index]" 形式の文字列

    Returns:
        tuple[str, int | None]: (アトリビュート名, インデックス or None)

    Raises:
        ValueError: "[" と "]" の対応が取れていないまたは index が整数でない場合
    """
    if "[" not in segment:
        if "]" in segment:
            raise ValueError(
                f"アトリビュートキーの書式が不正です: '{segment}'"
                " (例: 'attrName[0]')"
            )
        if not segment:
            raise ValueError("アトリビュートキーのセグメントが空文字列です")
        return segment, None

    if not segment.endswith("]"):
        raise ValueError(
            f"アトリビュートキーの書式が不正です: '{segment}'"
            " (例: 'attrName[0]')"
        )
    attr_name, bracket = segment.split("[", 1)
    index_str = bracket[:-1]  # "]" を除去
    try:
        index = int(index_str)
    except ValueError:
        raise ValueError(
            f"アトリビュートキーのインデックスが整数ではありません: '{segment}'"
        )
    return attr_name, index


def _make_dynamic_plug(
    node: Node, attr_name: str, parent_attr_path: str = ""
) -> Plug:
    """
    ノードとアトリビュート名から、動的に Plug インスタンスを生成して返す。

    lookup_attr_cls でアトリビュート型を特定し、対応する Attr インスタンスを
    動的に生成する。デスクリプタ経由のキャッシュと干渉しないよう、
    生成した Plug はノードのキャッシュには格納しない。

    Args:
        node (Node): 対象ノードのインスタンス
        attr_name (str): アトリビュート名（短縮名または長名）
        parent_attr_path (str): 親アトリビュートの attr_path。
            最上位アトリビュートの場合は空文字列を渡す。

    Returns:
        Plug: 対応する Plug インスタンス

    Raises:
        AttributeError: ノードにアトリビュートが存在しない、または
            対応する Attr クラスが見つからない場合
    """
    from .lookup import (
        lookup_attr_cls,
    )  # 循環インポート回避のため遅延インポート

    attr_cls = lookup_attr_cls(node.name, attr_name)
    if attr_cls is None:
        raise AttributeError(
            f"'{node.name}' にアトリビュート '{attr_name}' の対応クラスが見つかりません"
        )

    try:
        long_name = cmds.attributeQuery(
            attr_name, node=node.name, longName=True
        )
    except RuntimeError:
        logger.debug(
            "{} '{}.{}': {}".format(
                "attributeQuery longName failed for",
                node.name,
                attr_name,
                "using input name",
            )
        )
        long_name = attr_name

    try:
        multi = bool(
            cmds.attributeQuery(long_name, node=node.name, multi=True)
        )
    except RuntimeError:
        logger.debug(
            "{} '{}.{}': {}".format(
                "attributeQuery multi failed for",
                node.name,
                long_name,
                "defaulting to False",
            )
        )
        multi = False

    try:
        short_name = cmds.attributeQuery(
            long_name, node=node.name, shortName=True
        )
    except RuntimeError:
        logger.debug(
            "{} '{}.{}': {}".format(
                "attributeQuery shortName failed for",
                node.name,
                long_name,
                "using long name",
            )
        )
        short_name = long_name

    attr_path = (
        f"{parent_attr_path}.{long_name}" if parent_attr_path else long_name
    )

    attr = attr_cls(multi=multi)
    object.__setattr__(attr, "name", long_name)
    object.__setattr__(attr, "long_name", long_name)
    object.__setattr__(attr, "short_name", short_name)
    object.__setattr__(attr, "_attr_path", attr_path)
    object.__setattr__(attr, "_node", node)

    return attr.PLUG_CLS(
        node=node,
        attr=attr,
        attr_path=parent_attr_path,
        multi=multi,
    )


class Attr(ImmutableDescriptor, Generic[P]):
    __slots__ = (
        "_node",
        "_m_obj",
        "_parent_attr_path",
        "multi",
        "extra",
        "_default_value",
        "_min_value",
        "_max_value",
        "_soft_min_value",
        "_soft_max_value",
        "_enum_name",
        "_number_of_children",
        "_parent",
        "_readable",
        "_writable",
        "_category",
        "name",
        "long_name",
        "short_name",
        "_attr_path",
    )
    # type
    ATTR_TYPE: str = None
    DATA_TYPE: str = None
    # plug
    PLUG_CLS: Type[P] = None
    # name
    name: str
    long_name: str | None
    short_name: str | None
    # attr
    _attr_path: str

    def __init__(
        self,
        multi: bool = False,
        extra: bool = False,
        default_value: Any = None,
        min_value: Any = None,
        max_value: Any = None,
        soft_min_value: Any = None,
        soft_max_value: Any = None,
        enum_name: str | None = None,
        number_of_children: int | None = None,
        parent: str | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ):
        # node
        self._node: Node = None
        # m_obj
        self._m_obj: om.MObject = None
        # name
        self.name = ""
        self.long_name = None
        self.short_name = None
        # attr
        #   attr_path
        self._attr_path = ""
        self._parent_attr_path: str = ""
        #   multi
        self.multi: bool = multi
        #   extra attr flag
        self.extra: bool = extra
        # extra attr info
        self._default_value: Any = default_value
        self._min_value: Any = min_value
        self._max_value: Any = max_value
        self._soft_min_value: Any = soft_min_value
        self._soft_max_value: Any = soft_max_value
        self._enum_name: str | None = enum_name
        self._number_of_children: int | None = number_of_children
        self._parent: str | None = parent
        self._readable: bool | None = readable
        self._writable: bool | None = writable
        self._category: str | None = category

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.ATTR_TYPE is None:
            raise NotImplementedError(
                f"{cls.__name__} は、 ATTR_TYPE が定義されていません。定義してください。"
            )
        if cls.PLUG_CLS is None:
            raise NotImplementedError(
                f"{cls.__name__} は、 PLUG_CLS が定義されていません。定義してください。"
            )

    # __set_name__
    def _on_set_name(self, owner: Any, name: str):
        """
        __set_name__ 内で、実行されるメソッド

        Args:
            owner (Any): 親のクラス
            name (str): セットされている変数名
        """
        # name をセット
        if self.long_name is None:
            #  name, _attr_path, long_name にセット
            self.name = name
            self._attr_path = name
            self.long_name = name
        else:
            # short name をセット
            object.__setattr__(self, "short_name", name)

    # __get__
    def __get__(self, instance: object | None, owner: type) -> Self | P:
        """
        属性アクセスされた際に実行されるメソッド
        Node へのアクセスが、
        クラスアクセスの場合、 Attr を返し、
        インスタンスアクセスの場合、 Plug を返す

        Args:
            instance (object | None): インスタンスオブジェクト
            owner (type): 親クラス

        Returns:
            Self | P: Attr or Plug
        """
        # node, attr_path をセットする
        #   class アクセス
        if instance is None:
            # Node
            object.__setattr__(self, "_node", owner)
            self._set_m_obj__top_level_attr()
        #   instance アクセス
        else:
            # 親が Node
            if hasattr(instance, "NODE_TYPE"):
                object.__setattr__(self, "_node", instance)
                self._set_m_obj__top_level_attr()
            # 親が Attr or Plug
            else:
                instance: Plug[A] = instance
                # compound の子アトリビュートを node クラスに再定義する際に、自身を返す
                if instance._node is None:
                    return self
                object.__setattr__(self, "_node", instance._node)
                object.__setattr__(
                    self, "_parent_attr_path", instance._attr_path
                )
                self._set_attr_path(self._parent_attr_path)

                # _m_obj
                self._set_m_obj__child_level_attr(instance._attr._m_obj)

        # 戻り値
        #   Node が instance へのアクセス(Plug)
        if self._node.is_instance:
            key = (self.name, self._attr_path)
            parent_plug = None
            if self._parent_attr_path:
                parent_plug = instance
            if key not in self._node._plug_cache:
                self._node._plug_cache[key] = self.PLUG_CLS(
                    node=self._node,
                    attr=self,
                    attr_path=self._parent_attr_path,
                    multi=self.multi,
                    parent_plug=parent_plug,
                )
            return self._node._plug_cache[key]
        #   Node が class へのアクセス(Attr)
        else:
            return self

    # m_obj
    def _set_m_obj__top_level_attr(self):
        object.__setattr__(
            self,
            "_m_obj",
            self._node.node_class.attribute(self.long_name),
        )

    def _set_m_obj__child_level_attr(self, parent_m_obj: om.MObject):
        object.__setattr__(
            self,
            "_m_obj",
            self.find_child_attribute(parent_m_obj, self.long_name),
        )

    def find_child_attribute(
        self,
        compound_attr_obj: om.MObject,
        name: str,
    ) -> om.MObject | None:
        compound_fn = om.MFnCompoundAttribute(compound_attr_obj)

        for i in range(compound_fn.numChildren()):
            child_attr_obj = compound_fn.child(i)
            fn_attr = om.MFnAttribute(child_attr_obj)
            if fn_attr.name == name:
                return child_attr_obj

        return None

    # attr_path
    def _set_attr_path(self, parent_attr_path: str):
        """
        attr_path をセットする

        Args:
            parent_attr_path (str): 親の attr_path
        """
        # 親の attr_path がなければ終了する
        if not parent_attr_path:
            return

        # attr_path を生成する
        attr_path = f"{parent_attr_path}.{self.name}"

        # attr_path をセットする
        object.__setattr__(self, "_attr_path", attr_path)

    # str
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    # type
    @property
    def type(self) -> str:
        """
        アトリビュートの型

        Returns:
            str: アトリビュートの型
        """
        return self.ATTR_TYPE

    @property
    def is_data_type(self) -> bool:
        """
        データタイプのアトリビュートかどうか

        Returns:
            bool: データタイプのアトリビュートかどうか
        """
        return self.DATA_TYPE is not None

    # attr info
    def _query_attr_info(self, **kwargs) -> Any:
        """
        cmds.attributeQuery を安全に実行し、結果を返す。
        ノードのインスタンスが設定されていない場合は None を返す。

        Returns:
            Any: cmds.attributeQuery の結果。取得できない場合は None。
        """
        if self._node is None or not self._node.is_instance:
            return None
        try:
            return cmds.attributeQuery(
                self.long_name, node=self._node._cmd_access_name, **kwargs
            )
        except Exception:
            return None

    @property
    def default_value(self) -> Any:
        """アトリビュートのデフォルト値"""
        if self.extra:
            return self._default_value
        return self._query_attr_info(listDefault=True)

    @property
    def min_value(self) -> Any:
        """アトリビュートの最小値"""
        if self.extra:
            return self._min_value
        return self._query_attr_info(minimum=True)

    @property
    def max_value(self) -> Any:
        """アトリビュートの最大値"""
        if self.extra:
            return self._max_value
        return self._query_attr_info(maximum=True)

    @property
    def soft_min_value(self) -> Any:
        """アトリビュートのソフト最小値"""
        if self.extra:
            return self._soft_min_value
        return self._query_attr_info(softMin=True)

    @property
    def soft_max_value(self) -> Any:
        """アトリビュートのソフト最大値"""
        if self.extra:
            return self._soft_max_value
        return self._query_attr_info(softMax=True)

    @property
    def enum_name(self) -> str | None:
        """列挙型アトリビュートの列挙名"""
        if self._enum_name is not None:
            return self._enum_name
        return self._query_attr_info(listEnum=True)

    @property
    def number_of_children(self) -> int | None:
        """コンパウンドアトリビュートの子アトリビュート数"""
        if self.extra:
            return self._number_of_children
        return self._query_attr_info(numberOfChildren=True)

    @property
    def parent(self) -> str | None:
        """親アトリビュート名"""
        if self.extra:
            return self._parent
        return self._query_attr_info(listParent=True)

    @property
    def readable(self) -> bool | None:
        """アトリビュートが読み取り可能かどうか"""
        if self.extra:
            return self._readable
        return self._query_attr_info(readable=True)

    @property
    def writable(self) -> bool | None:
        """アトリビュートが書き込み可能かどうか"""
        if self.extra:
            return self._writable
        return self._query_attr_info(writable=True)

    @property
    def category(self) -> str | None:
        """アトリビュートのカテゴリ"""
        if self.extra:
            return self._category
        return self._query_attr_info(categories=True)

    # addAttr
    def add_attr(self, node_name: str):
        """
        対象ノードに、このアトリビュートを addAttr() する。
        既に存在する場合はスキップする。

        Args:
            node_name (str): 対象ノード名
        """
        if cmds.objExists(f"{node_name}.{self.long_name}"):
            return

        if self.is_data_type:
            kwargs = {"dataType": self.DATA_TYPE}
        else:
            kwargs = {"attributeType": self.ATTR_TYPE}
        kwargs["longName"] = self.long_name
        if self.short_name is not None:
            kwargs["shortName"] = self.short_name
        if self._default_value is not None:
            kwargs["defaultValue"] = self._default_value
        if self._min_value is not None:
            kwargs["minValue"] = self._min_value
        if self._max_value is not None:
            kwargs["maxValue"] = self._max_value
        if self._soft_min_value is not None:
            kwargs["softMinValue"] = self._soft_min_value
        if self._soft_max_value is not None:
            kwargs["softMaxValue"] = self._soft_max_value
        if self._enum_name is not None:
            kwargs["enumName"] = self._enum_name
        if self._number_of_children is not None:
            kwargs["numberOfChildren"] = self._number_of_children
        if self._parent is not None:
            kwargs["parent"] = self._parent
        if self._readable is not None:
            kwargs["readable"] = self._readable
        if self._writable is not None:
            kwargs["writable"] = self._writable
        if self._category is not None:
            kwargs["category"] = self._category

        cmds.addAttr(node_name, **kwargs)
