# coding: utf-8
from typing import Protocol, cast
from weakref import ReferenceType, ref

_REFERENCE_ATTRIBUTE = "_bd_util_maya_float_plug_view_reference"


class FloatMayaView(Protocol):
    """単一値・3成分で共通のMaya View接続枠に必要な状態。"""

    @property
    def is_disposed(self) -> bool:
        """Maya Viewが終了しているか返す。"""
        raise NotImplementedError


def require_view_slot(view_model: object, view_name: str) -> None:
    """同じ値に複数のMaya Viewを接続してUndoと表示単位を競合させない。"""
    reference = cast(
        ReferenceType[FloatMayaView] | None,
        getattr(view_model, _REFERENCE_ATTRIBUTE, None),
    )
    current = reference() if reference is not None else None
    if current is not None and not current.is_disposed:
        raise RuntimeError(f"同じViewModelへ複数の{view_name}を接続できません")


def claim_view_slot(view_model: object, view: FloatMayaView) -> None:
    """Maya Viewの弱参照を接続枠へ登録する。"""
    setattr(view_model, _REFERENCE_ATTRIBUTE, ref(view))


def release_view_slot(view_model: object, view: FloatMayaView) -> bool:
    """自身が保持している接続枠だけを解放する。"""
    reference = cast(
        ReferenceType[FloatMayaView] | None,
        getattr(view_model, _REFERENCE_ATTRIBUTE, None),
    )
    if reference is not None and reference() is view:
        delattr(view_model, _REFERENCE_ATTRIBUTE)
        return True
    return False
