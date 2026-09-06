# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.shot_label import GeneratedShotLabel
else:
    from ._generated.shot_label import GeneratedShotLabel


class ShotLabel(GeneratedShotLabel):
    __slots__ = ()

    NODE_TYPE = "shotLabel"
