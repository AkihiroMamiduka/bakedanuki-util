# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
import math
from numbers import Real
from types import NotImplementedType
from typing import cast, overload, Self, TYPE_CHECKING

from maya.api import OpenMaya as om

from ...._rotation import resolve_rotation_order, RotationOrder
from ..numeric.double.double3 import Double3
from ..scalar4 import Scalar4
from ..unit.angle.double3 import DoubleAngle3

if TYPE_CHECKING:
    from ....transform import TransformMatrix

_UNSET = object()


class Quat(Scalar4[float]):
    """Maya の XYZW 順で四元数を保持する不変のスナップショット。"""

    __slots__ = ()

    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(
        self,
        x: int | float,
        y: int | float,
        z: int | float,
        w: int | float,
    ) -> None: ...

    @overload
    def __init__(
        self,
        x: Quat | om.MQuaternion | Sequence[int | float],
    ) -> None: ...

    def __init__(
        self,
        x: object = _UNSET,
        y: object = _UNSET,
        z: object = _UNSET,
        w: object = _UNSET,
    ) -> None:
        """恒等回転、4 成分、または既存の四元数から値を作る。

        引数なしでは ``(0, 0, 0, 1)``。単独引数には Quat、
        MQuaternion、または XYZW 順の 4 要素を指定する。

        Raises:
            TypeError: 引数の組み合わせや成分の型が不正な場合。
            ValueError: 成分の個数が 4 でない場合。
        """
        values: tuple[float, ...]
        if x is _UNSET and y is _UNSET and z is _UNSET and w is _UNSET:
            values = (0.0, 0.0, 0.0, 1.0)
        elif y is _UNSET and z is _UNSET and w is _UNSET:
            if isinstance(x, Quat):
                values = x.as_tuple()
            elif isinstance(x, om.MQuaternion):
                values = (
                    float(x.x),
                    float(x.y),
                    float(x.z),
                    float(x.w),
                )
            else:
                values = self._numeric_sequence(
                    x,
                    name="value",
                    size=4,
                )
        elif all(value is not _UNSET for value in (x, y, z, w)):
            values = self._numeric_sequence(
                (x, y, z, w),
                name="components",
                size=4,
            )
        else:
            raise TypeError(
                "Quat requires no arguments, one quaternion source, "
                "or four numeric components"
            )

        object.__setattr__(self, "x", values[0])
        object.__setattr__(self, "y", values[1])
        object.__setattr__(self, "z", values[2])
        object.__setattr__(self, "w", values[3])

    @classmethod
    def from_euler(
        cls,
        rotate: Sequence[int | float],
        rotate_order: RotationOrder = "xyz",
    ) -> Self:
        """度数法の Euler 回転から四元数を作る。

        Args:
            rotate: X、Y、Z の角度。単位は度。
            rotate_order: Maya の回転順序。既定は ``xyz``。

        Returns:
            対応する四元数。
        """
        values = cls._numeric_sequence(rotate, name="rotate", size=3)
        radians = tuple(
            om.MAngle(value, om.MAngle.kDegrees).asRadians()
            for value in values
        )
        quaternion = om.MEulerRotation(
            *radians,
            resolve_rotation_order(rotate_order),
        ).asQuaternion()
        return cls._from_quaternion(quaternion)

    @classmethod
    def from_axis_angle(
        cls,
        axis: Sequence[int | float],
        angle: int | float,
    ) -> Self:
        """回転軸と度数法の角度から四元数を作る。

        Args:
            axis: 3 成分の回転軸。
            angle: 回転角。単位は度。

        Returns:
            対応する四元数。
        """
        axis_values = cls._numeric_sequence(axis, name="axis", size=3)
        angle_value = cls._numeric_value(angle, name="angle")
        radians = om.MAngle(
            angle_value,
            om.MAngle.kDegrees,
        ).asRadians()
        return cls._from_quaternion(
            om.MQuaternion(radians, om.MVector(*axis_values))
        )

    @classmethod
    def from_vectors(
        cls,
        source: Sequence[int | float],
        target: Sequence[int | float],
        factor: int | float = 1.0,
    ) -> Self:
        """source を target に向ける四元数を作る。

        Args:
            source: 元の 3 成分ベクトル。
            target: 向け先の 3 成分ベクトル。
            factor: 回転量に適用する係数。既定は 1.0。

        Returns:
            対応する四元数。
        """
        source_values = cls._numeric_sequence(
            source,
            name="source",
            size=3,
        )
        target_values = cls._numeric_sequence(
            target,
            name="target",
            size=3,
        )
        factor_value = cls._numeric_value(factor, name="factor")
        return cls._from_quaternion(
            om.MQuaternion(
                om.MVector(*source_values),
                om.MVector(*target_values),
                factor_value,
            )
        )

    @classmethod
    def from_matrix(
        cls,
        value: (
            TransformMatrix
            | om.MMatrix
            | om.MTransformationMatrix
            | Sequence[int | float]
            | Sequence[Sequence[int | float]]
        ),
    ) -> Self:
        """変換行列の回転成分から四元数を作る。

        Args:
            value: Maya の行列または 16 要素・4 行 4 列の行列値。

        Returns:
            抽出した回転を保持する四元数。
        """
        from ....transform import TransformMatrix

        return cls(TransformMatrix(value).quat)

    @property
    def quaternion(self) -> om.MQuaternion:
        """成分値のコピーを MQuaternion として返す。"""
        return om.MQuaternion(self.x, self.y, self.z, self.w)

    @property
    def length_squared(self) -> float:
        """4 成分の長さの二乗。"""
        return math.fsum(component * component for component in self)

    @property
    def length(self) -> float:
        """4 成分の長さ。"""
        return math.sqrt(self.length_squared)

    def is_finite(self) -> bool:
        """すべての成分が有限値かを返す。"""
        return all(math.isfinite(component) for component in self)

    def is_zero(
        self,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        """四元数の長さが許容値以下かを返す。

        Args:
            tolerance: 有限かつ非負の許容値。

        Raises:
            ValueError: 許容値が有限でない、または負の場合。
        """
        tolerance_value = self._tolerance(tolerance)
        return self.length <= tolerance_value

    def is_unit(
        self,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        """四元数の長さが 1 に十分近いかを返す。

        Args:
            tolerance: 有限かつ非負の許容値。

        Raises:
            ValueError: 許容値が有限でない、または負の場合。
        """
        tolerance_value = self._tolerance(tolerance)
        return abs(self.length - 1.0) <= tolerance_value

    def is_equivalent(
        self,
        other: Quat | om.MQuaternion,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        """MQuaternion と同じ規則で q と -q の等価性も判定する。

        Args:
            other: 比較する四元数。
            tolerance: 有限かつ非負の許容値。

        Returns:
            同じ回転を許容値内で表す場合は True。

        Raises:
            TypeError: 比較対象や許容値の型が不正な場合。
            ValueError: 許容値が有限でない、または負の場合。
        """
        other_quaternion = self._operand_quaternion(other)
        if other_quaternion is None:
            raise TypeError(
                "other must be Quat or MQuaternion; "
                f"got {type(other).__name__}"
            )
        return bool(
            self.quaternion.isEquivalent(
                other_quaternion,
                self._tolerance(tolerance),
            )
        )

    def to_euler(
        self,
        rotate_order: RotationOrder = "xyz",
    ) -> DoubleAngle3:
        """指定した回転順序の Euler 角を度数法で返す。

        Args:
            rotate_order: Maya の回転順序。既定は ``xyz``。

        Returns:
            X、Y、Z の角度を保持する DoubleAngle3。
        """
        value = self.quaternion.asEulerRotation()
        value.reorderIt(resolve_rotation_order(rotate_order))
        return DoubleAngle3(
            om.MAngle(value.x, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.y, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.z, om.MAngle.kRadians).asDegrees(),
        )

    def to_axis_angle(self) -> tuple[Double3, float]:
        """回転軸と度数法の角度を返す。

        Returns:
            回転軸の Double3 と、度単位の回転角。
        """
        axis, angle = self.quaternion.asAxisAngle()
        return (
            Double3(float(axis.x), float(axis.y), float(axis.z)),
            om.MAngle(angle, om.MAngle.kRadians).asDegrees(),
        )

    def to_transform_matrix(self) -> TransformMatrix:
        """この回転だけを持つ TransformMatrix を返す。"""
        from ....transform import TransformMatrix

        return TransformMatrix(quat=self)

    def normalized(self) -> Self:
        """MQuaternion.normal() と同じ規則で正規化した値を返す。"""
        return type(self)._from_quaternion(self.quaternion.normal())

    def inverse(self) -> Self:
        """MQuaternion.inverse() と同じ規則で逆元を返す。"""
        return type(self)._from_quaternion(self.quaternion.inverse())

    def conjugate(self) -> Self:
        """共役四元数を返す。"""
        return type(self)._from_quaternion(self.quaternion.conjugate())

    def slerp(
        self,
        other: Quat | om.MQuaternion,
        weight: int | float,
    ) -> Self:
        """最短経路で球面線形補間する。

        Args:
            other: 補間先の四元数。
            weight: 補間係数。0.0 は現在値、1.0 は補間先。

        Returns:
            補間後の新しい Quat。

        Raises:
            TypeError: 補間先や係数の型が不正な場合。
        """
        other_quaternion = self._operand_quaternion(other)
        if other_quaternion is None:
            raise TypeError(
                "other must be Quat or MQuaternion; "
                f"got {type(other).__name__}"
            )
        weight_value = self._numeric_value(weight, name="weight")
        return type(self)._from_quaternion(
            om.MQuaternion.slerp(
                self.quaternion,
                other_quaternion,
                weight_value,
            )
        )

    def __neg__(self) -> Self:
        return type(self)._from_quaternion(-self.quaternion)

    @overload
    def __mul__(self, other: Quat) -> Self: ...

    @overload
    def __mul__(self, other: om.MQuaternion) -> Self: ...

    def __mul__(self, other: object) -> Self | NotImplementedType:
        other_quaternion = self._operand_quaternion(other)
        if other_quaternion is None:
            return NotImplemented
        return type(self)._from_quaternion(self.quaternion * other_quaternion)

    @overload
    def __rmul__(self, other: Quat) -> Self: ...

    @overload
    def __rmul__(self, other: om.MQuaternion) -> Self: ...

    def __rmul__(self, other: object) -> Self | NotImplementedType:
        other_quaternion = self._operand_quaternion(other)
        if other_quaternion is None:
            return NotImplemented
        return type(self)._from_quaternion(other_quaternion * self.quaternion)

    @classmethod
    def _from_quaternion(cls, value: om.MQuaternion) -> Self:
        return cls(
            float(value.x),
            float(value.y),
            float(value.z),
            float(value.w),
        )

    @staticmethod
    def _operand_quaternion(value: object) -> om.MQuaternion | None:
        if isinstance(value, Quat):
            return value.quaternion
        if isinstance(value, om.MQuaternion):
            return om.MQuaternion(value)
        return None

    @classmethod
    def _numeric_sequence(
        cls,
        value: object,
        *,
        name: str,
        size: int,
    ) -> tuple[float, ...]:
        if not isinstance(value, Sequence) or isinstance(
            value,
            (str, bytes, bytearray),
        ):
            raise TypeError(
                f"{name} must contain exactly {size} numeric values"
            )
        sequence = cast(Sequence[object], value)
        if len(sequence) != size:
            raise ValueError(
                f"{name} must contain exactly {size} numeric values"
            )
        return tuple(
            cls._numeric_value(component, name=f"{name}[{index}]")
            for index, component in enumerate(sequence)
        )

    @staticmethod
    def _numeric_value(value: object, *, name: str) -> float:
        if not isinstance(value, Real):
            raise TypeError(
                f"{name} must be numeric; got {type(value).__name__}"
            )
        return float(value)

    @classmethod
    def _tolerance(cls, value: object) -> float:
        tolerance = cls._numeric_value(value, name="tolerance")
        if not math.isfinite(tolerance) or tolerance < 0.0:
            raise ValueError("tolerance must be finite and non-negative")
        return tolerance
