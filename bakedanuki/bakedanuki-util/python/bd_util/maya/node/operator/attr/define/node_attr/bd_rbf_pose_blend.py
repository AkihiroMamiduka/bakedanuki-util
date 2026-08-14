# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class Pose_translatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Pose_translateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "ptx"),
        ("translateY", "pty"),
        ("translateZ", "ptz"),
    )

    translateX = DoubleLinearField()
    ptx = translateX

    translateY = DoubleLinearField()
    pty = translateY

    translateZ = DoubleLinearField()
    ptz = translateZ


class Pose_translateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Pose_translatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField()
    ptx = translateX

    translateY = DoubleLinearField()
    pty = translateY

    translateZ = DoubleLinearField()
    ptz = translateZ


class Pose_translateField(
    DoubleLinear3CompoundBaseField[
        Pose_translateAttrOperator, Pose_translatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Pose_translateAttrOperator
    PLUG_CLS = Pose_translatePlugOperator

    translateX = DoubleLinearField()
    ptx = translateX

    translateY = DoubleLinearField()
    pty = translateY

    translateZ = DoubleLinearField()
    ptz = translateZ


class Pose_rotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["Pose_rotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "prx"),
        ("rotateY", "pry"),
        ("rotateZ", "prz"),
    )

    rotateX = DoubleAngleField()
    prx = rotateX

    rotateY = DoubleAngleField()
    pry = rotateY

    rotateZ = DoubleAngleField()
    prz = rotateZ


class Pose_rotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Pose_rotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    prx = rotateX

    rotateY = DoubleAngleField()
    pry = rotateY

    rotateZ = DoubleAngleField()
    prz = rotateZ


class Pose_rotateField(
    DoubleAngle3CompoundBaseField[
        Pose_rotateAttrOperator, Pose_rotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Pose_rotateAttrOperator
    PLUG_CLS = Pose_rotatePlugOperator

    rotateX = DoubleAngleField()
    prx = rotateX

    rotateY = DoubleAngleField()
    pry = rotateY

    rotateZ = DoubleAngleField()
    prz = rotateZ


class Pose_scalePlugOperator(
    Double3CompoundBasePlugOperator["Pose_scaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "psx"),
        ("scaleY", "psy"),
        ("scaleZ", "psz"),
    )

    scaleX = DoubleField()
    psx = scaleX

    scaleY = DoubleField()
    psy = scaleY

    scaleZ = DoubleField()
    psz = scaleZ


class Pose_scaleAttrOperator(
    Double3CompoundBaseAttrOperator[Pose_scalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField()
    psx = scaleX

    scaleY = DoubleField()
    psy = scaleY

    scaleZ = DoubleField()
    psz = scaleZ


class Pose_scaleField(
    Double3CompoundBaseField[Pose_scaleAttrOperator, Pose_scalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Pose_scaleAttrOperator
    PLUG_CLS = Pose_scalePlugOperator

    scaleX = DoubleField()
    psx = scaleX

    scaleY = DoubleField()
    psy = scaleY

    scaleZ = DoubleField()
    psz = scaleZ


class BaseTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["BaseTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseTranslateX", "btx"),
        ("baseTranslateY", "bty"),
        ("baseTranslateZ", "btz"),
    )

    baseTranslateX = DoubleLinearField(default_value=0.0)
    btx = baseTranslateX

    baseTranslateY = DoubleLinearField(default_value=0.0)
    bty = baseTranslateY

    baseTranslateZ = DoubleLinearField(default_value=0.0)
    btz = baseTranslateZ


class BaseTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[BaseTranslatePlugOperator]
):
    __slots__ = ()

    baseTranslateX = DoubleLinearField(default_value=0.0)
    btx = baseTranslateX

    baseTranslateY = DoubleLinearField(default_value=0.0)
    bty = baseTranslateY

    baseTranslateZ = DoubleLinearField(default_value=0.0)
    btz = baseTranslateZ


class BaseTranslateField(
    DoubleLinear3CompoundBaseField[
        BaseTranslateAttrOperator, BaseTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BaseTranslateAttrOperator
    PLUG_CLS = BaseTranslatePlugOperator

    baseTranslateX = DoubleLinearField(default_value=0.0)
    btx = baseTranslateX

    baseTranslateY = DoubleLinearField(default_value=0.0)
    bty = baseTranslateY

    baseTranslateZ = DoubleLinearField(default_value=0.0)
    btz = baseTranslateZ


class BaseRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["BaseRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseRotateX", "brx"),
        ("baseRotateY", "bry"),
        ("baseRotateZ", "brz"),
    )

    baseRotateX = DoubleAngleField(default_value=0.0)
    brx = baseRotateX

    baseRotateY = DoubleAngleField(default_value=0.0)
    bry = baseRotateY

    baseRotateZ = DoubleAngleField(default_value=0.0)
    brz = baseRotateZ


class BaseRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[BaseRotatePlugOperator]
):
    __slots__ = ()

    baseRotateX = DoubleAngleField(default_value=0.0)
    brx = baseRotateX

    baseRotateY = DoubleAngleField(default_value=0.0)
    bry = baseRotateY

    baseRotateZ = DoubleAngleField(default_value=0.0)
    brz = baseRotateZ


class BaseRotateField(
    DoubleAngle3CompoundBaseField[
        BaseRotateAttrOperator, BaseRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BaseRotateAttrOperator
    PLUG_CLS = BaseRotatePlugOperator

    baseRotateX = DoubleAngleField(default_value=0.0)
    brx = baseRotateX

    baseRotateY = DoubleAngleField(default_value=0.0)
    bry = baseRotateY

    baseRotateZ = DoubleAngleField(default_value=0.0)
    brz = baseRotateZ


class BaseScalePlugOperator(
    Double3CompoundBasePlugOperator["BaseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("baseScaleX", "bscx"),
        ("baseScaleY", "bscy"),
        ("baseScaleZ", "bscz"),
    )

    baseScaleX = DoubleField(default_value=1.0)
    bscx = baseScaleX

    baseScaleY = DoubleField(default_value=1.0)
    bscy = baseScaleY

    baseScaleZ = DoubleField(default_value=1.0)
    bscz = baseScaleZ


class BaseScaleAttrOperator(
    Double3CompoundBaseAttrOperator[BaseScalePlugOperator]
):
    __slots__ = ()

    baseScaleX = DoubleField(default_value=1.0)
    bscx = baseScaleX

    baseScaleY = DoubleField(default_value=1.0)
    bscy = baseScaleY

    baseScaleZ = DoubleField(default_value=1.0)
    bscz = baseScaleZ


class BaseScaleField(
    Double3CompoundBaseField[BaseScaleAttrOperator, BaseScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BaseScaleAttrOperator
    PLUG_CLS = BaseScalePlugOperator

    baseScaleX = DoubleField(default_value=1.0)
    bscx = baseScaleX

    baseScaleY = DoubleField(default_value=1.0)
    bscy = baseScaleY

    baseScaleZ = DoubleField(default_value=1.0)
    bscz = baseScaleZ


class PosePlugOperator(CompoundPlugOperator["PoseAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translate", "pt"),
        ("rotate", "pr"),
        ("scale", "ps"),
        ("enabled", "en"),
    )

    translate = Pose_translateField(default_value=(0.0, 0.0, 0.0))
    pt = translate

    rotate = Pose_rotateField(default_value=(0.0, 0.0, 0.0))
    pr = rotate

    scale = Pose_scaleField(default_value=(1.0, 1.0, 1.0))
    ps = scale

    enabled = BoolField(default_value=True)
    en = enabled


class PoseAttrOperator(CompoundAttrOperator[PosePlugOperator]):
    __slots__ = ()

    translate = Pose_translateField(default_value=(0.0, 0.0, 0.0))
    pt = translate

    rotate = Pose_rotateField(default_value=(0.0, 0.0, 0.0))
    pr = rotate

    scale = Pose_scaleField(default_value=(1.0, 1.0, 1.0))
    ps = scale

    enabled = BoolField(default_value=True)
    en = enabled


class PoseField(CompoundField[PoseAttrOperator, PosePlugOperator]):
    __slots__ = ()

    ATTR_CLS = PoseAttrOperator
    PLUG_CLS = PosePlugOperator


class OutputTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTranslateX", "otx"),
        ("outputTranslateY", "oty"),
        ("outputTranslateZ", "otz"),
    )

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputTranslatePlugOperator]
):
    __slots__ = ()

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputTranslateField(
    DoubleLinear3CompoundBaseField[
        OutputTranslateAttrOperator, OutputTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputTranslateAttrOperator
    PLUG_CLS = OutputTranslatePlugOperator

    outputTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    otx = outputTranslateX

    outputTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    oty = outputTranslateY

    outputTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    otz = outputTranslateZ


class OutputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputRotateX", "orx"),
        ("outputRotateY", "ory"),
        ("outputRotateZ", "orz"),
    )

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[
        OutputRotateAttrOperator, OutputRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputQuatPlugOperator(
    QuatCompoundBasePlugOperator["OutputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputQuatX", "oqx"),
        ("outputQuatY", "oqy"),
        ("outputQuatZ", "oqz"),
        ("outputQuatW", "oqw"),
    )

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=1.0, writable=False)
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=1.0, writable=False)
    oqw = outputQuatW


class OutputQuatField(
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=1.0, writable=False)
    oqw = outputQuatW


class OutputScalePlugOperator(
    Double3CompoundBasePlugOperator["OutputScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputScaleX", "osx"),
        ("outputScaleY", "osy"),
        ("outputScaleZ", "osz"),
    )

    outputScaleX = DoubleField(default_value=1.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=1.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=1.0, writable=False)
    osz = outputScaleZ


class OutputScaleAttrOperator(
    Double3CompoundBaseAttrOperator[OutputScalePlugOperator]
):
    __slots__ = ()

    outputScaleX = DoubleField(default_value=1.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=1.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=1.0, writable=False)
    osz = outputScaleZ


class OutputScaleField(
    Double3CompoundBaseField[OutputScaleAttrOperator, OutputScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputScaleAttrOperator
    PLUG_CLS = OutputScalePlugOperator

    outputScaleX = DoubleField(default_value=1.0, writable=False)
    osx = outputScaleX

    outputScaleY = DoubleField(default_value=1.0, writable=False)
    osy = outputScaleY

    outputScaleZ = DoubleField(default_value=1.0, writable=False)
    osz = outputScaleZ
