# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.round_dl import GeneratedRoundDL
else:
    from ._generated.round_dl import GeneratedRoundDL


class RoundDL(GeneratedRoundDL):
    __slots__ = ()

    NODE_TYPE = "roundDL"
