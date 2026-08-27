# coding: utf-8
from typing import Any

import pytest

from bd_util.maya.node.operator.attr._core import PlugOperator
from bd_util.maya.node.operator.attr.define.custom import Double3PlugOperator
from bd_util.maya.node.operator.attr.define.std.at.addr import AddrPlugOperator
from bd_util.maya.node.operator.attr.define.std.at.compound import (
    CompoundPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.generic import (
    GenericPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.light_data import (
    LightDataPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.message import (
    MessagePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import (
    DoublePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.typed import (
    TypedPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.mesh import (
    DataMeshPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.string import (
    DataStringPlugOperator,
)

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "plug_cls",
    (
        PlugOperator,
        CompoundPlugOperator,
        GenericPlugOperator,
        LightDataPlugOperator,
        MessagePlugOperator,
        TypedPlugOperator,
        DataMeshPlugOperator,
    ),
)
def test_value_operations_are_absent_from_unsupported_plug_types(
    plug_cls: type[PlugOperator[Any]],
) -> None:
    for method_name in ("get", "set", "set_direct", "value", "value_direct"):
        assert not hasattr(plug_cls, method_name)


@pytest.mark.parametrize(
    ("plug_cls", "available", "unavailable"),
    (
        (
            DoublePlugOperator,
            ("get", "set"),
            ("set_direct", "value", "value_direct"),
        ),
        (
            Double3PlugOperator,
            ("get", "set", "set_direct"),
            ("value", "value_direct"),
        ),
        (
            DataMatrixPlugOperator,
            ("get", "set_direct"),
            ("set", "value", "value_direct"),
        ),
        (
            DataStringPlugOperator,
            ("get", "set", "set_direct"),
            ("value", "value_direct"),
        ),
        (
            AddrPlugOperator,
            ("get", "set_direct"),
            ("set", "value", "value_direct"),
        ),
    ),
)
def test_supported_plug_types_expose_only_available_value_operations(
    plug_cls: type[PlugOperator[Any]],
    available: tuple[str, ...],
    unavailable: tuple[str, ...],
) -> None:
    for method_name in available:
        assert hasattr(plug_cls, method_name)
    for method_name in unavailable:
        assert not hasattr(plug_cls, method_name)
