# coding: utf-8
from __future__ import annotations

import maya.cmds as cmds

from .._core import DAG


class Transform(DAG):
    NODE_TYPE = "transform"

    @property
    def parent(self) -> str | None:
        """
        直接の親 transform ノード名を返す。

        親が存在しない（ワールド直下）場合は ``None`` を返す。

        Returns:
            str | None: 親ノード名、または ``None``
        """
        result = cmds.listRelatives(self.name, parent=True)
        if result:
            return result[0]
        return None

    @property
    def parents_from_root(self) -> list[str]:
        """
        ルート親から直接の親までの親ノード名リストを返す。

        例: 階層が ``|root|parent1|parent2|myNode`` の場合、
        ``["root", "parent1", "parent2"]`` を返す。

        Returns:
            list[str]: ルートから直親までの親ノード名リスト
        """
        long = self.long_name  # e.g. "|root|parent1|parent2|myNode"
        parts = [p for p in long.split("|") if p]
        return parts[:-1]

    @property
    def children(self) -> list[str]:
        """
        直接の子階層の transform ノード名リストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 直接の子 transform ノード名リスト
        """
        result = cmds.listRelatives(self.name, children=True) or []
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def descendants(self) -> list[str]:
        """
        子孫階層の全ての transform ノード名のフラットなリストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 子孫の transform ノード名リスト（1次元）
        """
        result = cmds.listRelatives(self.name, allDescendents=True) or []
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def shapes(self) -> list[str]:
        """
        直接の子階層のシェイプノード名リストを返す。

        Returns:
            list[str]: 直接の子シェイプノード名リスト
        """
        return cmds.listRelatives(self.name, shapes=True) or []
