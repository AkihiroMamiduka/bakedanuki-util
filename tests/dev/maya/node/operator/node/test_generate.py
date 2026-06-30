# coding: utf-8
from bd_util._dev.maya.node.operator.node.generate import (
    generate_node_attr_code,
    generate_node_class_code,
)
from bd_util.maya.attr.query import AttrInfo


def _attr(
    long_name: str,
    short_name: str,
    attribute_type: str,
    *,
    data_type: str | None = None,
    enum_name=None,
    multi: bool = False,
    number_of_children: int | None = None,
    parent: str | None = None,
) -> AttrInfo:
    return AttrInfo(
        long_name=long_name,
        short_name=short_name,
        attribute_type=attribute_type,
        data_type=data_type,
        default_value=None,
        min_value=None,
        max_value=None,
        soft_min_value=None,
        soft_max_value=None,
        enum_name=enum_name,
        multi=multi,
        number_of_children=number_of_children,
        parent=[parent] if parent is not None else None,
        readable=True,
        writable=True,
        category=None,
    )


def _plus_minus_average_attr_infos() -> list[AttrInfo]:
    return [
        _attr(
            "operation",
            "op",
            "enum",
            enum_name=["No operation:Sum:Subtract:Average"],
        ),
        _attr("input1D", "i1", "float", multi=True),
        _attr("input2D", "i2", "float2", multi=True, number_of_children=2),
        _attr("input2D.input2Dx", "i2x", "float", parent="input2D"),
        _attr("input2D.input2Dy", "i2y", "float", parent="input2D"),
        _attr("input3D", "i3", "float3", multi=True, number_of_children=3),
        _attr("input3D.input3Dx", "i3x", "float", parent="input3D"),
        _attr("input3D.input3Dy", "i3y", "float", parent="input3D"),
        _attr("input3D.input3Dz", "i3z", "float", parent="input3D"),
        _attr("output1D", "o1", "float"),
        _attr("output2D", "o2", "float2", number_of_children=2),
        _attr("output2Dx", "o2x", "float", parent="output2D"),
        _attr("output2Dy", "o2y", "float", parent="output2D"),
        _attr("output3D", "o3", "float3", number_of_children=3),
        _attr("output3Dx", "o3x", "float", parent="output3D"),
        _attr("output3Dy", "o3y", "float", parent="output3D"),
        _attr("output3Dz", "o3z", "float", parent="output3D"),
    ]


def _quat_like_attr_infos() -> list[AttrInfo]:
    return [
        _attr("input1Quat", "iq1", "compound", number_of_children=4),
        _attr("input1Quat.input1QuatX", "i1x", "double", parent="input1Quat"),
        _attr("input1Quat.input1QuatY", "i1y", "double", parent="input1Quat"),
        _attr("input1Quat.input1QuatZ", "i1z", "double", parent="input1Quat"),
        _attr("input1Quat.input1QuatW", "i1w", "double", parent="input1Quat"),
        _attr("input1QuatWDEPRECATED", "1w", "double"),
        _attr("numericShortAttr", "1n", "double"),
    ]


def _double4_quat_attr_infos() -> list[AttrInfo]:
    return [
        _attr("inputQuat", "iq", "double4", number_of_children=4),
        _attr("inputQuat.inputQuatX", "iqx", "double", parent="inputQuat"),
        _attr("inputQuat.inputQuatY", "iqy", "double", parent="inputQuat"),
        _attr("inputQuat.inputQuatZ", "iqz", "double", parent="inputQuat"),
        _attr("inputQuat.inputQuatW", "iqw", "double", parent="inputQuat"),
    ]


def test_generate_plus_minus_average_node_attr_code():
    code = generate_node_attr_code(
        "plusMinusAverage",
        attr_infos=_plus_minus_average_attr_infos(),
    )

    assert code is not None
    compile(code, "plus_minus_average_node_attr.py", "exec")

    assert "Float2CompoundBaseField" in code
    assert "Float3CompoundBaseField" in code
    assert "class Input2DPlugOperator(" in code
    assert "class Input2DAttrOperator(" in code
    assert "class Input2DField(" in code
    assert '("input2Dx", "i2x")' in code
    assert "input2Dx = FloatField()" in code
    assert "i2x = input2Dx" in code
    assert "class Output3DField(" in code
    assert "output3Dz = FloatField()" in code
    assert "o3z = output3Dz" in code


def test_generate_quat_like_compound_node_attr_code():
    code = generate_node_attr_code(
        "quatSlerp",
        attr_infos=_quat_like_attr_infos(),
    )

    assert code is not None
    compile(code, "quat_slerp_node_attr.py", "exec")

    assert "QuatCompoundBasePlugOperator" in code
    assert "QuatCompoundBaseAttrOperator" in code
    assert "QuatCompoundBaseField" in code
    assert "Double4CompoundBasePlugOperator" not in code
    assert "CompoundPlugOperator" not in code
    assert "class Input1QuatField(" in code
    assert '("input1QuatW", "i1w")' in code
    assert "i1w = input1QuatW" in code


def test_generate_double4_quat_compound_node_attr_code():
    code = generate_node_attr_code(
        "composeMatrix",
        attr_infos=_double4_quat_attr_infos(),
    )

    assert code is not None
    compile(code, "compose_matrix_node_attr.py", "exec")

    assert "QuatCompoundBasePlugOperator" in code
    assert "QuatCompoundBaseAttrOperator" in code
    assert "QuatCompoundBaseField" in code
    assert "class InputQuatField(" in code


def test_generate_plus_minus_average_node_class_code():
    code = generate_node_class_code(
        "plusMinusAverage",
        attr_infos=_plus_minus_average_attr_infos(),
    )

    compile(code, "plus_minus_average.py", "exec")

    assert "from ...attr.define.node_attr.plus_minus_average import" in code
    assert "Input2DField" in code
    assert "Input3DField" in code
    assert "Output2DField" in code
    assert "Output3DField" in code
    assert "class OperationEnumPlugOperator(EnumPlugOperator):" in code
    assert "class OperationEnumAttrOperator(EnumAttrOperator):" in code
    assert "class OperationEnumField(" in code
    assert "NO_OPERATION = 0" in code
    assert 'NO_OPERATION: "No operation"' in code
    assert "operation = OperationEnumField()" in code
    assert "op = operation" in code
    assert "input1D = FloatField(multi=True)" in code
    assert "input2D = Input2DField(multi=True)" in code
    assert "output3D = Output3DField()" in code
    assert "output3Dz = output3D.output3Dz" in code
    assert "o3z = output3Dz" in code


def test_generate_skips_deprecated_and_numeric_short_aliases():
    code = generate_node_class_code(
        "quatSlerp",
        attr_infos=_quat_like_attr_infos(),
    )

    compile(code, "quat_slerp.py", "exec")

    assert "input1Quat = Input1QuatField()" in code
    assert "iq1 = input1Quat" in code
    assert "input1QuatWDEPRECATED = DoubleField()" in code
    assert "one1w = input1QuatWDEPRECATED" not in code
    assert "numericShortAttr = DoubleField()" in code
    assert "onen = numericShortAttr" not in code
