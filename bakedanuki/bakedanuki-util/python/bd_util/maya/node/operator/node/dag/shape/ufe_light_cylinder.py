# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_cylinder import (
        GeneratedUfeLightCylinder,
    )
else:
    from ._generated.ufe_light_cylinder import GeneratedUfeLightCylinder


class UfeLightCylinder(GeneratedUfeLightCylinder):
    __slots__ = ()

    NODE_TYPE = "ufeLightCylinder"
