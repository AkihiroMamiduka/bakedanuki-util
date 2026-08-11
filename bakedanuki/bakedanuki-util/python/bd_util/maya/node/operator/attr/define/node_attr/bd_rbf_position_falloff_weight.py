# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Pose_positionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Pose_positionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "ppx"),
        ("positionY", "ppy"),
        ("positionZ", "ppz"),
    )

    positionX = DoubleLinearField()
    ppx = positionX

    positionY = DoubleLinearField()
    ppy = positionY

    positionZ = DoubleLinearField()
    ppz = positionZ


class Pose_positionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Pose_positionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleLinearField()
    ppx = positionX

    positionY = DoubleLinearField()
    ppy = positionY

    positionZ = DoubleLinearField()
    ppz = positionZ


class Pose_positionField(
    DoubleLinear3CompoundBaseField[
        Pose_positionAttrOperator, Pose_positionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Pose_positionAttrOperator
    PLUG_CLS = Pose_positionPlugOperator

    positionX = DoubleLinearField()
    ppx = positionX

    positionY = DoubleLinearField()
    ppy = positionY

    positionZ = DoubleLinearField()
    ppz = positionZ


class InputPositionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputPositionX", "ipx"),
        ("inputPositionY", "ipy"),
        ("inputPositionZ", "ipz"),
    )

    inputPositionX = DoubleLinearField(default_value=0.0)
    ipx = inputPositionX

    inputPositionY = DoubleLinearField(default_value=0.0)
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inputPositionZ


class InputPositionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPositionPlugOperator]
):
    __slots__ = ()

    inputPositionX = DoubleLinearField(default_value=0.0)
    ipx = inputPositionX

    inputPositionY = DoubleLinearField(default_value=0.0)
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inputPositionZ


class InputPositionField(
    DoubleLinear3CompoundBaseField[
        InputPositionAttrOperator, InputPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputPositionAttrOperator
    PLUG_CLS = InputPositionPlugOperator

    inputPositionX = DoubleLinearField(default_value=0.0)
    ipx = inputPositionX

    inputPositionY = DoubleLinearField(default_value=0.0)
    ipy = inputPositionY

    inputPositionZ = DoubleLinearField(default_value=0.0)
    ipz = inputPositionZ


class PosePlugOperator(CompoundPlugOperator["PoseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("position", "pp"),
        ("enabled", "en"),
        ("useRadiusOverride", "uro"),
        ("innerRadiusOverride", "iro"),
        ("outerRadiusOverride", "oro"),
    )

    position = Pose_positionField(default_value=(0.0, 0.0, 0.0))
    pp = position

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

    position = Pose_positionField(default_value=(0.0, 0.0, 0.0))
    pp = position

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
