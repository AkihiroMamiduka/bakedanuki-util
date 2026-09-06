# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.usd_default_settings import (
        GeneratedUsdDefaultSettings,
    )
else:
    from ._generated.usd_default_settings import GeneratedUsdDefaultSettings


class UsdDefaultSettings(GeneratedUsdDefaultSettings):
    __slots__ = ()

    NODE_TYPE = "UsdDefaultSettings"
