# coding: utf-8
from __future__ import annotations

import pytest

pytestmark = pytest.mark.maya


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
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric._base import (
        NumericBaseAttrOperator,
        NumericBasePlugOperator,
        NumericBaseField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range._base import (
        NumericRangeBaseAttrOperator,
        NumericRangeBasePlugOperator,
        NumericRangeBaseField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBaseAttrOperator,
        ScalarBasePlugOperator,
        ScalarBaseField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit._base import (
        UnitBaseAttrOperator,
        UnitBasePlugOperator,
        UnitBaseField,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range._base import (
        UnitRangeBaseAttrOperator,
        UnitRangeBasePlugOperator,
        UnitRangeBaseField,
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
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric._base import (
        NumericBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range._base import (
        NumericRangeBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit._base import (
        UnitBaseAttrOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range._base import (
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
    from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric._base import (
        NumericBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar._base import (
        ScalarBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit._base import (
        UnitBasePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.float_angle import (
        FloatAnglePlugOperator,
    )
    from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.float_linear import (
        FloatLinearPlugOperator,
    )

    assert isinstance(ScalarBasePlugOperator.keyframe, property)
    assert "keyframe" not in NumericBasePlugOperator.__dict__
    assert "keyframe" not in UnitBasePlugOperator.__dict__
    assert "keyframe" not in EnumPlugOperator.__dict__
    assert "keyframe" not in FloatAnglePlugOperator.__dict__
    assert "keyframe" not in FloatLinearPlugOperator.__dict__
