# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class _GeneratedIkSystem(DG):
    __slots__ = ()

    NODE_TYPE = "ikSystem"

    globalSnap = BoolField(default_value=True)
    gsn = globalSnap

    globalSolve = BoolField(default_value=True)
    gsv = globalSolve

    preMaya2011IKFKBlend = BoolField(default_value=False)
    pbd = preMaya2011IKFKBlend

    ikSolver = MessageField(multi=True, readable=False)
    sol = ikSolver

    handleGroupsList = TypedField()
    hgl = handleGroupsList

    handleGroupsListDirtyFlag = BoolField(default_value=False)
    hld = handleGroupsListDirtyFlag

    handleGroupsListSortedFlag = BoolField(default_value=False)
    hls = handleGroupsListSortedFlag
