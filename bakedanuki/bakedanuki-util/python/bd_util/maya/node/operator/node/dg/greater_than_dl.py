# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.greater_than_dl import GeneratedGreaterThanDL
else:
    from ._generated.greater_than_dl import GeneratedGreaterThanDL


class GreaterThanDL(GeneratedGreaterThanDL):
    __slots__ = ()

    NODE_TYPE = "greaterThanDL"
