# coding: utf-8
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Type, Generic, Self, Any, overload

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from ..node._core import NodeOperator

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class AccessMeta(type):

    def __getitem__(cls, key: str):
        return getattr(cls, key)


A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


class BaseAccess:

    def __init__(
        self,
        name: str,
        owner=None,
        instance=None,
        parent=None,
    ):
        self.name = name
        self.owner = owner
        self.instance = instance
        self.parent = parent

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"


class PlugOperator(Generic[A], ABC):
    __slots__ = (
        "_node",
        "_oprt_attr",
        "__attr_path",
        "_parent_attr_path",
        "parent_oprt_plug",
        "multi",
        "index",
        "_child_index",
        "_fn_attr",
        "_m_plug",
        "_array_m_plug",
        "_next_index_cache",
        "_next_index",
    )

    _REQUIRED_CMDS_ADD_ATTR: bool = False

    def __init__(
        self,
        node: NodeOperator,
        oprt_attr: A,
        parent_attr_path: str,
        multi: bool = False,
        index: int = None,
        parent_oprt_plug: PlugOperator | None = None,
    ):
        # args ----------------------------------------------------------------
        # multi
        self.multi: bool = multi
        # index
        self.index: int = index
        # node
        self._node: NodeOperator = node
        # attr
        self._oprt_attr: A = oprt_attr
        self.__attr_path: str = ""
        self._parent_attr_path: str = parent_attr_path
        self._child_index: int | None = oprt_attr.child_index
        # plug
        self.parent_oprt_plug: PlugOperator | None = parent_oprt_plug
        # args ----------------------------------------------------------------

        # attr
        self._fn_attr: om.MFnAttribute | None = None
        # plug
        self._m_plug: om.MPlug | None = None
        # array plug
        self._array_m_plug: om.MPlug | None = None
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
        return self.long_name

    @property
    def long_name(self) -> str:
        """
        自身のロングアトリビュート名

        Returns:
            str: 自身のロングアトリビュート名
        """
        name = self._oprt_attr.long_name
        # if self.index is not None:
        #     name = f"{name}[{self.index}]"
        return name

    @property
    def short_name(self) -> str:
        """
        自身のショートアトリビュート名

        Returns:
            str: 自身のショートアトリビュート名
        """
        name = self._oprt_attr.short_name
        # if self.index is not None:
        #     name = f"{name}[{self.index}]"
        return name

    @property
    def plug_name(self) -> str:
        """
        プラグ名

        Returns:
            str: 自身のプラグ名
        """
        return f"{self._node.name}.{self._attr_path}"

    @property
    def plug(self) -> om.MPlug:
        """
        MPlug インスタンスを取得する

        Returns:
            om.MPlug: MPlug インスタンス
        """
        # キャッシュがあればそれを返す
        if self._m_plug is not None:
            return self._m_plug

        # plug を取得する
        #   親アトリビュートがあり、index がない場合は、親の plug から自身の plug を探す
        if self.parent_oprt_plug is not None and self.index is None:
            parent_plug = self.parent_oprt_plug.plug
            plug = None
            if self._child_index is not None:
                try:
                    plug = parent_plug.child(self._child_index)
                except (IndexError, RuntimeError):
                    plug = None
            if plug is None:
                plug = self._find_child_plug(parent_plug, self.long_name)
            if plug is None:
                raise AttributeError(
                    "'{}' というアトリビュートは '{}' に存在しません".format(
                        self.long_name,
                        parent_plug,
                    )
                )
        #   それ以外は、ノードから直接 plug を探す
        else:
            plug = self._node.fn_node.findPlug(self.long_name, False)

        # index があれば、elementByLogicalIndex で plug を置き換える
        if self.index is not None:
            plug = plug.elementByLogicalIndex(self.index)

        # plug をキャッシュする
        self._m_plug = plug

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
        if self._array_m_plug is None:
            self._array_m_plug = self.plug.array()
        #   キャッシュを返す
        return self._array_m_plug

    # type
    @property
    def type(self) -> str:
        """
        アトリビュートの型

        Returns:
            str: アトリビュートの型
        """
        return self._oprt_attr.ATTR_TYPE

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

    # value
    @property
    def value_direct(self) -> Any:
        """
        アトリビュートの値をゲットする

        Returns:
            Any: アトリビュートの値
        """
        return self.get()

    @value_direct.setter
    def value_direct(self, value: Any):
        """
        アトリビュートに値をセットする

        Args:
            value (Any): セットする値
        """
        self.set_direct(value)

    # enum
    @property
    def enum_name(self) -> str | None:
        """
        列挙型アトリビュートの列挙名をゲットする

        Returns:
            str | None: 列挙型アトリビュートの列挙名。列挙型でない場合は None。
        """
        return self._oprt_attr.enum_full_name

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
            if self.index is not None:
                raise AttributeError(
                    f"{self.plug} は [{key}] アクセスができません"
                )
            plug: Self = type(self)(
                node=self._node,
                oprt_attr=self._oprt_attr,
                parent_attr_path=self._oprt_attr._attr_path,
                multi=self._oprt_attr.multi,
                index=key,
                parent_oprt_plug=self,
            )
            return plug
        elif key == next:
            if self.index is not None:
                raise AttributeError(
                    f"{self.plug} は [{key}] アクセスができません"
                )
            plug: Self = type(self)(
                node=self._node,
                oprt_attr=self._oprt_attr,
                parent_attr_path=self._oprt_attr._attr_path,
                multi=self._oprt_attr.multi,
                index=self._get_next_index(),
                parent_oprt_plug=self,
            )
            return plug
        elif isinstance(key, str):
            # attr_name, index = _parse_attr_segment(key)
            # plug = _make_dynamic_plug(self._node, attr_name, self._attr_path)
            # if index is not None:
            #     plug = plug[index]
            # return plug
            return getattr(self, key)
        raise TypeError(f"キーの型が不正です: {type(key)}")

    @property
    def _attr_path(self) -> str:
        """
        attr_path を作成する

        Args:
            parent_attr_path (str): 親アトリビュートの attr_path

        Returns:
            str: 自身の attr_path
        """
        # キャッシュがあればそれを返す
        if self.__attr_path:
            return self.__attr_path

        # 親の attr_path がなければ、自身の名前を返す
        if not self._parent_attr_path:
            return self.name

        # mulit_attr の index アクセスの場合
        if self.index is not None:
            self.__attr_path = f"{self._parent_attr_path}[{self.index}]"
            return self.__attr_path

        # attr_path を生成する
        return f"{self._parent_attr_path}.{self.name}"

    # str
    def __str__(self) -> str:
        return str(self.plug_name)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.plug_name}>"

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

    def set_direct(self, value: Any):
        """
        プラグに値を直接セットする: サブクラスでオーバーライドして、適切な型の値をセットするようにする
        set() メソッドは、DGModifier を使用して値をセットするのに対し、
        こちらは直接値をセットする為、即時反映され Undo が効かないことに注意が必要。
        """
        pass

    # connect
    def _normalize_to_plug(
        self, obj: PlugOperator | str | list[str]
    ) -> om.MPlug:
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
        if isinstance(obj, PlugOperator):
            obj: PlugOperator = obj
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

    def connect(self, other: PlugOperator | str | list[str]):
        """
        self から other へ connect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self.plug
        dst = self._normalize_to_plug(other)

        self._node._dg_mod.connect(src, dst)

    def _get_next_index(self) -> int:
        result = 0
        # キャッシュがあればそれを返す
        if self._next_index is not None:
            result = self._next_index
        # キャッシュがなければ Maya に問い合わせる
        else:
            indices = self.plug.getExistingArrayAttributeIndices()
            if indices:
                result = max(indices) + 1
            # キャッシュする
            self._next_index = result

        # インクリメントする
        self._next_index += 1

        # 戻り値
        return result

    def _get_next_plug(self) -> om.MPlug:
        return self.plug.elementByLogicalIndex(self._get_next_index())

    def connect_next_index(self, other: PlugOperator | str | list[str]):
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

    def disconnect(self, other: PlugOperator | str | list[str]):
        """
        self から other へ disconnect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._normalize_to_plug(self)
        dst = self._normalize_to_plug(other)

        self._node._dg_mod.disconnect(src, dst)

    def __gt__(
        self, other: PlugOperator | str | list[str]
    ) -> PlugOperator | str | list[str]:
        """
        self > other 演算子オーバーライド：接続

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.connect(other)
        return other

    def __lt__(self, other: PlugOperator | str | list[str]) -> Self:
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

    def __or__(self, other: PlugOperator | str | list[str]):
        """
        self | other 演算子オーバーライド：切断

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.disconnect(other)
        return other

    def __ror__(self, other: PlugOperator | str | list[str]):
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
        if self._oprt_attr.multi:
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
        return self._node.fn_node.hasAttribute(self.long_name)

    # add
    def add_attr(self):
        """
        対象ノードに、このアトリビュートを追加する
        既に存在する場合はスキップする
        """
        pass

    def cmds_add_attr(self, **kwargs):
        """
        cmds.addAttr() によるアトリビュートの追加

        api.OpenMaya では、 addAttribute() ができないものは、こちらで追加します。
        渡された引数はそのまま cmds.addAttr() に引き渡します。
        attributeType と dataType は、自動追加されますので、
        それ以外の引数を渡してください。
        """
        # ノードが存在しない場合はスキップ
        if not self._node.exists():
            return

        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # kwargs に追加
        #   attributeType/dataType
        kwargs["attributeType"] = self._oprt_attr.ATTR_TYPE
        if self._oprt_attr.DATA_TYPE is not None:
            kwargs["dataType"] = self._oprt_attr.DATA_TYPE
        #   longName/shortName
        kwargs["longName"] = self._oprt_attr.long_name
        if self._oprt_attr.short_name is not None:
            kwargs["shortName"] = self._oprt_attr.short_name

        # add
        cmds.addAttr(
            self._node._cmd_access_name,
            **kwargs,
        )


# def _parse_attr_segment(segment: str) -> tuple[str, int | None]:
#     """
#     "attrName[0]" や "attrName" 形式の文字列を、アトリビュート名とインデックスに分解する。

#     Args:
#         segment (str): "attrName" または "attrName[index]" 形式の文字列

#     Returns:
#         tuple[str, int | None]: (アトリビュート名, インデックス or None)

#     Raises:
#         ValueError: "[" と "]" の対応が取れていないまたは index が整数でない場合
#     """
#     if "[" not in segment:
#         if "]" in segment:
#             raise ValueError(
#                 f"アトリビュートキーの書式が不正です: '{segment}'"
#                 " (例: 'attrName[0]')"
#             )
#         if not segment:
#             raise ValueError("アトリビュートキーのセグメントが空文字列です")
#         return segment, None

#     if not segment.endswith("]"):
#         raise ValueError(
#             f"アトリビュートキーの書式が不正です: '{segment}'"
#             " (例: 'attrName[0]')"
#         )
#     attr_name, bracket = segment.split("[", 1)
#     index_str = bracket[:-1]  # "]" を除去
#     try:
#         index = int(index_str)
#     except ValueError:
#         raise ValueError(
#             f"アトリビュートキーのインデックスが整数ではありません: '{segment}'"
#         )
#     return attr_name, index


# def _make_dynamic_plug(
#     node: NodeOperator, attr_name: str, parent_attr_path: str = ""
# ) -> PlugOperator:
#     """
#     ノードとアトリビュート名から、動的に Plug インスタンスを生成して返す。

#     lookup_attr_cls でアトリビュート型を特定し、対応する Attr インスタンスを
#     動的に生成する。デスクリプタ経由のキャッシュと干渉しないよう、
#     生成した Plug はノードのキャッシュには格納しない。

#     Args:
#         node (Node): 対象ノードのインスタンス
#         attr_name (str): アトリビュート名（短縮名または長名）
#         parent_attr_path (str): 親アトリビュートの attr_path。
#             最上位アトリビュートの場合は空文字列を渡す。

#     Returns:
#         Plug: 対応する Plug インスタンス

#     Raises:
#         AttributeError: ノードにアトリビュートが存在しない、または
#             対応する Attr クラスが見つからない場合
#     """
#     from .lookup import (
#         lookup_attr_cls,
#     )  # 循環インポート回避のため遅延インポート

#     attr_cls = lookup_attr_cls(node.name, attr_name)
#     if attr_cls is None:
#         raise AttributeError(
#             f"'{node.name}' にアトリビュート '{attr_name}' の対応クラスが見つかりません"
#         )

#     try:
#         long_name = cmds.attributeQuery(
#             attr_name, node=node.name, longName=True
#         )
#     except RuntimeError:
#         raise RuntimeError(
#             "{} '{}.{}': {}".format(
#                 "attributeQuery longName failed for",
#                 node.name,
#                 attr_name,
#                 "using input name",
#             )
#         )
#         long_name = attr_name

#     try:
#         multi = bool(
#             cmds.attributeQuery(long_name, node=node.name, multi=True)
#         )
#     except RuntimeError:
#         raise RuntimeError(
#             "{} '{}.{}': {}".format(
#                 "attributeQuery multi failed for",
#                 node.name,
#                 long_name,
#                 "defaulting to False",
#             )
#         )
#         multi = False

#     try:
#         short_name = cmds.attributeQuery(
#             long_name, node=node.name, shortName=True
#         )
#     except RuntimeError:
#         raise RuntimeError(
#             "{} '{}.{}': {}".format(
#                 "attributeQuery shortName failed for",
#                 node.name,
#                 long_name,
#                 "using long name",
#             )
#         )
#         short_name = long_name

#     attr_path = (
#         f"{parent_attr_path}.{long_name}" if parent_attr_path else long_name
#     )

#     attr = attr_cls(multi=multi)
#     object.__setattr__(attr, "name", long_name)
#     object.__setattr__(attr, "long_name", long_name)
#     object.__setattr__(attr, "_short_name", short_name)
#     object.__setattr__(attr, "_attr_path", attr_path)
#     object.__setattr__(attr, "_node", node)

#     return attr.PLUG_CLS(
#         node=node,
#         attr=attr,
#         attr_path=parent_attr_path,
#         multi=multi,
#     )


class AttrOperator(Generic[P]):
    __slots__ = (
        "node_cls",
        "name",
        "long_name",
        "short_name",
        "_attr_path",
        "_parent_attr_path",
        "oprt_parent",
        "multi",
        "extra",
        "default_value",
        "min_value",
        "max_value",
        "soft_min_value",
        "soft_max_value",
        "enum_name",
        "number_of_children",
        "readable",
        "writable",
        "category",
        "child_index",
    )
    # type
    ATTR_TYPE: str = None
    DATA_TYPE: str = None
    # name
    name: str
    long_name: str | None
    # attr
    _attr_path: str

    def __init__(
        self,
        node_cls: Type[NodeOperator] | None = None,
        oprt_parent: str | None = None,
        name: str = "",
        long_name: str = "",
        short_name: str = "",
        attr_path: str = "",
        parent_attr_path: str = "",
        multi: bool = False,
        extra: bool = False,
        default_value: Any = None,
        min_value: Any = None,
        max_value: Any = None,
        soft_min_value: Any = None,
        soft_max_value: Any = None,
        enum_name: str | None = None,
        number_of_children: int | None = None,
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
        child_index: int | None = None,
    ):
        # node
        self.node_cls: Type[NodeOperator] | None = node_cls
        # name
        self.name: str = name
        self.long_name: str = long_name
        self.short_name: str = short_name
        # attr
        #   attr_path
        self._attr_path: str = attr_path
        self._parent_attr_path: str = parent_attr_path
        #   parent
        self.oprt_parent: str | None = oprt_parent
        #   multi
        self.multi: bool = multi
        #   extra attr flag
        self.extra: bool = extra
        # extra attr info
        self.default_value: Any = default_value
        self.min_value: Any = min_value
        self.max_value: Any = max_value
        self.soft_min_value: Any = soft_min_value
        self.soft_max_value: Any = soft_max_value
        self.enum_name: str | None = enum_name
        self.number_of_children: int | None = number_of_children
        self.readable: bool | None = readable
        self.writable: bool | None = writable
        self.category: str | None = category
        self.child_index: int | None = child_index

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.ATTR_TYPE is None:
            raise NotImplementedError(
                f"{cls.__name__} は、 ATTR_TYPE が定義されていません。定義してください。"
            )
        # if cls.PLUG_CLS is None:
        #     raise NotImplementedError(
        #         f"{cls.__name__} は、 PLUG_CLS が定義されていません。定義してください。"
        #     )

    # [] アクセス
    def __getitem__(
        self,
        key: str,
    ) -> Self:
        return getattr(self, key)

    # # __set_name__
    # def _on_set_name(self, owner: Any, name: str):
    #     """
    #     __set_name__ 内で、実行されるメソッド

    #     Args:
    #         owner (Any): 親のクラス
    #         name (str): セットされている変数名
    #     """
    #     # name をセット
    #     if self.long_name is None:
    #         #  name, _attr_path, long_name にセット
    #         self.name = name
    #         self._attr_path = name
    #         self.long_name = name
    #     else:
    #         # short name をセット
    #         object.__setattr__(self, "_short_name", name)

    # # __get__
    # def __get__(self, instance: object | None, owner: type) -> Self | P:
    #     """
    #     属性アクセスされた際に実行されるメソッド
    #     Node へのアクセスが、
    #     クラスアクセスの場合、 Attr を返し、
    #     インスタンスアクセスの場合、 Plug を返す

    #     Args:
    #         instance (object | None): インスタンスオブジェクト
    #         owner (type): 親クラス

    #     Returns:
    #         Self | P: Attr or Plug
    #     """
    #     # node, attr_path をセットする
    #     #   class アクセス
    #     if instance is None:
    #         # Node
    #         object.__setattr__(self, "_node", owner)
    #     #   instance アクセス
    #     else:
    #         # 親が Node
    #         if hasattr(instance, "NODE_TYPE"):
    #             object.__setattr__(self, "_node", instance)
    #         # 親が Attr or Plug
    #         else:
    #             instance: AttrOperator[P] | PlugOperator[A] = instance
    #             # compound の子アトリビュートを node クラスに再定義する際に、自身を返す
    #             if instance._node is None:
    #                 return self
    #             object.__setattr__(self, "_node", instance._node)
    #             object.__setattr__(
    #                 self, "_parent_attr_path", instance._attr_path
    #             )
    #             self._set_attr_path(self._parent_attr_path)

    #     # 戻り値
    #     #   Node が instance へのアクセス(Plug)
    #     if self._node.is_instance:
    #         key = (self.name, self._attr_path)
    #         parent_plug = None
    #         if self._parent_attr_path:
    #             parent_plug = instance
    #         if key not in self._node._plug_cache:
    #             self._node._plug_cache[key] = self.PLUG_CLS(
    #                 node=self._node,
    #                 attr=self,
    #                 attr_path=self._parent_attr_path,
    #                 multi=self.multi,
    #                 parent_plug=parent_plug,
    #             )
    #         return self._node._plug_cache[key]
    #     #   Node が class へのアクセス(Attr)
    #     else:
    #         return self

    # def find_child_attribute(
    #     self,
    #     compound_attr_obj: om.MObject,
    #     name: str,
    # ) -> om.MObject | None:
    #     if compound_attr_obj.isNull():
    #         raise RuntimeError(
    #             "{} {}: {}, {}: {}, {}: {}".format(
    #                 "compound_attr_obj が無効です。",
    #                 "self._node.node_class",
    #                 self._node.node_class,
    #                 "self.long_name",
    #                 self.long_name,
    #                 "compound_attr_obj.apiType()",
    #                 compound_attr_obj.apiType(),
    #             )
    #         )
    #     compound_fn = om.MFnCompoundAttribute(compound_attr_obj)

    #     for i in range(compound_fn.numChildren()):
    #         child_attr_obj = compound_fn.child(i)
    #         fn_attr = om.MFnAttribute(child_attr_obj)
    #         if fn_attr.name == name:
    #             return child_attr_obj

    #     return None

    # # attr_path
    # def _set_attr_path(self, parent_attr_path: str):
    #     """
    #     attr_path をセットする

    #     Args:
    #         parent_attr_path (str): 親の attr_path
    #     """
    #     # 親の attr_path がなければ終了する
    #     if not parent_attr_path:
    #         return

    #     # attr_path を生成する
    #     attr_path = f"{parent_attr_path}.{self.name}"

    #     # attr_path をセットする
    #     object.__setattr__(self, "_attr_path", attr_path)

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

    # # attr info
    # def _query_attr_info(self, **kwargs) -> Any:
    #     """
    #     cmds.attributeQuery を安全に実行し、結果を返す。
    #     ノードのインスタンスが設定されていない場合は None を返す。

    #     Returns:
    #         Any: cmds.attributeQuery の結果。取得できない場合は None。
    #     """
    #     if self._node is None or not self._node.is_instance:
    #         return None
    #     try:
    #         return cmds.attributeQuery(
    #             self.long_name, node=self._node._cmd_access_name, **kwargs
    #         )
    #     except Exception:
    #         return None

    # @property
    # def short_name(self) -> str | None:
    #     """アトリビュートのショート名"""
    #     if self._short_name is None:
    #         object.__setattr__(self, "_short_name", self.long_name)
    #     return self._short_name

    # @property
    # def default_value(self) -> Any:
    #     """アトリビュートのデフォルト値"""
    #     if self.extra:
    #         return self._default_value
    #     return self._query_attr_info(listDefault=True)

    # @property
    # def min_value(self) -> Any:
    #     """アトリビュートの最小値"""
    #     if self.extra:
    #         return self._min_value
    #     return self._query_attr_info(minimum=True)

    # @property
    # def max_value(self) -> Any:
    #     """アトリビュートの最大値"""
    #     if self.extra:
    #         return self._max_value
    #     return self._query_attr_info(maximum=True)

    # @property
    # def soft_min_value(self) -> Any:
    #     """アトリビュートのソフト最小値"""
    #     if self.extra:
    #         return self._soft_min_value
    #     return self._query_attr_info(softMin=True)

    # @property
    # def soft_max_value(self) -> Any:
    #     """アトリビュートのソフト最大値"""
    #     if self.extra:
    #         return self._soft_max_value
    #     return self._query_attr_info(softMax=True)

    # @property
    # def enum_full_name(self) -> str | None:
    #     """列挙型アトリビュートの列挙名"""
    #     if self._enum_name is not None:
    #         return self._enum_name
    #     return self._query_attr_info(listEnum=True)

    # @property
    # def number_of_children(self) -> int | None:
    #     """コンパウンドアトリビュートの子アトリビュート数"""
    #     if self.extra:
    #         return self._number_of_children
    #     return self._query_attr_info(numberOfChildren=True)

    # @property
    # def parent(self) -> str | None:
    #     """親アトリビュート名"""
    #     if self.extra:
    #         return self._parent
    #     return self._query_attr_info(listParent=True)

    # @property
    # def readable(self) -> bool | None:
    #     """アトリビュートが読み取り可能かどうか"""
    #     if self.extra:
    #         return self._readable
    #     return self._query_attr_info(readable=True)

    # @property
    # def writable(self) -> bool | None:
    #     """アトリビュートが書き込み可能かどうか"""
    #     if self.extra:
    #         return self._writable
    #     return self._query_attr_info(writable=True)

    # @property
    # def category(self) -> str | None:
    #     """アトリビュートのカテゴリ"""
    #     if self.extra:
    #         return self._category
    #     return self._query_attr_info(categories=True)


class AccessType:
    field = 0
    attr = 1
    plug = 2


class AttributeField(ImmutableDescriptor, Generic[A, P]):
    __slots__ = (
        "_node_cls",
        "_node",
        "oprt_parent",
        "name",
        "long_name",
        "_short_name",
        "_attr_path",
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
        "_readable",
        "_writable",
        "_category",
        "_child_index",
    )

    ATTR_CLS: type[A]
    PLUG_CLS: type[P]

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
        readable: bool | None = None,
        writable: bool | None = None,
        category: str | None = None,
    ):
        # node
        self._node_cls: type[NodeOperator] | None = None
        self._node: NodeOperator | None = None

        # parent
        self.oprt_parent: A | P | None = None

        # name
        self.long_name = None
        self._short_name = None

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
        self._readable: bool | None = readable
        self._writable: bool | None = writable
        self._category: str | None = category
        self._child_index: int | None = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.ATTR_CLS is None:
            raise NotImplementedError(
                f"{cls.__name__} は、 ATTR_CLS が定義されていません。定義してください。"
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
        if self._child_index is None:
            object.__setattr__(
                self, "_child_index", self._find_child_index(owner)
            )
        # name をセット
        if self.long_name is None:
            #  name, _attr_path, long_name にセット
            self.name = name
            self.long_name = name
            self._attr_path = name
        else:
            # short name をセット
            object.__setattr__(self, "_short_name", name)

    def _find_child_index(self, owner: Any) -> int | None:
        """
        owner 内での AttributeField の定義順を返す。

        同じ Field を short name として別名定義している場合は、
        最初に現れた名前だけを数える。
        """
        seen_ids = set()
        index = 0
        for value in vars(owner).values():
            if all(
                c.__name__ != "AttributeField" for c in type(value).__mro__
            ):
                continue

            obj_id = id(value)
            if obj_id in seen_ids:
                continue
            if value is self:
                return index

            seen_ids.add(obj_id)
            index += 1

        return None

    # __get__
    @overload
    def __get__(self, instance: None, owner: type) -> A: ...

    @overload
    def __get__(
        self,
        instance: AttrOperator[Any],
        owner: type,
    ) -> A: ...

    @overload
    def __get__(
        self,
        instance: PlugOperator[Any],
        owner: type,
    ) -> P: ...

    @overload
    def __get__(
        self,
        instance: AttributeField[Any],
        owner: type,
    ) -> Self: ...

    @overload
    def __get__(self, instance: NodeOperator, owner: type) -> P: ...

    def __get__(
        self,
        instance: (
            object
            | NodeOperator
            | AttrOperator[Any]
            | PlugOperator[Any]
            | AttributeField[Any]
            | None
        ),
        owner: type,
    ) -> A | P | Self:
        """
        属性アクセスされた際に実行されるメソッド
        Node へのアクセスが、
        クラスアクセスの場合、 Attr を返し、
        インスタンスアクセスの場合、 Plug を返す

        Args:
            instance (object | None): インスタンスオブジェクト
            owner (type): 親クラス

        Returns:
            A | P: AttrOperator or PlugOperator
        """
        access_type: int | None = None
        # node, attr_path をセットする
        #   class アクセス(Attr)
        if instance is None:
            # 親が Node(Attr)
            access_type = AccessType.attr
            object.__setattr__(self, "_node_cls", owner)
        #   instance アクセス(Attr or Plug)
        else:
            # 親が Node(Plug)
            if hasattr(instance, "NODE_TYPE"):
                access_type = AccessType.plug
                object.__setattr__(self, "_node_cls", owner)
                object.__setattr__(self, "_node", instance)
            # 親が Attr or Plug or Field
            else:
                instance: A | P = instance
                # 各種セットする
                object.__setattr__(self, "oprt_parent", instance)
                object.__setattr__(
                    self, "_parent_attr_path", instance._attr_path
                )
                self._set_attr_path(self._parent_attr_path)
                #   親が Attr
                mro = owner.__mro__
                #   親が Plug
                if any(c.__name__ == "PlugOperator" for c in mro):
                    access_type = AccessType.plug
                    instance: P = instance
                    object.__setattr__(self, "_node", instance._node)
                elif any(c.__name__ == "AttrOperator" for c in mro):
                    instance: A = instance
                    access_type = AccessType.attr
                #   親が Field
                else:
                    access_type = AccessType.field

        # 戻り値
        #   class 定義時ののアクセス(Field)
        if access_type == AccessType.field:
            return self
        #   Node が instance へのアクセス(Plug)（キャッシュ済）
        plug_cache_key = None
        if access_type == AccessType.plug:
            plug_cache_key = (self.name, self._attr_path)
            cached_plug = self._node._plug_cache.get(plug_cache_key)
            if cached_plug is not None:
                return cached_plug
        #   AttrOperator を生成
        oprt_attr = self.ATTR_CLS(
            node_cls=self._node_cls,
            oprt_parent=self.oprt_parent,
            name=self.name,
            long_name=self.long_name,
            short_name=self.short_name,
            attr_path=self._attr_path,
            parent_attr_path=self._parent_attr_path,
            multi=self.multi,
            extra=self.extra,
            default_value=self._default_value,
            min_value=self._min_value,
            max_value=self._max_value,
            soft_min_value=self._soft_min_value,
            soft_max_value=self._soft_max_value,
            enum_name=self._enum_name,
            number_of_children=self._number_of_children,
            readable=self._readable,
            writable=self._writable,
            category=self._category,
            child_index=self._child_index,
        )
        #   Node が instance へのアクセス(Plug)（キャッシュ無：新規）
        if access_type == AccessType.plug:
            # 親 Plug があればセットする
            parent_oprt_plug = None
            if self._parent_attr_path:
                parent_oprt_plug = instance
            # Plug を生成してキャッシュする
            plug = self.PLUG_CLS(
                node=self._node,
                oprt_attr=oprt_attr,
                parent_attr_path=self._parent_attr_path,
                multi=self.multi,
                parent_oprt_plug=parent_oprt_plug,
            )
            self._node._plug_cache[plug_cache_key] = plug
            return plug
        #   Node が class へのアクセス(Attr)
        elif access_type == AccessType.attr:
            return oprt_attr

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

    @property
    def short_name(self) -> str | None:
        """アトリビュートのショート名"""
        if self._short_name is None:
            object.__setattr__(self, "_short_name", self.long_name)
        return self._short_name
