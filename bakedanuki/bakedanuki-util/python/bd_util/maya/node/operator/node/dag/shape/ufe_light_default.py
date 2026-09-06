# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_default import GeneratedUfeLightDefault
else:
    from ._generated.ufe_light_default import GeneratedUfeLightDefault


class UfeLightDefault(GeneratedUfeLightDefault):
    __slots__ = ()

    NODE_TYPE = "ufeLightDefault"
