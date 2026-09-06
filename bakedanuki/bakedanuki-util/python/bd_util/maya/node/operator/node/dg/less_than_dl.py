# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.less_than_dl import GeneratedLessThanDL
else:
    from ._generated.less_than_dl import GeneratedLessThanDL


class LessThanDL(GeneratedLessThanDL):
    __slots__ = ()

    NODE_TYPE = "lessThanDL"
