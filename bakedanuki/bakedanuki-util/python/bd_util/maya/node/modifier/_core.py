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


@dataclass(slots=True)
class _DeferredBatchStep:
    callback: Callable[[ModifierManager], None] | None
    manager: ModifierManager | None = None

    def do_it(self) -> None:
        if self.callback is None:
            raise RuntimeError("A deferred batch cannot execute twice.")
        self.manager = ModifierManager()
        try:
            self.callback(self.manager)
            self.manager.do_it_dg()
        except Exception as error:
            try:
                self.manager.rollback()
            except Exception as rollback_error:
                error.add_note(
                    f"Deferred batch rollback also failed: {rollback_error!r}"
                )
            raise
        finally:
            self.callback = None

    def redo_it(self) -> None:
        if self.manager is None:
            raise RuntimeError("The deferred batch has not executed.")
        self.manager.redo_it()

    def undo_it(self) -> None:
        if self.manager is not None and self.manager.can_undo:
            self.manager.undo_it()


_Step = _ModifierStep | _AnimCurveStep | _DeferredBatchStep


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
    """DG・DAG・アニメーション編集を予約し、実行履歴を管理する。

    ``do_it_dg()`` / ``do_it_dag()`` ごとに履歴を確定する。予約した操作は
    実行までシーンに反映されない。
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
        """現在の DG modifier。遅延処理の予約後は取得し直す。"""
        return self._dg_mod

    @property
    def dag_mod(self) -> om.MDagModifier:
        """現在の DAG modifier。"""
        return self._dag_mod

    @property
    def can_undo(self) -> bool:
        """確定した操作の履歴があるか。"""
        return bool(self._done_stack)

    @property
    def can_redo(self) -> bool:
        """やり直し可能な履歴があるか。"""
        return bool(self._redo_stack)

    def queue_anim_curve_change(
        self, callback: Callable[[oma.MAnimCurveChange], None]
    ) -> None:
        """アニメーション編集を現在の DG 実行位置に予約する。

        callback は ``do_it_dg()`` 時に一度だけ呼ばれる。予約後は
        ``dg_mod`` が切り替わるため、必要なら取得し直す。

        Args:
            callback: 実行時に MAnimCurveChange を受け取る処理。
                編集には渡された変更履歴を使い、ノード作成は別に予約する。
        """
        if not callable(callback):
            raise TypeError("Animation edit callback must be callable.")
        self._queue_dg_step(_AnimCurveStep(callback, oma.MAnimCurveChange()))

    def queue_dg_modifier(
        self, callback: Callable[[om.MDGModifier], None]
    ) -> None:
        """先行する DG 操作の実行後に modifier を準備する。

        callback は ``do_it_dg()`` 時に一度だけ呼ばれる。Undo / Redo
        には完成した modifier を使う。予約後は ``dg_mod`` を取得し直す。

        Args:
            callback: 実行時に MDGModifier を受け取る処理。
                変更の予約だけを行い、``doIt()`` は呼ばない。
        """
        if not callable(callback):
            raise TypeError("DG modifier callback must be callable.")
        self._queue_dg_step(_ModifierStep(om.MDGModifier(), callback))

    def _queue_dg_step(self, step: _Step) -> None:
        self._pending_dg_steps.extend((_ModifierStep(self._dg_mod), step))
        self._dg_mod = om.MDGModifier()

    def queue_dg_batch(
        self, callback: Callable[[ModifierManager], None]
    ) -> None:
        """実行時のシーンに応じた複合操作を一つの履歴へ予約する。

        Undo / Redo には初回実行時に構築した履歴を使う。

        Args:
            callback: 実行時に新しい ModifierManager を受け取る処理。
                操作の予約だけを行い、即時編集や ``do_it_dg()`` は行わない。
        """
        if not callable(callback):
            raise TypeError("DG batch callback must be callable.")
        self._queue_dg_step(_DeferredBatchStep(callback))

    def do_it_dg(self):
        """予約済み DG・アニメーション操作を実行して履歴に確定する。"""
        self._do_it("dg")

    def do_it_dag(self):
        """予約済み DAG 操作を実行して履歴に確定する。"""
        self._do_it("dag")

    def undo_it(self):
        """確定済みの履歴を新しいものから順に取り消す。

        Raises:
            RuntimeError: 取り消せる履歴がない場合。
        """
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
        """取り消した履歴を元の順で再実行する。

        Raises:
            RuntimeError: やり直せる履歴がない、または実行履歴が残る場合。
        """
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
        """確定済み操作を取り消し、未実行の予約も破棄する。

        ``undo_it()`` と異なりやり直し履歴は残さない。途中で失敗しても
        残りの確定済み操作の取り消しを試みる。
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
        """予約中・確定済み・やり直し待ちの履歴をすべて破棄する。"""
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
        # 予約済み操作を 1 履歴にまとめ、失敗時は batch 内で元に戻す。
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
