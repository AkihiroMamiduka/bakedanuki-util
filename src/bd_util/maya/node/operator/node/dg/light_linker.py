# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.light_linker import (
    IgnoreField,
    LinkField,
    ShadowIgnoreField,
    ShadowLinkField,
)


class LightLinker(DG):
    __slots__ = ()

    NODE_TYPE = "lightLinker"

    link = LinkField(multi=True)
    lnk = link

    ignore = IgnoreField(multi=True)
    ign = ignore

    shadowLink = ShadowLinkField(multi=True)
    slnk = shadowLink

    shadowIgnore = ShadowIgnoreField(multi=True)
    sign = shadowIgnore
