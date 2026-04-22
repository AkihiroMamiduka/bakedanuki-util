# coding: utf-8

from enum import Enum

# maya
import maya.cmds as cmds
import maya.api.OpenMaya as om


class AttrKind(Enum):
    ATTRIBUTE_TYPE = 0
    DATA_TYPE = 1


def get_attr_kind(node, attr):

    sel = om.MSelectionList()
    sel.add(node)

    obj = sel.getDependNode(0)
    fn = om.MFnDependencyNode(obj)

    plug = fn.findPlug(attr, False)
    attr_obj = plug.attribute()

    if attr_obj.hasFn(om.MFn.kTypedAttribute):
        return AttrKind.DATA_TYPE

    return AttrKind.ATTRIBUTE_TYPE


def is_attribute_type(node, attr):
    return get_attr_kind(node, attr) == AttrKind.ATTRIBUTE_TYPE


def is_data_type(node, attr):
    return get_attr_kind(node, attr) == AttrKind.DATA_TYPE


def safe_query(func, *args, **kwargs):
    """例外が出ても None を返す安全ラッパー"""
    try:
        return func(*args, **kwargs)
    except Exception:
        return None


def print_attribute_info(node_type):
    node = cmds.createNode(node_type)

    attrs = cmds.listAttr(node) or []
    print(attrs)

    for attr in attrs:
        # long / short name
        long_name = attr
        short_name = safe_query(
            cmds.attributeQuery, attr, node=node, shortName=True
        )

        # attributeType / dataType
        attribute_type = safe_query(
            cmds.attributeQuery, attr, node=node, attributeType=True
        )

        is_dataType = is_data_type(node, attr)

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
        enum_name = safe_query(
            cmds.attributeQuery, attr, node=node, listEnum=True
        )

        # multi
        multi = safe_query(cmds.attributeQuery, attr, node=node, multi=True)

        # number of children
        number_of_children = safe_query(
            cmds.attributeQuery, attr, node=node, numberOfChildren=True
        )

        # parent
        parent = safe_query(
            cmds.attributeQuery, attr, node=node, listParent=True
        )

        # readable / writable
        readable = safe_query(
            cmds.attributeQuery, attr, node=node, readable=True
        )

        writable = safe_query(
            cmds.attributeQuery, attr, node=node, writable=True
        )

        # category
        category = safe_query(
            cmds.attributeQuery, attr, node=node, categories=True
        )

        # disconnect behaviour
        disconnect_behaviour = safe_query(
            cmds.attributeQuery, attr, node=node, disconnectBehavior=True
        )

        print("--------------------------------------------------------------")
        print("           longName:", long_name)
        print("          shortName:", short_name)
        print("      attributeType:", attribute_type)
        print("        is_dataType:", is_dataType)
        print("       defaultValue:", default_value)
        print("           minValue:", min_value)
        print("           maxValue:", max_value)
        print("       softMinValue:", soft_min_value)
        print("       softMaxValue:", soft_max_value)
        print("           enumName:", enum_name)
        print("              multi:", multi)
        print("   numberOfChildren:", number_of_children)
        print("             parent:", parent)
        print("           readable:", readable)
        print("           writable:", writable)
        print("           category:", category)
        print("disconnectBehaviour:", disconnect_behaviour)
