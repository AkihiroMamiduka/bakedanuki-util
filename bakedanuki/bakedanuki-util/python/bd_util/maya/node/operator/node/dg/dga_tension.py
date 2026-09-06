# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.dga_tension import GeneratedDgaTension
else:
    from ._generated.dga_tension import GeneratedDgaTension


class DgaTension(GeneratedDgaTension):
    __slots__ = ()

    NODE_TYPE = "dgaTension"
