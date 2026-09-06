# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.dga_visualizer import (
    ColorRampField,
    InputAttributesField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class NormalizationModeEnumPlugOperator(
    EnumPlugOperator["NormalizationModeEnumAttrOperator"]
):
    __slots__ = ()

    STATIC = 0
    DYNAMIC = 1


class NormalizationModeEnumAttrOperator(
    EnumAttrOperator[NormalizationModeEnumPlugOperator]
):
    __slots__ = ()

    STATIC = 0
    DYNAMIC = 1

    NAME_MAP = {
        STATIC: "static",
        DYNAMIC: "dynamic",
    }


class NormalizationModeEnumField(
    EnumField[
        NormalizationModeEnumAttrOperator, NormalizationModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalizationModeEnumAttrOperator
    PLUG_CLS = NormalizationModeEnumPlugOperator


class GeneratedDgaVisualizer(DG):
    __slots__ = ()

    NODE_TYPE = "dgaVisualizer"

    inputGeometry = GenericField()
    ig = inputGeometry

    outputGeometry = GenericField()
    og = outputGeometry

    soloInputIndex = LongField(default_value=0, min_value=0, max_value=10)
    sidx = soloInputIndex

    applyColorRamp = BoolField(default_value=True)
    acr = applyColorRamp

    colorRamp = ColorRampField(multi=True)
    cr = colorRamp

    inputAttributes = InputAttributesField(multi=True)
    iatt = inputAttributes

    normalizationMode = NormalizationModeEnumField(default_value=0)
    nm = normalizationMode

    normalizationMin = DoubleField(
        default_value=0.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    nmin = normalizationMin

    normalizationMax = DoubleField(
        default_value=1.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    nmax = normalizationMax

    useAbsoluteValue = BoolField(default_value=False)
    uabs = useAbsoluteValue
