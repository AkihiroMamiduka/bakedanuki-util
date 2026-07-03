# coding: utf-8
from typing import Self

# maya
from maya.api import OpenMaya as om

# self
from ....modifier import ModifierManager
from .._core import NodeOperator, DEFAULT_VALUE_AUTO_ADD_ATTR


class DAG(NodeOperator):
    __slots__ = (
        "_dag_path",
        "_full_path",
    )

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        auto_add_attr = kwargs.pop(
            "auto_add_attr", DEFAULT_VALUE_AUTO_ADD_ATTR
        )
        super().__init__(*args, auto_add_attr=False, **kwargs)

        # dag_path
        self._dag_path = om.MDagPath.getAPathTo(self.m_obj)
        # full_path
        self._full_path = None

        # auto_add_attr
        if auto_add_attr and self._extra_attributes:
            self._auto_add_extra_attrs()

    @classmethod
    def create(
        cls,
        modifier_manager: ModifierManager,
        name=None,
        auto_add_attr=DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Self:
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

        # ノード作成
        m_obj = modifier_manager.dag_mod.createNode(cls.NODE_TYPE)

        # インスタンス生成
        return cls(
            modifier_manager,
            m_obj=m_obj,
            name=name,
            auto_add_attr=auto_add_attr,
        )

    @property
    def _dag_mod(self) -> om.MDagModifier:
        return self.modifier_manager.dag_mod

    @property
    def full_path(self) -> str:
        if self._full_path is not None:
            return self._full_path
        self._full_path = self._dag_path.fullPathName()
        return self._full_path

    @property
    def _cmd_access_name(self):
        return self.full_path

    def rename(self, **kwargs) -> str:
        new_name = super().rename(**kwargs)

        # rename 後のフルパスを更新
        if self._full_path is not None:
            self._full_path = self._dag_path.fullPathName()

        return new_name
