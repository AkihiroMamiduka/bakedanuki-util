# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.dt.mesh import DataMeshField


class ColliderPlugOperator(
    CompoundPlugOperator["ColliderAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colliderMesh", "cm"),
        ("colliderMatrix", "cmx"),
        ("colliderEnabled", "ce"),
        ("colliderNormalFlipped", "cnf"),
    )

    colliderMesh = DataMeshField()
    cm = colliderMesh

    colliderMatrix = MatrixField()
    cmx = colliderMatrix

    colliderEnabled = BoolField(default_value=True)
    ce = colliderEnabled

    colliderNormalFlipped = BoolField(default_value=False)
    cnf = colliderNormalFlipped


class ColliderAttrOperator(
    CompoundAttrOperator[ColliderPlugOperator]
):
    __slots__ = ()

    colliderMesh = DataMeshField()
    cm = colliderMesh

    colliderMatrix = MatrixField()
    cmx = colliderMatrix

    colliderEnabled = BoolField(default_value=True)
    ce = colliderEnabled

    colliderNormalFlipped = BoolField(default_value=False)
    cnf = colliderNormalFlipped


class ColliderField(
    CompoundField[ColliderAttrOperator, ColliderPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColliderAttrOperator
    PLUG_CLS = ColliderPlugOperator
