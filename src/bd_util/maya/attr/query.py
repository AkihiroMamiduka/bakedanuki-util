# coding: utf-8

from enum import Enum
import dataclasses
import typing

# maya
import maya.cmds as cmds
import maya.api.OpenMaya as om


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


# info
@dataclasses.dataclass
class AttrInfo:
    long_name: str
    short_name: str
    attribute_type: str
    data_type: str
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


def safe_query(func, *args, **kwargs):
    """例外が出ても None を返す安全ラッパー"""
    try:
        return func(*args, **kwargs)
    except Exception:
        return None


def get_attr_info(node: str, attr: str) -> AttrInfo:
    """指定したノードの特定アトリビュートの AttrInfo を返す"""
    long_name = attr
    short_name = safe_query(cmds.attributeQuery, attr, node=node, shortName=True)
    attribute_type = safe_query(
        cmds.attributeQuery, attr, node=node, attributeType=True
    )
    data_type = get_data_type_name(node, attr)
    default_value = safe_query(
        cmds.attributeQuery, attr, node=node, listDefault=True
    )
    min_value = safe_query(
        cmds.attributeQuery, attr, node=node, minimum=True
    )
    max_value = safe_query(
        cmds.attributeQuery, attr, node=node, maximum=True
    )
    soft_min_value = safe_query(
        cmds.attributeQuery, attr, node=node, softMin=True
    )
    soft_max_value = safe_query(
        cmds.attributeQuery, attr, node=node, softMax=True
    )
    enum_name = safe_query(cmds.attributeQuery, attr, node=node, listEnum=True)
    multi = safe_query(cmds.attributeQuery, attr, node=node, multi=True)
    number_of_children = safe_query(
        cmds.attributeQuery, attr, node=node, numberOfChildren=True
    )
    parent = safe_query(cmds.attributeQuery, attr, node=node, listParent=True)
    readable = safe_query(cmds.attributeQuery, attr, node=node, readable=True)
    writable = safe_query(cmds.attributeQuery, attr, node=node, writable=True)
    category = safe_query(cmds.attributeQuery, attr, node=node, categories=True)

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
    )


def get_attribute_infos(node_type) -> list[AttrInfo]:
    # アトリビュート情報確認用に代理のノードを作成
    node = cmds.createNode(node_type)

    # 全てのアトリビュートを取得
    attrs = cmds.listAttr(node) or []

    attr_infos: list[AttrInfo] = []
    for attr in attrs:
        # long / short name
        long_name = attr
        short_name = cmds.attributeQuery(attr, node=node, shortName=True)

        # attributeType / dataType
        attribute_type = cmds.attributeQuery(
            attr, node=node, attributeType=True
        )
        data_type = get_data_type_name(node, attr)

        # default value
        default_value = safe_query(
            cmds.attributeQuery, attr, node=node, listDefault=True
        )

        # min / max
        min_value = safe_query(
            cmds.attributeQuery, attr, node=node, minimum=True
        )
        max_value = safe_query(
            cmds.attributeQuery, attr, node=node, maximum=True
        )
        soft_min_value = safe_query(
            cmds.attributeQuery, attr, node=node, softMin=True
        )
        soft_max_value = safe_query(
            cmds.attributeQuery, attr, node=node, softMax=True
        )

        # enum
        enum_name = cmds.attributeQuery(attr, node=node, listEnum=True)

        # multi
        multi = cmds.attributeQuery(attr, node=node, multi=True)

        # number of children
        number_of_children = cmds.attributeQuery(
            attr, node=node, numberOfChildren=True
        )

        # parent
        parent = cmds.attributeQuery(attr, node=node, listParent=True)

        # readable / writable
        readable = cmds.attributeQuery(attr, node=node, readable=True)
        writable = cmds.attributeQuery(attr, node=node, writable=True)

        # category
        category = cmds.attributeQuery(attr, node=node, categories=True)

        # 情報をまとめる
        attr_info = AttrInfo(
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
        )
        attr_infos.append(attr_info)

    # ノードを削除
    cmds.delete(node)

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
