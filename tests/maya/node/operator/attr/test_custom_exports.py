# coding: utf-8

from bd_util.maya.node.operator.attr.define import custom


def test_custom_exports_are_unique_and_bound():
    assert len(custom.__all__) == 108
    assert len(custom.__all__) == len(set(custom.__all__))
    assert all(hasattr(custom, name) for name in custom.__all__)


def test_custom_exports_cover_each_compound_family():
    expected_names = {
        "Double2CompoundBaseField",
        "Double4Field",
        "Quat4Field",
        "Float3CompoundBaseField",
        "Long3Field",
        "Short3Field",
        "DoubleAngle3CompoundBaseField",
        "FloatAngle3Field",
        "DoubleLinear3CompoundBaseField",
        "FloatLinear3Field",
    }

    assert expected_names <= set(custom.__all__)
