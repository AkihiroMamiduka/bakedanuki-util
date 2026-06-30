# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subd_tweak_uv import UvTweakField
from ...attr.define.std.at.typed import TypedField


class SubdTweakUV(DG):
    __slots__ = ()

    NODE_TYPE = "subdTweakUV"

    outSubdiv = TypedField()
    os = outSubdiv

    inSubdiv = TypedField()
    is_ = inSubdiv

    cachedSubdiv = TypedField()
    ic = cachedSubdiv

    inputComponents = TypedField()
    ics = inputComponents

    uvTweak = UvTweakField(multi=True)
    uvtk = uvTweak
