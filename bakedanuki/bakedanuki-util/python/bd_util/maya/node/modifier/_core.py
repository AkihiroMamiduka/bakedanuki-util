# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

# maya
from maya.api import OpenMaya as om


ModifierKind = Literal["dg", "dag"]


@dataclass(frozen=True, slots=True)
class _ExecutedModifier:
    kind: ModifierKind
    modifier: om.MDGModifier | om.MDagModifier

    def do_it(self):
        self.modifier.doIt()

    def undo_it(self):
        self.modifier.undoIt()


class ModifierManager:
    """
    Manages MDGModifier / MDagModifier undo and redo as one command.

    Executed modifiers are kept as closed history entries. After a modifier is
    executed, a fresh modifier is prepared for subsequent operations.
    """

    __slots__ = (
        "_dg_mod",
        "_dag_mod",
        "_pending_dag_parents",
        "_done_stack",
        "_redo_stack",
    )

    def __init__(self):
        self._dg_mod = om.MDGModifier()
        self._dag_mod = om.MDagModifier()
        self._pending_dag_parents: dict[
            om.MObjectHandle, om.MObject
        ] = {}
        self._done_stack: list[_ExecutedModifier] = []
        self._redo_stack: list[_ExecutedModifier] = []

    @property
    def dg_mod(self) -> om.MDGModifier:
        return self._dg_mod

    @property
    def dag_mod(self) -> om.MDagModifier:
        return self._dag_mod

    @property
    def can_undo(self) -> bool:
        return bool(self._done_stack)

    @property
    def can_redo(self) -> bool:
        return bool(self._redo_stack)

    def do_it_dg(self):
        self._do_it("dg")

    def do_it_dag(self):
        self._do_it("dag")

    def undo_it(self):
        if not self._done_stack:
            raise RuntimeError("No modifier history to undo.")

        undone_modifiers: list[_ExecutedModifier] = []
        try:
            for executed_modifier in reversed(self._done_stack):
                executed_modifier.undo_it()
                undone_modifiers.append(executed_modifier)
        except Exception:
            self._redo_stack = []
            raise

        self._redo_stack = list(reversed(undone_modifiers))
        self._done_stack = []

    def redo_it(self):
        if not self._redo_stack:
            raise RuntimeError("No undone modifier history to redo.")
        if self._done_stack:
            raise RuntimeError("Cannot redo while modifier history is active.")

        redone_modifiers: list[_ExecutedModifier] = []
        try:
            for executed_modifier in self._redo_stack:
                executed_modifier.do_it()
                redone_modifiers.append(executed_modifier)
        except Exception:
            self._done_stack = redone_modifiers
            raise

        self._done_stack = redone_modifiers
        self._redo_stack = []

    def clear(self):
        self._dg_mod = om.MDGModifier()
        self._dag_mod = om.MDagModifier()
        self._pending_dag_parents = {}
        self._done_stack = []
        self._redo_stack = []

    def record_pending_dag_parent(
        self,
        node: om.MObject,
        parent: om.MObject,
    ) -> None:
        self._pending_dag_parents[om.MObjectHandle(node)] = parent

    def would_create_dag_cycle(
        self,
        node: om.MObject,
        parent: om.MObject,
    ) -> bool:
        if node == parent:
            return True
        if not self._pending_dag_parents:
            return om.MFnDagNode(node).isParentOf(parent)

        target = om.MObjectHandle(node)
        visited: set[om.MObjectHandle] = set()
        pending = [parent]

        while pending:
            current = pending.pop()
            if current.isNull():
                continue

            current_handle = om.MObjectHandle(current)
            if current_handle == target:
                return True
            if current_handle in visited:
                continue
            visited.add(current_handle)

            pending_parent = self._pending_dag_parents.get(current_handle)
            if pending_parent is not None:
                pending.append(pending_parent)
                continue

            fn_dag = om.MFnDagNode(current)
            for index in range(fn_dag.parentCount()):
                current_parent = fn_dag.parent(index)
                if not current_parent.hasFn(om.MFn.kWorld):
                    pending.append(current_parent)

        return False

    def _do_it(self, kind: ModifierKind):
        if kind == "dg":
            modifier = self._dg_mod
        elif kind == "dag":
            modifier = self._dag_mod
        else:
            raise ValueError(f"Unsupported modifier kind: {kind}")

        modifier.doIt()

        self._done_stack.append(_ExecutedModifier(kind, modifier))
        self._redo_stack = []
        self._replace_current_modifier(kind)

    def _replace_current_modifier(self, kind: ModifierKind):
        if kind == "dg":
            self._dg_mod = om.MDGModifier()
        elif kind == "dag":
            self._dag_mod = om.MDagModifier()
            self._pending_dag_parents = {}
        else:
            raise ValueError(f"Unsupported modifier kind: {kind}")
