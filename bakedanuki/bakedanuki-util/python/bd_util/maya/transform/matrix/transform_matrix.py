# coding: utf-8
from __future__ import annotations

from types import NotImplementedType
from typing import Literal

from maya.api import OpenMaya as om

RotationOrder = Literal["xyz", "yzx", "zxy", "xzy", "yxz", "zyx"]

_ROTATION_ORDER_MAP: dict[str, int] = {
    "xyz": om.MEulerRotation.kXYZ,
    "yzx": om.MEulerRotation.kYZX,
    "zxy": om.MEulerRotation.kZXY,
    "xzy": om.MEulerRotation.kXZY,
    "yxz": om.MEulerRotation.kYXZ,
    "zyx": om.MEulerRotation.kZYX,
}


class TransformMatrix:
    """Maya の transform 行列を合成・分解するスナップショット値。"""

    __slots__ = ("_matrix",)

    def __init__(
        self,
        value: (
            TransformMatrix
            | str
            | om.MPlug
            | om.MMatrix
            | om.MTransformationMatrix
        ),
    ) -> None:
        self._matrix = self._to_matrix(value)

    @classmethod
    def _to_matrix(
        cls,
        value: (
            TransformMatrix
            | str
            | om.MPlug
            | om.MMatrix
            | om.MTransformationMatrix
        ),
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
        raise TypeError(
            "value must be TransformMatrix, matrix plug name, MPlug, "
            "MMatrix, or MTransformationMatrix; "
            f"got {type(value).__name__}"
        )

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
    def translate(self) -> tuple[float, float, float]:
        value = self.transformation_matrix.translation(om.MSpace.kTransform)
        return (float(value.x), float(value.y), float(value.z))

    @property
    def rotate(self) -> tuple[float, float, float]:
        """XYZ 順の Euler 回転を degree で返す。"""
        return self.get_rotate(order="xyz")

    def get_rotate(
        self,
        order: RotationOrder = "xyz",
    ) -> tuple[float, float, float]:
        """指定した回転順序の Euler 回転を degree で返す。"""
        if not isinstance(order, str):
            raise TypeError(f"order must be str; got {type(order).__name__}")

        normalized_order = order.lower()
        try:
            maya_order = _ROTATION_ORDER_MAP[normalized_order]
        except KeyError as error:
            supported = ", ".join(_ROTATION_ORDER_MAP)
            raise ValueError(
                f"Unsupported rotation order: {order!r}. "
                f"Expected one of: {supported}"
            ) from error

        value = self.transformation_matrix.rotation()
        value.reorderIt(maya_order)
        return tuple(
            om.MAngle(component, om.MAngle.kRadians).asDegrees()
            for component in (value.x, value.y, value.z)
        )

    @property
    def scale(self) -> tuple[float, float, float]:
        value = self.transformation_matrix.scale(om.MSpace.kTransform)
        return (float(value[0]), float(value[1]), float(value[2]))

    @property
    def shear(self) -> tuple[float, float, float]:
        value = self.transformation_matrix.shear(om.MSpace.kTransform)
        return (float(value[0]), float(value[1]), float(value[2]))

    @property
    def quat(self) -> tuple[float, float, float, float]:
        value = self.transformation_matrix.rotation(asQuaternion=True)
        return (
            float(value.x),
            float(value.y),
            float(value.z),
            float(value.w),
        )

    def inverse(self) -> TransformMatrix:
        """逆行列を新しい ``TransformMatrix`` として返す。"""
        return type(self)(self._matrix.inverse())

    def __mul__(
        self,
        other: object,
    ) -> TransformMatrix | NotImplementedType:
        if not isinstance(other, TransformMatrix):
            return NotImplemented
        return type(self)(self._matrix * other._matrix)
