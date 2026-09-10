# coding: utf-8
from __future__ import annotations

import weakref
from typing import Generic, Protocol, TypeVar, cast

from maya import cmds
from maya.api import OpenMaya as om

from ....ui.binding.float3 import Float3, Float3ViewModel
from ....ui.binding.float3.value import require_float3
from ....ui import FloatViewModel, qt
from ._float_plug_value import FloatPlugValue
from .float_plug import MayaFloatPlugStore
from .float_plug_resolver import MayaFloatPlug, resolve_float_plug
from .float3_plug_resolver import MayaFloat3Plug, require_float3_plug

_PlugT = TypeVar("_PlugT", bound=MayaFloat3Plug, covariant=True)


class _SetFloat3Attr(Protocol):
    """Maya command stubの可変長引数を3成分の型境界に限定する。"""

    def __call__(
        self, name: str, x: float, y: float, z: float, *, type: str
    ) -> None:
        """指定した型で親属性へ3成分を書き込む。"""
        raise NotImplementedError


class _ComponentPlugStore(MayaFloatPlugStore):
    """親属性への一括書き込み中の通知を抑止するscalar Store。"""

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        group: MayaFloat3PlugStore[MayaFloat3Plug],
    ) -> None:
        """グループの書き込み状態を参照して初期化する。"""
        self._group = group
        super().__init__(view_model, plug, group)

    def _callbacks_are_suppressed(self) -> bool:
        """一括書き込み完了後にまとめて表示を同期する。"""
        return self._group.is_writing or super()._callbacks_are_suppressed()


class MayaFloat3PlugStore(qt.QObject, Generic[_PlugT]):
    """3成分のMaya属性を正本として、各軸と親属性への編集を提供する。"""

    def __init__(
        self,
        view_model: Float3ViewModel,
        plug: _PlugT,
        owner: qt.QObject,
    ) -> None:
        """各軸のscalar StoreとcallbackをこのStoreの子として生成する。"""
        require_float3_plug(plug)
        super().__init__(owner)
        self._view_model_ref = weakref.ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._is_disposed = False
        self._write_depth = 0
        self._stores: list[MayaFloatPlugStore] = []
        self._codecs = tuple(
            FloatPlugValue(self._plug.child(i)) for i in range(3)
        )
        self._data_type = (
            "float3"
            if om.MFnNumericAttribute(self._plug.attribute()).numericType()
            == om.MFnNumericData.k3Float
            else "double3"
        )

        # 実際の子属性名からscalar Operatorを解決し、既存の通知・寿命管理を使う。
        try:
            for index, component in enumerate(
                (view_model.x, view_model.y, view_model.z)
            ):
                child_name = cast(
                    str,
                    om.MFnAttribute(self._plug.child(index).attribute()).name,
                )
                child = resolve_float_plug(
                    plug.node.cmd_access_name, child_name
                )
                self._stores.append(
                    _ComponentPlugStore(component, child, self)
                )
                component.set_value_command.can_execute_changed.connect(
                    self._on_component_state_changed
                )
        except Exception:
            self.dispose()
            raise

    @property
    def plug_operator(self) -> _PlugT:
        """入力した親plugを具体型のまま返す。"""
        return self._plug_operator

    @property
    def components(
        self,
    ) -> tuple[MayaFloatPlugStore, MayaFloatPlugStore, MayaFloatPlugStore]:
        """各軸の読み書きとcallbackを担当するStoreを返す。"""
        return self._stores[0], self._stores[1], self._stores[2]

    @property
    def is_disposed(self) -> bool:
        """同期を終了したか返す。"""
        return self._is_disposed or not qt.isValid(self)

    @property
    def is_writing(self) -> bool:
        """親属性への一括書き込み中か返す。"""
        return self._write_depth > 0

    @property
    def is_available(self) -> bool:
        """親と3つの子属性がすべて利用可能か返す。"""
        return (
            not self.is_disposed
            and self._attribute_handle.isValid()
            and len(self._stores) == 3
            and all(store.is_available for store in self._stores)
        )

    @property
    def is_writable(self) -> bool:
        """全成分と親属性への書き込みが許可されているか返す。"""
        return (
            self.is_available
            and bool(om.MFnAttribute(self._plug.attribute()).writable)
            and all(store.is_writable for store in self._stores)
        )

    def read(self) -> Float3:
        """各軸の実値を公開単位のtupleで返す。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya 3成分plugは利用できません")
        return require_float3(tuple(codec.read() for codec in self._codecs))

    def write(self, value: Float3) -> Float3:
        """一括変更の確定値を同期し、通知先からの再編集も読み直す。"""
        self._write_depth += 1
        try:
            actual = self._write_plug(value)
        finally:
            self._write_depth -= 1
        self.refresh()
        return self.read() if self.is_available else actual

    def refresh(self) -> bool:
        """構築時のViewModelが接続中の場合だけ正本を再同期する。"""
        view_model = self._view_model_ref()
        if view_model is None or view_model.is_disposed:
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        return view_model.refresh()

    def _write_plug(self, value: Float3) -> Float3:
        """全成分を事前検証し、1回のsetAttrでUndo可能な一括設定を行う。"""
        values = require_float3(value)
        if not self.is_writable:
            raise RuntimeError("同期対象のMaya 3成分plugへ書き込めません")

        # 親setAttrは子のhard limitを適用しないため、全成分を先に検証する。
        ui_values: list[float] = []
        for codec, component in zip(self._codecs, values):
            presentation = codec.presentation
            if (
                presentation.minimum is not None
                and component < presentation.minimum
            ):
                raise ValueError("valueはMaya属性の下限未満です")
            if (
                presentation.maximum is not None
                and component > presentation.maximum
            ):
                raise ValueError("valueはMaya属性の上限を超えています")
            ui_values.append(codec.to_ui(component))
        before = self.read()
        if tuple(ui_values) == tuple(
            codec.to_ui(v) for codec, v in zip(self._codecs, before)
        ):
            return before

        # 親属性への1回の書き込みで、Undoと3成分の確定をまとめる。
        set_attr = cast(_SetFloat3Attr, cmds.setAttr)
        path = self._plug.partialName(
            useFullAttributePath=True, useLongNames=True
        )
        set_attr(
            f"{self._plug_operator.node.cmd_access_name}.{path}",
            *ui_values,
            type=self._data_type,
        )
        return self.read()

    def dispose(self) -> None:
        """所有する全成分のMaya callbackを即座に解除する。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        for store in self._stores:
            if qt.isValid(store):
                store.dispose()

    @qt.Slot(bool)
    def _on_component_state_changed(self, _enabled: bool) -> None:
        """成分の削除や同期終了を検出し、残りのcallbackも解除する。"""
        if not self.is_disposed and any(
            store.is_disposed for store in self._stores
        ):
            self.dispose()
