# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subset_falloff import RampField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.string import DataStringField


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


class SubsetFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "subsetFalloff"

    falloffTags = DataStringField()
    ftg = falloffTags

    useFalloffTags = BoolField()
    uds = useFalloffTags

    mode = ModeEnumField()
    md = mode

    start = DoubleField()
    st = start

    end = DoubleField()
    ed = end

    ramp = RampField(multi=True)
    rmp = ramp

    scale = DoubleLinearField()
    scl = scale

    useOriginalGeometry = BoolField()
    uo = useOriginalGeometry

    withinBoundary = BoolField()
    wb = withinBoundary

    outputWeightFunction = TypedField()
    wft = outputWeightFunction
