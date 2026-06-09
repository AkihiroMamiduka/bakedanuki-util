# coding: utf-8
from typing import Self

# maya
from maya.api import OpenMaya as om

# self
from .._core import NodeOperator, DEFAULT_VALUE_AUTO_ADD_ATTR


class DAG(NodeOperator):
    __slots__ = (
        "_dag_mod",
        "_dag_path",
        "_full_path",
    )

    def __init__(
        self,
        *args,
        dag_mod: om.MDagModifier = om.MDagModifier(),
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        # dag_mod
        self._dag_mod = dag_mod
        # dag_path
        self._dag_path = om.MDagPath.getAPathTo(self.m_obj)
        # full_path
        self._full_path = None

    @classmethod
    def create(
        cls,
        dg_mod: om.MDGModifier,
        dag_mod: om.MDagModifier,
        name=None,
        auto_add_attr=DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> Self:
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

        # ノード作成
        m_obj = dag_mod.createNode(cls.NODE_TYPE)
        # ノード名を変更
        if name:
            dg_mod.renameNode(m_obj, name)

        # インスタンス生成
        return cls(
            dg_mod,
            dag_mod=dag_mod,
            m_obj=m_obj,
            name=name,
            auto_add_attr=auto_add_attr,
        )

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
