# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


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
        ("influence", "inf"),
    )

    inputQuat = Source_inputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat

    influence = DoubleField(default_value=1.0, min_value=0.0)
    inf = influence


class SourceAttrOperator(CompoundAttrOperator[SourcePlugOperator]):
    __slots__ = ()

    inputQuat = Source_inputQuatField(default_value=(0.0, 0.0, 0.0, 1.0))
    iq = inputQuat

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
        ("innerRadiusOverride", "iro"),
        ("outerRadiusOverride", "oro"),
    )

    sourceQuat = Pose_sourceQuatField(
        multi=True, default_value=(0.0, 0.0, 0.0, 0.0)
    )
    sq = sourceQuat

    enabled = BoolField(default_value=True)
    en = enabled

    useRadiusOverride = BoolField(default_value=False)
    uro = useRadiusOverride

    innerRadiusOverride = DoubleAngleField(default_value=0.0, min_value=0.0)
    iro = innerRadiusOverride

    outerRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    oro = outerRadiusOverride


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

    innerRadiusOverride = DoubleAngleField(default_value=0.0, min_value=0.0)
    iro = innerRadiusOverride

    outerRadiusOverride = DoubleAngleField(
        default_value=59.99999999999999, min_value=0.0
    )
    oro = outerRadiusOverride


class PoseField(CompoundField[PoseAttrOperator, PosePlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoseAttrOperator
    PLUG_CLS = PosePlugOperator
