# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
import math
from numbers import Real
from types import NotImplementedType
from typing import cast, overload, Self, TYPE_CHECKING

from maya.api import OpenMaya as om

from ......._rotation import resolve_rotation_order, RotationOrder
from .....unit.angle.double3 import DoubleAngle3
from ...double3 import Double3
from ..double4 import Double4

if TYPE_CHECKING:
    from .......transform import TransformMatrix

_UNSET = object()


class Quat(Double4):
    """Maya規約のraw Quaternionを保持するimmutableなsnapshot値。"""

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
        """XYZW成分、sequence、またはMQuaternionからsnapshotを作る。"""
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
        """degree単位のEuler回転からQuaternionを作る。"""
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
        """axisとdegree単位のangleからQuaternionを作る。"""
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
        """sourceからtargetへ向けるQuaternionを作る。"""
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
        """transform matrixの回転成分からQuaternionを作る。"""
        from .......transform import TransformMatrix

        return cls(TransformMatrix(value).quat)

    @property
    def quaternion(self) -> om.MQuaternion:
        """内部値のコピーをMQuaternionとして返す。"""
        return om.MQuaternion(self.x, self.y, self.z, self.w)

    @property
    def length_squared(self) -> float:
        return math.fsum(component * component for component in self)

    @property
    def length(self) -> float:
        return math.sqrt(self.length_squared)

    def is_finite(self) -> bool:
        return all(math.isfinite(component) for component in self)

    def is_zero(
        self,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        tolerance_value = self._tolerance(tolerance)
        return self.length <= tolerance_value

    def is_unit(
        self,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        tolerance_value = self._tolerance(tolerance)
        return abs(self.length - 1.0) <= tolerance_value

    def is_equivalent(
        self,
        other: Quat | om.MQuaternion,
        tolerance: int | float = om.MQuaternion.kTolerance,
    ) -> bool:
        """MQuaternionと同じ規則でqと-qを含む等価性を判定する。"""
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
        """指定した回転順序のEuler回転をdegreeで返す。"""
        value = self.quaternion.asEulerRotation()
        value.reorderIt(resolve_rotation_order(rotate_order))
        return DoubleAngle3(
            om.MAngle(value.x, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.y, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.z, om.MAngle.kRadians).asDegrees(),
        )

    def to_axis_angle(self) -> tuple[Double3, float]:
        """axisとdegree単位のangleを返す。"""
        axis, angle = self.quaternion.asAxisAngle()
        return (
            Double3(float(axis.x), float(axis.y), float(axis.z)),
            om.MAngle(angle, om.MAngle.kRadians).asDegrees(),
        )

    def to_transform_matrix(self) -> TransformMatrix:
        """回転だけを持つTransformMatrixを返す。"""
        from .......transform import TransformMatrix

        return TransformMatrix(quat=self)

    def normalized(self) -> Self:
        """MQuaternion.normal()と同じ規則で正規化した値を返す。"""
        return type(self)._from_quaternion(self.quaternion.normal())

    def inverse(self) -> Self:
        """MQuaternion.inverse()と同じ規則で逆元を返す。"""
        return type(self)._from_quaternion(self.quaternion.inverse())

    def conjugate(self) -> Self:
        """共役Quaternionを返す。"""
        return type(self)._from_quaternion(self.quaternion.conjugate())

    def slerp(
        self,
        other: Quat | om.MQuaternion,
        weight: int | float,
    ) -> Self:
        """shortest pathを使って球面線形補間する。"""
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
