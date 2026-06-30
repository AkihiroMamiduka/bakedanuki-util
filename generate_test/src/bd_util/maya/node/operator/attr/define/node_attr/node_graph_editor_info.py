# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2 import Double2Field


class TabGraphInfoPlugOperator(
    CompoundPlugOperator["TabGraphInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("tabName", "tn"),
        ("containerNode", "cn"),
        ("currentView", "cv"),
        ("compoundInfo", "ci"),
        ("tornOff", "to"),
        ("panelPos", "pp"),
        ("panelSize", "ps"),
        ("hasInternalLayout", "hil"),
        ("viewRectLow", "vl"),
        ("viewRectHigh", "vh"),
        ("nodeInfo", "ni"),
    )

    tabName = DataStringField()
    tn = tabName

    containerNode = MessageField()
    cn = containerNode

    currentView = LongField()
    cv = currentView

    compoundInfo = CompoundField()
    ci = compoundInfo

    tornOff = BoolField()
    to = tornOff

    panelPos = Double2Field()
    pp = panelPos

    panelSize = Double2Field()
    ps = panelSize

    hasInternalLayout = BoolField()
    hil = hasInternalLayout

    viewRectLow = Double2Field()
    vl = viewRectLow

    viewRectHigh = Double2Field()
    vh = viewRectHigh

    nodeInfo = CompoundField()
    ni = nodeInfo


class TabGraphInfoAttrOperator(
    CompoundAttrOperator[TabGraphInfoPlugOperator]
):
    __slots__ = ()

    tabName = DataStringField()
    tn = tabName

    containerNode = MessageField()
    cn = containerNode

    currentView = LongField()
    cv = currentView

    compoundInfo = CompoundField()
    ci = compoundInfo

    tornOff = BoolField()
    to = tornOff

    panelPos = Double2Field()
    pp = panelPos

    panelSize = Double2Field()
    ps = panelSize

    hasInternalLayout = BoolField()
    hil = hasInternalLayout

    viewRectLow = Double2Field()
    vl = viewRectLow

    viewRectHigh = Double2Field()
    vh = viewRectHigh

    nodeInfo = CompoundField()
    ni = nodeInfo


class TabGraphInfoField(
    CompoundField[TabGraphInfoAttrOperator, TabGraphInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TabGraphInfoAttrOperator
    PLUG_CLS = TabGraphInfoPlugOperator
