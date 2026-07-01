# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_collision import ColliderField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class XgmModifierCollision(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierCollision"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    mask = FloatField()
    mk = mask

    collisionDistance = FloatField()
    cd = collisionDistance

    meshSampling = LongField()
    ac = meshSampling

    resolveType = LongField()
    rt = resolveType

    iterations = LongField()
    it = iterations

    sigma = LongField()
    sg = sigma

    deformationPreserved = BoolField()
    dp = deformationPreserved

    tweak = TypedField()
    t = tweak

    collider = ColliderField(multi=True)
    cld = collider
