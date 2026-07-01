# coding: utf-8

from enum import Enum
import dataclasses
import typing

# maya
from .. import scene as u_scene
import maya.cmds as cmds
import maya.api.OpenMaya as om

# self
from ... import logger as u_logger

logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


# get
#   attr
def get_attr(node, attr) -> om.MObject:

    sel = om.MSelectionList()
    sel.add(node)

    obj = sel.getDependNode(0)
    fn = om.MFnDependencyNode(obj)

    plug = fn.findPlug(attr, False)
    attr_obj = plug.attribute()

    return attr_obj


def get_mfn_attribute(node, attr) -> om.MFnAttribute:
    return om.MFnAttribute(get_attr(node, attr))


def get_attr_path_name(node, attr) -> str | None:
    path_name = getattr(get_mfn_attribute(node, attr), "pathName", None)
    if path_name is None:
        return None
    if not callable(path_name):
        return path_name
    return path_name()


def get_attr_enforcing_unique_name(node, attr) -> bool | None:
    return getattr(get_mfn_attribute(node, attr), "enforcingUniqueName", None)


def get_attr_short_name(node, attr) -> str | None:
    short_name = safe_query(
        cmds.attributeQuery, attr, node=node, shortName=True
    )
    if short_name is not None:
        return short_name
    return getattr(get_mfn_attribute(node, attr), "shortName", None)


def is_typed_attr(node, attr):
    state = False
    if get_attr(node, attr).hasFn(om.MFn.kTypedAttribute):
        state = True
    return state


class AttrKind(Enum):
    ATTRIBUTE_TYPE = 0
    DATA_TYPE = 1


# type kind
def get_attr_kind(node, attr):
    if is_typed_attr(node, attr):
        return AttrKind.DATA_TYPE
    return AttrKind.ATTRIBUTE_TYPE


def is_attribute_type(node, attr):
    return get_attr_kind(node, attr) == AttrKind.ATTRIBUTE_TYPE


def is_data_type(node, attr):
    return get_attr_kind(node, attr) == AttrKind.DATA_TYPE


# data_type_name
def get_data_type_name(node, attr) -> str | None:
    attr_obj = get_attr(node, attr)

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


def get_attribute_type_name(node, attr) -> str | None:
    attribute_type = safe_query(
        cmds.attributeQuery, attr, node=node, attributeType=True
    )
    if attribute_type is not None:
        return attribute_type

    attr_obj = get_attr(node, attr)

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
    short_name: str
    attribute_type: str | None
    data_type: str | None
    default_value: typing.Any
    min_value: typing.Any
    max_value: typing.Any
    soft_min_value: typing.Any
    soft_max_value: typing.Any
    enum_name: str
    multi: bool
    number_of_children: int
    parent: str
    readable: bool
    writable: bool
    category: str
    path_name: str | None = None
    enforcing_unique_name: bool | None = None


def safe_query(func, *args, **kwargs):
    """
    例外が出ても None を返す安全ラッパー
    """
    try:
        return func(*args, **kwargs)
    except Exception:
        return None


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
    enum_name = safe_query(cmds.attributeQuery, attr, node=node, listEnum=True)

    # multi
    multi = safe_query(cmds.attributeQuery, attr, node=node, multi=True)

    # number of children
    number_of_children = safe_query(
        cmds.attributeQuery, attr, node=node, numberOfChildren=True
    )

    # parent
    parent = safe_query(cmds.attributeQuery, attr, node=node, listParent=True)

    # readable / writable
    readable = safe_query(cmds.attributeQuery, attr, node=node, readable=True)
    writable = safe_query(cmds.attributeQuery, attr, node=node, writable=True)

    # category
    category = safe_query(
        cmds.attributeQuery, attr, node=node, categories=True
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


def get_attribute_infos(
    node_type: str,
    mode_new_scene: bool = False,
    mode_error_skip: bool = False,
) -> list[AttrInfo]:
    def _post_process(node: str):
        # ノードを削除するか新規シーンにするか
        if mode_new_scene:
            u_scene.new_scene()
        else:
            cmds.delete(node)

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

    # 不明なノードタイプの場合は例外を出す
    if cmds.nodeType(node) == "unknown":
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


def print_attribute_infos(node_type, valid_value=True):
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
        if (
            valid_value
            and attr_info.enforcing_unique_name is not None
        ):
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
