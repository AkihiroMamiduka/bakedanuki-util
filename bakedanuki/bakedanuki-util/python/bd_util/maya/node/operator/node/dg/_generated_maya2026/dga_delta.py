# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.dga_delta import OutputAttributesField
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


class DeltaModeEnumPlugOperator(EnumPlugOperator["DeltaModeEnumAttrOperator"]):
    __slots__ = ()

    POSITION = 0
    NORMAL = 1


class DeltaModeEnumAttrOperator(EnumAttrOperator[DeltaModeEnumPlugOperator]):
    __slots__ = ()

    POSITION = 0
    NORMAL = 1

    NAME_MAP = {
        POSITION: "Position",
        NORMAL: "Normal",
    }


class DeltaModeEnumField(
    EnumField[DeltaModeEnumAttrOperator, DeltaModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DeltaModeEnumAttrOperator
    PLUG_CLS = DeltaModeEnumPlugOperator


class GeneratedDgaDelta(DG):
    __slots__ = ()

    NODE_TYPE = "dgaDelta"

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

    deltaMode = DeltaModeEnumField(default_value=0)
    dmode = deltaMode

    setupData = TypedField(writable=False)
    sd = setupData

    normalizeOutput = BoolField(default_value=False)
    norm = normalizeOutput

    normalizationMin = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=180.0
    )
    nmin = normalizationMin

    normalizationMax = DoubleField(
        default_value=100.0, min_value=0.0, soft_max_value=180.0
    )
    nmax = normalizationMax
