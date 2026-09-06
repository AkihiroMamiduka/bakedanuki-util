# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.dot_product_dl import GeneratedDotProductDL
else:
    from ._generated.dot_product_dl import GeneratedDotProductDL


class DotProductDL(GeneratedDotProductDL):
    __slots__ = ()

    NODE_TYPE = "dotProductDL"
