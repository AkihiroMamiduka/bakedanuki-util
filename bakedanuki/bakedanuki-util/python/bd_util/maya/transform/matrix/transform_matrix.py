# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
from numbers import Real
from types import NotImplementedType
from typing import cast, Literal, overload, TypeAlias

from maya.api import OpenMaya as om

from ...value import Double3, DoubleAngle3, DoubleLinear3, Quat

RotationOrder = Literal["xyz", "yzx", "zxy", "xzy", "yxz", "zyx"]

MatrixSequence: TypeAlias = (
    Sequence[int | float] | Sequence[Sequence[int | float]]
)
MatrixSource: TypeAlias = (
    str | om.MPlug | om.MMatrix | om.MTransformationMatrix | MatrixSequence
)

_UNSET = object()

_ROTATION_ORDER_MAP: dict[str, int] = {
    "xyz": om.MEulerRotation.kXYZ,
    "yzx": om.MEulerRotation.kYZX,
    "zxy": om.MEulerRotation.kZXY,
    "xzy": om.MEulerRotation.kXZY,
    "yxz": om.MEulerRotation.kYXZ,
    "zyx": om.MEulerRotation.kZYX,
}


def _resolve_rotation_order(order: object) -> int:
    if not isinstance(order, str):
        raise TypeError(f"order must be str; got {type(order).__name__}")

    normalized_order = order.lower()
    try:
        return _ROTATION_ORDER_MAP[normalized_order]
    except KeyError as error:
        supported = ", ".join(_ROTATION_ORDER_MAP)
        raise ValueError(
            f"Unsupported rotation order: {order!r}. "
            f"Expected one of: {supported}"
        ) from error


class TransformMatrix:
    """Mayaのtransform行列を合成・分解するsnapshot値。

    matrix sequenceは、MMatrixと同じrow-major順のflat 16要素、または
    4行4列として受け取る。keyword-onlyのtransform componentからも
    composeMatrix nodeと同じ規則で合成できる。
    """

    __slots__ = ("_matrix",)

    @overload
    def __init__(
        self,
        value: TransformMatrix | MatrixSource,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        translate: Sequence[int | float] | None = None,
        rotate: Sequence[int | float] | None = None,
        quat: Sequence[int | float] | None = None,
        rotate_order: RotationOrder = "xyz",
        scale: Sequence[int | float] | None = None,
        shear: Sequence[int | float] | None = None,
    ) -> None: ...

    def __init__(
        self,
        value: TransformMatrix | MatrixSource | object = _UNSET,
        *,
        translate: Sequence[int | float] | None = None,
        rotate: Sequence[int | float] | None = None,
        quat: Sequence[int | float] | None = None,
        rotate_order: RotationOrder = "xyz",
        scale: Sequence[int | float] | None = None,
        shear: Sequence[int | float] | None = None,
    ) -> None:
        """matrix source、またはtransform componentからsnapshotを作る。

        Args:
            value: TransformMatrix、matrix plug名、MPlug、MMatrix、
                MTransformationMatrix、flat 16要素のmatrix sequence、
                または4行4列のmatrix sequence。
            translate: centimeter単位のXYZ移動。省略時は``(0, 0, 0)``。
            rotate: degree単位のXYZ Euler回転。``quat``とは同時指定不可。
            quat: ``(x, y, z, w)``順のquaternion。``rotate``とは
                同時指定不可。
            rotate_order: Euler回転順序。既定値は``"xyz"``。
            scale: XYZ scale。省略時は``(1, 1, 1)``。
            shear: ``(xy, xz, yz)``順のshear。省略時は``(0, 0, 0)``。

        Raises:
            TypeError: 対応しないsource型の場合。
            ValueError: plugを解決できない場合、matrix値を取得できない場合、
                matrix sequence / componentが不正な場合、sourceとcomponentを
                同時指定した場合、または``rotate``と``quat``を同時指定した場合。
        """
        components = (translate, rotate, quat, scale, shear)
        if value is not _UNSET:
            if any(component is not None for component in components) or (
                rotate_order != "xyz"
            ):
                raise ValueError(
                    "value cannot be combined with transform components"
                )
            self._matrix = self._to_matrix(
                cast(TransformMatrix | MatrixSource, value)
            )
            return

        self._matrix = self._compose_matrix(
            translate=translate,
            rotate=rotate,
            quat=quat,
            rotate_order=rotate_order,
            scale=scale,
            shear=shear,
        )

    @classmethod
    def _to_matrix(
        cls,
        value: TransformMatrix | MatrixSource,
    ) -> om.MMatrix:
        if isinstance(value, cls):
            return value.matrix
        if isinstance(value, om.MTransformationMatrix):
            return om.MMatrix(value.asMatrix())
        if isinstance(value, om.MMatrix):
            return om.MMatrix(value)
        if isinstance(value, str):
            value = cls._get_plug(value)
        if isinstance(value, om.MPlug):
            return cls._matrix_from_plug(value)
        if isinstance(value, Sequence) and not isinstance(
            value,
            (str, bytes, bytearray),
        ):
            return cls._matrix_from_sequence(value)
        raise TypeError(
            "value must be TransformMatrix, matrix plug name, MPlug, "
            "MMatrix, MTransformationMatrix, or a matrix sequence; "
            f"got {type(value).__name__}"
        )

    @classmethod
    def _compose_matrix(
        cls,
        *,
        translate: Sequence[int | float] | None,
        rotate: Sequence[int | float] | None,
        quat: Sequence[int | float] | None,
        rotate_order: RotationOrder,
        scale: Sequence[int | float] | None,
        shear: Sequence[int | float] | None,
    ) -> om.MMatrix:
        if rotate is not None and quat is not None:
            raise ValueError("rotate and quat cannot be specified together")

        maya_rotate_order = _resolve_rotation_order(rotate_order)
        translate_values = cls._normalize_component(
            translate,
            name="translate",
            size=3,
            default=(0.0, 0.0, 0.0),
        )
        scale_values = cls._normalize_component(
            scale,
            name="scale",
            size=3,
            default=(1.0, 1.0, 1.0),
        )
        shear_values = cls._normalize_component(
            shear,
            name="shear",
            size=3,
            default=(0.0, 0.0, 0.0),
        )

        transformation = om.MTransformationMatrix()
        transformation.setTranslation(
            om.MVector(*translate_values),
            om.MSpace.kTransform,
        )

        if rotate is not None:
            rotate_values = cls._normalize_component(
                rotate,
                name="rotate",
                size=3,
                default=(0.0, 0.0, 0.0),
            )
            rotate_radians = tuple(
                om.MAngle(value, om.MAngle.kDegrees).asRadians()
                for value in rotate_values
            )
            transformation.setRotation(
                om.MEulerRotation(*rotate_radians, maya_rotate_order)
            )
        elif quat is not None:
            quat_values = cls._normalize_component(
                quat,
                name="quat",
                size=4,
                default=(0.0, 0.0, 0.0, 1.0),
            )
            if not any(quat_values):
                raise ValueError("quat must not be a zero quaternion")
            transformation.setRotation(om.MQuaternion(*quat_values))

        transformation.setScale(scale_values, om.MSpace.kTransform)
        transformation.setShear(shear_values, om.MSpace.kTransform)
        return om.MMatrix(transformation.asMatrix())

    @staticmethod
    def _normalize_component(
        value: object,
        *,
        name: str,
        size: int,
        default: tuple[float, ...],
    ) -> tuple[float, ...]:
        if value is None:
            return default
        if not isinstance(value, Sequence) or isinstance(
            value,
            (str, bytes, bytearray),
        ):
            raise ValueError(
                f"{name} must contain exactly {size} numeric values"
            )
        components = cast(Sequence[object], value)
        if len(components) != size or any(
            not isinstance(component, Real) for component in components
        ):
            raise ValueError(
                f"{name} must contain exactly {size} numeric values"
            )
        numeric_components = cast(Sequence[Real], components)
        return tuple(float(component) for component in numeric_components)

    @staticmethod
    def _matrix_from_sequence(value: MatrixSequence) -> om.MMatrix:
        error_message = (
            "matrix sequence must contain exactly 16 numeric values "
            "or four rows of four numeric values"
        )

        if len(value) == 16:
            normalized_value: object = tuple(value)
        elif len(value) == 4:
            rows: list[tuple[int | float, ...]] = []
            for row in value:
                if not isinstance(row, Sequence) or isinstance(
                    row,
                    (str, bytes, bytearray),
                ):
                    raise ValueError(error_message)
                if len(row) != 4:
                    raise ValueError(error_message)
                rows.append(tuple(row))
            normalized_value = tuple(rows)
        else:
            raise ValueError(error_message)

        try:
            return om.MMatrix(normalized_value)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError(error_message) from error

    @staticmethod
    def _get_plug(plug_name: str) -> om.MPlug:
        selection = om.MSelectionList()
        try:
            selection.add(plug_name)
            return selection.getPlug(0)
        except RuntimeError as error:
            raise ValueError(
                f"Could not resolve matrix plug: {plug_name!r}"
            ) from error

    @staticmethod
    def _matrix_from_plug(plug: om.MPlug) -> om.MMatrix:
        attribute = plug.attribute()
        is_typed_matrix = (
            attribute.hasFn(om.MFn.kTypedAttribute)
            and om.MFnTypedAttribute(attribute).attrType()
            == om.MFnData.kMatrix
        )
        is_matrix_attribute = attribute.hasFn(om.MFn.kMatrixAttribute)
        if not is_typed_matrix and not is_matrix_attribute:
            raise TypeError(f"Plug must be a matrix plug: {plug.name()}")

        try:
            matrix_data = om.MFnMatrixData(plug.asMObject())
            return om.MMatrix(matrix_data.matrix())
        except (RuntimeError, TypeError) as error:
            raise ValueError(
                f"Plug does not contain a matrix value: {plug.name()}"
            ) from error

    @property
    def matrix(self) -> om.MMatrix:
        """内部値のコピーを ``MMatrix`` として返す。"""
        return om.MMatrix(self._matrix)

    @property
    def transformation_matrix(self) -> om.MTransformationMatrix:
        """内部値のコピーを ``MTransformationMatrix`` として返す。"""
        return om.MTransformationMatrix(self._matrix)

    @property
    def translate(self) -> DoubleLinear3:
        value = self.transformation_matrix.translation(om.MSpace.kTransform)
        return DoubleLinear3(float(value.x), float(value.y), float(value.z))

    @property
    def rotate(self) -> DoubleAngle3:
        """XYZ 順の Euler 回転を degree で返す。"""
        return self.get_rotate(order="xyz")

    def get_rotate(
        self,
        order: RotationOrder = "xyz",
    ) -> DoubleAngle3:
        """指定した回転順序の Euler 回転を degree で返す。"""
        maya_order = _resolve_rotation_order(order)

        value = self.transformation_matrix.rotation()
        value.reorderIt(maya_order)
        return DoubleAngle3(
            om.MAngle(value.x, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.y, om.MAngle.kRadians).asDegrees(),
            om.MAngle(value.z, om.MAngle.kRadians).asDegrees(),
        )

    @property
    def scale(self) -> Double3:
        value = self.transformation_matrix.scale(om.MSpace.kTransform)
        return Double3(float(value[0]), float(value[1]), float(value[2]))

    @property
    def shear(self) -> Double3:
        value = self.transformation_matrix.shear(om.MSpace.kTransform)
        return Double3(float(value[0]), float(value[1]), float(value[2]))

    @property
    def quat(self) -> Quat:
        value = self.transformation_matrix.rotation(asQuaternion=True)
        return Quat(
            float(value.x),
            float(value.y),
            float(value.z),
            float(value.w),
        )

    def inverse(self) -> TransformMatrix:
        """逆行列を新しい ``TransformMatrix`` として返す。"""
        return type(self)(self._matrix.inverse())

    @overload
    def __mul__(self, other: TransformMatrix) -> TransformMatrix: ...

    @overload
    def __mul__(self, other: om.MMatrix) -> TransformMatrix: ...

    def __mul__(
        self,
        other: object,
    ) -> TransformMatrix | NotImplementedType:
        if isinstance(other, TransformMatrix):
            other_matrix = other._matrix
        elif isinstance(other, om.MMatrix):
            other_matrix = other
        else:
            return NotImplemented
        return type(self)(self._matrix * other_matrix)

    @overload
    def __rmul__(self, other: om.MMatrix) -> TransformMatrix: ...

    @overload
    def __rmul__(self, other: TransformMatrix) -> TransformMatrix: ...

    def __rmul__(
        self,
        other: object,
    ) -> TransformMatrix | NotImplementedType:
        if isinstance(other, TransformMatrix):
            other_matrix = other._matrix
        elif isinstance(other, om.MMatrix):
            other_matrix = other
        else:
            return NotImplemented
        return type(self)(other_matrix * self._matrix)
