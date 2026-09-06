# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.mult_dl import GeneratedMultDL
else:
    from ._generated.mult_dl import GeneratedMultDL


class MultDL(GeneratedMultDL):
    __slots__ = ()

    NODE_TYPE = "multDL"
