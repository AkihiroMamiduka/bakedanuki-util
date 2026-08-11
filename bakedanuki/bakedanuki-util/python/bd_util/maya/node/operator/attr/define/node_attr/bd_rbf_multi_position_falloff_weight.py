# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Source_inputPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Source_inputPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPositionX", "ipx"),
        ("inputPositionY", "ipy"),
        ("inputPositionZ", "ipz"),
    )

    inputPositionX = DoubleLinearField()
    ipx = inputPositionX

    inputPositionY = DoubleLinearField()
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField()
    ipz = inputPositionZ


class Source_inputPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Source_inputPositionPlugOperator]
):
    __slots__ = ()

    inputPositionX = DoubleLinearField()
    ipx = inputPositionX

    inputPositionY = DoubleLinearField()
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField()
    ipz = inputPositionZ


class Source_inputPositionField(
    DoubleLinear3CompoundBaseField[
        Source_inputPositionAttrOperator, Source_inputPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Source_inputPositionAttrOperator
    PLUG_CLS = Source_inputPositionPlugOperator

    inputPositionX = DoubleLinearField()
    ipx = inputPositionX

    inputPositionY = DoubleLinearField()
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField()
    ipz = inputPositionZ


class Pose_sourcePositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Pose_sourcePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourcePositionX", "spx"),
        ("sourcePositionY", "spy"),
        ("sourcePositionZ", "spz"),
    )

    sourcePositionX = DoubleLinearField(default_value=0.0)
    spx = sourcePositionX

    sourcePositionY = DoubleLinearField(default_value=0.0)
    spy = sourcePositionY

    sourcePositionZ = DoubleLinearField(default_value=0.0)
    spz = sourcePositionZ


class Pose_sourcePositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Pose_sourcePositionPlugOperator]
):
    __slots__ = ()

    sourcePositionX = DoubleLinearField(default_value=0.0)
    spx = sourcePositionX

    sourcePositionY = DoubleLinearField(default_value=0.0)
    spy = sourcePositionY

    sourcePositionZ = DoubleLinearField(default_value=0.0)
    spz = sourcePositionZ


class Pose_sourcePositionField(
    DoubleLinear3CompoundBaseField[
        Pose_sourcePositionAttrOperator, Pose_sourcePositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Pose_sourcePositionAttrOperator
    PLUG_CLS = Pose_sourcePositionPlugOperator


class SourcePlugOperator(CompoundPlugOperator["SourceAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPosition", "ip"),
        ("influence", "inf"),
    )

    inputPosition = Source_inputPositionField(default_value=(0.0, 0.0, 0.0))
    ip = inputPosition

    influence = DoubleField(default_value=1.0, min_value=0.0)
    inf = influence


class SourceAttrOperator(CompoundAttrOperator[SourcePlugOperator]):
    __slots__ = ()

    inputPosition = Source_inputPositionField(default_value=(0.0, 0.0, 0.0))
    ip = inputPosition

    influence = DoubleField(default_value=1.0, min_value=0.0)
    inf = influence


class SourceField(CompoundField[SourceAttrOperator, SourcePlugOperator]):
    __slots__ = ()

    ATTR_CLS = SourceAttrOperator
    PLUG_CLS = SourcePlugOperator


class PosePlugOperator(CompoundPlugOperator["PoseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sourcePosition", "sp"),
        ("enabled", "en"),
        ("useRadiusOverride", "uro"),
        ("innerRadiusOverride", "iro"),
        ("outerRadiusOverride", "oro"),
    )

    sourcePosition = Pose_sourcePositionField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    sp = sourcePosition

    enabled = BoolField(default_value=True)
    en = enabled

    useRadiusOverride = BoolField(default_value=False)
    uro = useRadiusOverride

    innerRadiusOverride = DoubleLinearField(default_value=0.0, min_value=0.0)
    iro = innerRadiusOverride

    outerRadiusOverride = DoubleLinearField(default_value=1.0, min_value=0.0)
    oro = outerRadiusOverride


class PoseAttrOperator(CompoundAttrOperator[PosePlugOperator]):
    __slots__ = ()

    sourcePosition = Pose_sourcePositionField(
        multi=True, default_value=(0.0, 0.0, 0.0)
    )
    sp = sourcePosition

    enabled = BoolField(default_value=True)
    en = enabled

    useRadiusOverride = BoolField(default_value=False)
    uro = useRadiusOverride

    innerRadiusOverride = DoubleLinearField(default_value=0.0, min_value=0.0)
    iro = innerRadiusOverride

    outerRadiusOverride = DoubleLinearField(default_value=1.0, min_value=0.0)
    oro = outerRadiusOverride


class PoseField(CompoundField[PoseAttrOperator, PosePlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoseAttrOperator
    PLUG_CLS = PosePlugOperator
