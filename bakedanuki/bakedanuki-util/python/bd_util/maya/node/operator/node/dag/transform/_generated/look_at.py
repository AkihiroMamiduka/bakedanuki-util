# coding: utf-8
from ..aim_constraint import AimConstraint
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedLookAt(AimConstraint):
    __slots__ = ()

    NODE_TYPE = "lookAt"

    distanceBetween = DoubleField(default_value=0.0)
    db = distanceBetween

    twist = DoubleAngleField(
        default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0
    )
    tws = twist

    displayConnector = BoolField(default_value=True)
    dc = displayConnector
