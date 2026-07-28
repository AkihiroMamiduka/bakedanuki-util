# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_modifier_collision import ColliderField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


class GeneratedXgmModifierCollision(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierCollision"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    collisionDistance = FloatField(
        default_value=0.009999999776482582,
        min_value=0.0010000000474974513,
        max_value=10.0,
    )
    cd = collisionDistance

    meshSampling = LongField(default_value=5, min_value=3, max_value=20)
    ac = meshSampling

    resolveType = LongField(default_value=0)
    rt = resolveType

    iterations = LongField(default_value=5, min_value=3, max_value=20)
    it = iterations

    sigma = LongField(default_value=1, min_value=0, max_value=3)
    sg = sigma

    deformationPreserved = BoolField(default_value=False)
    dp = deformationPreserved

    tweak = TypedField()
    t = tweak

    collider = ColliderField(multi=True)
    cld = collider
