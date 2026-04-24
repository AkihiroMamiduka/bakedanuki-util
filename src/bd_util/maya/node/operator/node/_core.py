# coding: utf-8
from __future__ import annotations
from typing import Self

# maya
import maya.cmds as cmds

# self
from ..... import logger as u_logger
from .....py.descriptor.immutable import ImmutableDescriptor
from .....py.metaclass.immutable_descriptor import ImmutableDescriptorMeta

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


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


class Node(metaclass=ImmutableDescriptorMeta):
    NODE_TYPE = None
    is_instance = IsInstance()
    _extra_attrs: tuple = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Collect all extra=True Attr descriptors from the class hierarchy.
        # Deduplicate by object identity so that short_name aliases (e.g.
        # ``mw = myWeight``) do not register the same Attr twice.
        extra_attrs = []
        seen_ids = set()
        for klass in cls.__mro__:
            for v in vars(klass).values():
                obj_id = id(v)
                if obj_id not in seen_ids and getattr(v, "extra", False):
                    seen_ids.add(obj_id)
                    extra_attrs.append(v)
        cls._extra_attrs = tuple(extra_attrs)

    def __init__(self, name: str, auto_add_attr: bool = True):
        self.name = name
        self._plug_cache = {}
        if auto_add_attr:
            self._auto_add_extra_attrs()

    def _auto_add_extra_attrs(self):
        """
        extra=True の Attr で、対象ノードに存在しないものを addAttr() する。
        """
        for attr in self._extra_attrs:
            attr.add_attr(self.name)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @classmethod
    def create(cls, name=None) -> Self:
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

        # name が指定されていなければ、NODE_TYPE を名前にする
        if name is None:
            name = cls.NODE_TYPE

        # ノード作成
        node = cmds.createNode(
            cls.NODE_TYPE,
            name=name,
            skipSelect=True,
        )

        # チャンネルボックスでのINPUTS OUTPUTSから表示を消す
        cmds.setAttr(f"{node}.isHistoricallyInteresting", False)

        # インスタンス生成
        return cls(node)

    def exists(self) -> bool:
        return cmds.objExists(self.name)

    def delete(self):
        if self.exists():
            cmds.delete(self.name)

    def rename(
        self,
        new_name: str | None = None,
        search: str | None = None,
        replace: str | None = None,
        prefix: str = "",
        suffix: str = "",
    ) -> str:
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
            replace (str | None): 置換文字列。``search`` と組み合わせて使用する。
            prefix (str): ピュアな名前の先頭に付加する文字列。
            suffix (str): ピュアな名前の末尾に付加する文字列。

        Returns:
            str: リネーム後のノード名（Maya が確定した名前）。

        Raises:
            ValueError: ``new_name`` と ``search`` / ``replace`` が同時に
                指定された場合。
        """
        if new_name is not None and (search is not None or replace is not None):
            raise ValueError(
                "new_name と search/replace を同時に指定することはできません。"
            )

        # ネームスペースとピュアな名前を分離する
        # Maya のノード名は "ns1:ns2:pureName" のような形式になる
        if ":" in self.name:
            namespace, pure_name = self.name.rsplit(":", 1)
            namespace_prefix = namespace + ":"
        else:
            namespace_prefix = ""
            pure_name = self.name

        # ピュアな名前を変換する
        if new_name is not None:
            pure_name = new_name
        elif search is not None:
            replace_str = replace if replace is not None else ""
            pure_name = pure_name.replace(search, replace_str)

        pure_name = prefix + pure_name + suffix

        # Maya でリネームし、確定した名前を self.name に反映する
        result = cmds.rename(self.name, namespace_prefix + pure_name)
        self.name = result
        return self.name
