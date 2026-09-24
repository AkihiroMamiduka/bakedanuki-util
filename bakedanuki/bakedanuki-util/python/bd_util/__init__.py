# coding: utf-8
"""Maya のノード操作、値型、UI 構築に使うユーティリティ。"""

from . import _version
from ._dev.reload import reload_package
from ._dev.timer import timer
from .py import json_file
from .maya.node.modifier import ModifierManager
from .maya.node.nodes import Nodes
from .maya.node.animation_clip import AnimationClip
from .maya.transform import TransformMatrix
from .maya.value import (
    Double2,
    Double3,
    Double4,
    DoubleAngle2,
    DoubleAngle3,
    DoubleLinear2,
    DoubleLinear3,
    Float2,
    Float3,
    FloatAngle2,
    FloatAngle3,
    FloatLinear2,
    FloatLinear3,
    Long2,
    Long3,
    Quat,
    Short2,
    Short3,
)
from .maya.mpx_cmd import (
    CommandResult,
    MPxCommandBase,
    deregister_commands,
    register_commands,
)

# パッケージのバージョン
__version__ = _version.__version__

# パッケージの公開API
__all__ = [
    "AnimationClip",
    "json_file",
    "reload_package",
    "timer",
    "MPxCommandBase",
    "CommandResult",
    "register_commands",
    "deregister_commands",
    "ModifierManager",
    "Nodes",
    "TransformMatrix",
    "Double2",
    "Double3",
    "Double4",
    "DoubleAngle2",
    "DoubleAngle3",
    "DoubleLinear2",
    "DoubleLinear3",
    "Float2",
    "Float3",
    "FloatAngle2",
    "FloatAngle3",
    "FloatLinear2",
    "FloatLinear3",
    "Long2",
    "Long3",
    "Quat",
    "Short2",
    "Short3",
]
