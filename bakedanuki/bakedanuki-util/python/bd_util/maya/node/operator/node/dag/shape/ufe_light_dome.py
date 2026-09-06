# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_dome import GeneratedUfeLightDome
else:
    from ._generated.ufe_light_dome import GeneratedUfeLightDome


class UfeLightDome(GeneratedUfeLightDome):
    __slots__ = ()

    NODE_TYPE = "ufeLightDome"
