# coding: utf-8
"""既存属性の完全なpathを扱う内部共通処理。"""

from typing import cast

from maya.api import OpenMaya as om


def attribute_path(plug: om.MPlug) -> str:
    """aliasを含まない長名の相対属性pathを返す。"""
    path = cast(
        str,
        plug.partialName(
            includeNodeName=False,
            useAlias=False,
            useFullAttributePath=True,
            useLongNames=True,
        ),
    )
    # 非一意な最上位名は先頭のdotでcompound配下と区別する
    if (
        not plug.isChild
        and not om.MFnAttribute(plug.attribute()).enforcingUniqueName
    ):
        return "." + path
    return path


def _matches_parent_path(plug: om.MPlug, parts: list[str]) -> bool:
    """最上位からleafまで、段数と各段の長名または短名が一致するか返す。"""
    chain = [plug]
    while chain[-1].isChild:
        chain.append(chain[-1].parent())
    if len(chain) != len(parts):
        return False
    for name, parent in zip(parts, reversed(chain), strict=True):
        attribute = om.MFnAttribute(parent.attribute())
        if name not in (attribute.name, attribute.shortName):
            return False
    return True


def find_attribute_plug(
    node: om.MFnDependencyNode, attribute_name: str
) -> om.MPlug:
    """長名・短名・完全な相対pathを曖昧なleaf名を許さず解決する。"""
    absolute_path = attribute_name.startswith(".")
    parts = attribute_name.removeprefix(".").split(".")
    if not all(parts) or any(char in attribute_name for char in "[]*?"):
        raise ValueError(
            "attribute_nameには単一の属性名か相対pathを指定してください"
        )
    check_parent_path = absolute_path or len(parts) > 1

    # 一意な実名は直接取得し、aliasや不正な親pathを受理しない
    try:
        direct = node.findPlug(parts[-1], False)
    except RuntimeError:
        direct = None
    if direct is not None:
        leaf = om.MFnAttribute(direct.attribute())
        if (
            leaf.enforcingUniqueName
            and parts[-1] in (leaf.name, leaf.shortName)
            and (not check_parent_path or _matches_parent_path(direct, parts))
        ):
            return direct

    # 非一意名など直接確定できない場合は全候補を調べ、曖昧さを拒否する
    matches: list[om.MPlug] = []
    for index in range(node.attributeCount()):
        attribute = node.attribute(index)
        leaf = om.MFnAttribute(attribute)
        if parts[-1] not in (leaf.name, leaf.shortName):
            continue
        plug = node.findPlug(attribute, False)
        if check_parent_path and not _matches_parent_path(plug, parts):
            continue
        matches.append(plug)
    if not matches:
        raise AttributeError(f"属性が見つかりません: {attribute_name}")
    if len(matches) != 1:
        raise ValueError(
            f"属性名が曖昧です。完全な相対pathを指定してください: {attribute_name}"
        )
    return matches[0]
