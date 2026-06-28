# coding: utf-8
from __future__ import annotations

# maya
import maya.cmds as cmds

# self
from .._core import DAG
from ....attr.define.custom.at.scalar_compound.numeric_compound.double_compound.double3 import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ....attr.define.custom.at.scalar_compound.unit_compound.angle_compound.double_angle3 import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ....attr.define.custom.at.scalar_compound.unit_compound.linear_compound.double_linear3 import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.unit_scalar_range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.at.unit_scalar_range.double_angle import (
    DoubleAngleField,
)


class TranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "tx"),
        ("translateY", "ty"),
        ("translateZ", "tz"),
    )

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateField(
    DoubleLinear3CompoundBaseField[
        TranslateAttrOperator, TranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator


class RotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperaotr"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateAttrOperaotr(
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperaotr, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperaotr
    PLUG_CLS = RotatePlugOperator


class ScalePlugOperator(Double3CompoundBasePlugOperator["ScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "sx"),
        ("scaleY", "sy"),
        ("scaleZ", "sz"),
    )

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
    sz = scaleZ


class ScaleAttrOperator(Double3CompoundBaseAttrOperator[ScalePlugOperator]):
    __slots__ = ()

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
    sz = scaleZ


class ScaleField(
    Double3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator


class Transform(DAG):
    NODE_TYPE = "transform"
    __slots__ = ()

    translate = TranslateField()
    t = translate

    rotate = RotateField()
    r = rotate

    scale = ScaleField()
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
