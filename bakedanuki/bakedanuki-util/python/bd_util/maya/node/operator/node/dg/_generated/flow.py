# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.flow import (
    AllCoordsField,
    CenterField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField


class SetFrontAxisEnumPlugOperator(EnumPlugOperator["SetFrontAxisEnumAttrOperator"]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class SetFrontAxisEnumAttrOperator(EnumAttrOperator[SetFrontAxisEnumPlugOperator]):
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


class SetUpAxisEnumPlugOperator(EnumPlugOperator["SetUpAxisEnumAttrOperator"]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class SetUpAxisEnumAttrOperator(EnumAttrOperator[SetUpAxisEnumPlugOperator]):
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


class GeneratedFlow(DG):
    __slots__ = ()

    NODE_TYPE = "flow"

    latticeOnObject = BoolField(default_value=False)
    lo = latticeOnObject

    motionPath = MessageField()
    mp = motionPath

    curve = GenericField(readable=False)
    crv = curve

    parmValue = DoubleLinearField(default_value=0.0, readable=False)
    pv = parmValue

    sDivisions = ShortField(default_value=2)
    sdv = sDivisions

    tDivisions = ShortField(default_value=5)
    tdv = tDivisions

    uDivisions = ShortField(default_value=2)
    udv = uDivisions

    inBaseMatrix = DataMatrixField(readable=False)
    ibm = inBaseMatrix

    defMatrixInv = DataMatrixField(readable=False)
    dmi = defMatrixInv

    setFrontAxis = SetFrontAxisEnumField(default_value=1, readable=False)
    sfa = setFrontAxis

    setUpAxis = SetUpAxisEnumField(default_value=2, readable=False)
    sua = setUpAxis

    orientMatrix = DataMatrixField(readable=False)
    omx = orientMatrix

    allCoords = AllCoordsField(default_value=(0.0, 0.0, 0.0), readable=False)
    ac = allCoords
    xCoord = allCoords.xCoord
    xc = xCoord
    yCoord = allCoords.yCoord
    yc = yCoord
    zCoord = allCoords.zCoord
    zc = zCoord

    center = CenterField(multi=True, default_value=(0.0, 0.0, 0.0), readable=False)
    ctr = center

    objectWorldMatrix = DataMatrixField(multi=True, readable=False)
    owmx = objectWorldMatrix

    outBaseMatrix = DataMatrixField(writable=False)
    obm = outBaseMatrix

    defPts = TypedField(writable=False)
    dpt = defPts
