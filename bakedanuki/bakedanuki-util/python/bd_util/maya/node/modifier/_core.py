# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal

# maya
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

ModifierKind = Literal["dg", "dag"]


@dataclass(slots=True)
class _ModifierStep:
    modifier: om.MDGModifier | om.MDagModifier
    callback: Callable[[om.MDGModifier], None] | None = None

    def do_it(self) -> None:
        try:
            if self.callback is not None:
                self.callback(self.modifier)
        finally:
            self.callback = None
        self.modifier.doIt()

    def redo_it(self) -> None:
        self.modifier.doIt()

    def undo_it(self) -> None:
        self.modifier.undoIt()


@dataclass(slots=True)
class _AnimCurveStep:
    callback: Callable[[oma.MAnimCurveChange], None] | None
    change: oma.MAnimCurveChange

    def do_it(self) -> None:
        if self.callback is None:
            raise RuntimeError("An animation edit cannot execute twice.")
        try:
            self.callback(self.change)
        finally:
            self.callback = None

    def redo_it(self) -> None:
        self.change.redoIt()

    def undo_it(self) -> None:
        self.change.undoIt()


_Step = _ModifierStep | _AnimCurveStep


@dataclass(frozen=True, slots=True)
class _ExecutedBatch:
    kind: ModifierKind
    steps: tuple[_Step, ...]

    def do_it(self) -> None:
        self._run(redo=False)

    def redo_it(self) -> None:
        self._run(redo=True)

    def _run(self, *, redo: bool) -> None:
        attempted: list[_Step] = []
        try:
            for step in self.steps:
                attempted.append(step)
                if redo:
                    step.redo_it()
                else:
                    step.do_it()
        except Exception as error:
            for step in reversed(attempted):
                try:
                    step.undo_it()
                except Exception as rollback_error:
                    error.add_note(
                        f"Failed operation rollback also failed: {rollback_error!r}"
                    )
            raise

    def undo_it(self) -> None:
        errors: list[Exception] = []
        for step in reversed(self.steps):
            try:
                step.undo_it()
            except Exception as error:
                errors.append(error)
        if errors:
            first_error = errors[0]
            for error in errors[1:]:
                first_error.add_note(
                    f"Another operation undo also failed: {error!r}"
                )
            raise first_error


class ModifierManager:
    """
    Manages DG, DAG and animation edits as one undoable command.

    Each explicit execution closes one history entry. Deferred DG and animation
    callbacks split pending operations into ordered steps without executing them.
    """

    __slots__ = (
        "_dg_mod",
        "_dag_mod",
        "_pending_dg_steps",
        "_pending_dag_parents",
        "_done_stack",
        "_redo_stack",
    )

    def __init__(self):
        self._dg_mod = om.MDGModifier()
        self._dag_mod = om.MDagModifier()
        self._pending_dg_steps: list[_Step] = []
        self._pending_dag_parents: dict[om.MObjectHandle, om.MObject] = {}
        self._done_stack: list[_ExecutedBatch] = []
        self._redo_stack: list[_ExecutedBatch] = []

    @property
    def dg_mod(self) -> om.MDGModifier:
        """Current DG buffer; reacquire after queuing a deferred callback."""
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

    def queue_anim_curve_change(
        self, callback: Callable[[oma.MAnimCurveChange], None]
    ) -> None:
        """Queue an API animation edit at the current DG execution position.

        The callback runs once during ``do_it_dg()``. All its mutations must
        use the supplied change cache so undo, redo and failure recovery can
        restore them. Node creation and other DG edits must be queued separately.
        Queuing an edit replaces ``dg_mod`` but does not execute pending work.
        """
        if not callable(callback):
            raise TypeError("Animation edit callback must be callable.")
        self._queue_dg_step(_AnimCurveStep(callback, oma.MAnimCurveChange()))

    def queue_dg_modifier(
        self, callback: Callable[[om.MDGModifier], None]
    ) -> None:
        """Defer preparing and executing a DG modifier until ``do_it_dg()``.

        The callback runs once after earlier DG steps have executed. It must
        only queue changes on the supplied modifier, without calling ``doIt``.
        Undo and redo use that modifier; the callback is not replayed.
        Queuing replaces ``dg_mod`` without executing pending work.
        """
        if not callable(callback):
            raise TypeError("DG modifier callback must be callable.")
        self._queue_dg_step(_ModifierStep(om.MDGModifier(), callback))

    def _queue_dg_step(self, step: _Step) -> None:
        self._pending_dg_steps.extend((_ModifierStep(self._dg_mod), step))
        self._dg_mod = om.MDGModifier()

    def do_it_dg(self):
        self._do_it("dg")

    def do_it_dag(self):
        self._do_it("dag")

    def undo_it(self):
        if not self._done_stack:
            raise RuntimeError("No modifier history to undo.")

        undone_modifiers: list[_ExecutedBatch] = []
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

        redone_modifiers: list[_ExecutedBatch] = []
        for executed_modifier in self._redo_stack:
            try:
                executed_modifier.redo_it()
            except Exception:
                self._done_stack = redone_modifiers
                self._clear_pending_modifiers()
                self._redo_stack = []
                raise
            redone_modifiers.append(executed_modifier)

        self._done_stack = redone_modifiers
        self._redo_stack = []

    def rollback(self) -> None:
        """Undo executed history and discard all pending command state.

        Unlike ``undo_it()``, rollback is terminal. It also clears pending
        modifiers and does not retain redo history. Every executed modifier is
        given a chance to undo even if an earlier undo operation fails.
        """
        errors: list[Exception] = []
        try:
            for executed_modifier in reversed(self._done_stack):
                try:
                    executed_modifier.undo_it()
                except Exception as error:
                    errors.append(error)
        finally:
            self.clear()

        if errors:
            first_error = errors[0]
            for error in errors[1:]:
                first_error.add_note(
                    f"Another modifier rollback also failed: {error!r}"
                )
            raise first_error

    def clear(self):
        self._clear_pending_modifiers()
        self._done_stack = []
        self._redo_stack = []

    def _clear_pending_modifiers(self):
        self._dg_mod = om.MDGModifier()
        self._dag_mod = om.MDagModifier()
        self._pending_dg_steps = []
        self._pending_dag_parents = {}

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
            steps = (*self._pending_dg_steps, _ModifierStep(self._dg_mod))
        elif kind == "dag":
            steps = (_ModifierStep(self._dag_mod),)
        else:
            raise ValueError(f"Unsupported modifier kind: {kind}")

        batch = _ExecutedBatch(kind, steps)
        try:
            batch.do_it()
        except Exception:
            self._clear_pending_modifiers()
            self._redo_stack = []
            raise

        self._done_stack.append(batch)
        self._redo_stack = []
        self._replace_current_modifier(kind)

    def _replace_current_modifier(self, kind: ModifierKind):
        if kind == "dg":
            self._dg_mod = om.MDGModifier()
            self._pending_dg_steps = []
        elif kind == "dag":
            self._dag_mod = om.MDagModifier()
            self._pending_dag_parents = {}
        else:
            raise ValueError(f"Unsupported modifier kind: {kind}")
