# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class Source_orderEnumPlugOperator(
    EnumPlugOperator["Source_orderEnumAttrOperator"]
):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1


class Source_orderEnumAttrOperator(
    EnumAttrOperator[Source_orderEnumPlugOperator]
):
    __slots__ = ()

    TWISTBEND = 0
    BENDTWIST = 1

    NAME_MAP = {
        TWISTBEND: "TwistBend",
        BENDTWIST: "BendTwist",
    }


class Source_orderEnumField(
    EnumField[Source_orderEnumAttrOperator, Source_orderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Source_orderEnumAttrOperator
    PLUG_CLS = Source_orderEnumPlugOperator


class Source_inputQuatPlugOperator(
    QuatCompoundBasePlugOperator["Source_inputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqx"),
        ("inputQuatY", "iqy"),
        ("inputQuatZ", "iqz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class Source_inputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[Source_inputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class Source_inputQuatField(
    QuatCompoundBaseField[
        Source_inputQuatAttrOperator, Source_inputQuatPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Source_inputQuatAttrOperator
    PLUG_CLS = Source_inputQuatPlugOperator

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class Source_axisQuatPlugOperator(
    QuatCompoundBasePlugOperator["Source_axisQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisQuatX", "aqx"),
        ("axisQuatY", "aqy"),
        ("axisQuatZ", "aqz"),
        ("axisQuatW", "aqw"),
    )

    axisQuatX = DoubleField()
    aqx = axisQuatX

    axisQuatY = DoubleField()
    aqy = axisQuatY

    axisQuatZ = DoubleField()
    aqz = axisQuatZ

    axisQuatW = DoubleField()
    aqw = axisQuatW


class Source_axisQuatAttrOperator(
    QuatCompoundBaseAttrOperator[Source_axisQuatPlugOperator]
):
    __slots__ = ()

    axisQuatX = DoubleField()
    aqx = axisQuatX

    axisQuatY = DoubleField()
    aqy = axisQuatY

    axisQuatZ = DoubleField()
    aqz = axisQuatZ

    axisQuatW = DoubleField()
    aqw = axisQuatW


class Source_axisQuatField(
    QuatCompoundBaseField[
        Source_axisQuatAttrOperator, Source_axisQuatPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Source_axisQuatAttrOperator
    PLUG_CLS = Source_axisQuatPlugOperator

    axisQuatX = DoubleField()
    aqx = axisQuatX

    axisQuatY = DoubleField()
    aqy = axisQuatY

    axisQuatZ = DoubleField()
    aqz = axisQuatZ

    axisQuatW = DoubleField()
    aqw = axisQuatW


class Pose_sourceQuatPlugOperator(
    QuatCompoundBasePlugOperator["Pose_sourceQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourceQuatX", "sqx"),
        ("sourceQuatY", "sqy"),
        ("sourceQuatZ", "sqz"),
        ("sourceQuatW", "sqw"),
    )

    sourceQuatX = DoubleField(default_value=0.0)
    sqx = sourceQuatX

    sourceQuatY = DoubleField(default_value=0.0)
    sqy = sourceQuatY

    sourceQuatZ = DoubleField(default_value=0.0)
    sqz = sourceQuatZ

    sourceQuatW = DoubleField(default_value=0.0)
    sqw = sourceQuatW


class Pose_sourceQuatAttrOperator(
    QuatCompoundBaseAttrOperator[Pose_sourceQuatPlugOperator]
):
    __slots__ = ()

    sourceQuatX = DoubleField(default_value=0.0)
    sqx = sourceQuatX

    sourceQuatY = DoubleField(default_value=0.0)
    sqy = sourceQuatY

    sourceQuatZ = DoubleField(default_value=0.0)
    sqz = sourceQuatZ

    sourceQuatW = DoubleField(default_value=0.0)
    sqw = sourceQuatW


class Pose_sourceQuatField(
    QuatCompoundBaseField[
        Pose_sourceQuatAttrOperator, Pose_sourceQuatPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Pose_sourceQuatAttrOperator
    PLUG_CLS = Pose_sourceQuatPlugOperator


class SourcePlugOperator(CompoundPlugOperator["SourceAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuat", "iq"),
        ("axisQuat", "aq"),
        ("order", "ord"),
        ("influence", "inf"),
    )

    inputQuat = Source_inputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat

    axisQuat = Source_axisQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    aq = axisQuat

    order = Source_orderEnumField(default_value=0)
    ord = order

    influence = DoubleField(default_value=1.0, min_value=0.0)
    inf = influence


class SourceAttrOperator(CompoundAttrOperator[SourcePlugOperator]):
    __slots__ = ()

    inputQuat = Source_inputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat

    axisQuat = Source_axisQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    aq = axisQuat

    order = Source_orderEnumField(default_value=0)
    ord = order

    influence = DoubleField(default_value=1.0, min_value=0.0)
    inf = influence


class SourceField(CompoundField[SourceAttrOperator, SourcePlugOperator]):
    __slots__ = ()

    ATTR_CLS = SourceAttrOperator
    PLUG_CLS = SourcePlugOperator


class PosePlugOperator(CompoundPlugOperator["PoseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourceQuat", "sq"),
        ("enabled", "en"),
        ("useRadiusOverride", "uro"),
        ("bendInnerRadiusOverride", "biro"),
        ("bendOuterRadiusOverride", "boro"),
        ("twistInnerRadiusOverride", "tiro"),
        ("twistOuterRadiusOverride", "toro"),
    )

    sourceQuat = Pose_sourceQuatField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    sq = sourceQuat

    enabled = BoolField(default_value=True)
    en = enabled

    useRadiusOverride = BoolField(default_value=False)
    uro = useRadiusOverride

    bendInnerRadiusOverride = DoubleAngleField(
        default_value=0.0, min_value=0.0
    )
    biro = bendInnerRadiusOverride

    bendOuterRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    boro = bendOuterRadiusOverride

    twistInnerRadiusOverride = DoubleAngleField(
        default_value=0.0, min_value=0.0
    )
    tiro = twistInnerRadiusOverride

    twistOuterRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    toro = twistOuterRadiusOverride


class PoseAttrOperator(CompoundAttrOperator[PosePlugOperator]):
    __slots__ = ()

    sourceQuat = Pose_sourceQuatField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    sq = sourceQuat

    enabled = BoolField(default_value=True)
    en = enabled

    useRadiusOverride = BoolField(default_value=False)
    uro = useRadiusOverride

    bendInnerRadiusOverride = DoubleAngleField(
        default_value=0.0, min_value=0.0
    )
    biro = bendInnerRadiusOverride

    bendOuterRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    boro = bendOuterRadiusOverride

    twistInnerRadiusOverride = DoubleAngleField(
        default_value=0.0, min_value=0.0
    )
    tiro = twistInnerRadiusOverride

    twistOuterRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    toro = twistOuterRadiusOverride


class PoseField(CompoundField[PoseAttrOperator, PosePlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoseAttrOperator
    PLUG_CLS = PosePlugOperator
