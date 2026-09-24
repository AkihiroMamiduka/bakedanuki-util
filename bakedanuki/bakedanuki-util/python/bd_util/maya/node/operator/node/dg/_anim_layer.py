"""Maya バージョン間で共用するアニメーションレイヤー操作。"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Self, cast

from maya import cmds
from maya.api import OpenMaya as om

from ....modifier import ModifierManager
from ...attr._core import PlugOperator
from ...attr import _keyframe_target
from .._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator


def _validate_name(name: object) -> None:
    if name is None:
        return
    if not isinstance(name, str):
        raise TypeError("name must be a string or None.")
    if not name or any(char in name for char in ".*?[]|"):
        raise ValueError("name must be a nonempty node name.")


def node_object(value: object) -> om.MObject:
    """ノード名またはノードオブジェクトを有効な `MObject` に変換する。"""
    if isinstance(value, NodeOperator):
        node = value.m_obj
    elif isinstance(value, om.MObject):
        node = value
    elif isinstance(value, str):
        if not value or any(char in value for char in ".*?[]"):
            raise ValueError("Expected one node name.")
        selection = om.MSelectionList()
        selection.add(value)
        if selection.length() != 1:
            raise ValueError("Expected one node name.")
        node = selection.getDependNode(0)
    else:
        raise TypeError("Expected a NodeOperator, MObject or node name.")
    if not om.MObjectHandle(node).isAlive() or not node.hasFn(
        om.MFn.kDependencyNode
    ):
        raise ValueError("The node is not available.")
    return node


def live_node(node: om.MObject) -> om.MFnDependencyNode:
    """シーン内で有効なノードの関数セットを返す。"""
    handle = om.MObjectHandle(node)
    if not handle.isAlive() or not handle.isValid():
        raise RuntimeError("The node is not available in the scene.")
    return om.MFnDependencyNode(node)


def _editable_layer(node: om.MObject) -> str:
    fn = live_node(node)
    _keyframe_target.check_editable_node(fn)
    name = fn.name()
    if not node.hasFn(om.MFn.kAnimLayer):
        raise TypeError("Expected an animation layer.")
    if name == cmds.animLayer(query=True, root=True):
        raise RuntimeError(
            "The base animation layer does not need explicit membership."
        )
    if fn.findPlug("lock", False).asBool():
        raise RuntimeError(f"Cannot edit locked animation layer {name}.")
    return name


@dataclass(frozen=True, slots=True)
class PlugIdentity:
    """登録対象プラグと、その生存確認に使うノード・属性を保持する。"""

    plug: om.MPlug
    node: om.MObjectHandle
    attribute: om.MObjectHandle

    @classmethod
    def capture(cls, value: object) -> PlugIdentity:
        """プラグを解決し、後で生存確認できる形で保持する。

        Args:
            value: `PlugOperator`、`MPlug`、またはプラグ名。

        Returns:
            登録時に再検証できるプラグ識別情報。
        """
        if isinstance(value, PlugOperator):
            plug = value.plug
        elif isinstance(value, om.MPlug):
            plug = value
        elif isinstance(value, str):
            if not value or any(char in value for char in "*?"):
                raise ValueError("Expected one plug name.")
            selection = om.MSelectionList()
            selection.add(value)
            if selection.length() != 1:
                raise ValueError("Expected one plug name.")
            plug = selection.getPlug(0)
        else:
            raise TypeError("Expected a PlugOperator, MPlug or plug name.")
        if plug.isNull:
            raise ValueError("The plug is not available.")
        return cls(
            plug,
            om.MObjectHandle(plug.node()),
            om.MObjectHandle(plug.attribute()),
        )

    def resolve(self) -> om.MPlug:
        """ノードと属性が残っていることを確認してプラグを返す。

        Raises:
            RuntimeError: 登録前にノードまたは属性が無効になった場合。
        """
        if not all(
            handle.isAlive() and handle.isValid()
            for handle in (self.node, self.attribute)
        ):
            raise RuntimeError(
                "The layer membership plug is not available in the scene."
            )
        attribute = self.attribute.object()
        fn = om.MFnDependencyNode(self.node.object())
        try:
            current = fn.attribute(om.MFnAttribute(attribute).name)
        except RuntimeError as exc:
            raise RuntimeError(
                "The layer membership attribute is not available in the scene."
            ) from exc
        if current != attribute:
            raise RuntimeError(
                "The layer membership attribute is not available in the scene."
            )
        return self.plug


def leaf_plugs(plug: om.MPlug) -> Iterator[om.MPlug]:
    """既存の配列要素と複合属性を展開し、末端のプラグを順に返す。"""
    if plug.isArray:
        for index in sorted(plug.getExistingArrayAttributeIndices()):
            yield from leaf_plugs(plug.elementByLogicalIndex(index))
    elif plug.isCompound:
        for index in range(plug.numChildren()):
            yield from leaf_plugs(plug.child(index))
    else:
        yield plug


def locked_plug(plug: om.MPlug) -> bool:
    """プラグ自身または親・配列属性がロックされているかを返す。"""
    while True:
        if plug.isLocked:
            return True
        if plug.isChild:
            plug = plug.parent()
        elif plug.isElement:
            plug = plug.array()
        else:
            return False


def supported_plug(plug: om.MPlug) -> bool:
    """プラグがレイヤー登録に対応する書き込み可能な型かを返す。"""
    attribute = plug.attribute()
    if not om.MFnAttribute(attribute).writable:
        return False
    if attribute.hasFn(om.MFn.kNumericAttribute):
        return om.MFnNumericAttribute(attribute).numericType() in (
            om.MFnNumericData.kBoolean,
            om.MFnNumericData.kShort,
            om.MFnNumericData.kInt,
            om.MFnNumericData.kFloat,
            om.MFnNumericData.kDouble,
        )
    return any(
        attribute.hasFn(kind)
        for kind in (
            om.MFn.kUnitAttribute,
            om.MFn.kEnumAttribute,
        )
    )


def _members(name: str) -> set[str]:
    result: set[str] = set()
    for member in (
        cast(
            list[str] | None, cmds.animLayer(name, query=True, attribute=True)
        )
        or ()
    ):
        selection = om.MSelectionList()
        selection.add(member)
        result.add(_keyframe_target.plug_path(selection.getPlug(0)))
    return result


class AnimLayerOperations(NodeOperator):
    """レイヤーの作成とメンバー登録を DG 履歴へ予約する。"""

    __slots__ = ()

    @classmethod
    def create(
        cls,
        modifier_manager: ModifierManager,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        override: bool = False,
    ) -> Self:
        """ベースを確保し、加算または Override レイヤーの作成を予約する。

        `modifier_manager.do_it_dg()` で一連の操作を実行する。

        Args:
            modifier_manager: 作成と Undo を管理するオブジェクト。
            name: 指定する場合のレイヤー名。
            auto_add_attr: 定義済みの追加属性も作成するか。
            override: `True` なら Override、`False` なら加算レイヤー。

        Returns:
            作成を予約したレイヤー。
        """
        if type(override) is not bool:
            raise TypeError("override must be a bool.")
        _validate_name(name)
        root: om.MObject | None = None

        def prepare_root(modifier: om.MDGModifier) -> None:
            nonlocal root
            root_name = cmds.animLayer(query=True, root=True)
            if root_name:
                root = node_object(root_name)
                _keyframe_target.check_editable_node(live_node(root))
            else:
                root = modifier.createNode("animLayer")
                modifier.renameNode(root, "BaseAnimation")
                modifier.newPlugValueBool(
                    om.MFnDependencyNode(root).findPlug("override", False),
                    True,
                )

        # ベースの有無は実行時のシーンで判定し、同じ履歴内に作成を積む。
        modifier_manager.queue_dg_modifier(prepare_root)
        result = super().create(modifier_manager, name, auto_add_attr)
        modifier_manager.dg_mod.newPlugValueBool(
            result.fn_node.findPlug("override", False), override
        )

        def prepare_layer(modifier: om.MDGModifier) -> None:
            if root is None:
                raise RuntimeError(
                    "The base animation layer was not prepared."
                )
            root_name = live_node(root).name()
            layer_name = live_node(result.m_obj).name()
            modifier.pythonCommandToExecute(
                lambda: cmds.animLayer(layer_name, edit=True, parent=root_name)
            )

        modifier_manager.queue_dg_modifier(prepare_layer)
        return result

    def add_plugs(
        self, plugs: Iterable[PlugOperator[Any] | om.MPlug | str]
    ) -> None:
        """指定プラグをレイヤーへ登録する操作を予約する。

        複合属性と既存の配列要素は末端のプラグに展開する。
        対象の編集可否は `modifier_manager.do_it_dg()` で確認する。

        Args:
            plugs: 登録するプラグの iterable。単一のプラグは受け付けない。
        """
        if isinstance(plugs, (str, PlugOperator, om.MPlug)):
            raise TypeError("plugs must be an iterable of plugs.")
        captured = tuple(PlugIdentity.capture(plug) for plug in plugs)
        self._queue_membership(captured, ())

    def add_nodes(
        self, nodes: Iterable[NodeOperator | om.MObject | str]
    ) -> None:
        """ノードの keyable かつ未ロックの対応プラグを登録予約する。

        対象プラグの列挙と編集可否の確認は
        `modifier_manager.do_it_dg()` の実行時に行う。

        Args:
            nodes: 登録するノードの iterable。単一のノードは受け付けない。
        """
        if isinstance(nodes, (str, NodeOperator, om.MObject)):
            raise TypeError("nodes must be an iterable of nodes.")
        captured = tuple(node_object(node) for node in nodes)
        self._queue_membership((), captured)

    def _queue_membership(
        self, plugs: tuple[PlugIdentity, ...], nodes: tuple[om.MObject, ...]
    ) -> None:
        if not plugs and not nodes:
            return
        layer = self.m_obj
        added: set[str] = set()

        def prepare(modifier: om.MDGModifier) -> None:
            name = _editable_layer(layer)
            candidates: list[om.MPlug] = []
            # 明示指定は無効な属性を拒否し、ノード指定は利用可能な属性だけを集める。
            for target in plugs:
                plug = target.resolve()
                _keyframe_target.check_editable_node(live_node(plug.node()))
                for leaf in leaf_plugs(plug):
                    if not supported_plug(leaf):
                        raise TypeError(
                            f"Unsupported animation layer plug: {_keyframe_target.plug_path(leaf)}"
                        )
                    if locked_plug(leaf):
                        raise RuntimeError(
                            f"Cannot register locked plug: {_keyframe_target.plug_path(leaf)}"
                        )
                    candidates.append(leaf)
            for node in nodes:
                fn = live_node(node)
                _keyframe_target.check_editable_node(fn)
                for index in range(fn.attributeCount()):
                    attribute = fn.attribute(index)
                    if not om.MFnAttribute(attribute).parent.isNull():
                        continue
                    candidates.extend(
                        leaf
                        for leaf in leaf_plugs(fn.findPlug(attribute, False))
                        if leaf.isKeyable
                        and not locked_plug(leaf)
                        and supported_plug(leaf)
                    )
            # 既存メンバーと同じ要求内の重複を除いて登録する。
            registered = _members(name)
            for plug in candidates:
                path = _keyframe_target.plug_path(plug)
                if path in registered or path in added:
                    continue
                added.add(path)

                def add(path: str = path) -> None:
                    cmds.animLayer(name, edit=True, attribute=path)

                modifier.pythonCommandToExecute(add)

        def verify(modifier: om.MDGModifier) -> None:
            # Maya command の成功後も実際の登録状態を確認する。
            if added and not added.issubset(_members(live_node(layer).name())):
                raise RuntimeError(
                    "Maya could not register all requested animation layer plugs."
                )

        self.modifier_manager.queue_dg_modifier(prepare)
        self.modifier_manager.queue_dg_modifier(verify)
