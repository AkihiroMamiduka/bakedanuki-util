# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.matrix import MatrixField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class PrimaryModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LOCK_AXIS = 0
    AIM = 1
    ALIGN = 2


class PrimaryModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LOCK_AXIS = 0
    AIM = 1
    ALIGN = 2

    NAME_MAP = {
        LOCK_AXIS: "Lock Axis",
        AIM: "Aim",
        ALIGN: "Align",
    }


class PrimaryModeEnumField(
    EnumField[PrimaryModeEnumAttrOperator, PrimaryModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrimaryModeEnumAttrOperator
    PLUG_CLS = PrimaryModeEnumPlugOperator


class SecondaryModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    AIM = 1
    ALIGN = 2


class SecondaryModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    AIM = 1
    ALIGN = 2

    NAME_MAP = {
        NONE: "None",
        AIM: "Aim",
        ALIGN: "Align",
    }


class SecondaryModeEnumField(
    EnumField[SecondaryModeEnumAttrOperator, SecondaryModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SecondaryModeEnumAttrOperator
    PLUG_CLS = SecondaryModeEnumPlugOperator


class PrimaryPlugOperator(
    CompoundPlugOperator["PrimaryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("primaryInputAxis", "pmi"),
        ("primaryMode", "prmd"),
        ("primaryTargetVector", "pmiv"),
        ("primaryTargetMatrix", "pmat"),
    )

    primaryInputAxis = Double3Field(default_value=(1.0, 0.0, 0.0))
    pmi = primaryInputAxis

    primaryMode = PrimaryModeEnumField(default_value=1)
    prmd = primaryMode

    primaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    pmiv = primaryTargetVector

    primaryTargetMatrix = MatrixField()
    pmat = primaryTargetMatrix


class PrimaryAttrOperator(
    CompoundAttrOperator[PrimaryPlugOperator]
):
    __slots__ = ()

    primaryInputAxis = Double3Field(default_value=(1.0, 0.0, 0.0))
    pmi = primaryInputAxis

    primaryMode = PrimaryModeEnumField(default_value=1)
    prmd = primaryMode

    primaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    pmiv = primaryTargetVector

    primaryTargetMatrix = MatrixField()
    pmat = primaryTargetMatrix


class PrimaryField(
    CompoundField[PrimaryAttrOperator, PrimaryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrimaryAttrOperator
    PLUG_CLS = PrimaryPlugOperator

    primaryInputAxis = Double3Field(default_value=(1.0, 0.0, 0.0))
    pmi = primaryInputAxis

    primaryMode = PrimaryModeEnumField(default_value=1)
    prmd = primaryMode

    primaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    pmiv = primaryTargetVector

    primaryTargetMatrix = MatrixField()
    pmat = primaryTargetMatrix


class SecondaryPlugOperator(
    CompoundPlugOperator["SecondaryAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("secondaryInputAxis", "smi"),
        ("secondaryMode", "sm"),
        ("secondaryTargetVector", "smiv"),
        ("secondaryTargetMatrix", "smat"),
    )

    secondaryInputAxis = Double3Field(default_value=(0.0, 1.0, 0.0))
    smi = secondaryInputAxis

    secondaryMode = SecondaryModeEnumField(default_value=0)
    sm = secondaryMode

    secondaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix


class SecondaryAttrOperator(
    CompoundAttrOperator[SecondaryPlugOperator]
):
    __slots__ = ()

    secondaryInputAxis = Double3Field(default_value=(0.0, 1.0, 0.0))
    smi = secondaryInputAxis

    secondaryMode = SecondaryModeEnumField(default_value=0)
    sm = secondaryMode

    secondaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix


class SecondaryField(
    CompoundField[SecondaryAttrOperator, SecondaryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SecondaryAttrOperator
    PLUG_CLS = SecondaryPlugOperator

    secondaryInputAxis = Double3Field(default_value=(0.0, 1.0, 0.0))
    smi = secondaryInputAxis

    secondaryMode = SecondaryModeEnumField(default_value=0)
    sm = secondaryMode

    secondaryTargetVector = Double3Field(default_value=(0.0, 0.0, 0.0))
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix
