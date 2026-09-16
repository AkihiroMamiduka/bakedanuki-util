# coding: utf-8
"""同じ値を複数のMaya属性へ明示入力するMVVMの公開入口。"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import replace
from typing import Generic, TypeVar

from maya.api import OpenMaya as om

from ....ui import (
    BoolBinding,
    BoolViewModel,
    EnumBinding,
    EnumDefinition,
    EnumViewModel,
    FloatBinding,
    FloatPresentation,
    FloatViewModel,
    qt,
)
from ....ui.binding.enum._connection import connect_queued_qt_signal
from ....ui.binding.enum.definition import require_enum_value
from ...node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from ._float_plug_value import FloatPlugValue
from ._enum_plug_value import EnumPlugValue
from ._plugs_store import PlugsStore, PlugTarget
from .float_plug_resolver import MayaFloatPlug, require_float_plug
from .enum_plug_resolver import MayaEnumPlug, require_enum_plug
from .plugs_state import MayaPlugTargetState

__all__ = [
    "MayaBoolPlugsBinding",
    "MayaFloatPlugsBinding",
    "MayaEnumPlugsBinding",
]

_ValueT = TypeVar("_ValueT", bool, float, int)


class _BoolCodec:
    """scalar boolと、配列配下ではないcompound子を読み書きする。"""

    def __init__(self, plug: object) -> None:
        """実体の型と祖先を検証し、単一boolの参照を保持する。"""
        if not isinstance(plug, BoolPlugOperator):
            raise TypeError("plugsにはbool用PlugOperatorを指定してください")
        self.plug = plug.plug
        attribute = self.plug.attribute()
        if self.plug.isCompound or not attribute.hasFn(
            om.MFn.kNumericAttribute
        ):
            raise TypeError("単一bool属性を指定してください")
        if (
            om.MFnNumericAttribute(attribute).numericType()
            != om.MFnNumericData.kBoolean
        ):
            raise TypeError("単一bool属性を指定してください")
        ancestor = self.plug
        while True:
            if ancestor.isArray or ancestor.isElement:
                raise TypeError("配列配下の属性には対応していません")
            if not ancestor.isChild:
                break
            ancestor = ancestor.parent()

    def read(self) -> bool:
        """正本のboolを読み取る。"""
        return self.plug.asBool()

    def to_ui(self, value: bool) -> bool:
        """暗黙のtruthiness変換を使わずboolだけを受け付ける。"""
        if type(value) is not bool:
            raise TypeError("valueにはboolを指定してください")
        return value

    def validate(self, value: bool) -> bool:
        """bool入力を検証する。"""
        return self.to_ui(value)


class _FloatCodec:
    """既存のfloat単位変換に一括入力前のhard limit検証を加える。"""

    def __init__(self, plug: MayaFloatPlug) -> None:
        """scalar floatの型と単位種別を検証する。"""
        self.value = FloatPlugValue(require_float_plug(plug).plug)

    def read(self) -> float:
        """公開単位で正本を読み取る。"""
        return self.value.read()

    def to_ui(self, value: float) -> float:
        """復旧値を含め、公開値をMayaの現在単位へ変換する。"""
        return self.value.to_ui(value)

    def validate(self, value: float) -> float:
        """hard limitと格納精度を変更前に検証する。"""
        result = self.to_ui(value)
        presentation = self.value.presentation
        if presentation.minimum is not None and value < presentation.minimum:
            raise ValueError("入力値は対象属性の下限未満です")
        if presentation.maximum is not None and value > presentation.maximum:
            raise ValueError("入力値は対象属性の上限を超えています")
        return result


class _EnumCodec:
    """読み取り・復旧は未定義値も保持し、新規入力だけを定義内に制限する。"""

    def __init__(self, plug: MayaEnumPlug) -> None:
        self.value = EnumPlugValue(require_enum_plug(plug).plug)

    def read(self) -> int:
        return self.value.read()

    def to_ui(self, value: int) -> int:
        return require_enum_value(value)

    def validate(self, value: int) -> int:
        value = self.to_ui(value)
        self.value.definition.require_value(value)
        return value


class _EnumPlugsStore(PlugsStore[int]):
    """定義が揃ったenum属性群の代表値と一括入力を提供する。"""

    def __init__(
        self,
        view_model: EnumViewModel,
        plugs: Sequence[MayaEnumPlug],
        owner: qt.QObject,
    ) -> None:
        self._view_model = view_model
        self._codecs = tuple(_EnumCodec(plug) for plug in plugs)
        if not self._codecs:
            raise ValueError("plugsには一つ以上の属性を指定してください")
        definition = self._codecs[0].value.definition
        if any(
            not definition.matches(codec.value.definition)
            for codec in self._codecs[1:]
        ):
            raise ValueError(
                "全対象のenum定義（整数値と項目名）を揃えてください"
            )
        self._definitions: tuple[EnumDefinition | None, ...] = ()
        targets = tuple(
            PlugTarget(plug.node, plug.plug, codec)
            for plug, codec in zip(plugs, self._codecs)
        )
        super().__init__(targets, owner)
        view_model.disposed.connect(self.dispose)
        connect_queued_qt_signal(view_model.destroyed, self.dispose)

    @property
    def definition(self) -> EnumDefinition:
        if not self.is_available:
            raise RuntimeError("代表属性は利用できません")
        return self._codecs[0].value.definition

    def _current_definitions(self) -> tuple[EnumDefinition | None, ...]:
        return tuple(
            codec.value.definition if target.is_available else None
            for target, codec in zip(self._targets, self._codecs)
        )

    def _definitions_match(self) -> bool:
        definitions = self._current_definitions()
        representative = definitions[0]
        return representative is not None and all(
            definition is None or representative.matches(definition)
            for definition in definitions[1:]
        )

    @property
    def is_writable(self) -> bool:
        return super().is_writable and self._definitions_match()

    def _validate_write_target(
        self, target: PlugTarget[int], requested: int
    ) -> None:
        super()._validate_write_target(target, requested)
        if not self._definitions_match():
            raise ValueError("入力中に対象のenum定義が変わりました")
        target.codec.validate(requested)

    def _read_state(self) -> bool:
        definitions = self._current_definitions()
        representative = definitions[0]
        states: list[MayaPlugTargetState] = []
        for target, definition in zip(self._targets, definitions):
            state = target.state()
            if (
                representative is not None
                and definition is not None
                and not representative.matches(definition)
            ):
                state = replace(
                    state,
                    is_writable=False,
                    reason="代表属性とenum定義（整数値と項目名）が一致しません",
                )
            states.append(state)
        values = tuple(
            target.codec.read() if state.is_available else None
            for target, state in zip(self._targets, states)
        )
        changed = (
            definitions != self._definitions
            or tuple(states) != self._states
            or values != self._values
        )
        self._definitions = definitions
        self._states = tuple(states)
        self._values = values
        return changed

    def _refresh_view_model(self) -> bool:
        view_model = self._view_model
        if view_model.is_disposed:
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        return view_model.refresh_from_store(self)

    def _validate_attached_view_model(self, view_model: EnumViewModel) -> None:
        if view_model is not self._view_model:
            raise ValueError("構築時のEnumViewModelへ接続してください")

    def dispose(self) -> None:
        super().dispose()
        view_model = self._view_model
        if not view_model.is_disposed and view_model.store is self:
            view_model.store_became_unavailable(self)


class _BoolPlugsStore(PlugsStore[bool]):
    """bool属性群の代表値と一括入力を対応ViewModelへ提供する。"""

    def __init__(
        self,
        view_model: BoolViewModel,
        plugs: Sequence[BoolPlugOperator],
        owner: qt.QObject,
    ) -> None:
        """全属性を検証してから監視を開始する。"""
        self._view_model = view_model
        targets = tuple(
            PlugTarget(plug.node, plug.plug, _BoolCodec(plug))
            for plug in plugs
        )
        super().__init__(targets, owner)

    def _refresh_view_model(self) -> bool:
        """代表と編集可否を同期し、削除時は入力を停止する。"""
        view_model = self._view_model
        if not qt.isValid(view_model) or view_model.is_disposed:
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        return view_model.refresh_from_store(self)


class _FloatPlugsStore(PlugsStore[float]):
    """同種単位の属性群を一つのfloat入力として提供する。"""

    def __init__(
        self,
        view_model: FloatViewModel,
        plugs: Sequence[MayaFloatPlug],
        owner: qt.QObject,
    ) -> None:
        """単位種別を揃え、代表の表示情報を維持する。"""
        self._view_model = view_model
        codecs = tuple(_FloatCodec(plug) for plug in plugs)
        if not codecs:
            raise ValueError("plugsには一つ以上の属性を指定してください")
        if any(codec.value.kind != codecs[0].value.kind for codec in codecs):
            raise TypeError("属性の単位種別は全対象で揃えてください")
        self._representative_codec = codecs[0]
        targets = tuple(
            PlugTarget(plug.node, plug.plug, codec)
            for plug, codec in zip(plugs, codecs)
        )
        super().__init__(targets, owner, float_view_model=view_model)

    @property
    def presentation(self) -> FloatPresentation:
        """代表属性の範囲・表示単位を維持して実値の表示を保つ。"""
        if not self.is_available:
            raise RuntimeError("代表属性は利用できません")
        return self._representative_codec.value.presentation

    def _refresh_view_model(self) -> bool:
        """代表属性の単位、実値、入力可否を同期する。"""
        view_model = self._view_model
        if not qt.isValid(view_model) or view_model.is_disposed:
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        if not self.is_available or not self.is_writable:
            view_model.end_edit()
        return view_model.refresh_from_store(self)


class _BoolPlugsViewModel(BoolViewModel):
    """代表との同値判定を行わず、属性群が入力差分を判断する。"""

    def _request_value(self, value: bool) -> bool:
        """ユーザーCommandだけを一括入力へ渡す。"""
        store = self.store
        if self.is_disposed or not isinstance(store, _BoolPlugsStore):
            return False
        return store.request_value(value)


class _FloatPlugsViewModel(FloatViewModel):
    """代表と同値の明示入力も、他対象の差分があれば適用する。"""

    def _request_value(self, value: float) -> bool:
        """Viewの連続編集状態を維持して一括入力を実行する。"""
        store = self.store
        if self.is_disposed or not isinstance(store, _FloatPlugsStore):
            return False
        return store.request_value(value)


class _EnumPlugsViewModel(EnumViewModel):
    """代表と同値の入力でも、後続対象の差分を適用する。"""

    def _request_value(self, value: int) -> bool:
        store = self.store
        if self.is_disposed or not isinstance(store, _EnumPlugsStore):
            return False
        return store.request_value(value)


class _PlugsBindingState(Generic[_ValueT]):
    """複数プラグの公開集約状態を同じ名前で提供する。"""

    _owned_group: PlugsStore[_ValueT] | None

    @property
    def _group(self) -> PlugsStore[_ValueT]:
        """構築済みの集約Storeを取得する。"""
        if self._owned_group is None:
            raise RuntimeError("属性群のBindingはまだ構築されていません")
        return self._owned_group

    @property
    def is_mixed(self) -> bool:
        """利用可能な対象の確定値が異なるか返す。"""
        return self._group.is_mixed

    @property
    def target_count(self) -> int:
        """入力対象として登録した属性数を返す。"""
        return self._group.target_count

    @property
    def writable_count(self) -> int:
        """個別に書込み可能な対象数を返す。"""
        return self._group.writable_count

    @property
    def target_states(self) -> tuple[MayaPlugTargetState, ...]:
        """代表を先頭とした全対象の状態と除外理由を返す。"""
        return self._group.target_states

    @property
    def state_changed(self) -> qt.QtCore.SignalInstance:
        """混在状態・対象値・編集可否の変更を引数なしで通知する。"""
        return self._group.state_changed

    @property
    def edit_failed(self) -> qt.QtCore.SignalInstance:
        """入力拒否・適用失敗の理由を文字列で通知する。"""
        return self._group.edit_failed


class MayaBoolPlugsBinding(
    _PlugsBindingState[bool], BoolBinding[_BoolPlugsStore]
):
    """複数のMaya bool属性を既存のBool Viewへ接続する。"""

    def __init__(
        self,
        plugs: Sequence[BoolPlugOperator],
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """対象順を固定し、先頭の実値を表示する。書込みは行わない。"""
        self._owned_group = None

        def create_store(view_model: BoolViewModel) -> _BoolPlugsStore:
            """専用ViewModelと同じ寿命の集約Storeを生成する。"""
            store = _BoolPlugsStore(view_model, plugs, self)
            self._owned_group = store
            return store

        self._initialize(create_store, parent=parent)

    def _create_view_model(self) -> BoolViewModel:
        """属性群専用の入力判定を使用する。"""
        return _BoolPlugsViewModel(parent=self)

    def apply_representative_value(self) -> bool:
        """代表の現在の実値を、編集可能な対象へ明示的に揃える。"""
        return self.set_value(self.store.read())

    def refresh(self) -> bool:
        """全対象の状態と代表値を、書込みなしで同期する。"""
        self._require_active()
        return self.store.refresh()

    def dispose(self) -> None:
        """所有する全callbackを解除して入力を停止する。"""
        try:
            if self._owned_group is not None:
                self._owned_group.dispose()
        finally:
            super().dispose()


class MayaFloatPlugsBinding(
    _PlugsBindingState[float], FloatBinding[_FloatPlugsStore]
):
    """同種単位の複数Maya属性を既存のFloat Viewへ接続する。"""

    def __init__(
        self,
        plugs: Sequence[MayaFloatPlug],
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        """全対象を検証し、値を書き戻さず初期表示する。"""
        self._owned_group = None

        def create_store(view_model: FloatViewModel) -> _FloatPlugsStore:
            """連続編集と監視を共有する集約Storeを生成する。"""
            store = _FloatPlugsStore(view_model, plugs, self)
            self._owned_group = store
            return store

        self._initialize(create_store, parent=parent)

    def _create_view_model(self) -> FloatViewModel:
        """属性群専用の同値判定を使用する。"""
        return _FloatPlugsViewModel(parent=self)

    def apply_representative_value(self) -> bool:
        """代表の未丸め実値を、編集可能な対象へ明示的に揃える。"""
        return self.set_value(self.store.read())

    def refresh(self) -> bool:
        """全対象の値・状態を、書込みなしで再取得する。"""
        self._require_active()
        return self.store.refresh()

    def dispose(self) -> None:
        """開いているUndoと全callbackを解除して入力を停止する。"""
        try:
            if self._owned_group is not None:
                self._owned_group.dispose()
        finally:
            super().dispose()


class MayaEnumPlugsBinding(
    _PlugsBindingState[int], EnumBinding[_EnumPlugsStore]
):
    """同じ定義の複数Maya enum属性を既存のEnum Viewへ接続する。"""

    def __init__(
        self,
        plugs: Sequence[MayaEnumPlug],
        *,
        parent: qt.QObject | None = None,
    ) -> None:
        self._owned_group = None

        def create_store(view_model: EnumViewModel) -> _EnumPlugsStore:
            store = _EnumPlugsStore(view_model, plugs, self)
            self._owned_group = store
            return store

        self._initialize(create_store, parent=parent)

    def _create_view_model(self) -> EnumViewModel:
        return _EnumPlugsViewModel(parent=self)

    def apply_representative_value(self) -> bool:
        """代表の実値を編集可能な対象へ揃える。未定義値は拒否する。"""
        return self.set_value(self.store.read())

    def refresh(self) -> bool:
        """全対象の定義・状態・代表値を、書込みなしで読み直す。"""
        self._require_active()
        return self.store.refresh()

    def dispose(self) -> None:
        try:
            if self._owned_group is not None:
                self._owned_group.dispose()
        finally:
            super().dispose()
