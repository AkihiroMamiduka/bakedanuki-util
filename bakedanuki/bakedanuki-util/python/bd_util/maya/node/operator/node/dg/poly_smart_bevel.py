# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.poly_smart_bevel import GeneratedPolySmartBevel
else:
    from ._generated.poly_smart_bevel import GeneratedPolySmartBevel


class PolySmartBevel(GeneratedPolySmartBevel):
    __slots__ = ()

    NODE_TYPE = "polySmartBevel"
