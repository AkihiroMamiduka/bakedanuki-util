# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


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

    primaryInputAxis = Double3Field()
    pmi = primaryInputAxis

    primaryMode = EnumField()
    prmd = primaryMode

    primaryTargetVector = Double3Field()
    pmiv = primaryTargetVector

    primaryTargetMatrix = MatrixField()
    pmat = primaryTargetMatrix


class PrimaryAttrOperator(
    CompoundAttrOperator[PrimaryPlugOperator]
):
    __slots__ = ()

    primaryInputAxis = Double3Field()
    pmi = primaryInputAxis

    primaryMode = EnumField()
    prmd = primaryMode

    primaryTargetVector = Double3Field()
    pmiv = primaryTargetVector

    primaryTargetMatrix = MatrixField()
    pmat = primaryTargetMatrix


class PrimaryField(
    CompoundField[PrimaryAttrOperator, PrimaryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrimaryAttrOperator
    PLUG_CLS = PrimaryPlugOperator

    primaryInputAxis = Double3Field()
    pmi = primaryInputAxis

    primaryMode = EnumField()
    prmd = primaryMode

    primaryTargetVector = Double3Field()
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

    secondaryInputAxis = Double3Field()
    smi = secondaryInputAxis

    secondaryMode = EnumField()
    sm = secondaryMode

    secondaryTargetVector = Double3Field()
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix


class SecondaryAttrOperator(
    CompoundAttrOperator[SecondaryPlugOperator]
):
    __slots__ = ()

    secondaryInputAxis = Double3Field()
    smi = secondaryInputAxis

    secondaryMode = EnumField()
    sm = secondaryMode

    secondaryTargetVector = Double3Field()
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix


class SecondaryField(
    CompoundField[SecondaryAttrOperator, SecondaryPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SecondaryAttrOperator
    PLUG_CLS = SecondaryPlugOperator

    secondaryInputAxis = Double3Field()
    smi = secondaryInputAxis

    secondaryMode = EnumField()
    sm = secondaryMode

    secondaryTargetVector = Double3Field()
    smiv = secondaryTargetVector

    secondaryTargetMatrix = MatrixField()
    smat = secondaryTargetMatrix
