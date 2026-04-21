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
