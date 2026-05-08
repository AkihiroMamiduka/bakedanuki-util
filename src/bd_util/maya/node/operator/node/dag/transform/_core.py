# coding: utf-8
from __future__ import annotations

import maya.cmds as cmds

from .._core import DAG


class Transform(DAG):
    NODE_TYPE = "transform"

    @property
    def parent(self) -> str | None:
        """
        直接の親 transform ノードのロングネームを返す。

        親が存在しない（ワールド直下）場合は ``None`` を返す。

        Returns:
            str | None: 親ノードのロングネーム（例: ``|root|parent``）、または ``None``
        """
        result = cmds.listRelatives(self.name, parent=True, fullPath=True)
        if result:
            return result[0]
        return None

    @property
    def parents_from_root(self) -> list[str]:
        """
        ルートから自身の親までの各階層のロングネームリストを返す（自身は含まない）。

        例: 階層が ``|root|parent1|parent2|myNode`` の場合、
        ``["|root", "|root|parent1", "|root|parent1|parent2"]`` を返す。

        Returns:
            list[str]: ルートから親までの各階層のロングネームリスト
        """
        long = self.long_name  # e.g. "|root|parent1|parent2|myNode"
        parts = [p for p in long.split("|") if p]
        return ["|" + "|".join(parts[: i + 1]) for i in range(len(parts) - 1)]

    @property
    def children(self) -> list[str]:
        """
        直接の子階層の transform ノードのロングネームリストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 直接の子 transform ノードのロングネームリスト
        """
        result = cmds.listRelatives(self.name, children=True, fullPath=True) or []
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def descendants(self) -> list[str]:
        """
        子孫階層の全ての transform ノードのロングネームのフラットなリストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 子孫の transform ノードのロングネームリスト（1次元）
        """
        result = cmds.listRelatives(self.name, allDescendents=True, fullPath=True) or []
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def shapes(self) -> list[str]:
        """
        直接の子階層のシェイプノードのロングネームリストを返す。

        Returns:
            list[str]: 直接の子シェイプノードのロングネームリスト
        """
        return cmds.listRelatives(self.name, shapes=True, fullPath=True) or []
