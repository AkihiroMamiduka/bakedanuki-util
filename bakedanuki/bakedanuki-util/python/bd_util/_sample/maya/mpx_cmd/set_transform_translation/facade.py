# coding: utf-8
from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, cast

from maya import cmds

from .....maya.value import DoubleLinear3
from .._plugin import ensure_sample_commands_plugin_loaded
from .mpx_command import SetTransformTranslationCommand
from .operation import SetTransformTranslationResult


class _SetTransformTranslationCallable(Protocol):
    def __call__(
        self,
        *,
        nodeName: str,
        translateX: float,
        translateY: float,
        translateZ: float,
    ) -> object: ...


def set_transform_translation(
    *,
    node_name: str,
    translation: Sequence[float],
) -> SetTransformTranslationResult:
    """Set a local translation through the registered undoable command."""
    translation_value = _coerce_translation(translation)
    ensure_sample_commands_plugin_loaded()

    command = cast(
        _SetTransformTranslationCallable,
        getattr(cmds, SetTransformTranslationCommand.COMMAND_NAME),
    )
    raw_result = command(
        nodeName=node_name,
        translateX=translation_value.x,
        translateY=translation_value.y,
        translateZ=translation_value.z,
    )
    return SetTransformTranslationResult(
        node_name=_decode_node_name(raw_result),
        translation=translation_value,
    )


def _coerce_translation(translation: Sequence[float]) -> DoubleLinear3:
    if isinstance(translation, (str, bytes)) or len(translation) != 3:
        raise ValueError("translation must contain exactly 3 values.")
    try:
        return DoubleLinear3(
            float(translation[0]),
            float(translation[1]),
            float(translation[2]),
        )
    except (TypeError, ValueError) as error:
        raise TypeError("translation values must be numeric.") from error


def _decode_node_name(raw_result: object) -> str:
    if isinstance(raw_result, str):
        return raw_result
    if (
        isinstance(raw_result, (list, tuple))
        and len(raw_result) == 1
        and isinstance(raw_result[0], str)
    ):
        return raw_result[0]
    raise TypeError(
        "Unexpected bduSampleSetTransformTranslation result: "
        f"{raw_result!r}"
    )
