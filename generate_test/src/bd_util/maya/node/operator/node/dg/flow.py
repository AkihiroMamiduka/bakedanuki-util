# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.flow import (
    AllCoordsField,
    CenterField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class SetFrontAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class SetFrontAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class SetFrontAxisEnumField(
    EnumField[SetFrontAxisEnumAttrOperator, SetFrontAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SetFrontAxisEnumAttrOperator
    PLUG_CLS = SetFrontAxisEnumPlugOperator


class SetUpAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class SetUpAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class SetUpAxisEnumField(
    EnumField[SetUpAxisEnumAttrOperator, SetUpAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SetUpAxisEnumAttrOperator
    PLUG_CLS = SetUpAxisEnumPlugOperator


class Flow(DG):
    __slots__ = ()

    NODE_TYPE = "flow"

    latticeOnObject = BoolField()
    lo = latticeOnObject

    motionPath = MessageField()
    mp = motionPath

    curve = GenericField()
    crv = curve

    parmValue = DoubleLinearField()
    pv = parmValue

    sDivisions = ShortField()
    sdv = sDivisions

    tDivisions = ShortField()
    tdv = tDivisions

    uDivisions = ShortField()
    udv = uDivisions

    inBaseMatrix = DataMatrixField()
    ibm = inBaseMatrix

    defMatrixInv = DataMatrixField()
    dmi = defMatrixInv

    setFrontAxis = SetFrontAxisEnumField()
    sfa = setFrontAxis

    setUpAxis = SetUpAxisEnumField()
    sua = setUpAxis

    orientMatrix = DataMatrixField()
    omx = orientMatrix

    allCoords = AllCoordsField()
    ac = allCoords
    xCoord = allCoords.xCoord
    xc = xCoord
    yCoord = allCoords.yCoord
    yc = yCoord
    zCoord = allCoords.zCoord
    zc = zCoord

    center = CenterField(multi=True)
    ctr = center

    objectWorldMatrix = DataMatrixField(multi=True)
    owmx = objectWorldMatrix

    outBaseMatrix = DataMatrixField()
    obm = outBaseMatrix

    defPts = TypedField()
    dpt = defPts
