# coding: utf-8
from __future__ import annotations

import pytest

pytestmark = pytest.mark.maya


def test_scalar_family_exports_are_bound():
    from bd_util.maya.node.operator.attr.define.std.at.scalar import (
        numeric,
        unit,
    )

    assert {
        "NumericBaseAttrOperator",
        "NumericBaseField",
        "NumericBasePlugOperator",
        "NumericRangeBaseAttrOperator",
        "NumericRangeBaseField",
        "NumericRangeBasePlugOperator",
        "double",
    } == set(numeric.__all__)
    assert {
        "UnitBaseAttrOperator",
        "UnitBaseField",
        "UnitBasePlugOperator",
        "UnitRangeBaseAttrOperator",
        "UnitRangeBaseField",
        "UnitRangeBasePlugOperator",
        "double_linear",
        "float_angle",
        "float_linear",
    } == set(unit.__all__)
    assert all(hasattr(numeric, name) for name in numeric.__all__)
    assert all(hasattr(unit, name) for name in unit.__all__)


def test_scalar_operator_families_share_scalar_base(new_scene):
    from bd_util.maya.node.operator.attr.define.std.at.compound import (
        CompoundAttrOperator,
        CompoundPlugOperator,
        CompoundField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.enum import (
        EnumAttrOperator,
        EnumPlugOperator,
        EnumField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric import (
        NumericBaseAttrOperator,
        NumericBaseField,
        NumericBasePlugOperator,
        NumericRangeBaseAttrOperator,
        NumericRangeBaseField,
        NumericRangeBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBaseAttrOperator,
        ScalarBasePlugOperator,
        ScalarBaseField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
        UnitBaseAttrOperator,
        UnitBaseField,
        UnitBasePlugOperator,
        UnitRangeBaseAttrOperator,
        UnitRangeBaseField,
        UnitRangeBasePlugOperator,
    )

    assert issubclass(NumericBasePlugOperator, ScalarBasePlugOperator)
    assert issubclass(NumericBaseAttrOperator, ScalarBaseAttrOperator)
    assert issubclass(NumericBaseField, ScalarBaseField)
    assert issubclass(NumericRangeBasePlugOperator, NumericBasePlugOperator)
    assert issubclass(NumericRangeBaseAttrOperator, NumericBaseAttrOperator)
    assert issubclass(NumericRangeBaseField, NumericBaseField)

    assert issubclass(UnitBasePlugOperator, ScalarBasePlugOperator)
    assert issubclass(UnitBaseAttrOperator, ScalarBaseAttrOperator)
    assert issubclass(UnitBaseField, ScalarBaseField)
    assert issubclass(UnitRangeBasePlugOperator, UnitBasePlugOperator)
    assert issubclass(UnitRangeBaseAttrOperator, UnitBaseAttrOperator)
    assert issubclass(UnitRangeBaseField, UnitBaseField)

    assert issubclass(EnumPlugOperator, ScalarBasePlugOperator)
    assert issubclass(EnumAttrOperator, ScalarBaseAttrOperator)
    assert issubclass(EnumField, ScalarBaseField)

    assert not issubclass(CompoundPlugOperator, ScalarBasePlugOperator)
    assert not issubclass(CompoundAttrOperator, ScalarBaseAttrOperator)
    assert not issubclass(CompoundField, ScalarBaseField)


def test_scalar_attr_type_placeholder_is_defined_on_scalar_base(new_scene):
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric import (
        NumericBaseAttrOperator,
        NumericRangeBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
        UnitBaseAttrOperator,
        UnitRangeBaseAttrOperator,
    )

    assert ScalarBaseAttrOperator.ATTR_TYPE == "abc"
    assert "ATTR_TYPE" not in NumericBaseAttrOperator.__dict__
    assert "ATTR_TYPE" not in NumericRangeBaseAttrOperator.__dict__
    assert "ATTR_TYPE" not in UnitBaseAttrOperator.__dict__
    assert "ATTR_TYPE" not in UnitRangeBaseAttrOperator.__dict__


def test_keyframe_property_is_defined_only_on_scalar_base(new_scene):
    from bd_util.maya.node.operator.attr.define.std.at.scalar.enum import (
        EnumPlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric import (
        NumericBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit import (
        UnitBasePlugOperator,
        float_angle,
        float_linear,
    )

    assert isinstance(ScalarBasePlugOperator.keyframe, property)
    assert "keyframe" not in NumericBasePlugOperator.__dict__
    assert "keyframe" not in UnitBasePlugOperator.__dict__
    assert "keyframe" not in EnumPlugOperator.__dict__
    assert "keyframe" not in float_angle.FloatAnglePlugOperator.__dict__
    assert "keyframe" not in float_linear.FloatLinearPlugOperator.__dict__
