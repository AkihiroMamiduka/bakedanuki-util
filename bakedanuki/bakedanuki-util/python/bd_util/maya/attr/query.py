# coding: utf-8

from collections.abc import Callable
import dataclasses
from enum import Enum
from typing import ParamSpec, TypeVar, cast

# maya
from .. import scene as u_scene
import maya.cmds as cmds
import maya.api.OpenMaya as om

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)

P = ParamSpec("P")
R = TypeVar("R")


# get
#   attr
def get_attr(node: str, attr: str) -> om.MObject:

    sel = om.MSelectionList()
    sel.add(node)

    obj = sel.getDependNode(0)
    fn = om.MFnDependencyNode(obj)

    plug = fn.findPlug(attr, False)
    attr_obj = plug.attribute()

    return attr_obj


def get_mfn_attribute(node: str, attr: str) -> om.MFnAttribute:
    return om.MFnAttribute(get_attr(node, attr))


def get_attr_path_name(node: str, attr: str) -> str | None:
    path_name = getattr(get_mfn_attribute(node, attr), "pathName", None)
    if path_name is None:
        return None
    if isinstance(path_name, str):
        return path_name
    if callable(path_name):
        value = cast(Callable[[], object], path_name)()
        return value if isinstance(value, str) else None
    return None


def get_attr_parent_names(node: str, attr: str) -> list[str] | None:
    parent = get_mfn_attribute(node, attr).parent
    if parent.isNull():
        return None
    return [om.MFnAttribute(parent).name]


def get_attr_enforcing_unique_name(node: str, attr: str) -> bool | None:
    value = getattr(get_mfn_attribute(node, attr), "enforcingUniqueName", None)
    return value if isinstance(value, bool) else None


def get_attr_short_name(node: str, attr: str) -> str | None:
    short_name = safe_query(
        cmds.attributeQuery, attr, node=node, shortName=True
    )
    if isinstance(short_name, str):
        return short_name
    fallback = getattr(get_mfn_attribute(node, attr), "shortName", None)
    return fallback if isinstance(fallback, str) else None


def is_typed_attr(node: str, attr: str) -> bool:
    attr_obj = safe_query(get_attr, node, attr)
    if attr_obj is None:
        return False
    return attr_obj.hasFn(om.MFn.kTypedAttribute)


class AttrKind(Enum):
    ATTRIBUTE_TYPE = 0
    DATA_TYPE = 1


# type kind
def get_attr_kind(node: str, attr: str) -> AttrKind:
    if is_typed_attr(node, attr):
        return AttrKind.DATA_TYPE
    return AttrKind.ATTRIBUTE_TYPE


def is_attribute_type(node: str, attr: str) -> bool:
    return get_attr_kind(node, attr) == AttrKind.ATTRIBUTE_TYPE


def is_data_type(node: str, attr: str) -> bool:
    return get_attr_kind(node, attr) == AttrKind.DATA_TYPE


# data_type_name
def get_data_type_name(node: str, attr: str) -> str | None:
    attr_obj = safe_query(get_attr, node, attr)
    if attr_obj is None:
        return None

    return get_data_type_name_from_attr(attr_obj)


def get_data_type_name_from_attr(attr_obj: om.MObject) -> str | None:
    """OpenMaya attribute object から data type 名を返す。"""

    if not attr_obj.hasFn(om.MFn.kTypedAttribute):
        return None

    fn_typed = om.MFnTypedAttribute(attr_obj)
    data_enum = fn_typed.attrType()

    mapping = {
        om.MFnData.kString: "string",
        om.MFnData.kMatrix: "matrix",
        om.MFnData.kMesh: "mesh",
        om.MFnData.kNurbsCurve: "nurbsCurve",
        om.MFnData.kNurbsSurface: "nurbsSurface",
        om.MFnData.kComponentList: "componentList",
        om.MFnData.kDoubleArray: "doubleArray",
        om.MFnData.kIntArray: "intArray",
        om.MFnData.kVectorArray: "vectorArray",
        om.MFnData.kPointArray: "pointArray",
        om.MFnData.kStringArray: "stringArray",
    }

    return mapping.get(data_enum, str(data_enum))


def get_numeric_attribute_type_name(attr_obj: om.MObject) -> str | None:
    if not attr_obj.hasFn(om.MFn.kNumericAttribute):
        return None

    numeric_type = om.MFnNumericAttribute(attr_obj).numericType()
    mapping = {
        om.MFnNumericData.kBoolean: "bool",
        om.MFnNumericData.kByte: "byte",
        om.MFnNumericData.kChar: "char",
        om.MFnNumericData.kShort: "short",
        om.MFnNumericData.kLong: "long",
        om.MFnNumericData.kInt64: "long long int",
        om.MFnNumericData.kFloat: "float",
        om.MFnNumericData.kDouble: "double",
        om.MFnNumericData.kAddr: "addr",
        om.MFnNumericData.k2Short: "short2",
        om.MFnNumericData.k3Short: "short3",
        om.MFnNumericData.k2Long: "long2",
        om.MFnNumericData.k3Long: "long3",
        om.MFnNumericData.k2Float: "float2",
        om.MFnNumericData.k3Float: "float3",
        om.MFnNumericData.k2Double: "double2",
        om.MFnNumericData.k3Double: "double3",
        om.MFnNumericData.k4Double: "double4",
    }
    return mapping.get(numeric_type)


def get_unit_attribute_type_name(attr_obj: om.MObject) -> str | None:
    if not attr_obj.hasFn(om.MFn.kUnitAttribute):
        return None

    unit_type = om.MFnUnitAttribute(attr_obj).unitType()
    mapping = {
        om.MFnUnitAttribute.kAngle: "doubleAngle",
        om.MFnUnitAttribute.kDistance: "doubleLinear",
        om.MFnUnitAttribute.kTime: "time",
    }
    return mapping.get(unit_type)


def get_matrix_attribute_type_name(attr_obj: om.MObject) -> str | None:
    if not attr_obj.hasFn(om.MFn.kMatrixAttribute):
        return None

    matrix_type = om.MFnMatrixAttribute(attr_obj).attrType()
    if matrix_type == om.MFnMatrixAttribute.kFloat:
        return "fltMatrix"
    return "matrix"


def get_attribute_type_name(node: str, attr: str) -> str | None:
    attribute_type = safe_query(
        cmds.attributeQuery, attr, node=node, attributeType=True
    )
    if isinstance(attribute_type, str):
        return attribute_type

    attr_obj = safe_query(get_attr, node, attr)
    if attr_obj is None:
        return None

    return get_attribute_type_name_from_attr(attr_obj)


def get_attribute_type_name_from_attr(
    attr_obj: om.MObject,
) -> str | None:
    """OpenMaya attribute object から attribute type 名を返す。"""

    for resolver in (
        get_numeric_attribute_type_name,
        get_unit_attribute_type_name,
        get_matrix_attribute_type_name,
    ):
        resolved = resolver(attr_obj)
        if resolved is not None:
            return resolved

    if attr_obj.hasFn(om.MFn.kEnumAttribute):
        return "enum"
    if attr_obj.hasFn(om.MFn.kMessageAttribute):
        return "message"
    if attr_obj.hasFn(om.MFn.kLightDataAttribute):
        return "lightData"
    if attr_obj.hasFn(om.MFn.kTypedAttribute):
        return "typed"
    if attr_obj.hasFn(om.MFn.kCompoundAttribute):
        return "compound"
    if hasattr(om.MFn, "kGenericAttribute") and attr_obj.hasFn(
        om.MFn.kGenericAttribute
    ):
        return "generic"

    return None


# info
@dataclasses.dataclass
class AttrInfo:
    long_name: str
    short_name: str | None
    attribute_type: str | None
    data_type: str | None
    default_value: object | None
    min_value: object | None
    max_value: object | None
    soft_min_value: object | None
    soft_max_value: object | None
    enum_name: list[str] | None
    multi: bool | None
    number_of_children: int | None
    parent: list[str] | None
    readable: bool | None
    writable: bool | None
    category: list[str] | None
    path_name: str | None = None
    enforcing_unique_name: bool | None = None


def safe_query(
    func: Callable[P, R],
    *args: P.args,
    **kwargs: P.kwargs,
) -> R | None:
    """
    例外が出ても None を返す安全ラッパー
    """
    try:
        return func(*args, **kwargs)
    except Exception:
        return None


def _as_bool(value: object) -> bool | None:
    return value if isinstance(value, bool) else None


def _as_int(value: object) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    return value


def _as_str_list(value: object) -> list[str] | None:
    if not isinstance(value, list):
        return None

    values = cast(list[object], value)
    if not all(isinstance(item, str) for item in values):
        return None
    return cast(list[str], values)


def get_attribute_info(node: str, attr: str) -> AttrInfo:
    # long / short name
    long_name = attr
    short_name = safe_query(get_attr_short_name, node, attr)
    path_name = safe_query(get_attr_path_name, node, attr)
    enforcing_unique_name = safe_query(
        get_attr_enforcing_unique_name, node, attr
    )

    # attributeType / dataType
    attribute_type = get_attribute_type_name(node, attr)
    data_type = get_data_type_name(node, attr)

    # default value
    default_value = safe_query(
        cmds.attributeQuery, attr, node=node, listDefault=True
    )

    # min / max
    min_value = safe_query(cmds.attributeQuery, attr, node=node, minimum=True)
    max_value = safe_query(cmds.attributeQuery, attr, node=node, maximum=True)
    soft_min_value = safe_query(
        cmds.attributeQuery, attr, node=node, softMin=True
    )
    soft_max_value = safe_query(
        cmds.attributeQuery, attr, node=node, softMax=True
    )

    # enum
    enum_name = _as_str_list(
        safe_query(cmds.attributeQuery, attr, node=node, listEnum=True)
    )

    # multi
    multi = _as_bool(
        safe_query(cmds.attributeQuery, attr, node=node, multi=True)
    )

    # number of children
    number_of_children = _as_int(
        safe_query(
            cmds.attributeQuery,
            attr,
            node=node,
            numberOfChildren=True,
        )
    )

    # parent
    parent = _as_str_list(
        safe_query(cmds.attributeQuery, attr, node=node, listParent=True)
    )
    if not parent:
        parent = safe_query(get_attr_parent_names, node, attr)

    # readable / writable
    readable = _as_bool(
        safe_query(cmds.attributeQuery, attr, node=node, readable=True)
    )
    writable = _as_bool(
        safe_query(cmds.attributeQuery, attr, node=node, writable=True)
    )

    # category
    category = _as_str_list(
        safe_query(cmds.attributeQuery, attr, node=node, categories=True)
    )

    # 情報をまとめる
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
        parent=parent,
        readable=readable,
        writable=writable,
        category=category,
        path_name=path_name,
        enforcing_unique_name=enforcing_unique_name,
    )


def get_attribute_info_by_type(node_type: str, attr: str) -> AttrInfo:
    """node instance を作成せず、node type から attribute 情報を返す。"""
    node_class = om.MNodeClass(node_type)
    attr_obj = node_class.attribute(attr)
    fn_attr = om.MFnAttribute(attr_obj)

    short_name = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        shortName=True,
    )
    if not isinstance(short_name, str):
        short_name = fn_attr.shortName

    path_name = getattr(fn_attr, "pathName", None)
    if callable(path_name):
        path_name = cast(Callable[[], object], path_name)()
    if not isinstance(path_name, str):
        path_name = None

    enforcing_unique_name = getattr(fn_attr, "enforcingUniqueName", None)
    if not isinstance(enforcing_unique_name, bool):
        enforcing_unique_name = None

    attribute_type = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        attributeType=True,
    )
    if not isinstance(attribute_type, str):
        attribute_type = get_attribute_type_name_from_attr(attr_obj)
    data_type = get_data_type_name_from_attr(attr_obj)

    default_value = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        listDefault=True,
    )
    min_value = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        minimum=True,
    )
    max_value = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        maximum=True,
    )
    soft_min_value = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        softMin=True,
    )
    soft_max_value = safe_query(
        cmds.attributeQuery,
        attr,
        type=node_type,
        softMax=True,
    )
    enum_name = _as_str_list(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            listEnum=True,
        )
    )
    multi = _as_bool(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            multi=True,
        )
    )
    number_of_children = _as_int(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            numberOfChildren=True,
        )
    )
    parent = _as_str_list(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            listParent=True,
        )
    )
    if not parent and not fn_attr.parent.isNull():
        parent = [om.MFnAttribute(fn_attr.parent).name]
    readable = _as_bool(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            readable=True,
        )
    )
    writable = _as_bool(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            writable=True,
        )
    )
    category = _as_str_list(
        safe_query(
            cmds.attributeQuery,
            attr,
            type=node_type,
            categories=True,
        )
    )

    return AttrInfo(
        long_name=fn_attr.name,
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
        parent=parent,
        readable=readable,
        writable=writable,
        category=category,
        path_name=path_name,
        enforcing_unique_name=enforcing_unique_name,
    )


def get_attribute_infos_by_type(node_type: str) -> list[AttrInfo]:
    """node instance を作成せず、登録済み node type の属性を取得する。"""
    node_class = om.MNodeClass(node_type)
    return [
        get_attribute_info_by_type(
            node_type,
            om.MFnAttribute(node_class.attribute(index)).name,
        )
        for index in range(node_class.attributeCount)
    ]


def get_attribute_infos(
    node_type: str,
    mode_new_scene: bool = False,
    mode_error_skip: bool = False,
) -> list[AttrInfo]:
    def _post_process(node: str) -> None:
        # ノードを削除するか新規シーンにするか
        if mode_new_scene:
            u_scene.new_scene()
        else:
            if safe_query(cmds.objExists, node):
                safe_query(cmds.delete, node)

    logger.debug(f"node_type: {node_type}")

    # アトリビュート情報確認用に代理のノードを作成
    try:
        node = cmds.createNode(node_type)
    except Exception:
        if mode_error_skip:
            logger.warning(
                f"Failed to create node of type '{node_type}'. Skipping."
            )
            return []
        else:
            raise ValueError(f"Invalid node type: '{node_type}'")

    created_node_type = safe_query(cmds.nodeType, node)
    if created_node_type is None:
        _post_process(node)
        if mode_error_skip:
            logger.warning(
                f"Failed to query created node '{node}' for node type "
                f"'{node_type}'. Skipping."
            )
            return []
        else:
            raise ValueError(f"Invalid node type: '{node_type}'")

    # 不明なノードタイプの場合は例外を出す
    if created_node_type == "unknown":
        _post_process(node)
        if mode_error_skip:
            logger.warning(f"Node type '{node_type}' is unknown. Skipping.")
            return []
        else:
            raise ValueError(f"Invalid node type: '{node_type}'")

    # アトリビュートの情報を取得
    attr_infos: list[AttrInfo] = []
    for attr in cmds.listAttr(node) or []:
        attr_infos.append(get_attribute_info(node, attr))

    # ノードを削除
    _post_process(node)

    # 戻り値
    return attr_infos


def print_attribute_infos(
    node_type: str,
    valid_value: bool = True,
) -> None:
    attr_infos: list[AttrInfo] = get_attribute_infos(node_type)
    for attr_info in attr_infos:

        # title
        title = "-" * 8
        title = "{} {} ({}) ({}) ".format(
            title,
            attr_info.long_name,
            attr_info.attribute_type,
            attr_info.data_type if attr_info.data_type else "",
        )
        title = title.ljust(50, "-")
        print(f"{title} ")

        # info
        if valid_value and attr_info.long_name:
            print("           longName:", attr_info.long_name)
        if valid_value and attr_info.short_name:
            print("          shortName:", attr_info.short_name)
        if valid_value and attr_info.path_name:
            print("           pathName:", attr_info.path_name)
        if valid_value and attr_info.enforcing_unique_name is not None:
            print(
                "enforcingUniqueName:",
                attr_info.enforcing_unique_name,
            )
        if valid_value and attr_info.attribute_type:
            print("      attributeType:", attr_info.attribute_type)
        if valid_value and attr_info.data_type:
            print("           dataType:", attr_info.data_type)
        if valid_value and attr_info.default_value:
            print("       defaultValue:", attr_info.default_value)
        if valid_value and attr_info.min_value:
            print("           minValue:", attr_info.min_value)
        if valid_value and attr_info.max_value:
            print("           maxValue:", attr_info.max_value)
        if valid_value and attr_info.soft_min_value:
            print("       softMinValue:", attr_info.soft_min_value)
        if valid_value and attr_info.soft_max_value:
            print("       softMaxValue:", attr_info.soft_max_value)
        if valid_value and attr_info.enum_name:
            print("           enumName:", attr_info.enum_name)
        if valid_value and attr_info.multi:
            print("              multi:", attr_info.multi)
        if valid_value and attr_info.number_of_children:
            print("   numberOfChildren:", attr_info.number_of_children)
        if valid_value and attr_info.parent:
            print("             parent:", attr_info.parent)
        if valid_value and attr_info.readable:
            print("           readable:", attr_info.readable)
        if valid_value and attr_info.writable:
            print("           writable:", attr_info.writable)
        if valid_value and attr_info.category:
            print("           category:", attr_info.category)
        print("")
