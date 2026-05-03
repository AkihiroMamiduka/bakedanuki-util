# coding: utf-8
from __future__ import annotations
from typing import TypeVar, Type, Generic, Self, Any

# maya
from maya import cmds

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from ..node._core import Node

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

A = TypeVar("A", bound="Attr")

P = TypeVar("P", bound="Plug")


class Plug(Generic[A]):
    def __init__(
        self,
        node: Node,
        attr: A,
        attr_path: str,
        multi: bool = False,
        index: int = None,
    ):
        self._node: Node = node
        self._attr: A = attr
        self.multi: bool = multi
        self.index: int = index
        self._attr_path: str = self._create_attr_path(
            parent_attr_path=attr_path
        )
        self._next_index_cache: dict[str, int] | None = None

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
    def plug(self) -> str:
        """
        "node.attr"形式の plug 文字列

        Returns:
            str: "node.attr"形式の plug 文字列
        """
        return f"{self._node.name}.{self._attr_path}"

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
    ) -> Plug:
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
                index=key,
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
        if self.name.endswith("]"):
            return self.name

        # attr_path を生成する
        return f"{parent_attr_path}.{self.name}"

    # str
    def __str__(self) -> str:
        return self.plug

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.plug}>"

    # get
    def get(self) -> Any:
        """
        アトリビュートの値を取得する

        Returns:
            Any: アトリビュートの値
        """
        return cmds.getAttr(self.plug)

    # set
    def set(self, value: Any):
        """
        アトリビュートに値をセットする

        Args:
            value (Any): アトリビュートの値
        """
        cmds.setAttr(self.plug, value)

    # connect
    @staticmethod
    def _normalize_to_plug(obj: Plug | str | list[str]) -> str:
        """
        渡されたオブジェクトから、 "node.attr" 形式の plug 文字列に変換し返す

        Args:
            obj (Plug | str | list[str]): 対象のオブジェクト

        Raises:
            ValueError: listで渡す際に、["node"]のようにアトリビュートが含まれていないとエラー
                        （誤）["node"]
                        （正）["node", "attr"...]
            TypeError: Plug | str | list[str] 以外が渡されればエラー

        Returns:
            str: "node.attr"形式の plug 文字列
        """
        # Plug
        if hasattr(obj, "plug"):
            obj: Plug = obj
            return obj.plug
        # str("node.attr")
        elif isinstance(obj, str):
            return obj
        # list or tuple(["node", "attr"...])
        elif isinstance(obj, (list, tuple)):
            if len(obj) < 2:
                raise ValueError("List/Tuple must be ['node', 'attr'...]")
            return ".".join([str(o) for o in obj])

        raise TypeError(f"Unsupported connection type: {type(obj)}")

    def connect(self, other: Plug | str | list[str]):
        """
        self から other へ cmds.connectAttr()

        Args:
            obj (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._normalize_to_plug(self)
        dst = self._normalize_to_plug(other)

        cmds.connectAttr(src, dst, force=True)

    def connect_next_index(self, other: Plug | str | list[str]):
        """
        マルチアトリビュートの最終インデックスの次へ接続する。

        self の attr_path に含まれるマルチアトリビュートに対して、
        現在の最大インデックスの次のインデックスへ other を接続する。

        初回呼び出し時に cmds.attributeQuery / cmds.getAttr でインデックスを
        スキャンしてキャッシュし、2回目以降はキャッシュをインクリメントするだけ
        なので高速に動作する。

        このメソッド以外の方法でコネクションが追加された場合は、
        :meth:`refresh_next_index` を呼び出してキャッシュを更新すること。

        Args:
            other (Plug | str | list[str]): 接続元のオブジェクト
        """
        node_name = self._node.name
        segments = self._attr_path.split(".")

        # --- 初回: キャッシュをスキャンして構築 ---
        if self._next_index_cache is None:
            self._next_index_cache = {}
            scanned_segments = []
            for segment in segments:
                # マルチアトリビュートのインデックスが指定されている場合は、探査する必要がないのでスキップ
                if "[" in segment:
                    scanned_segments.append(segment)
                    continue
                is_multi = cmds.attributeQuery(
                    segment,
                    node=node_name,
                    multi=True,
                )
                # マルチアトリビュートでない場合は、探査する必要がないのでスキップ
                if not is_multi:
                    scanned_segments.append(segment)
                    continue
                current_attr = ".".join(scanned_segments + [segment])
                current_plug = f"{node_name}.{current_attr}"
                indices = cmds.getAttr(current_plug, multiIndices=True)
                self._next_index_cache[segment] = (
                    (max(indices) + 1) if indices else 0
                )
                scanned_segments.append(segment)

        # --- キャッシュを使ってアトリビュートパスを構築 ---
        new_segments = []
        for segment in segments:
            if "[" not in segment and segment in self._next_index_cache:
                next_index = self._next_index_cache[segment]
                segment = f"{segment}[{next_index}]"
            new_segments.append(segment)

        new_attr_path = ".".join(new_segments)
        dst = f"{node_name}.{new_attr_path}"
        src = self._normalize_to_plug(other)

        cmds.connectAttr(src, dst, force=True)

        # --- 接続後にキャッシュをインクリメント ---
        for key in self._next_index_cache:
            self._next_index_cache[key] += 1

    def refresh_next_index(self):
        """
        connect_next_index() が保持しているインデックスキャッシュを破棄する。

        このメソッド以外の方法（cmds.connectAttr 等）でマルチアトリビュートへの
        コネクションが追加・削除された場合に呼び出すことで、
        次回の connect_next_index() 実行時に正しい最終インデックスを再スキャンする。
        """
        self._next_index_cache = None

    def disconnect(self, other: Plug | str | list[str]):
        """
        self から other へ cmds.disconnectAttr()

        Args:
            obj (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._normalize_to_plug(self)
        dst = self._normalize_to_plug(other)

        cmds.disconnectAttr(src, dst)

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

        cmds.connectAttr(src, dst)
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

        cmds.disconnectAttr(src, dst)
        return self

    # addAttr
    def add_attr(self):
        """
        このプラグが参照するアトリビュートを、対象ノードに addAttr() する。
        既に存在する場合はスキップする。
        """
        self._attr.add_attr(self._node.name)


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


def _make_dynamic_plug(node: Node, attr_name: str, parent_attr_path: str = "") -> Plug:
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
    from .lookup import lookup_attr_cls  # 循環インポート回避のため遅延インポート

    attr_cls = lookup_attr_cls(node.name, attr_name)
    if attr_cls is None:
        raise AttributeError(
            f"'{node.name}' にアトリビュート '{attr_name}' の対応クラスが見つかりません"
        )

    try:
        multi = bool(cmds.attributeQuery(attr_name, node=node.name, multi=True))
    except Exception:
        logger.debug(
            f"attributeQuery multi failed for '{node.name}.{attr_name}': defaulting to False"
        )
        multi = False

    try:
        short_name = cmds.attributeQuery(attr_name, node=node.name, shortName=True)
    except Exception:
        logger.debug(
            f"attributeQuery shortName failed for '{node.name}.{attr_name}': using long name"
        )
        short_name = attr_name

    attr_path = f"{parent_attr_path}.{attr_name}" if parent_attr_path else attr_name

    attr = attr_cls(multi=multi)
    object.__setattr__(attr, "name", attr_name)
    object.__setattr__(attr, "long_name", attr_name)
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
    __slots__ = ("_node",)
    # type
    ATTR_TYPE: str = None
    DATA_TYPE: str = None
    # plug
    PLUG_CLS: Type[P] = None
    # name
    name: str = ""
    long_name: str | None = None
    short_name: str | None = None
    # attr
    _attr_path: str = ""

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
        # attr
        #   attr_path
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
            # self.short_name = name
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
        #   instance アクセス
        else:
            # 親が Node
            if hasattr(instance, "NODE_TYPE"):
                object.__setattr__(self, "_node", instance)
            # 親が Attr or Plug
            else:
                instance: Attr = instance
                object.__setattr__(self, "_node", instance._node)
                object.__setattr__(
                    self, "_parent_attr_path", instance._attr_path
                )
                self._set_attr_path(self._parent_attr_path)

        # 戻り値
        #   Node が instance へのアクセス(Plug)
        if self._node.is_instance:
            key = (self.name, self._attr_path)
            if key not in self._node._plug_cache:
                self._node._plug_cache[key] = self.PLUG_CLS(
                    node=self._node,
                    attr=self,
                    attr_path=self._parent_attr_path,
                    multi=self.multi,
                )
            return self._node._plug_cache[key]
        #   Node が class へのアクセス(Attr)
        else:
            return self

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
                self.long_name, node=self._node.name, **kwargs
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
