# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField


class IkSystem(DG):
    __slots__ = ()

    NODE_TYPE = "ikSystem"

    globalSnap = BoolField()
    gsn = globalSnap

    globalSolve = BoolField()
    gsv = globalSolve

    preMaya2011IKFKBlend = BoolField()
    pbd = preMaya2011IKFKBlend

    ikSolver = MessageField(multi=True)
    sol = ikSolver

    handleGroupsList = TypedField()
    hgl = handleGroupsList

    handleGroupsListDirtyFlag = BoolField()
    hld = handleGroupsListDirtyFlag

    handleGroupsListSortedFlag = BoolField()
    hls = handleGroupsListSortedFlag
