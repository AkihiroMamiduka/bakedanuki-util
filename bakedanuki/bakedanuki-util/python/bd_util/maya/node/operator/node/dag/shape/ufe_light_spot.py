# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_spot import GeneratedUfeLightSpot
else:
    from ._generated.ufe_light_spot import GeneratedUfeLightSpot


class UfeLightSpot(GeneratedUfeLightSpot):
    __slots__ = ()

    NODE_TYPE = "ufeLightSpot"
