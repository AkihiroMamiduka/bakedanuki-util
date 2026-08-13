# coding: utf-8
"""
Maya ノードの attributeQuery 情報をもとに、Node Operator クラスの
Python ファイルを生成するモジュール。

生成される attribute 定義は node kind ごとの ``_generated`` package
以下に配置する。公開 module は従来のパスに維持し、生成 class を継承する
手書き可能な wrapper として扱う。

使用例::

    # Maya Python Script Editor で実行
    from bd_util._dev.maya.node.operator.node.generate import (
        generate_node_class_file,
    )

    generate_node_class_file(
        node_type="multiplyDivide",
        src_dir=r"C:/path/bakedanuki/bakedanuki-util/python",
    )
    # generated:
    # C:/path/bakedanuki/bakedanuki-util/python/bd_util/maya/node/operator/node/dg/_generated/multiply_divide.py
    # public:
    # C:/path/bakedanuki/bakedanuki-util/python/bd_util/maya/node/operator/node/dg/multiply_divide.py

    generate_node_class_file(
        node_type="joint",
        src_dir=r"C:/path/bakedanuki/bakedanuki-util/python",
        node_kind="transform",
    )
    # generated:
    # C:/path/bakedanuki/bakedanuki-util/python/bd_util/maya/node/operator/node/dag/transform/_generated/joint.py
    # public:
    # C:/path/bakedanuki/bakedanuki-util/python/bd_util/maya/node/operator/node/dag/transform/joint.py
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
import dataclasses
import keyword
import math
import pathlib
import re
from typing import cast

# self
from ...... import logger as u_logger
from ......maya.attr.query import AttrInfo, get_attribute_infos
from ......maya.node.all_types import (
    get_dag_node_types,
    get_dg_node_types,
    get_shape_types,
    get_transform_types,
)
from ......maya.node.type import (
    is_dag_node_type,
    is_shape_type,
    is_transform_type,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

# ---------------------------------------------------------------------------
# attribute_type → (Field クラス名, "define.at/dt モジュール名")
# ---------------------------------------------------------------------------

# attributeType ベースのマッピング (attr/define/std/at or attr/define/custom/at)
_AT_TYPE_MAP: dict[str, tuple[str, str]] = {
    "addr": ("AddrField", "define.std.at.addr"),
    "bool": ("BoolField", "define.std.at.scalar.numeric.bool"),
    "byte": ("ByteField", "define.std.at.scalar.numeric.range.byte"),
    "char": ("CharField", "define.std.at.scalar.numeric.range.char"),
    "compound": ("CompoundField", "define.std.at.compound"),
    "double": ("DoubleField", "define.std.at.scalar.numeric.range.double"),
    "double2": (
        "Double2Field",
        "define.custom",
    ),
    "double3": (
        "Double3Field",
        "define.custom",
    ),
    "double4": (
        "Double4Field",
        "define.custom",
    ),
    "doubleAngle": (
        "DoubleAngleField",
        "define.std.at.scalar.unit.range.double_angle",
    ),
    "doubleLinear": (
        "DoubleLinearField",
        "define.std.at.scalar.unit.range.double_linear",
    ),
    "enum": ("EnumField", "define.std.at.scalar.enum"),
    "float": ("FloatField", "define.std.at.scalar.numeric.range.float"),
    "float2": (
        "Float2Field",
        "define.custom",
    ),
    "float3": (
        "Float3Field",
        "define.custom",
    ),
    "floatAngle": (
        "FloatAngleField",
        "define.std.at.scalar.unit.range.float_angle",
    ),
    "floatLinear": (
        "FloatLinearField",
        "define.std.at.scalar.unit.range.float_linear",
    ),
    "fltMatrix": ("FltMatrixField", "define.std.at.flt_matrix"),
    "generic": ("GenericField", "define.std.at.generic"),
    "lightData": ("LightDataField", "define.std.at.light_data"),
    "long": ("LongField", "define.std.at.scalar.numeric.range.long"),
    "long2": (
        "Long2Field",
        "define.custom",
    ),
    "long3": (
        "Long3Field",
        "define.custom",
    ),
    "long long int": (
        "LongLongIntField",
        "define.std.at.scalar.numeric.range.long_long_int",
    ),
    "long_long_int": (
        "LongLongIntField",
        "define.std.at.scalar.numeric.range.long_long_int",
    ),
    "matrix": ("MatrixField", "define.std.at.matrix"),
    "message": ("MessageField", "define.std.at.message"),
    "polyFaces": ("TypedField", "define.std.at.typed"),
    "reflectance": ("ReflectanceField", "define.std.at.reflectance"),
    "short": ("ShortField", "define.std.at.scalar.numeric.range.short"),
    "short2": (
        "Short2Field",
        "define.custom",
    ),
    "short3": (
        "Short3Field",
        "define.custom",
    ),
    "spectrum": ("SpectrumField", "define.std.at.spectrum"),
    "time": ("TimeField", "define.std.at.scalar.unit.time"),
    "typed": ("TypedField", "define.std.at.typed"),
}

# dataType ベースのマッピング (dt/ ディレクトリ)
# attribute_type == "typed" のときに data_type で参照する
_DT_TYPE_MAP: dict[str, tuple[str, str]] = {
    "double2": ("DataDouble2Field", "define.std.dt.double2"),
    "double3": ("DataDouble3Field", "define.std.dt.double3"),
    "doubleArray": ("DataDoubleArrayField", "define.std.dt.double_array"),
    "float2": ("DataFloat2Field", "define.std.dt.float2"),
    "float3": ("DataFloat3Field", "define.std.dt.float3"),
    "floatArray": ("DataFloatArrayField", "define.std.dt.float_array"),
    "int32Array": ("DataInt32ArrayField", "define.std.dt.int32_array"),
    "lattice": ("DataLatticeField", "define.std.dt.lattice"),
    "long2": ("DataLong2Field", "define.std.dt.long2"),
    "long3": ("DataLong3Field", "define.std.dt.long3"),
    "matrix": ("DataMatrixField", "define.std.dt.matrix"),
    "mesh": ("DataMeshField", "define.std.dt.mesh"),
    "nurbsCurve": ("DataNurbsCurveField", "define.std.dt.nurbs_curve"),
    "nurbsSurface": (
        "DataNurbsSurfaceField",
        "define.std.dt.nurbs_surface",
    ),
    "pointArray": ("DataPointArrayField", "define.std.dt.point_array"),
    "reflectanceRGB": (
        "DataReflectanceRGBField",
        "define.std.dt.reflectance_rgb",
    ),
    "short2": ("DataShort2Field", "define.std.dt.short2"),
    "short3": ("DataShort3Field", "define.std.dt.short3"),
    "spectrumRGB": ("DataSpectrumRGBField", "define.std.dt.specrtrum_rgb"),
    "string": ("DataStringField", "define.std.dt.string"),
    "stringArray": ("DataStringArrayField", "define.std.dt.string_array"),
    "vectorArray": ("DataVectorArrayField", "define.std.dt.vector_array"),
}

# DG 基底クラス (_core.py の DG) で既に定義されているロング名 → スキップ対象
_DG_BASE_LONG_NAMES: frozenset[str] = frozenset(
    {
        "message",
        "caching",
        "frozen",
        "isHistoricallyInteresting",
        "nodeState",
        "binMembership",
    }
)

# DG node types that are intentionally outside the generated NodeOperator
# coverage. These are mostly editor/internal state nodes whose attributes are
# not useful as ordinary node-operation wrappers.
_SKIPPED_DG_NODE_TYPES: dict[str, str] = {
    "nodeGraphEditorInfo": (
        "Node Editor UI state node. Standalone mayapy cannot resolve all "
        "attribute types reliably, and the node is outside the practical "
        "NodeOperator target surface."
    ),
}

_SKIPPED_DAG_NODE_TYPES: dict[str, str] = {
    "caddyManipBase": (
        "Known unsafe manipulator node. Creating it from mayapy can cause a "
        "native Maya crash, so it is excluded from normal DAG generation."
    ),
    "placerTool": (
        "Known unsafe tool node. Creating it during DAG bulk generation can "
        "leave an unstable viewport tool overlay, so it is excluded from "
        "normal DAG generation."
    ),
}

_SKIPPED_DAG_NODE_TYPE_KEYWORDS: dict[str, str] = {
    "manip": (
        "Manipulator node type. Manipulator-related DAG nodes can make Maya "
        "unstable during bulk generation, so node types containing 'manip' "
        "are excluded from normal DAG generation."
    ),
}

# Maya 2025 / MtoA で default query がプロセス依存の未初期化値を返す
# Arnold attribute。安定した metadata として生成コードへ埋め込まない。
_ARNOLD_UNRELIABLE_DEFAULT_ATTRS: dict[str, frozenset[str]] = {
    "aiAOVDriver": frozenset(
        {
            "layerTolerance",
        }
    ),
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
    "aiMixShader": frozenset(
        {
            "shader1A",
            "shader2A",
        }
    ),
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
    "aiWriteInt": frozenset(
        {
            "beautyA",
        }
    ),
}

# node class 生成時の対象種別。
_NODE_KIND_DG = "dg"
_NODE_KIND_DAG = "dag"
_NODE_KIND_TRANSFORM = "transform"
_NODE_KIND_SHAPE = "shape"
_NODE_KIND_AUTO = "auto"

_VALID_NODE_KINDS: frozenset[str] = frozenset(
    {
        _NODE_KIND_DG,
        _NODE_KIND_DAG,
        _NODE_KIND_TRANSFORM,
        _NODE_KIND_SHAPE,
        _NODE_KIND_AUTO,
    }
)

_DAG_NODE_KINDS: frozenset[str] = frozenset(
    {
        _NODE_KIND_DAG,
        _NODE_KIND_TRANSFORM,
        _NODE_KIND_SHAPE,
    }
)


def _get_skipped_dag_node_type_reason(node_type: str) -> str | None:
    reason = _SKIPPED_DAG_NODE_TYPES.get(node_type)
    if reason:
        return reason

    node_type_lower = node_type.lower()
    for (
        skipped_keyword,
        skip_reason,
    ) in _SKIPPED_DAG_NODE_TYPE_KEYWORDS.items():
        if skipped_keyword.lower() in node_type_lower:
            return skip_reason
    return None


_INHERITED_ATTR_INFOS_CACHE: dict[str, list[AttrInfo]] = {}

# generate_node_class_file が src_dir から補完する DG node class パス部品
_DG_OUTPUT_REL_PARTS: tuple[str, ...] = (
    "bd_util",
    "maya",
    "node",
    "operator",
    "node",
    "dg",
)

# 互換用: 既存コードから参照されても DG 出力先を返す。
_OUTPUT_REL_PARTS = _DG_OUTPUT_REL_PARTS

# generate_node_class_file が src_dir から補完する DAG node class パス部品
_DAG_OUTPUT_REL_PARTS: tuple[str, ...] = (
    "bd_util",
    "maya",
    "node",
    "operator",
    "node",
    "dag",
)

_DAG_TRANSFORM_OUTPUT_REL_PARTS: tuple[str, ...] = (
    *_DAG_OUTPUT_REL_PARTS,
    "transform",
)

_DAG_SHAPE_OUTPUT_REL_PARTS: tuple[str, ...] = (
    *_DAG_OUTPUT_REL_PARTS,
    "shape",
)

# generate_node_class_file が src_dir から補完する node_attr パス部品
_NODE_ATTR_OUTPUT_REL_PARTS: tuple[str, ...] = (
    "bd_util",
    "maya",
    "node",
    "operator",
    "attr",
    "define",
    "node_attr",
)

# compound 型 → (基底 Plug, 基底 Attr, 基底 Field, node_attr からのモジュールパス)
_GENERIC_COMPOUND_AT_BASE: dict[str, tuple[str, str, str, str]] = {
    "compound": (
        "CompoundPlugOperator",
        "CompoundAttrOperator",
        "CompoundField",
        "std.at.compound",
    ),
    "lightData": (
        "LightDataPlugOperator",
        "LightDataAttrOperator",
        "LightDataField",
        "std.at.light_data",
    ),
}

_SCALAR_COMPOUND_AT_BASE: dict[
    tuple[str, str, int], tuple[str, str, str, str]
] = {
    (
        "double2",
        "double",
        2,
    ): (
        "Double2CompoundBasePlugOperator",
        "Double2CompoundBaseAttrOperator",
        "Double2CompoundBaseField",
        "custom",
    ),
    (
        "double3",
        "double",
        3,
    ): (
        "Double3CompoundBasePlugOperator",
        "Double3CompoundBaseAttrOperator",
        "Double3CompoundBaseField",
        "custom",
    ),
    (
        "double4",
        "double",
        4,
    ): (
        "Double4CompoundBasePlugOperator",
        "Double4CompoundBaseAttrOperator",
        "Double4CompoundBaseField",
        "custom",
    ),
    (
        "float2",
        "float",
        2,
    ): (
        "Float2CompoundBasePlugOperator",
        "Float2CompoundBaseAttrOperator",
        "Float2CompoundBaseField",
        "custom",
    ),
    (
        "float3",
        "float",
        3,
    ): (
        "Float3CompoundBasePlugOperator",
        "Float3CompoundBaseAttrOperator",
        "Float3CompoundBaseField",
        "custom",
    ),
    (
        "long2",
        "long",
        2,
    ): (
        "Long2CompoundBasePlugOperator",
        "Long2CompoundBaseAttrOperator",
        "Long2CompoundBaseField",
        "custom",
    ),
    (
        "long3",
        "long",
        3,
    ): (
        "Long3CompoundBasePlugOperator",
        "Long3CompoundBaseAttrOperator",
        "Long3CompoundBaseField",
        "custom",
    ),
    (
        "short2",
        "short",
        2,
    ): (
        "Short2CompoundBasePlugOperator",
        "Short2CompoundBaseAttrOperator",
        "Short2CompoundBaseField",
        "custom",
    ),
    (
        "short3",
        "short",
        3,
    ): (
        "Short3CompoundBasePlugOperator",
        "Short3CompoundBaseAttrOperator",
        "Short3CompoundBaseField",
        "custom",
    ),
    (
        "double2",
        "doubleAngle",
        2,
    ): (
        "DoubleAngle2CompoundBasePlugOperator",
        "DoubleAngle2CompoundBaseAttrOperator",
        "DoubleAngle2CompoundBaseField",
        "custom",
    ),
    (
        "double3",
        "doubleAngle",
        3,
    ): (
        "DoubleAngle3CompoundBasePlugOperator",
        "DoubleAngle3CompoundBaseAttrOperator",
        "DoubleAngle3CompoundBaseField",
        "custom",
    ),
    (
        "double2",
        "doubleLinear",
        2,
    ): (
        "DoubleLinear2CompoundBasePlugOperator",
        "DoubleLinear2CompoundBaseAttrOperator",
        "DoubleLinear2CompoundBaseField",
        "custom",
    ),
    (
        "double3",
        "doubleLinear",
        3,
    ): (
        "DoubleLinear3CompoundBasePlugOperator",
        "DoubleLinear3CompoundBaseAttrOperator",
        "DoubleLinear3CompoundBaseField",
        "custom",
    ),
    (
        "float2",
        "floatAngle",
        2,
    ): (
        "FloatAngle2CompoundBasePlugOperator",
        "FloatAngle2CompoundBaseAttrOperator",
        "FloatAngle2CompoundBaseField",
        "custom",
    ),
    (
        "float3",
        "floatAngle",
        3,
    ): (
        "FloatAngle3CompoundBasePlugOperator",
        "FloatAngle3CompoundBaseAttrOperator",
        "FloatAngle3CompoundBaseField",
        "custom",
    ),
    (
        "float2",
        "doubleAngle",
        2,
    ): (
        "FloatAngle2CompoundBasePlugOperator",
        "FloatAngle2CompoundBaseAttrOperator",
        "FloatAngle2CompoundBaseField",
        "custom",
    ),
    (
        "float3",
        "doubleAngle",
        3,
    ): (
        "FloatAngle3CompoundBasePlugOperator",
        "FloatAngle3CompoundBaseAttrOperator",
        "FloatAngle3CompoundBaseField",
        "custom",
    ),
    (
        "float2",
        "floatLinear",
        2,
    ): (
        "FloatLinear2CompoundBasePlugOperator",
        "FloatLinear2CompoundBaseAttrOperator",
        "FloatLinear2CompoundBaseField",
        "custom",
    ),
    (
        "float3",
        "floatLinear",
        3,
    ): (
        "FloatLinear3CompoundBasePlugOperator",
        "FloatLinear3CompoundBaseAttrOperator",
        "FloatLinear3CompoundBaseField",
        "custom",
    ),
    (
        "float2",
        "doubleLinear",
        2,
    ): (
        "FloatLinear2CompoundBasePlugOperator",
        "FloatLinear2CompoundBaseAttrOperator",
        "FloatLinear2CompoundBaseField",
        "custom",
    ),
    (
        "float3",
        "doubleLinear",
        3,
    ): (
        "FloatLinear3CompoundBasePlugOperator",
        "FloatLinear3CompoundBaseAttrOperator",
        "FloatLinear3CompoundBaseField",
        "custom",
    ),
}

_QUAT_COMPOUND_AT_BASE: tuple[str, str, str, str] = (
    "QuatCompoundBasePlugOperator",
    "QuatCompoundBaseAttrOperator",
    "QuatCompoundBaseField",
    "custom",
)


# ---------------------------------------------------------------------------
# 内部ユーティリティ
# ---------------------------------------------------------------------------


def _node_type_to_class_name(node_type: str) -> str:
    """ノードタイプ名をクラス名 (PascalCase) へ変換する。

    例: ``addDoubleLinear`` → ``AddDoubleLinear``
        ``MASH_Audio`` → ``MASHAudio``
        ``bdDbl_Add`` → ``BdDblAdd``
    """
    return "".join(
        part[0].upper() + part[1:] for part in node_type.split("_") if part
    )


def _node_kind_class_name(node_type: str, node_kind: str) -> str:
    return f"Generated{_node_type_to_class_name(node_type)}"


def _camel_to_snake(name: str) -> str:
    """camelCase 文字列を snake_case へ変換する。

    連続する大文字 (頭字語) はひとまとまりとして扱う。

    例::

        multiplyDivide      → multiply_divide
        HIK                 → hik
        MASH                → mash
        HIKCharacterNode    → hik_character_node
    """
    # 頭字語と次の単語の境界に _ を挿入 (例: HIKCharacter → HIK_Character)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    # 小文字/数字と大文字の境界に _ を挿入 (例: multiply_Divide → multiply_divide)
    name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", name)
    return name.lower().lstrip("_")


def _node_type_to_file_name(node_type: str) -> str:
    """ノードタイプ名をファイル名 (snake_case.py) へ変換する。

    例: ``multiplyDivide`` → ``multiply_divide.py``
    """
    return f"{_camel_to_snake(node_type)}.py"


def _validate_node_type_name_collisions(node_types: tuple[str, ...]) -> None:
    """Reject node types that collapse to the same Python symbol or module."""
    converters = {
        "class": _node_type_to_class_name,
        "module": _camel_to_snake,
    }
    collisions: list[str] = []

    for name_kind, converter in converters.items():
        mapped_names: dict[str, set[str]] = {}
        for node_type in node_types:
            mapped_names.setdefault(converter(node_type), set()).add(node_type)

        collisions.extend(
            "{} {!r}: {}".format(
                name_kind,
                mapped_name,
                ", ".join(repr(name) for name in sorted(source_names)),
            )
            for mapped_name, source_names in sorted(mapped_names.items())
            if len(source_names) > 1
        )

    if collisions:
        raise ValueError(
            "Node type name conversion collision: " + "; ".join(collisions)
        )


_NODE_TYPE_ASSIGNMENT_PATTERN = re.compile(
    r"^\s*NODE_TYPE\s*=\s*[\"']([^\"']+)[\"']",
    re.MULTILINE,
)


def _validate_existing_node_output(
    path: pathlib.Path,
    node_type: str,
) -> None:
    """Prevent a normalized file name from overwriting another node type."""
    if not path.is_file():
        return

    match = _NODE_TYPE_ASSIGNMENT_PATTERN.search(
        path.read_text(encoding="utf-8")
    )
    if match is None or match.group(1) == node_type:
        return

    raise ValueError(
        "Node type module name collision at {}: {!r} and {!r}".format(
            path,
            match.group(1),
            node_type,
        )
    )


def _resolve_node_kind(node_type: str, node_kind: str) -> str:
    """Return concrete generation kind for a node type."""
    if node_kind not in _VALID_NODE_KINDS:
        raise ValueError(
            "node_kind must be one of {}: {}".format(
                sorted(_VALID_NODE_KINDS),
                node_kind,
            )
        )

    if node_kind != _NODE_KIND_AUTO:
        return node_kind

    if is_transform_type(node_type):
        return _NODE_KIND_TRANSFORM
    if is_shape_type(node_type):
        return _NODE_KIND_SHAPE
    if is_dag_node_type(node_type):
        return _NODE_KIND_DAG
    return _NODE_KIND_DG


def _node_kind_base_class_name(node_type: str, node_kind: str) -> str:
    if node_kind == _NODE_KIND_DG:
        return "DG"
    if node_kind == _NODE_KIND_DAG:
        return "DAG"
    if node_kind == _NODE_KIND_TRANSFORM:
        if node_type == "transform":
            return "DAG"
        return "Transform"
    if node_kind == _NODE_KIND_SHAPE:
        if node_type == "shape":
            return "DAG"
        return "Shape"
    raise ValueError(f"Unsupported node kind: {node_kind}")


def _node_kind_base_import_line(node_type: str, node_kind: str) -> str:
    if node_kind == _NODE_KIND_DG:
        return "from .._core import DG"
    if node_kind == _NODE_KIND_DAG:
        return "from .._core import DAG"
    if node_kind == _NODE_KIND_TRANSFORM:
        if node_type == "transform":
            return "from ..._core import DAG"
        return "from .._core import Transform"
    if node_kind == _NODE_KIND_SHAPE:
        if node_type == "shape":
            return "from ..._core import DAG"
        return "from .._core import Shape"
    raise ValueError(f"Unsupported node kind: {node_kind}")


def _node_kind_attr_import_prefix(node_kind: str) -> str:
    if node_kind in {_NODE_KIND_TRANSFORM, _NODE_KIND_SHAPE}:
        return ".....attr"
    if node_kind in {_NODE_KIND_DG, _NODE_KIND_DAG}:
        return "....attr"
    raise ValueError(f"Unsupported node kind: {node_kind}")


def _node_kind_output_rel_parts(node_kind: str) -> tuple[str, ...]:
    if node_kind == _NODE_KIND_DG:
        return _DG_OUTPUT_REL_PARTS
    if node_kind == _NODE_KIND_DAG:
        return _DAG_OUTPUT_REL_PARTS
    if node_kind == _NODE_KIND_TRANSFORM:
        return _DAG_TRANSFORM_OUTPUT_REL_PARTS
    if node_kind == _NODE_KIND_SHAPE:
        return _DAG_SHAPE_OUTPUT_REL_PARTS
    raise ValueError(f"Unsupported node kind: {node_kind}")


def _node_kind_public_output_file_name(
    node_type: str,
    node_kind: str,
) -> str:
    if node_kind == _NODE_KIND_TRANSFORM and node_type == "transform":
        return "_core.py"
    if node_kind == _NODE_KIND_SHAPE and node_type == "shape":
        return "_core.py"
    return _node_type_to_file_name(node_type)


def _generated_package_parts(node_kind: str) -> tuple[str, ...]:
    return (*_node_kind_output_rel_parts(node_kind), "_generated")


def _generate_public_node_class_code(
    node_type: str,
    node_kind: str,
) -> str:
    class_name = _node_type_to_class_name(node_type)
    generated_class_name = _node_kind_class_name(node_type, node_kind)
    module_name = _camel_to_snake(node_type)

    if keyword.iskeyword(module_name):
        import_lines = [
            "from importlib import import_module",
            "",
            f"{generated_class_name} = import_module(",
            f'    f"{{__package__}}._generated.{module_name}"',
            f").{generated_class_name}",
        ]
    else:
        import_lines = [
            "from ._generated.{} import {}".format(
                module_name,
                generated_class_name,
            )
        ]

    lines = [
        "# coding: utf-8",
        *import_lines,
        "",
        "",
        f"class {class_name}({generated_class_name}):",
        "    __slots__ = ()",
        "",
        f'    NODE_TYPE = "{node_type}"',
        "",
    ]
    return "\n".join(lines)


def _node_kind_inherited_node_type(
    node_type: str,
    node_kind: str,
) -> str | None:
    if node_kind == _NODE_KIND_TRANSFORM and node_type != "transform":
        return "transform"
    return None


def _get_inherited_attr_infos(
    node_type: str,
    node_kind: str,
) -> list[AttrInfo]:
    inherited_node_type = _node_kind_inherited_node_type(
        node_type,
        node_kind,
    )
    if inherited_node_type is None:
        return []

    cached = _INHERITED_ATTR_INFOS_CACHE.get(inherited_node_type)
    if cached is not None:
        return cached

    attr_infos = get_attribute_infos(
        inherited_node_type,
        mode_new_scene=True,
        mode_error_skip=True,
    )
    _INHERITED_ATTR_INFOS_CACHE[inherited_node_type] = attr_infos
    return attr_infos


def _attr_long_names(attr_infos: list[AttrInfo]) -> frozenset[str]:
    return frozenset(_attr_long_name(info) for info in attr_infos)


def _omit_unreliable_default_values(
    node_type: str,
    attr_infos: list[AttrInfo],
) -> list[AttrInfo]:
    attr_names = _ARNOLD_UNRELIABLE_DEFAULT_ATTRS.get(node_type)
    if not attr_names:
        return attr_infos

    return [
        (
            dataclasses.replace(attr_info, default_value=None)
            if _attr_long_name(attr_info) in attr_names
            else attr_info
        )
        for attr_info in attr_infos
    ]


def _filter_inherited_attr_infos(
    attr_infos: list[AttrInfo],
    inherited_long_names: frozenset[str],
) -> list[AttrInfo]:
    if not inherited_long_names:
        return attr_infos

    filtered_attr_infos: list[AttrInfo] = []
    for info in attr_infos:
        long_name = _attr_long_name(info)
        parent_name = _attr_parent_name(info)
        if (
            long_name in inherited_long_names
            or parent_name in inherited_long_names
        ):
            continue
        filtered_attr_infos.append(info)
    return filtered_attr_infos


def _node_kind_base_long_names(node_kind: str) -> frozenset[str]:
    # DG base attrs are inherited by both DG and DAG dependency nodes.
    return _DG_BASE_LONG_NAMES


def _resolve_attr_class(attr_info: AttrInfo) -> tuple[str, str] | None:
    """AttrInfo から ``(Field クラス名, モジュールパス)`` を返す。

    ``attribute_type == "typed"`` かつ ``data_type`` が設定されている場合は
    ``_DT_TYPE_MAP`` で解決し、それ以外は ``_AT_TYPE_MAP`` で解決する。
    解決できない場合は ``None`` を返す。

    Returns:
        tuple[str, str] | None: (クラス名, モジュール相対パス) または None
    """
    # Some built-in attrs report dataType but no attributeType in MFn query.
    attribute_type = attr_info.attribute_type
    if attribute_type in {None, "typed"} and attr_info.data_type:
        result = _DT_TYPE_MAP.get(attr_info.data_type)
        if result:
            return result

    if attribute_type is None:
        return None
    return _AT_TYPE_MAP.get(attribute_type)


def _node_attr_module_path(module_path: str) -> str:
    """node_attr 生成ファイルから import できるモジュールパスへ変換する。"""
    if module_path == "custom" or module_path.startswith("custom."):
        return "custom"

    prefix = "define."
    if module_path.startswith(prefix):
        module_path = module_path[len(prefix) :]

    if module_path == "custom" or module_path.startswith("custom."):
        return "custom"

    return module_path


def _node_module_attr_path(module_path: str) -> str:
    """node 生成ファイル向けに custom attribute の import 窓口を統一する。"""
    if module_path == "define.custom" or module_path.startswith(
        "define.custom."
    ):
        return "define.custom"
    return module_path


def _attr_long_name(attr_info: AttrInfo) -> str:
    """Return the canonical Maya attr path used for generated code."""
    return getattr(attr_info, "path_name", None) or attr_info.long_name


def _attr_parent_name(attr_info: AttrInfo) -> str | None:
    """Return the canonical parent attr path for generated code."""
    if not attr_info.parent:
        return None

    long_name = _attr_long_name(attr_info)
    if "." in long_name:
        parent_path = long_name.rsplit(".", 1)[0]
        if parent_path:
            return parent_path

    return attr_info.parent[0]


def _normalize_attr_hierarchy(attr_infos: list[AttrInfo]) -> list[AttrInfo]:
    """Return copies whose path names preserve nested compound parents."""
    infos_by_name: dict[str, AttrInfo] = {}
    for info in attr_infos:
        for name in {
            info.long_name,
            info.long_name.rsplit(".", 1)[-1],
            info.path_name,
            info.path_name.rsplit(".", 1)[-1] if info.path_name else None,
        }:
            if name:
                infos_by_name.setdefault(name, info)

    resolved_paths: dict[int, str] = {}

    def _resolve_path(info: AttrInfo, resolving: set[int]) -> str:
        info_id = id(info)
        if info_id in resolved_paths:
            return resolved_paths[info_id]

        original_path = info.path_name or info.long_name
        if not info.parent or info_id in resolving:
            resolved_paths[info_id] = original_path
            return original_path

        parent_name = info.parent[0]
        parent_info = infos_by_name.get(parent_name)
        if parent_info is None:
            parent_info = infos_by_name.get(parent_name.rsplit(".", 1)[-1])
        if parent_info is None or parent_info is info:
            resolved_paths[info_id] = original_path
            return original_path

        parent_path = _resolve_path(parent_info, resolving | {info_id})
        if original_path.startswith(f"{parent_path}."):
            resolved_path = original_path
        else:
            local_name = original_path.rsplit(".", 1)[-1]
            resolved_path = f"{parent_path}.{local_name}"
        resolved_paths[info_id] = resolved_path
        return resolved_path

    return [
        dataclasses.replace(info, path_name=_resolve_path(info, set()))
        for info in attr_infos
    ]


def _uniform_child_attr_type(children: list[AttrInfo]) -> str | None:
    """Return child attributeType when all children share the same type."""
    if not children:
        return None

    child_types = [child.attribute_type for child in children]
    first_child_type = child_types[0]
    if first_child_type is None:
        return None
    if any(child_type != first_child_type for child_type in child_types):
        return None
    return first_child_type


def _is_quat_like_compound(
    parent_info: AttrInfo,
    children: list[AttrInfo],
    *,
    node_type: str | None = None,
) -> bool:
    """Return whether Maya reports a four-double compound as a quat."""
    parent_long_name = _attr_long_name(parent_info)
    has_quat_semantics = "quat" in parent_long_name.lower() or (
        node_type is not None
        and node_type.startswith("bdQuat_")
        and parent_long_name == "value"
    )
    return (
        parent_info.attribute_type in {"compound", "double4"}
        and has_quat_semantics
        and len(children) == 4
        and _uniform_child_attr_type(children) == "double"
    )


def _resolve_compound_base(
    parent_info: AttrInfo,
    children: list[AttrInfo],
    *,
    node_type: str | None = None,
) -> tuple[str, str, str, str] | None:
    """compound 親と子情報から現行の基底クラス群を返す。"""
    if _is_quat_like_compound(
        parent_info,
        children,
        node_type=node_type,
    ):
        return _QUAT_COMPOUND_AT_BASE

    attribute_type = parent_info.attribute_type
    if attribute_type is None:
        return None

    result = _GENERIC_COMPOUND_AT_BASE.get(attribute_type)
    if result is not None:
        return result

    first_child_type = _uniform_child_attr_type(children)
    if first_child_type is None:
        return None

    key = (attribute_type, first_child_type, len(children))
    return _SCALAR_COMPOUND_AT_BASE.get(key)


def _contains_angle_brackets_in_attribute_type(attr_info: AttrInfo) -> bool:
    """attributeType に ``<`` または ``>`` を含む場合に True を返す。

    ``attributeType`` が ``None`` の場合は False を返す（スキップしない）。
    None のまま下流の :func:`_resolve_attr_class` に渡すと ``None`` が返り、
    呼び出し元で TODO コメントが出力される。
    手動での追記が必要であることを示すために意図的に通過させる。
    """
    attr_type = attr_info.attribute_type
    if attr_type is None:
        return False
    return "<" in attr_type or ">" in attr_type


def _filter_supported_attr_infos(attr_infos: list[AttrInfo]) -> list[AttrInfo]:
    """``attributeType`` に ``<`` / ``>`` を含まない属性情報のみを返す。"""
    return [
        info
        for info in attr_infos
        if not _contains_angle_brackets_in_attribute_type(info)
    ]


def _parse_enum_entries(
    enum_name_raw: object,
) -> list[tuple[str, int | None]] | None:
    """``cmds.attributeQuery(..., listEnum=True)`` の戻り値をパースする。

    Maya は ``["No operation:Sum:Subtract:Average"]`` や
    ``["Normal:HasNoEffect:Blocking:Waiting-Normal=8:Waiting-HasNoEffect:Waiting-Blocking"]``
    のようなリストを返す。コロンで分割し、各エントリを ``(ラベル, 明示的整数値 or None)``
    のタプルとして返す。

    明示的整数値は、前の値から連続していない場合にのみ設定される。
    取得できない場合は ``None`` を返す。
    """
    if not enum_name_raw:
        return None

    if isinstance(enum_name_raw, (list, tuple)):
        enum_names = cast(Sequence[object], enum_name_raw)
        raw = str(enum_names[0]) if enum_names else ""
    else:
        raw = str(enum_name_raw)

    raw_parts = [p.strip() for p in raw.split(":") if p.strip()]
    if not raw_parts:
        return None

    entries: list[tuple[str, int | None]] = []
    next_value = 0
    for part in raw_parts:
        # Maya の explicit value は "ラベル=整数値" の形式。
        # ラベル自体に "=" が含まれる場合 ("==", "!=" 等) は、
        # 末尾の "=" から分割した右辺が純粋な非負整数の場合のみ
        # explicit value として認識する。
        val = next_value
        label = part
        if "=" in part:
            possible_label, possible_val = part.rsplit("=", 1)
            possible_val = possible_val.strip()
            if possible_val.isdigit():
                label = possible_label.strip()
                val = int(possible_val)

        explicit = val if val != next_value else None
        entries.append((label, explicit))
        next_value = val + 1

    return entries if entries else None


def _build_attr_init_args(attr_info: AttrInfo) -> list[str]:
    """Field コンストラクタ引数リストを生成する。

    例: ``multi=True`` / ``default_value=0.0`` / ``writable=False``
    """
    args: list[str] = []

    if attr_info.multi:
        args.append("multi=True")

    for arg_name, value in _iter_attr_metadata_args(attr_info):
        args.append(f"{arg_name}={_field_arg_literal(value)}")

    return args


def _field_arg_literal(value: object) -> str:
    """Return a stable Python literal for generated Field kwargs."""
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, float):
        if math.isnan(value):
            return 'float("nan")'
        if math.isinf(value):
            sign = "-" if value < 0 else ""
            return f'{sign}float("inf")'
    if isinstance(value, tuple):
        values = cast(tuple[object, ...], value)
        items = ", ".join(_field_arg_literal(item) for item in values)
        if len(values) == 1:
            items += ","
        return f"({items})"
    if isinstance(value, list):
        values = cast(list[object], value)
        items = ", ".join(_field_arg_literal(item) for item in values)
        return f"[{items}]"
    return repr(value)


def _normalize_attr_query_value(value: object) -> object | None:
    """Normalize Maya attributeQuery list results for Field kwargs."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        values = cast(Sequence[object], value)
        if not values:
            return None
        if len(values) == 1:
            return values[0]
        return tuple(values)
    return value


_BOOL_ATTR_TYPES: frozenset[str] = frozenset({"bool"})

_INT_ATTR_TYPES: frozenset[str] = frozenset(
    {
        "byte",
        "char",
        "short",
        "long",
        "long long int",
        "long_long_int",
        "short2",
        "short3",
        "long2",
        "long3",
    }
)

_ENUM_ATTR_TYPES: frozenset[str] = frozenset({"enum"})

_RANGE_ARG_NAMES: frozenset[str] = frozenset(
    {
        "min_value",
        "max_value",
        "soft_min_value",
        "soft_max_value",
    }
)


def _to_int_if_integral(value: object) -> object:
    """Convert Maya's numeric float result to int when it is integral."""
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def _normalize_int_metadata_value(value: object) -> object:
    """Normalize int-like metadata values, including compound tuples."""
    if isinstance(value, tuple):
        values = cast(tuple[object, ...], value)
        return tuple(_to_int_if_integral(item) for item in values)
    return _to_int_if_integral(value)


def _normalize_bool_metadata_value(value: object) -> object:
    """Normalize bool metadata default values from Maya query results."""
    value = _to_int_if_integral(value)
    if isinstance(value, int):
        return bool(value)
    return value


def _normalize_metadata_value(
    attr_info: AttrInfo,
    arg_name: str,
    value: object,
) -> object | None:
    """Normalize Field metadata by Maya attribute type."""
    attr_type = attr_info.attribute_type
    value = _normalize_attr_query_value(value)
    if value is None:
        return None

    if attr_type in _BOOL_ATTR_TYPES:
        if arg_name in _RANGE_ARG_NAMES:
            return None
        return _normalize_bool_metadata_value(value)

    if attr_type in _ENUM_ATTR_TYPES:
        if arg_name in _RANGE_ARG_NAMES:
            return None
        return _normalize_int_metadata_value(value)

    if attr_type in _INT_ATTR_TYPES:
        return _normalize_int_metadata_value(value)

    return value


def _replace_compound_default_with_child_defaults(
    attr_info: AttrInfo,
    children: list[AttrInfo],
) -> AttrInfo:
    """Use child metadata units for a compound default value."""
    if attr_info.default_value is None:
        return attr_info

    child_defaults: list[object] = []
    for child in children:
        value = _normalize_metadata_value(
            child,
            "default_value",
            child.default_value,
        )
        if value is None or isinstance(value, tuple):
            return attr_info
        child_defaults.append(value)
    if not child_defaults:
        return attr_info
    return dataclasses.replace(
        attr_info,
        default_value=tuple(child_defaults),
    )


def _normalize_category_value(value: object) -> str | None:
    """Normalize Maya category query results to AttributeField's string API."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        values = cast(Sequence[object], value)
        if not values:
            return None
        value = values[0]
    if value is None:
        return None
    return str(value)


def _iter_attr_metadata_args(
    attr_info: AttrInfo,
) -> Iterator[tuple[str, object]]:
    """Yield generated Field metadata kwargs for known Maya attr state."""
    for arg_name, value in (
        ("default_value", attr_info.default_value),
        ("min_value", attr_info.min_value),
        ("max_value", attr_info.max_value),
        ("soft_min_value", attr_info.soft_min_value),
        ("soft_max_value", attr_info.soft_max_value),
    ):
        value = _normalize_metadata_value(attr_info, arg_name, value)
        if value is not None:
            yield arg_name, value

    if attr_info.readable is False:
        yield "readable", False
    if attr_info.writable is False:
        yield "writable", False

    category = _normalize_category_value(attr_info.category)
    if category is not None:
        yield "category", category


# 記号をその英単語名に変換するマッピング。長い記号を先に処理する。
_SYMBOL_WORD_MAP: list[tuple[str, str]] = [
    ("==", "EQUAL_EQUAL"),
    ("!=", "NOT_EQUAL"),
    ("<=", "LESS_EQUAL"),
    (">=", "GREATER_EQUAL"),
    ("<", "LESS"),
    (">", "GREATER"),
    ("=", "EQUAL"),
    ("!", "NOT"),
    ("+", "PLUS"),
    ("-", "MINUS"),
    ("*", "STAR"),
    ("/", "SLASH"),
    ("&", "AMP"),
    ("|", "PIPE"),
    ("^", "CARET"),
    ("~", "TILDE"),
    ("%", "PERCENT"),
    ("@", "AT"),
    ("#", "HASH"),
    ("$", "DOLLAR"),
    ("?", "QUESTION"),
]


def _label_to_enum_member_name(label: str) -> str:
    """ラベル文字列を SCREAMING_SNAKE_CASE の Enum メンバー名へ変換する。

    記号ラベル (``"=="``, ``"!="`` 等) は :data:`_SYMBOL_WORD_MAP` で英単語に
    置き換えてから変換する。

    例:

    * ``"No operation"`` → ``"NO_OPERATION"``
    * ``"Waiting-Normal"`` → ``"WAITING_NORMAL"``
    * ``"=="`` → ``"EQUAL_EQUAL"``
    * ``"!="`` → ``"NOT_EQUAL"``
    * ``"<="`` → ``"LESS_EQUAL"``
    * ``"3D"`` → ``"_3D"`` (先頭が数字の場合はアンダースコアを付与)
    """
    # 記号を英単語に置き換える
    name = label
    for symbol, word in _SYMBOL_WORD_MAP:
        name = name.replace(symbol, f"_{word}_")

    # 英数字以外をアンダースコアに統一し、前後の余分なアンダースコアを除去
    name = re.sub(r"[^a-zA-Z0-9]+", "_", name)
    name = name.strip("_")
    if not name:
        # マッピングにない記号のみからなるラベルの場合、16進エンコードで代替
        name = "LABEL_" + label.encode().hex().upper()
    elif name[0].isdigit():
        name = "_" + name
    return name.upper()


_DIGIT_WORD: dict[str, str] = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


_GENERATED_COMPOUND_CLASS_NAME_COLLISIONS = {
    "CompoundPlugOperator",
    "CompoundAttrOperator",
    "CompoundField",
}

_MAX_GENERATED_LINE_LENGTH = 79

_FIELD_NAME_COLLISIONS = {
    "create",
    "delete",
    "delete_non_check",
    "exists",
    "fn_node",
    "is_instance",
    "local_name",
    "long_name",
    "m_obj",
    "modifier_manager",
    "name",
    "namespace",
    "namespace_colon",
    "node_class",
    "rename",
}


def _safe_attr_name(name: str) -> str:
    """Python の予約語・数字始まりと衝突するアトリビュート名を安全な識別子へ変換する。

    * Python の予約語の場合は末尾に ``_`` を付与する。
      例: ``from`` → ``from_``、``is`` → ``is_``
    * 先頭が数字の場合は、その数字を英単語に置き換える。
      例: ``11w`` → ``one1w``、``3d`` → ``threed``
    """
    name = re.sub(r"[^0-9a-zA-Z_]+", "_", name).strip("_")
    if not name:
        name = "attr"

    if name[0].isdigit():
        name = _DIGIT_WORD.get(name[0], f"digit{name[0]}") + name[1:]
    if keyword.iskeyword(name):
        name = name + "_"
    return name


def _safe_field_name(name: str) -> str:
    """Return a safe Python descriptor name for generated fields."""
    safe_name = _safe_attr_name(name)
    while safe_name in _FIELD_NAME_COLLISIONS:
        safe_name += "_"
    return safe_name


def _field_init_args(
    base_args: list[str],
    python_name: str,
    long_name: str,
    short_name: str | None,
) -> str:
    """Build Field constructor args, preserving Maya names when escaped."""
    args = list(base_args)
    if python_name != long_name:
        args.append(f'long_name="{long_name}"')
        if short_name:
            args.append(f'short_name="{short_name}"')
    return ", ".join(args)


def _is_deprecated_attr_name(name: str | None) -> bool:
    """Return True when Maya marks an attribute name as deprecated."""
    return bool(name and "deprecated" in name.lower())


def _should_emit_short_alias(
    short_name: str | None,
    long_name: str,
) -> bool:
    """Return True when a short name should be emitted as a Python alias."""
    if not short_name or short_name == long_name:
        return False
    if "." in short_name:
        return False
    if short_name[0].isdigit():
        return False
    if _is_deprecated_attr_name(short_name) or _is_deprecated_attr_name(
        long_name
    ):
        return False
    return True


def _build_import_lines(module_path: str, cls_names: list[str]) -> list[str]:
    """import 行を手書きコードに近い形で生成する。"""
    if len(cls_names) == 1:
        return [f"from {module_path} import {cls_names[0]}"]

    lines = [f"from {module_path} import ("]
    for cls_name in cls_names:
        lines.append(f"    {cls_name},")
    lines.append(")")
    return lines


def _build_class_header_lines(
    class_name: str,
    base_expr: str,
) -> list[str]:
    """generic base を持つ class 宣言を読みやすい複数行で生成する。"""
    return [
        f"class {class_name}(",
        f"    {base_expr}",
        "):",
    ]


def _get_child_attr_name(child_long_name: str, parent_long_name: str) -> str:
    """子アトリビュートの実際の名前を返す。マルチアトリビュートの場合は親プレフィックスを除去する。

    例::

        _get_child_attr_name("input2D.input2Dx", "input2D")  → "input2Dx"
        _get_child_attr_name("output2Dx",        "output2D") → "output2Dx"
    """
    prefix = parent_long_name + "."
    if child_long_name.startswith(prefix):
        return child_long_name[len(prefix) :]
    return child_long_name


def _long_name_to_compound_class_names(
    long_name: str,
) -> tuple[str, str, str]:
    """long_name を PascalCase の custom compound クラス名へ変換する。

    例: ``"input2D"`` →
    ``("Input2DPlugOperator", "Input2DAttrOperator", "Input2DField")``
    """
    safe_name = _safe_attr_name(long_name)
    pascal = safe_name[:1].upper() + safe_name[1:]
    if (
        f"{pascal}PlugOperator" in _GENERATED_COMPOUND_CLASS_NAME_COLLISIONS
        or f"{pascal}AttrOperator" in _GENERATED_COMPOUND_CLASS_NAME_COLLISIONS
        or f"{pascal}Field" in _GENERATED_COMPOUND_CLASS_NAME_COLLISIONS
    ):
        pascal = f"{pascal}Value"
    return f"{pascal}PlugOperator", f"{pascal}AttrOperator", f"{pascal}Field"


def _long_name_to_enum_class_name(long_name: str) -> str:
    """アトリビュートの long_name を PascalCase の Enum クラス名へ変換する。

    例: ``"operation"`` → ``"OperationEnum"``、
        ``"nodeState"`` → ``"NodeStateEnum"``
    """
    safe_name = _safe_attr_name(long_name)
    return safe_name[0].upper() + safe_name[1:] + "Enum"


def _enum_entries_to_name_values(
    entries: list[tuple[str, int | None]],
) -> list[tuple[str, str, int]]:
    """パース済み enum entry を ``(member, label, value)`` へ変換する。"""
    result: list[tuple[str, str, int]] = []
    used_member_names: set[str] = set()
    next_value = 0
    for label, explicit_value in entries:
        value = next_value if explicit_value is None else explicit_value
        member_name = _label_to_enum_member_name(label)
        if member_name in used_member_names:
            value_suffix = str(value).replace("-", "MINUS_")
            base_name = f"{member_name}_{value_suffix}"
            suffix = 2
            while base_name in used_member_names:
                base_name = f"{member_name}_{value_suffix}_{suffix}"
                suffix += 1
            member_name = base_name
        used_member_names.add(member_name)
        result.append((member_name, label, value))
        next_value = value + 1
    return result


def _build_enum_class_lines(
    base_name: str,
    entries: list[tuple[str, int | None]],
) -> list[str]:
    """現行 EnumOperator / EnumField 形式のコード行リストを生成する。

    Args:
        base_name (str): 生成するベース名 (例: ``"OperationEnum"``)
        entries (list[tuple[str, int | None]]): ``(ラベル, 明示的整数値 or None)`` のリスト

    Returns:
        list[str]: クラス定義のコード行リスト
    """
    name_values = _enum_entries_to_name_values(entries)
    plug_cls_name = f"{base_name}PlugOperator"
    attr_cls_name = f"{base_name}AttrOperator"
    field_cls_name = f"{base_name}Field"

    lines: list[str] = [
        f'class {plug_cls_name}(EnumPlugOperator["{attr_cls_name}"]):'
    ]
    lines.append("    __slots__ = ()")
    lines.append("")
    for member_name, _label, value in name_values:
        lines.append(f"    {member_name} = {value}")
    lines.append("")
    lines.append("")

    lines.append(f"class {attr_cls_name}(EnumAttrOperator[{plug_cls_name}]):")
    lines.append("    __slots__ = ()")
    lines.append("")
    for member_name, _label, value in name_values:
        lines.append(f"    {member_name} = {value}")
    lines.append("")
    lines.append("    NAME_MAP = {")
    for member_name, label, _value in name_values:
        name_map_line = f'        {member_name}: "{label}",'
        if len(name_map_line) <= _MAX_GENERATED_LINE_LENGTH:
            lines.append(name_map_line)
        else:
            lines.extend(
                (
                    f"        {member_name}: (",
                    f'            "{label}"',
                    "        ),",
                )
            )
    lines.append("    }")
    lines.append("")
    lines.append("")

    lines.append(f"class {field_cls_name}(")
    lines.append(f"    EnumField[{attr_cls_name}, {plug_cls_name}]")
    lines.append("):")
    lines.append("    __slots__ = ()")
    lines.append("")
    lines.append(f"    ATTR_CLS = {attr_cls_name}")
    lines.append(f"    PLUG_CLS = {plug_cls_name}")
    return lines


# ---------------------------------------------------------------------------
# 公開 API
# ---------------------------------------------------------------------------


# generate
def generate_node_attr_code(
    node_type: str,
    attr_infos: list[AttrInfo] | None = None,
) -> str | None:
    """compound 型アトリビュートを持つノードの
    node_attr ファイルコードを生成する。

    生成されるコードは ``bd_util.maya.node.operator.attr.define.node_attr`` 以下に配置する
    ことを想定した相対インポートを使用する。

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"multiplyDivide"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。

    Returns:
        str | None: 生成された Python コード文字列。
            対象の compound アトリビュートが存在しない場合は ``None``。
    """
    if attr_infos is None:
        attr_infos = get_attribute_infos(
            node_type,
            mode_new_scene=True,
            mode_error_skip=True,
        )

    attr_infos = _omit_unreliable_default_values(node_type, attr_infos)
    attr_infos = _filter_supported_attr_infos(attr_infos)
    attr_infos = _normalize_attr_hierarchy(attr_infos)

    # 子アトリビュートを親ごとにグループ化
    compound_children_map: dict[str, list[AttrInfo]] = {}
    for info in attr_infos:
        parent_name = _attr_parent_name(info)
        if parent_name is not None:
            compound_children_map.setdefault(parent_name, []).append(info)

    # compound タイプの親アトリビュートのみ対象（子が存在し、基底解決できるものに限る）
    compound_parents: list[AttrInfo] = [
        info
        for info in attr_infos
        if (
            compound_children_map.get(_attr_long_name(info))
            and _resolve_compound_base(
                info,
                compound_children_map.get(_attr_long_name(info), []),
                node_type=node_type,
            )
        )
    ]
    compound_parents.sort(
        key=lambda info: _attr_long_name(info).count("."),
        reverse=True,
    )

    if not compound_parents:
        return None

    # インポート収集: module_path → list[class_name]
    # 同一モジュール内は手書きコードに寄せるため、追加順を保持する。
    module_imports: dict[str, list[str]] = {}

    def _add_import(cls_name: str, mod_path: str) -> None:
        mod_path = _node_attr_module_path(mod_path)
        cls_names = module_imports.setdefault(mod_path, [])
        if cls_name not in cls_names:
            cls_names.append(cls_name)

    # 生成する EnumOperator / EnumField クラス: base_name -> entries
    enum_classes: dict[str, list[tuple[str, int | None]]] = {}

    # 各 compound アトリビュートのクラスブロックを生成
    class_blocks: list[list[str]] = []

    compound_field_classes = {
        _attr_long_name(info): _long_name_to_compound_class_names(
            _attr_long_name(info)
        )[2]
        for info in compound_parents
    }

    for parent_info in compound_parents:
        parent_long = _attr_long_name(parent_info)
        children = compound_children_map.get(parent_long, [])
        if not children:
            continue

        compound_base = _resolve_compound_base(
            parent_info,
            children,
            node_type=node_type,
        )
        if compound_base is None:
            continue

        base_plug_cls, base_attr_cls, base_field_cls, base_module = (
            compound_base
        )
        _add_import(base_attr_cls, base_module)
        _add_import(base_plug_cls, base_module)
        _add_import(base_field_cls, base_module)

        plug_cls_name, attr_cls_name, field_cls_name = (
            _long_name_to_compound_class_names(parent_long)
        )

        # 子アトリビュート行の生成
        child_body_lines: list[str] = []
        for child_info in children:
            child_name = _get_child_attr_name(
                _attr_long_name(child_info), parent_long
            )
            child_short = child_info.short_name

            child_module: str | None = None
            child_cls_name = compound_field_classes.get(
                _attr_long_name(child_info)
            )
            if child_cls_name is None:
                child_resolved = _resolve_attr_class(child_info)
                if child_resolved is None:
                    child_body_lines.append(
                        f"    # TODO: {child_name}"
                        f" (attributeType={child_info.attribute_type}) は未対応"
                    )
                    continue
                child_cls_name, child_module = child_resolved

            if child_info.attribute_type == "enum":
                entries = _parse_enum_entries(child_info.enum_name)
                if entries:
                    enum_cls_name = _long_name_to_enum_class_name(
                        _attr_long_name(child_info)
                    )
                    enum_classes.setdefault(enum_cls_name, entries)
                    child_cls_name = f"{enum_cls_name}Field"
                    _add_import("EnumAttrOperator", "std.at.scalar.enum")
                    _add_import("EnumPlugOperator", "std.at.scalar.enum")
                    _add_import("EnumField", "std.at.scalar.enum")
                else:
                    if child_module is not None:
                        _add_import(child_cls_name, child_module)
            elif child_module is not None:
                _add_import(child_cls_name, child_module)

            safe_child_name = _safe_field_name(child_name)
            init_args = _field_init_args(
                _build_attr_init_args(child_info),
                safe_child_name,
                child_name,
                child_short,
            )
            field_declaration = safe_child_name
            if safe_child_name == "extra" or (
                safe_child_name == "value" and child_cls_name == "TypedField"
            ):
                # Keep the descriptor visible to Pyright when a compound child
                # shadows an operator property with a different return type.
                field_declaration = f"{safe_child_name}: {child_cls_name}"
            child_body_lines.append(
                f"    {field_declaration} = {child_cls_name}({init_args})"
            )
            if _should_emit_short_alias(child_short, child_name):
                safe_child_short = _safe_field_name(child_short)
                if safe_child_short != safe_child_name:
                    child_body_lines.append(
                        f"    {safe_child_short} = {safe_child_name}"
                    )
            child_body_lines.append("")

        # 末尾の空行を除去
        while child_body_lines and child_body_lines[-1] == "":
            child_body_lines.pop()

        # Plug クラスブロック
        plug_block: list[str] = _build_class_header_lines(
            plug_cls_name,
            f'{base_plug_cls}["{attr_cls_name}"]',
        )
        plug_block.append("    __slots__ = ()")
        if children:
            plug_block.append("    CHILD_ATTR_NAMES = (")
            for child_info in children:
                child_name = _get_child_attr_name(
                    _attr_long_name(child_info),
                    parent_long,
                )
                child_short = child_info.short_name or child_name
                plug_block.append(
                    f'        ("{child_name}", "{child_short}"),'
                )
            plug_block.append("    )")
        if child_body_lines:
            plug_block.append("")
            plug_block.extend(child_body_lines)
        else:
            plug_block.append("")
            plug_block.append("    pass")

        # AttrOperator クラスブロック
        attr_block: list[str] = _build_class_header_lines(
            attr_cls_name,
            f"{base_attr_cls}[{plug_cls_name}]",
        )
        attr_block.append("    __slots__ = ()")
        if child_body_lines:
            attr_block.append("")
            attr_block.extend(child_body_lines)

        # Field クラスブロック
        field_block: list[str] = _build_class_header_lines(
            field_cls_name,
            f"{base_field_cls}[{attr_cls_name}, {plug_cls_name}]",
        )
        field_block.extend(
            [
                "    __slots__ = ()",
                "",
                f"    ATTR_CLS = {attr_cls_name}",
                f"    PLUG_CLS = {plug_cls_name}",
            ]
        )
        if child_body_lines and not parent_info.multi:
            field_block.append("")
            field_block.extend(child_body_lines)

        class_blocks.append(plug_block)
        class_blocks.append(attr_block)
        class_blocks.append(field_block)

    if not class_blocks:
        return None

    # インポート行の生成 (モジュールパスでソート、同一モジュール内はクラス名でソート)
    import_lines: list[str] = []
    for mod_path in sorted(
        module_imports.keys(),
        key=lambda path: (0 if path.startswith("std.") else 1, path),
    ):
        cls_names = module_imports[mod_path]
        import_lines.extend(_build_import_lines(f"..{mod_path}", cls_names))

    # コード全体を組み立てる
    lines: list[str] = ["# coding: utf-8"]
    lines.append("")
    lines.extend(import_lines)
    lines.append("")
    lines.append("")

    for enum_cls_name, entries in enum_classes.items():
        lines.extend(_build_enum_class_lines(enum_cls_name, entries))
        lines.append("")
        lines.append("")

    for i, block in enumerate(class_blocks):
        lines.extend(block)
        if i < len(class_blocks) - 1:
            lines.append("")
            lines.append("")
    lines.append("")

    return "\n".join(lines)


# generate
def generate_node_class_code(
    node_type: str,
    attr_infos: list[AttrInfo] | None = None,
    *,
    node_kind: str = _NODE_KIND_DG,
    inherited_attr_infos: list[AttrInfo] | None = None,
) -> str:
    """Maya ノードタイプの属性情報をもとに Node Operator クラスの Python コードを生成する。

    生成されるコードは ``node_kind`` に応じた node package の
    ``_generated`` package 以下に配置することを想定した相対インポートを
    使用する。

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"addDoubleLinear"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。
        node_kind (str): ``"dg"`` / ``"dag"`` / ``"transform"`` /
            ``"shape"`` / ``"auto"`` のいずれか。
        inherited_attr_infos (list[AttrInfo] | None): 継承元ノードで定義済みの
            属性情報。指定された属性は生成対象から除外する。

    Returns:
        str: 生成された Python コード文字列
    """
    resolved_node_kind = _resolve_node_kind(node_type, node_kind)
    should_query_inherited_attrs = attr_infos is None

    if attr_infos is None:
        attr_infos = get_attribute_infos(
            node_type,
            mode_new_scene=True,
            mode_error_skip=True,
        )

    attr_infos = _omit_unreliable_default_values(node_type, attr_infos)

    if inherited_attr_infos is None:
        if should_query_inherited_attrs:
            inherited_attr_infos = _get_inherited_attr_infos(
                node_type,
                resolved_node_kind,
            )
        else:
            inherited_attr_infos = []

    inherited_long_names = _attr_long_names(inherited_attr_infos)

    attr_infos = _filter_supported_attr_infos(attr_infos)
    attr_infos = _normalize_attr_hierarchy(attr_infos)
    attr_infos = _filter_inherited_attr_infos(
        attr_infos,
        inherited_long_names,
    )

    # attr_infos が空の場合は警告を出して空のクラスコードを返す
    if not attr_infos:
        logger.warning(
            f"No attribute infos found for node type '{node_type}'. "
            "Generating empty class."
        )
        attr_infos = []

    class_name = _node_kind_class_name(node_type, resolved_node_kind)
    base_class_name = _node_kind_base_class_name(
        node_type,
        resolved_node_kind,
    )
    attr_import_prefix = _node_kind_attr_import_prefix(resolved_node_kind)
    base_long_names = (
        _node_kind_base_long_names(resolved_node_kind) | inherited_long_names
    )

    # short_name → long_name  (short_name が long_name と異なる場合のみ)
    short_to_long: dict[str, str] = {}
    for info in attr_infos:
        long_name = _attr_long_name(info)
        if info.short_name and info.short_name != long_name:
            short_to_long[info.short_name] = long_name

    # 使用する Field クラスとそのインポートパスを収集する
    # クラス名 → "define.std..." or "define.custom..."
    imports: dict[str, str] = {}

    # 生成する EnumOperator / EnumField クラス: (ベース名, エントリリスト)
    enum_classes: list[tuple[str, list[tuple[str, int | None]]]] = []

    # 生成するアトリビュート行
    attr_lines: list[str] = []

    # compound 型の子アトリビュートを親ごとにグループ化
    compound_children_map: dict[str, list[AttrInfo]] = {}
    for info in attr_infos:
        parent_name = _attr_parent_name(info)
        if parent_name is not None:
            compound_children_map.setdefault(parent_name, []).append(info)

    # compound 型で子が存在する親アトリビュート → カスタム Field クラス名
    # (node_attr/{snake_case}.py で定義されるクラスを参照する)
    custom_compound_cls: dict[str, str] = {}
    for info in attr_infos:
        if (
            _attr_parent_name(info) is None
            and compound_children_map.get(_attr_long_name(info))
            and _resolve_compound_base(
                info,
                compound_children_map.get(_attr_long_name(info), []),
                node_type=node_type,
            )
        ):
            _, _, field_cls_name = _long_name_to_compound_class_names(
                _attr_long_name(info)
            )
            custom_compound_cls[_attr_long_name(info)] = field_cls_name

    # node_attr モジュールからインポートするクラス名のセット
    node_attr_imports: set[str] = set()

    for attr_info in attr_infos:
        long_name = _attr_long_name(attr_info)

        # 基底クラスで定義済みのアトリビュートはスキップ
        if long_name in base_long_names:
            continue

        # 子アトリビュート (compound の子) はスキップ
        # compound の内部定義は node_attr/ で別途行う
        if _attr_parent_name(attr_info) is not None:
            continue

        # listAttr が short_name も返してきた場合はスキップ
        # (long_name が別のアトリビュートの short_name と一致するケース)
        if long_name in short_to_long:
            continue

        # compound 型で子が存在する場合はカスタムクラスを使用する
        if long_name in custom_compound_cls:
            attr_info = _replace_compound_default_with_child_defaults(
                attr_info,
                compound_children_map.get(long_name, []),
            )
            args = _build_attr_init_args(attr_info)
            field_cls_name = custom_compound_cls[long_name]
            node_attr_imports.add(field_cls_name)
            safe_long_name = _safe_field_name(long_name)
            short_name = attr_info.short_name
            init_args = _field_init_args(
                args,
                safe_long_name,
                long_name,
                short_name,
            )
            attr_lines.append(
                f"    {safe_long_name} = {field_cls_name}({init_args})"
            )
            if _should_emit_short_alias(short_name, long_name):
                safe_short_name = _safe_field_name(short_name)
                if safe_short_name != safe_long_name:
                    attr_lines.append(
                        f"    {safe_short_name} = {safe_long_name}"
                    )

            # non-multi の compound 親属性は node.<child> の直アクセスを追加する
            if not attr_info.multi:
                for child_info in compound_children_map.get(long_name, []):
                    if _resolve_attr_class(child_info) is None:
                        continue
                    child_name = _get_child_attr_name(
                        _attr_long_name(child_info), long_name
                    )
                    safe_child_name = _safe_field_name(child_name)
                    attr_lines.append(
                        f"    {safe_child_name} = "
                        f"{safe_long_name}.{safe_child_name}"
                    )
                    child_short = child_info.short_name
                    if _should_emit_short_alias(child_short, child_name):
                        safe_child_short = _safe_field_name(child_short)
                        if safe_child_short != safe_child_name:
                            attr_lines.append(
                                f"    {safe_child_short} = {safe_child_name}"
                            )
            attr_lines.append("")
            continue

        # コンストラクタ引数を組み立てる
        args = _build_attr_init_args(attr_info)

        # Field クラスを解決する
        resolved = _resolve_attr_class(attr_info)
        if resolved is None:
            attr_lines.append(
                f"    # TODO: {long_name} "
                f"(attributeType={attr_info.attribute_type}, "
                f"dataType={attr_info.data_type}) "
                "は未対応のため手動で追加してください"
            )
            attr_lines.append("")
            continue

        field_cls_name, module_path = resolved
        imports[field_cls_name] = module_path

        if attr_info.attribute_type == "enum":
            entries = _parse_enum_entries(attr_info.enum_name)
            if entries:
                enum_cls_name = _long_name_to_enum_class_name(long_name)
                enum_classes.append((enum_cls_name, entries))
                field_cls_name = f"{enum_cls_name}Field"
                imports.pop("EnumField", None)

        safe_long_name = _safe_field_name(long_name)
        short_name = attr_info.short_name
        init_args = _field_init_args(
            args,
            safe_long_name,
            long_name,
            short_name,
        )
        attr_lines.append(
            f"    {safe_long_name} = {field_cls_name}({init_args})"
        )

        # short_name のエイリアス行
        if _should_emit_short_alias(short_name, long_name):
            safe_short_name = _safe_field_name(short_name)
            if safe_short_name != safe_long_name:
                attr_lines.append(f"    {safe_short_name} = {safe_long_name}")
        attr_lines.append("")

    # インポート行 (モジュールパスでソートして並びを安定させる)
    import_lines: list[str] = [
        _node_kind_base_import_line(node_type, resolved_node_kind)
    ]
    if node_attr_imports:
        snake_type = _camel_to_snake(node_type)
        import_lines.extend(
            _build_import_lines(
                f"{attr_import_prefix}.define.node_attr.{snake_type}",
                sorted(node_attr_imports),
            )
        )
    if enum_classes:
        import_lines.extend(
            _build_import_lines(
                f"{attr_import_prefix}.define.std.at.scalar.enum",
                ["EnumAttrOperator", "EnumPlugOperator", "EnumField"],
            )
        )
    for cls_name, mod_path in sorted(imports.items(), key=lambda kv: kv[1]):
        import_lines.extend(
            _build_import_lines(
                f"{attr_import_prefix}.{_node_module_attr_path(mod_path)}",
                [cls_name],
            )
        )

    # コード全体を組み立てる
    lines: list[str] = []
    lines.append("# coding: utf-8")
    lines.extend(import_lines)
    lines.append("")
    lines.append("")
    for enum_cls_name, entries in enum_classes:
        lines.extend(_build_enum_class_lines(enum_cls_name, entries))
        lines.append("")
        lines.append("")
    lines.append(f"class {class_name}({base_class_name}):")
    lines.append("    __slots__ = ()")
    lines.append("")
    lines.append(f'    NODE_TYPE = "{node_type}"')
    if attr_lines:
        # 末尾の空行を除去してからクラス本体に追加する
        while attr_lines and attr_lines[-1] == "":
            attr_lines.pop()
        lines.append("")
        lines.extend(attr_lines)
    lines.append("")

    return "\n".join(lines)


def generate_node_class_file(
    node_type: str,
    src_dir: str | pathlib.Path,
    attr_infos: list[AttrInfo] | None = None,
    *,
    include_skipped: bool = False,
    node_kind: str = _NODE_KIND_DG,
    inherited_attr_infos: list[AttrInfo] | None = None,
) -> None:
    """Maya ノードタイプの属性情報をもとに Node Operator クラスの Python ファイルを生成する。

    ``src_dir`` に ``bd_util`` パッケージの親ディレクトリを指定するだけで、出力先パスを自動で構築する。

    compound 型アトリビュート
    (compound, double2/3/4, float2/3, lightData, long2/3, short2/3)
    が存在する場合は、node_attr ファイルも同時に生成する。

    生成 class の出力先::

        {src_dir}/bd_util/maya/node/operator/node/dg/_generated/{snake_case_node_type}.py
        {src_dir}/bd_util/maya/node/operator/node/dag/_generated/{snake_case_node_type}.py
        {src_dir}/bd_util/maya/node/operator/node/dag/transform/_generated/{snake_case_node_type}.py
        {src_dir}/bd_util/maya/node/operator/node/dag/shape/_generated/{snake_case_node_type}.py

    公開 wrapper は従来の node module path に、存在しない場合だけ作成する。
    既存 wrapper は手書きコードを保護するため上書きしない。

    compound attribute がある場合は、従来どおり次へ出力する::

        {src_dir}/bd_util/maya/node/operator/attr/define/node_attr/{snake_case_node_type}.py

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"multiplyDivide"``)
        src_dir (str | pathlib.Path): ``bd_util`` パッケージの親ディレクトリへのパス
            (例: ``r"C:/path/bakedanuki/bakedanuki-util/python"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。
        include_skipped (bool): ``True`` の場合、通常は除外される特殊ノードも
            調査用に生成する。
        node_kind (str): ``"dg"`` / ``"dag"`` / ``"transform"`` /
            ``"shape"`` / ``"auto"`` のいずれか。
        inherited_attr_infos (list[AttrInfo] | None): 継承元ノードで定義済みの
            属性情報。指定された属性は生成対象から除外する。
    """
    resolved_node_kind = _resolve_node_kind(node_type, node_kind)

    skip_reason = None
    if resolved_node_kind == _NODE_KIND_DG:
        skip_reason = _SKIPPED_DG_NODE_TYPES.get(node_type)
    elif resolved_node_kind in _DAG_NODE_KINDS:
        skip_reason = _get_skipped_dag_node_type_reason(node_type)
    if skip_reason and not include_skipped:
        logger.warning(f"Skipping node type '{node_type}': {skip_reason}")
        return

    if attr_infos is None:
        attr_infos = get_attribute_infos(
            node_type,
            mode_new_scene=True,
            mode_error_skip=True,
        )

    if inherited_attr_infos is None:
        inherited_attr_infos = _get_inherited_attr_infos(
            node_type,
            resolved_node_kind,
        )

    attr_infos = _filter_inherited_attr_infos(
        attr_infos,
        _attr_long_names(inherited_attr_infos),
    )

    generated_package_path = pathlib.Path(src_dir).joinpath(
        *_generated_package_parts(resolved_node_kind)
    )
    output_path = generated_package_path.joinpath(
        _node_type_to_file_name(node_type)
    )
    public_output_path = (
        pathlib.Path(src_dir)
        .joinpath(*_node_kind_output_rel_parts(resolved_node_kind))
        .joinpath(
            _node_kind_public_output_file_name(
                node_type,
                resolved_node_kind,
            )
        )
    )
    _validate_existing_node_output(output_path, node_type)
    _validate_existing_node_output(public_output_path, node_type)

    # node_attr ファイルを生成 (compound アトリビュートがある場合のみ)
    node_attr_code = generate_node_attr_code(node_type, attr_infos=attr_infos)
    if node_attr_code:
        node_attr_path = (
            pathlib.Path(src_dir)
            .joinpath(*_NODE_ATTR_OUTPUT_REL_PARTS)
            .joinpath(_node_type_to_file_name(node_type))
        )
        node_attr_path.parent.mkdir(parents=True, exist_ok=True)
        node_attr_path.write_text(node_attr_code, encoding="utf-8")

    # メインのノードクラスファイルを生成
    code = generate_node_class_code(
        node_type,
        attr_infos=attr_infos,
        node_kind=resolved_node_kind,
        inherited_attr_infos=[],
    )
    if not code:
        logger.warning(
            f"Generated code for node type '{node_type}' is empty. "
            "Skipping file generation."
        )
        return
    generated_package_path.mkdir(parents=True, exist_ok=True)
    generated_package_init_path = generated_package_path / "__init__.py"
    if not generated_package_init_path.exists():
        generated_package_init_path.write_text(
            "# coding: utf-8\n",
            encoding="utf-8",
        )

    output_path.write_text(code, encoding="utf-8")

    if not public_output_path.exists():
        public_output_path.parent.mkdir(parents=True, exist_ok=True)
        public_output_path.write_text(
            _generate_public_node_class_code(
                node_type,
                resolved_node_kind,
            ),
            encoding="utf-8",
        )


#   node_type ごとのファイル生成
def generate_specific_node_class_file_core(
    src_dir: str | pathlib.Path,
    func_get_node_types: Callable[[], list[str]],
    *,
    include_skipped: bool = False,
    node_kind: str = _NODE_KIND_DG,
) -> None:
    node_types = tuple(func_get_node_types())
    _validate_node_type_name_collisions(node_types)

    for node_type in node_types:
        generate_node_class_file(
            node_type,
            src_dir,
            include_skipped=include_skipped,
            node_kind=node_kind,
        )


#       dg_node
def generate_dg_node_class_files(
    src_dir: str | pathlib.Path,
    *,
    include_skipped: bool = False,
) -> None:
    generate_specific_node_class_file_core(
        src_dir=src_dir,
        func_get_node_types=get_dg_node_types,
        include_skipped=include_skipped,
        node_kind=_NODE_KIND_DG,
    )


#       dag_node
def generate_dag_node_class_files(
    src_dir: str | pathlib.Path,
    *,
    include_skipped: bool = False,
) -> None:
    generate_specific_node_class_file_core(
        src_dir=src_dir,
        func_get_node_types=get_dag_node_types,
        include_skipped=include_skipped,
        node_kind=_NODE_KIND_AUTO,
    )


#           transform
def generate_transform_node_class_files(
    src_dir: str | pathlib.Path,
    *,
    include_skipped: bool = False,
) -> None:
    generate_specific_node_class_file_core(
        src_dir=src_dir,
        func_get_node_types=get_transform_types,
        include_skipped=include_skipped,
        node_kind=_NODE_KIND_TRANSFORM,
    )


#           shape
def generate_shape_node_class_files(
    src_dir: str | pathlib.Path,
    *,
    include_skipped: bool = False,
) -> None:
    generate_specific_node_class_file_core(
        src_dir=src_dir,
        func_get_node_types=get_shape_types,
        include_skipped=include_skipped,
        node_kind=_NODE_KIND_SHAPE,
    )
