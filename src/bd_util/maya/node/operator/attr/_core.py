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
        attr: Type[A],
        attr_path: str,
        multi: bool = False,
        index: int = None,
    ):
        self._node: Node = node
        self._attr: Type[A] = attr
        self.multi: bool = multi
        self.index: int = index
        self._attr_path: str = self._create_attr_path(
            parent_attr_path=attr_path
        )

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

    # [] アクセス
    def __getitem__(
        self,
        index: int,
    ) -> Self:
        """
        [index]指定された、自身の Plug を返す

        Args:
            index (int): インデックス

        Raises:
            AttributeError: 親アトリビュートが[index]アクセスされている場合、
                            さらに[index]アクセスするアトリビュートは無い為、エラー

        Returns:
            Self: [index]指定された自身の plug
        """
        if self.name.endswith("]"):
            raise AttributeError(
                f"{self.plug} は [{index}] アクセスができません"
            )

        plug: Self = type(self)(
            node=self._node,
            attr=self._attr,
            attr_path=self._attr._attr_path,
            index=index,
        )
        return plug

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


class Attr(ImmutableDescriptor, Generic[P]):
    __slots__ = ("_node",)
    ATTR_TYPE: str = None
    PLUG_CLS: Type[P] = None
    name: str = ""
    _attr_path: str = ""
    mutli: bool = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.PLUG_CLS is None:
            raise NotImplementedError(
                f"{cls.__name__} は、 PLUG_CLS が定義されていません。定義してください。"
            )

    def __init__(self, multi=False):
        self.mutli = multi
        self._node: Node = None
        self._parent_attr_path: str = ""

    # __set_name__
    def _on_set_name(self, owner: Any, name: str):
        """
        __set_name__ 内で、実行されるメソッド

        Args:
            owner (Any): 親のクラス
            name (str): セットされている変数名
        """
        self.name = name
        self._attr_path = name

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
            if isinstance(instance, Node):
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
            return self.PLUG_CLS(
                node=self._node,
                attr=self,
                attr_path=self._parent_attr_path,
                multi=self.mutli,
            )
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
