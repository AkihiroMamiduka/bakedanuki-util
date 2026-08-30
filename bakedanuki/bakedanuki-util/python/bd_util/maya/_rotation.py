# coding: utf-8
from typing import Literal

from maya.api import OpenMaya as om

RotationOrderName = Literal["xyz", "yzx", "zxy", "xzy", "yxz", "zyx"]
RotationOrder = RotationOrderName | int

_ROTATION_ORDER_MAP: dict[str, int] = {
    "xyz": om.MEulerRotation.kXYZ,
    "yzx": om.MEulerRotation.kYZX,
    "zxy": om.MEulerRotation.kZXY,
    "xzy": om.MEulerRotation.kXZY,
    "yxz": om.MEulerRotation.kYXZ,
    "zyx": om.MEulerRotation.kZYX,
}


def resolve_rotation_order(rotate_order: object) -> int:
    if isinstance(rotate_order, str):
        normalized_order = rotate_order.lower()
        try:
            return _ROTATION_ORDER_MAP[normalized_order]
        except KeyError as error:
            supported = ", ".join(_ROTATION_ORDER_MAP)
            raise ValueError(
                f"Unsupported rotation order: {rotate_order!r}. "
                f"Expected one of: {supported}"
            ) from error

    if isinstance(rotate_order, bool) or not isinstance(rotate_order, int):
        raise TypeError(
            "rotate_order must be str or int; "
            f"got {type(rotate_order).__name__}"
        )

    if rotate_order not in _ROTATION_ORDER_MAP.values():
        raise ValueError(
            f"Unsupported rotation order index: {rotate_order}. "
            "Expected an integer from 0 through 5"
        )
    return rotate_order
