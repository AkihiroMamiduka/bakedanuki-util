# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.dga_to_array import GeneratedDgaToArray
else:
    from ._generated.dga_to_array import GeneratedDgaToArray


class DgaToArray(GeneratedDgaToArray):
    __slots__ = ()

    NODE_TYPE = "dgaToArray"
