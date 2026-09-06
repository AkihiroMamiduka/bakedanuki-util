# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_directional import (
        GeneratedUfeLightDirectional,
    )
else:
    from ._generated.ufe_light_directional import GeneratedUfeLightDirectional


class UfeLightDirectional(GeneratedUfeLightDirectional):
    __slots__ = ()

    NODE_TYPE = "ufeLightDirectional"
