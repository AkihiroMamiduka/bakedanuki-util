# coding: utf-8
from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import TypeVar, Type, Generic, Self, Any, Protocol, overload

# maya
from maya import cmds
from maya.api import OpenMaya as om

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from .keyframe import KeyframeManager
from ..node._core import NodeOperator

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class AccessMeta(type):

    def __getitem__(cls, key: str):
        return getattr(cls, key)


A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")

_ConnectionTarget = TypeVar(
    "_ConnectionTarget",
    bound="PlugOperator[Any] | str | list[str]",
)

_NextValue = TypeVar("_NextValue")
_NextDefault = TypeVar("_NextDefault")


class _NextIndexSentinel(Protocol):

    @overload
    def __call__(
        self,
        iterator: Iterator[_NextValue],
        /,
    ) -> _NextValue: ...

    @overload
    def __call__(
        self,
        iterator: Iterator[_NextValue],
        default: _NextDefault,
        /,
    ) -> _NextValue | _NextDefault: ...


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
        "_indexed_plug_cache",
        "_next_index",
        "_keyframe_manager",
    )

    _REQUIRED_CMDS_ADD_ATTR: bool = False

    def __init__(
        self,
        node: NodeOperator,
        oprt_attr: A,
        parent_attr_path: str,
        multi: bool = False,
        index: int | None = None,
        parent_oprt_plug: PlugOperator[Any] | None = None,
    ):
        # args ----------------------------------------------------------------
        # multi
        self.multi: bool = multi
        # index
        self.index: int | None = index
        # node
        self._node: NodeOperator = node
        # attr
        self._oprt_attr: A = oprt_attr
        self.__attr_path: str = ""
        self._parent_attr_path: str = parent_attr_path
        self._child_index: int | None = oprt_attr.child_index
        # plug
        self.parent_oprt_plug: PlugOperator[Any] | None = parent_oprt_plug
        # args ----------------------------------------------------------------

        # attr
        self._fn_attr: om.MFnAttribute | None = None
        # plug
        self._m_plug: om.MPlug | None = None
        # array plug
        self._array_m_plug: om.MPlug | None = None
        self._indexed_plug_cache: dict[int, Self] | None = None
        self._next_index: int | None = None
        self._keyframe_manager: KeyframeManager | None = None

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
        #   __getitem__() が作成した index plug は、親 multi plug から直接取得する
        parent_oprt_plug = self.parent_oprt_plug
        index = self.index
        indexed_from_parent = False
        if (
            parent_oprt_plug is not None
            and index is not None
            and self._oprt_attr is parent_oprt_plug._oprt_attr
        ):
            plug = parent_oprt_plug.plug.elementByLogicalIndex(index)
            indexed_from_parent = True
        # 親アトリビュートがあり、index がない場合は、親の plug から自身の plug を探す
        elif parent_oprt_plug is not None:
            parent_plug = parent_oprt_plug.plug
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
        if index is not None and not indexed_from_parent:
            plug = plug.elementByLogicalIndex(index)

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
        key: int | str | _NextIndexSentinel,
    ) -> Self:
        """
        [index] 指定（int）または文字列によるサブアトリビュートアクセス（str）を行い、
        対応する Plug を返す。

        int を渡すと既存の multi アトリビュート用インデックスアクセスとして動作する。
        str を渡すと、サブアトリビュート名から動的に Plug を生成して返す。
        str には "subAttr" または "subAttr[0]" 形式を使用できる。

        Args:
            key (int | str | _NextIndexSentinel):
                インデックス（int）、サブアトリビュート名（str）、
                または次の空き index を表す builtin の next

        Raises:
            AttributeError: 親アトリビュートが [index] アクセスされている場合に
                            さらに int インデックスアクセスしようとした場合
            AttributeError: 指定した文字列アトリビュートがノードに存在しない場合
            TypeError: int / str / next 以外の値が渡された場合

        Returns:
            Plug: 対応する Plug インスタンス
        """
        if isinstance(key, int):
            if self.index is not None:
                raise AttributeError(
                    f"{self.plug} は [{key}] アクセスができません"
                )
            indexed_plug_cache = self._indexed_plug_cache
            if indexed_plug_cache is not None:
                cached_plug = indexed_plug_cache.get(key)
                if cached_plug is not None:
                    return cached_plug
            plug: Self = type(self)(
                node=self._node,
                oprt_attr=self._oprt_attr,
                parent_attr_path=self._oprt_attr._attr_path,
                multi=self._oprt_attr.multi,
                index=key,
                parent_oprt_plug=self,
            )
            if indexed_plug_cache is None:
                indexed_plug_cache = {}
                self._indexed_plug_cache = indexed_plug_cache
            indexed_plug_cache[key] = plug
            return plug
        elif key == next:
            if self.index is not None:
                raise AttributeError(
                    f"{self.plug} は [{key}] アクセスができません"
                )
            return self[self._get_next_index()]
        elif isinstance(key, str):
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

    def _to_anim_curve_value(self, value: Any) -> Any:
        return value

    def _from_anim_curve_value(self, value: Any) -> Any:
        return value

    def _get_keyframe_manager(self) -> KeyframeManager:
        if self._keyframe_manager is None:
            self._keyframe_manager = KeyframeManager(
                plug=self.plug,
                plug_name=self.plug_name,
                value_converter=self._to_anim_curve_value,
                value_reader=self._from_anim_curve_value,
            )
        return self._keyframe_manager

    # connect
    def _normalize_to_plug(
        self, obj: PlugOperator[Any] | str | list[str]
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
            plug = obj._m_plug
            if plug is not None:
                return plug
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

    def connect(self, other: PlugOperator[Any] | str | list[str]):
        """
        self から other へ connect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._m_plug
        if src is None:
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
        plug = self._m_plug
        if plug is None:
            plug = self.plug
        return plug.elementByLogicalIndex(self._get_next_index())

    def connect_next_index(
        self,
        other: PlugOperator[Any] | str | list[str],
    ):
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

    def disconnect(self, other: PlugOperator[Any] | str | list[str]):
        """
        self から other へ disconnect()

        Args:
            other (Plug | str | list[str]): 対象のオブジェクト
        """
        src = self._m_plug
        if src is None:
            src = self.plug
        dst = self._normalize_to_plug(other)

        self._node._dg_mod.disconnect(src, dst)

    def __gt__(
        self,
        other: _ConnectionTarget,
    ) -> _ConnectionTarget:
        """
        self > other 演算子オーバーライド：接続
            .connect() の糖衣構文
            大量処理で少しでも(メソッド1個分の)速度を詰めるなら src.connect(dst)
            さらに詰めるなら Plug をローカル変数に保持して再利用するのが良いと思います。

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.connect(other)
        return other

    def __lt__(
        self,
        other: PlugOperator[Any] | str | list[str],
    ) -> Self:
        """
        other > self 演算子のオーバーライド：接続

        Args:
            other (Plug | str | list[str]): 切断元の対象

        Returns:
            Self: self をそのまま返す
        """
        dst = self._m_plug
        if dst is None:
            dst = self.plug
        src = self._normalize_to_plug(other)

        self._node._dg_mod.connect(src, dst)
        return self

    def __or__(
        self,
        other: _ConnectionTarget,
    ) -> _ConnectionTarget:
        """
        self | other 演算子オーバーライド：切断

        Args:
            other (Plug | str | list[str]): 接続先の対象

        Returns:
            (Plug | str | list[str]): other をそのまま返す
        """
        self.disconnect(other)
        return other

    def __ror__(
        self,
        other: PlugOperator[Any] | str | list[str],
    ) -> Self:
        """
        other | self 演算子のオーバーライド：切断

        Args:
            other (Plug | str | list[str]): 切断元の対象

        Returns:
            Self: self をそのまま返す
        """
        src = self._normalize_to_plug(other)
        dst = self._m_plug
        if dst is None:
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

    # add attr options
    def _apply_mfn_attr_options(self, fn_attr: om.MFnAttribute):
        if self.multi:
            fn_attr.array = True

        readable = self._oprt_attr.readable
        if readable is not None:
            fn_attr.readable = readable

        writable = self._oprt_attr.writable
        if writable is not None:
            fn_attr.writable = writable

        category = self._oprt_attr.category
        if category is not None:
            fn_attr.addToCategory(category)

    def _cmds_add_attr_option_kwargs(self) -> dict[str, Any]:
        kwargs = {}
        if self.multi:
            kwargs["multi"] = True

        readable = self._oprt_attr.readable
        if readable is not None:
            kwargs["readable"] = readable

        writable = self._oprt_attr.writable
        if writable is not None:
            kwargs["writable"] = writable

        category = self._oprt_attr.category
        if category is not None:
            kwargs["category"] = category

        return kwargs

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
        for key, value in self._cmds_add_attr_option_kwargs().items():
            kwargs.setdefault(key, value)

        # add
        cmds.addAttr(
            self._node._cmd_access_name,
            **kwargs,
        )


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

    # [] アクセス
    def __getitem__(
        self,
        key: str,
    ) -> Self:
        return getattr(self, key)

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


class AttributeField(ImmutableDescriptor, Generic[A, P]):
    __slots__ = (
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
        long_name: str | None = None,
        short_name: str | None = None,
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
        # parent
        self.oprt_parent: A | P | None = None

        # name
        self.long_name = None
        self._short_name = None
        if long_name is not None:
            self.long_name = long_name
        if short_name is not None:
            self._short_name = short_name

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
        if not self._attr_path:
            #  name, _attr_path, long_name にセット
            self.name = name
            if self.long_name is None:
                self.long_name = name
            self._attr_path = self.long_name
        else:
            # short name をセット
            if self._short_name is None:
                object.__setattr__(self, "_short_name", name)

        if isinstance(self.oprt_parent, AttributeField):
            parent_attr_path = self.oprt_parent._attr_path
            if parent_attr_path:
                object.__setattr__(self, "_parent_attr_path", parent_attr_path)
                self._set_attr_path(parent_attr_path)

    def _find_child_index(self, owner: Any) -> int | None:
        """
        owner 内での AttributeField の定義順を返す。

        同じ Field を short name として別名定義している場合は、
        最初に現れた名前だけを数える。
        """
        seen_ids = set()
        index = 0
        for value in vars(owner).values():
            if not isinstance(value, AttributeField):
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
        instance: AttributeField[Any, Any],
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
            | AttributeField[Any, Any]
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
        if isinstance(instance, NodeOperator):
            attr_path = self._attr_path
            plug_cache = instance._plug_cache
            if plug_cache is None:
                plug_cache = {}
                instance._plug_cache = plug_cache
            else:
                cached_plug = plug_cache.get(attr_path)
                if cached_plug is not None:
                    return cached_plug

            oprt_attr = owner._attributes_map_by_long_name.get(self.long_name)
            if oprt_attr is None:
                oprt_attr = self.ATTR_CLS(
                    node_cls=owner,
                    oprt_parent=self.oprt_parent,
                    name=self.name,
                    long_name=self.long_name,
                    short_name=self.short_name,
                    attr_path=attr_path,
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

            plug = self.PLUG_CLS(
                node=instance,
                oprt_attr=oprt_attr,
                parent_attr_path=self._parent_attr_path,
                multi=self.multi,
            )
            plug_cache[attr_path] = plug
            return plug

        if isinstance(instance, PlugOperator):
            name = self.name
            long_name = self.long_name
            short_name = self.short_name
            parent_attr_path = instance._attr_path
            child_long_name = getattr(instance, "child_long_name", None)
            if child_long_name is not None:
                long_name = child_long_name(name, self._child_index)
                short_name = instance.child_short_name(name, self._child_index)
            attr_path = self._attr_path
            if parent_attr_path:
                attr_path = f"{parent_attr_path}.{long_name}"

            node = instance._node
            plug_cache = node._plug_cache
            if plug_cache is None:
                plug_cache = {}
                node._plug_cache = plug_cache
            else:
                cached_plug = plug_cache.get(attr_path)
                if cached_plug is not None:
                    return cached_plug

            oprt_attr = self.ATTR_CLS(
                node_cls=instance._oprt_attr.node_cls,
                oprt_parent=instance,
                name=name,
                long_name=long_name,
                short_name=short_name,
                attr_path=attr_path,
                parent_attr_path=parent_attr_path,
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
            plug = self.PLUG_CLS(
                node=node,
                oprt_attr=oprt_attr,
                parent_attr_path=parent_attr_path,
                multi=self.multi,
                parent_oprt_plug=instance,
            )
            plug_cache[attr_path] = plug
            return plug

        oprt_parent = self.oprt_parent
        parent_attr_path = self._parent_attr_path
        attr_path = self._attr_path

        # node class, attr_path を解決する
        #   class アクセス(Attr)
        if instance is None:
            # 親が Node(Attr)
            node_cls = owner
        #   親が Attr
        elif isinstance(instance, AttrOperator):
            oprt_parent = instance
            parent_attr_path = instance._attr_path
            if parent_attr_path:
                attr_path = f"{parent_attr_path}.{self.name}"
            node_cls = instance.node_cls
        #   親が Field
        elif isinstance(instance, AttributeField):
            # class 定義時の alias 構築だけは Field 自体へ反映する
            object.__setattr__(self, "oprt_parent", instance)
            object.__setattr__(self, "_parent_attr_path", instance._attr_path)
            self._set_attr_path(self._parent_attr_path)
            return self
        else:
            raise TypeError(
                f"Unsupported attribute access type: {type(instance)}"
            )

        #   AttrOperator を生成
        oprt_attr = self.ATTR_CLS(
            node_cls=node_cls,
            oprt_parent=oprt_parent,
            name=self.name,
            long_name=self.long_name,
            short_name=self.short_name,
            attr_path=attr_path,
            parent_attr_path=parent_attr_path,
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
