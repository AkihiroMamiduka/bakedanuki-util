# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2026.log_dl import GeneratedLogDL
else:
    from ._generated.log_dl import GeneratedLogDL


class LogDL(GeneratedLogDL):
    __slots__ = ()

    NODE_TYPE = "logDL"
