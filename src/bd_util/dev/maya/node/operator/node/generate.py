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
# attribute_type → (クラス名, "at.モジュール名" or "dt.モジュール名")
# ---------------------------------------------------------------------------

# attributeType ベースのマッピング (at/ ディレクトリ)
_AT_TYPE_MAP: dict[str, tuple[str, str]] = {
    "bool": ("BoolAttr", "at.bool"),
    "byte": ("ByteAttr", "at.byte"),
    "char": ("CharAttr", "at.char"),
    "compound": ("CompoundAttr", "at.compound"),
    "double": ("DoubleAttr", "at.double"),
    "double2": ("Double2Attr", "at.double2"),
    "double3": ("Double3Attr", "at.double3"),
    "doubleAngle": ("DoubleAngleAttr", "at.double_angle"),
    "doubleLinear": ("DoubleLinearAttr", "at.double_linear"),
    "enum": ("EnumAttr", "at.enum"),
    "float": ("FloatAttr", "at.float"),
    "float2": ("Float2Attr", "at.float2"),
    "float3": ("Float3Attr", "at.float3"),
    "fltMatrix": ("FltMatrixAttr", "at.flt_matrix"),
    "long": ("LongAttr", "at.long"),
    "long2": ("Long2Attr", "at.long2"),
    "long3": ("Long3Attr", "at.long3"),
    "matrix": ("MatrixAttr", "at.matrix"),
    "message": ("MessageAttr", "at.message"),
    "reflectance": ("ReflectanceAttr", "at.reflectance"),
    "short": ("ShortAttr", "at.short"),
    "short2": ("Short2Attr", "at.short2"),
    "short3": ("Short3Attr", "at.short3"),
    "spectrum": ("SpectrumAttr", "at.spectrum"),
    "time": ("TimeAttr", "at.time"),
    "typed": ("TypedAttr", "at.typed"),
}

# dataType ベースのマッピング (dt/ ディレクトリ)
# attribute_type == "typed" のときに data_type で参照する
_DT_TYPE_MAP: dict[str, tuple[str, str]] = {
    "double2": ("DataDouble2Attr", "dt.double2"),
    "double3": ("DataDouble3Attr", "dt.double3"),
    "doubleArray": ("DataDoubleArrayAttr", "dt.double_array"),
    "float2": ("DataFloat2Attr", "dt.float2"),
    "float3": ("DataFloat3Attr", "dt.float3"),
    "floatArray": ("DataFloatArrayAttr", "dt.float_array"),
    "int32Array": ("DataInt32ArrayAttr", "dt.int32_array"),
    "lattice": ("DataLatticeAttr", "dt.lattice"),
    "long2": ("DataLong2Attr", "dt.long2"),
    "long3": ("DataLong3Attr", "dt.long3"),
    "matrix": ("DataMatrixAttr", "dt.matrix"),
    "mesh": ("DataMeshAttr", "dt.mesh"),
    "nurbsCurve": ("DataNurbsCurveAttr", "dt.nurbs_curve"),
    "nurbsSurface": ("DataNurbsSurfaceAttr", "dt.nurbs_surface"),
    "pointArray": ("DataPointArrayAttr", "dt.point_array"),
    "reflectanceRGB": ("DataReflectanceRGBAttr", "dt.reflectance_rgb"),
    "short2": ("DataShort2Attr", "dt.short2"),
    "short3": ("DataShort3Attr", "dt.short3"),
    "spectrumRGB": ("DataSpectrumRGBAttr", "dt.specrtrum_rgb"),
    "string": ("DataStringAttr", "dt.string"),
    "stringArray": ("DataStringArrayAttr", "dt.string_array"),
    "vectorArray": ("DataVectorArrayAttr", "dt.vector_array"),
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

    例: ``multiplyDivide`` → ``multiply_divide``
    """
    return re.sub(r"([A-Z])", r"_\1", name).lower().lstrip("_")


def _node_type_to_file_name(node_type: str) -> str:
    """ノードタイプ名をファイル名 (snake_case.py) へ変換する。

    例: ``multiplyDivide`` → ``multiply_divide.py``
    """
    return f"{_camel_to_snake(node_type)}.py"


def _resolve_attr_class(attr_info: AttrInfo) -> tuple[str, str] | None:
    """AttrInfo から ``(クラス名, モジュールパス)`` を返す。

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
    """Attr コンストラクタ引数文字列を生成する。

    例: ``multi=True``

    .. note::
        ``enum`` 型の ``enum_name`` 引数は :func:`generate_node_class_code` 内で
        生成された ``AttributeEnum`` サブクラス名を用いて別途設定される。
    """
    args: list[str] = []

    if attr_info.multi:
        args.append("multi=True")

    return ", ".join(args)


def _label_to_enum_member_name(label: str) -> str:
    """ラベル文字列を SCREAMING_SNAKE_CASE の Enum メンバー名へ変換する。

    例: ``"No operation"`` → ``"NO_OPERATION"``、
        ``"Waiting-Normal"`` → ``"WAITING_NORMAL"``、
        ``"3D"`` → ``"_3D"`` (先頭が数字の場合はアンダースコアを付与)
    """
    name = re.sub(r"[^a-zA-Z0-9]+", "_", label)
    name = name.strip("_")
    if name and name[0].isdigit():
        name = "_" + name
    return name.upper()


def _long_name_to_enum_class_name(long_name: str) -> str:
    """アトリビュートの long_name を PascalCase の Enum クラス名へ変換する。

    例: ``"operation"`` → ``"OperationEnum"``、
        ``"nodeState"`` → ``"NodeStateEnum"``
    """
    return long_name[0].upper() + long_name[1:] + "Enum"


def _build_enum_class_lines(
    class_name: str,
    entries: list[tuple[str, int | None]],
) -> list[str]:
    """``AttributeEnum`` サブクラスのコード行リストを生成する。

    Args:
        class_name (str): 生成するクラス名 (例: ``"OperationEnum"``)
        entries (list[tuple[str, int | None]]): ``(ラベル, 明示的整数値 or None)`` のリスト

    Returns:
        list[str]: クラス定義のコード行リスト
    """
    lines: list[str] = [f"class {class_name}(AttributeEnum):"]
    for label, explicit_val in entries:
        member_name = _label_to_enum_member_name(label)
        if explicit_val is not None:
            lines.append(f'    {member_name} = ("{label}", {explicit_val})')
        else:
            lines.append(f'    {member_name} = "{label}"')
    return lines


# ---------------------------------------------------------------------------
# 公開 API
# ---------------------------------------------------------------------------


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

    # 使用する Attr クラスとそのインポートパスを収集する
    # クラス名 → "at.xxx" or "dt.xxx"
    imports: dict[str, str] = {}

    # 生成する AttributeEnum サブクラス: (クラス名, エントリリスト)
    enum_classes: list[tuple[str, list[tuple[str, int | None]]]] = []

    # 生成するアトリビュート行
    attr_lines: list[str] = []

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

        # Attr クラスを解決する
        resolved = _resolve_attr_class(attr_info)
        if resolved is None:
            attr_lines.append(
                f"    # TODO: {long_name} (attributeType={attr_info.attribute_type}, dataType={attr_info.data_type}) は未対応のため手動で追加してください"
            )
            continue

        attr_cls_name, module_path = resolved
        imports[attr_cls_name] = module_path

        # コンストラクタ引数を組み立てる
        args: list[str] = []
        if attr_info.multi:
            args.append("multi=True")

        if attr_info.attribute_type == "enum":
            entries = _parse_enum_entries(attr_info.enum_name)
            if entries:
                enum_cls_name = _long_name_to_enum_class_name(long_name)
                enum_classes.append((enum_cls_name, entries))
                args.append(f"enum_name={enum_cls_name}")

        init_args = ", ".join(args)
        attr_lines.append(f"    {long_name} = {attr_cls_name}({init_args})")

        # short_name のエイリアス行
        short_name = attr_info.short_name
        if short_name and short_name != long_name:
            attr_lines.append(f"    {short_name} = {long_name}")

    # インポート行 (モジュールパスでソートして並びを安定させる)
    import_lines: list[str] = ["from ._core import DG"]
    if enum_classes:
        import_lines.append("from .....attr.enum import AttributeEnum")
    for cls_name, mod_path in sorted(imports.items(), key=lambda kv: kv[1]):
        import_lines.append(f"from ...attr.{mod_path} import {cls_name}")

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
    lines.append(f'    NODE_TYPE = "{node_type}"')
    if attr_lines:
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

    出力先::

        {src_dir}/bd_util/maya/node/operator/node/dg/{snake_case_node_type}.py

    Args:
        node_type (str): Maya ノードタイプ名 (例: ``"multiplyDivide"``)
        src_dir (str | pathlib.Path): リポジトリの src ディレクトリへのパス
            (例: ``r"C:/path/bakedanuki-util/src"``)
        attr_infos (list[AttrInfo] | None): 属性情報のリスト。
            ``None`` の場合は :func:`~bd_util.maya.attr.query.get_attribute_infos`
            で自動取得する。
    """
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
