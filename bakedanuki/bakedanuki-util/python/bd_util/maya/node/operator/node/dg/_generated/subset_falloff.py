# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.subset_falloff import RampField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONNECTIVITY = 0
    VOLUME = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONNECTIVITY = 0
    VOLUME = 1

    NAME_MAP = {
        CONNECTIVITY: "Connectivity",
        VOLUME: "Volume",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class GeneratedSubsetFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "subsetFalloff"

    falloffTags = DataStringField()
    ftg = falloffTags

    useFalloffTags = BoolField(default_value=False)
    uds = useFalloffTags

    mode = ModeEnumField(default_value=0)
    md = mode

    start = DoubleField(default_value=0.0, min_value=0.0)
    st = start

    end = DoubleField(default_value=1.0, min_value=0.0)
    ed = end

    ramp = RampField(multi=True, default_value=(0.0, 0.0, 0.0))
    rmp = ramp

    scale = DoubleLinearField(default_value=1.0, min_value=0.01, soft_min_value=0.0, soft_max_value=25.0)
    scl = scale

    useOriginalGeometry = BoolField(default_value=True)
    uo = useOriginalGeometry

    withinBoundary = BoolField(default_value=True)
    wb = withinBoundary

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction
