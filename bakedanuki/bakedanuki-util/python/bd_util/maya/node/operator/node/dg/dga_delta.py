# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.dga_delta import GeneratedDgaDelta
else:
    from ._generated.dga_delta import GeneratedDgaDelta


class DgaDelta(GeneratedDgaDelta):
    __slots__ = ()

    NODE_TYPE = "dgaDelta"
