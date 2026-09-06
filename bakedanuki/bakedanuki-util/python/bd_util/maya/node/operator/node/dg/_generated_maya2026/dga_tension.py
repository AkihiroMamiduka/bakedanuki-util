# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.dga_tension import (
    OutputAttributesField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class TensionModeEnumPlugOperator(
    EnumPlugOperator["TensionModeEnumAttrOperator"]
):
    __slots__ = ()

    EDGE = 0
    UV = 2


class TensionModeEnumAttrOperator(
    EnumAttrOperator[TensionModeEnumPlugOperator]
):
    __slots__ = ()

    EDGE = 0
    UV = 2

    NAME_MAP = {
        EDGE: "Edge",
        UV: "UV",
    }


class TensionModeEnumField(
    EnumField[TensionModeEnumAttrOperator, TensionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TensionModeEnumAttrOperator
    PLUG_CLS = TensionModeEnumPlugOperator


class GeneratedDgaTension(DG):
    __slots__ = ()

    NODE_TYPE = "dgaTension"

    inputGeometry = GenericField()
    ig = inputGeometry

    originalGeometry = GenericField()
    orggeom = originalGeometry

    referenceGeometry = GenericField()
    refgeom = referenceGeometry

    componentTagExpression = DataStringField()
    ctx = componentTagExpression

    outputGeometry = GenericField(writable=False)
    og = outputGeometry

    outputAttributes = OutputAttributesField(multi=True, writable=False)
    oatt = outputAttributes

    setupData = TypedField(writable=False)
    sd = setupData

    tensionMode = TensionModeEnumField(default_value=0)
    tmode = tensionMode

    normalizeTensions = BoolField(default_value=False)
    tnorm = normalizeTensions

    maxSquash = DoubleField(
        default_value=2.0, min_value=1.0, soft_max_value=5.0
    )
    mxsq = maxSquash

    maxStretch = DoubleField(
        default_value=2.0, min_value=1.0, soft_max_value=5.0
    )
    mxst = maxStretch

    uvSetName = DataStringField()
    uvn = uvSetName
