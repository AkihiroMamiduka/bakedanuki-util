# coding: utf-8
from __future__ import annotations

from typing import Protocol, cast

from maya import cmds

from .._plugin import ensure_sample_commands_plugin_loaded
from .mpx_command import CreateTransformsCommand
from .operation import CreateTransformsResult


class _CreateTransformsCallable(Protocol):
    def __call__(
        self,
        *,
        prefix: str,
        count: int,
    ) -> object: ...


def create_transforms(
    *,
    prefix: str = "bduSample",
    count: int = 2,
) -> CreateTransformsResult:
    """Create transforms through the registered undoable Maya command."""
    ensure_sample_commands_plugin_loaded()

    command = cast(
        _CreateTransformsCallable,
        getattr(cmds, CreateTransformsCommand.COMMAND_NAME),
    )
    raw_result = command(prefix=prefix, count=count)
    return CreateTransformsResult(node_names=_decode_node_names(raw_result))


def _decode_node_names(raw_result: object) -> tuple[str, ...]:
    if isinstance(raw_result, str):
        return (raw_result,)
    if isinstance(raw_result, (list, tuple)):
        raw_items = cast(list[object] | tuple[object, ...], raw_result)
        node_names: list[str] = []
        for item in raw_items:
            if not isinstance(item, str):
                break
            node_names.append(item)
        else:
            return tuple(node_names)
    raise TypeError(
        f"Unexpected bduSampleCreateTransforms result: {raw_result!r}"
    )
