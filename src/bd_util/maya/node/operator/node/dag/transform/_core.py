# coding: utf-8
from __future__ import annotations

# maya
import maya.cmds as cmds

# self
from .._core import DAG
from ....attr.at.double3 import Double3AttrOperator, Double3PlugOperator
from ....attr.at.double import DoubleAttrOperator
from ....attr.at.double_linear import DoubleLinearAttrOperator
from ....attr.at.double_angle import DoubleAngleAttrOperator


class TranslatePlug(Double3PlugOperator["TranslateAttr"]):
    __slots__ = ()

    translateX = DoubleLinearAttrOperator()
    tx = translateX

    translateY = DoubleLinearAttrOperator()
    ty = translateY

    translateZ = DoubleLinearAttrOperator()
    tz = translateZ


class TranslateAttr(Double3AttrOperator[TranslatePlug]):
    __slots__ = ()

    PLUG_CLS = TranslatePlug

    translateX = DoubleLinearAttrOperator()
    tx = translateX

    translateY = DoubleLinearAttrOperator()
    ty = translateY

    translateZ = DoubleLinearAttrOperator()
    tz = translateZ


class RotatePlug(Double3PlugOperator["RotateAttr"]):
    __slots__ = ()


class RotateAttr(Double3AttrOperator[RotatePlug]):
    __slots__ = ()

    PLUG_CLS = RotatePlug

    rotateX = DoubleAngleAttrOperator()
    rx = rotateX

    rotateY = DoubleAngleAttrOperator()
    ry = rotateY

    rotateZ = DoubleAngleAttrOperator()
    rz = rotateZ


class ScalePlug(Double3PlugOperator["ScaleAttr"]):
    __slots__ = ()


class ScaleAttr(Double3AttrOperator[ScalePlug]):
    __slots__ = ()

    PLUG_CLS = ScalePlug

    scaleX = DoubleAttrOperator()
    sx = scaleX

    scaleY = DoubleAttrOperator()
    sy = scaleY

    scaleZ = DoubleAttrOperator()
    sz = scaleZ


class Transform(DAG):
    NODE_TYPE = "transform"
    __slots__ = ()

    translate = TranslateAttr()
    t = translate

    rotate = RotateAttr()
    r = rotate

    scale = ScaleAttr()
    s = scale

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
        parts = [p for p in self.long_name.split("|") if p]
        return ["|" + "|".join(parts[: i + 1]) for i in range(len(parts) - 1)]

    @property
    def children(self) -> list[str]:
        """
        直接の子階層の transform ノードのロングネームリストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 直接の子 transform ノードのロングネームリスト
        """
        result = (
            cmds.listRelatives(self.name, children=True, fullPath=True) or []
        )
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def descendants(self) -> list[str]:
        """
        子孫階層の全ての transform ノードのロングネームのフラットなリストを返す。
        シェイプノードは含まない。

        Returns:
            list[str]: 子孫の transform ノードのロングネームリスト（1次元）
        """
        result = (
            cmds.listRelatives(self.name, allDescendents=True, fullPath=True)
            or []
        )
        return [c for c in result if not cmds.objectType(c, isAType="shape")]

    @property
    def shapes(self) -> list[str]:
        """
        直接の子階層のシェイプノードのロングネームリストを返す。

        Returns:
            list[str]: 直接の子シェイプノードのロングネームリスト
        """
        return cmds.listRelatives(self.name, shapes=True, fullPath=True) or []
