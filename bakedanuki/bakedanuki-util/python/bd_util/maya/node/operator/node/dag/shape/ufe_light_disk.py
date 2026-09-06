# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.ufe_light_disk import GeneratedUfeLightDisk
else:
    from ._generated.ufe_light_disk import GeneratedUfeLightDisk


class UfeLightDisk(GeneratedUfeLightDisk):
    __slots__ = ()

    NODE_TYPE = "ufeLightDisk"
