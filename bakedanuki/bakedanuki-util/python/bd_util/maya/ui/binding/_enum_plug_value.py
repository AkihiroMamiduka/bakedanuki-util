# coding: utf-8
from collections.abc import Callable
from typing import cast

from maya import cmds
from maya.api import OpenMaya as om

from ....ui.binding.enum.definition import EnumDefinition, EnumItem


def _field_name(attribute: om.MFnEnumAttribute, value: int) -> str | None:
    try:
        return attribute.fieldName(value)
    except (RuntimeError, OverflowError):
        return None


class EnumPlugValue:
    """実際のMaya属性から整数値とenum定義を読む。"""

    def __init__(self, plug: om.MPlug) -> None:
        self._plug = plug
        self._raw_definition: str | None = None
        self._definition = EnumDefinition()

    def read(self) -> int:
        """Maya enum属性の現在の整数値を返す。"""
        return self._plug.asShort()

    def matches(self, value: int) -> bool:
        """指定値がMaya enum属性の現在値と一致するか返す。"""
        return self.read() == value

    @property
    def definition(self) -> EnumDefinition:
        """現在のMaya enum定義を取得し、変更時にキャッシュを更新する。"""
        # enumNameは値が飛ぶ箇所だけ=整数を含む。毎回queryして外部編集も検出する。
        fn = om.MFnEnumAttribute(self._plug.attribute())
        if fn.dynamic:
            query = cast(Callable[..., str], cmds.addAttr)
            raw = query(self._plug.name(), query=True, enumName=True)
        else:
            query_static = cast(Callable[..., list[str]], cmds.attributeQuery)
            node = self._plug.node()
            node_name = (
                om.MFnDagNode(node).fullPathName()
                if node.hasFn(om.MFn.kDagNode)
                else om.MFnDependencyNode(node).name()
            )
            raw = query_static(fn.name, node=node_name, listEnum=True)[0]
        if raw == self._raw_definition:
            return self._definition
        items: list[EnumItem] = []
        next_value = 0
        for part in raw.split(":") if raw else ():
            name = part
            value = next_value
            if _field_name(fn, value) != part and "=" in part:
                candidate, number = part.rsplit("=", 1)
                try:
                    explicit = int(number)
                except ValueError:
                    pass
                else:
                    # 名前自体の=と区別し、Maya APIの実定義で確認する。
                    actual_name = _field_name(fn, explicit)
                    if actual_name == candidate:
                        name, value = candidate, explicit
            if _field_name(fn, value) != name:
                raise ValueError("Mayaのenum定義を解決できません")
            items.append(EnumItem(value, name))
            next_value = value + 1
        definition = EnumDefinition(tuple(items))
        self._definition = definition
        self._raw_definition = raw
        return definition
