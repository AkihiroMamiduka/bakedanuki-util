# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.add_dl import GeneratedAddDL
else:
    from ._generated.add_dl import GeneratedAddDL


class AddDL(GeneratedAddDL):
    __slots__ = ()

    NODE_TYPE = "addDL"
