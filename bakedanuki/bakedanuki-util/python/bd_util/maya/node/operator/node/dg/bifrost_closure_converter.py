# coding: utf-8
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._generated_maya2027.bifrost_closure_converter import (
        GeneratedBifrostClosureConverter,
    )
else:
    from ._generated.bifrost_closure_converter import (
        GeneratedBifrostClosureConverter,
    )


class BifrostClosureConverter(GeneratedBifrostClosureConverter):
    __slots__ = ()

    NODE_TYPE = "bifrostClosureConverter"
