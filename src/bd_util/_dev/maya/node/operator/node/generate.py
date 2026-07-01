# coding: utf-8
"""
Maya ノードの attributeQuery 情報をもとに、Node Operator クラスの
Python ファイルを生成するモジュール。

生成されるファイルは ``bd_util.maya.node.operator.node.dg`` 以下に配置し、
既存の ``AddDoubleLinear`` / ``PlusMinusAverage`` / ``WtAddMatrix`` と同じ
スタイルで利用できることを想定している。

使用例::

    # Maya Python Script Editor で実行
    from bd_util.maya.node.operator.node.generate import generate_node_class_file

    generate_node_class_file(
        node_type="multiplyDivide",
        src_dir=r"C:/path/bakedanuki-util/src",
    )
    # → C:/path/bakedanuki-util/src/bd_util/maya/node/operator/node/dg/multiply_divide.py
"""

from __future__ import annotations

import keyword
import pathlib
import re

# self
from ...... import logger as u_logger
from ......maya.attr.query import AttrInfo, get_attribute_infos
from ......maya.node.all_types import (
    get_dg_node_types,
)

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

# ---------------------------------------------------------------------------
# attribute_type → (Field クラス名, "define.at/dt モジュール名")
# ---------------------------------------------------------------------------

# attributeType ベースのマッピング (attr/define/std/at or attr/define/custom/at)
_AT_TYPE_MAP: dict[str, tuple[str, str]] = {
    "addr": ("AddrField", "define.std.at.addr"),
    "bool": ("BoolField", "define.std.at.numeric_scalar.bool"),
    "byte": ("ByteField", "define.std.at.numeric_scalar_range.byte"),
    "char": ("CharField", "define.std.at.numeric_scalar_range.char"),
    "compound": ("CompoundField", "define.std.at.compound"),
    "double": ("DoubleField", "define.std.at.numeric_scalar_range.double"),
    "double2": (
        "Double2Field",
        "define.custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2",
    ),
    "double3": (
        "Double3Field",
        "define.custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3",
    ),
    "double4": (
        "Double4Field",
        "define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4",
    ),
    "doubleAngle": (
        "DoubleAngleField",
        "define.std.at.unit_scalar_range.double_angle",
    ),
    "doubleLinear": (
        "DoubleLinearField",
        "define.std.at.unit_scalar_range.double_linear",
    ),
    "enum": ("EnumField", "define.std.at.enum"),
    "float": ("FloatField", "define.std.at.numeric_scalar_range.float"),
    "float2": (
        "Float2Field",
        "define.custom.at.scalar_compound.numeric_compound.float_compound.float2_compound.float2",
    ),
    "float3": (
        "Float3Field",
        "define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3",
    ),
    "floatAngle": (
        "FloatAngleField",
        "define.std.at.unit_scalar_range.float_angle",
    ),
    "floatLinear": (
        "FloatLinearField",
        "define.std.at.unit_scalar_range.float_linear",
    ),
    "fltMatrix": ("FltMatrixField", "define.std.at.flt_matrix"),
    "generic": ("GenericField", "define.std.at.generic"),
    "lightData": ("LightDataField", "define.std.at.light_data"),
    "long": ("LongField", "define.std.at.numeric_scalar_range.long"),
    "long2": (
        "Long2Field",
        "define.custom.at.scalar_compound.numeric_compound.long_compound.long2_compound.long2",
    ),
    "long3": (
        "Long3Field",
        "define.custom.at.scalar_compound.numeric_compound.long_compound.long3_compound.long3",
    ),
    "long long int": (
        "LongLongIntField",
        "define.std.at.numeric_scalar_range.long_long_int",
    ),
    "long_long_int": (
        "LongLongIntField",
        "define.std.at.numeric_scalar_range.long_long_int",
    ),
    "matrix": ("MatrixField", "define.std.at.matrix"),
    "message": ("MessageField", "define.std.at.message"),
    "reflectance": ("ReflectanceField", "define.std.at.reflectance"),
    "short": ("ShortField", "define.std.at.numeric_scalar_range.short"),
    "short2": (
        "Short2Field",
        "define.custom.at.scalar_compound.numeric_compound.short_compound.short2_compound.short2",
    ),
    "short3": (
        "Short3Field",
        "define.custom.at.scalar_compound.numeric_compound.short_compound.short3_compound.short3",
    ),
    "spectrum": ("SpectrumField", "define.std.at.spectrum"),
    "time": ("TimeField", "define.std.at.unit_scalar.time"),
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

# generate_node_class_file が src_dir から補完するパス部品
_OUTPUT_REL_PARTS: tuple[str, ...] = (
    "bd_util",
    "maya",
    "node",
    "operator",
    "node",
    "dg",
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
        "custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base",
    ),
    (
        "double3",
        "double",
        3,
    ): (
        "Double3CompoundBasePlugOperator",
        "Double3CompoundBaseAttrOperator",
        "Double3CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base",
    ),
    (
        "double4",
        "double",
        4,
    ): (
        "Double4CompoundBasePlugOperator",
        "Double4CompoundBaseAttrOperator",
        "Double4CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.double_compound.double4_compound._base",
    ),
    (
        "float2",
        "float",
        2,
    ): (
        "Float2CompoundBasePlugOperator",
        "Float2CompoundBaseAttrOperator",
        "Float2CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base",
    ),
    (
        "float3",
        "float",
        3,
    ): (
        "Float3CompoundBasePlugOperator",
        "Float3CompoundBaseAttrOperator",
        "Float3CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base",
    ),
    (
        "long2",
        "long",
        2,
    ): (
        "Long2CompoundBasePlugOperator",
        "Long2CompoundBaseAttrOperator",
        "Long2CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.long_compound.long2_compound._base",
    ),
    (
        "long3",
        "long",
        3,
    ): (
        "Long3CompoundBasePlugOperator",
        "Long3CompoundBaseAttrOperator",
        "Long3CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.long_compound.long3_compound._base",
    ),
    (
        "short2",
        "short",
        2,
    ): (
        "Short2CompoundBasePlugOperator",
        "Short2CompoundBaseAttrOperator",
        "Short2CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.short_compound.short2_compound._base",
    ),
    (
        "short3",
        "short",
        3,
    ): (
        "Short3CompoundBasePlugOperator",
        "Short3CompoundBaseAttrOperator",
        "Short3CompoundBaseField",
        "custom.at.scalar_compound.numeric_compound.short_compound.short3_compound._base",
    ),
    (
        "double2",
        "doubleAngle",
        2,
    ): (
        "DoubleAngle2CompoundBasePlugOperator",
        "DoubleAngle2CompoundBaseAttrOperator",
        "DoubleAngle2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.double2._base",
    ),
    (
        "double3",
        "doubleAngle",
        3,
    ): (
        "DoubleAngle3CompoundBasePlugOperator",
        "DoubleAngle3CompoundBaseAttrOperator",
        "DoubleAngle3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.double3._base",
    ),
    (
        "double2",
        "doubleLinear",
        2,
    ): (
        "DoubleLinear2CompoundBasePlugOperator",
        "DoubleLinear2CompoundBaseAttrOperator",
        "DoubleLinear2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.double2._base",
    ),
    (
        "double3",
        "doubleLinear",
        3,
    ): (
        "DoubleLinear3CompoundBasePlugOperator",
        "DoubleLinear3CompoundBaseAttrOperator",
        "DoubleLinear3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.double3._base",
    ),
    (
        "float2",
        "floatAngle",
        2,
    ): (
        "FloatAngle2CompoundBasePlugOperator",
        "FloatAngle2CompoundBaseAttrOperator",
        "FloatAngle2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.float2._base",
    ),
    (
        "float3",
        "floatAngle",
        3,
    ): (
        "FloatAngle3CompoundBasePlugOperator",
        "FloatAngle3CompoundBaseAttrOperator",
        "FloatAngle3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.float3._base",
    ),
    (
        "float2",
        "doubleAngle",
        2,
    ): (
        "FloatAngle2CompoundBasePlugOperator",
        "FloatAngle2CompoundBaseAttrOperator",
        "FloatAngle2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.float2._base",
    ),
    (
        "float3",
        "doubleAngle",
        3,
    ): (
        "FloatAngle3CompoundBasePlugOperator",
        "FloatAngle3CompoundBaseAttrOperator",
        "FloatAngle3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.angle_compound.float3._base",
    ),
    (
        "float2",
        "floatLinear",
        2,
    ): (
        "FloatLinear2CompoundBasePlugOperator",
        "FloatLinear2CompoundBaseAttrOperator",
        "FloatLinear2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.float2._base",
    ),
    (
        "float3",
        "floatLinear",
        3,
    ): (
        "FloatLinear3CompoundBasePlugOperator",
        "FloatLinear3CompoundBaseAttrOperator",
        "FloatLinear3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.float3._base",
    ),
    (
        "float2",
        "doubleLinear",
        2,
    ): (
        "FloatLinear2CompoundBasePlugOperator",
        "FloatLinear2CompoundBaseAttrOperator",
        "FloatLinear2CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.float2._base",
    ),
    (
        "float3",
        "doubleLinear",
        3,
    ): (
        "FloatLinear3CompoundBasePlugOperator",
        "FloatLinear3CompoundBaseAttrOperator",
        "FloatLinear3CompoundBaseField",
        "custom.at.scalar_compound.unit_compound.linear_compound.float3._base",
    ),
}

_QUAT_COMPOUND_AT_BASE: tuple[str, str, str, str] = (
    "QuatCompoundBasePlugOperator",
    "QuatCompoundBaseAttrOperator",
    "QuatCompoundBaseField",
    "custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound._base",
)


# ---------------------------------------------------------------------------
# 内部ユーティリティ
# ---------------------------------------------------------------------------


def _node_type_to_class_name(node_type: str) -> str:
    """ノードタイプ名 (camelCase) をクラス名 (PascalCase) へ変換する。

    例: ``addDoubleLinear`` → ``AddDoubleLinear``
    """
    return node_type[0].upper() + node_type[1:]


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


def _resolve_attr_class(attr_info: AttrInfo) -> tuple[str, str] | None:
    """AttrInfo から ``(Field クラス名, モジュールパス)`` を返す。

    ``attribute_type == "typed"`` かつ ``data_type`` が設定されている場合は
    ``_DT_TYPE_MAP`` で解決し、それ以外は ``_AT_TYPE_MAP`` で解決する。
    解決できない場合は ``None`` を返す。

    Returns:
        tuple[str, str] | None: (クラス名, モジュール相対パス) または None
    """
    if attr_info.attribute_type == "typed" and attr_info.data_type:
        result = _DT_TYPE_MAP.get(attr_info.data_type)
        if result:
            return result

    return _AT_TYPE_MAP.get(attr_info.attribute_type)


def _node_attr_module_path(module_path: str) -> str:
    """node_attr 生成ファイルから import できるモジュールパスへ変換する。"""
    prefix = "define."
    if module_path.startswith(prefix):
        return module_path[len(prefix) :]
    return module_path


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
) -> bool:
    """Return True for Maya quat attrs reported as compound + four double children."""
    return (
        parent_info.attribute_type in {"compound", "double4"}
        and "quat" in parent_info.long_name.lower()
        and len(children) == 4
        and _uniform_child_attr_type(children) == "double"
    )


def _resolve_compound_base(
    parent_info: AttrInfo,
    children: list[AttrInfo],
) -> tuple[str, str, str, str] | None:
    """compound 親と子情報から現行の基底クラス群を返す。"""
    if _is_quat_like_compound(parent_info, children):
        return _QUAT_COMPOUND_AT_BASE

    result = _GENERIC_COMPOUND_AT_BASE.get(parent_info.attribute_type)
    if result is not None:
        return result

    first_child_type = _uniform_child_attr_type(children)
    if first_child_type is None:
        return None

    key = (parent_info.attribute_type, first_child_type, len(children))
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
        raw = str(enum_name_raw[0]) if enum_name_raw else ""
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


def _build_attr_init_args(attr_info: AttrInfo) -> str:
    """Field コンストラクタ引数文字列を生成する。

    例: ``multi=True``

    .. note::
        現状は ``multi=True`` のみを生成する。
    """
    args: list[str] = []

    if attr_info.multi:
        args.append("multi=True")

    return ", ".join(args)


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
    return f"{pascal}PlugOperator", f"{pascal}AttrOperator", f"{pascal}Field"


def _long_name_to_enum_class_name(long_name: str) -> str:
    """アトリビュートの long_name を PascalCase の Enum クラス名へ変換する。

    例: ``"operation"`` → ``"OperationEnum"``、
        ``"nodeState"`` → ``"NodeStateEnum"``
    """
    return long_name[0].upper() + long_name[1:] + "Enum"


def _enum_entries_to_name_values(
    entries: list[tuple[str, int | None]],
) -> list[tuple[str, str, int]]:
    """パース済み enum entry を ``(member, label, value)`` へ変換する。"""
    result: list[tuple[str, str, int]] = []
    next_value = 0
    for label, explicit_value in entries:
        value = next_value if explicit_value is None else explicit_value
        result.append((_label_to_enum_member_name(label), label, value))
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

    lines: list[str] = [f"class {plug_cls_name}(EnumPlugOperator):"]
    lines.append("    __slots__ = ()")
    lines.append("")
    for member_name, _label, value in name_values:
        lines.append(f"    {member_name} = {value}")
    lines.append("")
    lines.append("")

    lines.append(f"class {attr_cls_name}(EnumAttrOperator):")
    lines.append("    __slots__ = ()")
    lines.append("")
    for member_name, _label, value in name_values:
        lines.append(f"    {member_name} = {value}")
    lines.append("")
    lines.append("    NAME_MAP = {")
    for member_name, label, _value in name_values:
        lines.append(f'        {member_name}: "{label}",')
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

    attr_infos = _filter_supported_attr_infos(attr_infos)

    # 子アトリビュートを親ごとにグループ化
    compound_children_map: dict[str, list[AttrInfo]] = {}
    for info in attr_infos:
        if info.parent is not None:
            parent_name = info.parent[0]
            compound_children_map.setdefault(parent_name, []).append(info)

    # compound タイプの親アトリビュートのみ対象（子が存在し、基底解決できるものに限る）
    compound_parents: list[AttrInfo] = [
        info
        for info in attr_infos
        if (
            info.parent is None
            and compound_children_map.get(info.long_name)
            and _resolve_compound_base(
                info,
                compound_children_map.get(info.long_name, []),
            )
        )
    ]

    if not compound_parents:
        return None

    # インポート収集: module_path → list[class_name]
    # 同一モジュール内は手書きコードに寄せるため、追加順を保持する。
    module_imports: dict[str, list[str]] = {}

    def _add_import(cls_name: str, mod_path: str) -> None:
        cls_names = module_imports.setdefault(mod_path, [])
        if cls_name not in cls_names:
            cls_names.append(cls_name)

    # 各 compound アトリビュートのクラスブロックを生成
    class_blocks: list[list[str]] = []

    for parent_info in compound_parents:
        parent_long = parent_info.long_name
        children = compound_children_map.get(parent_long, [])
        if not children:
            continue

        compound_base = _resolve_compound_base(parent_info, children)
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
                child_info.long_name, parent_long
            )
            child_short = child_info.short_name

            child_resolved = _resolve_attr_class(child_info)
            if child_resolved is None:
                child_body_lines.append(
                    f"    # TODO: {child_name}"
                    f" (attributeType={child_info.attribute_type}) は未対応"
                )
                continue

            child_cls_name, child_module = child_resolved
            _add_import(child_cls_name, _node_attr_module_path(child_module))

            safe_child_name = _safe_attr_name(child_name)
            child_body_lines.append(
                f"    {safe_child_name} = {child_cls_name}()"
            )
            if _should_emit_short_alias(child_short, child_name):
                safe_child_short = _safe_attr_name(child_short)
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
                    child_info.long_name,
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
) -> str:
    """Maya ノードタイプの属性情報をもとに Node Operator クラスの Python コードを生成する。

    生成されるコードは ``bd_util.maya.node.operator.node.dg`` 以下に配置する
    ことを想定した相対インポートを使用する。

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"addDoubleLinear"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。

    Returns:
        str: 生成された Python コード文字列
    """
    if attr_infos is None:
        attr_infos = get_attribute_infos(
            node_type,
            mode_new_scene=True,
            mode_error_skip=True,
        )

    attr_infos = _filter_supported_attr_infos(attr_infos)

    # attr_infos が空の場合は警告を出して空のクラスコードを返す
    if not attr_infos:
        logger.warning(
            f"No attribute infos found for node type '{node_type}'. Generating empty class."
        )
        attr_infos = []

    class_name = _node_type_to_class_name(node_type)

    # short_name → long_name  (short_name が long_name と異なる場合のみ)
    short_to_long: dict[str, str] = {}
    for info in attr_infos:
        if info.short_name and info.short_name != info.long_name:
            short_to_long[info.short_name] = info.long_name

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
        if info.parent is not None:
            parent_name = info.parent[0]
            compound_children_map.setdefault(parent_name, []).append(info)

    # compound 型で子が存在する親アトリビュート → カスタム Field クラス名
    # (node_attr/{snake_case}.py で定義されるクラスを参照する)
    custom_compound_cls: dict[str, str] = {}
    for info in attr_infos:
        if (
            info.parent is None
            and compound_children_map.get(info.long_name)
            and _resolve_compound_base(
                info,
                compound_children_map.get(info.long_name, []),
            )
        ):
            _, _, field_cls_name = _long_name_to_compound_class_names(
                info.long_name
            )
            custom_compound_cls[info.long_name] = field_cls_name

    # node_attr モジュールからインポートするクラス名のセット
    node_attr_imports: set[str] = set()

    for attr_info in attr_infos:
        long_name = attr_info.long_name

        # DG 基底クラスで定義済みのアトリビュートはスキップ
        if long_name in _DG_BASE_LONG_NAMES:
            continue

        # 子アトリビュート (compound の子) はスキップ
        # compound の内部定義は node_attr/ で別途行う
        if attr_info.parent is not None:
            continue

        # listAttr が short_name も返してきた場合はスキップ
        # (long_name が別のアトリビュートの short_name と一致するケース)
        if long_name in short_to_long:
            continue

        # コンストラクタ引数を組み立てる
        args: list[str] = []
        if attr_info.multi:
            args.append("multi=True")

        # compound 型で子が存在する場合はカスタムクラスを使用する
        if long_name in custom_compound_cls:
            field_cls_name = custom_compound_cls[long_name]
            node_attr_imports.add(field_cls_name)
            init_args = ", ".join(args)
            safe_long_name = _safe_attr_name(long_name)
            attr_lines.append(
                f"    {safe_long_name} = {field_cls_name}({init_args})"
            )
            short_name = attr_info.short_name
            if _should_emit_short_alias(short_name, long_name):
                safe_short_name = _safe_attr_name(short_name)
                attr_lines.append(f"    {safe_short_name} = {safe_long_name}")

            # non-multi の compound 親属性は node.<child> の直アクセスを追加する
            if not attr_info.multi:
                for child_info in compound_children_map.get(long_name, []):
                    if _resolve_attr_class(child_info) is None:
                        continue
                    child_name = _get_child_attr_name(
                        child_info.long_name, long_name
                    )
                    safe_child_name = _safe_attr_name(child_name)
                    attr_lines.append(
                        f"    {safe_child_name} = {safe_long_name}.{safe_child_name}"
                    )
                    child_short = child_info.short_name
                    if _should_emit_short_alias(child_short, child_name):
                        safe_child_short = _safe_attr_name(child_short)
                        attr_lines.append(
                            f"    {safe_child_short} = {safe_child_name}"
                        )
            attr_lines.append("")
            continue

        # Field クラスを解決する
        resolved = _resolve_attr_class(attr_info)
        if resolved is None:
            attr_lines.append(
                f"    # TODO: {long_name} (attributeType={attr_info.attribute_type}, dataType={attr_info.data_type}) は未対応のため手動で追加してください"
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

        init_args = ", ".join(args)
        safe_long_name = _safe_attr_name(long_name)
        attr_lines.append(
            f"    {safe_long_name} = {field_cls_name}({init_args})"
        )

        # short_name のエイリアス行
        short_name = attr_info.short_name
        if _should_emit_short_alias(short_name, long_name):
            safe_short_name = _safe_attr_name(short_name)
            attr_lines.append(f"    {safe_short_name} = {safe_long_name}")
        attr_lines.append("")

    # インポート行 (モジュールパスでソートして並びを安定させる)
    import_lines: list[str] = ["from ._core import DG"]
    if node_attr_imports:
        snake_type = _camel_to_snake(node_type)
        import_lines.extend(
            _build_import_lines(
                f"...attr.define.node_attr.{snake_type}",
                sorted(node_attr_imports),
            )
        )
    if enum_classes:
        import_lines.extend(
            _build_import_lines(
                "...attr.define.std.at.enum",
                ["EnumAttrOperator", "EnumPlugOperator", "EnumField"],
            )
        )
    for cls_name, mod_path in sorted(imports.items(), key=lambda kv: kv[1]):
        import_lines.extend(
            _build_import_lines(f"...attr.{mod_path}", [cls_name])
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
    lines.append(f"class {class_name}(DG):")
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
) -> None:
    """Maya ノードタイプの属性情報をもとに Node Operator クラスの Python ファイルを生成する。

    ``src_dir`` に src ディレクトリを指定するだけで、出力先パスを自動で構築する。

    compound 型アトリビュート (compound, double2/3/4, float2/3, lightData, long2/3, short2/3) が存在する場合は、
    node_attr ファイルも同時に生成する。

    出力先::

        {src_dir}/bd_util/maya/node/operator/node/dg/{snake_case_node_type}.py
        {src_dir}/bd_util/maya/node/operator/attr/node_attr/{snake_case_node_type}.py  (compound アトリビュートがある場合のみ)

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"multiplyDivide"``)
        src_dir (str | pathlib.Path): リポジトリの src ディレクトリへのパス
            (例: ``r"C:/path/bakedanuki-util/src"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。
    """
    if attr_infos is None:
        attr_infos = get_attribute_infos(
            node_type,
            mode_new_scene=True,
            mode_error_skip=True,
        )

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
    code = generate_node_class_code(node_type, attr_infos=attr_infos)
    if not code:
        logger.warning(
            f"Generated code for node type '{node_type}' is empty. Skipping file generation."
        )
        return
    output_path = (
        pathlib.Path(src_dir)
        .joinpath(*_OUTPUT_REL_PARTS)
        .joinpath(_node_type_to_file_name(node_type))
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(code, encoding="utf-8")


#   node_type ごとのファイル生成
def generate_specific_node_class_file_core(
    src_dir: str | pathlib.Path,
    func_get_node_types: callable,
) -> None:
    for node_type in func_get_node_types():
        generate_node_class_file(node_type, src_dir)


#       dg_node
def generate_dg_node_class_files(src_dir: str | pathlib.Path) -> None:
    generate_specific_node_class_file_core(
        src_dir=src_dir,
        func_get_node_types=get_dg_node_types,
    )
