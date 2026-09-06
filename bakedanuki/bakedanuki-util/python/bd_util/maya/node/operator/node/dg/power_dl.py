# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.power_dl import GeneratedPowerDL
else:
    from ._generated.power_dl import GeneratedPowerDL


class PowerDL(GeneratedPowerDL):
    __slots__ = ()

    NODE_TYPE = "powerDL"
