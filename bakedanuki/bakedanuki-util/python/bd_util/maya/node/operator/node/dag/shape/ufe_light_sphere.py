# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_sphere import GeneratedUfeLightSphere
else:
    from ._generated.ufe_light_sphere import GeneratedUfeLightSphere


class UfeLightSphere(GeneratedUfeLightSphere):
    __slots__ = ()

    NODE_TYPE = "ufeLightSphere"
