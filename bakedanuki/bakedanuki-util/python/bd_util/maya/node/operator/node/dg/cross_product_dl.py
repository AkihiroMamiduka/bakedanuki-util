# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.cross_product_dl import GeneratedCrossProductDL
else:
    from ._generated.cross_product_dl import GeneratedCrossProductDL


class CrossProductDL(GeneratedCrossProductDL):
    __slots__ = ()

    NODE_TYPE = "crossProductDL"
