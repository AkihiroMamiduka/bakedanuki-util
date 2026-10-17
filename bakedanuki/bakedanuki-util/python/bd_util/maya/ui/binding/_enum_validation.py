# coding: utf-8
"""一括値入力と値Pasteで共有するenum定義の検証方針。"""

from collections.abc import Callable, Generator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Literal, Protocol

from ....ui import EnumDefinition
from ._enum_plug_value import EnumPlugValue


class EnumValidationTarget(Protocol):
    """削除履歴も含む属性実体の可用性を提供する。"""

    @property
    def is_available(self) -> bool:
        """操作開始時と同じ属性が利用できるか返す。"""
        raise NotImplementedError


class EnumValidationCodec(Protocol):
    """一括操作中だけ比較元のenum定義を固定するcodec契約。"""

    value: EnumPlugValue
    operation_definition: EnumDefinition | None


@dataclass(frozen=True)
class EnumOperationSnapshot:
    """開始時の定義と可用性を保持し、終了時の全対象を確認する。"""

    definition: EnumDefinition
    available: tuple[bool, ...]

    def validate(
        self,
        targets: Sequence[EnumValidationTarget],
        read_definitions: Callable[[], Sequence[EnumDefinition | None]],
    ) -> None:
        """削除済みplugを読む前に消失を拒否し、残存する全定義を照合する。"""
        if not targets[0].is_available or any(
            available and not target.is_available
            for target, available in zip(targets, self.available, strict=True)
        ):
            raise RuntimeError("入力中に対象属性が削除されました")
        if any(
            definition is not None and not self.definition.matches(definition)
            for definition in read_definitions()
        ):
            raise ValueError("入力中に対象のenum定義が変わりました")


@contextmanager
def enum_operation_validation(
    targets: Sequence[EnumValidationTarget],
    codecs: Sequence[EnumValidationCodec],
    read_definitions: Callable[[], Sequence[EnumDefinition | None]],
) -> Generator[EnumOperationSnapshot, None, None]:
    """表示用と一時Storeで同じ開始時照合と操作終了後の解除を行う。"""
    if any(codec.operation_definition is not None for codec in codecs):
        raise RuntimeError("enumの一括検証中に別の操作は開始できません")
    if not targets[0].is_available:
        raise RuntimeError("代表のMaya属性は利用できません")
    definitions = read_definitions()
    representative = definitions[0]
    if representative is None or any(
        definition is not None and not representative.matches(definition)
        for definition in definitions[1:]
    ):
        raise ValueError("全対象のenum定義（整数値と項目名）を揃えてください")
    snapshot = EnumOperationSnapshot(
        representative, tuple(target.is_available for target in targets)
    )
    for codec in codecs:
        codec.operation_definition = representative
    try:
        yield snapshot
    finally:
        for codec in codecs:
            codec.operation_definition = None


def require_enum_validation(
    value: object,
) -> Literal["per_write", "operation"]:
    """動的呼出しからも既知のenum検証方針だけを受け付ける。"""
    if value == "per_write":
        return "per_write"
    if value == "operation":
        return "operation"
    raise ValueError("enum_validationにはper_writeまたはoperationを指定します")
