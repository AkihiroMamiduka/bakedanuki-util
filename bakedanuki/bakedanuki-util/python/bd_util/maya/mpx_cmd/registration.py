# coding: utf-8
from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from maya.api import OpenMaya as om

from .base import MPxCommandBase

CommandType = type[MPxCommandBase[Any]]


def register_commands(
    plugin: om.MObject,
    command_types: Iterable[CommandType],
) -> None:
    """Register commands and undo partial registration on failure."""
    plugin_fn = om.MFnPlugin(plugin)
    registered_names: list[str] = []

    try:
        for command_type in command_types:
            command_name = _command_name(command_type)
            plugin_fn.registerCommand(
                command_name,
                command_type.creator,
                command_type.create_syntax,
            )
            registered_names.append(command_name)
    except Exception as error:
        _rollback_registration(plugin_fn, registered_names, error)
        raise


def deregister_commands(
    plugin: om.MObject,
    command_types: Iterable[CommandType],
) -> None:
    """Deregister commands in reverse registration order."""
    plugin_fn = om.MFnPlugin(plugin)
    command_names = [
        _command_name(command_type) for command_type in command_types
    ]
    errors: list[tuple[str, Exception]] = []

    for command_name in reversed(command_names):
        try:
            plugin_fn.deregisterCommand(command_name)
        except Exception as error:
            errors.append((command_name, error))

    if errors:
        command_name, first_error = errors[0]
        for failed_name, error in errors[1:]:
            first_error.add_note(
                f"Deregistering command '{failed_name}' also failed: "
                f"{error!r}"
            )
        first_error.add_note(
            f"Failed while deregistering command '{command_name}'."
        )
        raise first_error


def _command_name(command_type: CommandType) -> str:
    command_name = command_type.COMMAND_NAME
    if not command_name:
        raise ValueError(
            f"{command_type.__qualname__}.COMMAND_NAME must not be empty."
        )
    return command_name


def _rollback_registration(
    plugin_fn: om.MFnPlugin,
    registered_names: list[str],
    original_error: Exception,
) -> None:
    for command_name in reversed(registered_names):
        try:
            plugin_fn.deregisterCommand(command_name)
        except Exception as rollback_error:
            original_error.add_note(
                f"Rolling back command registration for '{command_name}' "
                f"also failed: {rollback_error!r}"
            )
