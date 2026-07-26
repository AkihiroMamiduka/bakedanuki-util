# coding: utf-8
from bd_util._dev.maya.node.operator.node.generate import (
    _ARNOLD_UNRELIABLE_DEFAULT_ATTRS,
    _AT_TYPE_MAP,
    generate_node_attr_code,
    generate_node_class_code,
    generate_node_class_file,
)
from bd_util.maya.attr.query import AttrInfo
from bd_util.maya.node.operator.attr.define.std.dt.string import DataStringField


def test_scalar_attribute_type_map_uses_scalar_package_hierarchy():
    expected_modules = {
        "bool": "define.std.at.scalar.numeric.bool",
        "byte": "define.std.at.scalar.numeric.range.byte",
        "char": "define.std.at.scalar.numeric.range.char",
        "double": "define.std.at.scalar.numeric.range.double",
        "doubleAngle": "define.std.at.scalar.unit.range.double_angle",
        "doubleLinear": "define.std.at.scalar.unit.range.double_linear",
        "enum": "define.std.at.scalar.enum",
        "float": "define.std.at.scalar.numeric.range.float",
        "floatAngle": "define.std.at.scalar.unit.range.float_angle",
        "floatLinear": "define.std.at.scalar.unit.range.float_linear",
        "long": "define.std.at.scalar.numeric.range.long",
        "long long int": "define.std.at.scalar.numeric.range.long_long_int",
        "long_long_int": "define.std.at.scalar.numeric.range.long_long_int",
        "short": "define.std.at.scalar.numeric.range.short",
        "time": "define.std.at.scalar.unit.time",
    }

    for attribute_type, expected_module in expected_modules.items():
        assert _AT_TYPE_MAP[attribute_type][1] == expected_module


def test_arnold_unreliable_default_attrs_are_narrowly_scoped():
    assert _ARNOLD_UNRELIABLE_DEFAULT_ATTRS == {
        "aiAOVDriver": frozenset({"layerTolerance"}),
        "aiImagerLightMixer": frozenset(
            {
                "layerTint",
                "layerTintR",
                "layerTintG",
                "layerIntensity",
                "layerExposure",
            }
        ),
        "aiLayerShader": frozenset(
            {
                "input1A",
                "input2A",
                "input4A",
                "input5A",
                "input7A",
            }
        ),
        "aiMixShader": frozenset({"shader1A", "shader2A"}),
        "aiPassthrough": frozenset(
            {
                "eval2A",
                "eval3A",
                "eval4A",
                "eval5A",
                "eval6A",
                "eval11A",
                "eval14A",
                "eval18A",
            }
        ),
        "aiWriteInt": frozenset({"beautyA"}),
    }


def _attr(
    long_name: str,
    short_name: str,
    attribute_type: str | None,
    *,
    data_type: str | None = None,
    enum_name=None,
    default_value=None,
    min_value=None,
    max_value=None,
    soft_min_value=None,
    soft_max_value=None,
    multi: bool = False,
    number_of_children: int | None = None,
    parent: str | None = None,
    readable: bool | None = True,
    writable: bool | None = True,
    category=None,
    path_name: str | None = None,
    enforcing_unique_name: bool | None = None,
) -> AttrInfo:
    return AttrInfo(
        long_name=long_name,
        short_name=short_name,
        attribute_type=attribute_type,
        data_type=data_type,
        default_value=default_value,
        min_value=min_value,
        max_value=max_value,
        soft_min_value=soft_min_value,
        soft_max_value=soft_max_value,
        enum_name=enum_name,
        multi=multi,
        number_of_children=number_of_children,
        parent=[parent] if parent is not None else None,
        readable=readable,
        writable=writable,
        category=category,
        path_name=path_name,
        enforcing_unique_name=enforcing_unique_name,
    )


def test_generate_omits_only_known_unreliable_arnold_defaults():
    code = generate_node_class_code(
        "aiLayerShader",
        attr_infos=[
            _attr(
                "input1A",
                "input1a",
                "float",
                default_value=[123.0],
                min_value=[0.0],
                max_value=[1.0],
            ),
            _attr(
                "input3A",
                "input3a",
                "float",
                default_value=[0.0],
                min_value=[0.0],
                max_value=[1.0],
            ),
        ],
    )

    assert "input1A = FloatField(min_value=0.0, max_value=1.0)" in code
    assert "input1A = FloatField(default_value=" not in code
    assert (
        "input3A = FloatField(default_value=0.0, min_value=0.0, "
        "max_value=1.0)" in code
    )


def test_generate_node_attr_omits_known_unreliable_arnold_child_default():
    code = generate_node_attr_code(
        "aiImagerLightMixer",
        attr_infos=[
            _attr(
                "layerTint",
                "layer_tint",
                "float3",
                default_value=[123.0, 456.0, 1.0],
                number_of_children=3,
            ),
            _attr(
                "layerTint.layerTintR",
                "layer_tintr",
                "float",
                default_value=[123.0],
                parent="layerTint",
                path_name="layerTintR",
            ),
            _attr(
                "layerTint.layerTintG",
                "layer_tintg",
                "float",
                default_value=[456.0],
                parent="layerTint",
                path_name="layerTintG",
            ),
            _attr(
                "layerTint.layerTintB",
                "layer_tintb",
                "float",
                default_value=[1.0],
                parent="layerTint",
                path_name="layerTintB",
            ),
        ],
    )

    assert code is not None
    assert "layerTintR = FloatField()" in code
    assert "layerTintG = FloatField()" in code
    assert "layerTintB = FloatField(default_value=1.0)" in code


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


def _unsafe_identifier_attr_infos() -> list[AttrInfo]:
    return [
        _attr(".weight", ".w", "float", multi=True),
        _attr(".pnts", ".pt", "double3", multi=True, number_of_children=3),
        _attr(".pnts.px", ".pt.x", "double", parent=".pnts"),
        _attr(".pnts.py", ".pt.y", "double", parent=".pnts"),
        _attr(".pnts.pz", ".pt.z", "double", parent=".pnts"),
        _attr("weightList", "wl", "compound", multi=True, number_of_children=1),
        _attr("weightList.weights", "wl.w", "float", parent="weightList"),
    ]


def _path_name_attr_infos() -> list[AttrInfo]:
    return [
        _attr(
            "pnts",
            ".pt",
            "double3",
            multi=True,
            number_of_children=3,
            path_name=".pnts",
            enforcing_unique_name=False,
        ),
        _attr(
            "px",
            ".pt.x",
            "double",
            parent=".pnts",
            path_name=".pnts.px",
            enforcing_unique_name=False,
        ),
        _attr(
            "py",
            ".pt.y",
            "double",
            parent=".pnts",
            path_name=".pnts.py",
            enforcing_unique_name=False,
        ),
        _attr(
            "pz",
            ".pt.z",
            "double",
            parent=".pnts",
            path_name=".pnts.pz",
            enforcing_unique_name=False,
        ),
    ]


def _reserved_name_attr_infos() -> list[AttrInfo]:
    return [
        _attr("name", "nm", "typed", data_type="string"),
        _attr("compound", "cmp", "compound", number_of_children=1),
        _attr("compound.value", "cv", "float", parent="compound"),
    ]


def _duplicate_enum_attr_infos() -> list[AttrInfo]:
    return [
        _attr(
            "frameBufferFormat",
            "fbf",
            "enum",
            enum_name=[
                "RGBA:8-bits fixed per channel=1:"
                "RGBA=2:16-bit float per channel=3"
            ],
        ),
    ]


def _datatype_only_attr_infos() -> list[AttrInfo]:
    return [
        _attr("localXform", "lx", None, data_type="matrix"),
        _attr("positionList", "pl", None, data_type="vectorArray"),
    ]


def _compound_enum_attr_infos() -> list[AttrInfo]:
    return [
        _attr("primary", "pm", "compound", number_of_children=2),
        _attr(
            "primary.primaryMode",
            "prmd",
            "enum",
            parent="primary",
            enum_name=["None:Vector:Matrix"],
        ),
        _attr("primary.primaryWeight", "prw", "double", parent="primary"),
    ]


def _transform_like_attr_infos() -> list[AttrInfo]:
    return [
        _attr("message", "msg", "message"),
        _attr("translate", "t", "double3", number_of_children=3),
        _attr("translate.translateX", "tx", "doubleLinear", parent="translate"),
        _attr("translate.translateY", "ty", "doubleLinear", parent="translate"),
        _attr("translate.translateZ", "tz", "doubleLinear", parent="translate"),
    ]


def _shape_like_attr_infos() -> list[AttrInfo]:
    return [
        _attr("message", "msg", "message"),
        _attr(
            "outMesh",
            "out",
            "typed",
            data_type="mesh",
            writable=False,
        ),
        _attr("face", "fc", "polyFaces", data_type="0", multi=True),
    ]


def _joint_like_attr_infos() -> list[AttrInfo]:
    return [
        *_transform_like_attr_infos(),
        _attr("jointOrient", "jo", "double3", number_of_children=3),
        _attr(
            "jointOrient.jointOrientX",
            "jox",
            "doubleAngle",
            parent="jointOrient",
        ),
        _attr(
            "jointOrient.jointOrientY",
            "joy",
            "doubleAngle",
            parent="jointOrient",
        ),
        _attr(
            "jointOrient.jointOrientZ",
            "joz",
            "doubleAngle",
            parent="jointOrient",
        ),
        _attr(
            "segmentScaleCompensate",
            "ssc",
            "bool",
            default_value=[1.0],
        ),
    ]


def test_attribute_field_accepts_explicit_maya_names():
    class Dummy:
        name_ = DataStringField(long_name="name", short_name="nm")
        nm = name_

    field = Dummy.__dict__["name_"]

    assert field.name == "name_"
    assert field.long_name == "name"
    assert field.short_name == "nm"
    assert field._attr_path == "name"
    assert Dummy.__dict__["nm"] is field


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


def test_generate_sanitizes_invalid_names_and_skips_dotted_short_aliases():
    node_attr_code = generate_node_attr_code(
        "blendShape",
        attr_infos=_unsafe_identifier_attr_infos(),
    )
    assert node_attr_code is not None
    compile(node_attr_code, "blend_shape_node_attr.py", "exec")

    assert "class PntsPlugOperator(" in node_attr_code
    assert "class .pntsPlugOperator(" not in node_attr_code
    assert ".pt.x = px" not in node_attr_code
    assert '("px", ".pt.x")' in node_attr_code
    assert '("weights", "wl.w")' in node_attr_code
    assert "wl.w = weights" not in node_attr_code

    node_code = generate_node_class_code(
        "blendShape",
        attr_infos=_unsafe_identifier_attr_infos(),
    )
    compile(node_code, "blend_shape.py", "exec")

    assert (
        'weight = FloatField(multi=True, long_name=".weight", short_name=".w")'
        in node_code
    )
    assert ".weight = FloatField" not in node_code
    assert ".w = " not in node_code
    assert (
        'pnts = PntsField(multi=True, long_name=".pnts", short_name=".pt")'
        in node_code
    )
    assert ".pnts = " not in node_code
    assert ".pt = " not in node_code


def test_generate_prefers_attr_path_name_when_available():
    node_attr_code = generate_node_attr_code(
        "hierarchyTestNode4",
        attr_infos=_path_name_attr_infos(),
    )
    assert node_attr_code is not None
    compile(node_attr_code, "hierarchy_test_node4_node_attr.py", "exec")

    assert "class PntsPlugOperator(" in node_attr_code
    assert '("px", ".pt.x")' in node_attr_code
    assert "px = DoubleField()" in node_attr_code

    node_code = generate_node_class_code(
        "hierarchyTestNode4",
        attr_infos=_path_name_attr_infos(),
    )
    compile(node_code, "hierarchy_test_node4.py", "exec")

    assert (
        'pnts = PntsField(multi=True, long_name=".pnts", short_name=".pt")'
        in node_code
    )
    assert "pt = pnts" not in node_code


def test_generate_escapes_reserved_field_and_class_names():
    node_attr_code = generate_node_attr_code(
        "reservedNode",
        attr_infos=_reserved_name_attr_infos(),
    )
    assert node_attr_code is not None
    compile(node_attr_code, "reserved_node_attr.py", "exec")

    assert "class CompoundValuePlugOperator(" in node_attr_code
    assert "class CompoundAttrOperator(" not in node_attr_code
    assert "class CompoundValueField(" in node_attr_code

    node_code = generate_node_class_code(
        "reservedNode",
        attr_infos=_reserved_name_attr_infos(),
    )
    compile(node_code, "reserved_node.py", "exec")

    assert (
        'name_ = DataStringField(long_name="name", short_name="nm")'
        in node_code
    )
    assert "nm = name_" in node_code
    assert "name = DataStringField" not in node_code
    assert "compound = CompoundValueField()" in node_code
    assert "cmp = compound" in node_code


def test_generate_plus_minus_average_node_class_code():
    code = generate_node_class_code(
        "plusMinusAverage",
        attr_infos=_plus_minus_average_attr_infos(),
    )

    compile(code, "plus_minus_average.py", "exec")

    assert "from ....attr.define.node_attr.plus_minus_average import" in code
    assert "from ....attr.define.std.at.scalar.enum import" in code
    assert (
        "from ....attr.define.std.at.scalar.numeric.range.float "
        "import FloatField"
    ) in code
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
    assert "class _GeneratedPlusMinusAverage(DG):" in code


def test_generate_transform_node_class_code():
    code = generate_node_class_code(
        "joint",
        attr_infos=_joint_like_attr_infos(),
        node_kind="transform",
        inherited_attr_infos=_transform_like_attr_infos(),
    )

    compile(code, "joint.py", "exec")

    assert "from .._core import Transform" in code
    assert "from .....attr.define.node_attr.joint import JointOrientField" in code
    assert (
        "from .....attr.define.std.at.scalar.numeric.bool "
        "import BoolField"
    ) in code
    assert "class _GeneratedJoint(Transform):" in code
    assert 'NODE_TYPE = "joint"' in code
    assert "message = MessageField()" not in code
    assert "translate = TranslateField()" not in code
    assert "translateX = translate.translateX" not in code
    assert "jointOrient = JointOrientField()" in code
    assert "jo = jointOrient" in code
    assert "jointOrientX = jointOrient.jointOrientX" in code
    assert "jox = jointOrientX" in code
    assert "segmentScaleCompensate = BoolField(default_value=True)" in code
    assert "ssc = segmentScaleCompensate" in code


def test_generate_transform_base_node_class_code():
    code = generate_node_class_code(
        "transform",
        attr_infos=_transform_like_attr_infos(),
        node_kind="transform",
    )

    compile(code, "transform.py", "exec")

    assert "from ..._core import DAG" in code
    assert "from .....attr.define.node_attr.transform import TranslateField" in code
    assert "class _GeneratedTransform(DAG):" in code
    assert 'NODE_TYPE = "transform"' in code
    assert "translate = TranslateField()" in code


def test_generate_shape_node_class_code():
    code = generate_node_class_code(
        "mesh",
        attr_infos=_shape_like_attr_infos(),
        node_kind="shape",
    )

    compile(code, "mesh.py", "exec")

    assert "from .._core import Shape" in code
    assert "from .....attr.define.std.dt.mesh import DataMeshField" in code
    assert "class _GeneratedMesh(Shape):" in code
    assert 'NODE_TYPE = "mesh"' in code
    assert "message = MessageField()" not in code
    assert "outMesh = DataMeshField(writable=False)" in code
    assert "out = outMesh" in code
    assert "face = TypedField(multi=True)" in code
    assert "fc = face" in code
    assert "TODO: face" not in code


def test_generate_field_init_args_include_attribute_metadata():
    code = generate_node_class_code(
        "metadataNode",
        attr_infos=[
            _attr(
                "input",
                "in",
                "float",
                default_value=[0.5],
                min_value=[0.0],
                max_value=[1.0],
                soft_min_value=[0.25],
                soft_max_value=[0.75],
                category=["bdMetadata"],
            ),
            _attr(
                "output",
                "out",
                "double",
                default_value=[0.0],
                writable=False,
            ),
            _attr(
                "hidden",
                "hdn",
                "bool",
                default_value=[0.0],
                min_value=[0.0],
                max_value=[1.0],
                readable=False,
            ),
            _attr(
                "count",
                "cnt",
                "long",
                default_value=[3.0],
                min_value=[0.0],
                max_value=[10.0],
            ),
            _attr(
                "mode",
                "md",
                "enum",
                enum_name=["Off:On:Auto"],
                default_value=[2.0],
                min_value=[0.0],
                max_value=[2.0],
            ),
            _attr(
                "vector",
                "vec",
                "float3",
                default_value=[1.0, 2.0, 3.0],
                min_value=[-1.0, -2.0, -3.0],
                number_of_children=3,
            ),
            _attr(
                "indices",
                "idx",
                "long3",
                default_value=[1.0, 2.0, 3.0],
                min_value=[0.0, 0.0, 0.0],
                number_of_children=3,
            ),
            _attr(
                "notANumber",
                "nanv",
                "float",
                default_value=[float("nan")],
            ),
            _attr(
                "infiniteRange",
                "infr",
                "float2",
                default_value=[float("-inf"), float("inf")],
                number_of_children=2,
            ),
        ],
    )

    compile(code, "metadata_node.py", "exec")

    assert (
        "input = FloatField(default_value=0.5, min_value=0.0, "
        'max_value=1.0, soft_min_value=0.25, soft_max_value=0.75, category="bdMetadata")'
        in code
    )
    assert "output = DoubleField(default_value=0.0, writable=False)" in code
    assert "hidden = BoolField(default_value=False, readable=False)" in code
    assert "count = LongField(default_value=3, min_value=0, max_value=10)" in code
    assert "mode = ModeEnumField(default_value=2)" in code
    assert (
        "vector = Float3Field(default_value=(1.0, 2.0, 3.0), "
        "min_value=(-1.0, -2.0, -3.0))"
        in code
    )
    assert (
        "indices = Long3Field(default_value=(1, 2, 3), min_value=(0, 0, 0))"
        in code
    )
    assert 'notANumber = FloatField(default_value=float("nan"))' in code
    assert (
        'infiniteRange = Float2Field(default_value=(-float("inf"), '
        'float("inf")))'
        in code
    )
    assert "readable=True" not in code
    assert "writable=True" not in code
    assert "hidden = BoolField(default_value=0.0" not in code
    assert "mode = ModeEnumField(default_value=2, min_value=" not in code


def test_generate_suffixes_duplicate_enum_member_names():
    code = generate_node_class_code(
        "hardwareRenderGlobals",
        attr_infos=_duplicate_enum_attr_infos(),
    )

    compile(code, "hardware_render_globals.py", "exec")

    assert "    RGBA = 0" in code
    assert "    RGBA_2 = 2" in code
    assert '        RGBA: "RGBA",' in code
    assert '        RGBA_2: "RGBA",' in code


def test_generate_resolves_data_type_when_attribute_type_is_missing():
    code = generate_node_class_code(
        "dataTypeOnlyNode",
        attr_infos=_datatype_only_attr_infos(),
    )

    compile(code, "data_type_only_node.py", "exec")

    assert "DataMatrixField" in code
    assert "DataVectorArrayField" in code
    assert "localXform = DataMatrixField()" in code
    assert "positionList = DataVectorArrayField()" in code
    assert "TODO: localXform" not in code
    assert "TODO: positionList" not in code


def test_generate_compound_child_enum_uses_generated_enum_field():
    code = generate_node_attr_code(
        "compoundEnumNode",
        attr_infos=_compound_enum_attr_infos(),
    )

    assert code is not None
    compile(code, "compound_enum_node_attr.py", "exec")

    assert "class Primary_primaryModeEnumPlugOperator(" in code
    assert "class Primary_primaryModeEnumAttrOperator(" in code
    assert "class Primary_primaryModeEnumField(" in code
    assert "NAME_MAP = {" in code
    assert "primaryMode = Primary_primaryModeEnumField()" in code
    assert "primaryMode = EnumField()" not in code


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


def test_generate_node_class_file_skips_internal_node_type(tmp_path):
    generate_node_class_file(
        "nodeGraphEditorInfo",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dg",
        "node_graph_editor_info.py",
    )

    assert not output_path.exists()


def test_generate_node_class_file_can_include_skipped_node_type(tmp_path):
    generate_node_class_file(
        "nodeGraphEditorInfo",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        include_skipped=True,
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dg",
        "_generated",
        "node_graph_editor_info.py",
    )
    public_path = output_path.parent.parent / "node_graph_editor_info.py"
    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(code, "node_graph_editor_info.py", "exec")
    compile(public_code, "node_graph_editor_info_public.py", "exec")
    assert 'NODE_TYPE = "nodeGraphEditorInfo"' in code
    assert "default = BoolField()" in code
    assert "def_ = default" in code
    assert (
        "class NodeGraphEditorInfo(_GeneratedNodeGraphEditorInfo):"
        in public_code
    )


def test_generate_node_class_file_preserves_existing_public_wrapper(tmp_path):
    public_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dg",
        "custom_node.py",
    )
    public_path.parent.mkdir(parents=True, exist_ok=True)
    public_path.write_text("# handwritten public wrapper\n", encoding="utf-8")

    generate_node_class_file(
        "customNode",
        tmp_path,
        attr_infos=[_attr("input", "in", "float")],
    )

    generated_path = public_path.parent / "_generated" / "custom_node.py"

    assert generated_path.exists()
    assert (
        public_path.read_text(encoding="utf-8")
        == "# handwritten public wrapper\n"
    )


def test_generate_node_class_file_supports_keyword_module_wrapper(tmp_path):
    generate_node_class_file(
        "and",
        tmp_path,
        attr_infos=[_attr("input", "in", "float")],
    )

    public_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dg",
        "and.py",
    )
    code = public_path.read_text(encoding="utf-8")

    compile(code, "and_public.py", "exec")
    assert "from importlib import import_module" in code
    assert 'f"{__package__}._generated.and"' in code
    assert "class And(_GeneratedAnd):" in code


def test_generate_node_class_file_skips_unsafe_dag_node_type(tmp_path):
    generate_node_class_file(
        "caddyManipBase",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "caddy_manip_base.py",
    )

    assert not output_path.exists()


def test_generate_node_class_file_can_include_unsafe_dag_node_type(tmp_path):
    generate_node_class_file(
        "caddyManipBase",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        include_skipped=True,
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "_generated",
        "caddy_manip_base.py",
    )
    public_path = output_path.parent.parent / "caddy_manip_base.py"
    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(code, "caddy_manip_base.py", "exec")
    compile(public_code, "caddy_manip_base_public.py", "exec")
    assert 'NODE_TYPE = "caddyManipBase"' in code
    assert "default = BoolField()" in code
    assert "def_ = default" in code
    assert "class CaddyManipBase(_GeneratedCaddyManipBase):" in public_code


def test_generate_node_class_file_skips_unsafe_dag_tool_node_type(tmp_path):
    generate_node_class_file(
        "placerTool",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "placer_tool.py",
    )

    assert not output_path.exists()


def test_generate_node_class_file_can_include_unsafe_dag_tool_node_type(
    tmp_path,
):
    generate_node_class_file(
        "placerTool",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        include_skipped=True,
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "_generated",
        "placer_tool.py",
    )
    public_path = output_path.parent.parent / "placer_tool.py"
    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(code, "placer_tool.py", "exec")
    compile(public_code, "placer_tool_public.py", "exec")
    assert 'NODE_TYPE = "placerTool"' in code
    assert "default = BoolField()" in code
    assert "def_ = default" in code
    assert "class PlacerTool(_GeneratedPlacerTool):" in public_code


def test_generate_node_class_file_outputs_xgm_dag_node_type(tmp_path):
    generate_node_class_file(
        "xgmSubPatch",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "_generated",
        "xgm_sub_patch.py",
    )
    public_path = output_path.parent.parent / "xgm_sub_patch.py"
    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(code, "xgm_sub_patch.py", "exec")
    compile(public_code, "xgm_sub_patch_public.py", "exec")
    assert 'NODE_TYPE = "xgmSubPatch"' in code
    assert "default = BoolField()" in code
    assert "def_ = default" in code
    assert "class XgmSubPatch(_GeneratedXgmSubPatch):" in public_code


def test_generate_node_class_file_skips_unsafe_dag_node_type_keyword(
    tmp_path,
):
    generate_node_class_file(
        "buttonManip",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "button_manip.py",
    )

    assert not output_path.exists()


def test_generate_node_class_file_can_include_unsafe_dag_node_type_keyword(
    tmp_path,
):
    generate_node_class_file(
        "buttonManip",
        tmp_path,
        attr_infos=[_attr("default", "def", "bool")],
        include_skipped=True,
        node_kind="dag",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "_generated",
        "button_manip.py",
    )
    public_path = output_path.parent.parent / "button_manip.py"
    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(code, "button_manip.py", "exec")
    compile(public_code, "button_manip_public.py", "exec")
    assert 'NODE_TYPE = "buttonManip"' in code
    assert "default = BoolField()" in code
    assert "def_ = default" in code
    assert "class ButtonManip(_GeneratedButtonManip):" in public_code


def test_generate_node_class_file_outputs_transform_node_path(tmp_path):
    generate_node_class_file(
        "joint",
        tmp_path,
        attr_infos=_joint_like_attr_infos(),
        node_kind="transform",
        inherited_attr_infos=_transform_like_attr_infos(),
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "transform",
        "_generated",
        "joint.py",
    )
    public_path = output_path.parent.parent / "joint.py"
    node_attr_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "attr",
        "define",
        "node_attr",
        "joint.py",
    )

    assert output_path.exists()
    assert node_attr_path.exists()

    code = output_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")
    node_attr_code = node_attr_path.read_text(encoding="utf-8")

    compile(code, "joint.py", "exec")
    compile(public_code, "joint_public.py", "exec")
    compile(node_attr_code, "joint_node_attr.py", "exec")
    assert "from .._core import Transform" in code
    assert "from .....attr.define.node_attr.joint import JointOrientField" in code
    assert "class Joint(_GeneratedJoint):" in public_code
    assert "translate = TranslateField()" not in code
    assert "class TranslateField(" not in node_attr_code
    assert "class JointOrientField(" in node_attr_code


def test_generate_node_class_file_outputs_transform_base_path(tmp_path):
    core_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "transform",
        "_core.py",
    )
    core_path.parent.mkdir(parents=True, exist_ok=True)
    core_path.write_text("# manual transform class\n", encoding="utf-8")

    generate_node_class_file(
        "transform",
        tmp_path,
        attr_infos=_transform_like_attr_infos(),
        node_kind="transform",
    )

    output_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "transform",
        "_generated",
        "transform.py",
    )

    assert output_path.exists()
    assert core_path.read_text(encoding="utf-8") == "# manual transform class\n"

    code = output_path.read_text(encoding="utf-8")

    compile(code, "transform.py", "exec")
    assert "from ..._core import DAG" in code
    assert "class _GeneratedTransform(DAG):" in code


def test_generate_node_class_file_outputs_shape_base_path(tmp_path):
    generate_node_class_file(
        "shape",
        tmp_path,
        attr_infos=_shape_like_attr_infos(),
        node_kind="shape",
    )

    generated_path = tmp_path.joinpath(
        "bd_util",
        "maya",
        "node",
        "operator",
        "node",
        "dag",
        "shape",
        "_generated",
        "shape.py",
    )
    public_path = generated_path.parent.parent / "_core.py"
    generated_code = generated_path.read_text(encoding="utf-8")
    public_code = public_path.read_text(encoding="utf-8")

    compile(generated_code, "shape.py", "exec")
    compile(public_code, "shape_public.py", "exec")
    assert "from ..._core import DAG" in generated_code
    assert "class _GeneratedShape(DAG):" in generated_code
    assert "class Shape(_GeneratedShape):" in public_code
