# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.dga_visualizer import GeneratedDgaVisualizer
else:
    from ._generated.dga_visualizer import GeneratedDgaVisualizer


class DgaVisualizer(GeneratedDgaVisualizer):
    __slots__ = ()

    NODE_TYPE = "dgaVisualizer"
