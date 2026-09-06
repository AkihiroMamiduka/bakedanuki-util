# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.anim_in_context_node import (
        GeneratedAnimInContextNode,
    )
else:
    from ._generated.anim_in_context_node import GeneratedAnimInContextNode


class AnimInContextNode(GeneratedAnimInContextNode):
    __slots__ = ()

    NODE_TYPE = "animInContextNode"
