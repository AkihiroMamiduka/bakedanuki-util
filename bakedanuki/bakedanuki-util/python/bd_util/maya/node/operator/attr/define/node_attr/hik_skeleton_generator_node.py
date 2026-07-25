# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField


class ReferenceTPlugOperator(
    CompoundPlugOperator["ReferenceTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ReferenceTx", "ReferenceTx"),
        ("ReferenceTy", "ReferenceTy"),
        ("ReferenceTz", "ReferenceTz"),
    )

    ReferenceTx = DoubleLinearField(default_value=0.0)

    ReferenceTy = DoubleLinearField(default_value=0.0)

    ReferenceTz = DoubleLinearField(default_value=0.0)


class ReferenceTAttrOperator(
    CompoundAttrOperator[ReferenceTPlugOperator]
):
    __slots__ = ()

    ReferenceTx = DoubleLinearField(default_value=0.0)

    ReferenceTy = DoubleLinearField(default_value=0.0)

    ReferenceTz = DoubleLinearField(default_value=0.0)


class ReferenceTField(
    CompoundField[ReferenceTAttrOperator, ReferenceTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReferenceTAttrOperator
    PLUG_CLS = ReferenceTPlugOperator

    ReferenceTx = DoubleLinearField(default_value=0.0)

    ReferenceTy = DoubleLinearField(default_value=0.0)

    ReferenceTz = DoubleLinearField(default_value=0.0)


class ReferenceRPlugOperator(
    CompoundPlugOperator["ReferenceRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ReferenceRx", "ReferenceRx"),
        ("ReferenceRy", "ReferenceRy"),
        ("ReferenceRz", "ReferenceRz"),
    )

    ReferenceRx = DoubleAngleField(default_value=0.0)

    ReferenceRy = DoubleAngleField(default_value=0.0)

    ReferenceRz = DoubleAngleField(default_value=0.0)


class ReferenceRAttrOperator(
    CompoundAttrOperator[ReferenceRPlugOperator]
):
    __slots__ = ()

    ReferenceRx = DoubleAngleField(default_value=0.0)

    ReferenceRy = DoubleAngleField(default_value=0.0)

    ReferenceRz = DoubleAngleField(default_value=0.0)


class ReferenceRField(
    CompoundField[ReferenceRAttrOperator, ReferenceRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReferenceRAttrOperator
    PLUG_CLS = ReferenceRPlugOperator

    ReferenceRx = DoubleAngleField(default_value=0.0)

    ReferenceRy = DoubleAngleField(default_value=0.0)

    ReferenceRz = DoubleAngleField(default_value=0.0)


class ReferenceSPlugOperator(
    CompoundPlugOperator["ReferenceSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ReferenceSx", "ReferenceSx"),
        ("ReferenceSy", "ReferenceSy"),
        ("ReferenceSz", "ReferenceSz"),
    )

    ReferenceSx = DoubleField(default_value=1.0)

    ReferenceSy = DoubleField(default_value=1.0)

    ReferenceSz = DoubleField(default_value=1.0)


class ReferenceSAttrOperator(
    CompoundAttrOperator[ReferenceSPlugOperator]
):
    __slots__ = ()

    ReferenceSx = DoubleField(default_value=1.0)

    ReferenceSy = DoubleField(default_value=1.0)

    ReferenceSz = DoubleField(default_value=1.0)


class ReferenceSField(
    CompoundField[ReferenceSAttrOperator, ReferenceSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ReferenceSAttrOperator
    PLUG_CLS = ReferenceSPlugOperator

    ReferenceSx = DoubleField(default_value=1.0)

    ReferenceSy = DoubleField(default_value=1.0)

    ReferenceSz = DoubleField(default_value=1.0)


class HipsTPlugOperator(
    CompoundPlugOperator["HipsTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsTx", "HipsTx"),
        ("HipsTy", "HipsTy"),
        ("HipsTz", "HipsTz"),
    )

    HipsTx = DoubleLinearField(default_value=0.0)

    HipsTy = DoubleLinearField(default_value=0.0)

    HipsTz = DoubleLinearField(default_value=0.0)


class HipsTAttrOperator(
    CompoundAttrOperator[HipsTPlugOperator]
):
    __slots__ = ()

    HipsTx = DoubleLinearField(default_value=0.0)

    HipsTy = DoubleLinearField(default_value=0.0)

    HipsTz = DoubleLinearField(default_value=0.0)


class HipsTField(
    CompoundField[HipsTAttrOperator, HipsTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTAttrOperator
    PLUG_CLS = HipsTPlugOperator

    HipsTx = DoubleLinearField(default_value=0.0)

    HipsTy = DoubleLinearField(default_value=0.0)

    HipsTz = DoubleLinearField(default_value=0.0)


class HipsRPlugOperator(
    CompoundPlugOperator["HipsRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsRx", "HipsRx"),
        ("HipsRy", "HipsRy"),
        ("HipsRz", "HipsRz"),
    )

    HipsRx = DoubleAngleField(default_value=0.0)

    HipsRy = DoubleAngleField(default_value=0.0)

    HipsRz = DoubleAngleField(default_value=0.0)


class HipsRAttrOperator(
    CompoundAttrOperator[HipsRPlugOperator]
):
    __slots__ = ()

    HipsRx = DoubleAngleField(default_value=0.0)

    HipsRy = DoubleAngleField(default_value=0.0)

    HipsRz = DoubleAngleField(default_value=0.0)


class HipsRField(
    CompoundField[HipsRAttrOperator, HipsRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsRAttrOperator
    PLUG_CLS = HipsRPlugOperator

    HipsRx = DoubleAngleField(default_value=0.0)

    HipsRy = DoubleAngleField(default_value=0.0)

    HipsRz = DoubleAngleField(default_value=0.0)


class HipsSPlugOperator(
    CompoundPlugOperator["HipsSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsSx", "HipsSx"),
        ("HipsSy", "HipsSy"),
        ("HipsSz", "HipsSz"),
    )

    HipsSx = DoubleField(default_value=1.0)

    HipsSy = DoubleField(default_value=1.0)

    HipsSz = DoubleField(default_value=1.0)


class HipsSAttrOperator(
    CompoundAttrOperator[HipsSPlugOperator]
):
    __slots__ = ()

    HipsSx = DoubleField(default_value=1.0)

    HipsSy = DoubleField(default_value=1.0)

    HipsSz = DoubleField(default_value=1.0)


class HipsSField(
    CompoundField[HipsSAttrOperator, HipsSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsSAttrOperator
    PLUG_CLS = HipsSPlugOperator

    HipsSx = DoubleField(default_value=1.0)

    HipsSy = DoubleField(default_value=1.0)

    HipsSz = DoubleField(default_value=1.0)


class LeftUpLegTPlugOperator(
    CompoundPlugOperator["LeftUpLegTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegTx", "LeftUpLegTx"),
        ("LeftUpLegTy", "LeftUpLegTy"),
        ("LeftUpLegTz", "LeftUpLegTz"),
    )

    LeftUpLegTx = DoubleLinearField(default_value=0.0)

    LeftUpLegTy = DoubleLinearField(default_value=0.0)

    LeftUpLegTz = DoubleLinearField(default_value=0.0)


class LeftUpLegTAttrOperator(
    CompoundAttrOperator[LeftUpLegTPlugOperator]
):
    __slots__ = ()

    LeftUpLegTx = DoubleLinearField(default_value=0.0)

    LeftUpLegTy = DoubleLinearField(default_value=0.0)

    LeftUpLegTz = DoubleLinearField(default_value=0.0)


class LeftUpLegTField(
    CompoundField[LeftUpLegTAttrOperator, LeftUpLegTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegTAttrOperator
    PLUG_CLS = LeftUpLegTPlugOperator

    LeftUpLegTx = DoubleLinearField(default_value=0.0)

    LeftUpLegTy = DoubleLinearField(default_value=0.0)

    LeftUpLegTz = DoubleLinearField(default_value=0.0)


class LeftUpLegRPlugOperator(
    CompoundPlugOperator["LeftUpLegRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegRx", "LeftUpLegRx"),
        ("LeftUpLegRy", "LeftUpLegRy"),
        ("LeftUpLegRz", "LeftUpLegRz"),
    )

    LeftUpLegRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRz = DoubleAngleField(default_value=0.0)


class LeftUpLegRAttrOperator(
    CompoundAttrOperator[LeftUpLegRPlugOperator]
):
    __slots__ = ()

    LeftUpLegRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRz = DoubleAngleField(default_value=0.0)


class LeftUpLegRField(
    CompoundField[LeftUpLegRAttrOperator, LeftUpLegRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRAttrOperator
    PLUG_CLS = LeftUpLegRPlugOperator

    LeftUpLegRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRz = DoubleAngleField(default_value=0.0)


class LeftUpLegSPlugOperator(
    CompoundPlugOperator["LeftUpLegSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegSx", "LeftUpLegSx"),
        ("LeftUpLegSy", "LeftUpLegSy"),
        ("LeftUpLegSz", "LeftUpLegSz"),
    )

    LeftUpLegSx = DoubleField(default_value=1.0)

    LeftUpLegSy = DoubleField(default_value=1.0)

    LeftUpLegSz = DoubleField(default_value=1.0)


class LeftUpLegSAttrOperator(
    CompoundAttrOperator[LeftUpLegSPlugOperator]
):
    __slots__ = ()

    LeftUpLegSx = DoubleField(default_value=1.0)

    LeftUpLegSy = DoubleField(default_value=1.0)

    LeftUpLegSz = DoubleField(default_value=1.0)


class LeftUpLegSField(
    CompoundField[LeftUpLegSAttrOperator, LeftUpLegSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegSAttrOperator
    PLUG_CLS = LeftUpLegSPlugOperator

    LeftUpLegSx = DoubleField(default_value=1.0)

    LeftUpLegSy = DoubleField(default_value=1.0)

    LeftUpLegSz = DoubleField(default_value=1.0)


class LeftLegTPlugOperator(
    CompoundPlugOperator["LeftLegTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegTx", "LeftLegTx"),
        ("LeftLegTy", "LeftLegTy"),
        ("LeftLegTz", "LeftLegTz"),
    )

    LeftLegTx = DoubleLinearField(default_value=0.0)

    LeftLegTy = DoubleLinearField(default_value=0.0)

    LeftLegTz = DoubleLinearField(default_value=0.0)


class LeftLegTAttrOperator(
    CompoundAttrOperator[LeftLegTPlugOperator]
):
    __slots__ = ()

    LeftLegTx = DoubleLinearField(default_value=0.0)

    LeftLegTy = DoubleLinearField(default_value=0.0)

    LeftLegTz = DoubleLinearField(default_value=0.0)


class LeftLegTField(
    CompoundField[LeftLegTAttrOperator, LeftLegTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegTAttrOperator
    PLUG_CLS = LeftLegTPlugOperator

    LeftLegTx = DoubleLinearField(default_value=0.0)

    LeftLegTy = DoubleLinearField(default_value=0.0)

    LeftLegTz = DoubleLinearField(default_value=0.0)


class LeftLegRPlugOperator(
    CompoundPlugOperator["LeftLegRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegRx", "LeftLegRx"),
        ("LeftLegRy", "LeftLegRy"),
        ("LeftLegRz", "LeftLegRz"),
    )

    LeftLegRx = DoubleAngleField(default_value=0.0)

    LeftLegRy = DoubleAngleField(default_value=0.0)

    LeftLegRz = DoubleAngleField(default_value=0.0)


class LeftLegRAttrOperator(
    CompoundAttrOperator[LeftLegRPlugOperator]
):
    __slots__ = ()

    LeftLegRx = DoubleAngleField(default_value=0.0)

    LeftLegRy = DoubleAngleField(default_value=0.0)

    LeftLegRz = DoubleAngleField(default_value=0.0)


class LeftLegRField(
    CompoundField[LeftLegRAttrOperator, LeftLegRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRAttrOperator
    PLUG_CLS = LeftLegRPlugOperator

    LeftLegRx = DoubleAngleField(default_value=0.0)

    LeftLegRy = DoubleAngleField(default_value=0.0)

    LeftLegRz = DoubleAngleField(default_value=0.0)


class LeftLegSPlugOperator(
    CompoundPlugOperator["LeftLegSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegSx", "LeftLegSx"),
        ("LeftLegSy", "LeftLegSy"),
        ("LeftLegSz", "LeftLegSz"),
    )

    LeftLegSx = DoubleField(default_value=1.0)

    LeftLegSy = DoubleField(default_value=1.0)

    LeftLegSz = DoubleField(default_value=1.0)


class LeftLegSAttrOperator(
    CompoundAttrOperator[LeftLegSPlugOperator]
):
    __slots__ = ()

    LeftLegSx = DoubleField(default_value=1.0)

    LeftLegSy = DoubleField(default_value=1.0)

    LeftLegSz = DoubleField(default_value=1.0)


class LeftLegSField(
    CompoundField[LeftLegSAttrOperator, LeftLegSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegSAttrOperator
    PLUG_CLS = LeftLegSPlugOperator

    LeftLegSx = DoubleField(default_value=1.0)

    LeftLegSy = DoubleField(default_value=1.0)

    LeftLegSz = DoubleField(default_value=1.0)


class LeftFootTPlugOperator(
    CompoundPlugOperator["LeftFootTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootTx", "LeftFootTx"),
        ("LeftFootTy", "LeftFootTy"),
        ("LeftFootTz", "LeftFootTz"),
    )

    LeftFootTx = DoubleLinearField(default_value=0.0)

    LeftFootTy = DoubleLinearField(default_value=0.0)

    LeftFootTz = DoubleLinearField(default_value=0.0)


class LeftFootTAttrOperator(
    CompoundAttrOperator[LeftFootTPlugOperator]
):
    __slots__ = ()

    LeftFootTx = DoubleLinearField(default_value=0.0)

    LeftFootTy = DoubleLinearField(default_value=0.0)

    LeftFootTz = DoubleLinearField(default_value=0.0)


class LeftFootTField(
    CompoundField[LeftFootTAttrOperator, LeftFootTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootTAttrOperator
    PLUG_CLS = LeftFootTPlugOperator

    LeftFootTx = DoubleLinearField(default_value=0.0)

    LeftFootTy = DoubleLinearField(default_value=0.0)

    LeftFootTz = DoubleLinearField(default_value=0.0)


class LeftFootRPlugOperator(
    CompoundPlugOperator["LeftFootRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRx", "LeftFootRx"),
        ("LeftFootRy", "LeftFootRy"),
        ("LeftFootRz", "LeftFootRz"),
    )

    LeftFootRx = DoubleAngleField(default_value=0.0)

    LeftFootRy = DoubleAngleField(default_value=0.0)

    LeftFootRz = DoubleAngleField(default_value=0.0)


class LeftFootRAttrOperator(
    CompoundAttrOperator[LeftFootRPlugOperator]
):
    __slots__ = ()

    LeftFootRx = DoubleAngleField(default_value=0.0)

    LeftFootRy = DoubleAngleField(default_value=0.0)

    LeftFootRz = DoubleAngleField(default_value=0.0)


class LeftFootRField(
    CompoundField[LeftFootRAttrOperator, LeftFootRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRAttrOperator
    PLUG_CLS = LeftFootRPlugOperator

    LeftFootRx = DoubleAngleField(default_value=0.0)

    LeftFootRy = DoubleAngleField(default_value=0.0)

    LeftFootRz = DoubleAngleField(default_value=0.0)


class LeftFootSPlugOperator(
    CompoundPlugOperator["LeftFootSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootSx", "LeftFootSx"),
        ("LeftFootSy", "LeftFootSy"),
        ("LeftFootSz", "LeftFootSz"),
    )

    LeftFootSx = DoubleField(default_value=1.0)

    LeftFootSy = DoubleField(default_value=1.0)

    LeftFootSz = DoubleField(default_value=1.0)


class LeftFootSAttrOperator(
    CompoundAttrOperator[LeftFootSPlugOperator]
):
    __slots__ = ()

    LeftFootSx = DoubleField(default_value=1.0)

    LeftFootSy = DoubleField(default_value=1.0)

    LeftFootSz = DoubleField(default_value=1.0)


class LeftFootSField(
    CompoundField[LeftFootSAttrOperator, LeftFootSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootSAttrOperator
    PLUG_CLS = LeftFootSPlugOperator

    LeftFootSx = DoubleField(default_value=1.0)

    LeftFootSy = DoubleField(default_value=1.0)

    LeftFootSz = DoubleField(default_value=1.0)


class RightUpLegTPlugOperator(
    CompoundPlugOperator["RightUpLegTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegTx", "RightUpLegTx"),
        ("RightUpLegTy", "RightUpLegTy"),
        ("RightUpLegTz", "RightUpLegTz"),
    )

    RightUpLegTx = DoubleLinearField(default_value=0.0)

    RightUpLegTy = DoubleLinearField(default_value=0.0)

    RightUpLegTz = DoubleLinearField(default_value=0.0)


class RightUpLegTAttrOperator(
    CompoundAttrOperator[RightUpLegTPlugOperator]
):
    __slots__ = ()

    RightUpLegTx = DoubleLinearField(default_value=0.0)

    RightUpLegTy = DoubleLinearField(default_value=0.0)

    RightUpLegTz = DoubleLinearField(default_value=0.0)


class RightUpLegTField(
    CompoundField[RightUpLegTAttrOperator, RightUpLegTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegTAttrOperator
    PLUG_CLS = RightUpLegTPlugOperator

    RightUpLegTx = DoubleLinearField(default_value=0.0)

    RightUpLegTy = DoubleLinearField(default_value=0.0)

    RightUpLegTz = DoubleLinearField(default_value=0.0)


class RightUpLegRPlugOperator(
    CompoundPlugOperator["RightUpLegRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegRx", "RightUpLegRx"),
        ("RightUpLegRy", "RightUpLegRy"),
        ("RightUpLegRz", "RightUpLegRz"),
    )

    RightUpLegRx = DoubleAngleField(default_value=0.0)

    RightUpLegRy = DoubleAngleField(default_value=0.0)

    RightUpLegRz = DoubleAngleField(default_value=0.0)


class RightUpLegRAttrOperator(
    CompoundAttrOperator[RightUpLegRPlugOperator]
):
    __slots__ = ()

    RightUpLegRx = DoubleAngleField(default_value=0.0)

    RightUpLegRy = DoubleAngleField(default_value=0.0)

    RightUpLegRz = DoubleAngleField(default_value=0.0)


class RightUpLegRField(
    CompoundField[RightUpLegRAttrOperator, RightUpLegRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRAttrOperator
    PLUG_CLS = RightUpLegRPlugOperator

    RightUpLegRx = DoubleAngleField(default_value=0.0)

    RightUpLegRy = DoubleAngleField(default_value=0.0)

    RightUpLegRz = DoubleAngleField(default_value=0.0)


class RightUpLegSPlugOperator(
    CompoundPlugOperator["RightUpLegSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegSx", "RightUpLegSx"),
        ("RightUpLegSy", "RightUpLegSy"),
        ("RightUpLegSz", "RightUpLegSz"),
    )

    RightUpLegSx = DoubleField(default_value=1.0)

    RightUpLegSy = DoubleField(default_value=1.0)

    RightUpLegSz = DoubleField(default_value=1.0)


class RightUpLegSAttrOperator(
    CompoundAttrOperator[RightUpLegSPlugOperator]
):
    __slots__ = ()

    RightUpLegSx = DoubleField(default_value=1.0)

    RightUpLegSy = DoubleField(default_value=1.0)

    RightUpLegSz = DoubleField(default_value=1.0)


class RightUpLegSField(
    CompoundField[RightUpLegSAttrOperator, RightUpLegSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegSAttrOperator
    PLUG_CLS = RightUpLegSPlugOperator

    RightUpLegSx = DoubleField(default_value=1.0)

    RightUpLegSy = DoubleField(default_value=1.0)

    RightUpLegSz = DoubleField(default_value=1.0)


class RightLegTPlugOperator(
    CompoundPlugOperator["RightLegTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegTx", "RightLegTx"),
        ("RightLegTy", "RightLegTy"),
        ("RightLegTz", "RightLegTz"),
    )

    RightLegTx = DoubleLinearField(default_value=0.0)

    RightLegTy = DoubleLinearField(default_value=0.0)

    RightLegTz = DoubleLinearField(default_value=0.0)


class RightLegTAttrOperator(
    CompoundAttrOperator[RightLegTPlugOperator]
):
    __slots__ = ()

    RightLegTx = DoubleLinearField(default_value=0.0)

    RightLegTy = DoubleLinearField(default_value=0.0)

    RightLegTz = DoubleLinearField(default_value=0.0)


class RightLegTField(
    CompoundField[RightLegTAttrOperator, RightLegTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegTAttrOperator
    PLUG_CLS = RightLegTPlugOperator

    RightLegTx = DoubleLinearField(default_value=0.0)

    RightLegTy = DoubleLinearField(default_value=0.0)

    RightLegTz = DoubleLinearField(default_value=0.0)


class RightLegRPlugOperator(
    CompoundPlugOperator["RightLegRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegRx", "RightLegRx"),
        ("RightLegRy", "RightLegRy"),
        ("RightLegRz", "RightLegRz"),
    )

    RightLegRx = DoubleAngleField(default_value=0.0)

    RightLegRy = DoubleAngleField(default_value=0.0)

    RightLegRz = DoubleAngleField(default_value=0.0)


class RightLegRAttrOperator(
    CompoundAttrOperator[RightLegRPlugOperator]
):
    __slots__ = ()

    RightLegRx = DoubleAngleField(default_value=0.0)

    RightLegRy = DoubleAngleField(default_value=0.0)

    RightLegRz = DoubleAngleField(default_value=0.0)


class RightLegRField(
    CompoundField[RightLegRAttrOperator, RightLegRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRAttrOperator
    PLUG_CLS = RightLegRPlugOperator

    RightLegRx = DoubleAngleField(default_value=0.0)

    RightLegRy = DoubleAngleField(default_value=0.0)

    RightLegRz = DoubleAngleField(default_value=0.0)


class RightLegSPlugOperator(
    CompoundPlugOperator["RightLegSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegSx", "RightLegSx"),
        ("RightLegSy", "RightLegSy"),
        ("RightLegSz", "RightLegSz"),
    )

    RightLegSx = DoubleField(default_value=1.0)

    RightLegSy = DoubleField(default_value=1.0)

    RightLegSz = DoubleField(default_value=1.0)


class RightLegSAttrOperator(
    CompoundAttrOperator[RightLegSPlugOperator]
):
    __slots__ = ()

    RightLegSx = DoubleField(default_value=1.0)

    RightLegSy = DoubleField(default_value=1.0)

    RightLegSz = DoubleField(default_value=1.0)


class RightLegSField(
    CompoundField[RightLegSAttrOperator, RightLegSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegSAttrOperator
    PLUG_CLS = RightLegSPlugOperator

    RightLegSx = DoubleField(default_value=1.0)

    RightLegSy = DoubleField(default_value=1.0)

    RightLegSz = DoubleField(default_value=1.0)


class RightFootTPlugOperator(
    CompoundPlugOperator["RightFootTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootTx", "RightFootTx"),
        ("RightFootTy", "RightFootTy"),
        ("RightFootTz", "RightFootTz"),
    )

    RightFootTx = DoubleLinearField(default_value=0.0)

    RightFootTy = DoubleLinearField(default_value=0.0)

    RightFootTz = DoubleLinearField(default_value=0.0)


class RightFootTAttrOperator(
    CompoundAttrOperator[RightFootTPlugOperator]
):
    __slots__ = ()

    RightFootTx = DoubleLinearField(default_value=0.0)

    RightFootTy = DoubleLinearField(default_value=0.0)

    RightFootTz = DoubleLinearField(default_value=0.0)


class RightFootTField(
    CompoundField[RightFootTAttrOperator, RightFootTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootTAttrOperator
    PLUG_CLS = RightFootTPlugOperator

    RightFootTx = DoubleLinearField(default_value=0.0)

    RightFootTy = DoubleLinearField(default_value=0.0)

    RightFootTz = DoubleLinearField(default_value=0.0)


class RightFootRPlugOperator(
    CompoundPlugOperator["RightFootRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRx", "RightFootRx"),
        ("RightFootRy", "RightFootRy"),
        ("RightFootRz", "RightFootRz"),
    )

    RightFootRx = DoubleAngleField(default_value=0.0)

    RightFootRy = DoubleAngleField(default_value=0.0)

    RightFootRz = DoubleAngleField(default_value=0.0)


class RightFootRAttrOperator(
    CompoundAttrOperator[RightFootRPlugOperator]
):
    __slots__ = ()

    RightFootRx = DoubleAngleField(default_value=0.0)

    RightFootRy = DoubleAngleField(default_value=0.0)

    RightFootRz = DoubleAngleField(default_value=0.0)


class RightFootRField(
    CompoundField[RightFootRAttrOperator, RightFootRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRAttrOperator
    PLUG_CLS = RightFootRPlugOperator

    RightFootRx = DoubleAngleField(default_value=0.0)

    RightFootRy = DoubleAngleField(default_value=0.0)

    RightFootRz = DoubleAngleField(default_value=0.0)


class RightFootSPlugOperator(
    CompoundPlugOperator["RightFootSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootSx", "RightFootSx"),
        ("RightFootSy", "RightFootSy"),
        ("RightFootSz", "RightFootSz"),
    )

    RightFootSx = DoubleField(default_value=1.0)

    RightFootSy = DoubleField(default_value=1.0)

    RightFootSz = DoubleField(default_value=1.0)


class RightFootSAttrOperator(
    CompoundAttrOperator[RightFootSPlugOperator]
):
    __slots__ = ()

    RightFootSx = DoubleField(default_value=1.0)

    RightFootSy = DoubleField(default_value=1.0)

    RightFootSz = DoubleField(default_value=1.0)


class RightFootSField(
    CompoundField[RightFootSAttrOperator, RightFootSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootSAttrOperator
    PLUG_CLS = RightFootSPlugOperator

    RightFootSx = DoubleField(default_value=1.0)

    RightFootSy = DoubleField(default_value=1.0)

    RightFootSz = DoubleField(default_value=1.0)


class SpineTPlugOperator(
    CompoundPlugOperator["SpineTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("SpineTx", "SpineTx"),
        ("SpineTy", "SpineTy"),
        ("SpineTz", "SpineTz"),
    )

    SpineTx = DoubleLinearField(default_value=0.0)

    SpineTy = DoubleLinearField(default_value=0.0)

    SpineTz = DoubleLinearField(default_value=0.0)


class SpineTAttrOperator(
    CompoundAttrOperator[SpineTPlugOperator]
):
    __slots__ = ()

    SpineTx = DoubleLinearField(default_value=0.0)

    SpineTy = DoubleLinearField(default_value=0.0)

    SpineTz = DoubleLinearField(default_value=0.0)


class SpineTField(
    CompoundField[SpineTAttrOperator, SpineTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpineTAttrOperator
    PLUG_CLS = SpineTPlugOperator

    SpineTx = DoubleLinearField(default_value=0.0)

    SpineTy = DoubleLinearField(default_value=0.0)

    SpineTz = DoubleLinearField(default_value=0.0)


class SpineRPlugOperator(
    CompoundPlugOperator["SpineRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("SpineRx", "SpineRx"),
        ("SpineRy", "SpineRy"),
        ("SpineRz", "SpineRz"),
    )

    SpineRx = DoubleAngleField(default_value=0.0)

    SpineRy = DoubleAngleField(default_value=0.0)

    SpineRz = DoubleAngleField(default_value=0.0)


class SpineRAttrOperator(
    CompoundAttrOperator[SpineRPlugOperator]
):
    __slots__ = ()

    SpineRx = DoubleAngleField(default_value=0.0)

    SpineRy = DoubleAngleField(default_value=0.0)

    SpineRz = DoubleAngleField(default_value=0.0)


class SpineRField(
    CompoundField[SpineRAttrOperator, SpineRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpineRAttrOperator
    PLUG_CLS = SpineRPlugOperator

    SpineRx = DoubleAngleField(default_value=0.0)

    SpineRy = DoubleAngleField(default_value=0.0)

    SpineRz = DoubleAngleField(default_value=0.0)


class SpineSPlugOperator(
    CompoundPlugOperator["SpineSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("SpineSx", "SpineSx"),
        ("SpineSy", "SpineSy"),
        ("SpineSz", "SpineSz"),
    )

    SpineSx = DoubleField(default_value=1.0)

    SpineSy = DoubleField(default_value=1.0)

    SpineSz = DoubleField(default_value=1.0)


class SpineSAttrOperator(
    CompoundAttrOperator[SpineSPlugOperator]
):
    __slots__ = ()

    SpineSx = DoubleField(default_value=1.0)

    SpineSy = DoubleField(default_value=1.0)

    SpineSz = DoubleField(default_value=1.0)


class SpineSField(
    CompoundField[SpineSAttrOperator, SpineSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SpineSAttrOperator
    PLUG_CLS = SpineSPlugOperator

    SpineSx = DoubleField(default_value=1.0)

    SpineSy = DoubleField(default_value=1.0)

    SpineSz = DoubleField(default_value=1.0)


class LeftArmTPlugOperator(
    CompoundPlugOperator["LeftArmTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmTx", "LeftArmTx"),
        ("LeftArmTy", "LeftArmTy"),
        ("LeftArmTz", "LeftArmTz"),
    )

    LeftArmTx = DoubleLinearField(default_value=0.0)

    LeftArmTy = DoubleLinearField(default_value=0.0)

    LeftArmTz = DoubleLinearField(default_value=0.0)


class LeftArmTAttrOperator(
    CompoundAttrOperator[LeftArmTPlugOperator]
):
    __slots__ = ()

    LeftArmTx = DoubleLinearField(default_value=0.0)

    LeftArmTy = DoubleLinearField(default_value=0.0)

    LeftArmTz = DoubleLinearField(default_value=0.0)


class LeftArmTField(
    CompoundField[LeftArmTAttrOperator, LeftArmTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmTAttrOperator
    PLUG_CLS = LeftArmTPlugOperator

    LeftArmTx = DoubleLinearField(default_value=0.0)

    LeftArmTy = DoubleLinearField(default_value=0.0)

    LeftArmTz = DoubleLinearField(default_value=0.0)


class LeftArmRPlugOperator(
    CompoundPlugOperator["LeftArmRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmRx", "LeftArmRx"),
        ("LeftArmRy", "LeftArmRy"),
        ("LeftArmRz", "LeftArmRz"),
    )

    LeftArmRx = DoubleAngleField(default_value=0.0)

    LeftArmRy = DoubleAngleField(default_value=0.0)

    LeftArmRz = DoubleAngleField(default_value=0.0)


class LeftArmRAttrOperator(
    CompoundAttrOperator[LeftArmRPlugOperator]
):
    __slots__ = ()

    LeftArmRx = DoubleAngleField(default_value=0.0)

    LeftArmRy = DoubleAngleField(default_value=0.0)

    LeftArmRz = DoubleAngleField(default_value=0.0)


class LeftArmRField(
    CompoundField[LeftArmRAttrOperator, LeftArmRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRAttrOperator
    PLUG_CLS = LeftArmRPlugOperator

    LeftArmRx = DoubleAngleField(default_value=0.0)

    LeftArmRy = DoubleAngleField(default_value=0.0)

    LeftArmRz = DoubleAngleField(default_value=0.0)


class LeftArmSPlugOperator(
    CompoundPlugOperator["LeftArmSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmSx", "LeftArmSx"),
        ("LeftArmSy", "LeftArmSy"),
        ("LeftArmSz", "LeftArmSz"),
    )

    LeftArmSx = DoubleField(default_value=1.0)

    LeftArmSy = DoubleField(default_value=1.0)

    LeftArmSz = DoubleField(default_value=1.0)


class LeftArmSAttrOperator(
    CompoundAttrOperator[LeftArmSPlugOperator]
):
    __slots__ = ()

    LeftArmSx = DoubleField(default_value=1.0)

    LeftArmSy = DoubleField(default_value=1.0)

    LeftArmSz = DoubleField(default_value=1.0)


class LeftArmSField(
    CompoundField[LeftArmSAttrOperator, LeftArmSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmSAttrOperator
    PLUG_CLS = LeftArmSPlugOperator

    LeftArmSx = DoubleField(default_value=1.0)

    LeftArmSy = DoubleField(default_value=1.0)

    LeftArmSz = DoubleField(default_value=1.0)


class LeftForeArmTPlugOperator(
    CompoundPlugOperator["LeftForeArmTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmTx", "LeftForeArmTx"),
        ("LeftForeArmTy", "LeftForeArmTy"),
        ("LeftForeArmTz", "LeftForeArmTz"),
    )

    LeftForeArmTx = DoubleLinearField(default_value=0.0)

    LeftForeArmTy = DoubleLinearField(default_value=0.0)

    LeftForeArmTz = DoubleLinearField(default_value=0.0)


class LeftForeArmTAttrOperator(
    CompoundAttrOperator[LeftForeArmTPlugOperator]
):
    __slots__ = ()

    LeftForeArmTx = DoubleLinearField(default_value=0.0)

    LeftForeArmTy = DoubleLinearField(default_value=0.0)

    LeftForeArmTz = DoubleLinearField(default_value=0.0)


class LeftForeArmTField(
    CompoundField[LeftForeArmTAttrOperator, LeftForeArmTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmTAttrOperator
    PLUG_CLS = LeftForeArmTPlugOperator

    LeftForeArmTx = DoubleLinearField(default_value=0.0)

    LeftForeArmTy = DoubleLinearField(default_value=0.0)

    LeftForeArmTz = DoubleLinearField(default_value=0.0)


class LeftForeArmRPlugOperator(
    CompoundPlugOperator["LeftForeArmRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmRx", "LeftForeArmRx"),
        ("LeftForeArmRy", "LeftForeArmRy"),
        ("LeftForeArmRz", "LeftForeArmRz"),
    )

    LeftForeArmRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRz = DoubleAngleField(default_value=0.0)


class LeftForeArmRAttrOperator(
    CompoundAttrOperator[LeftForeArmRPlugOperator]
):
    __slots__ = ()

    LeftForeArmRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRz = DoubleAngleField(default_value=0.0)


class LeftForeArmRField(
    CompoundField[LeftForeArmRAttrOperator, LeftForeArmRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRAttrOperator
    PLUG_CLS = LeftForeArmRPlugOperator

    LeftForeArmRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRz = DoubleAngleField(default_value=0.0)


class LeftForeArmSPlugOperator(
    CompoundPlugOperator["LeftForeArmSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmSx", "LeftForeArmSx"),
        ("LeftForeArmSy", "LeftForeArmSy"),
        ("LeftForeArmSz", "LeftForeArmSz"),
    )

    LeftForeArmSx = DoubleField(default_value=1.0)

    LeftForeArmSy = DoubleField(default_value=1.0)

    LeftForeArmSz = DoubleField(default_value=1.0)


class LeftForeArmSAttrOperator(
    CompoundAttrOperator[LeftForeArmSPlugOperator]
):
    __slots__ = ()

    LeftForeArmSx = DoubleField(default_value=1.0)

    LeftForeArmSy = DoubleField(default_value=1.0)

    LeftForeArmSz = DoubleField(default_value=1.0)


class LeftForeArmSField(
    CompoundField[LeftForeArmSAttrOperator, LeftForeArmSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmSAttrOperator
    PLUG_CLS = LeftForeArmSPlugOperator

    LeftForeArmSx = DoubleField(default_value=1.0)

    LeftForeArmSy = DoubleField(default_value=1.0)

    LeftForeArmSz = DoubleField(default_value=1.0)


class LeftHandTPlugOperator(
    CompoundPlugOperator["LeftHandTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandTx", "LeftHandTx"),
        ("LeftHandTy", "LeftHandTy"),
        ("LeftHandTz", "LeftHandTz"),
    )

    LeftHandTx = DoubleLinearField(default_value=0.0)

    LeftHandTy = DoubleLinearField(default_value=0.0)

    LeftHandTz = DoubleLinearField(default_value=0.0)


class LeftHandTAttrOperator(
    CompoundAttrOperator[LeftHandTPlugOperator]
):
    __slots__ = ()

    LeftHandTx = DoubleLinearField(default_value=0.0)

    LeftHandTy = DoubleLinearField(default_value=0.0)

    LeftHandTz = DoubleLinearField(default_value=0.0)


class LeftHandTField(
    CompoundField[LeftHandTAttrOperator, LeftHandTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandTAttrOperator
    PLUG_CLS = LeftHandTPlugOperator

    LeftHandTx = DoubleLinearField(default_value=0.0)

    LeftHandTy = DoubleLinearField(default_value=0.0)

    LeftHandTz = DoubleLinearField(default_value=0.0)


class LeftHandRPlugOperator(
    CompoundPlugOperator["LeftHandRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRx", "LeftHandRx"),
        ("LeftHandRy", "LeftHandRy"),
        ("LeftHandRz", "LeftHandRz"),
    )

    LeftHandRx = DoubleAngleField(default_value=0.0)

    LeftHandRy = DoubleAngleField(default_value=0.0)

    LeftHandRz = DoubleAngleField(default_value=0.0)


class LeftHandRAttrOperator(
    CompoundAttrOperator[LeftHandRPlugOperator]
):
    __slots__ = ()

    LeftHandRx = DoubleAngleField(default_value=0.0)

    LeftHandRy = DoubleAngleField(default_value=0.0)

    LeftHandRz = DoubleAngleField(default_value=0.0)


class LeftHandRField(
    CompoundField[LeftHandRAttrOperator, LeftHandRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRAttrOperator
    PLUG_CLS = LeftHandRPlugOperator

    LeftHandRx = DoubleAngleField(default_value=0.0)

    LeftHandRy = DoubleAngleField(default_value=0.0)

    LeftHandRz = DoubleAngleField(default_value=0.0)


class LeftHandSPlugOperator(
    CompoundPlugOperator["LeftHandSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandSx", "LeftHandSx"),
        ("LeftHandSy", "LeftHandSy"),
        ("LeftHandSz", "LeftHandSz"),
    )

    LeftHandSx = DoubleField(default_value=1.0)

    LeftHandSy = DoubleField(default_value=1.0)

    LeftHandSz = DoubleField(default_value=1.0)


class LeftHandSAttrOperator(
    CompoundAttrOperator[LeftHandSPlugOperator]
):
    __slots__ = ()

    LeftHandSx = DoubleField(default_value=1.0)

    LeftHandSy = DoubleField(default_value=1.0)

    LeftHandSz = DoubleField(default_value=1.0)


class LeftHandSField(
    CompoundField[LeftHandSAttrOperator, LeftHandSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandSAttrOperator
    PLUG_CLS = LeftHandSPlugOperator

    LeftHandSx = DoubleField(default_value=1.0)

    LeftHandSy = DoubleField(default_value=1.0)

    LeftHandSz = DoubleField(default_value=1.0)


class RightArmTPlugOperator(
    CompoundPlugOperator["RightArmTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmTx", "RightArmTx"),
        ("RightArmTy", "RightArmTy"),
        ("RightArmTz", "RightArmTz"),
    )

    RightArmTx = DoubleLinearField(default_value=0.0)

    RightArmTy = DoubleLinearField(default_value=0.0)

    RightArmTz = DoubleLinearField(default_value=0.0)


class RightArmTAttrOperator(
    CompoundAttrOperator[RightArmTPlugOperator]
):
    __slots__ = ()

    RightArmTx = DoubleLinearField(default_value=0.0)

    RightArmTy = DoubleLinearField(default_value=0.0)

    RightArmTz = DoubleLinearField(default_value=0.0)


class RightArmTField(
    CompoundField[RightArmTAttrOperator, RightArmTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmTAttrOperator
    PLUG_CLS = RightArmTPlugOperator

    RightArmTx = DoubleLinearField(default_value=0.0)

    RightArmTy = DoubleLinearField(default_value=0.0)

    RightArmTz = DoubleLinearField(default_value=0.0)


class RightArmRPlugOperator(
    CompoundPlugOperator["RightArmRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmRx", "RightArmRx"),
        ("RightArmRy", "RightArmRy"),
        ("RightArmRz", "RightArmRz"),
    )

    RightArmRx = DoubleAngleField(default_value=0.0)

    RightArmRy = DoubleAngleField(default_value=0.0)

    RightArmRz = DoubleAngleField(default_value=0.0)


class RightArmRAttrOperator(
    CompoundAttrOperator[RightArmRPlugOperator]
):
    __slots__ = ()

    RightArmRx = DoubleAngleField(default_value=0.0)

    RightArmRy = DoubleAngleField(default_value=0.0)

    RightArmRz = DoubleAngleField(default_value=0.0)


class RightArmRField(
    CompoundField[RightArmRAttrOperator, RightArmRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRAttrOperator
    PLUG_CLS = RightArmRPlugOperator

    RightArmRx = DoubleAngleField(default_value=0.0)

    RightArmRy = DoubleAngleField(default_value=0.0)

    RightArmRz = DoubleAngleField(default_value=0.0)


class RightArmSPlugOperator(
    CompoundPlugOperator["RightArmSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmSx", "RightArmSx"),
        ("RightArmSy", "RightArmSy"),
        ("RightArmSz", "RightArmSz"),
    )

    RightArmSx = DoubleField(default_value=1.0)

    RightArmSy = DoubleField(default_value=1.0)

    RightArmSz = DoubleField(default_value=1.0)


class RightArmSAttrOperator(
    CompoundAttrOperator[RightArmSPlugOperator]
):
    __slots__ = ()

    RightArmSx = DoubleField(default_value=1.0)

    RightArmSy = DoubleField(default_value=1.0)

    RightArmSz = DoubleField(default_value=1.0)


class RightArmSField(
    CompoundField[RightArmSAttrOperator, RightArmSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmSAttrOperator
    PLUG_CLS = RightArmSPlugOperator

    RightArmSx = DoubleField(default_value=1.0)

    RightArmSy = DoubleField(default_value=1.0)

    RightArmSz = DoubleField(default_value=1.0)


class RightForeArmTPlugOperator(
    CompoundPlugOperator["RightForeArmTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmTx", "RightForeArmTx"),
        ("RightForeArmTy", "RightForeArmTy"),
        ("RightForeArmTz", "RightForeArmTz"),
    )

    RightForeArmTx = DoubleLinearField(default_value=0.0)

    RightForeArmTy = DoubleLinearField(default_value=0.0)

    RightForeArmTz = DoubleLinearField(default_value=0.0)


class RightForeArmTAttrOperator(
    CompoundAttrOperator[RightForeArmTPlugOperator]
):
    __slots__ = ()

    RightForeArmTx = DoubleLinearField(default_value=0.0)

    RightForeArmTy = DoubleLinearField(default_value=0.0)

    RightForeArmTz = DoubleLinearField(default_value=0.0)


class RightForeArmTField(
    CompoundField[RightForeArmTAttrOperator, RightForeArmTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmTAttrOperator
    PLUG_CLS = RightForeArmTPlugOperator

    RightForeArmTx = DoubleLinearField(default_value=0.0)

    RightForeArmTy = DoubleLinearField(default_value=0.0)

    RightForeArmTz = DoubleLinearField(default_value=0.0)


class RightForeArmRPlugOperator(
    CompoundPlugOperator["RightForeArmRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmRx", "RightForeArmRx"),
        ("RightForeArmRy", "RightForeArmRy"),
        ("RightForeArmRz", "RightForeArmRz"),
    )

    RightForeArmRx = DoubleAngleField(default_value=0.0)

    RightForeArmRy = DoubleAngleField(default_value=0.0)

    RightForeArmRz = DoubleAngleField(default_value=0.0)


class RightForeArmRAttrOperator(
    CompoundAttrOperator[RightForeArmRPlugOperator]
):
    __slots__ = ()

    RightForeArmRx = DoubleAngleField(default_value=0.0)

    RightForeArmRy = DoubleAngleField(default_value=0.0)

    RightForeArmRz = DoubleAngleField(default_value=0.0)


class RightForeArmRField(
    CompoundField[RightForeArmRAttrOperator, RightForeArmRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRAttrOperator
    PLUG_CLS = RightForeArmRPlugOperator

    RightForeArmRx = DoubleAngleField(default_value=0.0)

    RightForeArmRy = DoubleAngleField(default_value=0.0)

    RightForeArmRz = DoubleAngleField(default_value=0.0)


class RightForeArmSPlugOperator(
    CompoundPlugOperator["RightForeArmSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmSx", "RightForeArmSx"),
        ("RightForeArmSy", "RightForeArmSy"),
        ("RightForeArmSz", "RightForeArmSz"),
    )

    RightForeArmSx = DoubleField(default_value=1.0)

    RightForeArmSy = DoubleField(default_value=1.0)

    RightForeArmSz = DoubleField(default_value=1.0)


class RightForeArmSAttrOperator(
    CompoundAttrOperator[RightForeArmSPlugOperator]
):
    __slots__ = ()

    RightForeArmSx = DoubleField(default_value=1.0)

    RightForeArmSy = DoubleField(default_value=1.0)

    RightForeArmSz = DoubleField(default_value=1.0)


class RightForeArmSField(
    CompoundField[RightForeArmSAttrOperator, RightForeArmSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmSAttrOperator
    PLUG_CLS = RightForeArmSPlugOperator

    RightForeArmSx = DoubleField(default_value=1.0)

    RightForeArmSy = DoubleField(default_value=1.0)

    RightForeArmSz = DoubleField(default_value=1.0)


class RightHandTPlugOperator(
    CompoundPlugOperator["RightHandTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandTx", "RightHandTx"),
        ("RightHandTy", "RightHandTy"),
        ("RightHandTz", "RightHandTz"),
    )

    RightHandTx = DoubleLinearField(default_value=0.0)

    RightHandTy = DoubleLinearField(default_value=0.0)

    RightHandTz = DoubleLinearField(default_value=0.0)


class RightHandTAttrOperator(
    CompoundAttrOperator[RightHandTPlugOperator]
):
    __slots__ = ()

    RightHandTx = DoubleLinearField(default_value=0.0)

    RightHandTy = DoubleLinearField(default_value=0.0)

    RightHandTz = DoubleLinearField(default_value=0.0)


class RightHandTField(
    CompoundField[RightHandTAttrOperator, RightHandTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandTAttrOperator
    PLUG_CLS = RightHandTPlugOperator

    RightHandTx = DoubleLinearField(default_value=0.0)

    RightHandTy = DoubleLinearField(default_value=0.0)

    RightHandTz = DoubleLinearField(default_value=0.0)


class RightHandRPlugOperator(
    CompoundPlugOperator["RightHandRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRx", "RightHandRx"),
        ("RightHandRy", "RightHandRy"),
        ("RightHandRz", "RightHandRz"),
    )

    RightHandRx = DoubleAngleField(default_value=0.0)

    RightHandRy = DoubleAngleField(default_value=0.0)

    RightHandRz = DoubleAngleField(default_value=0.0)


class RightHandRAttrOperator(
    CompoundAttrOperator[RightHandRPlugOperator]
):
    __slots__ = ()

    RightHandRx = DoubleAngleField(default_value=0.0)

    RightHandRy = DoubleAngleField(default_value=0.0)

    RightHandRz = DoubleAngleField(default_value=0.0)


class RightHandRField(
    CompoundField[RightHandRAttrOperator, RightHandRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRAttrOperator
    PLUG_CLS = RightHandRPlugOperator

    RightHandRx = DoubleAngleField(default_value=0.0)

    RightHandRy = DoubleAngleField(default_value=0.0)

    RightHandRz = DoubleAngleField(default_value=0.0)


class RightHandSPlugOperator(
    CompoundPlugOperator["RightHandSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandSx", "RightHandSx"),
        ("RightHandSy", "RightHandSy"),
        ("RightHandSz", "RightHandSz"),
    )

    RightHandSx = DoubleField(default_value=1.0)

    RightHandSy = DoubleField(default_value=1.0)

    RightHandSz = DoubleField(default_value=1.0)


class RightHandSAttrOperator(
    CompoundAttrOperator[RightHandSPlugOperator]
):
    __slots__ = ()

    RightHandSx = DoubleField(default_value=1.0)

    RightHandSy = DoubleField(default_value=1.0)

    RightHandSz = DoubleField(default_value=1.0)


class RightHandSField(
    CompoundField[RightHandSAttrOperator, RightHandSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandSAttrOperator
    PLUG_CLS = RightHandSPlugOperator

    RightHandSx = DoubleField(default_value=1.0)

    RightHandSy = DoubleField(default_value=1.0)

    RightHandSz = DoubleField(default_value=1.0)


class HeadTPlugOperator(
    CompoundPlugOperator["HeadTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HeadTx", "HeadTx"),
        ("HeadTy", "HeadTy"),
        ("HeadTz", "HeadTz"),
    )

    HeadTx = DoubleLinearField(default_value=0.0)

    HeadTy = DoubleLinearField(default_value=0.0)

    HeadTz = DoubleLinearField(default_value=0.0)


class HeadTAttrOperator(
    CompoundAttrOperator[HeadTPlugOperator]
):
    __slots__ = ()

    HeadTx = DoubleLinearField(default_value=0.0)

    HeadTy = DoubleLinearField(default_value=0.0)

    HeadTz = DoubleLinearField(default_value=0.0)


class HeadTField(
    CompoundField[HeadTAttrOperator, HeadTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadTAttrOperator
    PLUG_CLS = HeadTPlugOperator

    HeadTx = DoubleLinearField(default_value=0.0)

    HeadTy = DoubleLinearField(default_value=0.0)

    HeadTz = DoubleLinearField(default_value=0.0)


class HeadRPlugOperator(
    CompoundPlugOperator["HeadRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HeadRx", "HeadRx"),
        ("HeadRy", "HeadRy"),
        ("HeadRz", "HeadRz"),
    )

    HeadRx = DoubleAngleField(default_value=0.0)

    HeadRy = DoubleAngleField(default_value=0.0)

    HeadRz = DoubleAngleField(default_value=0.0)


class HeadRAttrOperator(
    CompoundAttrOperator[HeadRPlugOperator]
):
    __slots__ = ()

    HeadRx = DoubleAngleField(default_value=0.0)

    HeadRy = DoubleAngleField(default_value=0.0)

    HeadRz = DoubleAngleField(default_value=0.0)


class HeadRField(
    CompoundField[HeadRAttrOperator, HeadRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadRAttrOperator
    PLUG_CLS = HeadRPlugOperator

    HeadRx = DoubleAngleField(default_value=0.0)

    HeadRy = DoubleAngleField(default_value=0.0)

    HeadRz = DoubleAngleField(default_value=0.0)


class HeadSPlugOperator(
    CompoundPlugOperator["HeadSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HeadSx", "HeadSx"),
        ("HeadSy", "HeadSy"),
        ("HeadSz", "HeadSz"),
    )

    HeadSx = DoubleField(default_value=1.0)

    HeadSy = DoubleField(default_value=1.0)

    HeadSz = DoubleField(default_value=1.0)


class HeadSAttrOperator(
    CompoundAttrOperator[HeadSPlugOperator]
):
    __slots__ = ()

    HeadSx = DoubleField(default_value=1.0)

    HeadSy = DoubleField(default_value=1.0)

    HeadSz = DoubleField(default_value=1.0)


class HeadSField(
    CompoundField[HeadSAttrOperator, HeadSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HeadSAttrOperator
    PLUG_CLS = HeadSPlugOperator

    HeadSx = DoubleField(default_value=1.0)

    HeadSy = DoubleField(default_value=1.0)

    HeadSz = DoubleField(default_value=1.0)


class LeftToeBaseTPlugOperator(
    CompoundPlugOperator["LeftToeBaseTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftToeBaseTx", "LeftToeBaseTx"),
        ("LeftToeBaseTy", "LeftToeBaseTy"),
        ("LeftToeBaseTz", "LeftToeBaseTz"),
    )

    LeftToeBaseTx = DoubleLinearField(default_value=0.0)

    LeftToeBaseTy = DoubleLinearField(default_value=0.0)

    LeftToeBaseTz = DoubleLinearField(default_value=0.0)


class LeftToeBaseTAttrOperator(
    CompoundAttrOperator[LeftToeBaseTPlugOperator]
):
    __slots__ = ()

    LeftToeBaseTx = DoubleLinearField(default_value=0.0)

    LeftToeBaseTy = DoubleLinearField(default_value=0.0)

    LeftToeBaseTz = DoubleLinearField(default_value=0.0)


class LeftToeBaseTField(
    CompoundField[LeftToeBaseTAttrOperator, LeftToeBaseTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftToeBaseTAttrOperator
    PLUG_CLS = LeftToeBaseTPlugOperator

    LeftToeBaseTx = DoubleLinearField(default_value=0.0)

    LeftToeBaseTy = DoubleLinearField(default_value=0.0)

    LeftToeBaseTz = DoubleLinearField(default_value=0.0)


class LeftToeBaseRPlugOperator(
    CompoundPlugOperator["LeftToeBaseRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftToeBaseRx", "LeftToeBaseRx"),
        ("LeftToeBaseRy", "LeftToeBaseRy"),
        ("LeftToeBaseRz", "LeftToeBaseRz"),
    )

    LeftToeBaseRx = DoubleAngleField(default_value=0.0)

    LeftToeBaseRy = DoubleAngleField(default_value=0.0)

    LeftToeBaseRz = DoubleAngleField(default_value=0.0)


class LeftToeBaseRAttrOperator(
    CompoundAttrOperator[LeftToeBaseRPlugOperator]
):
    __slots__ = ()

    LeftToeBaseRx = DoubleAngleField(default_value=0.0)

    LeftToeBaseRy = DoubleAngleField(default_value=0.0)

    LeftToeBaseRz = DoubleAngleField(default_value=0.0)


class LeftToeBaseRField(
    CompoundField[LeftToeBaseRAttrOperator, LeftToeBaseRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftToeBaseRAttrOperator
    PLUG_CLS = LeftToeBaseRPlugOperator

    LeftToeBaseRx = DoubleAngleField(default_value=0.0)

    LeftToeBaseRy = DoubleAngleField(default_value=0.0)

    LeftToeBaseRz = DoubleAngleField(default_value=0.0)


class LeftToeBaseSPlugOperator(
    CompoundPlugOperator["LeftToeBaseSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftToeBaseSx", "LeftToeBaseSx"),
        ("LeftToeBaseSy", "LeftToeBaseSy"),
        ("LeftToeBaseSz", "LeftToeBaseSz"),
    )

    LeftToeBaseSx = DoubleField(default_value=1.0)

    LeftToeBaseSy = DoubleField(default_value=1.0)

    LeftToeBaseSz = DoubleField(default_value=1.0)


class LeftToeBaseSAttrOperator(
    CompoundAttrOperator[LeftToeBaseSPlugOperator]
):
    __slots__ = ()

    LeftToeBaseSx = DoubleField(default_value=1.0)

    LeftToeBaseSy = DoubleField(default_value=1.0)

    LeftToeBaseSz = DoubleField(default_value=1.0)


class LeftToeBaseSField(
    CompoundField[LeftToeBaseSAttrOperator, LeftToeBaseSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftToeBaseSAttrOperator
    PLUG_CLS = LeftToeBaseSPlugOperator

    LeftToeBaseSx = DoubleField(default_value=1.0)

    LeftToeBaseSy = DoubleField(default_value=1.0)

    LeftToeBaseSz = DoubleField(default_value=1.0)


class RightToeBaseTPlugOperator(
    CompoundPlugOperator["RightToeBaseTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightToeBaseTx", "RightToeBaseTx"),
        ("RightToeBaseTy", "RightToeBaseTy"),
        ("RightToeBaseTz", "RightToeBaseTz"),
    )

    RightToeBaseTx = DoubleLinearField(default_value=0.0)

    RightToeBaseTy = DoubleLinearField(default_value=0.0)

    RightToeBaseTz = DoubleLinearField(default_value=0.0)


class RightToeBaseTAttrOperator(
    CompoundAttrOperator[RightToeBaseTPlugOperator]
):
    __slots__ = ()

    RightToeBaseTx = DoubleLinearField(default_value=0.0)

    RightToeBaseTy = DoubleLinearField(default_value=0.0)

    RightToeBaseTz = DoubleLinearField(default_value=0.0)


class RightToeBaseTField(
    CompoundField[RightToeBaseTAttrOperator, RightToeBaseTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightToeBaseTAttrOperator
    PLUG_CLS = RightToeBaseTPlugOperator

    RightToeBaseTx = DoubleLinearField(default_value=0.0)

    RightToeBaseTy = DoubleLinearField(default_value=0.0)

    RightToeBaseTz = DoubleLinearField(default_value=0.0)


class RightToeBaseRPlugOperator(
    CompoundPlugOperator["RightToeBaseRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightToeBaseRx", "RightToeBaseRx"),
        ("RightToeBaseRy", "RightToeBaseRy"),
        ("RightToeBaseRz", "RightToeBaseRz"),
    )

    RightToeBaseRx = DoubleAngleField(default_value=0.0)

    RightToeBaseRy = DoubleAngleField(default_value=0.0)

    RightToeBaseRz = DoubleAngleField(default_value=0.0)


class RightToeBaseRAttrOperator(
    CompoundAttrOperator[RightToeBaseRPlugOperator]
):
    __slots__ = ()

    RightToeBaseRx = DoubleAngleField(default_value=0.0)

    RightToeBaseRy = DoubleAngleField(default_value=0.0)

    RightToeBaseRz = DoubleAngleField(default_value=0.0)


class RightToeBaseRField(
    CompoundField[RightToeBaseRAttrOperator, RightToeBaseRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightToeBaseRAttrOperator
    PLUG_CLS = RightToeBaseRPlugOperator

    RightToeBaseRx = DoubleAngleField(default_value=0.0)

    RightToeBaseRy = DoubleAngleField(default_value=0.0)

    RightToeBaseRz = DoubleAngleField(default_value=0.0)


class RightToeBaseSPlugOperator(
    CompoundPlugOperator["RightToeBaseSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightToeBaseSx", "RightToeBaseSx"),
        ("RightToeBaseSy", "RightToeBaseSy"),
        ("RightToeBaseSz", "RightToeBaseSz"),
    )

    RightToeBaseSx = DoubleField(default_value=1.0)

    RightToeBaseSy = DoubleField(default_value=1.0)

    RightToeBaseSz = DoubleField(default_value=1.0)


class RightToeBaseSAttrOperator(
    CompoundAttrOperator[RightToeBaseSPlugOperator]
):
    __slots__ = ()

    RightToeBaseSx = DoubleField(default_value=1.0)

    RightToeBaseSy = DoubleField(default_value=1.0)

    RightToeBaseSz = DoubleField(default_value=1.0)


class RightToeBaseSField(
    CompoundField[RightToeBaseSAttrOperator, RightToeBaseSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightToeBaseSAttrOperator
    PLUG_CLS = RightToeBaseSPlugOperator

    RightToeBaseSx = DoubleField(default_value=1.0)

    RightToeBaseSy = DoubleField(default_value=1.0)

    RightToeBaseSz = DoubleField(default_value=1.0)


class LeftShoulderTPlugOperator(
    CompoundPlugOperator["LeftShoulderTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderTx", "LeftShoulderTx"),
        ("LeftShoulderTy", "LeftShoulderTy"),
        ("LeftShoulderTz", "LeftShoulderTz"),
    )

    LeftShoulderTx = DoubleLinearField(default_value=0.0)

    LeftShoulderTy = DoubleLinearField(default_value=0.0)

    LeftShoulderTz = DoubleLinearField(default_value=0.0)


class LeftShoulderTAttrOperator(
    CompoundAttrOperator[LeftShoulderTPlugOperator]
):
    __slots__ = ()

    LeftShoulderTx = DoubleLinearField(default_value=0.0)

    LeftShoulderTy = DoubleLinearField(default_value=0.0)

    LeftShoulderTz = DoubleLinearField(default_value=0.0)


class LeftShoulderTField(
    CompoundField[LeftShoulderTAttrOperator, LeftShoulderTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderTAttrOperator
    PLUG_CLS = LeftShoulderTPlugOperator

    LeftShoulderTx = DoubleLinearField(default_value=0.0)

    LeftShoulderTy = DoubleLinearField(default_value=0.0)

    LeftShoulderTz = DoubleLinearField(default_value=0.0)


class LeftShoulderRPlugOperator(
    CompoundPlugOperator["LeftShoulderRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderRx", "LeftShoulderRx"),
        ("LeftShoulderRy", "LeftShoulderRy"),
        ("LeftShoulderRz", "LeftShoulderRz"),
    )

    LeftShoulderRx = DoubleAngleField(default_value=0.0)

    LeftShoulderRy = DoubleAngleField(default_value=0.0)

    LeftShoulderRz = DoubleAngleField(default_value=0.0)


class LeftShoulderRAttrOperator(
    CompoundAttrOperator[LeftShoulderRPlugOperator]
):
    __slots__ = ()

    LeftShoulderRx = DoubleAngleField(default_value=0.0)

    LeftShoulderRy = DoubleAngleField(default_value=0.0)

    LeftShoulderRz = DoubleAngleField(default_value=0.0)


class LeftShoulderRField(
    CompoundField[LeftShoulderRAttrOperator, LeftShoulderRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderRAttrOperator
    PLUG_CLS = LeftShoulderRPlugOperator

    LeftShoulderRx = DoubleAngleField(default_value=0.0)

    LeftShoulderRy = DoubleAngleField(default_value=0.0)

    LeftShoulderRz = DoubleAngleField(default_value=0.0)


class LeftShoulderSPlugOperator(
    CompoundPlugOperator["LeftShoulderSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderSx", "LeftShoulderSx"),
        ("LeftShoulderSy", "LeftShoulderSy"),
        ("LeftShoulderSz", "LeftShoulderSz"),
    )

    LeftShoulderSx = DoubleField(default_value=1.0)

    LeftShoulderSy = DoubleField(default_value=1.0)

    LeftShoulderSz = DoubleField(default_value=1.0)


class LeftShoulderSAttrOperator(
    CompoundAttrOperator[LeftShoulderSPlugOperator]
):
    __slots__ = ()

    LeftShoulderSx = DoubleField(default_value=1.0)

    LeftShoulderSy = DoubleField(default_value=1.0)

    LeftShoulderSz = DoubleField(default_value=1.0)


class LeftShoulderSField(
    CompoundField[LeftShoulderSAttrOperator, LeftShoulderSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderSAttrOperator
    PLUG_CLS = LeftShoulderSPlugOperator

    LeftShoulderSx = DoubleField(default_value=1.0)

    LeftShoulderSy = DoubleField(default_value=1.0)

    LeftShoulderSz = DoubleField(default_value=1.0)


class RightShoulderTPlugOperator(
    CompoundPlugOperator["RightShoulderTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderTx", "RightShoulderTx"),
        ("RightShoulderTy", "RightShoulderTy"),
        ("RightShoulderTz", "RightShoulderTz"),
    )

    RightShoulderTx = DoubleLinearField(default_value=0.0)

    RightShoulderTy = DoubleLinearField(default_value=0.0)

    RightShoulderTz = DoubleLinearField(default_value=0.0)


class RightShoulderTAttrOperator(
    CompoundAttrOperator[RightShoulderTPlugOperator]
):
    __slots__ = ()

    RightShoulderTx = DoubleLinearField(default_value=0.0)

    RightShoulderTy = DoubleLinearField(default_value=0.0)

    RightShoulderTz = DoubleLinearField(default_value=0.0)


class RightShoulderTField(
    CompoundField[RightShoulderTAttrOperator, RightShoulderTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderTAttrOperator
    PLUG_CLS = RightShoulderTPlugOperator

    RightShoulderTx = DoubleLinearField(default_value=0.0)

    RightShoulderTy = DoubleLinearField(default_value=0.0)

    RightShoulderTz = DoubleLinearField(default_value=0.0)


class RightShoulderRPlugOperator(
    CompoundPlugOperator["RightShoulderRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderRx", "RightShoulderRx"),
        ("RightShoulderRy", "RightShoulderRy"),
        ("RightShoulderRz", "RightShoulderRz"),
    )

    RightShoulderRx = DoubleAngleField(default_value=0.0)

    RightShoulderRy = DoubleAngleField(default_value=0.0)

    RightShoulderRz = DoubleAngleField(default_value=0.0)


class RightShoulderRAttrOperator(
    CompoundAttrOperator[RightShoulderRPlugOperator]
):
    __slots__ = ()

    RightShoulderRx = DoubleAngleField(default_value=0.0)

    RightShoulderRy = DoubleAngleField(default_value=0.0)

    RightShoulderRz = DoubleAngleField(default_value=0.0)


class RightShoulderRField(
    CompoundField[RightShoulderRAttrOperator, RightShoulderRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderRAttrOperator
    PLUG_CLS = RightShoulderRPlugOperator

    RightShoulderRx = DoubleAngleField(default_value=0.0)

    RightShoulderRy = DoubleAngleField(default_value=0.0)

    RightShoulderRz = DoubleAngleField(default_value=0.0)


class RightShoulderSPlugOperator(
    CompoundPlugOperator["RightShoulderSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderSx", "RightShoulderSx"),
        ("RightShoulderSy", "RightShoulderSy"),
        ("RightShoulderSz", "RightShoulderSz"),
    )

    RightShoulderSx = DoubleField(default_value=1.0)

    RightShoulderSy = DoubleField(default_value=1.0)

    RightShoulderSz = DoubleField(default_value=1.0)


class RightShoulderSAttrOperator(
    CompoundAttrOperator[RightShoulderSPlugOperator]
):
    __slots__ = ()

    RightShoulderSx = DoubleField(default_value=1.0)

    RightShoulderSy = DoubleField(default_value=1.0)

    RightShoulderSz = DoubleField(default_value=1.0)


class RightShoulderSField(
    CompoundField[RightShoulderSAttrOperator, RightShoulderSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderSAttrOperator
    PLUG_CLS = RightShoulderSPlugOperator

    RightShoulderSx = DoubleField(default_value=1.0)

    RightShoulderSy = DoubleField(default_value=1.0)

    RightShoulderSz = DoubleField(default_value=1.0)


class NeckTPlugOperator(
    CompoundPlugOperator["NeckTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NeckTx", "NeckTx"),
        ("NeckTy", "NeckTy"),
        ("NeckTz", "NeckTz"),
    )

    NeckTx = DoubleLinearField(default_value=0.0)

    NeckTy = DoubleLinearField(default_value=0.0)

    NeckTz = DoubleLinearField(default_value=0.0)


class NeckTAttrOperator(
    CompoundAttrOperator[NeckTPlugOperator]
):
    __slots__ = ()

    NeckTx = DoubleLinearField(default_value=0.0)

    NeckTy = DoubleLinearField(default_value=0.0)

    NeckTz = DoubleLinearField(default_value=0.0)


class NeckTField(
    CompoundField[NeckTAttrOperator, NeckTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NeckTAttrOperator
    PLUG_CLS = NeckTPlugOperator

    NeckTx = DoubleLinearField(default_value=0.0)

    NeckTy = DoubleLinearField(default_value=0.0)

    NeckTz = DoubleLinearField(default_value=0.0)


class NeckRPlugOperator(
    CompoundPlugOperator["NeckRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NeckRx", "NeckRx"),
        ("NeckRy", "NeckRy"),
        ("NeckRz", "NeckRz"),
    )

    NeckRx = DoubleAngleField(default_value=0.0)

    NeckRy = DoubleAngleField(default_value=0.0)

    NeckRz = DoubleAngleField(default_value=0.0)


class NeckRAttrOperator(
    CompoundAttrOperator[NeckRPlugOperator]
):
    __slots__ = ()

    NeckRx = DoubleAngleField(default_value=0.0)

    NeckRy = DoubleAngleField(default_value=0.0)

    NeckRz = DoubleAngleField(default_value=0.0)


class NeckRField(
    CompoundField[NeckRAttrOperator, NeckRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NeckRAttrOperator
    PLUG_CLS = NeckRPlugOperator

    NeckRx = DoubleAngleField(default_value=0.0)

    NeckRy = DoubleAngleField(default_value=0.0)

    NeckRz = DoubleAngleField(default_value=0.0)


class NeckSPlugOperator(
    CompoundPlugOperator["NeckSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NeckSx", "NeckSx"),
        ("NeckSy", "NeckSy"),
        ("NeckSz", "NeckSz"),
    )

    NeckSx = DoubleField(default_value=1.0)

    NeckSy = DoubleField(default_value=1.0)

    NeckSz = DoubleField(default_value=1.0)


class NeckSAttrOperator(
    CompoundAttrOperator[NeckSPlugOperator]
):
    __slots__ = ()

    NeckSx = DoubleField(default_value=1.0)

    NeckSy = DoubleField(default_value=1.0)

    NeckSz = DoubleField(default_value=1.0)


class NeckSField(
    CompoundField[NeckSAttrOperator, NeckSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NeckSAttrOperator
    PLUG_CLS = NeckSPlugOperator

    NeckSx = DoubleField(default_value=1.0)

    NeckSy = DoubleField(default_value=1.0)

    NeckSz = DoubleField(default_value=1.0)


class LeftFingerBaseTPlugOperator(
    CompoundPlugOperator["LeftFingerBaseTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFingerBaseTx", "LeftFingerBaseTx"),
        ("LeftFingerBaseTy", "LeftFingerBaseTy"),
        ("LeftFingerBaseTz", "LeftFingerBaseTz"),
    )

    LeftFingerBaseTx = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTy = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTz = DoubleLinearField(default_value=0.0)


class LeftFingerBaseTAttrOperator(
    CompoundAttrOperator[LeftFingerBaseTPlugOperator]
):
    __slots__ = ()

    LeftFingerBaseTx = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTy = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTz = DoubleLinearField(default_value=0.0)


class LeftFingerBaseTField(
    CompoundField[LeftFingerBaseTAttrOperator, LeftFingerBaseTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFingerBaseTAttrOperator
    PLUG_CLS = LeftFingerBaseTPlugOperator

    LeftFingerBaseTx = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTy = DoubleLinearField(default_value=0.0)

    LeftFingerBaseTz = DoubleLinearField(default_value=0.0)


class LeftFingerBaseRPlugOperator(
    CompoundPlugOperator["LeftFingerBaseRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFingerBaseRx", "LeftFingerBaseRx"),
        ("LeftFingerBaseRy", "LeftFingerBaseRy"),
        ("LeftFingerBaseRz", "LeftFingerBaseRz"),
    )

    LeftFingerBaseRx = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRy = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRz = DoubleAngleField(default_value=0.0)


class LeftFingerBaseRAttrOperator(
    CompoundAttrOperator[LeftFingerBaseRPlugOperator]
):
    __slots__ = ()

    LeftFingerBaseRx = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRy = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRz = DoubleAngleField(default_value=0.0)


class LeftFingerBaseRField(
    CompoundField[LeftFingerBaseRAttrOperator, LeftFingerBaseRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFingerBaseRAttrOperator
    PLUG_CLS = LeftFingerBaseRPlugOperator

    LeftFingerBaseRx = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRy = DoubleAngleField(default_value=0.0)

    LeftFingerBaseRz = DoubleAngleField(default_value=0.0)


class LeftFingerBaseSPlugOperator(
    CompoundPlugOperator["LeftFingerBaseSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFingerBaseSx", "LeftFingerBaseSx"),
        ("LeftFingerBaseSy", "LeftFingerBaseSy"),
        ("LeftFingerBaseSz", "LeftFingerBaseSz"),
    )

    LeftFingerBaseSx = DoubleField(default_value=1.0)

    LeftFingerBaseSy = DoubleField(default_value=1.0)

    LeftFingerBaseSz = DoubleField(default_value=1.0)


class LeftFingerBaseSAttrOperator(
    CompoundAttrOperator[LeftFingerBaseSPlugOperator]
):
    __slots__ = ()

    LeftFingerBaseSx = DoubleField(default_value=1.0)

    LeftFingerBaseSy = DoubleField(default_value=1.0)

    LeftFingerBaseSz = DoubleField(default_value=1.0)


class LeftFingerBaseSField(
    CompoundField[LeftFingerBaseSAttrOperator, LeftFingerBaseSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFingerBaseSAttrOperator
    PLUG_CLS = LeftFingerBaseSPlugOperator

    LeftFingerBaseSx = DoubleField(default_value=1.0)

    LeftFingerBaseSy = DoubleField(default_value=1.0)

    LeftFingerBaseSz = DoubleField(default_value=1.0)


class RightFingerBaseTPlugOperator(
    CompoundPlugOperator["RightFingerBaseTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFingerBaseTx", "RightFingerBaseTx"),
        ("RightFingerBaseTy", "RightFingerBaseTy"),
        ("RightFingerBaseTz", "RightFingerBaseTz"),
    )

    RightFingerBaseTx = DoubleLinearField(default_value=0.0)

    RightFingerBaseTy = DoubleLinearField(default_value=0.0)

    RightFingerBaseTz = DoubleLinearField(default_value=0.0)


class RightFingerBaseTAttrOperator(
    CompoundAttrOperator[RightFingerBaseTPlugOperator]
):
    __slots__ = ()

    RightFingerBaseTx = DoubleLinearField(default_value=0.0)

    RightFingerBaseTy = DoubleLinearField(default_value=0.0)

    RightFingerBaseTz = DoubleLinearField(default_value=0.0)


class RightFingerBaseTField(
    CompoundField[RightFingerBaseTAttrOperator, RightFingerBaseTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFingerBaseTAttrOperator
    PLUG_CLS = RightFingerBaseTPlugOperator

    RightFingerBaseTx = DoubleLinearField(default_value=0.0)

    RightFingerBaseTy = DoubleLinearField(default_value=0.0)

    RightFingerBaseTz = DoubleLinearField(default_value=0.0)


class RightFingerBaseRPlugOperator(
    CompoundPlugOperator["RightFingerBaseRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFingerBaseRx", "RightFingerBaseRx"),
        ("RightFingerBaseRy", "RightFingerBaseRy"),
        ("RightFingerBaseRz", "RightFingerBaseRz"),
    )

    RightFingerBaseRx = DoubleAngleField(default_value=0.0)

    RightFingerBaseRy = DoubleAngleField(default_value=0.0)

    RightFingerBaseRz = DoubleAngleField(default_value=0.0)


class RightFingerBaseRAttrOperator(
    CompoundAttrOperator[RightFingerBaseRPlugOperator]
):
    __slots__ = ()

    RightFingerBaseRx = DoubleAngleField(default_value=0.0)

    RightFingerBaseRy = DoubleAngleField(default_value=0.0)

    RightFingerBaseRz = DoubleAngleField(default_value=0.0)


class RightFingerBaseRField(
    CompoundField[RightFingerBaseRAttrOperator, RightFingerBaseRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFingerBaseRAttrOperator
    PLUG_CLS = RightFingerBaseRPlugOperator

    RightFingerBaseRx = DoubleAngleField(default_value=0.0)

    RightFingerBaseRy = DoubleAngleField(default_value=0.0)

    RightFingerBaseRz = DoubleAngleField(default_value=0.0)


class RightFingerBaseSPlugOperator(
    CompoundPlugOperator["RightFingerBaseSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFingerBaseSx", "RightFingerBaseSx"),
        ("RightFingerBaseSy", "RightFingerBaseSy"),
        ("RightFingerBaseSz", "RightFingerBaseSz"),
    )

    RightFingerBaseSx = DoubleField(default_value=1.0)

    RightFingerBaseSy = DoubleField(default_value=1.0)

    RightFingerBaseSz = DoubleField(default_value=1.0)


class RightFingerBaseSAttrOperator(
    CompoundAttrOperator[RightFingerBaseSPlugOperator]
):
    __slots__ = ()

    RightFingerBaseSx = DoubleField(default_value=1.0)

    RightFingerBaseSy = DoubleField(default_value=1.0)

    RightFingerBaseSz = DoubleField(default_value=1.0)


class RightFingerBaseSField(
    CompoundField[RightFingerBaseSAttrOperator, RightFingerBaseSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFingerBaseSAttrOperator
    PLUG_CLS = RightFingerBaseSPlugOperator

    RightFingerBaseSx = DoubleField(default_value=1.0)

    RightFingerBaseSy = DoubleField(default_value=1.0)

    RightFingerBaseSz = DoubleField(default_value=1.0)


class Spine1TPlugOperator(
    CompoundPlugOperator["Spine1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine1Tx", "Spine1Tx"),
        ("Spine1Ty", "Spine1Ty"),
        ("Spine1Tz", "Spine1Tz"),
    )

    Spine1Tx = DoubleLinearField(default_value=0.0)

    Spine1Ty = DoubleLinearField(default_value=0.0)

    Spine1Tz = DoubleLinearField(default_value=0.0)


class Spine1TAttrOperator(
    CompoundAttrOperator[Spine1TPlugOperator]
):
    __slots__ = ()

    Spine1Tx = DoubleLinearField(default_value=0.0)

    Spine1Ty = DoubleLinearField(default_value=0.0)

    Spine1Tz = DoubleLinearField(default_value=0.0)


class Spine1TField(
    CompoundField[Spine1TAttrOperator, Spine1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine1TAttrOperator
    PLUG_CLS = Spine1TPlugOperator

    Spine1Tx = DoubleLinearField(default_value=0.0)

    Spine1Ty = DoubleLinearField(default_value=0.0)

    Spine1Tz = DoubleLinearField(default_value=0.0)


class Spine1RPlugOperator(
    CompoundPlugOperator["Spine1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine1Rx", "Spine1Rx"),
        ("Spine1Ry", "Spine1Ry"),
        ("Spine1Rz", "Spine1Rz"),
    )

    Spine1Rx = DoubleAngleField(default_value=0.0)

    Spine1Ry = DoubleAngleField(default_value=0.0)

    Spine1Rz = DoubleAngleField(default_value=0.0)


class Spine1RAttrOperator(
    CompoundAttrOperator[Spine1RPlugOperator]
):
    __slots__ = ()

    Spine1Rx = DoubleAngleField(default_value=0.0)

    Spine1Ry = DoubleAngleField(default_value=0.0)

    Spine1Rz = DoubleAngleField(default_value=0.0)


class Spine1RField(
    CompoundField[Spine1RAttrOperator, Spine1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine1RAttrOperator
    PLUG_CLS = Spine1RPlugOperator

    Spine1Rx = DoubleAngleField(default_value=0.0)

    Spine1Ry = DoubleAngleField(default_value=0.0)

    Spine1Rz = DoubleAngleField(default_value=0.0)


class Spine1SPlugOperator(
    CompoundPlugOperator["Spine1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine1Sx", "Spine1Sx"),
        ("Spine1Sy", "Spine1Sy"),
        ("Spine1Sz", "Spine1Sz"),
    )

    Spine1Sx = DoubleField(default_value=1.0)

    Spine1Sy = DoubleField(default_value=1.0)

    Spine1Sz = DoubleField(default_value=1.0)


class Spine1SAttrOperator(
    CompoundAttrOperator[Spine1SPlugOperator]
):
    __slots__ = ()

    Spine1Sx = DoubleField(default_value=1.0)

    Spine1Sy = DoubleField(default_value=1.0)

    Spine1Sz = DoubleField(default_value=1.0)


class Spine1SField(
    CompoundField[Spine1SAttrOperator, Spine1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine1SAttrOperator
    PLUG_CLS = Spine1SPlugOperator

    Spine1Sx = DoubleField(default_value=1.0)

    Spine1Sy = DoubleField(default_value=1.0)

    Spine1Sz = DoubleField(default_value=1.0)


class Spine2TPlugOperator(
    CompoundPlugOperator["Spine2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine2Tx", "Spine2Tx"),
        ("Spine2Ty", "Spine2Ty"),
        ("Spine2Tz", "Spine2Tz"),
    )

    Spine2Tx = DoubleLinearField(default_value=0.0)

    Spine2Ty = DoubleLinearField(default_value=0.0)

    Spine2Tz = DoubleLinearField(default_value=0.0)


class Spine2TAttrOperator(
    CompoundAttrOperator[Spine2TPlugOperator]
):
    __slots__ = ()

    Spine2Tx = DoubleLinearField(default_value=0.0)

    Spine2Ty = DoubleLinearField(default_value=0.0)

    Spine2Tz = DoubleLinearField(default_value=0.0)


class Spine2TField(
    CompoundField[Spine2TAttrOperator, Spine2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine2TAttrOperator
    PLUG_CLS = Spine2TPlugOperator

    Spine2Tx = DoubleLinearField(default_value=0.0)

    Spine2Ty = DoubleLinearField(default_value=0.0)

    Spine2Tz = DoubleLinearField(default_value=0.0)


class Spine2RPlugOperator(
    CompoundPlugOperator["Spine2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine2Rx", "Spine2Rx"),
        ("Spine2Ry", "Spine2Ry"),
        ("Spine2Rz", "Spine2Rz"),
    )

    Spine2Rx = DoubleAngleField(default_value=0.0)

    Spine2Ry = DoubleAngleField(default_value=0.0)

    Spine2Rz = DoubleAngleField(default_value=0.0)


class Spine2RAttrOperator(
    CompoundAttrOperator[Spine2RPlugOperator]
):
    __slots__ = ()

    Spine2Rx = DoubleAngleField(default_value=0.0)

    Spine2Ry = DoubleAngleField(default_value=0.0)

    Spine2Rz = DoubleAngleField(default_value=0.0)


class Spine2RField(
    CompoundField[Spine2RAttrOperator, Spine2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine2RAttrOperator
    PLUG_CLS = Spine2RPlugOperator

    Spine2Rx = DoubleAngleField(default_value=0.0)

    Spine2Ry = DoubleAngleField(default_value=0.0)

    Spine2Rz = DoubleAngleField(default_value=0.0)


class Spine2SPlugOperator(
    CompoundPlugOperator["Spine2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine2Sx", "Spine2Sx"),
        ("Spine2Sy", "Spine2Sy"),
        ("Spine2Sz", "Spine2Sz"),
    )

    Spine2Sx = DoubleField(default_value=1.0)

    Spine2Sy = DoubleField(default_value=1.0)

    Spine2Sz = DoubleField(default_value=1.0)


class Spine2SAttrOperator(
    CompoundAttrOperator[Spine2SPlugOperator]
):
    __slots__ = ()

    Spine2Sx = DoubleField(default_value=1.0)

    Spine2Sy = DoubleField(default_value=1.0)

    Spine2Sz = DoubleField(default_value=1.0)


class Spine2SField(
    CompoundField[Spine2SAttrOperator, Spine2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine2SAttrOperator
    PLUG_CLS = Spine2SPlugOperator

    Spine2Sx = DoubleField(default_value=1.0)

    Spine2Sy = DoubleField(default_value=1.0)

    Spine2Sz = DoubleField(default_value=1.0)


class Spine3TPlugOperator(
    CompoundPlugOperator["Spine3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine3Tx", "Spine3Tx"),
        ("Spine3Ty", "Spine3Ty"),
        ("Spine3Tz", "Spine3Tz"),
    )

    Spine3Tx = DoubleLinearField(default_value=0.0)

    Spine3Ty = DoubleLinearField(default_value=0.0)

    Spine3Tz = DoubleLinearField(default_value=0.0)


class Spine3TAttrOperator(
    CompoundAttrOperator[Spine3TPlugOperator]
):
    __slots__ = ()

    Spine3Tx = DoubleLinearField(default_value=0.0)

    Spine3Ty = DoubleLinearField(default_value=0.0)

    Spine3Tz = DoubleLinearField(default_value=0.0)


class Spine3TField(
    CompoundField[Spine3TAttrOperator, Spine3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine3TAttrOperator
    PLUG_CLS = Spine3TPlugOperator

    Spine3Tx = DoubleLinearField(default_value=0.0)

    Spine3Ty = DoubleLinearField(default_value=0.0)

    Spine3Tz = DoubleLinearField(default_value=0.0)


class Spine3RPlugOperator(
    CompoundPlugOperator["Spine3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine3Rx", "Spine3Rx"),
        ("Spine3Ry", "Spine3Ry"),
        ("Spine3Rz", "Spine3Rz"),
    )

    Spine3Rx = DoubleAngleField(default_value=0.0)

    Spine3Ry = DoubleAngleField(default_value=0.0)

    Spine3Rz = DoubleAngleField(default_value=0.0)


class Spine3RAttrOperator(
    CompoundAttrOperator[Spine3RPlugOperator]
):
    __slots__ = ()

    Spine3Rx = DoubleAngleField(default_value=0.0)

    Spine3Ry = DoubleAngleField(default_value=0.0)

    Spine3Rz = DoubleAngleField(default_value=0.0)


class Spine3RField(
    CompoundField[Spine3RAttrOperator, Spine3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine3RAttrOperator
    PLUG_CLS = Spine3RPlugOperator

    Spine3Rx = DoubleAngleField(default_value=0.0)

    Spine3Ry = DoubleAngleField(default_value=0.0)

    Spine3Rz = DoubleAngleField(default_value=0.0)


class Spine3SPlugOperator(
    CompoundPlugOperator["Spine3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine3Sx", "Spine3Sx"),
        ("Spine3Sy", "Spine3Sy"),
        ("Spine3Sz", "Spine3Sz"),
    )

    Spine3Sx = DoubleField(default_value=1.0)

    Spine3Sy = DoubleField(default_value=1.0)

    Spine3Sz = DoubleField(default_value=1.0)


class Spine3SAttrOperator(
    CompoundAttrOperator[Spine3SPlugOperator]
):
    __slots__ = ()

    Spine3Sx = DoubleField(default_value=1.0)

    Spine3Sy = DoubleField(default_value=1.0)

    Spine3Sz = DoubleField(default_value=1.0)


class Spine3SField(
    CompoundField[Spine3SAttrOperator, Spine3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine3SAttrOperator
    PLUG_CLS = Spine3SPlugOperator

    Spine3Sx = DoubleField(default_value=1.0)

    Spine3Sy = DoubleField(default_value=1.0)

    Spine3Sz = DoubleField(default_value=1.0)


class Spine4TPlugOperator(
    CompoundPlugOperator["Spine4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine4Tx", "Spine4Tx"),
        ("Spine4Ty", "Spine4Ty"),
        ("Spine4Tz", "Spine4Tz"),
    )

    Spine4Tx = DoubleLinearField(default_value=0.0)

    Spine4Ty = DoubleLinearField(default_value=0.0)

    Spine4Tz = DoubleLinearField(default_value=0.0)


class Spine4TAttrOperator(
    CompoundAttrOperator[Spine4TPlugOperator]
):
    __slots__ = ()

    Spine4Tx = DoubleLinearField(default_value=0.0)

    Spine4Ty = DoubleLinearField(default_value=0.0)

    Spine4Tz = DoubleLinearField(default_value=0.0)


class Spine4TField(
    CompoundField[Spine4TAttrOperator, Spine4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine4TAttrOperator
    PLUG_CLS = Spine4TPlugOperator

    Spine4Tx = DoubleLinearField(default_value=0.0)

    Spine4Ty = DoubleLinearField(default_value=0.0)

    Spine4Tz = DoubleLinearField(default_value=0.0)


class Spine4RPlugOperator(
    CompoundPlugOperator["Spine4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine4Rx", "Spine4Rx"),
        ("Spine4Ry", "Spine4Ry"),
        ("Spine4Rz", "Spine4Rz"),
    )

    Spine4Rx = DoubleAngleField(default_value=0.0)

    Spine4Ry = DoubleAngleField(default_value=0.0)

    Spine4Rz = DoubleAngleField(default_value=0.0)


class Spine4RAttrOperator(
    CompoundAttrOperator[Spine4RPlugOperator]
):
    __slots__ = ()

    Spine4Rx = DoubleAngleField(default_value=0.0)

    Spine4Ry = DoubleAngleField(default_value=0.0)

    Spine4Rz = DoubleAngleField(default_value=0.0)


class Spine4RField(
    CompoundField[Spine4RAttrOperator, Spine4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine4RAttrOperator
    PLUG_CLS = Spine4RPlugOperator

    Spine4Rx = DoubleAngleField(default_value=0.0)

    Spine4Ry = DoubleAngleField(default_value=0.0)

    Spine4Rz = DoubleAngleField(default_value=0.0)


class Spine4SPlugOperator(
    CompoundPlugOperator["Spine4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine4Sx", "Spine4Sx"),
        ("Spine4Sy", "Spine4Sy"),
        ("Spine4Sz", "Spine4Sz"),
    )

    Spine4Sx = DoubleField(default_value=1.0)

    Spine4Sy = DoubleField(default_value=1.0)

    Spine4Sz = DoubleField(default_value=1.0)


class Spine4SAttrOperator(
    CompoundAttrOperator[Spine4SPlugOperator]
):
    __slots__ = ()

    Spine4Sx = DoubleField(default_value=1.0)

    Spine4Sy = DoubleField(default_value=1.0)

    Spine4Sz = DoubleField(default_value=1.0)


class Spine4SField(
    CompoundField[Spine4SAttrOperator, Spine4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine4SAttrOperator
    PLUG_CLS = Spine4SPlugOperator

    Spine4Sx = DoubleField(default_value=1.0)

    Spine4Sy = DoubleField(default_value=1.0)

    Spine4Sz = DoubleField(default_value=1.0)


class Spine5TPlugOperator(
    CompoundPlugOperator["Spine5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine5Tx", "Spine5Tx"),
        ("Spine5Ty", "Spine5Ty"),
        ("Spine5Tz", "Spine5Tz"),
    )

    Spine5Tx = DoubleLinearField(default_value=0.0)

    Spine5Ty = DoubleLinearField(default_value=0.0)

    Spine5Tz = DoubleLinearField(default_value=0.0)


class Spine5TAttrOperator(
    CompoundAttrOperator[Spine5TPlugOperator]
):
    __slots__ = ()

    Spine5Tx = DoubleLinearField(default_value=0.0)

    Spine5Ty = DoubleLinearField(default_value=0.0)

    Spine5Tz = DoubleLinearField(default_value=0.0)


class Spine5TField(
    CompoundField[Spine5TAttrOperator, Spine5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine5TAttrOperator
    PLUG_CLS = Spine5TPlugOperator

    Spine5Tx = DoubleLinearField(default_value=0.0)

    Spine5Ty = DoubleLinearField(default_value=0.0)

    Spine5Tz = DoubleLinearField(default_value=0.0)


class Spine5RPlugOperator(
    CompoundPlugOperator["Spine5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine5Rx", "Spine5Rx"),
        ("Spine5Ry", "Spine5Ry"),
        ("Spine5Rz", "Spine5Rz"),
    )

    Spine5Rx = DoubleAngleField(default_value=0.0)

    Spine5Ry = DoubleAngleField(default_value=0.0)

    Spine5Rz = DoubleAngleField(default_value=0.0)


class Spine5RAttrOperator(
    CompoundAttrOperator[Spine5RPlugOperator]
):
    __slots__ = ()

    Spine5Rx = DoubleAngleField(default_value=0.0)

    Spine5Ry = DoubleAngleField(default_value=0.0)

    Spine5Rz = DoubleAngleField(default_value=0.0)


class Spine5RField(
    CompoundField[Spine5RAttrOperator, Spine5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine5RAttrOperator
    PLUG_CLS = Spine5RPlugOperator

    Spine5Rx = DoubleAngleField(default_value=0.0)

    Spine5Ry = DoubleAngleField(default_value=0.0)

    Spine5Rz = DoubleAngleField(default_value=0.0)


class Spine5SPlugOperator(
    CompoundPlugOperator["Spine5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine5Sx", "Spine5Sx"),
        ("Spine5Sy", "Spine5Sy"),
        ("Spine5Sz", "Spine5Sz"),
    )

    Spine5Sx = DoubleField(default_value=1.0)

    Spine5Sy = DoubleField(default_value=1.0)

    Spine5Sz = DoubleField(default_value=1.0)


class Spine5SAttrOperator(
    CompoundAttrOperator[Spine5SPlugOperator]
):
    __slots__ = ()

    Spine5Sx = DoubleField(default_value=1.0)

    Spine5Sy = DoubleField(default_value=1.0)

    Spine5Sz = DoubleField(default_value=1.0)


class Spine5SField(
    CompoundField[Spine5SAttrOperator, Spine5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine5SAttrOperator
    PLUG_CLS = Spine5SPlugOperator

    Spine5Sx = DoubleField(default_value=1.0)

    Spine5Sy = DoubleField(default_value=1.0)

    Spine5Sz = DoubleField(default_value=1.0)


class Spine6TPlugOperator(
    CompoundPlugOperator["Spine6TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine6Tx", "Spine6Tx"),
        ("Spine6Ty", "Spine6Ty"),
        ("Spine6Tz", "Spine6Tz"),
    )

    Spine6Tx = DoubleLinearField(default_value=0.0)

    Spine6Ty = DoubleLinearField(default_value=0.0)

    Spine6Tz = DoubleLinearField(default_value=0.0)


class Spine6TAttrOperator(
    CompoundAttrOperator[Spine6TPlugOperator]
):
    __slots__ = ()

    Spine6Tx = DoubleLinearField(default_value=0.0)

    Spine6Ty = DoubleLinearField(default_value=0.0)

    Spine6Tz = DoubleLinearField(default_value=0.0)


class Spine6TField(
    CompoundField[Spine6TAttrOperator, Spine6TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine6TAttrOperator
    PLUG_CLS = Spine6TPlugOperator

    Spine6Tx = DoubleLinearField(default_value=0.0)

    Spine6Ty = DoubleLinearField(default_value=0.0)

    Spine6Tz = DoubleLinearField(default_value=0.0)


class Spine6RPlugOperator(
    CompoundPlugOperator["Spine6RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine6Rx", "Spine6Rx"),
        ("Spine6Ry", "Spine6Ry"),
        ("Spine6Rz", "Spine6Rz"),
    )

    Spine6Rx = DoubleAngleField(default_value=0.0)

    Spine6Ry = DoubleAngleField(default_value=0.0)

    Spine6Rz = DoubleAngleField(default_value=0.0)


class Spine6RAttrOperator(
    CompoundAttrOperator[Spine6RPlugOperator]
):
    __slots__ = ()

    Spine6Rx = DoubleAngleField(default_value=0.0)

    Spine6Ry = DoubleAngleField(default_value=0.0)

    Spine6Rz = DoubleAngleField(default_value=0.0)


class Spine6RField(
    CompoundField[Spine6RAttrOperator, Spine6RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine6RAttrOperator
    PLUG_CLS = Spine6RPlugOperator

    Spine6Rx = DoubleAngleField(default_value=0.0)

    Spine6Ry = DoubleAngleField(default_value=0.0)

    Spine6Rz = DoubleAngleField(default_value=0.0)


class Spine6SPlugOperator(
    CompoundPlugOperator["Spine6SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine6Sx", "Spine6Sx"),
        ("Spine6Sy", "Spine6Sy"),
        ("Spine6Sz", "Spine6Sz"),
    )

    Spine6Sx = DoubleField(default_value=1.0)

    Spine6Sy = DoubleField(default_value=1.0)

    Spine6Sz = DoubleField(default_value=1.0)


class Spine6SAttrOperator(
    CompoundAttrOperator[Spine6SPlugOperator]
):
    __slots__ = ()

    Spine6Sx = DoubleField(default_value=1.0)

    Spine6Sy = DoubleField(default_value=1.0)

    Spine6Sz = DoubleField(default_value=1.0)


class Spine6SField(
    CompoundField[Spine6SAttrOperator, Spine6SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine6SAttrOperator
    PLUG_CLS = Spine6SPlugOperator

    Spine6Sx = DoubleField(default_value=1.0)

    Spine6Sy = DoubleField(default_value=1.0)

    Spine6Sz = DoubleField(default_value=1.0)


class Spine7TPlugOperator(
    CompoundPlugOperator["Spine7TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine7Tx", "Spine7Tx"),
        ("Spine7Ty", "Spine7Ty"),
        ("Spine7Tz", "Spine7Tz"),
    )

    Spine7Tx = DoubleLinearField(default_value=0.0)

    Spine7Ty = DoubleLinearField(default_value=0.0)

    Spine7Tz = DoubleLinearField(default_value=0.0)


class Spine7TAttrOperator(
    CompoundAttrOperator[Spine7TPlugOperator]
):
    __slots__ = ()

    Spine7Tx = DoubleLinearField(default_value=0.0)

    Spine7Ty = DoubleLinearField(default_value=0.0)

    Spine7Tz = DoubleLinearField(default_value=0.0)


class Spine7TField(
    CompoundField[Spine7TAttrOperator, Spine7TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine7TAttrOperator
    PLUG_CLS = Spine7TPlugOperator

    Spine7Tx = DoubleLinearField(default_value=0.0)

    Spine7Ty = DoubleLinearField(default_value=0.0)

    Spine7Tz = DoubleLinearField(default_value=0.0)


class Spine7RPlugOperator(
    CompoundPlugOperator["Spine7RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine7Rx", "Spine7Rx"),
        ("Spine7Ry", "Spine7Ry"),
        ("Spine7Rz", "Spine7Rz"),
    )

    Spine7Rx = DoubleAngleField(default_value=0.0)

    Spine7Ry = DoubleAngleField(default_value=0.0)

    Spine7Rz = DoubleAngleField(default_value=0.0)


class Spine7RAttrOperator(
    CompoundAttrOperator[Spine7RPlugOperator]
):
    __slots__ = ()

    Spine7Rx = DoubleAngleField(default_value=0.0)

    Spine7Ry = DoubleAngleField(default_value=0.0)

    Spine7Rz = DoubleAngleField(default_value=0.0)


class Spine7RField(
    CompoundField[Spine7RAttrOperator, Spine7RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine7RAttrOperator
    PLUG_CLS = Spine7RPlugOperator

    Spine7Rx = DoubleAngleField(default_value=0.0)

    Spine7Ry = DoubleAngleField(default_value=0.0)

    Spine7Rz = DoubleAngleField(default_value=0.0)


class Spine7SPlugOperator(
    CompoundPlugOperator["Spine7SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine7Sx", "Spine7Sx"),
        ("Spine7Sy", "Spine7Sy"),
        ("Spine7Sz", "Spine7Sz"),
    )

    Spine7Sx = DoubleField(default_value=1.0)

    Spine7Sy = DoubleField(default_value=1.0)

    Spine7Sz = DoubleField(default_value=1.0)


class Spine7SAttrOperator(
    CompoundAttrOperator[Spine7SPlugOperator]
):
    __slots__ = ()

    Spine7Sx = DoubleField(default_value=1.0)

    Spine7Sy = DoubleField(default_value=1.0)

    Spine7Sz = DoubleField(default_value=1.0)


class Spine7SField(
    CompoundField[Spine7SAttrOperator, Spine7SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine7SAttrOperator
    PLUG_CLS = Spine7SPlugOperator

    Spine7Sx = DoubleField(default_value=1.0)

    Spine7Sy = DoubleField(default_value=1.0)

    Spine7Sz = DoubleField(default_value=1.0)


class Spine8TPlugOperator(
    CompoundPlugOperator["Spine8TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine8Tx", "Spine8Tx"),
        ("Spine8Ty", "Spine8Ty"),
        ("Spine8Tz", "Spine8Tz"),
    )

    Spine8Tx = DoubleLinearField(default_value=0.0)

    Spine8Ty = DoubleLinearField(default_value=0.0)

    Spine8Tz = DoubleLinearField(default_value=0.0)


class Spine8TAttrOperator(
    CompoundAttrOperator[Spine8TPlugOperator]
):
    __slots__ = ()

    Spine8Tx = DoubleLinearField(default_value=0.0)

    Spine8Ty = DoubleLinearField(default_value=0.0)

    Spine8Tz = DoubleLinearField(default_value=0.0)


class Spine8TField(
    CompoundField[Spine8TAttrOperator, Spine8TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine8TAttrOperator
    PLUG_CLS = Spine8TPlugOperator

    Spine8Tx = DoubleLinearField(default_value=0.0)

    Spine8Ty = DoubleLinearField(default_value=0.0)

    Spine8Tz = DoubleLinearField(default_value=0.0)


class Spine8RPlugOperator(
    CompoundPlugOperator["Spine8RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine8Rx", "Spine8Rx"),
        ("Spine8Ry", "Spine8Ry"),
        ("Spine8Rz", "Spine8Rz"),
    )

    Spine8Rx = DoubleAngleField(default_value=0.0)

    Spine8Ry = DoubleAngleField(default_value=0.0)

    Spine8Rz = DoubleAngleField(default_value=0.0)


class Spine8RAttrOperator(
    CompoundAttrOperator[Spine8RPlugOperator]
):
    __slots__ = ()

    Spine8Rx = DoubleAngleField(default_value=0.0)

    Spine8Ry = DoubleAngleField(default_value=0.0)

    Spine8Rz = DoubleAngleField(default_value=0.0)


class Spine8RField(
    CompoundField[Spine8RAttrOperator, Spine8RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine8RAttrOperator
    PLUG_CLS = Spine8RPlugOperator

    Spine8Rx = DoubleAngleField(default_value=0.0)

    Spine8Ry = DoubleAngleField(default_value=0.0)

    Spine8Rz = DoubleAngleField(default_value=0.0)


class Spine8SPlugOperator(
    CompoundPlugOperator["Spine8SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine8Sx", "Spine8Sx"),
        ("Spine8Sy", "Spine8Sy"),
        ("Spine8Sz", "Spine8Sz"),
    )

    Spine8Sx = DoubleField(default_value=1.0)

    Spine8Sy = DoubleField(default_value=1.0)

    Spine8Sz = DoubleField(default_value=1.0)


class Spine8SAttrOperator(
    CompoundAttrOperator[Spine8SPlugOperator]
):
    __slots__ = ()

    Spine8Sx = DoubleField(default_value=1.0)

    Spine8Sy = DoubleField(default_value=1.0)

    Spine8Sz = DoubleField(default_value=1.0)


class Spine8SField(
    CompoundField[Spine8SAttrOperator, Spine8SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine8SAttrOperator
    PLUG_CLS = Spine8SPlugOperator

    Spine8Sx = DoubleField(default_value=1.0)

    Spine8Sy = DoubleField(default_value=1.0)

    Spine8Sz = DoubleField(default_value=1.0)


class Spine9TPlugOperator(
    CompoundPlugOperator["Spine9TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine9Tx", "Spine9Tx"),
        ("Spine9Ty", "Spine9Ty"),
        ("Spine9Tz", "Spine9Tz"),
    )

    Spine9Tx = DoubleLinearField(default_value=0.0)

    Spine9Ty = DoubleLinearField(default_value=0.0)

    Spine9Tz = DoubleLinearField(default_value=0.0)


class Spine9TAttrOperator(
    CompoundAttrOperator[Spine9TPlugOperator]
):
    __slots__ = ()

    Spine9Tx = DoubleLinearField(default_value=0.0)

    Spine9Ty = DoubleLinearField(default_value=0.0)

    Spine9Tz = DoubleLinearField(default_value=0.0)


class Spine9TField(
    CompoundField[Spine9TAttrOperator, Spine9TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine9TAttrOperator
    PLUG_CLS = Spine9TPlugOperator

    Spine9Tx = DoubleLinearField(default_value=0.0)

    Spine9Ty = DoubleLinearField(default_value=0.0)

    Spine9Tz = DoubleLinearField(default_value=0.0)


class Spine9RPlugOperator(
    CompoundPlugOperator["Spine9RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine9Rx", "Spine9Rx"),
        ("Spine9Ry", "Spine9Ry"),
        ("Spine9Rz", "Spine9Rz"),
    )

    Spine9Rx = DoubleAngleField(default_value=0.0)

    Spine9Ry = DoubleAngleField(default_value=0.0)

    Spine9Rz = DoubleAngleField(default_value=0.0)


class Spine9RAttrOperator(
    CompoundAttrOperator[Spine9RPlugOperator]
):
    __slots__ = ()

    Spine9Rx = DoubleAngleField(default_value=0.0)

    Spine9Ry = DoubleAngleField(default_value=0.0)

    Spine9Rz = DoubleAngleField(default_value=0.0)


class Spine9RField(
    CompoundField[Spine9RAttrOperator, Spine9RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine9RAttrOperator
    PLUG_CLS = Spine9RPlugOperator

    Spine9Rx = DoubleAngleField(default_value=0.0)

    Spine9Ry = DoubleAngleField(default_value=0.0)

    Spine9Rz = DoubleAngleField(default_value=0.0)


class Spine9SPlugOperator(
    CompoundPlugOperator["Spine9SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Spine9Sx", "Spine9Sx"),
        ("Spine9Sy", "Spine9Sy"),
        ("Spine9Sz", "Spine9Sz"),
    )

    Spine9Sx = DoubleField(default_value=1.0)

    Spine9Sy = DoubleField(default_value=1.0)

    Spine9Sz = DoubleField(default_value=1.0)


class Spine9SAttrOperator(
    CompoundAttrOperator[Spine9SPlugOperator]
):
    __slots__ = ()

    Spine9Sx = DoubleField(default_value=1.0)

    Spine9Sy = DoubleField(default_value=1.0)

    Spine9Sz = DoubleField(default_value=1.0)


class Spine9SField(
    CompoundField[Spine9SAttrOperator, Spine9SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Spine9SAttrOperator
    PLUG_CLS = Spine9SPlugOperator

    Spine9Sx = DoubleField(default_value=1.0)

    Spine9Sy = DoubleField(default_value=1.0)

    Spine9Sz = DoubleField(default_value=1.0)


class Neck1TPlugOperator(
    CompoundPlugOperator["Neck1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck1Tx", "Neck1Tx"),
        ("Neck1Ty", "Neck1Ty"),
        ("Neck1Tz", "Neck1Tz"),
    )

    Neck1Tx = DoubleLinearField(default_value=0.0)

    Neck1Ty = DoubleLinearField(default_value=0.0)

    Neck1Tz = DoubleLinearField(default_value=0.0)


class Neck1TAttrOperator(
    CompoundAttrOperator[Neck1TPlugOperator]
):
    __slots__ = ()

    Neck1Tx = DoubleLinearField(default_value=0.0)

    Neck1Ty = DoubleLinearField(default_value=0.0)

    Neck1Tz = DoubleLinearField(default_value=0.0)


class Neck1TField(
    CompoundField[Neck1TAttrOperator, Neck1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck1TAttrOperator
    PLUG_CLS = Neck1TPlugOperator

    Neck1Tx = DoubleLinearField(default_value=0.0)

    Neck1Ty = DoubleLinearField(default_value=0.0)

    Neck1Tz = DoubleLinearField(default_value=0.0)


class Neck1RPlugOperator(
    CompoundPlugOperator["Neck1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck1Rx", "Neck1Rx"),
        ("Neck1Ry", "Neck1Ry"),
        ("Neck1Rz", "Neck1Rz"),
    )

    Neck1Rx = DoubleAngleField(default_value=0.0)

    Neck1Ry = DoubleAngleField(default_value=0.0)

    Neck1Rz = DoubleAngleField(default_value=0.0)


class Neck1RAttrOperator(
    CompoundAttrOperator[Neck1RPlugOperator]
):
    __slots__ = ()

    Neck1Rx = DoubleAngleField(default_value=0.0)

    Neck1Ry = DoubleAngleField(default_value=0.0)

    Neck1Rz = DoubleAngleField(default_value=0.0)


class Neck1RField(
    CompoundField[Neck1RAttrOperator, Neck1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck1RAttrOperator
    PLUG_CLS = Neck1RPlugOperator

    Neck1Rx = DoubleAngleField(default_value=0.0)

    Neck1Ry = DoubleAngleField(default_value=0.0)

    Neck1Rz = DoubleAngleField(default_value=0.0)


class Neck1SPlugOperator(
    CompoundPlugOperator["Neck1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck1Sx", "Neck1Sx"),
        ("Neck1Sy", "Neck1Sy"),
        ("Neck1Sz", "Neck1Sz"),
    )

    Neck1Sx = DoubleField(default_value=1.0)

    Neck1Sy = DoubleField(default_value=1.0)

    Neck1Sz = DoubleField(default_value=1.0)


class Neck1SAttrOperator(
    CompoundAttrOperator[Neck1SPlugOperator]
):
    __slots__ = ()

    Neck1Sx = DoubleField(default_value=1.0)

    Neck1Sy = DoubleField(default_value=1.0)

    Neck1Sz = DoubleField(default_value=1.0)


class Neck1SField(
    CompoundField[Neck1SAttrOperator, Neck1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck1SAttrOperator
    PLUG_CLS = Neck1SPlugOperator

    Neck1Sx = DoubleField(default_value=1.0)

    Neck1Sy = DoubleField(default_value=1.0)

    Neck1Sz = DoubleField(default_value=1.0)


class Neck2TPlugOperator(
    CompoundPlugOperator["Neck2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck2Tx", "Neck2Tx"),
        ("Neck2Ty", "Neck2Ty"),
        ("Neck2Tz", "Neck2Tz"),
    )

    Neck2Tx = DoubleLinearField(default_value=0.0)

    Neck2Ty = DoubleLinearField(default_value=0.0)

    Neck2Tz = DoubleLinearField(default_value=0.0)


class Neck2TAttrOperator(
    CompoundAttrOperator[Neck2TPlugOperator]
):
    __slots__ = ()

    Neck2Tx = DoubleLinearField(default_value=0.0)

    Neck2Ty = DoubleLinearField(default_value=0.0)

    Neck2Tz = DoubleLinearField(default_value=0.0)


class Neck2TField(
    CompoundField[Neck2TAttrOperator, Neck2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck2TAttrOperator
    PLUG_CLS = Neck2TPlugOperator

    Neck2Tx = DoubleLinearField(default_value=0.0)

    Neck2Ty = DoubleLinearField(default_value=0.0)

    Neck2Tz = DoubleLinearField(default_value=0.0)


class Neck2RPlugOperator(
    CompoundPlugOperator["Neck2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck2Rx", "Neck2Rx"),
        ("Neck2Ry", "Neck2Ry"),
        ("Neck2Rz", "Neck2Rz"),
    )

    Neck2Rx = DoubleAngleField(default_value=0.0)

    Neck2Ry = DoubleAngleField(default_value=0.0)

    Neck2Rz = DoubleAngleField(default_value=0.0)


class Neck2RAttrOperator(
    CompoundAttrOperator[Neck2RPlugOperator]
):
    __slots__ = ()

    Neck2Rx = DoubleAngleField(default_value=0.0)

    Neck2Ry = DoubleAngleField(default_value=0.0)

    Neck2Rz = DoubleAngleField(default_value=0.0)


class Neck2RField(
    CompoundField[Neck2RAttrOperator, Neck2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck2RAttrOperator
    PLUG_CLS = Neck2RPlugOperator

    Neck2Rx = DoubleAngleField(default_value=0.0)

    Neck2Ry = DoubleAngleField(default_value=0.0)

    Neck2Rz = DoubleAngleField(default_value=0.0)


class Neck2SPlugOperator(
    CompoundPlugOperator["Neck2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck2Sx", "Neck2Sx"),
        ("Neck2Sy", "Neck2Sy"),
        ("Neck2Sz", "Neck2Sz"),
    )

    Neck2Sx = DoubleField(default_value=1.0)

    Neck2Sy = DoubleField(default_value=1.0)

    Neck2Sz = DoubleField(default_value=1.0)


class Neck2SAttrOperator(
    CompoundAttrOperator[Neck2SPlugOperator]
):
    __slots__ = ()

    Neck2Sx = DoubleField(default_value=1.0)

    Neck2Sy = DoubleField(default_value=1.0)

    Neck2Sz = DoubleField(default_value=1.0)


class Neck2SField(
    CompoundField[Neck2SAttrOperator, Neck2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck2SAttrOperator
    PLUG_CLS = Neck2SPlugOperator

    Neck2Sx = DoubleField(default_value=1.0)

    Neck2Sy = DoubleField(default_value=1.0)

    Neck2Sz = DoubleField(default_value=1.0)


class Neck3TPlugOperator(
    CompoundPlugOperator["Neck3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck3Tx", "Neck3Tx"),
        ("Neck3Ty", "Neck3Ty"),
        ("Neck3Tz", "Neck3Tz"),
    )

    Neck3Tx = DoubleLinearField(default_value=0.0)

    Neck3Ty = DoubleLinearField(default_value=0.0)

    Neck3Tz = DoubleLinearField(default_value=0.0)


class Neck3TAttrOperator(
    CompoundAttrOperator[Neck3TPlugOperator]
):
    __slots__ = ()

    Neck3Tx = DoubleLinearField(default_value=0.0)

    Neck3Ty = DoubleLinearField(default_value=0.0)

    Neck3Tz = DoubleLinearField(default_value=0.0)


class Neck3TField(
    CompoundField[Neck3TAttrOperator, Neck3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck3TAttrOperator
    PLUG_CLS = Neck3TPlugOperator

    Neck3Tx = DoubleLinearField(default_value=0.0)

    Neck3Ty = DoubleLinearField(default_value=0.0)

    Neck3Tz = DoubleLinearField(default_value=0.0)


class Neck3RPlugOperator(
    CompoundPlugOperator["Neck3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck3Rx", "Neck3Rx"),
        ("Neck3Ry", "Neck3Ry"),
        ("Neck3Rz", "Neck3Rz"),
    )

    Neck3Rx = DoubleAngleField(default_value=0.0)

    Neck3Ry = DoubleAngleField(default_value=0.0)

    Neck3Rz = DoubleAngleField(default_value=0.0)


class Neck3RAttrOperator(
    CompoundAttrOperator[Neck3RPlugOperator]
):
    __slots__ = ()

    Neck3Rx = DoubleAngleField(default_value=0.0)

    Neck3Ry = DoubleAngleField(default_value=0.0)

    Neck3Rz = DoubleAngleField(default_value=0.0)


class Neck3RField(
    CompoundField[Neck3RAttrOperator, Neck3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck3RAttrOperator
    PLUG_CLS = Neck3RPlugOperator

    Neck3Rx = DoubleAngleField(default_value=0.0)

    Neck3Ry = DoubleAngleField(default_value=0.0)

    Neck3Rz = DoubleAngleField(default_value=0.0)


class Neck3SPlugOperator(
    CompoundPlugOperator["Neck3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck3Sx", "Neck3Sx"),
        ("Neck3Sy", "Neck3Sy"),
        ("Neck3Sz", "Neck3Sz"),
    )

    Neck3Sx = DoubleField(default_value=1.0)

    Neck3Sy = DoubleField(default_value=1.0)

    Neck3Sz = DoubleField(default_value=1.0)


class Neck3SAttrOperator(
    CompoundAttrOperator[Neck3SPlugOperator]
):
    __slots__ = ()

    Neck3Sx = DoubleField(default_value=1.0)

    Neck3Sy = DoubleField(default_value=1.0)

    Neck3Sz = DoubleField(default_value=1.0)


class Neck3SField(
    CompoundField[Neck3SAttrOperator, Neck3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck3SAttrOperator
    PLUG_CLS = Neck3SPlugOperator

    Neck3Sx = DoubleField(default_value=1.0)

    Neck3Sy = DoubleField(default_value=1.0)

    Neck3Sz = DoubleField(default_value=1.0)


class Neck4TPlugOperator(
    CompoundPlugOperator["Neck4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck4Tx", "Neck4Tx"),
        ("Neck4Ty", "Neck4Ty"),
        ("Neck4Tz", "Neck4Tz"),
    )

    Neck4Tx = DoubleLinearField(default_value=0.0)

    Neck4Ty = DoubleLinearField(default_value=0.0)

    Neck4Tz = DoubleLinearField(default_value=0.0)


class Neck4TAttrOperator(
    CompoundAttrOperator[Neck4TPlugOperator]
):
    __slots__ = ()

    Neck4Tx = DoubleLinearField(default_value=0.0)

    Neck4Ty = DoubleLinearField(default_value=0.0)

    Neck4Tz = DoubleLinearField(default_value=0.0)


class Neck4TField(
    CompoundField[Neck4TAttrOperator, Neck4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck4TAttrOperator
    PLUG_CLS = Neck4TPlugOperator

    Neck4Tx = DoubleLinearField(default_value=0.0)

    Neck4Ty = DoubleLinearField(default_value=0.0)

    Neck4Tz = DoubleLinearField(default_value=0.0)


class Neck4RPlugOperator(
    CompoundPlugOperator["Neck4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck4Rx", "Neck4Rx"),
        ("Neck4Ry", "Neck4Ry"),
        ("Neck4Rz", "Neck4Rz"),
    )

    Neck4Rx = DoubleAngleField(default_value=0.0)

    Neck4Ry = DoubleAngleField(default_value=0.0)

    Neck4Rz = DoubleAngleField(default_value=0.0)


class Neck4RAttrOperator(
    CompoundAttrOperator[Neck4RPlugOperator]
):
    __slots__ = ()

    Neck4Rx = DoubleAngleField(default_value=0.0)

    Neck4Ry = DoubleAngleField(default_value=0.0)

    Neck4Rz = DoubleAngleField(default_value=0.0)


class Neck4RField(
    CompoundField[Neck4RAttrOperator, Neck4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck4RAttrOperator
    PLUG_CLS = Neck4RPlugOperator

    Neck4Rx = DoubleAngleField(default_value=0.0)

    Neck4Ry = DoubleAngleField(default_value=0.0)

    Neck4Rz = DoubleAngleField(default_value=0.0)


class Neck4SPlugOperator(
    CompoundPlugOperator["Neck4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck4Sx", "Neck4Sx"),
        ("Neck4Sy", "Neck4Sy"),
        ("Neck4Sz", "Neck4Sz"),
    )

    Neck4Sx = DoubleField(default_value=1.0)

    Neck4Sy = DoubleField(default_value=1.0)

    Neck4Sz = DoubleField(default_value=1.0)


class Neck4SAttrOperator(
    CompoundAttrOperator[Neck4SPlugOperator]
):
    __slots__ = ()

    Neck4Sx = DoubleField(default_value=1.0)

    Neck4Sy = DoubleField(default_value=1.0)

    Neck4Sz = DoubleField(default_value=1.0)


class Neck4SField(
    CompoundField[Neck4SAttrOperator, Neck4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck4SAttrOperator
    PLUG_CLS = Neck4SPlugOperator

    Neck4Sx = DoubleField(default_value=1.0)

    Neck4Sy = DoubleField(default_value=1.0)

    Neck4Sz = DoubleField(default_value=1.0)


class Neck5TPlugOperator(
    CompoundPlugOperator["Neck5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck5Tx", "Neck5Tx"),
        ("Neck5Ty", "Neck5Ty"),
        ("Neck5Tz", "Neck5Tz"),
    )

    Neck5Tx = DoubleLinearField(default_value=0.0)

    Neck5Ty = DoubleLinearField(default_value=0.0)

    Neck5Tz = DoubleLinearField(default_value=0.0)


class Neck5TAttrOperator(
    CompoundAttrOperator[Neck5TPlugOperator]
):
    __slots__ = ()

    Neck5Tx = DoubleLinearField(default_value=0.0)

    Neck5Ty = DoubleLinearField(default_value=0.0)

    Neck5Tz = DoubleLinearField(default_value=0.0)


class Neck5TField(
    CompoundField[Neck5TAttrOperator, Neck5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck5TAttrOperator
    PLUG_CLS = Neck5TPlugOperator

    Neck5Tx = DoubleLinearField(default_value=0.0)

    Neck5Ty = DoubleLinearField(default_value=0.0)

    Neck5Tz = DoubleLinearField(default_value=0.0)


class Neck5RPlugOperator(
    CompoundPlugOperator["Neck5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck5Rx", "Neck5Rx"),
        ("Neck5Ry", "Neck5Ry"),
        ("Neck5Rz", "Neck5Rz"),
    )

    Neck5Rx = DoubleAngleField(default_value=0.0)

    Neck5Ry = DoubleAngleField(default_value=0.0)

    Neck5Rz = DoubleAngleField(default_value=0.0)


class Neck5RAttrOperator(
    CompoundAttrOperator[Neck5RPlugOperator]
):
    __slots__ = ()

    Neck5Rx = DoubleAngleField(default_value=0.0)

    Neck5Ry = DoubleAngleField(default_value=0.0)

    Neck5Rz = DoubleAngleField(default_value=0.0)


class Neck5RField(
    CompoundField[Neck5RAttrOperator, Neck5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck5RAttrOperator
    PLUG_CLS = Neck5RPlugOperator

    Neck5Rx = DoubleAngleField(default_value=0.0)

    Neck5Ry = DoubleAngleField(default_value=0.0)

    Neck5Rz = DoubleAngleField(default_value=0.0)


class Neck5SPlugOperator(
    CompoundPlugOperator["Neck5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck5Sx", "Neck5Sx"),
        ("Neck5Sy", "Neck5Sy"),
        ("Neck5Sz", "Neck5Sz"),
    )

    Neck5Sx = DoubleField(default_value=1.0)

    Neck5Sy = DoubleField(default_value=1.0)

    Neck5Sz = DoubleField(default_value=1.0)


class Neck5SAttrOperator(
    CompoundAttrOperator[Neck5SPlugOperator]
):
    __slots__ = ()

    Neck5Sx = DoubleField(default_value=1.0)

    Neck5Sy = DoubleField(default_value=1.0)

    Neck5Sz = DoubleField(default_value=1.0)


class Neck5SField(
    CompoundField[Neck5SAttrOperator, Neck5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck5SAttrOperator
    PLUG_CLS = Neck5SPlugOperator

    Neck5Sx = DoubleField(default_value=1.0)

    Neck5Sy = DoubleField(default_value=1.0)

    Neck5Sz = DoubleField(default_value=1.0)


class Neck6TPlugOperator(
    CompoundPlugOperator["Neck6TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck6Tx", "Neck6Tx"),
        ("Neck6Ty", "Neck6Ty"),
        ("Neck6Tz", "Neck6Tz"),
    )

    Neck6Tx = DoubleLinearField(default_value=0.0)

    Neck6Ty = DoubleLinearField(default_value=0.0)

    Neck6Tz = DoubleLinearField(default_value=0.0)


class Neck6TAttrOperator(
    CompoundAttrOperator[Neck6TPlugOperator]
):
    __slots__ = ()

    Neck6Tx = DoubleLinearField(default_value=0.0)

    Neck6Ty = DoubleLinearField(default_value=0.0)

    Neck6Tz = DoubleLinearField(default_value=0.0)


class Neck6TField(
    CompoundField[Neck6TAttrOperator, Neck6TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck6TAttrOperator
    PLUG_CLS = Neck6TPlugOperator

    Neck6Tx = DoubleLinearField(default_value=0.0)

    Neck6Ty = DoubleLinearField(default_value=0.0)

    Neck6Tz = DoubleLinearField(default_value=0.0)


class Neck6RPlugOperator(
    CompoundPlugOperator["Neck6RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck6Rx", "Neck6Rx"),
        ("Neck6Ry", "Neck6Ry"),
        ("Neck6Rz", "Neck6Rz"),
    )

    Neck6Rx = DoubleAngleField(default_value=0.0)

    Neck6Ry = DoubleAngleField(default_value=0.0)

    Neck6Rz = DoubleAngleField(default_value=0.0)


class Neck6RAttrOperator(
    CompoundAttrOperator[Neck6RPlugOperator]
):
    __slots__ = ()

    Neck6Rx = DoubleAngleField(default_value=0.0)

    Neck6Ry = DoubleAngleField(default_value=0.0)

    Neck6Rz = DoubleAngleField(default_value=0.0)


class Neck6RField(
    CompoundField[Neck6RAttrOperator, Neck6RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck6RAttrOperator
    PLUG_CLS = Neck6RPlugOperator

    Neck6Rx = DoubleAngleField(default_value=0.0)

    Neck6Ry = DoubleAngleField(default_value=0.0)

    Neck6Rz = DoubleAngleField(default_value=0.0)


class Neck6SPlugOperator(
    CompoundPlugOperator["Neck6SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck6Sx", "Neck6Sx"),
        ("Neck6Sy", "Neck6Sy"),
        ("Neck6Sz", "Neck6Sz"),
    )

    Neck6Sx = DoubleField(default_value=1.0)

    Neck6Sy = DoubleField(default_value=1.0)

    Neck6Sz = DoubleField(default_value=1.0)


class Neck6SAttrOperator(
    CompoundAttrOperator[Neck6SPlugOperator]
):
    __slots__ = ()

    Neck6Sx = DoubleField(default_value=1.0)

    Neck6Sy = DoubleField(default_value=1.0)

    Neck6Sz = DoubleField(default_value=1.0)


class Neck6SField(
    CompoundField[Neck6SAttrOperator, Neck6SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck6SAttrOperator
    PLUG_CLS = Neck6SPlugOperator

    Neck6Sx = DoubleField(default_value=1.0)

    Neck6Sy = DoubleField(default_value=1.0)

    Neck6Sz = DoubleField(default_value=1.0)


class Neck7TPlugOperator(
    CompoundPlugOperator["Neck7TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck7Tx", "Neck7Tx"),
        ("Neck7Ty", "Neck7Ty"),
        ("Neck7Tz", "Neck7Tz"),
    )

    Neck7Tx = DoubleLinearField(default_value=0.0)

    Neck7Ty = DoubleLinearField(default_value=0.0)

    Neck7Tz = DoubleLinearField(default_value=0.0)


class Neck7TAttrOperator(
    CompoundAttrOperator[Neck7TPlugOperator]
):
    __slots__ = ()

    Neck7Tx = DoubleLinearField(default_value=0.0)

    Neck7Ty = DoubleLinearField(default_value=0.0)

    Neck7Tz = DoubleLinearField(default_value=0.0)


class Neck7TField(
    CompoundField[Neck7TAttrOperator, Neck7TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck7TAttrOperator
    PLUG_CLS = Neck7TPlugOperator

    Neck7Tx = DoubleLinearField(default_value=0.0)

    Neck7Ty = DoubleLinearField(default_value=0.0)

    Neck7Tz = DoubleLinearField(default_value=0.0)


class Neck7RPlugOperator(
    CompoundPlugOperator["Neck7RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck7Rx", "Neck7Rx"),
        ("Neck7Ry", "Neck7Ry"),
        ("Neck7Rz", "Neck7Rz"),
    )

    Neck7Rx = DoubleAngleField(default_value=0.0)

    Neck7Ry = DoubleAngleField(default_value=0.0)

    Neck7Rz = DoubleAngleField(default_value=0.0)


class Neck7RAttrOperator(
    CompoundAttrOperator[Neck7RPlugOperator]
):
    __slots__ = ()

    Neck7Rx = DoubleAngleField(default_value=0.0)

    Neck7Ry = DoubleAngleField(default_value=0.0)

    Neck7Rz = DoubleAngleField(default_value=0.0)


class Neck7RField(
    CompoundField[Neck7RAttrOperator, Neck7RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck7RAttrOperator
    PLUG_CLS = Neck7RPlugOperator

    Neck7Rx = DoubleAngleField(default_value=0.0)

    Neck7Ry = DoubleAngleField(default_value=0.0)

    Neck7Rz = DoubleAngleField(default_value=0.0)


class Neck7SPlugOperator(
    CompoundPlugOperator["Neck7SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck7Sx", "Neck7Sx"),
        ("Neck7Sy", "Neck7Sy"),
        ("Neck7Sz", "Neck7Sz"),
    )

    Neck7Sx = DoubleField(default_value=1.0)

    Neck7Sy = DoubleField(default_value=1.0)

    Neck7Sz = DoubleField(default_value=1.0)


class Neck7SAttrOperator(
    CompoundAttrOperator[Neck7SPlugOperator]
):
    __slots__ = ()

    Neck7Sx = DoubleField(default_value=1.0)

    Neck7Sy = DoubleField(default_value=1.0)

    Neck7Sz = DoubleField(default_value=1.0)


class Neck7SField(
    CompoundField[Neck7SAttrOperator, Neck7SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck7SAttrOperator
    PLUG_CLS = Neck7SPlugOperator

    Neck7Sx = DoubleField(default_value=1.0)

    Neck7Sy = DoubleField(default_value=1.0)

    Neck7Sz = DoubleField(default_value=1.0)


class Neck8TPlugOperator(
    CompoundPlugOperator["Neck8TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck8Tx", "Neck8Tx"),
        ("Neck8Ty", "Neck8Ty"),
        ("Neck8Tz", "Neck8Tz"),
    )

    Neck8Tx = DoubleLinearField(default_value=0.0)

    Neck8Ty = DoubleLinearField(default_value=0.0)

    Neck8Tz = DoubleLinearField(default_value=0.0)


class Neck8TAttrOperator(
    CompoundAttrOperator[Neck8TPlugOperator]
):
    __slots__ = ()

    Neck8Tx = DoubleLinearField(default_value=0.0)

    Neck8Ty = DoubleLinearField(default_value=0.0)

    Neck8Tz = DoubleLinearField(default_value=0.0)


class Neck8TField(
    CompoundField[Neck8TAttrOperator, Neck8TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck8TAttrOperator
    PLUG_CLS = Neck8TPlugOperator

    Neck8Tx = DoubleLinearField(default_value=0.0)

    Neck8Ty = DoubleLinearField(default_value=0.0)

    Neck8Tz = DoubleLinearField(default_value=0.0)


class Neck8RPlugOperator(
    CompoundPlugOperator["Neck8RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck8Rx", "Neck8Rx"),
        ("Neck8Ry", "Neck8Ry"),
        ("Neck8Rz", "Neck8Rz"),
    )

    Neck8Rx = DoubleAngleField(default_value=0.0)

    Neck8Ry = DoubleAngleField(default_value=0.0)

    Neck8Rz = DoubleAngleField(default_value=0.0)


class Neck8RAttrOperator(
    CompoundAttrOperator[Neck8RPlugOperator]
):
    __slots__ = ()

    Neck8Rx = DoubleAngleField(default_value=0.0)

    Neck8Ry = DoubleAngleField(default_value=0.0)

    Neck8Rz = DoubleAngleField(default_value=0.0)


class Neck8RField(
    CompoundField[Neck8RAttrOperator, Neck8RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck8RAttrOperator
    PLUG_CLS = Neck8RPlugOperator

    Neck8Rx = DoubleAngleField(default_value=0.0)

    Neck8Ry = DoubleAngleField(default_value=0.0)

    Neck8Rz = DoubleAngleField(default_value=0.0)


class Neck8SPlugOperator(
    CompoundPlugOperator["Neck8SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck8Sx", "Neck8Sx"),
        ("Neck8Sy", "Neck8Sy"),
        ("Neck8Sz", "Neck8Sz"),
    )

    Neck8Sx = DoubleField(default_value=1.0)

    Neck8Sy = DoubleField(default_value=1.0)

    Neck8Sz = DoubleField(default_value=1.0)


class Neck8SAttrOperator(
    CompoundAttrOperator[Neck8SPlugOperator]
):
    __slots__ = ()

    Neck8Sx = DoubleField(default_value=1.0)

    Neck8Sy = DoubleField(default_value=1.0)

    Neck8Sz = DoubleField(default_value=1.0)


class Neck8SField(
    CompoundField[Neck8SAttrOperator, Neck8SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck8SAttrOperator
    PLUG_CLS = Neck8SPlugOperator

    Neck8Sx = DoubleField(default_value=1.0)

    Neck8Sy = DoubleField(default_value=1.0)

    Neck8Sz = DoubleField(default_value=1.0)


class Neck9TPlugOperator(
    CompoundPlugOperator["Neck9TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck9Tx", "Neck9Tx"),
        ("Neck9Ty", "Neck9Ty"),
        ("Neck9Tz", "Neck9Tz"),
    )

    Neck9Tx = DoubleLinearField(default_value=0.0)

    Neck9Ty = DoubleLinearField(default_value=0.0)

    Neck9Tz = DoubleLinearField(default_value=0.0)


class Neck9TAttrOperator(
    CompoundAttrOperator[Neck9TPlugOperator]
):
    __slots__ = ()

    Neck9Tx = DoubleLinearField(default_value=0.0)

    Neck9Ty = DoubleLinearField(default_value=0.0)

    Neck9Tz = DoubleLinearField(default_value=0.0)


class Neck9TField(
    CompoundField[Neck9TAttrOperator, Neck9TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck9TAttrOperator
    PLUG_CLS = Neck9TPlugOperator

    Neck9Tx = DoubleLinearField(default_value=0.0)

    Neck9Ty = DoubleLinearField(default_value=0.0)

    Neck9Tz = DoubleLinearField(default_value=0.0)


class Neck9RPlugOperator(
    CompoundPlugOperator["Neck9RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck9Rx", "Neck9Rx"),
        ("Neck9Ry", "Neck9Ry"),
        ("Neck9Rz", "Neck9Rz"),
    )

    Neck9Rx = DoubleAngleField(default_value=0.0)

    Neck9Ry = DoubleAngleField(default_value=0.0)

    Neck9Rz = DoubleAngleField(default_value=0.0)


class Neck9RAttrOperator(
    CompoundAttrOperator[Neck9RPlugOperator]
):
    __slots__ = ()

    Neck9Rx = DoubleAngleField(default_value=0.0)

    Neck9Ry = DoubleAngleField(default_value=0.0)

    Neck9Rz = DoubleAngleField(default_value=0.0)


class Neck9RField(
    CompoundField[Neck9RAttrOperator, Neck9RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck9RAttrOperator
    PLUG_CLS = Neck9RPlugOperator

    Neck9Rx = DoubleAngleField(default_value=0.0)

    Neck9Ry = DoubleAngleField(default_value=0.0)

    Neck9Rz = DoubleAngleField(default_value=0.0)


class Neck9SPlugOperator(
    CompoundPlugOperator["Neck9SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("Neck9Sx", "Neck9Sx"),
        ("Neck9Sy", "Neck9Sy"),
        ("Neck9Sz", "Neck9Sz"),
    )

    Neck9Sx = DoubleField(default_value=1.0)

    Neck9Sy = DoubleField(default_value=1.0)

    Neck9Sz = DoubleField(default_value=1.0)


class Neck9SAttrOperator(
    CompoundAttrOperator[Neck9SPlugOperator]
):
    __slots__ = ()

    Neck9Sx = DoubleField(default_value=1.0)

    Neck9Sy = DoubleField(default_value=1.0)

    Neck9Sz = DoubleField(default_value=1.0)


class Neck9SField(
    CompoundField[Neck9SAttrOperator, Neck9SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Neck9SAttrOperator
    PLUG_CLS = Neck9SPlugOperator

    Neck9Sx = DoubleField(default_value=1.0)

    Neck9Sy = DoubleField(default_value=1.0)

    Neck9Sz = DoubleField(default_value=1.0)


class LeftUpLegRollTPlugOperator(
    CompoundPlugOperator["LeftUpLegRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegRollTx", "LeftUpLegRollTx"),
        ("LeftUpLegRollTy", "LeftUpLegRollTy"),
        ("LeftUpLegRollTz", "LeftUpLegRollTz"),
    )

    LeftUpLegRollTx = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTy = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTz = DoubleLinearField(default_value=0.0)


class LeftUpLegRollTAttrOperator(
    CompoundAttrOperator[LeftUpLegRollTPlugOperator]
):
    __slots__ = ()

    LeftUpLegRollTx = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTy = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTz = DoubleLinearField(default_value=0.0)


class LeftUpLegRollTField(
    CompoundField[LeftUpLegRollTAttrOperator, LeftUpLegRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollTAttrOperator
    PLUG_CLS = LeftUpLegRollTPlugOperator

    LeftUpLegRollTx = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTy = DoubleLinearField(default_value=0.0)

    LeftUpLegRollTz = DoubleLinearField(default_value=0.0)


class LeftUpLegRollRPlugOperator(
    CompoundPlugOperator["LeftUpLegRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegRollRx", "LeftUpLegRollRx"),
        ("LeftUpLegRollRy", "LeftUpLegRollRy"),
        ("LeftUpLegRollRz", "LeftUpLegRollRz"),
    )

    LeftUpLegRollRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRz = DoubleAngleField(default_value=0.0)


class LeftUpLegRollRAttrOperator(
    CompoundAttrOperator[LeftUpLegRollRPlugOperator]
):
    __slots__ = ()

    LeftUpLegRollRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRz = DoubleAngleField(default_value=0.0)


class LeftUpLegRollRField(
    CompoundField[LeftUpLegRollRAttrOperator, LeftUpLegRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollRAttrOperator
    PLUG_CLS = LeftUpLegRollRPlugOperator

    LeftUpLegRollRx = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRy = DoubleAngleField(default_value=0.0)

    LeftUpLegRollRz = DoubleAngleField(default_value=0.0)


class LeftUpLegRollSPlugOperator(
    CompoundPlugOperator["LeftUpLegRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftUpLegRollSx", "LeftUpLegRollSx"),
        ("LeftUpLegRollSy", "LeftUpLegRollSy"),
        ("LeftUpLegRollSz", "LeftUpLegRollSz"),
    )

    LeftUpLegRollSx = DoubleField(default_value=1.0)

    LeftUpLegRollSy = DoubleField(default_value=1.0)

    LeftUpLegRollSz = DoubleField(default_value=1.0)


class LeftUpLegRollSAttrOperator(
    CompoundAttrOperator[LeftUpLegRollSPlugOperator]
):
    __slots__ = ()

    LeftUpLegRollSx = DoubleField(default_value=1.0)

    LeftUpLegRollSy = DoubleField(default_value=1.0)

    LeftUpLegRollSz = DoubleField(default_value=1.0)


class LeftUpLegRollSField(
    CompoundField[LeftUpLegRollSAttrOperator, LeftUpLegRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollSAttrOperator
    PLUG_CLS = LeftUpLegRollSPlugOperator

    LeftUpLegRollSx = DoubleField(default_value=1.0)

    LeftUpLegRollSy = DoubleField(default_value=1.0)

    LeftUpLegRollSz = DoubleField(default_value=1.0)


class LeftLegRollTPlugOperator(
    CompoundPlugOperator["LeftLegRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegRollTx", "LeftLegRollTx"),
        ("LeftLegRollTy", "LeftLegRollTy"),
        ("LeftLegRollTz", "LeftLegRollTz"),
    )

    LeftLegRollTx = DoubleLinearField(default_value=0.0)

    LeftLegRollTy = DoubleLinearField(default_value=0.0)

    LeftLegRollTz = DoubleLinearField(default_value=0.0)


class LeftLegRollTAttrOperator(
    CompoundAttrOperator[LeftLegRollTPlugOperator]
):
    __slots__ = ()

    LeftLegRollTx = DoubleLinearField(default_value=0.0)

    LeftLegRollTy = DoubleLinearField(default_value=0.0)

    LeftLegRollTz = DoubleLinearField(default_value=0.0)


class LeftLegRollTField(
    CompoundField[LeftLegRollTAttrOperator, LeftLegRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollTAttrOperator
    PLUG_CLS = LeftLegRollTPlugOperator

    LeftLegRollTx = DoubleLinearField(default_value=0.0)

    LeftLegRollTy = DoubleLinearField(default_value=0.0)

    LeftLegRollTz = DoubleLinearField(default_value=0.0)


class LeftLegRollRPlugOperator(
    CompoundPlugOperator["LeftLegRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegRollRx", "LeftLegRollRx"),
        ("LeftLegRollRy", "LeftLegRollRy"),
        ("LeftLegRollRz", "LeftLegRollRz"),
    )

    LeftLegRollRx = DoubleAngleField(default_value=0.0)

    LeftLegRollRy = DoubleAngleField(default_value=0.0)

    LeftLegRollRz = DoubleAngleField(default_value=0.0)


class LeftLegRollRAttrOperator(
    CompoundAttrOperator[LeftLegRollRPlugOperator]
):
    __slots__ = ()

    LeftLegRollRx = DoubleAngleField(default_value=0.0)

    LeftLegRollRy = DoubleAngleField(default_value=0.0)

    LeftLegRollRz = DoubleAngleField(default_value=0.0)


class LeftLegRollRField(
    CompoundField[LeftLegRollRAttrOperator, LeftLegRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollRAttrOperator
    PLUG_CLS = LeftLegRollRPlugOperator

    LeftLegRollRx = DoubleAngleField(default_value=0.0)

    LeftLegRollRy = DoubleAngleField(default_value=0.0)

    LeftLegRollRz = DoubleAngleField(default_value=0.0)


class LeftLegRollSPlugOperator(
    CompoundPlugOperator["LeftLegRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftLegRollSx", "LeftLegRollSx"),
        ("LeftLegRollSy", "LeftLegRollSy"),
        ("LeftLegRollSz", "LeftLegRollSz"),
    )

    LeftLegRollSx = DoubleField(default_value=1.0)

    LeftLegRollSy = DoubleField(default_value=1.0)

    LeftLegRollSz = DoubleField(default_value=1.0)


class LeftLegRollSAttrOperator(
    CompoundAttrOperator[LeftLegRollSPlugOperator]
):
    __slots__ = ()

    LeftLegRollSx = DoubleField(default_value=1.0)

    LeftLegRollSy = DoubleField(default_value=1.0)

    LeftLegRollSz = DoubleField(default_value=1.0)


class LeftLegRollSField(
    CompoundField[LeftLegRollSAttrOperator, LeftLegRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollSAttrOperator
    PLUG_CLS = LeftLegRollSPlugOperator

    LeftLegRollSx = DoubleField(default_value=1.0)

    LeftLegRollSy = DoubleField(default_value=1.0)

    LeftLegRollSz = DoubleField(default_value=1.0)


class RightUpLegRollTPlugOperator(
    CompoundPlugOperator["RightUpLegRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegRollTx", "RightUpLegRollTx"),
        ("RightUpLegRollTy", "RightUpLegRollTy"),
        ("RightUpLegRollTz", "RightUpLegRollTz"),
    )

    RightUpLegRollTx = DoubleLinearField(default_value=0.0)

    RightUpLegRollTy = DoubleLinearField(default_value=0.0)

    RightUpLegRollTz = DoubleLinearField(default_value=0.0)


class RightUpLegRollTAttrOperator(
    CompoundAttrOperator[RightUpLegRollTPlugOperator]
):
    __slots__ = ()

    RightUpLegRollTx = DoubleLinearField(default_value=0.0)

    RightUpLegRollTy = DoubleLinearField(default_value=0.0)

    RightUpLegRollTz = DoubleLinearField(default_value=0.0)


class RightUpLegRollTField(
    CompoundField[RightUpLegRollTAttrOperator, RightUpLegRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollTAttrOperator
    PLUG_CLS = RightUpLegRollTPlugOperator

    RightUpLegRollTx = DoubleLinearField(default_value=0.0)

    RightUpLegRollTy = DoubleLinearField(default_value=0.0)

    RightUpLegRollTz = DoubleLinearField(default_value=0.0)


class RightUpLegRollRPlugOperator(
    CompoundPlugOperator["RightUpLegRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegRollRx", "RightUpLegRollRx"),
        ("RightUpLegRollRy", "RightUpLegRollRy"),
        ("RightUpLegRollRz", "RightUpLegRollRz"),
    )

    RightUpLegRollRx = DoubleAngleField(default_value=0.0)

    RightUpLegRollRy = DoubleAngleField(default_value=0.0)

    RightUpLegRollRz = DoubleAngleField(default_value=0.0)


class RightUpLegRollRAttrOperator(
    CompoundAttrOperator[RightUpLegRollRPlugOperator]
):
    __slots__ = ()

    RightUpLegRollRx = DoubleAngleField(default_value=0.0)

    RightUpLegRollRy = DoubleAngleField(default_value=0.0)

    RightUpLegRollRz = DoubleAngleField(default_value=0.0)


class RightUpLegRollRField(
    CompoundField[RightUpLegRollRAttrOperator, RightUpLegRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollRAttrOperator
    PLUG_CLS = RightUpLegRollRPlugOperator

    RightUpLegRollRx = DoubleAngleField(default_value=0.0)

    RightUpLegRollRy = DoubleAngleField(default_value=0.0)

    RightUpLegRollRz = DoubleAngleField(default_value=0.0)


class RightUpLegRollSPlugOperator(
    CompoundPlugOperator["RightUpLegRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightUpLegRollSx", "RightUpLegRollSx"),
        ("RightUpLegRollSy", "RightUpLegRollSy"),
        ("RightUpLegRollSz", "RightUpLegRollSz"),
    )

    RightUpLegRollSx = DoubleField(default_value=1.0)

    RightUpLegRollSy = DoubleField(default_value=1.0)

    RightUpLegRollSz = DoubleField(default_value=1.0)


class RightUpLegRollSAttrOperator(
    CompoundAttrOperator[RightUpLegRollSPlugOperator]
):
    __slots__ = ()

    RightUpLegRollSx = DoubleField(default_value=1.0)

    RightUpLegRollSy = DoubleField(default_value=1.0)

    RightUpLegRollSz = DoubleField(default_value=1.0)


class RightUpLegRollSField(
    CompoundField[RightUpLegRollSAttrOperator, RightUpLegRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollSAttrOperator
    PLUG_CLS = RightUpLegRollSPlugOperator

    RightUpLegRollSx = DoubleField(default_value=1.0)

    RightUpLegRollSy = DoubleField(default_value=1.0)

    RightUpLegRollSz = DoubleField(default_value=1.0)


class RightLegRollTPlugOperator(
    CompoundPlugOperator["RightLegRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegRollTx", "RightLegRollTx"),
        ("RightLegRollTy", "RightLegRollTy"),
        ("RightLegRollTz", "RightLegRollTz"),
    )

    RightLegRollTx = DoubleLinearField(default_value=0.0)

    RightLegRollTy = DoubleLinearField(default_value=0.0)

    RightLegRollTz = DoubleLinearField(default_value=0.0)


class RightLegRollTAttrOperator(
    CompoundAttrOperator[RightLegRollTPlugOperator]
):
    __slots__ = ()

    RightLegRollTx = DoubleLinearField(default_value=0.0)

    RightLegRollTy = DoubleLinearField(default_value=0.0)

    RightLegRollTz = DoubleLinearField(default_value=0.0)


class RightLegRollTField(
    CompoundField[RightLegRollTAttrOperator, RightLegRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollTAttrOperator
    PLUG_CLS = RightLegRollTPlugOperator

    RightLegRollTx = DoubleLinearField(default_value=0.0)

    RightLegRollTy = DoubleLinearField(default_value=0.0)

    RightLegRollTz = DoubleLinearField(default_value=0.0)


class RightLegRollRPlugOperator(
    CompoundPlugOperator["RightLegRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegRollRx", "RightLegRollRx"),
        ("RightLegRollRy", "RightLegRollRy"),
        ("RightLegRollRz", "RightLegRollRz"),
    )

    RightLegRollRx = DoubleAngleField(default_value=0.0)

    RightLegRollRy = DoubleAngleField(default_value=0.0)

    RightLegRollRz = DoubleAngleField(default_value=0.0)


class RightLegRollRAttrOperator(
    CompoundAttrOperator[RightLegRollRPlugOperator]
):
    __slots__ = ()

    RightLegRollRx = DoubleAngleField(default_value=0.0)

    RightLegRollRy = DoubleAngleField(default_value=0.0)

    RightLegRollRz = DoubleAngleField(default_value=0.0)


class RightLegRollRField(
    CompoundField[RightLegRollRAttrOperator, RightLegRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollRAttrOperator
    PLUG_CLS = RightLegRollRPlugOperator

    RightLegRollRx = DoubleAngleField(default_value=0.0)

    RightLegRollRy = DoubleAngleField(default_value=0.0)

    RightLegRollRz = DoubleAngleField(default_value=0.0)


class RightLegRollSPlugOperator(
    CompoundPlugOperator["RightLegRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightLegRollSx", "RightLegRollSx"),
        ("RightLegRollSy", "RightLegRollSy"),
        ("RightLegRollSz", "RightLegRollSz"),
    )

    RightLegRollSx = DoubleField(default_value=1.0)

    RightLegRollSy = DoubleField(default_value=1.0)

    RightLegRollSz = DoubleField(default_value=1.0)


class RightLegRollSAttrOperator(
    CompoundAttrOperator[RightLegRollSPlugOperator]
):
    __slots__ = ()

    RightLegRollSx = DoubleField(default_value=1.0)

    RightLegRollSy = DoubleField(default_value=1.0)

    RightLegRollSz = DoubleField(default_value=1.0)


class RightLegRollSField(
    CompoundField[RightLegRollSAttrOperator, RightLegRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollSAttrOperator
    PLUG_CLS = RightLegRollSPlugOperator

    RightLegRollSx = DoubleField(default_value=1.0)

    RightLegRollSy = DoubleField(default_value=1.0)

    RightLegRollSz = DoubleField(default_value=1.0)


class LeftArmRollTPlugOperator(
    CompoundPlugOperator["LeftArmRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmRollTx", "LeftArmRollTx"),
        ("LeftArmRollTy", "LeftArmRollTy"),
        ("LeftArmRollTz", "LeftArmRollTz"),
    )

    LeftArmRollTx = DoubleLinearField(default_value=0.0)

    LeftArmRollTy = DoubleLinearField(default_value=0.0)

    LeftArmRollTz = DoubleLinearField(default_value=0.0)


class LeftArmRollTAttrOperator(
    CompoundAttrOperator[LeftArmRollTPlugOperator]
):
    __slots__ = ()

    LeftArmRollTx = DoubleLinearField(default_value=0.0)

    LeftArmRollTy = DoubleLinearField(default_value=0.0)

    LeftArmRollTz = DoubleLinearField(default_value=0.0)


class LeftArmRollTField(
    CompoundField[LeftArmRollTAttrOperator, LeftArmRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollTAttrOperator
    PLUG_CLS = LeftArmRollTPlugOperator

    LeftArmRollTx = DoubleLinearField(default_value=0.0)

    LeftArmRollTy = DoubleLinearField(default_value=0.0)

    LeftArmRollTz = DoubleLinearField(default_value=0.0)


class LeftArmRollRPlugOperator(
    CompoundPlugOperator["LeftArmRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmRollRx", "LeftArmRollRx"),
        ("LeftArmRollRy", "LeftArmRollRy"),
        ("LeftArmRollRz", "LeftArmRollRz"),
    )

    LeftArmRollRx = DoubleAngleField(default_value=0.0)

    LeftArmRollRy = DoubleAngleField(default_value=0.0)

    LeftArmRollRz = DoubleAngleField(default_value=0.0)


class LeftArmRollRAttrOperator(
    CompoundAttrOperator[LeftArmRollRPlugOperator]
):
    __slots__ = ()

    LeftArmRollRx = DoubleAngleField(default_value=0.0)

    LeftArmRollRy = DoubleAngleField(default_value=0.0)

    LeftArmRollRz = DoubleAngleField(default_value=0.0)


class LeftArmRollRField(
    CompoundField[LeftArmRollRAttrOperator, LeftArmRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollRAttrOperator
    PLUG_CLS = LeftArmRollRPlugOperator

    LeftArmRollRx = DoubleAngleField(default_value=0.0)

    LeftArmRollRy = DoubleAngleField(default_value=0.0)

    LeftArmRollRz = DoubleAngleField(default_value=0.0)


class LeftArmRollSPlugOperator(
    CompoundPlugOperator["LeftArmRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftArmRollSx", "LeftArmRollSx"),
        ("LeftArmRollSy", "LeftArmRollSy"),
        ("LeftArmRollSz", "LeftArmRollSz"),
    )

    LeftArmRollSx = DoubleField(default_value=1.0)

    LeftArmRollSy = DoubleField(default_value=1.0)

    LeftArmRollSz = DoubleField(default_value=1.0)


class LeftArmRollSAttrOperator(
    CompoundAttrOperator[LeftArmRollSPlugOperator]
):
    __slots__ = ()

    LeftArmRollSx = DoubleField(default_value=1.0)

    LeftArmRollSy = DoubleField(default_value=1.0)

    LeftArmRollSz = DoubleField(default_value=1.0)


class LeftArmRollSField(
    CompoundField[LeftArmRollSAttrOperator, LeftArmRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollSAttrOperator
    PLUG_CLS = LeftArmRollSPlugOperator

    LeftArmRollSx = DoubleField(default_value=1.0)

    LeftArmRollSy = DoubleField(default_value=1.0)

    LeftArmRollSz = DoubleField(default_value=1.0)


class LeftForeArmRollTPlugOperator(
    CompoundPlugOperator["LeftForeArmRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmRollTx", "LeftForeArmRollTx"),
        ("LeftForeArmRollTy", "LeftForeArmRollTy"),
        ("LeftForeArmRollTz", "LeftForeArmRollTz"),
    )

    LeftForeArmRollTx = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTy = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTz = DoubleLinearField(default_value=0.0)


class LeftForeArmRollTAttrOperator(
    CompoundAttrOperator[LeftForeArmRollTPlugOperator]
):
    __slots__ = ()

    LeftForeArmRollTx = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTy = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTz = DoubleLinearField(default_value=0.0)


class LeftForeArmRollTField(
    CompoundField[LeftForeArmRollTAttrOperator, LeftForeArmRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollTAttrOperator
    PLUG_CLS = LeftForeArmRollTPlugOperator

    LeftForeArmRollTx = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTy = DoubleLinearField(default_value=0.0)

    LeftForeArmRollTz = DoubleLinearField(default_value=0.0)


class LeftForeArmRollRPlugOperator(
    CompoundPlugOperator["LeftForeArmRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmRollRx", "LeftForeArmRollRx"),
        ("LeftForeArmRollRy", "LeftForeArmRollRy"),
        ("LeftForeArmRollRz", "LeftForeArmRollRz"),
    )

    LeftForeArmRollRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRz = DoubleAngleField(default_value=0.0)


class LeftForeArmRollRAttrOperator(
    CompoundAttrOperator[LeftForeArmRollRPlugOperator]
):
    __slots__ = ()

    LeftForeArmRollRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRz = DoubleAngleField(default_value=0.0)


class LeftForeArmRollRField(
    CompoundField[LeftForeArmRollRAttrOperator, LeftForeArmRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollRAttrOperator
    PLUG_CLS = LeftForeArmRollRPlugOperator

    LeftForeArmRollRx = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRy = DoubleAngleField(default_value=0.0)

    LeftForeArmRollRz = DoubleAngleField(default_value=0.0)


class LeftForeArmRollSPlugOperator(
    CompoundPlugOperator["LeftForeArmRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftForeArmRollSx", "LeftForeArmRollSx"),
        ("LeftForeArmRollSy", "LeftForeArmRollSy"),
        ("LeftForeArmRollSz", "LeftForeArmRollSz"),
    )

    LeftForeArmRollSx = DoubleField(default_value=1.0)

    LeftForeArmRollSy = DoubleField(default_value=1.0)

    LeftForeArmRollSz = DoubleField(default_value=1.0)


class LeftForeArmRollSAttrOperator(
    CompoundAttrOperator[LeftForeArmRollSPlugOperator]
):
    __slots__ = ()

    LeftForeArmRollSx = DoubleField(default_value=1.0)

    LeftForeArmRollSy = DoubleField(default_value=1.0)

    LeftForeArmRollSz = DoubleField(default_value=1.0)


class LeftForeArmRollSField(
    CompoundField[LeftForeArmRollSAttrOperator, LeftForeArmRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollSAttrOperator
    PLUG_CLS = LeftForeArmRollSPlugOperator

    LeftForeArmRollSx = DoubleField(default_value=1.0)

    LeftForeArmRollSy = DoubleField(default_value=1.0)

    LeftForeArmRollSz = DoubleField(default_value=1.0)


class RightArmRollTPlugOperator(
    CompoundPlugOperator["RightArmRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmRollTx", "RightArmRollTx"),
        ("RightArmRollTy", "RightArmRollTy"),
        ("RightArmRollTz", "RightArmRollTz"),
    )

    RightArmRollTx = DoubleLinearField(default_value=0.0)

    RightArmRollTy = DoubleLinearField(default_value=0.0)

    RightArmRollTz = DoubleLinearField(default_value=0.0)


class RightArmRollTAttrOperator(
    CompoundAttrOperator[RightArmRollTPlugOperator]
):
    __slots__ = ()

    RightArmRollTx = DoubleLinearField(default_value=0.0)

    RightArmRollTy = DoubleLinearField(default_value=0.0)

    RightArmRollTz = DoubleLinearField(default_value=0.0)


class RightArmRollTField(
    CompoundField[RightArmRollTAttrOperator, RightArmRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollTAttrOperator
    PLUG_CLS = RightArmRollTPlugOperator

    RightArmRollTx = DoubleLinearField(default_value=0.0)

    RightArmRollTy = DoubleLinearField(default_value=0.0)

    RightArmRollTz = DoubleLinearField(default_value=0.0)


class RightArmRollRPlugOperator(
    CompoundPlugOperator["RightArmRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmRollRx", "RightArmRollRx"),
        ("RightArmRollRy", "RightArmRollRy"),
        ("RightArmRollRz", "RightArmRollRz"),
    )

    RightArmRollRx = DoubleAngleField(default_value=0.0)

    RightArmRollRy = DoubleAngleField(default_value=0.0)

    RightArmRollRz = DoubleAngleField(default_value=0.0)


class RightArmRollRAttrOperator(
    CompoundAttrOperator[RightArmRollRPlugOperator]
):
    __slots__ = ()

    RightArmRollRx = DoubleAngleField(default_value=0.0)

    RightArmRollRy = DoubleAngleField(default_value=0.0)

    RightArmRollRz = DoubleAngleField(default_value=0.0)


class RightArmRollRField(
    CompoundField[RightArmRollRAttrOperator, RightArmRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollRAttrOperator
    PLUG_CLS = RightArmRollRPlugOperator

    RightArmRollRx = DoubleAngleField(default_value=0.0)

    RightArmRollRy = DoubleAngleField(default_value=0.0)

    RightArmRollRz = DoubleAngleField(default_value=0.0)


class RightArmRollSPlugOperator(
    CompoundPlugOperator["RightArmRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightArmRollSx", "RightArmRollSx"),
        ("RightArmRollSy", "RightArmRollSy"),
        ("RightArmRollSz", "RightArmRollSz"),
    )

    RightArmRollSx = DoubleField(default_value=1.0)

    RightArmRollSy = DoubleField(default_value=1.0)

    RightArmRollSz = DoubleField(default_value=1.0)


class RightArmRollSAttrOperator(
    CompoundAttrOperator[RightArmRollSPlugOperator]
):
    __slots__ = ()

    RightArmRollSx = DoubleField(default_value=1.0)

    RightArmRollSy = DoubleField(default_value=1.0)

    RightArmRollSz = DoubleField(default_value=1.0)


class RightArmRollSField(
    CompoundField[RightArmRollSAttrOperator, RightArmRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollSAttrOperator
    PLUG_CLS = RightArmRollSPlugOperator

    RightArmRollSx = DoubleField(default_value=1.0)

    RightArmRollSy = DoubleField(default_value=1.0)

    RightArmRollSz = DoubleField(default_value=1.0)


class RightForeArmRollTPlugOperator(
    CompoundPlugOperator["RightForeArmRollTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmRollTx", "RightForeArmRollTx"),
        ("RightForeArmRollTy", "RightForeArmRollTy"),
        ("RightForeArmRollTz", "RightForeArmRollTz"),
    )

    RightForeArmRollTx = DoubleLinearField(default_value=0.0)

    RightForeArmRollTy = DoubleLinearField(default_value=0.0)

    RightForeArmRollTz = DoubleLinearField(default_value=0.0)


class RightForeArmRollTAttrOperator(
    CompoundAttrOperator[RightForeArmRollTPlugOperator]
):
    __slots__ = ()

    RightForeArmRollTx = DoubleLinearField(default_value=0.0)

    RightForeArmRollTy = DoubleLinearField(default_value=0.0)

    RightForeArmRollTz = DoubleLinearField(default_value=0.0)


class RightForeArmRollTField(
    CompoundField[RightForeArmRollTAttrOperator, RightForeArmRollTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollTAttrOperator
    PLUG_CLS = RightForeArmRollTPlugOperator

    RightForeArmRollTx = DoubleLinearField(default_value=0.0)

    RightForeArmRollTy = DoubleLinearField(default_value=0.0)

    RightForeArmRollTz = DoubleLinearField(default_value=0.0)


class RightForeArmRollRPlugOperator(
    CompoundPlugOperator["RightForeArmRollRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmRollRx", "RightForeArmRollRx"),
        ("RightForeArmRollRy", "RightForeArmRollRy"),
        ("RightForeArmRollRz", "RightForeArmRollRz"),
    )

    RightForeArmRollRx = DoubleAngleField(default_value=0.0)

    RightForeArmRollRy = DoubleAngleField(default_value=0.0)

    RightForeArmRollRz = DoubleAngleField(default_value=0.0)


class RightForeArmRollRAttrOperator(
    CompoundAttrOperator[RightForeArmRollRPlugOperator]
):
    __slots__ = ()

    RightForeArmRollRx = DoubleAngleField(default_value=0.0)

    RightForeArmRollRy = DoubleAngleField(default_value=0.0)

    RightForeArmRollRz = DoubleAngleField(default_value=0.0)


class RightForeArmRollRField(
    CompoundField[RightForeArmRollRAttrOperator, RightForeArmRollRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollRAttrOperator
    PLUG_CLS = RightForeArmRollRPlugOperator

    RightForeArmRollRx = DoubleAngleField(default_value=0.0)

    RightForeArmRollRy = DoubleAngleField(default_value=0.0)

    RightForeArmRollRz = DoubleAngleField(default_value=0.0)


class RightForeArmRollSPlugOperator(
    CompoundPlugOperator["RightForeArmRollSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightForeArmRollSx", "RightForeArmRollSx"),
        ("RightForeArmRollSy", "RightForeArmRollSy"),
        ("RightForeArmRollSz", "RightForeArmRollSz"),
    )

    RightForeArmRollSx = DoubleField(default_value=1.0)

    RightForeArmRollSy = DoubleField(default_value=1.0)

    RightForeArmRollSz = DoubleField(default_value=1.0)


class RightForeArmRollSAttrOperator(
    CompoundAttrOperator[RightForeArmRollSPlugOperator]
):
    __slots__ = ()

    RightForeArmRollSx = DoubleField(default_value=1.0)

    RightForeArmRollSy = DoubleField(default_value=1.0)

    RightForeArmRollSz = DoubleField(default_value=1.0)


class RightForeArmRollSField(
    CompoundField[RightForeArmRollSAttrOperator, RightForeArmRollSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollSAttrOperator
    PLUG_CLS = RightForeArmRollSPlugOperator

    RightForeArmRollSx = DoubleField(default_value=1.0)

    RightForeArmRollSy = DoubleField(default_value=1.0)

    RightForeArmRollSz = DoubleField(default_value=1.0)


class HipsTranslationTPlugOperator(
    CompoundPlugOperator["HipsTranslationTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsTranslationTx", "HipsTranslationTx"),
        ("HipsTranslationTy", "HipsTranslationTy"),
        ("HipsTranslationTz", "HipsTranslationTz"),
    )

    HipsTranslationTx = DoubleLinearField(default_value=0.0)

    HipsTranslationTy = DoubleLinearField(default_value=0.0)

    HipsTranslationTz = DoubleLinearField(default_value=0.0)


class HipsTranslationTAttrOperator(
    CompoundAttrOperator[HipsTranslationTPlugOperator]
):
    __slots__ = ()

    HipsTranslationTx = DoubleLinearField(default_value=0.0)

    HipsTranslationTy = DoubleLinearField(default_value=0.0)

    HipsTranslationTz = DoubleLinearField(default_value=0.0)


class HipsTranslationTField(
    CompoundField[HipsTranslationTAttrOperator, HipsTranslationTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationTAttrOperator
    PLUG_CLS = HipsTranslationTPlugOperator

    HipsTranslationTx = DoubleLinearField(default_value=0.0)

    HipsTranslationTy = DoubleLinearField(default_value=0.0)

    HipsTranslationTz = DoubleLinearField(default_value=0.0)


class HipsTranslationRPlugOperator(
    CompoundPlugOperator["HipsTranslationRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsTranslationRx", "HipsTranslationRx"),
        ("HipsTranslationRy", "HipsTranslationRy"),
        ("HipsTranslationRz", "HipsTranslationRz"),
    )

    HipsTranslationRx = DoubleAngleField(default_value=0.0)

    HipsTranslationRy = DoubleAngleField(default_value=0.0)

    HipsTranslationRz = DoubleAngleField(default_value=0.0)


class HipsTranslationRAttrOperator(
    CompoundAttrOperator[HipsTranslationRPlugOperator]
):
    __slots__ = ()

    HipsTranslationRx = DoubleAngleField(default_value=0.0)

    HipsTranslationRy = DoubleAngleField(default_value=0.0)

    HipsTranslationRz = DoubleAngleField(default_value=0.0)


class HipsTranslationRField(
    CompoundField[HipsTranslationRAttrOperator, HipsTranslationRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationRAttrOperator
    PLUG_CLS = HipsTranslationRPlugOperator

    HipsTranslationRx = DoubleAngleField(default_value=0.0)

    HipsTranslationRy = DoubleAngleField(default_value=0.0)

    HipsTranslationRz = DoubleAngleField(default_value=0.0)


class HipsTranslationSPlugOperator(
    CompoundPlugOperator["HipsTranslationSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("HipsTranslationSx", "HipsTranslationSx"),
        ("HipsTranslationSy", "HipsTranslationSy"),
        ("HipsTranslationSz", "HipsTranslationSz"),
    )

    HipsTranslationSx = DoubleField(default_value=1.0)

    HipsTranslationSy = DoubleField(default_value=1.0)

    HipsTranslationSz = DoubleField(default_value=1.0)


class HipsTranslationSAttrOperator(
    CompoundAttrOperator[HipsTranslationSPlugOperator]
):
    __slots__ = ()

    HipsTranslationSx = DoubleField(default_value=1.0)

    HipsTranslationSy = DoubleField(default_value=1.0)

    HipsTranslationSz = DoubleField(default_value=1.0)


class HipsTranslationSField(
    CompoundField[HipsTranslationSAttrOperator, HipsTranslationSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationSAttrOperator
    PLUG_CLS = HipsTranslationSPlugOperator

    HipsTranslationSx = DoubleField(default_value=1.0)

    HipsTranslationSy = DoubleField(default_value=1.0)

    HipsTranslationSz = DoubleField(default_value=1.0)


class LeftHandThumb1TPlugOperator(
    CompoundPlugOperator["LeftHandThumb1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb1Tx", "LeftHandThumb1Tx"),
        ("LeftHandThumb1Ty", "LeftHandThumb1Ty"),
        ("LeftHandThumb1Tz", "LeftHandThumb1Tz"),
    )

    LeftHandThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb1TAttrOperator(
    CompoundAttrOperator[LeftHandThumb1TPlugOperator]
):
    __slots__ = ()

    LeftHandThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb1TField(
    CompoundField[LeftHandThumb1TAttrOperator, LeftHandThumb1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb1TAttrOperator
    PLUG_CLS = LeftHandThumb1TPlugOperator

    LeftHandThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb1RPlugOperator(
    CompoundPlugOperator["LeftHandThumb1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb1Rx", "LeftHandThumb1Rx"),
        ("LeftHandThumb1Ry", "LeftHandThumb1Ry"),
        ("LeftHandThumb1Rz", "LeftHandThumb1Rz"),
    )

    LeftHandThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb1RAttrOperator(
    CompoundAttrOperator[LeftHandThumb1RPlugOperator]
):
    __slots__ = ()

    LeftHandThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb1RField(
    CompoundField[LeftHandThumb1RAttrOperator, LeftHandThumb1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb1RAttrOperator
    PLUG_CLS = LeftHandThumb1RPlugOperator

    LeftHandThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb1SPlugOperator(
    CompoundPlugOperator["LeftHandThumb1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb1Sx", "LeftHandThumb1Sx"),
        ("LeftHandThumb1Sy", "LeftHandThumb1Sy"),
        ("LeftHandThumb1Sz", "LeftHandThumb1Sz"),
    )

    LeftHandThumb1Sx = DoubleField(default_value=1.0)

    LeftHandThumb1Sy = DoubleField(default_value=1.0)

    LeftHandThumb1Sz = DoubleField(default_value=1.0)


class LeftHandThumb1SAttrOperator(
    CompoundAttrOperator[LeftHandThumb1SPlugOperator]
):
    __slots__ = ()

    LeftHandThumb1Sx = DoubleField(default_value=1.0)

    LeftHandThumb1Sy = DoubleField(default_value=1.0)

    LeftHandThumb1Sz = DoubleField(default_value=1.0)


class LeftHandThumb1SField(
    CompoundField[LeftHandThumb1SAttrOperator, LeftHandThumb1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb1SAttrOperator
    PLUG_CLS = LeftHandThumb1SPlugOperator

    LeftHandThumb1Sx = DoubleField(default_value=1.0)

    LeftHandThumb1Sy = DoubleField(default_value=1.0)

    LeftHandThumb1Sz = DoubleField(default_value=1.0)


class LeftHandThumb2TPlugOperator(
    CompoundPlugOperator["LeftHandThumb2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb2Tx", "LeftHandThumb2Tx"),
        ("LeftHandThumb2Ty", "LeftHandThumb2Ty"),
        ("LeftHandThumb2Tz", "LeftHandThumb2Tz"),
    )

    LeftHandThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb2TAttrOperator(
    CompoundAttrOperator[LeftHandThumb2TPlugOperator]
):
    __slots__ = ()

    LeftHandThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb2TField(
    CompoundField[LeftHandThumb2TAttrOperator, LeftHandThumb2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb2TAttrOperator
    PLUG_CLS = LeftHandThumb2TPlugOperator

    LeftHandThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb2RPlugOperator(
    CompoundPlugOperator["LeftHandThumb2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb2Rx", "LeftHandThumb2Rx"),
        ("LeftHandThumb2Ry", "LeftHandThumb2Ry"),
        ("LeftHandThumb2Rz", "LeftHandThumb2Rz"),
    )

    LeftHandThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb2RAttrOperator(
    CompoundAttrOperator[LeftHandThumb2RPlugOperator]
):
    __slots__ = ()

    LeftHandThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb2RField(
    CompoundField[LeftHandThumb2RAttrOperator, LeftHandThumb2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb2RAttrOperator
    PLUG_CLS = LeftHandThumb2RPlugOperator

    LeftHandThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb2SPlugOperator(
    CompoundPlugOperator["LeftHandThumb2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb2Sx", "LeftHandThumb2Sx"),
        ("LeftHandThumb2Sy", "LeftHandThumb2Sy"),
        ("LeftHandThumb2Sz", "LeftHandThumb2Sz"),
    )

    LeftHandThumb2Sx = DoubleField(default_value=1.0)

    LeftHandThumb2Sy = DoubleField(default_value=1.0)

    LeftHandThumb2Sz = DoubleField(default_value=1.0)


class LeftHandThumb2SAttrOperator(
    CompoundAttrOperator[LeftHandThumb2SPlugOperator]
):
    __slots__ = ()

    LeftHandThumb2Sx = DoubleField(default_value=1.0)

    LeftHandThumb2Sy = DoubleField(default_value=1.0)

    LeftHandThumb2Sz = DoubleField(default_value=1.0)


class LeftHandThumb2SField(
    CompoundField[LeftHandThumb2SAttrOperator, LeftHandThumb2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb2SAttrOperator
    PLUG_CLS = LeftHandThumb2SPlugOperator

    LeftHandThumb2Sx = DoubleField(default_value=1.0)

    LeftHandThumb2Sy = DoubleField(default_value=1.0)

    LeftHandThumb2Sz = DoubleField(default_value=1.0)


class LeftHandThumb3TPlugOperator(
    CompoundPlugOperator["LeftHandThumb3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb3Tx", "LeftHandThumb3Tx"),
        ("LeftHandThumb3Ty", "LeftHandThumb3Ty"),
        ("LeftHandThumb3Tz", "LeftHandThumb3Tz"),
    )

    LeftHandThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb3TAttrOperator(
    CompoundAttrOperator[LeftHandThumb3TPlugOperator]
):
    __slots__ = ()

    LeftHandThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb3TField(
    CompoundField[LeftHandThumb3TAttrOperator, LeftHandThumb3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb3TAttrOperator
    PLUG_CLS = LeftHandThumb3TPlugOperator

    LeftHandThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb3RPlugOperator(
    CompoundPlugOperator["LeftHandThumb3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb3Rx", "LeftHandThumb3Rx"),
        ("LeftHandThumb3Ry", "LeftHandThumb3Ry"),
        ("LeftHandThumb3Rz", "LeftHandThumb3Rz"),
    )

    LeftHandThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb3RAttrOperator(
    CompoundAttrOperator[LeftHandThumb3RPlugOperator]
):
    __slots__ = ()

    LeftHandThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb3RField(
    CompoundField[LeftHandThumb3RAttrOperator, LeftHandThumb3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb3RAttrOperator
    PLUG_CLS = LeftHandThumb3RPlugOperator

    LeftHandThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb3SPlugOperator(
    CompoundPlugOperator["LeftHandThumb3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb3Sx", "LeftHandThumb3Sx"),
        ("LeftHandThumb3Sy", "LeftHandThumb3Sy"),
        ("LeftHandThumb3Sz", "LeftHandThumb3Sz"),
    )

    LeftHandThumb3Sx = DoubleField(default_value=1.0)

    LeftHandThumb3Sy = DoubleField(default_value=1.0)

    LeftHandThumb3Sz = DoubleField(default_value=1.0)


class LeftHandThumb3SAttrOperator(
    CompoundAttrOperator[LeftHandThumb3SPlugOperator]
):
    __slots__ = ()

    LeftHandThumb3Sx = DoubleField(default_value=1.0)

    LeftHandThumb3Sy = DoubleField(default_value=1.0)

    LeftHandThumb3Sz = DoubleField(default_value=1.0)


class LeftHandThumb3SField(
    CompoundField[LeftHandThumb3SAttrOperator, LeftHandThumb3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb3SAttrOperator
    PLUG_CLS = LeftHandThumb3SPlugOperator

    LeftHandThumb3Sx = DoubleField(default_value=1.0)

    LeftHandThumb3Sy = DoubleField(default_value=1.0)

    LeftHandThumb3Sz = DoubleField(default_value=1.0)


class LeftHandThumb4TPlugOperator(
    CompoundPlugOperator["LeftHandThumb4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb4Tx", "LeftHandThumb4Tx"),
        ("LeftHandThumb4Ty", "LeftHandThumb4Ty"),
        ("LeftHandThumb4Tz", "LeftHandThumb4Tz"),
    )

    LeftHandThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb4TAttrOperator(
    CompoundAttrOperator[LeftHandThumb4TPlugOperator]
):
    __slots__ = ()

    LeftHandThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb4TField(
    CompoundField[LeftHandThumb4TAttrOperator, LeftHandThumb4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb4TAttrOperator
    PLUG_CLS = LeftHandThumb4TPlugOperator

    LeftHandThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftHandThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftHandThumb4RPlugOperator(
    CompoundPlugOperator["LeftHandThumb4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb4Rx", "LeftHandThumb4Rx"),
        ("LeftHandThumb4Ry", "LeftHandThumb4Ry"),
        ("LeftHandThumb4Rz", "LeftHandThumb4Rz"),
    )

    LeftHandThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb4RAttrOperator(
    CompoundAttrOperator[LeftHandThumb4RPlugOperator]
):
    __slots__ = ()

    LeftHandThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb4RField(
    CompoundField[LeftHandThumb4RAttrOperator, LeftHandThumb4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb4RAttrOperator
    PLUG_CLS = LeftHandThumb4RPlugOperator

    LeftHandThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftHandThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftHandThumb4SPlugOperator(
    CompoundPlugOperator["LeftHandThumb4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandThumb4Sx", "LeftHandThumb4Sx"),
        ("LeftHandThumb4Sy", "LeftHandThumb4Sy"),
        ("LeftHandThumb4Sz", "LeftHandThumb4Sz"),
    )

    LeftHandThumb4Sx = DoubleField(default_value=1.0)

    LeftHandThumb4Sy = DoubleField(default_value=1.0)

    LeftHandThumb4Sz = DoubleField(default_value=1.0)


class LeftHandThumb4SAttrOperator(
    CompoundAttrOperator[LeftHandThumb4SPlugOperator]
):
    __slots__ = ()

    LeftHandThumb4Sx = DoubleField(default_value=1.0)

    LeftHandThumb4Sy = DoubleField(default_value=1.0)

    LeftHandThumb4Sz = DoubleField(default_value=1.0)


class LeftHandThumb4SField(
    CompoundField[LeftHandThumb4SAttrOperator, LeftHandThumb4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandThumb4SAttrOperator
    PLUG_CLS = LeftHandThumb4SPlugOperator

    LeftHandThumb4Sx = DoubleField(default_value=1.0)

    LeftHandThumb4Sy = DoubleField(default_value=1.0)

    LeftHandThumb4Sz = DoubleField(default_value=1.0)


class LeftHandIndex1TPlugOperator(
    CompoundPlugOperator["LeftHandIndex1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex1Tx", "LeftHandIndex1Tx"),
        ("LeftHandIndex1Ty", "LeftHandIndex1Ty"),
        ("LeftHandIndex1Tz", "LeftHandIndex1Tz"),
    )

    LeftHandIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex1TAttrOperator(
    CompoundAttrOperator[LeftHandIndex1TPlugOperator]
):
    __slots__ = ()

    LeftHandIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex1TField(
    CompoundField[LeftHandIndex1TAttrOperator, LeftHandIndex1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex1TAttrOperator
    PLUG_CLS = LeftHandIndex1TPlugOperator

    LeftHandIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex1RPlugOperator(
    CompoundPlugOperator["LeftHandIndex1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex1Rx", "LeftHandIndex1Rx"),
        ("LeftHandIndex1Ry", "LeftHandIndex1Ry"),
        ("LeftHandIndex1Rz", "LeftHandIndex1Rz"),
    )

    LeftHandIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex1RAttrOperator(
    CompoundAttrOperator[LeftHandIndex1RPlugOperator]
):
    __slots__ = ()

    LeftHandIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex1RField(
    CompoundField[LeftHandIndex1RAttrOperator, LeftHandIndex1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex1RAttrOperator
    PLUG_CLS = LeftHandIndex1RPlugOperator

    LeftHandIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex1SPlugOperator(
    CompoundPlugOperator["LeftHandIndex1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex1Sx", "LeftHandIndex1Sx"),
        ("LeftHandIndex1Sy", "LeftHandIndex1Sy"),
        ("LeftHandIndex1Sz", "LeftHandIndex1Sz"),
    )

    LeftHandIndex1Sx = DoubleField(default_value=1.0)

    LeftHandIndex1Sy = DoubleField(default_value=1.0)

    LeftHandIndex1Sz = DoubleField(default_value=1.0)


class LeftHandIndex1SAttrOperator(
    CompoundAttrOperator[LeftHandIndex1SPlugOperator]
):
    __slots__ = ()

    LeftHandIndex1Sx = DoubleField(default_value=1.0)

    LeftHandIndex1Sy = DoubleField(default_value=1.0)

    LeftHandIndex1Sz = DoubleField(default_value=1.0)


class LeftHandIndex1SField(
    CompoundField[LeftHandIndex1SAttrOperator, LeftHandIndex1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex1SAttrOperator
    PLUG_CLS = LeftHandIndex1SPlugOperator

    LeftHandIndex1Sx = DoubleField(default_value=1.0)

    LeftHandIndex1Sy = DoubleField(default_value=1.0)

    LeftHandIndex1Sz = DoubleField(default_value=1.0)


class LeftHandIndex2TPlugOperator(
    CompoundPlugOperator["LeftHandIndex2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex2Tx", "LeftHandIndex2Tx"),
        ("LeftHandIndex2Ty", "LeftHandIndex2Ty"),
        ("LeftHandIndex2Tz", "LeftHandIndex2Tz"),
    )

    LeftHandIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex2TAttrOperator(
    CompoundAttrOperator[LeftHandIndex2TPlugOperator]
):
    __slots__ = ()

    LeftHandIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex2TField(
    CompoundField[LeftHandIndex2TAttrOperator, LeftHandIndex2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex2TAttrOperator
    PLUG_CLS = LeftHandIndex2TPlugOperator

    LeftHandIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex2RPlugOperator(
    CompoundPlugOperator["LeftHandIndex2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex2Rx", "LeftHandIndex2Rx"),
        ("LeftHandIndex2Ry", "LeftHandIndex2Ry"),
        ("LeftHandIndex2Rz", "LeftHandIndex2Rz"),
    )

    LeftHandIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex2RAttrOperator(
    CompoundAttrOperator[LeftHandIndex2RPlugOperator]
):
    __slots__ = ()

    LeftHandIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex2RField(
    CompoundField[LeftHandIndex2RAttrOperator, LeftHandIndex2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex2RAttrOperator
    PLUG_CLS = LeftHandIndex2RPlugOperator

    LeftHandIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex2SPlugOperator(
    CompoundPlugOperator["LeftHandIndex2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex2Sx", "LeftHandIndex2Sx"),
        ("LeftHandIndex2Sy", "LeftHandIndex2Sy"),
        ("LeftHandIndex2Sz", "LeftHandIndex2Sz"),
    )

    LeftHandIndex2Sx = DoubleField(default_value=1.0)

    LeftHandIndex2Sy = DoubleField(default_value=1.0)

    LeftHandIndex2Sz = DoubleField(default_value=1.0)


class LeftHandIndex2SAttrOperator(
    CompoundAttrOperator[LeftHandIndex2SPlugOperator]
):
    __slots__ = ()

    LeftHandIndex2Sx = DoubleField(default_value=1.0)

    LeftHandIndex2Sy = DoubleField(default_value=1.0)

    LeftHandIndex2Sz = DoubleField(default_value=1.0)


class LeftHandIndex2SField(
    CompoundField[LeftHandIndex2SAttrOperator, LeftHandIndex2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex2SAttrOperator
    PLUG_CLS = LeftHandIndex2SPlugOperator

    LeftHandIndex2Sx = DoubleField(default_value=1.0)

    LeftHandIndex2Sy = DoubleField(default_value=1.0)

    LeftHandIndex2Sz = DoubleField(default_value=1.0)


class LeftHandIndex3TPlugOperator(
    CompoundPlugOperator["LeftHandIndex3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex3Tx", "LeftHandIndex3Tx"),
        ("LeftHandIndex3Ty", "LeftHandIndex3Ty"),
        ("LeftHandIndex3Tz", "LeftHandIndex3Tz"),
    )

    LeftHandIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex3TAttrOperator(
    CompoundAttrOperator[LeftHandIndex3TPlugOperator]
):
    __slots__ = ()

    LeftHandIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex3TField(
    CompoundField[LeftHandIndex3TAttrOperator, LeftHandIndex3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex3TAttrOperator
    PLUG_CLS = LeftHandIndex3TPlugOperator

    LeftHandIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex3RPlugOperator(
    CompoundPlugOperator["LeftHandIndex3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex3Rx", "LeftHandIndex3Rx"),
        ("LeftHandIndex3Ry", "LeftHandIndex3Ry"),
        ("LeftHandIndex3Rz", "LeftHandIndex3Rz"),
    )

    LeftHandIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex3RAttrOperator(
    CompoundAttrOperator[LeftHandIndex3RPlugOperator]
):
    __slots__ = ()

    LeftHandIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex3RField(
    CompoundField[LeftHandIndex3RAttrOperator, LeftHandIndex3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex3RAttrOperator
    PLUG_CLS = LeftHandIndex3RPlugOperator

    LeftHandIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex3SPlugOperator(
    CompoundPlugOperator["LeftHandIndex3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex3Sx", "LeftHandIndex3Sx"),
        ("LeftHandIndex3Sy", "LeftHandIndex3Sy"),
        ("LeftHandIndex3Sz", "LeftHandIndex3Sz"),
    )

    LeftHandIndex3Sx = DoubleField(default_value=1.0)

    LeftHandIndex3Sy = DoubleField(default_value=1.0)

    LeftHandIndex3Sz = DoubleField(default_value=1.0)


class LeftHandIndex3SAttrOperator(
    CompoundAttrOperator[LeftHandIndex3SPlugOperator]
):
    __slots__ = ()

    LeftHandIndex3Sx = DoubleField(default_value=1.0)

    LeftHandIndex3Sy = DoubleField(default_value=1.0)

    LeftHandIndex3Sz = DoubleField(default_value=1.0)


class LeftHandIndex3SField(
    CompoundField[LeftHandIndex3SAttrOperator, LeftHandIndex3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex3SAttrOperator
    PLUG_CLS = LeftHandIndex3SPlugOperator

    LeftHandIndex3Sx = DoubleField(default_value=1.0)

    LeftHandIndex3Sy = DoubleField(default_value=1.0)

    LeftHandIndex3Sz = DoubleField(default_value=1.0)


class LeftHandIndex4TPlugOperator(
    CompoundPlugOperator["LeftHandIndex4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex4Tx", "LeftHandIndex4Tx"),
        ("LeftHandIndex4Ty", "LeftHandIndex4Ty"),
        ("LeftHandIndex4Tz", "LeftHandIndex4Tz"),
    )

    LeftHandIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex4TAttrOperator(
    CompoundAttrOperator[LeftHandIndex4TPlugOperator]
):
    __slots__ = ()

    LeftHandIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex4TField(
    CompoundField[LeftHandIndex4TAttrOperator, LeftHandIndex4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex4TAttrOperator
    PLUG_CLS = LeftHandIndex4TPlugOperator

    LeftHandIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftHandIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftHandIndex4RPlugOperator(
    CompoundPlugOperator["LeftHandIndex4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex4Rx", "LeftHandIndex4Rx"),
        ("LeftHandIndex4Ry", "LeftHandIndex4Ry"),
        ("LeftHandIndex4Rz", "LeftHandIndex4Rz"),
    )

    LeftHandIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex4RAttrOperator(
    CompoundAttrOperator[LeftHandIndex4RPlugOperator]
):
    __slots__ = ()

    LeftHandIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex4RField(
    CompoundField[LeftHandIndex4RAttrOperator, LeftHandIndex4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex4RAttrOperator
    PLUG_CLS = LeftHandIndex4RPlugOperator

    LeftHandIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftHandIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftHandIndex4SPlugOperator(
    CompoundPlugOperator["LeftHandIndex4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandIndex4Sx", "LeftHandIndex4Sx"),
        ("LeftHandIndex4Sy", "LeftHandIndex4Sy"),
        ("LeftHandIndex4Sz", "LeftHandIndex4Sz"),
    )

    LeftHandIndex4Sx = DoubleField(default_value=1.0)

    LeftHandIndex4Sy = DoubleField(default_value=1.0)

    LeftHandIndex4Sz = DoubleField(default_value=1.0)


class LeftHandIndex4SAttrOperator(
    CompoundAttrOperator[LeftHandIndex4SPlugOperator]
):
    __slots__ = ()

    LeftHandIndex4Sx = DoubleField(default_value=1.0)

    LeftHandIndex4Sy = DoubleField(default_value=1.0)

    LeftHandIndex4Sz = DoubleField(default_value=1.0)


class LeftHandIndex4SField(
    CompoundField[LeftHandIndex4SAttrOperator, LeftHandIndex4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandIndex4SAttrOperator
    PLUG_CLS = LeftHandIndex4SPlugOperator

    LeftHandIndex4Sx = DoubleField(default_value=1.0)

    LeftHandIndex4Sy = DoubleField(default_value=1.0)

    LeftHandIndex4Sz = DoubleField(default_value=1.0)


class LeftHandMiddle1TPlugOperator(
    CompoundPlugOperator["LeftHandMiddle1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle1Tx", "LeftHandMiddle1Tx"),
        ("LeftHandMiddle1Ty", "LeftHandMiddle1Ty"),
        ("LeftHandMiddle1Tz", "LeftHandMiddle1Tz"),
    )

    LeftHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle1TAttrOperator(
    CompoundAttrOperator[LeftHandMiddle1TPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle1TField(
    CompoundField[LeftHandMiddle1TAttrOperator, LeftHandMiddle1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle1TAttrOperator
    PLUG_CLS = LeftHandMiddle1TPlugOperator

    LeftHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle1RPlugOperator(
    CompoundPlugOperator["LeftHandMiddle1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle1Rx", "LeftHandMiddle1Rx"),
        ("LeftHandMiddle1Ry", "LeftHandMiddle1Ry"),
        ("LeftHandMiddle1Rz", "LeftHandMiddle1Rz"),
    )

    LeftHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle1RAttrOperator(
    CompoundAttrOperator[LeftHandMiddle1RPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle1RField(
    CompoundField[LeftHandMiddle1RAttrOperator, LeftHandMiddle1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle1RAttrOperator
    PLUG_CLS = LeftHandMiddle1RPlugOperator

    LeftHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle1SPlugOperator(
    CompoundPlugOperator["LeftHandMiddle1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle1Sx", "LeftHandMiddle1Sx"),
        ("LeftHandMiddle1Sy", "LeftHandMiddle1Sy"),
        ("LeftHandMiddle1Sz", "LeftHandMiddle1Sz"),
    )

    LeftHandMiddle1Sx = DoubleField(default_value=1.0)

    LeftHandMiddle1Sy = DoubleField(default_value=1.0)

    LeftHandMiddle1Sz = DoubleField(default_value=1.0)


class LeftHandMiddle1SAttrOperator(
    CompoundAttrOperator[LeftHandMiddle1SPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle1Sx = DoubleField(default_value=1.0)

    LeftHandMiddle1Sy = DoubleField(default_value=1.0)

    LeftHandMiddle1Sz = DoubleField(default_value=1.0)


class LeftHandMiddle1SField(
    CompoundField[LeftHandMiddle1SAttrOperator, LeftHandMiddle1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle1SAttrOperator
    PLUG_CLS = LeftHandMiddle1SPlugOperator

    LeftHandMiddle1Sx = DoubleField(default_value=1.0)

    LeftHandMiddle1Sy = DoubleField(default_value=1.0)

    LeftHandMiddle1Sz = DoubleField(default_value=1.0)


class LeftHandMiddle2TPlugOperator(
    CompoundPlugOperator["LeftHandMiddle2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle2Tx", "LeftHandMiddle2Tx"),
        ("LeftHandMiddle2Ty", "LeftHandMiddle2Ty"),
        ("LeftHandMiddle2Tz", "LeftHandMiddle2Tz"),
    )

    LeftHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle2TAttrOperator(
    CompoundAttrOperator[LeftHandMiddle2TPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle2TField(
    CompoundField[LeftHandMiddle2TAttrOperator, LeftHandMiddle2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle2TAttrOperator
    PLUG_CLS = LeftHandMiddle2TPlugOperator

    LeftHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle2RPlugOperator(
    CompoundPlugOperator["LeftHandMiddle2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle2Rx", "LeftHandMiddle2Rx"),
        ("LeftHandMiddle2Ry", "LeftHandMiddle2Ry"),
        ("LeftHandMiddle2Rz", "LeftHandMiddle2Rz"),
    )

    LeftHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle2RAttrOperator(
    CompoundAttrOperator[LeftHandMiddle2RPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle2RField(
    CompoundField[LeftHandMiddle2RAttrOperator, LeftHandMiddle2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle2RAttrOperator
    PLUG_CLS = LeftHandMiddle2RPlugOperator

    LeftHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle2SPlugOperator(
    CompoundPlugOperator["LeftHandMiddle2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle2Sx", "LeftHandMiddle2Sx"),
        ("LeftHandMiddle2Sy", "LeftHandMiddle2Sy"),
        ("LeftHandMiddle2Sz", "LeftHandMiddle2Sz"),
    )

    LeftHandMiddle2Sx = DoubleField(default_value=1.0)

    LeftHandMiddle2Sy = DoubleField(default_value=1.0)

    LeftHandMiddle2Sz = DoubleField(default_value=1.0)


class LeftHandMiddle2SAttrOperator(
    CompoundAttrOperator[LeftHandMiddle2SPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle2Sx = DoubleField(default_value=1.0)

    LeftHandMiddle2Sy = DoubleField(default_value=1.0)

    LeftHandMiddle2Sz = DoubleField(default_value=1.0)


class LeftHandMiddle2SField(
    CompoundField[LeftHandMiddle2SAttrOperator, LeftHandMiddle2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle2SAttrOperator
    PLUG_CLS = LeftHandMiddle2SPlugOperator

    LeftHandMiddle2Sx = DoubleField(default_value=1.0)

    LeftHandMiddle2Sy = DoubleField(default_value=1.0)

    LeftHandMiddle2Sz = DoubleField(default_value=1.0)


class LeftHandMiddle3TPlugOperator(
    CompoundPlugOperator["LeftHandMiddle3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle3Tx", "LeftHandMiddle3Tx"),
        ("LeftHandMiddle3Ty", "LeftHandMiddle3Ty"),
        ("LeftHandMiddle3Tz", "LeftHandMiddle3Tz"),
    )

    LeftHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle3TAttrOperator(
    CompoundAttrOperator[LeftHandMiddle3TPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle3TField(
    CompoundField[LeftHandMiddle3TAttrOperator, LeftHandMiddle3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle3TAttrOperator
    PLUG_CLS = LeftHandMiddle3TPlugOperator

    LeftHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle3RPlugOperator(
    CompoundPlugOperator["LeftHandMiddle3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle3Rx", "LeftHandMiddle3Rx"),
        ("LeftHandMiddle3Ry", "LeftHandMiddle3Ry"),
        ("LeftHandMiddle3Rz", "LeftHandMiddle3Rz"),
    )

    LeftHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle3RAttrOperator(
    CompoundAttrOperator[LeftHandMiddle3RPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle3RField(
    CompoundField[LeftHandMiddle3RAttrOperator, LeftHandMiddle3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle3RAttrOperator
    PLUG_CLS = LeftHandMiddle3RPlugOperator

    LeftHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle3SPlugOperator(
    CompoundPlugOperator["LeftHandMiddle3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle3Sx", "LeftHandMiddle3Sx"),
        ("LeftHandMiddle3Sy", "LeftHandMiddle3Sy"),
        ("LeftHandMiddle3Sz", "LeftHandMiddle3Sz"),
    )

    LeftHandMiddle3Sx = DoubleField(default_value=1.0)

    LeftHandMiddle3Sy = DoubleField(default_value=1.0)

    LeftHandMiddle3Sz = DoubleField(default_value=1.0)


class LeftHandMiddle3SAttrOperator(
    CompoundAttrOperator[LeftHandMiddle3SPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle3Sx = DoubleField(default_value=1.0)

    LeftHandMiddle3Sy = DoubleField(default_value=1.0)

    LeftHandMiddle3Sz = DoubleField(default_value=1.0)


class LeftHandMiddle3SField(
    CompoundField[LeftHandMiddle3SAttrOperator, LeftHandMiddle3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle3SAttrOperator
    PLUG_CLS = LeftHandMiddle3SPlugOperator

    LeftHandMiddle3Sx = DoubleField(default_value=1.0)

    LeftHandMiddle3Sy = DoubleField(default_value=1.0)

    LeftHandMiddle3Sz = DoubleField(default_value=1.0)


class LeftHandMiddle4TPlugOperator(
    CompoundPlugOperator["LeftHandMiddle4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle4Tx", "LeftHandMiddle4Tx"),
        ("LeftHandMiddle4Ty", "LeftHandMiddle4Ty"),
        ("LeftHandMiddle4Tz", "LeftHandMiddle4Tz"),
    )

    LeftHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle4TAttrOperator(
    CompoundAttrOperator[LeftHandMiddle4TPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle4TField(
    CompoundField[LeftHandMiddle4TAttrOperator, LeftHandMiddle4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle4TAttrOperator
    PLUG_CLS = LeftHandMiddle4TPlugOperator

    LeftHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftHandMiddle4RPlugOperator(
    CompoundPlugOperator["LeftHandMiddle4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle4Rx", "LeftHandMiddle4Rx"),
        ("LeftHandMiddle4Ry", "LeftHandMiddle4Ry"),
        ("LeftHandMiddle4Rz", "LeftHandMiddle4Rz"),
    )

    LeftHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle4RAttrOperator(
    CompoundAttrOperator[LeftHandMiddle4RPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle4RField(
    CompoundField[LeftHandMiddle4RAttrOperator, LeftHandMiddle4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle4RAttrOperator
    PLUG_CLS = LeftHandMiddle4RPlugOperator

    LeftHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftHandMiddle4SPlugOperator(
    CompoundPlugOperator["LeftHandMiddle4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandMiddle4Sx", "LeftHandMiddle4Sx"),
        ("LeftHandMiddle4Sy", "LeftHandMiddle4Sy"),
        ("LeftHandMiddle4Sz", "LeftHandMiddle4Sz"),
    )

    LeftHandMiddle4Sx = DoubleField(default_value=1.0)

    LeftHandMiddle4Sy = DoubleField(default_value=1.0)

    LeftHandMiddle4Sz = DoubleField(default_value=1.0)


class LeftHandMiddle4SAttrOperator(
    CompoundAttrOperator[LeftHandMiddle4SPlugOperator]
):
    __slots__ = ()

    LeftHandMiddle4Sx = DoubleField(default_value=1.0)

    LeftHandMiddle4Sy = DoubleField(default_value=1.0)

    LeftHandMiddle4Sz = DoubleField(default_value=1.0)


class LeftHandMiddle4SField(
    CompoundField[LeftHandMiddle4SAttrOperator, LeftHandMiddle4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandMiddle4SAttrOperator
    PLUG_CLS = LeftHandMiddle4SPlugOperator

    LeftHandMiddle4Sx = DoubleField(default_value=1.0)

    LeftHandMiddle4Sy = DoubleField(default_value=1.0)

    LeftHandMiddle4Sz = DoubleField(default_value=1.0)


class LeftHandRing1TPlugOperator(
    CompoundPlugOperator["LeftHandRing1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing1Tx", "LeftHandRing1Tx"),
        ("LeftHandRing1Ty", "LeftHandRing1Ty"),
        ("LeftHandRing1Tz", "LeftHandRing1Tz"),
    )

    LeftHandRing1Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing1Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing1Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing1TAttrOperator(
    CompoundAttrOperator[LeftHandRing1TPlugOperator]
):
    __slots__ = ()

    LeftHandRing1Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing1Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing1Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing1TField(
    CompoundField[LeftHandRing1TAttrOperator, LeftHandRing1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing1TAttrOperator
    PLUG_CLS = LeftHandRing1TPlugOperator

    LeftHandRing1Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing1Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing1Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing1RPlugOperator(
    CompoundPlugOperator["LeftHandRing1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing1Rx", "LeftHandRing1Rx"),
        ("LeftHandRing1Ry", "LeftHandRing1Ry"),
        ("LeftHandRing1Rz", "LeftHandRing1Rz"),
    )

    LeftHandRing1Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing1Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing1Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing1RAttrOperator(
    CompoundAttrOperator[LeftHandRing1RPlugOperator]
):
    __slots__ = ()

    LeftHandRing1Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing1Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing1Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing1RField(
    CompoundField[LeftHandRing1RAttrOperator, LeftHandRing1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing1RAttrOperator
    PLUG_CLS = LeftHandRing1RPlugOperator

    LeftHandRing1Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing1Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing1Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing1SPlugOperator(
    CompoundPlugOperator["LeftHandRing1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing1Sx", "LeftHandRing1Sx"),
        ("LeftHandRing1Sy", "LeftHandRing1Sy"),
        ("LeftHandRing1Sz", "LeftHandRing1Sz"),
    )

    LeftHandRing1Sx = DoubleField(default_value=1.0)

    LeftHandRing1Sy = DoubleField(default_value=1.0)

    LeftHandRing1Sz = DoubleField(default_value=1.0)


class LeftHandRing1SAttrOperator(
    CompoundAttrOperator[LeftHandRing1SPlugOperator]
):
    __slots__ = ()

    LeftHandRing1Sx = DoubleField(default_value=1.0)

    LeftHandRing1Sy = DoubleField(default_value=1.0)

    LeftHandRing1Sz = DoubleField(default_value=1.0)


class LeftHandRing1SField(
    CompoundField[LeftHandRing1SAttrOperator, LeftHandRing1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing1SAttrOperator
    PLUG_CLS = LeftHandRing1SPlugOperator

    LeftHandRing1Sx = DoubleField(default_value=1.0)

    LeftHandRing1Sy = DoubleField(default_value=1.0)

    LeftHandRing1Sz = DoubleField(default_value=1.0)


class LeftHandRing2TPlugOperator(
    CompoundPlugOperator["LeftHandRing2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing2Tx", "LeftHandRing2Tx"),
        ("LeftHandRing2Ty", "LeftHandRing2Ty"),
        ("LeftHandRing2Tz", "LeftHandRing2Tz"),
    )

    LeftHandRing2Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing2Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing2Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing2TAttrOperator(
    CompoundAttrOperator[LeftHandRing2TPlugOperator]
):
    __slots__ = ()

    LeftHandRing2Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing2Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing2Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing2TField(
    CompoundField[LeftHandRing2TAttrOperator, LeftHandRing2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing2TAttrOperator
    PLUG_CLS = LeftHandRing2TPlugOperator

    LeftHandRing2Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing2Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing2Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing2RPlugOperator(
    CompoundPlugOperator["LeftHandRing2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing2Rx", "LeftHandRing2Rx"),
        ("LeftHandRing2Ry", "LeftHandRing2Ry"),
        ("LeftHandRing2Rz", "LeftHandRing2Rz"),
    )

    LeftHandRing2Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing2Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing2Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing2RAttrOperator(
    CompoundAttrOperator[LeftHandRing2RPlugOperator]
):
    __slots__ = ()

    LeftHandRing2Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing2Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing2Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing2RField(
    CompoundField[LeftHandRing2RAttrOperator, LeftHandRing2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing2RAttrOperator
    PLUG_CLS = LeftHandRing2RPlugOperator

    LeftHandRing2Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing2Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing2Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing2SPlugOperator(
    CompoundPlugOperator["LeftHandRing2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing2Sx", "LeftHandRing2Sx"),
        ("LeftHandRing2Sy", "LeftHandRing2Sy"),
        ("LeftHandRing2Sz", "LeftHandRing2Sz"),
    )

    LeftHandRing2Sx = DoubleField(default_value=1.0)

    LeftHandRing2Sy = DoubleField(default_value=1.0)

    LeftHandRing2Sz = DoubleField(default_value=1.0)


class LeftHandRing2SAttrOperator(
    CompoundAttrOperator[LeftHandRing2SPlugOperator]
):
    __slots__ = ()

    LeftHandRing2Sx = DoubleField(default_value=1.0)

    LeftHandRing2Sy = DoubleField(default_value=1.0)

    LeftHandRing2Sz = DoubleField(default_value=1.0)


class LeftHandRing2SField(
    CompoundField[LeftHandRing2SAttrOperator, LeftHandRing2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing2SAttrOperator
    PLUG_CLS = LeftHandRing2SPlugOperator

    LeftHandRing2Sx = DoubleField(default_value=1.0)

    LeftHandRing2Sy = DoubleField(default_value=1.0)

    LeftHandRing2Sz = DoubleField(default_value=1.0)


class LeftHandRing3TPlugOperator(
    CompoundPlugOperator["LeftHandRing3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing3Tx", "LeftHandRing3Tx"),
        ("LeftHandRing3Ty", "LeftHandRing3Ty"),
        ("LeftHandRing3Tz", "LeftHandRing3Tz"),
    )

    LeftHandRing3Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing3Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing3Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing3TAttrOperator(
    CompoundAttrOperator[LeftHandRing3TPlugOperator]
):
    __slots__ = ()

    LeftHandRing3Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing3Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing3Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing3TField(
    CompoundField[LeftHandRing3TAttrOperator, LeftHandRing3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing3TAttrOperator
    PLUG_CLS = LeftHandRing3TPlugOperator

    LeftHandRing3Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing3Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing3Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing3RPlugOperator(
    CompoundPlugOperator["LeftHandRing3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing3Rx", "LeftHandRing3Rx"),
        ("LeftHandRing3Ry", "LeftHandRing3Ry"),
        ("LeftHandRing3Rz", "LeftHandRing3Rz"),
    )

    LeftHandRing3Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing3Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing3Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing3RAttrOperator(
    CompoundAttrOperator[LeftHandRing3RPlugOperator]
):
    __slots__ = ()

    LeftHandRing3Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing3Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing3Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing3RField(
    CompoundField[LeftHandRing3RAttrOperator, LeftHandRing3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing3RAttrOperator
    PLUG_CLS = LeftHandRing3RPlugOperator

    LeftHandRing3Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing3Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing3Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing3SPlugOperator(
    CompoundPlugOperator["LeftHandRing3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing3Sx", "LeftHandRing3Sx"),
        ("LeftHandRing3Sy", "LeftHandRing3Sy"),
        ("LeftHandRing3Sz", "LeftHandRing3Sz"),
    )

    LeftHandRing3Sx = DoubleField(default_value=1.0)

    LeftHandRing3Sy = DoubleField(default_value=1.0)

    LeftHandRing3Sz = DoubleField(default_value=1.0)


class LeftHandRing3SAttrOperator(
    CompoundAttrOperator[LeftHandRing3SPlugOperator]
):
    __slots__ = ()

    LeftHandRing3Sx = DoubleField(default_value=1.0)

    LeftHandRing3Sy = DoubleField(default_value=1.0)

    LeftHandRing3Sz = DoubleField(default_value=1.0)


class LeftHandRing3SField(
    CompoundField[LeftHandRing3SAttrOperator, LeftHandRing3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing3SAttrOperator
    PLUG_CLS = LeftHandRing3SPlugOperator

    LeftHandRing3Sx = DoubleField(default_value=1.0)

    LeftHandRing3Sy = DoubleField(default_value=1.0)

    LeftHandRing3Sz = DoubleField(default_value=1.0)


class LeftHandRing4TPlugOperator(
    CompoundPlugOperator["LeftHandRing4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing4Tx", "LeftHandRing4Tx"),
        ("LeftHandRing4Ty", "LeftHandRing4Ty"),
        ("LeftHandRing4Tz", "LeftHandRing4Tz"),
    )

    LeftHandRing4Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing4Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing4Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing4TAttrOperator(
    CompoundAttrOperator[LeftHandRing4TPlugOperator]
):
    __slots__ = ()

    LeftHandRing4Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing4Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing4Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing4TField(
    CompoundField[LeftHandRing4TAttrOperator, LeftHandRing4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing4TAttrOperator
    PLUG_CLS = LeftHandRing4TPlugOperator

    LeftHandRing4Tx = DoubleLinearField(default_value=0.0)

    LeftHandRing4Ty = DoubleLinearField(default_value=0.0)

    LeftHandRing4Tz = DoubleLinearField(default_value=0.0)


class LeftHandRing4RPlugOperator(
    CompoundPlugOperator["LeftHandRing4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing4Rx", "LeftHandRing4Rx"),
        ("LeftHandRing4Ry", "LeftHandRing4Ry"),
        ("LeftHandRing4Rz", "LeftHandRing4Rz"),
    )

    LeftHandRing4Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing4Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing4Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing4RAttrOperator(
    CompoundAttrOperator[LeftHandRing4RPlugOperator]
):
    __slots__ = ()

    LeftHandRing4Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing4Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing4Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing4RField(
    CompoundField[LeftHandRing4RAttrOperator, LeftHandRing4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing4RAttrOperator
    PLUG_CLS = LeftHandRing4RPlugOperator

    LeftHandRing4Rx = DoubleAngleField(default_value=0.0)

    LeftHandRing4Ry = DoubleAngleField(default_value=0.0)

    LeftHandRing4Rz = DoubleAngleField(default_value=0.0)


class LeftHandRing4SPlugOperator(
    CompoundPlugOperator["LeftHandRing4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandRing4Sx", "LeftHandRing4Sx"),
        ("LeftHandRing4Sy", "LeftHandRing4Sy"),
        ("LeftHandRing4Sz", "LeftHandRing4Sz"),
    )

    LeftHandRing4Sx = DoubleField(default_value=1.0)

    LeftHandRing4Sy = DoubleField(default_value=1.0)

    LeftHandRing4Sz = DoubleField(default_value=1.0)


class LeftHandRing4SAttrOperator(
    CompoundAttrOperator[LeftHandRing4SPlugOperator]
):
    __slots__ = ()

    LeftHandRing4Sx = DoubleField(default_value=1.0)

    LeftHandRing4Sy = DoubleField(default_value=1.0)

    LeftHandRing4Sz = DoubleField(default_value=1.0)


class LeftHandRing4SField(
    CompoundField[LeftHandRing4SAttrOperator, LeftHandRing4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandRing4SAttrOperator
    PLUG_CLS = LeftHandRing4SPlugOperator

    LeftHandRing4Sx = DoubleField(default_value=1.0)

    LeftHandRing4Sy = DoubleField(default_value=1.0)

    LeftHandRing4Sz = DoubleField(default_value=1.0)


class LeftHandPinky1TPlugOperator(
    CompoundPlugOperator["LeftHandPinky1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky1Tx", "LeftHandPinky1Tx"),
        ("LeftHandPinky1Ty", "LeftHandPinky1Ty"),
        ("LeftHandPinky1Tz", "LeftHandPinky1Tz"),
    )

    LeftHandPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky1TAttrOperator(
    CompoundAttrOperator[LeftHandPinky1TPlugOperator]
):
    __slots__ = ()

    LeftHandPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky1TField(
    CompoundField[LeftHandPinky1TAttrOperator, LeftHandPinky1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky1TAttrOperator
    PLUG_CLS = LeftHandPinky1TPlugOperator

    LeftHandPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky1RPlugOperator(
    CompoundPlugOperator["LeftHandPinky1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky1Rx", "LeftHandPinky1Rx"),
        ("LeftHandPinky1Ry", "LeftHandPinky1Ry"),
        ("LeftHandPinky1Rz", "LeftHandPinky1Rz"),
    )

    LeftHandPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky1RAttrOperator(
    CompoundAttrOperator[LeftHandPinky1RPlugOperator]
):
    __slots__ = ()

    LeftHandPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky1RField(
    CompoundField[LeftHandPinky1RAttrOperator, LeftHandPinky1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky1RAttrOperator
    PLUG_CLS = LeftHandPinky1RPlugOperator

    LeftHandPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky1SPlugOperator(
    CompoundPlugOperator["LeftHandPinky1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky1Sx", "LeftHandPinky1Sx"),
        ("LeftHandPinky1Sy", "LeftHandPinky1Sy"),
        ("LeftHandPinky1Sz", "LeftHandPinky1Sz"),
    )

    LeftHandPinky1Sx = DoubleField(default_value=1.0)

    LeftHandPinky1Sy = DoubleField(default_value=1.0)

    LeftHandPinky1Sz = DoubleField(default_value=1.0)


class LeftHandPinky1SAttrOperator(
    CompoundAttrOperator[LeftHandPinky1SPlugOperator]
):
    __slots__ = ()

    LeftHandPinky1Sx = DoubleField(default_value=1.0)

    LeftHandPinky1Sy = DoubleField(default_value=1.0)

    LeftHandPinky1Sz = DoubleField(default_value=1.0)


class LeftHandPinky1SField(
    CompoundField[LeftHandPinky1SAttrOperator, LeftHandPinky1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky1SAttrOperator
    PLUG_CLS = LeftHandPinky1SPlugOperator

    LeftHandPinky1Sx = DoubleField(default_value=1.0)

    LeftHandPinky1Sy = DoubleField(default_value=1.0)

    LeftHandPinky1Sz = DoubleField(default_value=1.0)


class LeftHandPinky2TPlugOperator(
    CompoundPlugOperator["LeftHandPinky2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky2Tx", "LeftHandPinky2Tx"),
        ("LeftHandPinky2Ty", "LeftHandPinky2Ty"),
        ("LeftHandPinky2Tz", "LeftHandPinky2Tz"),
    )

    LeftHandPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky2TAttrOperator(
    CompoundAttrOperator[LeftHandPinky2TPlugOperator]
):
    __slots__ = ()

    LeftHandPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky2TField(
    CompoundField[LeftHandPinky2TAttrOperator, LeftHandPinky2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky2TAttrOperator
    PLUG_CLS = LeftHandPinky2TPlugOperator

    LeftHandPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky2RPlugOperator(
    CompoundPlugOperator["LeftHandPinky2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky2Rx", "LeftHandPinky2Rx"),
        ("LeftHandPinky2Ry", "LeftHandPinky2Ry"),
        ("LeftHandPinky2Rz", "LeftHandPinky2Rz"),
    )

    LeftHandPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky2RAttrOperator(
    CompoundAttrOperator[LeftHandPinky2RPlugOperator]
):
    __slots__ = ()

    LeftHandPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky2RField(
    CompoundField[LeftHandPinky2RAttrOperator, LeftHandPinky2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky2RAttrOperator
    PLUG_CLS = LeftHandPinky2RPlugOperator

    LeftHandPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky2SPlugOperator(
    CompoundPlugOperator["LeftHandPinky2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky2Sx", "LeftHandPinky2Sx"),
        ("LeftHandPinky2Sy", "LeftHandPinky2Sy"),
        ("LeftHandPinky2Sz", "LeftHandPinky2Sz"),
    )

    LeftHandPinky2Sx = DoubleField(default_value=1.0)

    LeftHandPinky2Sy = DoubleField(default_value=1.0)

    LeftHandPinky2Sz = DoubleField(default_value=1.0)


class LeftHandPinky2SAttrOperator(
    CompoundAttrOperator[LeftHandPinky2SPlugOperator]
):
    __slots__ = ()

    LeftHandPinky2Sx = DoubleField(default_value=1.0)

    LeftHandPinky2Sy = DoubleField(default_value=1.0)

    LeftHandPinky2Sz = DoubleField(default_value=1.0)


class LeftHandPinky2SField(
    CompoundField[LeftHandPinky2SAttrOperator, LeftHandPinky2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky2SAttrOperator
    PLUG_CLS = LeftHandPinky2SPlugOperator

    LeftHandPinky2Sx = DoubleField(default_value=1.0)

    LeftHandPinky2Sy = DoubleField(default_value=1.0)

    LeftHandPinky2Sz = DoubleField(default_value=1.0)


class LeftHandPinky3TPlugOperator(
    CompoundPlugOperator["LeftHandPinky3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky3Tx", "LeftHandPinky3Tx"),
        ("LeftHandPinky3Ty", "LeftHandPinky3Ty"),
        ("LeftHandPinky3Tz", "LeftHandPinky3Tz"),
    )

    LeftHandPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky3TAttrOperator(
    CompoundAttrOperator[LeftHandPinky3TPlugOperator]
):
    __slots__ = ()

    LeftHandPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky3TField(
    CompoundField[LeftHandPinky3TAttrOperator, LeftHandPinky3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky3TAttrOperator
    PLUG_CLS = LeftHandPinky3TPlugOperator

    LeftHandPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky3RPlugOperator(
    CompoundPlugOperator["LeftHandPinky3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky3Rx", "LeftHandPinky3Rx"),
        ("LeftHandPinky3Ry", "LeftHandPinky3Ry"),
        ("LeftHandPinky3Rz", "LeftHandPinky3Rz"),
    )

    LeftHandPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky3RAttrOperator(
    CompoundAttrOperator[LeftHandPinky3RPlugOperator]
):
    __slots__ = ()

    LeftHandPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky3RField(
    CompoundField[LeftHandPinky3RAttrOperator, LeftHandPinky3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky3RAttrOperator
    PLUG_CLS = LeftHandPinky3RPlugOperator

    LeftHandPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky3SPlugOperator(
    CompoundPlugOperator["LeftHandPinky3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky3Sx", "LeftHandPinky3Sx"),
        ("LeftHandPinky3Sy", "LeftHandPinky3Sy"),
        ("LeftHandPinky3Sz", "LeftHandPinky3Sz"),
    )

    LeftHandPinky3Sx = DoubleField(default_value=1.0)

    LeftHandPinky3Sy = DoubleField(default_value=1.0)

    LeftHandPinky3Sz = DoubleField(default_value=1.0)


class LeftHandPinky3SAttrOperator(
    CompoundAttrOperator[LeftHandPinky3SPlugOperator]
):
    __slots__ = ()

    LeftHandPinky3Sx = DoubleField(default_value=1.0)

    LeftHandPinky3Sy = DoubleField(default_value=1.0)

    LeftHandPinky3Sz = DoubleField(default_value=1.0)


class LeftHandPinky3SField(
    CompoundField[LeftHandPinky3SAttrOperator, LeftHandPinky3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky3SAttrOperator
    PLUG_CLS = LeftHandPinky3SPlugOperator

    LeftHandPinky3Sx = DoubleField(default_value=1.0)

    LeftHandPinky3Sy = DoubleField(default_value=1.0)

    LeftHandPinky3Sz = DoubleField(default_value=1.0)


class LeftHandPinky4TPlugOperator(
    CompoundPlugOperator["LeftHandPinky4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky4Tx", "LeftHandPinky4Tx"),
        ("LeftHandPinky4Ty", "LeftHandPinky4Ty"),
        ("LeftHandPinky4Tz", "LeftHandPinky4Tz"),
    )

    LeftHandPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky4TAttrOperator(
    CompoundAttrOperator[LeftHandPinky4TPlugOperator]
):
    __slots__ = ()

    LeftHandPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky4TField(
    CompoundField[LeftHandPinky4TAttrOperator, LeftHandPinky4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky4TAttrOperator
    PLUG_CLS = LeftHandPinky4TPlugOperator

    LeftHandPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftHandPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftHandPinky4RPlugOperator(
    CompoundPlugOperator["LeftHandPinky4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky4Rx", "LeftHandPinky4Rx"),
        ("LeftHandPinky4Ry", "LeftHandPinky4Ry"),
        ("LeftHandPinky4Rz", "LeftHandPinky4Rz"),
    )

    LeftHandPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky4RAttrOperator(
    CompoundAttrOperator[LeftHandPinky4RPlugOperator]
):
    __slots__ = ()

    LeftHandPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky4RField(
    CompoundField[LeftHandPinky4RAttrOperator, LeftHandPinky4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky4RAttrOperator
    PLUG_CLS = LeftHandPinky4RPlugOperator

    LeftHandPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftHandPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftHandPinky4SPlugOperator(
    CompoundPlugOperator["LeftHandPinky4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandPinky4Sx", "LeftHandPinky4Sx"),
        ("LeftHandPinky4Sy", "LeftHandPinky4Sy"),
        ("LeftHandPinky4Sz", "LeftHandPinky4Sz"),
    )

    LeftHandPinky4Sx = DoubleField(default_value=1.0)

    LeftHandPinky4Sy = DoubleField(default_value=1.0)

    LeftHandPinky4Sz = DoubleField(default_value=1.0)


class LeftHandPinky4SAttrOperator(
    CompoundAttrOperator[LeftHandPinky4SPlugOperator]
):
    __slots__ = ()

    LeftHandPinky4Sx = DoubleField(default_value=1.0)

    LeftHandPinky4Sy = DoubleField(default_value=1.0)

    LeftHandPinky4Sz = DoubleField(default_value=1.0)


class LeftHandPinky4SField(
    CompoundField[LeftHandPinky4SAttrOperator, LeftHandPinky4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandPinky4SAttrOperator
    PLUG_CLS = LeftHandPinky4SPlugOperator

    LeftHandPinky4Sx = DoubleField(default_value=1.0)

    LeftHandPinky4Sy = DoubleField(default_value=1.0)

    LeftHandPinky4Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger1TPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger1Tx", "LeftHandExtraFinger1Tx"),
        ("LeftHandExtraFinger1Ty", "LeftHandExtraFinger1Ty"),
        ("LeftHandExtraFinger1Tz", "LeftHandExtraFinger1Tz"),
    )

    LeftHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger1TAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger1TPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger1TField(
    CompoundField[LeftHandExtraFinger1TAttrOperator, LeftHandExtraFinger1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger1TAttrOperator
    PLUG_CLS = LeftHandExtraFinger1TPlugOperator

    LeftHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger1RPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger1Rx", "LeftHandExtraFinger1Rx"),
        ("LeftHandExtraFinger1Ry", "LeftHandExtraFinger1Ry"),
        ("LeftHandExtraFinger1Rz", "LeftHandExtraFinger1Rz"),
    )

    LeftHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger1RAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger1RPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger1RField(
    CompoundField[LeftHandExtraFinger1RAttrOperator, LeftHandExtraFinger1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger1RAttrOperator
    PLUG_CLS = LeftHandExtraFinger1RPlugOperator

    LeftHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger1SPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger1Sx", "LeftHandExtraFinger1Sx"),
        ("LeftHandExtraFinger1Sy", "LeftHandExtraFinger1Sy"),
        ("LeftHandExtraFinger1Sz", "LeftHandExtraFinger1Sz"),
    )

    LeftHandExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger1SAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger1SPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger1SField(
    CompoundField[LeftHandExtraFinger1SAttrOperator, LeftHandExtraFinger1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger1SAttrOperator
    PLUG_CLS = LeftHandExtraFinger1SPlugOperator

    LeftHandExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger2TPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger2Tx", "LeftHandExtraFinger2Tx"),
        ("LeftHandExtraFinger2Ty", "LeftHandExtraFinger2Ty"),
        ("LeftHandExtraFinger2Tz", "LeftHandExtraFinger2Tz"),
    )

    LeftHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger2TAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger2TPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger2TField(
    CompoundField[LeftHandExtraFinger2TAttrOperator, LeftHandExtraFinger2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger2TAttrOperator
    PLUG_CLS = LeftHandExtraFinger2TPlugOperator

    LeftHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger2RPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger2Rx", "LeftHandExtraFinger2Rx"),
        ("LeftHandExtraFinger2Ry", "LeftHandExtraFinger2Ry"),
        ("LeftHandExtraFinger2Rz", "LeftHandExtraFinger2Rz"),
    )

    LeftHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger2RAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger2RPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger2RField(
    CompoundField[LeftHandExtraFinger2RAttrOperator, LeftHandExtraFinger2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger2RAttrOperator
    PLUG_CLS = LeftHandExtraFinger2RPlugOperator

    LeftHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger2SPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger2Sx", "LeftHandExtraFinger2Sx"),
        ("LeftHandExtraFinger2Sy", "LeftHandExtraFinger2Sy"),
        ("LeftHandExtraFinger2Sz", "LeftHandExtraFinger2Sz"),
    )

    LeftHandExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger2SAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger2SPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger2SField(
    CompoundField[LeftHandExtraFinger2SAttrOperator, LeftHandExtraFinger2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger2SAttrOperator
    PLUG_CLS = LeftHandExtraFinger2SPlugOperator

    LeftHandExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger3TPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger3Tx", "LeftHandExtraFinger3Tx"),
        ("LeftHandExtraFinger3Ty", "LeftHandExtraFinger3Ty"),
        ("LeftHandExtraFinger3Tz", "LeftHandExtraFinger3Tz"),
    )

    LeftHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger3TAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger3TPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger3TField(
    CompoundField[LeftHandExtraFinger3TAttrOperator, LeftHandExtraFinger3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger3TAttrOperator
    PLUG_CLS = LeftHandExtraFinger3TPlugOperator

    LeftHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger3RPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger3Rx", "LeftHandExtraFinger3Rx"),
        ("LeftHandExtraFinger3Ry", "LeftHandExtraFinger3Ry"),
        ("LeftHandExtraFinger3Rz", "LeftHandExtraFinger3Rz"),
    )

    LeftHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger3RAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger3RPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger3RField(
    CompoundField[LeftHandExtraFinger3RAttrOperator, LeftHandExtraFinger3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger3RAttrOperator
    PLUG_CLS = LeftHandExtraFinger3RPlugOperator

    LeftHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger3SPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger3Sx", "LeftHandExtraFinger3Sx"),
        ("LeftHandExtraFinger3Sy", "LeftHandExtraFinger3Sy"),
        ("LeftHandExtraFinger3Sz", "LeftHandExtraFinger3Sz"),
    )

    LeftHandExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger3SAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger3SPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger3SField(
    CompoundField[LeftHandExtraFinger3SAttrOperator, LeftHandExtraFinger3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger3SAttrOperator
    PLUG_CLS = LeftHandExtraFinger3SPlugOperator

    LeftHandExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger4TPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger4Tx", "LeftHandExtraFinger4Tx"),
        ("LeftHandExtraFinger4Ty", "LeftHandExtraFinger4Ty"),
        ("LeftHandExtraFinger4Tz", "LeftHandExtraFinger4Tz"),
    )

    LeftHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger4TAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger4TPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger4TField(
    CompoundField[LeftHandExtraFinger4TAttrOperator, LeftHandExtraFinger4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger4TAttrOperator
    PLUG_CLS = LeftHandExtraFinger4TPlugOperator

    LeftHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftHandExtraFinger4RPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger4Rx", "LeftHandExtraFinger4Rx"),
        ("LeftHandExtraFinger4Ry", "LeftHandExtraFinger4Ry"),
        ("LeftHandExtraFinger4Rz", "LeftHandExtraFinger4Rz"),
    )

    LeftHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger4RAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger4RPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger4RField(
    CompoundField[LeftHandExtraFinger4RAttrOperator, LeftHandExtraFinger4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger4RAttrOperator
    PLUG_CLS = LeftHandExtraFinger4RPlugOperator

    LeftHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftHandExtraFinger4SPlugOperator(
    CompoundPlugOperator["LeftHandExtraFinger4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftHandExtraFinger4Sx", "LeftHandExtraFinger4Sx"),
        ("LeftHandExtraFinger4Sy", "LeftHandExtraFinger4Sy"),
        ("LeftHandExtraFinger4Sz", "LeftHandExtraFinger4Sz"),
    )

    LeftHandExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger4SAttrOperator(
    CompoundAttrOperator[LeftHandExtraFinger4SPlugOperator]
):
    __slots__ = ()

    LeftHandExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftHandExtraFinger4SField(
    CompoundField[LeftHandExtraFinger4SAttrOperator, LeftHandExtraFinger4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftHandExtraFinger4SAttrOperator
    PLUG_CLS = LeftHandExtraFinger4SPlugOperator

    LeftHandExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftHandExtraFinger4Sz = DoubleField(default_value=1.0)


class RightHandThumb1TPlugOperator(
    CompoundPlugOperator["RightHandThumb1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb1Tx", "RightHandThumb1Tx"),
        ("RightHandThumb1Ty", "RightHandThumb1Ty"),
        ("RightHandThumb1Tz", "RightHandThumb1Tz"),
    )

    RightHandThumb1Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb1Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb1Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb1TAttrOperator(
    CompoundAttrOperator[RightHandThumb1TPlugOperator]
):
    __slots__ = ()

    RightHandThumb1Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb1Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb1Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb1TField(
    CompoundField[RightHandThumb1TAttrOperator, RightHandThumb1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb1TAttrOperator
    PLUG_CLS = RightHandThumb1TPlugOperator

    RightHandThumb1Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb1Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb1Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb1RPlugOperator(
    CompoundPlugOperator["RightHandThumb1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb1Rx", "RightHandThumb1Rx"),
        ("RightHandThumb1Ry", "RightHandThumb1Ry"),
        ("RightHandThumb1Rz", "RightHandThumb1Rz"),
    )

    RightHandThumb1Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb1Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb1Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb1RAttrOperator(
    CompoundAttrOperator[RightHandThumb1RPlugOperator]
):
    __slots__ = ()

    RightHandThumb1Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb1Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb1Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb1RField(
    CompoundField[RightHandThumb1RAttrOperator, RightHandThumb1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb1RAttrOperator
    PLUG_CLS = RightHandThumb1RPlugOperator

    RightHandThumb1Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb1Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb1Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb1SPlugOperator(
    CompoundPlugOperator["RightHandThumb1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb1Sx", "RightHandThumb1Sx"),
        ("RightHandThumb1Sy", "RightHandThumb1Sy"),
        ("RightHandThumb1Sz", "RightHandThumb1Sz"),
    )

    RightHandThumb1Sx = DoubleField(default_value=1.0)

    RightHandThumb1Sy = DoubleField(default_value=1.0)

    RightHandThumb1Sz = DoubleField(default_value=1.0)


class RightHandThumb1SAttrOperator(
    CompoundAttrOperator[RightHandThumb1SPlugOperator]
):
    __slots__ = ()

    RightHandThumb1Sx = DoubleField(default_value=1.0)

    RightHandThumb1Sy = DoubleField(default_value=1.0)

    RightHandThumb1Sz = DoubleField(default_value=1.0)


class RightHandThumb1SField(
    CompoundField[RightHandThumb1SAttrOperator, RightHandThumb1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb1SAttrOperator
    PLUG_CLS = RightHandThumb1SPlugOperator

    RightHandThumb1Sx = DoubleField(default_value=1.0)

    RightHandThumb1Sy = DoubleField(default_value=1.0)

    RightHandThumb1Sz = DoubleField(default_value=1.0)


class RightHandThumb2TPlugOperator(
    CompoundPlugOperator["RightHandThumb2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb2Tx", "RightHandThumb2Tx"),
        ("RightHandThumb2Ty", "RightHandThumb2Ty"),
        ("RightHandThumb2Tz", "RightHandThumb2Tz"),
    )

    RightHandThumb2Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb2Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb2Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb2TAttrOperator(
    CompoundAttrOperator[RightHandThumb2TPlugOperator]
):
    __slots__ = ()

    RightHandThumb2Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb2Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb2Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb2TField(
    CompoundField[RightHandThumb2TAttrOperator, RightHandThumb2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb2TAttrOperator
    PLUG_CLS = RightHandThumb2TPlugOperator

    RightHandThumb2Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb2Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb2Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb2RPlugOperator(
    CompoundPlugOperator["RightHandThumb2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb2Rx", "RightHandThumb2Rx"),
        ("RightHandThumb2Ry", "RightHandThumb2Ry"),
        ("RightHandThumb2Rz", "RightHandThumb2Rz"),
    )

    RightHandThumb2Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb2Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb2Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb2RAttrOperator(
    CompoundAttrOperator[RightHandThumb2RPlugOperator]
):
    __slots__ = ()

    RightHandThumb2Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb2Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb2Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb2RField(
    CompoundField[RightHandThumb2RAttrOperator, RightHandThumb2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb2RAttrOperator
    PLUG_CLS = RightHandThumb2RPlugOperator

    RightHandThumb2Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb2Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb2Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb2SPlugOperator(
    CompoundPlugOperator["RightHandThumb2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb2Sx", "RightHandThumb2Sx"),
        ("RightHandThumb2Sy", "RightHandThumb2Sy"),
        ("RightHandThumb2Sz", "RightHandThumb2Sz"),
    )

    RightHandThumb2Sx = DoubleField(default_value=1.0)

    RightHandThumb2Sy = DoubleField(default_value=1.0)

    RightHandThumb2Sz = DoubleField(default_value=1.0)


class RightHandThumb2SAttrOperator(
    CompoundAttrOperator[RightHandThumb2SPlugOperator]
):
    __slots__ = ()

    RightHandThumb2Sx = DoubleField(default_value=1.0)

    RightHandThumb2Sy = DoubleField(default_value=1.0)

    RightHandThumb2Sz = DoubleField(default_value=1.0)


class RightHandThumb2SField(
    CompoundField[RightHandThumb2SAttrOperator, RightHandThumb2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb2SAttrOperator
    PLUG_CLS = RightHandThumb2SPlugOperator

    RightHandThumb2Sx = DoubleField(default_value=1.0)

    RightHandThumb2Sy = DoubleField(default_value=1.0)

    RightHandThumb2Sz = DoubleField(default_value=1.0)


class RightHandThumb3TPlugOperator(
    CompoundPlugOperator["RightHandThumb3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb3Tx", "RightHandThumb3Tx"),
        ("RightHandThumb3Ty", "RightHandThumb3Ty"),
        ("RightHandThumb3Tz", "RightHandThumb3Tz"),
    )

    RightHandThumb3Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb3Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb3Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb3TAttrOperator(
    CompoundAttrOperator[RightHandThumb3TPlugOperator]
):
    __slots__ = ()

    RightHandThumb3Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb3Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb3Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb3TField(
    CompoundField[RightHandThumb3TAttrOperator, RightHandThumb3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb3TAttrOperator
    PLUG_CLS = RightHandThumb3TPlugOperator

    RightHandThumb3Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb3Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb3Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb3RPlugOperator(
    CompoundPlugOperator["RightHandThumb3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb3Rx", "RightHandThumb3Rx"),
        ("RightHandThumb3Ry", "RightHandThumb3Ry"),
        ("RightHandThumb3Rz", "RightHandThumb3Rz"),
    )

    RightHandThumb3Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb3Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb3Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb3RAttrOperator(
    CompoundAttrOperator[RightHandThumb3RPlugOperator]
):
    __slots__ = ()

    RightHandThumb3Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb3Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb3Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb3RField(
    CompoundField[RightHandThumb3RAttrOperator, RightHandThumb3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb3RAttrOperator
    PLUG_CLS = RightHandThumb3RPlugOperator

    RightHandThumb3Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb3Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb3Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb3SPlugOperator(
    CompoundPlugOperator["RightHandThumb3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb3Sx", "RightHandThumb3Sx"),
        ("RightHandThumb3Sy", "RightHandThumb3Sy"),
        ("RightHandThumb3Sz", "RightHandThumb3Sz"),
    )

    RightHandThumb3Sx = DoubleField(default_value=1.0)

    RightHandThumb3Sy = DoubleField(default_value=1.0)

    RightHandThumb3Sz = DoubleField(default_value=1.0)


class RightHandThumb3SAttrOperator(
    CompoundAttrOperator[RightHandThumb3SPlugOperator]
):
    __slots__ = ()

    RightHandThumb3Sx = DoubleField(default_value=1.0)

    RightHandThumb3Sy = DoubleField(default_value=1.0)

    RightHandThumb3Sz = DoubleField(default_value=1.0)


class RightHandThumb3SField(
    CompoundField[RightHandThumb3SAttrOperator, RightHandThumb3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb3SAttrOperator
    PLUG_CLS = RightHandThumb3SPlugOperator

    RightHandThumb3Sx = DoubleField(default_value=1.0)

    RightHandThumb3Sy = DoubleField(default_value=1.0)

    RightHandThumb3Sz = DoubleField(default_value=1.0)


class RightHandThumb4TPlugOperator(
    CompoundPlugOperator["RightHandThumb4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb4Tx", "RightHandThumb4Tx"),
        ("RightHandThumb4Ty", "RightHandThumb4Ty"),
        ("RightHandThumb4Tz", "RightHandThumb4Tz"),
    )

    RightHandThumb4Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb4Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb4Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb4TAttrOperator(
    CompoundAttrOperator[RightHandThumb4TPlugOperator]
):
    __slots__ = ()

    RightHandThumb4Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb4Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb4Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb4TField(
    CompoundField[RightHandThumb4TAttrOperator, RightHandThumb4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb4TAttrOperator
    PLUG_CLS = RightHandThumb4TPlugOperator

    RightHandThumb4Tx = DoubleLinearField(default_value=0.0)

    RightHandThumb4Ty = DoubleLinearField(default_value=0.0)

    RightHandThumb4Tz = DoubleLinearField(default_value=0.0)


class RightHandThumb4RPlugOperator(
    CompoundPlugOperator["RightHandThumb4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb4Rx", "RightHandThumb4Rx"),
        ("RightHandThumb4Ry", "RightHandThumb4Ry"),
        ("RightHandThumb4Rz", "RightHandThumb4Rz"),
    )

    RightHandThumb4Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb4Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb4Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb4RAttrOperator(
    CompoundAttrOperator[RightHandThumb4RPlugOperator]
):
    __slots__ = ()

    RightHandThumb4Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb4Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb4Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb4RField(
    CompoundField[RightHandThumb4RAttrOperator, RightHandThumb4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb4RAttrOperator
    PLUG_CLS = RightHandThumb4RPlugOperator

    RightHandThumb4Rx = DoubleAngleField(default_value=0.0)

    RightHandThumb4Ry = DoubleAngleField(default_value=0.0)

    RightHandThumb4Rz = DoubleAngleField(default_value=0.0)


class RightHandThumb4SPlugOperator(
    CompoundPlugOperator["RightHandThumb4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandThumb4Sx", "RightHandThumb4Sx"),
        ("RightHandThumb4Sy", "RightHandThumb4Sy"),
        ("RightHandThumb4Sz", "RightHandThumb4Sz"),
    )

    RightHandThumb4Sx = DoubleField(default_value=1.0)

    RightHandThumb4Sy = DoubleField(default_value=1.0)

    RightHandThumb4Sz = DoubleField(default_value=1.0)


class RightHandThumb4SAttrOperator(
    CompoundAttrOperator[RightHandThumb4SPlugOperator]
):
    __slots__ = ()

    RightHandThumb4Sx = DoubleField(default_value=1.0)

    RightHandThumb4Sy = DoubleField(default_value=1.0)

    RightHandThumb4Sz = DoubleField(default_value=1.0)


class RightHandThumb4SField(
    CompoundField[RightHandThumb4SAttrOperator, RightHandThumb4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandThumb4SAttrOperator
    PLUG_CLS = RightHandThumb4SPlugOperator

    RightHandThumb4Sx = DoubleField(default_value=1.0)

    RightHandThumb4Sy = DoubleField(default_value=1.0)

    RightHandThumb4Sz = DoubleField(default_value=1.0)


class RightHandIndex1TPlugOperator(
    CompoundPlugOperator["RightHandIndex1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex1Tx", "RightHandIndex1Tx"),
        ("RightHandIndex1Ty", "RightHandIndex1Ty"),
        ("RightHandIndex1Tz", "RightHandIndex1Tz"),
    )

    RightHandIndex1Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex1Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex1Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex1TAttrOperator(
    CompoundAttrOperator[RightHandIndex1TPlugOperator]
):
    __slots__ = ()

    RightHandIndex1Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex1Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex1Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex1TField(
    CompoundField[RightHandIndex1TAttrOperator, RightHandIndex1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex1TAttrOperator
    PLUG_CLS = RightHandIndex1TPlugOperator

    RightHandIndex1Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex1Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex1Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex1RPlugOperator(
    CompoundPlugOperator["RightHandIndex1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex1Rx", "RightHandIndex1Rx"),
        ("RightHandIndex1Ry", "RightHandIndex1Ry"),
        ("RightHandIndex1Rz", "RightHandIndex1Rz"),
    )

    RightHandIndex1Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex1Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex1Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex1RAttrOperator(
    CompoundAttrOperator[RightHandIndex1RPlugOperator]
):
    __slots__ = ()

    RightHandIndex1Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex1Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex1Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex1RField(
    CompoundField[RightHandIndex1RAttrOperator, RightHandIndex1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex1RAttrOperator
    PLUG_CLS = RightHandIndex1RPlugOperator

    RightHandIndex1Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex1Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex1Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex1SPlugOperator(
    CompoundPlugOperator["RightHandIndex1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex1Sx", "RightHandIndex1Sx"),
        ("RightHandIndex1Sy", "RightHandIndex1Sy"),
        ("RightHandIndex1Sz", "RightHandIndex1Sz"),
    )

    RightHandIndex1Sx = DoubleField(default_value=1.0)

    RightHandIndex1Sy = DoubleField(default_value=1.0)

    RightHandIndex1Sz = DoubleField(default_value=1.0)


class RightHandIndex1SAttrOperator(
    CompoundAttrOperator[RightHandIndex1SPlugOperator]
):
    __slots__ = ()

    RightHandIndex1Sx = DoubleField(default_value=1.0)

    RightHandIndex1Sy = DoubleField(default_value=1.0)

    RightHandIndex1Sz = DoubleField(default_value=1.0)


class RightHandIndex1SField(
    CompoundField[RightHandIndex1SAttrOperator, RightHandIndex1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex1SAttrOperator
    PLUG_CLS = RightHandIndex1SPlugOperator

    RightHandIndex1Sx = DoubleField(default_value=1.0)

    RightHandIndex1Sy = DoubleField(default_value=1.0)

    RightHandIndex1Sz = DoubleField(default_value=1.0)


class RightHandIndex2TPlugOperator(
    CompoundPlugOperator["RightHandIndex2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex2Tx", "RightHandIndex2Tx"),
        ("RightHandIndex2Ty", "RightHandIndex2Ty"),
        ("RightHandIndex2Tz", "RightHandIndex2Tz"),
    )

    RightHandIndex2Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex2Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex2Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex2TAttrOperator(
    CompoundAttrOperator[RightHandIndex2TPlugOperator]
):
    __slots__ = ()

    RightHandIndex2Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex2Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex2Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex2TField(
    CompoundField[RightHandIndex2TAttrOperator, RightHandIndex2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex2TAttrOperator
    PLUG_CLS = RightHandIndex2TPlugOperator

    RightHandIndex2Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex2Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex2Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex2RPlugOperator(
    CompoundPlugOperator["RightHandIndex2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex2Rx", "RightHandIndex2Rx"),
        ("RightHandIndex2Ry", "RightHandIndex2Ry"),
        ("RightHandIndex2Rz", "RightHandIndex2Rz"),
    )

    RightHandIndex2Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex2Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex2Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex2RAttrOperator(
    CompoundAttrOperator[RightHandIndex2RPlugOperator]
):
    __slots__ = ()

    RightHandIndex2Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex2Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex2Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex2RField(
    CompoundField[RightHandIndex2RAttrOperator, RightHandIndex2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex2RAttrOperator
    PLUG_CLS = RightHandIndex2RPlugOperator

    RightHandIndex2Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex2Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex2Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex2SPlugOperator(
    CompoundPlugOperator["RightHandIndex2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex2Sx", "RightHandIndex2Sx"),
        ("RightHandIndex2Sy", "RightHandIndex2Sy"),
        ("RightHandIndex2Sz", "RightHandIndex2Sz"),
    )

    RightHandIndex2Sx = DoubleField(default_value=1.0)

    RightHandIndex2Sy = DoubleField(default_value=1.0)

    RightHandIndex2Sz = DoubleField(default_value=1.0)


class RightHandIndex2SAttrOperator(
    CompoundAttrOperator[RightHandIndex2SPlugOperator]
):
    __slots__ = ()

    RightHandIndex2Sx = DoubleField(default_value=1.0)

    RightHandIndex2Sy = DoubleField(default_value=1.0)

    RightHandIndex2Sz = DoubleField(default_value=1.0)


class RightHandIndex2SField(
    CompoundField[RightHandIndex2SAttrOperator, RightHandIndex2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex2SAttrOperator
    PLUG_CLS = RightHandIndex2SPlugOperator

    RightHandIndex2Sx = DoubleField(default_value=1.0)

    RightHandIndex2Sy = DoubleField(default_value=1.0)

    RightHandIndex2Sz = DoubleField(default_value=1.0)


class RightHandIndex3TPlugOperator(
    CompoundPlugOperator["RightHandIndex3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex3Tx", "RightHandIndex3Tx"),
        ("RightHandIndex3Ty", "RightHandIndex3Ty"),
        ("RightHandIndex3Tz", "RightHandIndex3Tz"),
    )

    RightHandIndex3Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex3Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex3Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex3TAttrOperator(
    CompoundAttrOperator[RightHandIndex3TPlugOperator]
):
    __slots__ = ()

    RightHandIndex3Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex3Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex3Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex3TField(
    CompoundField[RightHandIndex3TAttrOperator, RightHandIndex3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex3TAttrOperator
    PLUG_CLS = RightHandIndex3TPlugOperator

    RightHandIndex3Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex3Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex3Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex3RPlugOperator(
    CompoundPlugOperator["RightHandIndex3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex3Rx", "RightHandIndex3Rx"),
        ("RightHandIndex3Ry", "RightHandIndex3Ry"),
        ("RightHandIndex3Rz", "RightHandIndex3Rz"),
    )

    RightHandIndex3Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex3Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex3Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex3RAttrOperator(
    CompoundAttrOperator[RightHandIndex3RPlugOperator]
):
    __slots__ = ()

    RightHandIndex3Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex3Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex3Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex3RField(
    CompoundField[RightHandIndex3RAttrOperator, RightHandIndex3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex3RAttrOperator
    PLUG_CLS = RightHandIndex3RPlugOperator

    RightHandIndex3Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex3Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex3Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex3SPlugOperator(
    CompoundPlugOperator["RightHandIndex3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex3Sx", "RightHandIndex3Sx"),
        ("RightHandIndex3Sy", "RightHandIndex3Sy"),
        ("RightHandIndex3Sz", "RightHandIndex3Sz"),
    )

    RightHandIndex3Sx = DoubleField(default_value=1.0)

    RightHandIndex3Sy = DoubleField(default_value=1.0)

    RightHandIndex3Sz = DoubleField(default_value=1.0)


class RightHandIndex3SAttrOperator(
    CompoundAttrOperator[RightHandIndex3SPlugOperator]
):
    __slots__ = ()

    RightHandIndex3Sx = DoubleField(default_value=1.0)

    RightHandIndex3Sy = DoubleField(default_value=1.0)

    RightHandIndex3Sz = DoubleField(default_value=1.0)


class RightHandIndex3SField(
    CompoundField[RightHandIndex3SAttrOperator, RightHandIndex3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex3SAttrOperator
    PLUG_CLS = RightHandIndex3SPlugOperator

    RightHandIndex3Sx = DoubleField(default_value=1.0)

    RightHandIndex3Sy = DoubleField(default_value=1.0)

    RightHandIndex3Sz = DoubleField(default_value=1.0)


class RightHandIndex4TPlugOperator(
    CompoundPlugOperator["RightHandIndex4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex4Tx", "RightHandIndex4Tx"),
        ("RightHandIndex4Ty", "RightHandIndex4Ty"),
        ("RightHandIndex4Tz", "RightHandIndex4Tz"),
    )

    RightHandIndex4Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex4Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex4Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex4TAttrOperator(
    CompoundAttrOperator[RightHandIndex4TPlugOperator]
):
    __slots__ = ()

    RightHandIndex4Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex4Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex4Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex4TField(
    CompoundField[RightHandIndex4TAttrOperator, RightHandIndex4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex4TAttrOperator
    PLUG_CLS = RightHandIndex4TPlugOperator

    RightHandIndex4Tx = DoubleLinearField(default_value=0.0)

    RightHandIndex4Ty = DoubleLinearField(default_value=0.0)

    RightHandIndex4Tz = DoubleLinearField(default_value=0.0)


class RightHandIndex4RPlugOperator(
    CompoundPlugOperator["RightHandIndex4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex4Rx", "RightHandIndex4Rx"),
        ("RightHandIndex4Ry", "RightHandIndex4Ry"),
        ("RightHandIndex4Rz", "RightHandIndex4Rz"),
    )

    RightHandIndex4Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex4Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex4Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex4RAttrOperator(
    CompoundAttrOperator[RightHandIndex4RPlugOperator]
):
    __slots__ = ()

    RightHandIndex4Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex4Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex4Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex4RField(
    CompoundField[RightHandIndex4RAttrOperator, RightHandIndex4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex4RAttrOperator
    PLUG_CLS = RightHandIndex4RPlugOperator

    RightHandIndex4Rx = DoubleAngleField(default_value=0.0)

    RightHandIndex4Ry = DoubleAngleField(default_value=0.0)

    RightHandIndex4Rz = DoubleAngleField(default_value=0.0)


class RightHandIndex4SPlugOperator(
    CompoundPlugOperator["RightHandIndex4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandIndex4Sx", "RightHandIndex4Sx"),
        ("RightHandIndex4Sy", "RightHandIndex4Sy"),
        ("RightHandIndex4Sz", "RightHandIndex4Sz"),
    )

    RightHandIndex4Sx = DoubleField(default_value=1.0)

    RightHandIndex4Sy = DoubleField(default_value=1.0)

    RightHandIndex4Sz = DoubleField(default_value=1.0)


class RightHandIndex4SAttrOperator(
    CompoundAttrOperator[RightHandIndex4SPlugOperator]
):
    __slots__ = ()

    RightHandIndex4Sx = DoubleField(default_value=1.0)

    RightHandIndex4Sy = DoubleField(default_value=1.0)

    RightHandIndex4Sz = DoubleField(default_value=1.0)


class RightHandIndex4SField(
    CompoundField[RightHandIndex4SAttrOperator, RightHandIndex4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandIndex4SAttrOperator
    PLUG_CLS = RightHandIndex4SPlugOperator

    RightHandIndex4Sx = DoubleField(default_value=1.0)

    RightHandIndex4Sy = DoubleField(default_value=1.0)

    RightHandIndex4Sz = DoubleField(default_value=1.0)


class RightHandMiddle1TPlugOperator(
    CompoundPlugOperator["RightHandMiddle1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle1Tx", "RightHandMiddle1Tx"),
        ("RightHandMiddle1Ty", "RightHandMiddle1Ty"),
        ("RightHandMiddle1Tz", "RightHandMiddle1Tz"),
    )

    RightHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle1TAttrOperator(
    CompoundAttrOperator[RightHandMiddle1TPlugOperator]
):
    __slots__ = ()

    RightHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle1TField(
    CompoundField[RightHandMiddle1TAttrOperator, RightHandMiddle1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle1TAttrOperator
    PLUG_CLS = RightHandMiddle1TPlugOperator

    RightHandMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle1RPlugOperator(
    CompoundPlugOperator["RightHandMiddle1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle1Rx", "RightHandMiddle1Rx"),
        ("RightHandMiddle1Ry", "RightHandMiddle1Ry"),
        ("RightHandMiddle1Rz", "RightHandMiddle1Rz"),
    )

    RightHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle1RAttrOperator(
    CompoundAttrOperator[RightHandMiddle1RPlugOperator]
):
    __slots__ = ()

    RightHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle1RField(
    CompoundField[RightHandMiddle1RAttrOperator, RightHandMiddle1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle1RAttrOperator
    PLUG_CLS = RightHandMiddle1RPlugOperator

    RightHandMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle1SPlugOperator(
    CompoundPlugOperator["RightHandMiddle1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle1Sx", "RightHandMiddle1Sx"),
        ("RightHandMiddle1Sy", "RightHandMiddle1Sy"),
        ("RightHandMiddle1Sz", "RightHandMiddle1Sz"),
    )

    RightHandMiddle1Sx = DoubleField(default_value=1.0)

    RightHandMiddle1Sy = DoubleField(default_value=1.0)

    RightHandMiddle1Sz = DoubleField(default_value=1.0)


class RightHandMiddle1SAttrOperator(
    CompoundAttrOperator[RightHandMiddle1SPlugOperator]
):
    __slots__ = ()

    RightHandMiddle1Sx = DoubleField(default_value=1.0)

    RightHandMiddle1Sy = DoubleField(default_value=1.0)

    RightHandMiddle1Sz = DoubleField(default_value=1.0)


class RightHandMiddle1SField(
    CompoundField[RightHandMiddle1SAttrOperator, RightHandMiddle1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle1SAttrOperator
    PLUG_CLS = RightHandMiddle1SPlugOperator

    RightHandMiddle1Sx = DoubleField(default_value=1.0)

    RightHandMiddle1Sy = DoubleField(default_value=1.0)

    RightHandMiddle1Sz = DoubleField(default_value=1.0)


class RightHandMiddle2TPlugOperator(
    CompoundPlugOperator["RightHandMiddle2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle2Tx", "RightHandMiddle2Tx"),
        ("RightHandMiddle2Ty", "RightHandMiddle2Ty"),
        ("RightHandMiddle2Tz", "RightHandMiddle2Tz"),
    )

    RightHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle2TAttrOperator(
    CompoundAttrOperator[RightHandMiddle2TPlugOperator]
):
    __slots__ = ()

    RightHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle2TField(
    CompoundField[RightHandMiddle2TAttrOperator, RightHandMiddle2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle2TAttrOperator
    PLUG_CLS = RightHandMiddle2TPlugOperator

    RightHandMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle2RPlugOperator(
    CompoundPlugOperator["RightHandMiddle2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle2Rx", "RightHandMiddle2Rx"),
        ("RightHandMiddle2Ry", "RightHandMiddle2Ry"),
        ("RightHandMiddle2Rz", "RightHandMiddle2Rz"),
    )

    RightHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle2RAttrOperator(
    CompoundAttrOperator[RightHandMiddle2RPlugOperator]
):
    __slots__ = ()

    RightHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle2RField(
    CompoundField[RightHandMiddle2RAttrOperator, RightHandMiddle2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle2RAttrOperator
    PLUG_CLS = RightHandMiddle2RPlugOperator

    RightHandMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle2SPlugOperator(
    CompoundPlugOperator["RightHandMiddle2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle2Sx", "RightHandMiddle2Sx"),
        ("RightHandMiddle2Sy", "RightHandMiddle2Sy"),
        ("RightHandMiddle2Sz", "RightHandMiddle2Sz"),
    )

    RightHandMiddle2Sx = DoubleField(default_value=1.0)

    RightHandMiddle2Sy = DoubleField(default_value=1.0)

    RightHandMiddle2Sz = DoubleField(default_value=1.0)


class RightHandMiddle2SAttrOperator(
    CompoundAttrOperator[RightHandMiddle2SPlugOperator]
):
    __slots__ = ()

    RightHandMiddle2Sx = DoubleField(default_value=1.0)

    RightHandMiddle2Sy = DoubleField(default_value=1.0)

    RightHandMiddle2Sz = DoubleField(default_value=1.0)


class RightHandMiddle2SField(
    CompoundField[RightHandMiddle2SAttrOperator, RightHandMiddle2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle2SAttrOperator
    PLUG_CLS = RightHandMiddle2SPlugOperator

    RightHandMiddle2Sx = DoubleField(default_value=1.0)

    RightHandMiddle2Sy = DoubleField(default_value=1.0)

    RightHandMiddle2Sz = DoubleField(default_value=1.0)


class RightHandMiddle3TPlugOperator(
    CompoundPlugOperator["RightHandMiddle3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle3Tx", "RightHandMiddle3Tx"),
        ("RightHandMiddle3Ty", "RightHandMiddle3Ty"),
        ("RightHandMiddle3Tz", "RightHandMiddle3Tz"),
    )

    RightHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle3TAttrOperator(
    CompoundAttrOperator[RightHandMiddle3TPlugOperator]
):
    __slots__ = ()

    RightHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle3TField(
    CompoundField[RightHandMiddle3TAttrOperator, RightHandMiddle3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle3TAttrOperator
    PLUG_CLS = RightHandMiddle3TPlugOperator

    RightHandMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle3RPlugOperator(
    CompoundPlugOperator["RightHandMiddle3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle3Rx", "RightHandMiddle3Rx"),
        ("RightHandMiddle3Ry", "RightHandMiddle3Ry"),
        ("RightHandMiddle3Rz", "RightHandMiddle3Rz"),
    )

    RightHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle3RAttrOperator(
    CompoundAttrOperator[RightHandMiddle3RPlugOperator]
):
    __slots__ = ()

    RightHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle3RField(
    CompoundField[RightHandMiddle3RAttrOperator, RightHandMiddle3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle3RAttrOperator
    PLUG_CLS = RightHandMiddle3RPlugOperator

    RightHandMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle3SPlugOperator(
    CompoundPlugOperator["RightHandMiddle3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle3Sx", "RightHandMiddle3Sx"),
        ("RightHandMiddle3Sy", "RightHandMiddle3Sy"),
        ("RightHandMiddle3Sz", "RightHandMiddle3Sz"),
    )

    RightHandMiddle3Sx = DoubleField(default_value=1.0)

    RightHandMiddle3Sy = DoubleField(default_value=1.0)

    RightHandMiddle3Sz = DoubleField(default_value=1.0)


class RightHandMiddle3SAttrOperator(
    CompoundAttrOperator[RightHandMiddle3SPlugOperator]
):
    __slots__ = ()

    RightHandMiddle3Sx = DoubleField(default_value=1.0)

    RightHandMiddle3Sy = DoubleField(default_value=1.0)

    RightHandMiddle3Sz = DoubleField(default_value=1.0)


class RightHandMiddle3SField(
    CompoundField[RightHandMiddle3SAttrOperator, RightHandMiddle3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle3SAttrOperator
    PLUG_CLS = RightHandMiddle3SPlugOperator

    RightHandMiddle3Sx = DoubleField(default_value=1.0)

    RightHandMiddle3Sy = DoubleField(default_value=1.0)

    RightHandMiddle3Sz = DoubleField(default_value=1.0)


class RightHandMiddle4TPlugOperator(
    CompoundPlugOperator["RightHandMiddle4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle4Tx", "RightHandMiddle4Tx"),
        ("RightHandMiddle4Ty", "RightHandMiddle4Ty"),
        ("RightHandMiddle4Tz", "RightHandMiddle4Tz"),
    )

    RightHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle4TAttrOperator(
    CompoundAttrOperator[RightHandMiddle4TPlugOperator]
):
    __slots__ = ()

    RightHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle4TField(
    CompoundField[RightHandMiddle4TAttrOperator, RightHandMiddle4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle4TAttrOperator
    PLUG_CLS = RightHandMiddle4TPlugOperator

    RightHandMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightHandMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightHandMiddle4RPlugOperator(
    CompoundPlugOperator["RightHandMiddle4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle4Rx", "RightHandMiddle4Rx"),
        ("RightHandMiddle4Ry", "RightHandMiddle4Ry"),
        ("RightHandMiddle4Rz", "RightHandMiddle4Rz"),
    )

    RightHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle4RAttrOperator(
    CompoundAttrOperator[RightHandMiddle4RPlugOperator]
):
    __slots__ = ()

    RightHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle4RField(
    CompoundField[RightHandMiddle4RAttrOperator, RightHandMiddle4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle4RAttrOperator
    PLUG_CLS = RightHandMiddle4RPlugOperator

    RightHandMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightHandMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightHandMiddle4SPlugOperator(
    CompoundPlugOperator["RightHandMiddle4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandMiddle4Sx", "RightHandMiddle4Sx"),
        ("RightHandMiddle4Sy", "RightHandMiddle4Sy"),
        ("RightHandMiddle4Sz", "RightHandMiddle4Sz"),
    )

    RightHandMiddle4Sx = DoubleField(default_value=1.0)

    RightHandMiddle4Sy = DoubleField(default_value=1.0)

    RightHandMiddle4Sz = DoubleField(default_value=1.0)


class RightHandMiddle4SAttrOperator(
    CompoundAttrOperator[RightHandMiddle4SPlugOperator]
):
    __slots__ = ()

    RightHandMiddle4Sx = DoubleField(default_value=1.0)

    RightHandMiddle4Sy = DoubleField(default_value=1.0)

    RightHandMiddle4Sz = DoubleField(default_value=1.0)


class RightHandMiddle4SField(
    CompoundField[RightHandMiddle4SAttrOperator, RightHandMiddle4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandMiddle4SAttrOperator
    PLUG_CLS = RightHandMiddle4SPlugOperator

    RightHandMiddle4Sx = DoubleField(default_value=1.0)

    RightHandMiddle4Sy = DoubleField(default_value=1.0)

    RightHandMiddle4Sz = DoubleField(default_value=1.0)


class RightHandRing1TPlugOperator(
    CompoundPlugOperator["RightHandRing1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing1Tx", "RightHandRing1Tx"),
        ("RightHandRing1Ty", "RightHandRing1Ty"),
        ("RightHandRing1Tz", "RightHandRing1Tz"),
    )

    RightHandRing1Tx = DoubleLinearField(default_value=0.0)

    RightHandRing1Ty = DoubleLinearField(default_value=0.0)

    RightHandRing1Tz = DoubleLinearField(default_value=0.0)


class RightHandRing1TAttrOperator(
    CompoundAttrOperator[RightHandRing1TPlugOperator]
):
    __slots__ = ()

    RightHandRing1Tx = DoubleLinearField(default_value=0.0)

    RightHandRing1Ty = DoubleLinearField(default_value=0.0)

    RightHandRing1Tz = DoubleLinearField(default_value=0.0)


class RightHandRing1TField(
    CompoundField[RightHandRing1TAttrOperator, RightHandRing1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing1TAttrOperator
    PLUG_CLS = RightHandRing1TPlugOperator

    RightHandRing1Tx = DoubleLinearField(default_value=0.0)

    RightHandRing1Ty = DoubleLinearField(default_value=0.0)

    RightHandRing1Tz = DoubleLinearField(default_value=0.0)


class RightHandRing1RPlugOperator(
    CompoundPlugOperator["RightHandRing1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing1Rx", "RightHandRing1Rx"),
        ("RightHandRing1Ry", "RightHandRing1Ry"),
        ("RightHandRing1Rz", "RightHandRing1Rz"),
    )

    RightHandRing1Rx = DoubleAngleField(default_value=0.0)

    RightHandRing1Ry = DoubleAngleField(default_value=0.0)

    RightHandRing1Rz = DoubleAngleField(default_value=0.0)


class RightHandRing1RAttrOperator(
    CompoundAttrOperator[RightHandRing1RPlugOperator]
):
    __slots__ = ()

    RightHandRing1Rx = DoubleAngleField(default_value=0.0)

    RightHandRing1Ry = DoubleAngleField(default_value=0.0)

    RightHandRing1Rz = DoubleAngleField(default_value=0.0)


class RightHandRing1RField(
    CompoundField[RightHandRing1RAttrOperator, RightHandRing1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing1RAttrOperator
    PLUG_CLS = RightHandRing1RPlugOperator

    RightHandRing1Rx = DoubleAngleField(default_value=0.0)

    RightHandRing1Ry = DoubleAngleField(default_value=0.0)

    RightHandRing1Rz = DoubleAngleField(default_value=0.0)


class RightHandRing1SPlugOperator(
    CompoundPlugOperator["RightHandRing1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing1Sx", "RightHandRing1Sx"),
        ("RightHandRing1Sy", "RightHandRing1Sy"),
        ("RightHandRing1Sz", "RightHandRing1Sz"),
    )

    RightHandRing1Sx = DoubleField(default_value=1.0)

    RightHandRing1Sy = DoubleField(default_value=1.0)

    RightHandRing1Sz = DoubleField(default_value=1.0)


class RightHandRing1SAttrOperator(
    CompoundAttrOperator[RightHandRing1SPlugOperator]
):
    __slots__ = ()

    RightHandRing1Sx = DoubleField(default_value=1.0)

    RightHandRing1Sy = DoubleField(default_value=1.0)

    RightHandRing1Sz = DoubleField(default_value=1.0)


class RightHandRing1SField(
    CompoundField[RightHandRing1SAttrOperator, RightHandRing1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing1SAttrOperator
    PLUG_CLS = RightHandRing1SPlugOperator

    RightHandRing1Sx = DoubleField(default_value=1.0)

    RightHandRing1Sy = DoubleField(default_value=1.0)

    RightHandRing1Sz = DoubleField(default_value=1.0)


class RightHandRing2TPlugOperator(
    CompoundPlugOperator["RightHandRing2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing2Tx", "RightHandRing2Tx"),
        ("RightHandRing2Ty", "RightHandRing2Ty"),
        ("RightHandRing2Tz", "RightHandRing2Tz"),
    )

    RightHandRing2Tx = DoubleLinearField(default_value=0.0)

    RightHandRing2Ty = DoubleLinearField(default_value=0.0)

    RightHandRing2Tz = DoubleLinearField(default_value=0.0)


class RightHandRing2TAttrOperator(
    CompoundAttrOperator[RightHandRing2TPlugOperator]
):
    __slots__ = ()

    RightHandRing2Tx = DoubleLinearField(default_value=0.0)

    RightHandRing2Ty = DoubleLinearField(default_value=0.0)

    RightHandRing2Tz = DoubleLinearField(default_value=0.0)


class RightHandRing2TField(
    CompoundField[RightHandRing2TAttrOperator, RightHandRing2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing2TAttrOperator
    PLUG_CLS = RightHandRing2TPlugOperator

    RightHandRing2Tx = DoubleLinearField(default_value=0.0)

    RightHandRing2Ty = DoubleLinearField(default_value=0.0)

    RightHandRing2Tz = DoubleLinearField(default_value=0.0)


class RightHandRing2RPlugOperator(
    CompoundPlugOperator["RightHandRing2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing2Rx", "RightHandRing2Rx"),
        ("RightHandRing2Ry", "RightHandRing2Ry"),
        ("RightHandRing2Rz", "RightHandRing2Rz"),
    )

    RightHandRing2Rx = DoubleAngleField(default_value=0.0)

    RightHandRing2Ry = DoubleAngleField(default_value=0.0)

    RightHandRing2Rz = DoubleAngleField(default_value=0.0)


class RightHandRing2RAttrOperator(
    CompoundAttrOperator[RightHandRing2RPlugOperator]
):
    __slots__ = ()

    RightHandRing2Rx = DoubleAngleField(default_value=0.0)

    RightHandRing2Ry = DoubleAngleField(default_value=0.0)

    RightHandRing2Rz = DoubleAngleField(default_value=0.0)


class RightHandRing2RField(
    CompoundField[RightHandRing2RAttrOperator, RightHandRing2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing2RAttrOperator
    PLUG_CLS = RightHandRing2RPlugOperator

    RightHandRing2Rx = DoubleAngleField(default_value=0.0)

    RightHandRing2Ry = DoubleAngleField(default_value=0.0)

    RightHandRing2Rz = DoubleAngleField(default_value=0.0)


class RightHandRing2SPlugOperator(
    CompoundPlugOperator["RightHandRing2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing2Sx", "RightHandRing2Sx"),
        ("RightHandRing2Sy", "RightHandRing2Sy"),
        ("RightHandRing2Sz", "RightHandRing2Sz"),
    )

    RightHandRing2Sx = DoubleField(default_value=1.0)

    RightHandRing2Sy = DoubleField(default_value=1.0)

    RightHandRing2Sz = DoubleField(default_value=1.0)


class RightHandRing2SAttrOperator(
    CompoundAttrOperator[RightHandRing2SPlugOperator]
):
    __slots__ = ()

    RightHandRing2Sx = DoubleField(default_value=1.0)

    RightHandRing2Sy = DoubleField(default_value=1.0)

    RightHandRing2Sz = DoubleField(default_value=1.0)


class RightHandRing2SField(
    CompoundField[RightHandRing2SAttrOperator, RightHandRing2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing2SAttrOperator
    PLUG_CLS = RightHandRing2SPlugOperator

    RightHandRing2Sx = DoubleField(default_value=1.0)

    RightHandRing2Sy = DoubleField(default_value=1.0)

    RightHandRing2Sz = DoubleField(default_value=1.0)


class RightHandRing3TPlugOperator(
    CompoundPlugOperator["RightHandRing3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing3Tx", "RightHandRing3Tx"),
        ("RightHandRing3Ty", "RightHandRing3Ty"),
        ("RightHandRing3Tz", "RightHandRing3Tz"),
    )

    RightHandRing3Tx = DoubleLinearField(default_value=0.0)

    RightHandRing3Ty = DoubleLinearField(default_value=0.0)

    RightHandRing3Tz = DoubleLinearField(default_value=0.0)


class RightHandRing3TAttrOperator(
    CompoundAttrOperator[RightHandRing3TPlugOperator]
):
    __slots__ = ()

    RightHandRing3Tx = DoubleLinearField(default_value=0.0)

    RightHandRing3Ty = DoubleLinearField(default_value=0.0)

    RightHandRing3Tz = DoubleLinearField(default_value=0.0)


class RightHandRing3TField(
    CompoundField[RightHandRing3TAttrOperator, RightHandRing3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing3TAttrOperator
    PLUG_CLS = RightHandRing3TPlugOperator

    RightHandRing3Tx = DoubleLinearField(default_value=0.0)

    RightHandRing3Ty = DoubleLinearField(default_value=0.0)

    RightHandRing3Tz = DoubleLinearField(default_value=0.0)


class RightHandRing3RPlugOperator(
    CompoundPlugOperator["RightHandRing3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing3Rx", "RightHandRing3Rx"),
        ("RightHandRing3Ry", "RightHandRing3Ry"),
        ("RightHandRing3Rz", "RightHandRing3Rz"),
    )

    RightHandRing3Rx = DoubleAngleField(default_value=0.0)

    RightHandRing3Ry = DoubleAngleField(default_value=0.0)

    RightHandRing3Rz = DoubleAngleField(default_value=0.0)


class RightHandRing3RAttrOperator(
    CompoundAttrOperator[RightHandRing3RPlugOperator]
):
    __slots__ = ()

    RightHandRing3Rx = DoubleAngleField(default_value=0.0)

    RightHandRing3Ry = DoubleAngleField(default_value=0.0)

    RightHandRing3Rz = DoubleAngleField(default_value=0.0)


class RightHandRing3RField(
    CompoundField[RightHandRing3RAttrOperator, RightHandRing3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing3RAttrOperator
    PLUG_CLS = RightHandRing3RPlugOperator

    RightHandRing3Rx = DoubleAngleField(default_value=0.0)

    RightHandRing3Ry = DoubleAngleField(default_value=0.0)

    RightHandRing3Rz = DoubleAngleField(default_value=0.0)


class RightHandRing3SPlugOperator(
    CompoundPlugOperator["RightHandRing3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing3Sx", "RightHandRing3Sx"),
        ("RightHandRing3Sy", "RightHandRing3Sy"),
        ("RightHandRing3Sz", "RightHandRing3Sz"),
    )

    RightHandRing3Sx = DoubleField(default_value=1.0)

    RightHandRing3Sy = DoubleField(default_value=1.0)

    RightHandRing3Sz = DoubleField(default_value=1.0)


class RightHandRing3SAttrOperator(
    CompoundAttrOperator[RightHandRing3SPlugOperator]
):
    __slots__ = ()

    RightHandRing3Sx = DoubleField(default_value=1.0)

    RightHandRing3Sy = DoubleField(default_value=1.0)

    RightHandRing3Sz = DoubleField(default_value=1.0)


class RightHandRing3SField(
    CompoundField[RightHandRing3SAttrOperator, RightHandRing3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing3SAttrOperator
    PLUG_CLS = RightHandRing3SPlugOperator

    RightHandRing3Sx = DoubleField(default_value=1.0)

    RightHandRing3Sy = DoubleField(default_value=1.0)

    RightHandRing3Sz = DoubleField(default_value=1.0)


class RightHandRing4TPlugOperator(
    CompoundPlugOperator["RightHandRing4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing4Tx", "RightHandRing4Tx"),
        ("RightHandRing4Ty", "RightHandRing4Ty"),
        ("RightHandRing4Tz", "RightHandRing4Tz"),
    )

    RightHandRing4Tx = DoubleLinearField(default_value=0.0)

    RightHandRing4Ty = DoubleLinearField(default_value=0.0)

    RightHandRing4Tz = DoubleLinearField(default_value=0.0)


class RightHandRing4TAttrOperator(
    CompoundAttrOperator[RightHandRing4TPlugOperator]
):
    __slots__ = ()

    RightHandRing4Tx = DoubleLinearField(default_value=0.0)

    RightHandRing4Ty = DoubleLinearField(default_value=0.0)

    RightHandRing4Tz = DoubleLinearField(default_value=0.0)


class RightHandRing4TField(
    CompoundField[RightHandRing4TAttrOperator, RightHandRing4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing4TAttrOperator
    PLUG_CLS = RightHandRing4TPlugOperator

    RightHandRing4Tx = DoubleLinearField(default_value=0.0)

    RightHandRing4Ty = DoubleLinearField(default_value=0.0)

    RightHandRing4Tz = DoubleLinearField(default_value=0.0)


class RightHandRing4RPlugOperator(
    CompoundPlugOperator["RightHandRing4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing4Rx", "RightHandRing4Rx"),
        ("RightHandRing4Ry", "RightHandRing4Ry"),
        ("RightHandRing4Rz", "RightHandRing4Rz"),
    )

    RightHandRing4Rx = DoubleAngleField(default_value=0.0)

    RightHandRing4Ry = DoubleAngleField(default_value=0.0)

    RightHandRing4Rz = DoubleAngleField(default_value=0.0)


class RightHandRing4RAttrOperator(
    CompoundAttrOperator[RightHandRing4RPlugOperator]
):
    __slots__ = ()

    RightHandRing4Rx = DoubleAngleField(default_value=0.0)

    RightHandRing4Ry = DoubleAngleField(default_value=0.0)

    RightHandRing4Rz = DoubleAngleField(default_value=0.0)


class RightHandRing4RField(
    CompoundField[RightHandRing4RAttrOperator, RightHandRing4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing4RAttrOperator
    PLUG_CLS = RightHandRing4RPlugOperator

    RightHandRing4Rx = DoubleAngleField(default_value=0.0)

    RightHandRing4Ry = DoubleAngleField(default_value=0.0)

    RightHandRing4Rz = DoubleAngleField(default_value=0.0)


class RightHandRing4SPlugOperator(
    CompoundPlugOperator["RightHandRing4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandRing4Sx", "RightHandRing4Sx"),
        ("RightHandRing4Sy", "RightHandRing4Sy"),
        ("RightHandRing4Sz", "RightHandRing4Sz"),
    )

    RightHandRing4Sx = DoubleField(default_value=1.0)

    RightHandRing4Sy = DoubleField(default_value=1.0)

    RightHandRing4Sz = DoubleField(default_value=1.0)


class RightHandRing4SAttrOperator(
    CompoundAttrOperator[RightHandRing4SPlugOperator]
):
    __slots__ = ()

    RightHandRing4Sx = DoubleField(default_value=1.0)

    RightHandRing4Sy = DoubleField(default_value=1.0)

    RightHandRing4Sz = DoubleField(default_value=1.0)


class RightHandRing4SField(
    CompoundField[RightHandRing4SAttrOperator, RightHandRing4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandRing4SAttrOperator
    PLUG_CLS = RightHandRing4SPlugOperator

    RightHandRing4Sx = DoubleField(default_value=1.0)

    RightHandRing4Sy = DoubleField(default_value=1.0)

    RightHandRing4Sz = DoubleField(default_value=1.0)


class RightHandPinky1TPlugOperator(
    CompoundPlugOperator["RightHandPinky1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky1Tx", "RightHandPinky1Tx"),
        ("RightHandPinky1Ty", "RightHandPinky1Ty"),
        ("RightHandPinky1Tz", "RightHandPinky1Tz"),
    )

    RightHandPinky1Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky1Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky1Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky1TAttrOperator(
    CompoundAttrOperator[RightHandPinky1TPlugOperator]
):
    __slots__ = ()

    RightHandPinky1Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky1Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky1Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky1TField(
    CompoundField[RightHandPinky1TAttrOperator, RightHandPinky1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky1TAttrOperator
    PLUG_CLS = RightHandPinky1TPlugOperator

    RightHandPinky1Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky1Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky1Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky1RPlugOperator(
    CompoundPlugOperator["RightHandPinky1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky1Rx", "RightHandPinky1Rx"),
        ("RightHandPinky1Ry", "RightHandPinky1Ry"),
        ("RightHandPinky1Rz", "RightHandPinky1Rz"),
    )

    RightHandPinky1Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky1Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky1Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky1RAttrOperator(
    CompoundAttrOperator[RightHandPinky1RPlugOperator]
):
    __slots__ = ()

    RightHandPinky1Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky1Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky1Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky1RField(
    CompoundField[RightHandPinky1RAttrOperator, RightHandPinky1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky1RAttrOperator
    PLUG_CLS = RightHandPinky1RPlugOperator

    RightHandPinky1Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky1Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky1Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky1SPlugOperator(
    CompoundPlugOperator["RightHandPinky1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky1Sx", "RightHandPinky1Sx"),
        ("RightHandPinky1Sy", "RightHandPinky1Sy"),
        ("RightHandPinky1Sz", "RightHandPinky1Sz"),
    )

    RightHandPinky1Sx = DoubleField(default_value=1.0)

    RightHandPinky1Sy = DoubleField(default_value=1.0)

    RightHandPinky1Sz = DoubleField(default_value=1.0)


class RightHandPinky1SAttrOperator(
    CompoundAttrOperator[RightHandPinky1SPlugOperator]
):
    __slots__ = ()

    RightHandPinky1Sx = DoubleField(default_value=1.0)

    RightHandPinky1Sy = DoubleField(default_value=1.0)

    RightHandPinky1Sz = DoubleField(default_value=1.0)


class RightHandPinky1SField(
    CompoundField[RightHandPinky1SAttrOperator, RightHandPinky1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky1SAttrOperator
    PLUG_CLS = RightHandPinky1SPlugOperator

    RightHandPinky1Sx = DoubleField(default_value=1.0)

    RightHandPinky1Sy = DoubleField(default_value=1.0)

    RightHandPinky1Sz = DoubleField(default_value=1.0)


class RightHandPinky2TPlugOperator(
    CompoundPlugOperator["RightHandPinky2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky2Tx", "RightHandPinky2Tx"),
        ("RightHandPinky2Ty", "RightHandPinky2Ty"),
        ("RightHandPinky2Tz", "RightHandPinky2Tz"),
    )

    RightHandPinky2Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky2Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky2Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky2TAttrOperator(
    CompoundAttrOperator[RightHandPinky2TPlugOperator]
):
    __slots__ = ()

    RightHandPinky2Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky2Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky2Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky2TField(
    CompoundField[RightHandPinky2TAttrOperator, RightHandPinky2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky2TAttrOperator
    PLUG_CLS = RightHandPinky2TPlugOperator

    RightHandPinky2Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky2Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky2Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky2RPlugOperator(
    CompoundPlugOperator["RightHandPinky2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky2Rx", "RightHandPinky2Rx"),
        ("RightHandPinky2Ry", "RightHandPinky2Ry"),
        ("RightHandPinky2Rz", "RightHandPinky2Rz"),
    )

    RightHandPinky2Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky2Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky2Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky2RAttrOperator(
    CompoundAttrOperator[RightHandPinky2RPlugOperator]
):
    __slots__ = ()

    RightHandPinky2Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky2Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky2Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky2RField(
    CompoundField[RightHandPinky2RAttrOperator, RightHandPinky2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky2RAttrOperator
    PLUG_CLS = RightHandPinky2RPlugOperator

    RightHandPinky2Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky2Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky2Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky2SPlugOperator(
    CompoundPlugOperator["RightHandPinky2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky2Sx", "RightHandPinky2Sx"),
        ("RightHandPinky2Sy", "RightHandPinky2Sy"),
        ("RightHandPinky2Sz", "RightHandPinky2Sz"),
    )

    RightHandPinky2Sx = DoubleField(default_value=1.0)

    RightHandPinky2Sy = DoubleField(default_value=1.0)

    RightHandPinky2Sz = DoubleField(default_value=1.0)


class RightHandPinky2SAttrOperator(
    CompoundAttrOperator[RightHandPinky2SPlugOperator]
):
    __slots__ = ()

    RightHandPinky2Sx = DoubleField(default_value=1.0)

    RightHandPinky2Sy = DoubleField(default_value=1.0)

    RightHandPinky2Sz = DoubleField(default_value=1.0)


class RightHandPinky2SField(
    CompoundField[RightHandPinky2SAttrOperator, RightHandPinky2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky2SAttrOperator
    PLUG_CLS = RightHandPinky2SPlugOperator

    RightHandPinky2Sx = DoubleField(default_value=1.0)

    RightHandPinky2Sy = DoubleField(default_value=1.0)

    RightHandPinky2Sz = DoubleField(default_value=1.0)


class RightHandPinky3TPlugOperator(
    CompoundPlugOperator["RightHandPinky3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky3Tx", "RightHandPinky3Tx"),
        ("RightHandPinky3Ty", "RightHandPinky3Ty"),
        ("RightHandPinky3Tz", "RightHandPinky3Tz"),
    )

    RightHandPinky3Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky3Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky3Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky3TAttrOperator(
    CompoundAttrOperator[RightHandPinky3TPlugOperator]
):
    __slots__ = ()

    RightHandPinky3Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky3Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky3Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky3TField(
    CompoundField[RightHandPinky3TAttrOperator, RightHandPinky3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky3TAttrOperator
    PLUG_CLS = RightHandPinky3TPlugOperator

    RightHandPinky3Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky3Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky3Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky3RPlugOperator(
    CompoundPlugOperator["RightHandPinky3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky3Rx", "RightHandPinky3Rx"),
        ("RightHandPinky3Ry", "RightHandPinky3Ry"),
        ("RightHandPinky3Rz", "RightHandPinky3Rz"),
    )

    RightHandPinky3Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky3Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky3Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky3RAttrOperator(
    CompoundAttrOperator[RightHandPinky3RPlugOperator]
):
    __slots__ = ()

    RightHandPinky3Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky3Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky3Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky3RField(
    CompoundField[RightHandPinky3RAttrOperator, RightHandPinky3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky3RAttrOperator
    PLUG_CLS = RightHandPinky3RPlugOperator

    RightHandPinky3Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky3Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky3Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky3SPlugOperator(
    CompoundPlugOperator["RightHandPinky3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky3Sx", "RightHandPinky3Sx"),
        ("RightHandPinky3Sy", "RightHandPinky3Sy"),
        ("RightHandPinky3Sz", "RightHandPinky3Sz"),
    )

    RightHandPinky3Sx = DoubleField(default_value=1.0)

    RightHandPinky3Sy = DoubleField(default_value=1.0)

    RightHandPinky3Sz = DoubleField(default_value=1.0)


class RightHandPinky3SAttrOperator(
    CompoundAttrOperator[RightHandPinky3SPlugOperator]
):
    __slots__ = ()

    RightHandPinky3Sx = DoubleField(default_value=1.0)

    RightHandPinky3Sy = DoubleField(default_value=1.0)

    RightHandPinky3Sz = DoubleField(default_value=1.0)


class RightHandPinky3SField(
    CompoundField[RightHandPinky3SAttrOperator, RightHandPinky3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky3SAttrOperator
    PLUG_CLS = RightHandPinky3SPlugOperator

    RightHandPinky3Sx = DoubleField(default_value=1.0)

    RightHandPinky3Sy = DoubleField(default_value=1.0)

    RightHandPinky3Sz = DoubleField(default_value=1.0)


class RightHandPinky4TPlugOperator(
    CompoundPlugOperator["RightHandPinky4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky4Tx", "RightHandPinky4Tx"),
        ("RightHandPinky4Ty", "RightHandPinky4Ty"),
        ("RightHandPinky4Tz", "RightHandPinky4Tz"),
    )

    RightHandPinky4Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky4Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky4Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky4TAttrOperator(
    CompoundAttrOperator[RightHandPinky4TPlugOperator]
):
    __slots__ = ()

    RightHandPinky4Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky4Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky4Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky4TField(
    CompoundField[RightHandPinky4TAttrOperator, RightHandPinky4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky4TAttrOperator
    PLUG_CLS = RightHandPinky4TPlugOperator

    RightHandPinky4Tx = DoubleLinearField(default_value=0.0)

    RightHandPinky4Ty = DoubleLinearField(default_value=0.0)

    RightHandPinky4Tz = DoubleLinearField(default_value=0.0)


class RightHandPinky4RPlugOperator(
    CompoundPlugOperator["RightHandPinky4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky4Rx", "RightHandPinky4Rx"),
        ("RightHandPinky4Ry", "RightHandPinky4Ry"),
        ("RightHandPinky4Rz", "RightHandPinky4Rz"),
    )

    RightHandPinky4Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky4Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky4Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky4RAttrOperator(
    CompoundAttrOperator[RightHandPinky4RPlugOperator]
):
    __slots__ = ()

    RightHandPinky4Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky4Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky4Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky4RField(
    CompoundField[RightHandPinky4RAttrOperator, RightHandPinky4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky4RAttrOperator
    PLUG_CLS = RightHandPinky4RPlugOperator

    RightHandPinky4Rx = DoubleAngleField(default_value=0.0)

    RightHandPinky4Ry = DoubleAngleField(default_value=0.0)

    RightHandPinky4Rz = DoubleAngleField(default_value=0.0)


class RightHandPinky4SPlugOperator(
    CompoundPlugOperator["RightHandPinky4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandPinky4Sx", "RightHandPinky4Sx"),
        ("RightHandPinky4Sy", "RightHandPinky4Sy"),
        ("RightHandPinky4Sz", "RightHandPinky4Sz"),
    )

    RightHandPinky4Sx = DoubleField(default_value=1.0)

    RightHandPinky4Sy = DoubleField(default_value=1.0)

    RightHandPinky4Sz = DoubleField(default_value=1.0)


class RightHandPinky4SAttrOperator(
    CompoundAttrOperator[RightHandPinky4SPlugOperator]
):
    __slots__ = ()

    RightHandPinky4Sx = DoubleField(default_value=1.0)

    RightHandPinky4Sy = DoubleField(default_value=1.0)

    RightHandPinky4Sz = DoubleField(default_value=1.0)


class RightHandPinky4SField(
    CompoundField[RightHandPinky4SAttrOperator, RightHandPinky4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandPinky4SAttrOperator
    PLUG_CLS = RightHandPinky4SPlugOperator

    RightHandPinky4Sx = DoubleField(default_value=1.0)

    RightHandPinky4Sy = DoubleField(default_value=1.0)

    RightHandPinky4Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger1TPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger1Tx", "RightHandExtraFinger1Tx"),
        ("RightHandExtraFinger1Ty", "RightHandExtraFinger1Ty"),
        ("RightHandExtraFinger1Tz", "RightHandExtraFinger1Tz"),
    )

    RightHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger1TAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger1TPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger1TField(
    CompoundField[RightHandExtraFinger1TAttrOperator, RightHandExtraFinger1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger1TAttrOperator
    PLUG_CLS = RightHandExtraFinger1TPlugOperator

    RightHandExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger1RPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger1Rx", "RightHandExtraFinger1Rx"),
        ("RightHandExtraFinger1Ry", "RightHandExtraFinger1Ry"),
        ("RightHandExtraFinger1Rz", "RightHandExtraFinger1Rz"),
    )

    RightHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger1RAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger1RPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger1RField(
    CompoundField[RightHandExtraFinger1RAttrOperator, RightHandExtraFinger1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger1RAttrOperator
    PLUG_CLS = RightHandExtraFinger1RPlugOperator

    RightHandExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger1SPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger1Sx", "RightHandExtraFinger1Sx"),
        ("RightHandExtraFinger1Sy", "RightHandExtraFinger1Sy"),
        ("RightHandExtraFinger1Sz", "RightHandExtraFinger1Sz"),
    )

    RightHandExtraFinger1Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger1SAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger1SPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger1Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger1SField(
    CompoundField[RightHandExtraFinger1SAttrOperator, RightHandExtraFinger1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger1SAttrOperator
    PLUG_CLS = RightHandExtraFinger1SPlugOperator

    RightHandExtraFinger1Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger1Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger2TPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger2Tx", "RightHandExtraFinger2Tx"),
        ("RightHandExtraFinger2Ty", "RightHandExtraFinger2Ty"),
        ("RightHandExtraFinger2Tz", "RightHandExtraFinger2Tz"),
    )

    RightHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger2TAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger2TPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger2TField(
    CompoundField[RightHandExtraFinger2TAttrOperator, RightHandExtraFinger2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger2TAttrOperator
    PLUG_CLS = RightHandExtraFinger2TPlugOperator

    RightHandExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger2RPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger2Rx", "RightHandExtraFinger2Rx"),
        ("RightHandExtraFinger2Ry", "RightHandExtraFinger2Ry"),
        ("RightHandExtraFinger2Rz", "RightHandExtraFinger2Rz"),
    )

    RightHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger2RAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger2RPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger2RField(
    CompoundField[RightHandExtraFinger2RAttrOperator, RightHandExtraFinger2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger2RAttrOperator
    PLUG_CLS = RightHandExtraFinger2RPlugOperator

    RightHandExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger2SPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger2Sx", "RightHandExtraFinger2Sx"),
        ("RightHandExtraFinger2Sy", "RightHandExtraFinger2Sy"),
        ("RightHandExtraFinger2Sz", "RightHandExtraFinger2Sz"),
    )

    RightHandExtraFinger2Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger2SAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger2SPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger2Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger2SField(
    CompoundField[RightHandExtraFinger2SAttrOperator, RightHandExtraFinger2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger2SAttrOperator
    PLUG_CLS = RightHandExtraFinger2SPlugOperator

    RightHandExtraFinger2Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger2Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger3TPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger3Tx", "RightHandExtraFinger3Tx"),
        ("RightHandExtraFinger3Ty", "RightHandExtraFinger3Ty"),
        ("RightHandExtraFinger3Tz", "RightHandExtraFinger3Tz"),
    )

    RightHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger3TAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger3TPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger3TField(
    CompoundField[RightHandExtraFinger3TAttrOperator, RightHandExtraFinger3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger3TAttrOperator
    PLUG_CLS = RightHandExtraFinger3TPlugOperator

    RightHandExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger3RPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger3Rx", "RightHandExtraFinger3Rx"),
        ("RightHandExtraFinger3Ry", "RightHandExtraFinger3Ry"),
        ("RightHandExtraFinger3Rz", "RightHandExtraFinger3Rz"),
    )

    RightHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger3RAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger3RPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger3RField(
    CompoundField[RightHandExtraFinger3RAttrOperator, RightHandExtraFinger3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger3RAttrOperator
    PLUG_CLS = RightHandExtraFinger3RPlugOperator

    RightHandExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger3SPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger3Sx", "RightHandExtraFinger3Sx"),
        ("RightHandExtraFinger3Sy", "RightHandExtraFinger3Sy"),
        ("RightHandExtraFinger3Sz", "RightHandExtraFinger3Sz"),
    )

    RightHandExtraFinger3Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger3SAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger3SPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger3Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger3SField(
    CompoundField[RightHandExtraFinger3SAttrOperator, RightHandExtraFinger3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger3SAttrOperator
    PLUG_CLS = RightHandExtraFinger3SPlugOperator

    RightHandExtraFinger3Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger3Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger4TPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger4Tx", "RightHandExtraFinger4Tx"),
        ("RightHandExtraFinger4Ty", "RightHandExtraFinger4Ty"),
        ("RightHandExtraFinger4Tz", "RightHandExtraFinger4Tz"),
    )

    RightHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger4TAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger4TPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger4TField(
    CompoundField[RightHandExtraFinger4TAttrOperator, RightHandExtraFinger4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger4TAttrOperator
    PLUG_CLS = RightHandExtraFinger4TPlugOperator

    RightHandExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightHandExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightHandExtraFinger4RPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger4Rx", "RightHandExtraFinger4Rx"),
        ("RightHandExtraFinger4Ry", "RightHandExtraFinger4Ry"),
        ("RightHandExtraFinger4Rz", "RightHandExtraFinger4Rz"),
    )

    RightHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger4RAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger4RPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger4RField(
    CompoundField[RightHandExtraFinger4RAttrOperator, RightHandExtraFinger4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger4RAttrOperator
    PLUG_CLS = RightHandExtraFinger4RPlugOperator

    RightHandExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightHandExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightHandExtraFinger4SPlugOperator(
    CompoundPlugOperator["RightHandExtraFinger4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightHandExtraFinger4Sx", "RightHandExtraFinger4Sx"),
        ("RightHandExtraFinger4Sy", "RightHandExtraFinger4Sy"),
        ("RightHandExtraFinger4Sz", "RightHandExtraFinger4Sz"),
    )

    RightHandExtraFinger4Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger4SAttrOperator(
    CompoundAttrOperator[RightHandExtraFinger4SPlugOperator]
):
    __slots__ = ()

    RightHandExtraFinger4Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sz = DoubleField(default_value=1.0)


class RightHandExtraFinger4SField(
    CompoundField[RightHandExtraFinger4SAttrOperator, RightHandExtraFinger4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightHandExtraFinger4SAttrOperator
    PLUG_CLS = RightHandExtraFinger4SPlugOperator

    RightHandExtraFinger4Sx = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sy = DoubleField(default_value=1.0)

    RightHandExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftFootThumb1TPlugOperator(
    CompoundPlugOperator["LeftFootThumb1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb1Tx", "LeftFootThumb1Tx"),
        ("LeftFootThumb1Ty", "LeftFootThumb1Ty"),
        ("LeftFootThumb1Tz", "LeftFootThumb1Tz"),
    )

    LeftFootThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb1TAttrOperator(
    CompoundAttrOperator[LeftFootThumb1TPlugOperator]
):
    __slots__ = ()

    LeftFootThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb1TField(
    CompoundField[LeftFootThumb1TAttrOperator, LeftFootThumb1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb1TAttrOperator
    PLUG_CLS = LeftFootThumb1TPlugOperator

    LeftFootThumb1Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb1Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb1RPlugOperator(
    CompoundPlugOperator["LeftFootThumb1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb1Rx", "LeftFootThumb1Rx"),
        ("LeftFootThumb1Ry", "LeftFootThumb1Ry"),
        ("LeftFootThumb1Rz", "LeftFootThumb1Rz"),
    )

    LeftFootThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb1RAttrOperator(
    CompoundAttrOperator[LeftFootThumb1RPlugOperator]
):
    __slots__ = ()

    LeftFootThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb1RField(
    CompoundField[LeftFootThumb1RAttrOperator, LeftFootThumb1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb1RAttrOperator
    PLUG_CLS = LeftFootThumb1RPlugOperator

    LeftFootThumb1Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb1Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb1SPlugOperator(
    CompoundPlugOperator["LeftFootThumb1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb1Sx", "LeftFootThumb1Sx"),
        ("LeftFootThumb1Sy", "LeftFootThumb1Sy"),
        ("LeftFootThumb1Sz", "LeftFootThumb1Sz"),
    )

    LeftFootThumb1Sx = DoubleField(default_value=1.0)

    LeftFootThumb1Sy = DoubleField(default_value=1.0)

    LeftFootThumb1Sz = DoubleField(default_value=1.0)


class LeftFootThumb1SAttrOperator(
    CompoundAttrOperator[LeftFootThumb1SPlugOperator]
):
    __slots__ = ()

    LeftFootThumb1Sx = DoubleField(default_value=1.0)

    LeftFootThumb1Sy = DoubleField(default_value=1.0)

    LeftFootThumb1Sz = DoubleField(default_value=1.0)


class LeftFootThumb1SField(
    CompoundField[LeftFootThumb1SAttrOperator, LeftFootThumb1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb1SAttrOperator
    PLUG_CLS = LeftFootThumb1SPlugOperator

    LeftFootThumb1Sx = DoubleField(default_value=1.0)

    LeftFootThumb1Sy = DoubleField(default_value=1.0)

    LeftFootThumb1Sz = DoubleField(default_value=1.0)


class LeftFootThumb2TPlugOperator(
    CompoundPlugOperator["LeftFootThumb2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb2Tx", "LeftFootThumb2Tx"),
        ("LeftFootThumb2Ty", "LeftFootThumb2Ty"),
        ("LeftFootThumb2Tz", "LeftFootThumb2Tz"),
    )

    LeftFootThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb2TAttrOperator(
    CompoundAttrOperator[LeftFootThumb2TPlugOperator]
):
    __slots__ = ()

    LeftFootThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb2TField(
    CompoundField[LeftFootThumb2TAttrOperator, LeftFootThumb2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb2TAttrOperator
    PLUG_CLS = LeftFootThumb2TPlugOperator

    LeftFootThumb2Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb2Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb2RPlugOperator(
    CompoundPlugOperator["LeftFootThumb2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb2Rx", "LeftFootThumb2Rx"),
        ("LeftFootThumb2Ry", "LeftFootThumb2Ry"),
        ("LeftFootThumb2Rz", "LeftFootThumb2Rz"),
    )

    LeftFootThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb2RAttrOperator(
    CompoundAttrOperator[LeftFootThumb2RPlugOperator]
):
    __slots__ = ()

    LeftFootThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb2RField(
    CompoundField[LeftFootThumb2RAttrOperator, LeftFootThumb2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb2RAttrOperator
    PLUG_CLS = LeftFootThumb2RPlugOperator

    LeftFootThumb2Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb2Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb2SPlugOperator(
    CompoundPlugOperator["LeftFootThumb2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb2Sx", "LeftFootThumb2Sx"),
        ("LeftFootThumb2Sy", "LeftFootThumb2Sy"),
        ("LeftFootThumb2Sz", "LeftFootThumb2Sz"),
    )

    LeftFootThumb2Sx = DoubleField(default_value=1.0)

    LeftFootThumb2Sy = DoubleField(default_value=1.0)

    LeftFootThumb2Sz = DoubleField(default_value=1.0)


class LeftFootThumb2SAttrOperator(
    CompoundAttrOperator[LeftFootThumb2SPlugOperator]
):
    __slots__ = ()

    LeftFootThumb2Sx = DoubleField(default_value=1.0)

    LeftFootThumb2Sy = DoubleField(default_value=1.0)

    LeftFootThumb2Sz = DoubleField(default_value=1.0)


class LeftFootThumb2SField(
    CompoundField[LeftFootThumb2SAttrOperator, LeftFootThumb2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb2SAttrOperator
    PLUG_CLS = LeftFootThumb2SPlugOperator

    LeftFootThumb2Sx = DoubleField(default_value=1.0)

    LeftFootThumb2Sy = DoubleField(default_value=1.0)

    LeftFootThumb2Sz = DoubleField(default_value=1.0)


class LeftFootThumb3TPlugOperator(
    CompoundPlugOperator["LeftFootThumb3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb3Tx", "LeftFootThumb3Tx"),
        ("LeftFootThumb3Ty", "LeftFootThumb3Ty"),
        ("LeftFootThumb3Tz", "LeftFootThumb3Tz"),
    )

    LeftFootThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb3TAttrOperator(
    CompoundAttrOperator[LeftFootThumb3TPlugOperator]
):
    __slots__ = ()

    LeftFootThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb3TField(
    CompoundField[LeftFootThumb3TAttrOperator, LeftFootThumb3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb3TAttrOperator
    PLUG_CLS = LeftFootThumb3TPlugOperator

    LeftFootThumb3Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb3Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb3RPlugOperator(
    CompoundPlugOperator["LeftFootThumb3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb3Rx", "LeftFootThumb3Rx"),
        ("LeftFootThumb3Ry", "LeftFootThumb3Ry"),
        ("LeftFootThumb3Rz", "LeftFootThumb3Rz"),
    )

    LeftFootThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb3RAttrOperator(
    CompoundAttrOperator[LeftFootThumb3RPlugOperator]
):
    __slots__ = ()

    LeftFootThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb3RField(
    CompoundField[LeftFootThumb3RAttrOperator, LeftFootThumb3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb3RAttrOperator
    PLUG_CLS = LeftFootThumb3RPlugOperator

    LeftFootThumb3Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb3Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb3SPlugOperator(
    CompoundPlugOperator["LeftFootThumb3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb3Sx", "LeftFootThumb3Sx"),
        ("LeftFootThumb3Sy", "LeftFootThumb3Sy"),
        ("LeftFootThumb3Sz", "LeftFootThumb3Sz"),
    )

    LeftFootThumb3Sx = DoubleField(default_value=1.0)

    LeftFootThumb3Sy = DoubleField(default_value=1.0)

    LeftFootThumb3Sz = DoubleField(default_value=1.0)


class LeftFootThumb3SAttrOperator(
    CompoundAttrOperator[LeftFootThumb3SPlugOperator]
):
    __slots__ = ()

    LeftFootThumb3Sx = DoubleField(default_value=1.0)

    LeftFootThumb3Sy = DoubleField(default_value=1.0)

    LeftFootThumb3Sz = DoubleField(default_value=1.0)


class LeftFootThumb3SField(
    CompoundField[LeftFootThumb3SAttrOperator, LeftFootThumb3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb3SAttrOperator
    PLUG_CLS = LeftFootThumb3SPlugOperator

    LeftFootThumb3Sx = DoubleField(default_value=1.0)

    LeftFootThumb3Sy = DoubleField(default_value=1.0)

    LeftFootThumb3Sz = DoubleField(default_value=1.0)


class LeftFootThumb4TPlugOperator(
    CompoundPlugOperator["LeftFootThumb4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb4Tx", "LeftFootThumb4Tx"),
        ("LeftFootThumb4Ty", "LeftFootThumb4Ty"),
        ("LeftFootThumb4Tz", "LeftFootThumb4Tz"),
    )

    LeftFootThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb4TAttrOperator(
    CompoundAttrOperator[LeftFootThumb4TPlugOperator]
):
    __slots__ = ()

    LeftFootThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb4TField(
    CompoundField[LeftFootThumb4TAttrOperator, LeftFootThumb4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb4TAttrOperator
    PLUG_CLS = LeftFootThumb4TPlugOperator

    LeftFootThumb4Tx = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Ty = DoubleLinearField(default_value=0.0)

    LeftFootThumb4Tz = DoubleLinearField(default_value=0.0)


class LeftFootThumb4RPlugOperator(
    CompoundPlugOperator["LeftFootThumb4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb4Rx", "LeftFootThumb4Rx"),
        ("LeftFootThumb4Ry", "LeftFootThumb4Ry"),
        ("LeftFootThumb4Rz", "LeftFootThumb4Rz"),
    )

    LeftFootThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb4RAttrOperator(
    CompoundAttrOperator[LeftFootThumb4RPlugOperator]
):
    __slots__ = ()

    LeftFootThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb4RField(
    CompoundField[LeftFootThumb4RAttrOperator, LeftFootThumb4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb4RAttrOperator
    PLUG_CLS = LeftFootThumb4RPlugOperator

    LeftFootThumb4Rx = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Ry = DoubleAngleField(default_value=0.0)

    LeftFootThumb4Rz = DoubleAngleField(default_value=0.0)


class LeftFootThumb4SPlugOperator(
    CompoundPlugOperator["LeftFootThumb4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootThumb4Sx", "LeftFootThumb4Sx"),
        ("LeftFootThumb4Sy", "LeftFootThumb4Sy"),
        ("LeftFootThumb4Sz", "LeftFootThumb4Sz"),
    )

    LeftFootThumb4Sx = DoubleField(default_value=1.0)

    LeftFootThumb4Sy = DoubleField(default_value=1.0)

    LeftFootThumb4Sz = DoubleField(default_value=1.0)


class LeftFootThumb4SAttrOperator(
    CompoundAttrOperator[LeftFootThumb4SPlugOperator]
):
    __slots__ = ()

    LeftFootThumb4Sx = DoubleField(default_value=1.0)

    LeftFootThumb4Sy = DoubleField(default_value=1.0)

    LeftFootThumb4Sz = DoubleField(default_value=1.0)


class LeftFootThumb4SField(
    CompoundField[LeftFootThumb4SAttrOperator, LeftFootThumb4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootThumb4SAttrOperator
    PLUG_CLS = LeftFootThumb4SPlugOperator

    LeftFootThumb4Sx = DoubleField(default_value=1.0)

    LeftFootThumb4Sy = DoubleField(default_value=1.0)

    LeftFootThumb4Sz = DoubleField(default_value=1.0)


class LeftFootIndex1TPlugOperator(
    CompoundPlugOperator["LeftFootIndex1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex1Tx", "LeftFootIndex1Tx"),
        ("LeftFootIndex1Ty", "LeftFootIndex1Ty"),
        ("LeftFootIndex1Tz", "LeftFootIndex1Tz"),
    )

    LeftFootIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex1TAttrOperator(
    CompoundAttrOperator[LeftFootIndex1TPlugOperator]
):
    __slots__ = ()

    LeftFootIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex1TField(
    CompoundField[LeftFootIndex1TAttrOperator, LeftFootIndex1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex1TAttrOperator
    PLUG_CLS = LeftFootIndex1TPlugOperator

    LeftFootIndex1Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex1Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex1RPlugOperator(
    CompoundPlugOperator["LeftFootIndex1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex1Rx", "LeftFootIndex1Rx"),
        ("LeftFootIndex1Ry", "LeftFootIndex1Ry"),
        ("LeftFootIndex1Rz", "LeftFootIndex1Rz"),
    )

    LeftFootIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex1RAttrOperator(
    CompoundAttrOperator[LeftFootIndex1RPlugOperator]
):
    __slots__ = ()

    LeftFootIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex1RField(
    CompoundField[LeftFootIndex1RAttrOperator, LeftFootIndex1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex1RAttrOperator
    PLUG_CLS = LeftFootIndex1RPlugOperator

    LeftFootIndex1Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex1Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex1SPlugOperator(
    CompoundPlugOperator["LeftFootIndex1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex1Sx", "LeftFootIndex1Sx"),
        ("LeftFootIndex1Sy", "LeftFootIndex1Sy"),
        ("LeftFootIndex1Sz", "LeftFootIndex1Sz"),
    )

    LeftFootIndex1Sx = DoubleField(default_value=1.0)

    LeftFootIndex1Sy = DoubleField(default_value=1.0)

    LeftFootIndex1Sz = DoubleField(default_value=1.0)


class LeftFootIndex1SAttrOperator(
    CompoundAttrOperator[LeftFootIndex1SPlugOperator]
):
    __slots__ = ()

    LeftFootIndex1Sx = DoubleField(default_value=1.0)

    LeftFootIndex1Sy = DoubleField(default_value=1.0)

    LeftFootIndex1Sz = DoubleField(default_value=1.0)


class LeftFootIndex1SField(
    CompoundField[LeftFootIndex1SAttrOperator, LeftFootIndex1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex1SAttrOperator
    PLUG_CLS = LeftFootIndex1SPlugOperator

    LeftFootIndex1Sx = DoubleField(default_value=1.0)

    LeftFootIndex1Sy = DoubleField(default_value=1.0)

    LeftFootIndex1Sz = DoubleField(default_value=1.0)


class LeftFootIndex2TPlugOperator(
    CompoundPlugOperator["LeftFootIndex2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex2Tx", "LeftFootIndex2Tx"),
        ("LeftFootIndex2Ty", "LeftFootIndex2Ty"),
        ("LeftFootIndex2Tz", "LeftFootIndex2Tz"),
    )

    LeftFootIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex2TAttrOperator(
    CompoundAttrOperator[LeftFootIndex2TPlugOperator]
):
    __slots__ = ()

    LeftFootIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex2TField(
    CompoundField[LeftFootIndex2TAttrOperator, LeftFootIndex2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex2TAttrOperator
    PLUG_CLS = LeftFootIndex2TPlugOperator

    LeftFootIndex2Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex2Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex2RPlugOperator(
    CompoundPlugOperator["LeftFootIndex2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex2Rx", "LeftFootIndex2Rx"),
        ("LeftFootIndex2Ry", "LeftFootIndex2Ry"),
        ("LeftFootIndex2Rz", "LeftFootIndex2Rz"),
    )

    LeftFootIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex2RAttrOperator(
    CompoundAttrOperator[LeftFootIndex2RPlugOperator]
):
    __slots__ = ()

    LeftFootIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex2RField(
    CompoundField[LeftFootIndex2RAttrOperator, LeftFootIndex2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex2RAttrOperator
    PLUG_CLS = LeftFootIndex2RPlugOperator

    LeftFootIndex2Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex2Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex2SPlugOperator(
    CompoundPlugOperator["LeftFootIndex2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex2Sx", "LeftFootIndex2Sx"),
        ("LeftFootIndex2Sy", "LeftFootIndex2Sy"),
        ("LeftFootIndex2Sz", "LeftFootIndex2Sz"),
    )

    LeftFootIndex2Sx = DoubleField(default_value=1.0)

    LeftFootIndex2Sy = DoubleField(default_value=1.0)

    LeftFootIndex2Sz = DoubleField(default_value=1.0)


class LeftFootIndex2SAttrOperator(
    CompoundAttrOperator[LeftFootIndex2SPlugOperator]
):
    __slots__ = ()

    LeftFootIndex2Sx = DoubleField(default_value=1.0)

    LeftFootIndex2Sy = DoubleField(default_value=1.0)

    LeftFootIndex2Sz = DoubleField(default_value=1.0)


class LeftFootIndex2SField(
    CompoundField[LeftFootIndex2SAttrOperator, LeftFootIndex2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex2SAttrOperator
    PLUG_CLS = LeftFootIndex2SPlugOperator

    LeftFootIndex2Sx = DoubleField(default_value=1.0)

    LeftFootIndex2Sy = DoubleField(default_value=1.0)

    LeftFootIndex2Sz = DoubleField(default_value=1.0)


class LeftFootIndex3TPlugOperator(
    CompoundPlugOperator["LeftFootIndex3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex3Tx", "LeftFootIndex3Tx"),
        ("LeftFootIndex3Ty", "LeftFootIndex3Ty"),
        ("LeftFootIndex3Tz", "LeftFootIndex3Tz"),
    )

    LeftFootIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex3TAttrOperator(
    CompoundAttrOperator[LeftFootIndex3TPlugOperator]
):
    __slots__ = ()

    LeftFootIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex3TField(
    CompoundField[LeftFootIndex3TAttrOperator, LeftFootIndex3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex3TAttrOperator
    PLUG_CLS = LeftFootIndex3TPlugOperator

    LeftFootIndex3Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex3Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex3RPlugOperator(
    CompoundPlugOperator["LeftFootIndex3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex3Rx", "LeftFootIndex3Rx"),
        ("LeftFootIndex3Ry", "LeftFootIndex3Ry"),
        ("LeftFootIndex3Rz", "LeftFootIndex3Rz"),
    )

    LeftFootIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex3RAttrOperator(
    CompoundAttrOperator[LeftFootIndex3RPlugOperator]
):
    __slots__ = ()

    LeftFootIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex3RField(
    CompoundField[LeftFootIndex3RAttrOperator, LeftFootIndex3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex3RAttrOperator
    PLUG_CLS = LeftFootIndex3RPlugOperator

    LeftFootIndex3Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex3Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex3SPlugOperator(
    CompoundPlugOperator["LeftFootIndex3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex3Sx", "LeftFootIndex3Sx"),
        ("LeftFootIndex3Sy", "LeftFootIndex3Sy"),
        ("LeftFootIndex3Sz", "LeftFootIndex3Sz"),
    )

    LeftFootIndex3Sx = DoubleField(default_value=1.0)

    LeftFootIndex3Sy = DoubleField(default_value=1.0)

    LeftFootIndex3Sz = DoubleField(default_value=1.0)


class LeftFootIndex3SAttrOperator(
    CompoundAttrOperator[LeftFootIndex3SPlugOperator]
):
    __slots__ = ()

    LeftFootIndex3Sx = DoubleField(default_value=1.0)

    LeftFootIndex3Sy = DoubleField(default_value=1.0)

    LeftFootIndex3Sz = DoubleField(default_value=1.0)


class LeftFootIndex3SField(
    CompoundField[LeftFootIndex3SAttrOperator, LeftFootIndex3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex3SAttrOperator
    PLUG_CLS = LeftFootIndex3SPlugOperator

    LeftFootIndex3Sx = DoubleField(default_value=1.0)

    LeftFootIndex3Sy = DoubleField(default_value=1.0)

    LeftFootIndex3Sz = DoubleField(default_value=1.0)


class LeftFootIndex4TPlugOperator(
    CompoundPlugOperator["LeftFootIndex4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex4Tx", "LeftFootIndex4Tx"),
        ("LeftFootIndex4Ty", "LeftFootIndex4Ty"),
        ("LeftFootIndex4Tz", "LeftFootIndex4Tz"),
    )

    LeftFootIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex4TAttrOperator(
    CompoundAttrOperator[LeftFootIndex4TPlugOperator]
):
    __slots__ = ()

    LeftFootIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex4TField(
    CompoundField[LeftFootIndex4TAttrOperator, LeftFootIndex4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex4TAttrOperator
    PLUG_CLS = LeftFootIndex4TPlugOperator

    LeftFootIndex4Tx = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Ty = DoubleLinearField(default_value=0.0)

    LeftFootIndex4Tz = DoubleLinearField(default_value=0.0)


class LeftFootIndex4RPlugOperator(
    CompoundPlugOperator["LeftFootIndex4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex4Rx", "LeftFootIndex4Rx"),
        ("LeftFootIndex4Ry", "LeftFootIndex4Ry"),
        ("LeftFootIndex4Rz", "LeftFootIndex4Rz"),
    )

    LeftFootIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex4RAttrOperator(
    CompoundAttrOperator[LeftFootIndex4RPlugOperator]
):
    __slots__ = ()

    LeftFootIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex4RField(
    CompoundField[LeftFootIndex4RAttrOperator, LeftFootIndex4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex4RAttrOperator
    PLUG_CLS = LeftFootIndex4RPlugOperator

    LeftFootIndex4Rx = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Ry = DoubleAngleField(default_value=0.0)

    LeftFootIndex4Rz = DoubleAngleField(default_value=0.0)


class LeftFootIndex4SPlugOperator(
    CompoundPlugOperator["LeftFootIndex4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootIndex4Sx", "LeftFootIndex4Sx"),
        ("LeftFootIndex4Sy", "LeftFootIndex4Sy"),
        ("LeftFootIndex4Sz", "LeftFootIndex4Sz"),
    )

    LeftFootIndex4Sx = DoubleField(default_value=1.0)

    LeftFootIndex4Sy = DoubleField(default_value=1.0)

    LeftFootIndex4Sz = DoubleField(default_value=1.0)


class LeftFootIndex4SAttrOperator(
    CompoundAttrOperator[LeftFootIndex4SPlugOperator]
):
    __slots__ = ()

    LeftFootIndex4Sx = DoubleField(default_value=1.0)

    LeftFootIndex4Sy = DoubleField(default_value=1.0)

    LeftFootIndex4Sz = DoubleField(default_value=1.0)


class LeftFootIndex4SField(
    CompoundField[LeftFootIndex4SAttrOperator, LeftFootIndex4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootIndex4SAttrOperator
    PLUG_CLS = LeftFootIndex4SPlugOperator

    LeftFootIndex4Sx = DoubleField(default_value=1.0)

    LeftFootIndex4Sy = DoubleField(default_value=1.0)

    LeftFootIndex4Sz = DoubleField(default_value=1.0)


class LeftFootMiddle1TPlugOperator(
    CompoundPlugOperator["LeftFootMiddle1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle1Tx", "LeftFootMiddle1Tx"),
        ("LeftFootMiddle1Ty", "LeftFootMiddle1Ty"),
        ("LeftFootMiddle1Tz", "LeftFootMiddle1Tz"),
    )

    LeftFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle1TAttrOperator(
    CompoundAttrOperator[LeftFootMiddle1TPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle1TField(
    CompoundField[LeftFootMiddle1TAttrOperator, LeftFootMiddle1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle1TAttrOperator
    PLUG_CLS = LeftFootMiddle1TPlugOperator

    LeftFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle1RPlugOperator(
    CompoundPlugOperator["LeftFootMiddle1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle1Rx", "LeftFootMiddle1Rx"),
        ("LeftFootMiddle1Ry", "LeftFootMiddle1Ry"),
        ("LeftFootMiddle1Rz", "LeftFootMiddle1Rz"),
    )

    LeftFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle1RAttrOperator(
    CompoundAttrOperator[LeftFootMiddle1RPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle1RField(
    CompoundField[LeftFootMiddle1RAttrOperator, LeftFootMiddle1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle1RAttrOperator
    PLUG_CLS = LeftFootMiddle1RPlugOperator

    LeftFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle1SPlugOperator(
    CompoundPlugOperator["LeftFootMiddle1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle1Sx", "LeftFootMiddle1Sx"),
        ("LeftFootMiddle1Sy", "LeftFootMiddle1Sy"),
        ("LeftFootMiddle1Sz", "LeftFootMiddle1Sz"),
    )

    LeftFootMiddle1Sx = DoubleField(default_value=1.0)

    LeftFootMiddle1Sy = DoubleField(default_value=1.0)

    LeftFootMiddle1Sz = DoubleField(default_value=1.0)


class LeftFootMiddle1SAttrOperator(
    CompoundAttrOperator[LeftFootMiddle1SPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle1Sx = DoubleField(default_value=1.0)

    LeftFootMiddle1Sy = DoubleField(default_value=1.0)

    LeftFootMiddle1Sz = DoubleField(default_value=1.0)


class LeftFootMiddle1SField(
    CompoundField[LeftFootMiddle1SAttrOperator, LeftFootMiddle1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle1SAttrOperator
    PLUG_CLS = LeftFootMiddle1SPlugOperator

    LeftFootMiddle1Sx = DoubleField(default_value=1.0)

    LeftFootMiddle1Sy = DoubleField(default_value=1.0)

    LeftFootMiddle1Sz = DoubleField(default_value=1.0)


class LeftFootMiddle2TPlugOperator(
    CompoundPlugOperator["LeftFootMiddle2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle2Tx", "LeftFootMiddle2Tx"),
        ("LeftFootMiddle2Ty", "LeftFootMiddle2Ty"),
        ("LeftFootMiddle2Tz", "LeftFootMiddle2Tz"),
    )

    LeftFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle2TAttrOperator(
    CompoundAttrOperator[LeftFootMiddle2TPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle2TField(
    CompoundField[LeftFootMiddle2TAttrOperator, LeftFootMiddle2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle2TAttrOperator
    PLUG_CLS = LeftFootMiddle2TPlugOperator

    LeftFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle2RPlugOperator(
    CompoundPlugOperator["LeftFootMiddle2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle2Rx", "LeftFootMiddle2Rx"),
        ("LeftFootMiddle2Ry", "LeftFootMiddle2Ry"),
        ("LeftFootMiddle2Rz", "LeftFootMiddle2Rz"),
    )

    LeftFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle2RAttrOperator(
    CompoundAttrOperator[LeftFootMiddle2RPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle2RField(
    CompoundField[LeftFootMiddle2RAttrOperator, LeftFootMiddle2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle2RAttrOperator
    PLUG_CLS = LeftFootMiddle2RPlugOperator

    LeftFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle2SPlugOperator(
    CompoundPlugOperator["LeftFootMiddle2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle2Sx", "LeftFootMiddle2Sx"),
        ("LeftFootMiddle2Sy", "LeftFootMiddle2Sy"),
        ("LeftFootMiddle2Sz", "LeftFootMiddle2Sz"),
    )

    LeftFootMiddle2Sx = DoubleField(default_value=1.0)

    LeftFootMiddle2Sy = DoubleField(default_value=1.0)

    LeftFootMiddle2Sz = DoubleField(default_value=1.0)


class LeftFootMiddle2SAttrOperator(
    CompoundAttrOperator[LeftFootMiddle2SPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle2Sx = DoubleField(default_value=1.0)

    LeftFootMiddle2Sy = DoubleField(default_value=1.0)

    LeftFootMiddle2Sz = DoubleField(default_value=1.0)


class LeftFootMiddle2SField(
    CompoundField[LeftFootMiddle2SAttrOperator, LeftFootMiddle2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle2SAttrOperator
    PLUG_CLS = LeftFootMiddle2SPlugOperator

    LeftFootMiddle2Sx = DoubleField(default_value=1.0)

    LeftFootMiddle2Sy = DoubleField(default_value=1.0)

    LeftFootMiddle2Sz = DoubleField(default_value=1.0)


class LeftFootMiddle3TPlugOperator(
    CompoundPlugOperator["LeftFootMiddle3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle3Tx", "LeftFootMiddle3Tx"),
        ("LeftFootMiddle3Ty", "LeftFootMiddle3Ty"),
        ("LeftFootMiddle3Tz", "LeftFootMiddle3Tz"),
    )

    LeftFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle3TAttrOperator(
    CompoundAttrOperator[LeftFootMiddle3TPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle3TField(
    CompoundField[LeftFootMiddle3TAttrOperator, LeftFootMiddle3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle3TAttrOperator
    PLUG_CLS = LeftFootMiddle3TPlugOperator

    LeftFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle3RPlugOperator(
    CompoundPlugOperator["LeftFootMiddle3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle3Rx", "LeftFootMiddle3Rx"),
        ("LeftFootMiddle3Ry", "LeftFootMiddle3Ry"),
        ("LeftFootMiddle3Rz", "LeftFootMiddle3Rz"),
    )

    LeftFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle3RAttrOperator(
    CompoundAttrOperator[LeftFootMiddle3RPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle3RField(
    CompoundField[LeftFootMiddle3RAttrOperator, LeftFootMiddle3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle3RAttrOperator
    PLUG_CLS = LeftFootMiddle3RPlugOperator

    LeftFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle3SPlugOperator(
    CompoundPlugOperator["LeftFootMiddle3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle3Sx", "LeftFootMiddle3Sx"),
        ("LeftFootMiddle3Sy", "LeftFootMiddle3Sy"),
        ("LeftFootMiddle3Sz", "LeftFootMiddle3Sz"),
    )

    LeftFootMiddle3Sx = DoubleField(default_value=1.0)

    LeftFootMiddle3Sy = DoubleField(default_value=1.0)

    LeftFootMiddle3Sz = DoubleField(default_value=1.0)


class LeftFootMiddle3SAttrOperator(
    CompoundAttrOperator[LeftFootMiddle3SPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle3Sx = DoubleField(default_value=1.0)

    LeftFootMiddle3Sy = DoubleField(default_value=1.0)

    LeftFootMiddle3Sz = DoubleField(default_value=1.0)


class LeftFootMiddle3SField(
    CompoundField[LeftFootMiddle3SAttrOperator, LeftFootMiddle3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle3SAttrOperator
    PLUG_CLS = LeftFootMiddle3SPlugOperator

    LeftFootMiddle3Sx = DoubleField(default_value=1.0)

    LeftFootMiddle3Sy = DoubleField(default_value=1.0)

    LeftFootMiddle3Sz = DoubleField(default_value=1.0)


class LeftFootMiddle4TPlugOperator(
    CompoundPlugOperator["LeftFootMiddle4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle4Tx", "LeftFootMiddle4Tx"),
        ("LeftFootMiddle4Ty", "LeftFootMiddle4Ty"),
        ("LeftFootMiddle4Tz", "LeftFootMiddle4Tz"),
    )

    LeftFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle4TAttrOperator(
    CompoundAttrOperator[LeftFootMiddle4TPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle4TField(
    CompoundField[LeftFootMiddle4TAttrOperator, LeftFootMiddle4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle4TAttrOperator
    PLUG_CLS = LeftFootMiddle4TPlugOperator

    LeftFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    LeftFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class LeftFootMiddle4RPlugOperator(
    CompoundPlugOperator["LeftFootMiddle4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle4Rx", "LeftFootMiddle4Rx"),
        ("LeftFootMiddle4Ry", "LeftFootMiddle4Ry"),
        ("LeftFootMiddle4Rz", "LeftFootMiddle4Rz"),
    )

    LeftFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle4RAttrOperator(
    CompoundAttrOperator[LeftFootMiddle4RPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle4RField(
    CompoundField[LeftFootMiddle4RAttrOperator, LeftFootMiddle4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle4RAttrOperator
    PLUG_CLS = LeftFootMiddle4RPlugOperator

    LeftFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    LeftFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class LeftFootMiddle4SPlugOperator(
    CompoundPlugOperator["LeftFootMiddle4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootMiddle4Sx", "LeftFootMiddle4Sx"),
        ("LeftFootMiddle4Sy", "LeftFootMiddle4Sy"),
        ("LeftFootMiddle4Sz", "LeftFootMiddle4Sz"),
    )

    LeftFootMiddle4Sx = DoubleField(default_value=1.0)

    LeftFootMiddle4Sy = DoubleField(default_value=1.0)

    LeftFootMiddle4Sz = DoubleField(default_value=1.0)


class LeftFootMiddle4SAttrOperator(
    CompoundAttrOperator[LeftFootMiddle4SPlugOperator]
):
    __slots__ = ()

    LeftFootMiddle4Sx = DoubleField(default_value=1.0)

    LeftFootMiddle4Sy = DoubleField(default_value=1.0)

    LeftFootMiddle4Sz = DoubleField(default_value=1.0)


class LeftFootMiddle4SField(
    CompoundField[LeftFootMiddle4SAttrOperator, LeftFootMiddle4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootMiddle4SAttrOperator
    PLUG_CLS = LeftFootMiddle4SPlugOperator

    LeftFootMiddle4Sx = DoubleField(default_value=1.0)

    LeftFootMiddle4Sy = DoubleField(default_value=1.0)

    LeftFootMiddle4Sz = DoubleField(default_value=1.0)


class LeftFootRing1TPlugOperator(
    CompoundPlugOperator["LeftFootRing1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing1Tx", "LeftFootRing1Tx"),
        ("LeftFootRing1Ty", "LeftFootRing1Ty"),
        ("LeftFootRing1Tz", "LeftFootRing1Tz"),
    )

    LeftFootRing1Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing1Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing1Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing1TAttrOperator(
    CompoundAttrOperator[LeftFootRing1TPlugOperator]
):
    __slots__ = ()

    LeftFootRing1Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing1Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing1Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing1TField(
    CompoundField[LeftFootRing1TAttrOperator, LeftFootRing1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing1TAttrOperator
    PLUG_CLS = LeftFootRing1TPlugOperator

    LeftFootRing1Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing1Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing1Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing1RPlugOperator(
    CompoundPlugOperator["LeftFootRing1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing1Rx", "LeftFootRing1Rx"),
        ("LeftFootRing1Ry", "LeftFootRing1Ry"),
        ("LeftFootRing1Rz", "LeftFootRing1Rz"),
    )

    LeftFootRing1Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing1Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing1Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing1RAttrOperator(
    CompoundAttrOperator[LeftFootRing1RPlugOperator]
):
    __slots__ = ()

    LeftFootRing1Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing1Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing1Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing1RField(
    CompoundField[LeftFootRing1RAttrOperator, LeftFootRing1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing1RAttrOperator
    PLUG_CLS = LeftFootRing1RPlugOperator

    LeftFootRing1Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing1Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing1Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing1SPlugOperator(
    CompoundPlugOperator["LeftFootRing1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing1Sx", "LeftFootRing1Sx"),
        ("LeftFootRing1Sy", "LeftFootRing1Sy"),
        ("LeftFootRing1Sz", "LeftFootRing1Sz"),
    )

    LeftFootRing1Sx = DoubleField(default_value=1.0)

    LeftFootRing1Sy = DoubleField(default_value=1.0)

    LeftFootRing1Sz = DoubleField(default_value=1.0)


class LeftFootRing1SAttrOperator(
    CompoundAttrOperator[LeftFootRing1SPlugOperator]
):
    __slots__ = ()

    LeftFootRing1Sx = DoubleField(default_value=1.0)

    LeftFootRing1Sy = DoubleField(default_value=1.0)

    LeftFootRing1Sz = DoubleField(default_value=1.0)


class LeftFootRing1SField(
    CompoundField[LeftFootRing1SAttrOperator, LeftFootRing1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing1SAttrOperator
    PLUG_CLS = LeftFootRing1SPlugOperator

    LeftFootRing1Sx = DoubleField(default_value=1.0)

    LeftFootRing1Sy = DoubleField(default_value=1.0)

    LeftFootRing1Sz = DoubleField(default_value=1.0)


class LeftFootRing2TPlugOperator(
    CompoundPlugOperator["LeftFootRing2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing2Tx", "LeftFootRing2Tx"),
        ("LeftFootRing2Ty", "LeftFootRing2Ty"),
        ("LeftFootRing2Tz", "LeftFootRing2Tz"),
    )

    LeftFootRing2Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing2Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing2Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing2TAttrOperator(
    CompoundAttrOperator[LeftFootRing2TPlugOperator]
):
    __slots__ = ()

    LeftFootRing2Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing2Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing2Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing2TField(
    CompoundField[LeftFootRing2TAttrOperator, LeftFootRing2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing2TAttrOperator
    PLUG_CLS = LeftFootRing2TPlugOperator

    LeftFootRing2Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing2Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing2Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing2RPlugOperator(
    CompoundPlugOperator["LeftFootRing2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing2Rx", "LeftFootRing2Rx"),
        ("LeftFootRing2Ry", "LeftFootRing2Ry"),
        ("LeftFootRing2Rz", "LeftFootRing2Rz"),
    )

    LeftFootRing2Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing2Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing2Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing2RAttrOperator(
    CompoundAttrOperator[LeftFootRing2RPlugOperator]
):
    __slots__ = ()

    LeftFootRing2Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing2Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing2Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing2RField(
    CompoundField[LeftFootRing2RAttrOperator, LeftFootRing2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing2RAttrOperator
    PLUG_CLS = LeftFootRing2RPlugOperator

    LeftFootRing2Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing2Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing2Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing2SPlugOperator(
    CompoundPlugOperator["LeftFootRing2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing2Sx", "LeftFootRing2Sx"),
        ("LeftFootRing2Sy", "LeftFootRing2Sy"),
        ("LeftFootRing2Sz", "LeftFootRing2Sz"),
    )

    LeftFootRing2Sx = DoubleField(default_value=1.0)

    LeftFootRing2Sy = DoubleField(default_value=1.0)

    LeftFootRing2Sz = DoubleField(default_value=1.0)


class LeftFootRing2SAttrOperator(
    CompoundAttrOperator[LeftFootRing2SPlugOperator]
):
    __slots__ = ()

    LeftFootRing2Sx = DoubleField(default_value=1.0)

    LeftFootRing2Sy = DoubleField(default_value=1.0)

    LeftFootRing2Sz = DoubleField(default_value=1.0)


class LeftFootRing2SField(
    CompoundField[LeftFootRing2SAttrOperator, LeftFootRing2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing2SAttrOperator
    PLUG_CLS = LeftFootRing2SPlugOperator

    LeftFootRing2Sx = DoubleField(default_value=1.0)

    LeftFootRing2Sy = DoubleField(default_value=1.0)

    LeftFootRing2Sz = DoubleField(default_value=1.0)


class LeftFootRing3TPlugOperator(
    CompoundPlugOperator["LeftFootRing3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing3Tx", "LeftFootRing3Tx"),
        ("LeftFootRing3Ty", "LeftFootRing3Ty"),
        ("LeftFootRing3Tz", "LeftFootRing3Tz"),
    )

    LeftFootRing3Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing3Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing3Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing3TAttrOperator(
    CompoundAttrOperator[LeftFootRing3TPlugOperator]
):
    __slots__ = ()

    LeftFootRing3Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing3Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing3Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing3TField(
    CompoundField[LeftFootRing3TAttrOperator, LeftFootRing3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing3TAttrOperator
    PLUG_CLS = LeftFootRing3TPlugOperator

    LeftFootRing3Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing3Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing3Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing3RPlugOperator(
    CompoundPlugOperator["LeftFootRing3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing3Rx", "LeftFootRing3Rx"),
        ("LeftFootRing3Ry", "LeftFootRing3Ry"),
        ("LeftFootRing3Rz", "LeftFootRing3Rz"),
    )

    LeftFootRing3Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing3Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing3Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing3RAttrOperator(
    CompoundAttrOperator[LeftFootRing3RPlugOperator]
):
    __slots__ = ()

    LeftFootRing3Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing3Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing3Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing3RField(
    CompoundField[LeftFootRing3RAttrOperator, LeftFootRing3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing3RAttrOperator
    PLUG_CLS = LeftFootRing3RPlugOperator

    LeftFootRing3Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing3Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing3Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing3SPlugOperator(
    CompoundPlugOperator["LeftFootRing3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing3Sx", "LeftFootRing3Sx"),
        ("LeftFootRing3Sy", "LeftFootRing3Sy"),
        ("LeftFootRing3Sz", "LeftFootRing3Sz"),
    )

    LeftFootRing3Sx = DoubleField(default_value=1.0)

    LeftFootRing3Sy = DoubleField(default_value=1.0)

    LeftFootRing3Sz = DoubleField(default_value=1.0)


class LeftFootRing3SAttrOperator(
    CompoundAttrOperator[LeftFootRing3SPlugOperator]
):
    __slots__ = ()

    LeftFootRing3Sx = DoubleField(default_value=1.0)

    LeftFootRing3Sy = DoubleField(default_value=1.0)

    LeftFootRing3Sz = DoubleField(default_value=1.0)


class LeftFootRing3SField(
    CompoundField[LeftFootRing3SAttrOperator, LeftFootRing3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing3SAttrOperator
    PLUG_CLS = LeftFootRing3SPlugOperator

    LeftFootRing3Sx = DoubleField(default_value=1.0)

    LeftFootRing3Sy = DoubleField(default_value=1.0)

    LeftFootRing3Sz = DoubleField(default_value=1.0)


class LeftFootRing4TPlugOperator(
    CompoundPlugOperator["LeftFootRing4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing4Tx", "LeftFootRing4Tx"),
        ("LeftFootRing4Ty", "LeftFootRing4Ty"),
        ("LeftFootRing4Tz", "LeftFootRing4Tz"),
    )

    LeftFootRing4Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing4Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing4Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing4TAttrOperator(
    CompoundAttrOperator[LeftFootRing4TPlugOperator]
):
    __slots__ = ()

    LeftFootRing4Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing4Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing4Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing4TField(
    CompoundField[LeftFootRing4TAttrOperator, LeftFootRing4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing4TAttrOperator
    PLUG_CLS = LeftFootRing4TPlugOperator

    LeftFootRing4Tx = DoubleLinearField(default_value=0.0)

    LeftFootRing4Ty = DoubleLinearField(default_value=0.0)

    LeftFootRing4Tz = DoubleLinearField(default_value=0.0)


class LeftFootRing4RPlugOperator(
    CompoundPlugOperator["LeftFootRing4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing4Rx", "LeftFootRing4Rx"),
        ("LeftFootRing4Ry", "LeftFootRing4Ry"),
        ("LeftFootRing4Rz", "LeftFootRing4Rz"),
    )

    LeftFootRing4Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing4Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing4Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing4RAttrOperator(
    CompoundAttrOperator[LeftFootRing4RPlugOperator]
):
    __slots__ = ()

    LeftFootRing4Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing4Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing4Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing4RField(
    CompoundField[LeftFootRing4RAttrOperator, LeftFootRing4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing4RAttrOperator
    PLUG_CLS = LeftFootRing4RPlugOperator

    LeftFootRing4Rx = DoubleAngleField(default_value=0.0)

    LeftFootRing4Ry = DoubleAngleField(default_value=0.0)

    LeftFootRing4Rz = DoubleAngleField(default_value=0.0)


class LeftFootRing4SPlugOperator(
    CompoundPlugOperator["LeftFootRing4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootRing4Sx", "LeftFootRing4Sx"),
        ("LeftFootRing4Sy", "LeftFootRing4Sy"),
        ("LeftFootRing4Sz", "LeftFootRing4Sz"),
    )

    LeftFootRing4Sx = DoubleField(default_value=1.0)

    LeftFootRing4Sy = DoubleField(default_value=1.0)

    LeftFootRing4Sz = DoubleField(default_value=1.0)


class LeftFootRing4SAttrOperator(
    CompoundAttrOperator[LeftFootRing4SPlugOperator]
):
    __slots__ = ()

    LeftFootRing4Sx = DoubleField(default_value=1.0)

    LeftFootRing4Sy = DoubleField(default_value=1.0)

    LeftFootRing4Sz = DoubleField(default_value=1.0)


class LeftFootRing4SField(
    CompoundField[LeftFootRing4SAttrOperator, LeftFootRing4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootRing4SAttrOperator
    PLUG_CLS = LeftFootRing4SPlugOperator

    LeftFootRing4Sx = DoubleField(default_value=1.0)

    LeftFootRing4Sy = DoubleField(default_value=1.0)

    LeftFootRing4Sz = DoubleField(default_value=1.0)


class LeftFootPinky1TPlugOperator(
    CompoundPlugOperator["LeftFootPinky1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky1Tx", "LeftFootPinky1Tx"),
        ("LeftFootPinky1Ty", "LeftFootPinky1Ty"),
        ("LeftFootPinky1Tz", "LeftFootPinky1Tz"),
    )

    LeftFootPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky1TAttrOperator(
    CompoundAttrOperator[LeftFootPinky1TPlugOperator]
):
    __slots__ = ()

    LeftFootPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky1TField(
    CompoundField[LeftFootPinky1TAttrOperator, LeftFootPinky1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky1TAttrOperator
    PLUG_CLS = LeftFootPinky1TPlugOperator

    LeftFootPinky1Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky1Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky1RPlugOperator(
    CompoundPlugOperator["LeftFootPinky1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky1Rx", "LeftFootPinky1Rx"),
        ("LeftFootPinky1Ry", "LeftFootPinky1Ry"),
        ("LeftFootPinky1Rz", "LeftFootPinky1Rz"),
    )

    LeftFootPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky1RAttrOperator(
    CompoundAttrOperator[LeftFootPinky1RPlugOperator]
):
    __slots__ = ()

    LeftFootPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky1RField(
    CompoundField[LeftFootPinky1RAttrOperator, LeftFootPinky1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky1RAttrOperator
    PLUG_CLS = LeftFootPinky1RPlugOperator

    LeftFootPinky1Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky1Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky1SPlugOperator(
    CompoundPlugOperator["LeftFootPinky1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky1Sx", "LeftFootPinky1Sx"),
        ("LeftFootPinky1Sy", "LeftFootPinky1Sy"),
        ("LeftFootPinky1Sz", "LeftFootPinky1Sz"),
    )

    LeftFootPinky1Sx = DoubleField(default_value=1.0)

    LeftFootPinky1Sy = DoubleField(default_value=1.0)

    LeftFootPinky1Sz = DoubleField(default_value=1.0)


class LeftFootPinky1SAttrOperator(
    CompoundAttrOperator[LeftFootPinky1SPlugOperator]
):
    __slots__ = ()

    LeftFootPinky1Sx = DoubleField(default_value=1.0)

    LeftFootPinky1Sy = DoubleField(default_value=1.0)

    LeftFootPinky1Sz = DoubleField(default_value=1.0)


class LeftFootPinky1SField(
    CompoundField[LeftFootPinky1SAttrOperator, LeftFootPinky1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky1SAttrOperator
    PLUG_CLS = LeftFootPinky1SPlugOperator

    LeftFootPinky1Sx = DoubleField(default_value=1.0)

    LeftFootPinky1Sy = DoubleField(default_value=1.0)

    LeftFootPinky1Sz = DoubleField(default_value=1.0)


class LeftFootPinky2TPlugOperator(
    CompoundPlugOperator["LeftFootPinky2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky2Tx", "LeftFootPinky2Tx"),
        ("LeftFootPinky2Ty", "LeftFootPinky2Ty"),
        ("LeftFootPinky2Tz", "LeftFootPinky2Tz"),
    )

    LeftFootPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky2TAttrOperator(
    CompoundAttrOperator[LeftFootPinky2TPlugOperator]
):
    __slots__ = ()

    LeftFootPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky2TField(
    CompoundField[LeftFootPinky2TAttrOperator, LeftFootPinky2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky2TAttrOperator
    PLUG_CLS = LeftFootPinky2TPlugOperator

    LeftFootPinky2Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky2Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky2RPlugOperator(
    CompoundPlugOperator["LeftFootPinky2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky2Rx", "LeftFootPinky2Rx"),
        ("LeftFootPinky2Ry", "LeftFootPinky2Ry"),
        ("LeftFootPinky2Rz", "LeftFootPinky2Rz"),
    )

    LeftFootPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky2RAttrOperator(
    CompoundAttrOperator[LeftFootPinky2RPlugOperator]
):
    __slots__ = ()

    LeftFootPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky2RField(
    CompoundField[LeftFootPinky2RAttrOperator, LeftFootPinky2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky2RAttrOperator
    PLUG_CLS = LeftFootPinky2RPlugOperator

    LeftFootPinky2Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky2Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky2SPlugOperator(
    CompoundPlugOperator["LeftFootPinky2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky2Sx", "LeftFootPinky2Sx"),
        ("LeftFootPinky2Sy", "LeftFootPinky2Sy"),
        ("LeftFootPinky2Sz", "LeftFootPinky2Sz"),
    )

    LeftFootPinky2Sx = DoubleField(default_value=1.0)

    LeftFootPinky2Sy = DoubleField(default_value=1.0)

    LeftFootPinky2Sz = DoubleField(default_value=1.0)


class LeftFootPinky2SAttrOperator(
    CompoundAttrOperator[LeftFootPinky2SPlugOperator]
):
    __slots__ = ()

    LeftFootPinky2Sx = DoubleField(default_value=1.0)

    LeftFootPinky2Sy = DoubleField(default_value=1.0)

    LeftFootPinky2Sz = DoubleField(default_value=1.0)


class LeftFootPinky2SField(
    CompoundField[LeftFootPinky2SAttrOperator, LeftFootPinky2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky2SAttrOperator
    PLUG_CLS = LeftFootPinky2SPlugOperator

    LeftFootPinky2Sx = DoubleField(default_value=1.0)

    LeftFootPinky2Sy = DoubleField(default_value=1.0)

    LeftFootPinky2Sz = DoubleField(default_value=1.0)


class LeftFootPinky3TPlugOperator(
    CompoundPlugOperator["LeftFootPinky3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky3Tx", "LeftFootPinky3Tx"),
        ("LeftFootPinky3Ty", "LeftFootPinky3Ty"),
        ("LeftFootPinky3Tz", "LeftFootPinky3Tz"),
    )

    LeftFootPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky3TAttrOperator(
    CompoundAttrOperator[LeftFootPinky3TPlugOperator]
):
    __slots__ = ()

    LeftFootPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky3TField(
    CompoundField[LeftFootPinky3TAttrOperator, LeftFootPinky3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky3TAttrOperator
    PLUG_CLS = LeftFootPinky3TPlugOperator

    LeftFootPinky3Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky3Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky3RPlugOperator(
    CompoundPlugOperator["LeftFootPinky3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky3Rx", "LeftFootPinky3Rx"),
        ("LeftFootPinky3Ry", "LeftFootPinky3Ry"),
        ("LeftFootPinky3Rz", "LeftFootPinky3Rz"),
    )

    LeftFootPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky3RAttrOperator(
    CompoundAttrOperator[LeftFootPinky3RPlugOperator]
):
    __slots__ = ()

    LeftFootPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky3RField(
    CompoundField[LeftFootPinky3RAttrOperator, LeftFootPinky3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky3RAttrOperator
    PLUG_CLS = LeftFootPinky3RPlugOperator

    LeftFootPinky3Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky3Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky3SPlugOperator(
    CompoundPlugOperator["LeftFootPinky3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky3Sx", "LeftFootPinky3Sx"),
        ("LeftFootPinky3Sy", "LeftFootPinky3Sy"),
        ("LeftFootPinky3Sz", "LeftFootPinky3Sz"),
    )

    LeftFootPinky3Sx = DoubleField(default_value=1.0)

    LeftFootPinky3Sy = DoubleField(default_value=1.0)

    LeftFootPinky3Sz = DoubleField(default_value=1.0)


class LeftFootPinky3SAttrOperator(
    CompoundAttrOperator[LeftFootPinky3SPlugOperator]
):
    __slots__ = ()

    LeftFootPinky3Sx = DoubleField(default_value=1.0)

    LeftFootPinky3Sy = DoubleField(default_value=1.0)

    LeftFootPinky3Sz = DoubleField(default_value=1.0)


class LeftFootPinky3SField(
    CompoundField[LeftFootPinky3SAttrOperator, LeftFootPinky3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky3SAttrOperator
    PLUG_CLS = LeftFootPinky3SPlugOperator

    LeftFootPinky3Sx = DoubleField(default_value=1.0)

    LeftFootPinky3Sy = DoubleField(default_value=1.0)

    LeftFootPinky3Sz = DoubleField(default_value=1.0)


class LeftFootPinky4TPlugOperator(
    CompoundPlugOperator["LeftFootPinky4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky4Tx", "LeftFootPinky4Tx"),
        ("LeftFootPinky4Ty", "LeftFootPinky4Ty"),
        ("LeftFootPinky4Tz", "LeftFootPinky4Tz"),
    )

    LeftFootPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky4TAttrOperator(
    CompoundAttrOperator[LeftFootPinky4TPlugOperator]
):
    __slots__ = ()

    LeftFootPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky4TField(
    CompoundField[LeftFootPinky4TAttrOperator, LeftFootPinky4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky4TAttrOperator
    PLUG_CLS = LeftFootPinky4TPlugOperator

    LeftFootPinky4Tx = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Ty = DoubleLinearField(default_value=0.0)

    LeftFootPinky4Tz = DoubleLinearField(default_value=0.0)


class LeftFootPinky4RPlugOperator(
    CompoundPlugOperator["LeftFootPinky4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky4Rx", "LeftFootPinky4Rx"),
        ("LeftFootPinky4Ry", "LeftFootPinky4Ry"),
        ("LeftFootPinky4Rz", "LeftFootPinky4Rz"),
    )

    LeftFootPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky4RAttrOperator(
    CompoundAttrOperator[LeftFootPinky4RPlugOperator]
):
    __slots__ = ()

    LeftFootPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky4RField(
    CompoundField[LeftFootPinky4RAttrOperator, LeftFootPinky4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky4RAttrOperator
    PLUG_CLS = LeftFootPinky4RPlugOperator

    LeftFootPinky4Rx = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Ry = DoubleAngleField(default_value=0.0)

    LeftFootPinky4Rz = DoubleAngleField(default_value=0.0)


class LeftFootPinky4SPlugOperator(
    CompoundPlugOperator["LeftFootPinky4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootPinky4Sx", "LeftFootPinky4Sx"),
        ("LeftFootPinky4Sy", "LeftFootPinky4Sy"),
        ("LeftFootPinky4Sz", "LeftFootPinky4Sz"),
    )

    LeftFootPinky4Sx = DoubleField(default_value=1.0)

    LeftFootPinky4Sy = DoubleField(default_value=1.0)

    LeftFootPinky4Sz = DoubleField(default_value=1.0)


class LeftFootPinky4SAttrOperator(
    CompoundAttrOperator[LeftFootPinky4SPlugOperator]
):
    __slots__ = ()

    LeftFootPinky4Sx = DoubleField(default_value=1.0)

    LeftFootPinky4Sy = DoubleField(default_value=1.0)

    LeftFootPinky4Sz = DoubleField(default_value=1.0)


class LeftFootPinky4SField(
    CompoundField[LeftFootPinky4SAttrOperator, LeftFootPinky4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootPinky4SAttrOperator
    PLUG_CLS = LeftFootPinky4SPlugOperator

    LeftFootPinky4Sx = DoubleField(default_value=1.0)

    LeftFootPinky4Sy = DoubleField(default_value=1.0)

    LeftFootPinky4Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger1TPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger1Tx", "LeftFootExtraFinger1Tx"),
        ("LeftFootExtraFinger1Ty", "LeftFootExtraFinger1Ty"),
        ("LeftFootExtraFinger1Tz", "LeftFootExtraFinger1Tz"),
    )

    LeftFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger1TAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger1TPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger1TField(
    CompoundField[LeftFootExtraFinger1TAttrOperator, LeftFootExtraFinger1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger1TAttrOperator
    PLUG_CLS = LeftFootExtraFinger1TPlugOperator

    LeftFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger1RPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger1Rx", "LeftFootExtraFinger1Rx"),
        ("LeftFootExtraFinger1Ry", "LeftFootExtraFinger1Ry"),
        ("LeftFootExtraFinger1Rz", "LeftFootExtraFinger1Rz"),
    )

    LeftFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger1RAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger1RPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger1RField(
    CompoundField[LeftFootExtraFinger1RAttrOperator, LeftFootExtraFinger1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger1RAttrOperator
    PLUG_CLS = LeftFootExtraFinger1RPlugOperator

    LeftFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger1SPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger1Sx", "LeftFootExtraFinger1Sx"),
        ("LeftFootExtraFinger1Sy", "LeftFootExtraFinger1Sy"),
        ("LeftFootExtraFinger1Sz", "LeftFootExtraFinger1Sz"),
    )

    LeftFootExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger1SAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger1SPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger1SField(
    CompoundField[LeftFootExtraFinger1SAttrOperator, LeftFootExtraFinger1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger1SAttrOperator
    PLUG_CLS = LeftFootExtraFinger1SPlugOperator

    LeftFootExtraFinger1Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger1Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger2TPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger2Tx", "LeftFootExtraFinger2Tx"),
        ("LeftFootExtraFinger2Ty", "LeftFootExtraFinger2Ty"),
        ("LeftFootExtraFinger2Tz", "LeftFootExtraFinger2Tz"),
    )

    LeftFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger2TAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger2TPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger2TField(
    CompoundField[LeftFootExtraFinger2TAttrOperator, LeftFootExtraFinger2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger2TAttrOperator
    PLUG_CLS = LeftFootExtraFinger2TPlugOperator

    LeftFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger2RPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger2Rx", "LeftFootExtraFinger2Rx"),
        ("LeftFootExtraFinger2Ry", "LeftFootExtraFinger2Ry"),
        ("LeftFootExtraFinger2Rz", "LeftFootExtraFinger2Rz"),
    )

    LeftFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger2RAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger2RPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger2RField(
    CompoundField[LeftFootExtraFinger2RAttrOperator, LeftFootExtraFinger2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger2RAttrOperator
    PLUG_CLS = LeftFootExtraFinger2RPlugOperator

    LeftFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger2SPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger2Sx", "LeftFootExtraFinger2Sx"),
        ("LeftFootExtraFinger2Sy", "LeftFootExtraFinger2Sy"),
        ("LeftFootExtraFinger2Sz", "LeftFootExtraFinger2Sz"),
    )

    LeftFootExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger2SAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger2SPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger2SField(
    CompoundField[LeftFootExtraFinger2SAttrOperator, LeftFootExtraFinger2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger2SAttrOperator
    PLUG_CLS = LeftFootExtraFinger2SPlugOperator

    LeftFootExtraFinger2Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger2Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger3TPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger3Tx", "LeftFootExtraFinger3Tx"),
        ("LeftFootExtraFinger3Ty", "LeftFootExtraFinger3Ty"),
        ("LeftFootExtraFinger3Tz", "LeftFootExtraFinger3Tz"),
    )

    LeftFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger3TAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger3TPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger3TField(
    CompoundField[LeftFootExtraFinger3TAttrOperator, LeftFootExtraFinger3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger3TAttrOperator
    PLUG_CLS = LeftFootExtraFinger3TPlugOperator

    LeftFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger3RPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger3Rx", "LeftFootExtraFinger3Rx"),
        ("LeftFootExtraFinger3Ry", "LeftFootExtraFinger3Ry"),
        ("LeftFootExtraFinger3Rz", "LeftFootExtraFinger3Rz"),
    )

    LeftFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger3RAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger3RPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger3RField(
    CompoundField[LeftFootExtraFinger3RAttrOperator, LeftFootExtraFinger3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger3RAttrOperator
    PLUG_CLS = LeftFootExtraFinger3RPlugOperator

    LeftFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger3SPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger3Sx", "LeftFootExtraFinger3Sx"),
        ("LeftFootExtraFinger3Sy", "LeftFootExtraFinger3Sy"),
        ("LeftFootExtraFinger3Sz", "LeftFootExtraFinger3Sz"),
    )

    LeftFootExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger3SAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger3SPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger3SField(
    CompoundField[LeftFootExtraFinger3SAttrOperator, LeftFootExtraFinger3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger3SAttrOperator
    PLUG_CLS = LeftFootExtraFinger3SPlugOperator

    LeftFootExtraFinger3Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger3Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger4TPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger4Tx", "LeftFootExtraFinger4Tx"),
        ("LeftFootExtraFinger4Ty", "LeftFootExtraFinger4Ty"),
        ("LeftFootExtraFinger4Tz", "LeftFootExtraFinger4Tz"),
    )

    LeftFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger4TAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger4TPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger4TField(
    CompoundField[LeftFootExtraFinger4TAttrOperator, LeftFootExtraFinger4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger4TAttrOperator
    PLUG_CLS = LeftFootExtraFinger4TPlugOperator

    LeftFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    LeftFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class LeftFootExtraFinger4RPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger4Rx", "LeftFootExtraFinger4Rx"),
        ("LeftFootExtraFinger4Ry", "LeftFootExtraFinger4Ry"),
        ("LeftFootExtraFinger4Rz", "LeftFootExtraFinger4Rz"),
    )

    LeftFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger4RAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger4RPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger4RField(
    CompoundField[LeftFootExtraFinger4RAttrOperator, LeftFootExtraFinger4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger4RAttrOperator
    PLUG_CLS = LeftFootExtraFinger4RPlugOperator

    LeftFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    LeftFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class LeftFootExtraFinger4SPlugOperator(
    CompoundPlugOperator["LeftFootExtraFinger4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftFootExtraFinger4Sx", "LeftFootExtraFinger4Sx"),
        ("LeftFootExtraFinger4Sy", "LeftFootExtraFinger4Sy"),
        ("LeftFootExtraFinger4Sz", "LeftFootExtraFinger4Sz"),
    )

    LeftFootExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger4SAttrOperator(
    CompoundAttrOperator[LeftFootExtraFinger4SPlugOperator]
):
    __slots__ = ()

    LeftFootExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftFootExtraFinger4SField(
    CompoundField[LeftFootExtraFinger4SAttrOperator, LeftFootExtraFinger4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftFootExtraFinger4SAttrOperator
    PLUG_CLS = LeftFootExtraFinger4SPlugOperator

    LeftFootExtraFinger4Sx = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sy = DoubleField(default_value=1.0)

    LeftFootExtraFinger4Sz = DoubleField(default_value=1.0)


class RightFootThumb1TPlugOperator(
    CompoundPlugOperator["RightFootThumb1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb1Tx", "RightFootThumb1Tx"),
        ("RightFootThumb1Ty", "RightFootThumb1Ty"),
        ("RightFootThumb1Tz", "RightFootThumb1Tz"),
    )

    RightFootThumb1Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb1Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb1Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb1TAttrOperator(
    CompoundAttrOperator[RightFootThumb1TPlugOperator]
):
    __slots__ = ()

    RightFootThumb1Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb1Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb1Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb1TField(
    CompoundField[RightFootThumb1TAttrOperator, RightFootThumb1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb1TAttrOperator
    PLUG_CLS = RightFootThumb1TPlugOperator

    RightFootThumb1Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb1Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb1Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb1RPlugOperator(
    CompoundPlugOperator["RightFootThumb1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb1Rx", "RightFootThumb1Rx"),
        ("RightFootThumb1Ry", "RightFootThumb1Ry"),
        ("RightFootThumb1Rz", "RightFootThumb1Rz"),
    )

    RightFootThumb1Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb1Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb1Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb1RAttrOperator(
    CompoundAttrOperator[RightFootThumb1RPlugOperator]
):
    __slots__ = ()

    RightFootThumb1Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb1Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb1Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb1RField(
    CompoundField[RightFootThumb1RAttrOperator, RightFootThumb1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb1RAttrOperator
    PLUG_CLS = RightFootThumb1RPlugOperator

    RightFootThumb1Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb1Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb1Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb1SPlugOperator(
    CompoundPlugOperator["RightFootThumb1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb1Sx", "RightFootThumb1Sx"),
        ("RightFootThumb1Sy", "RightFootThumb1Sy"),
        ("RightFootThumb1Sz", "RightFootThumb1Sz"),
    )

    RightFootThumb1Sx = DoubleField(default_value=1.0)

    RightFootThumb1Sy = DoubleField(default_value=1.0)

    RightFootThumb1Sz = DoubleField(default_value=1.0)


class RightFootThumb1SAttrOperator(
    CompoundAttrOperator[RightFootThumb1SPlugOperator]
):
    __slots__ = ()

    RightFootThumb1Sx = DoubleField(default_value=1.0)

    RightFootThumb1Sy = DoubleField(default_value=1.0)

    RightFootThumb1Sz = DoubleField(default_value=1.0)


class RightFootThumb1SField(
    CompoundField[RightFootThumb1SAttrOperator, RightFootThumb1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb1SAttrOperator
    PLUG_CLS = RightFootThumb1SPlugOperator

    RightFootThumb1Sx = DoubleField(default_value=1.0)

    RightFootThumb1Sy = DoubleField(default_value=1.0)

    RightFootThumb1Sz = DoubleField(default_value=1.0)


class RightFootThumb2TPlugOperator(
    CompoundPlugOperator["RightFootThumb2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb2Tx", "RightFootThumb2Tx"),
        ("RightFootThumb2Ty", "RightFootThumb2Ty"),
        ("RightFootThumb2Tz", "RightFootThumb2Tz"),
    )

    RightFootThumb2Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb2Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb2Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb2TAttrOperator(
    CompoundAttrOperator[RightFootThumb2TPlugOperator]
):
    __slots__ = ()

    RightFootThumb2Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb2Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb2Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb2TField(
    CompoundField[RightFootThumb2TAttrOperator, RightFootThumb2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb2TAttrOperator
    PLUG_CLS = RightFootThumb2TPlugOperator

    RightFootThumb2Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb2Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb2Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb2RPlugOperator(
    CompoundPlugOperator["RightFootThumb2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb2Rx", "RightFootThumb2Rx"),
        ("RightFootThumb2Ry", "RightFootThumb2Ry"),
        ("RightFootThumb2Rz", "RightFootThumb2Rz"),
    )

    RightFootThumb2Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb2Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb2Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb2RAttrOperator(
    CompoundAttrOperator[RightFootThumb2RPlugOperator]
):
    __slots__ = ()

    RightFootThumb2Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb2Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb2Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb2RField(
    CompoundField[RightFootThumb2RAttrOperator, RightFootThumb2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb2RAttrOperator
    PLUG_CLS = RightFootThumb2RPlugOperator

    RightFootThumb2Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb2Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb2Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb2SPlugOperator(
    CompoundPlugOperator["RightFootThumb2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb2Sx", "RightFootThumb2Sx"),
        ("RightFootThumb2Sy", "RightFootThumb2Sy"),
        ("RightFootThumb2Sz", "RightFootThumb2Sz"),
    )

    RightFootThumb2Sx = DoubleField(default_value=1.0)

    RightFootThumb2Sy = DoubleField(default_value=1.0)

    RightFootThumb2Sz = DoubleField(default_value=1.0)


class RightFootThumb2SAttrOperator(
    CompoundAttrOperator[RightFootThumb2SPlugOperator]
):
    __slots__ = ()

    RightFootThumb2Sx = DoubleField(default_value=1.0)

    RightFootThumb2Sy = DoubleField(default_value=1.0)

    RightFootThumb2Sz = DoubleField(default_value=1.0)


class RightFootThumb2SField(
    CompoundField[RightFootThumb2SAttrOperator, RightFootThumb2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb2SAttrOperator
    PLUG_CLS = RightFootThumb2SPlugOperator

    RightFootThumb2Sx = DoubleField(default_value=1.0)

    RightFootThumb2Sy = DoubleField(default_value=1.0)

    RightFootThumb2Sz = DoubleField(default_value=1.0)


class RightFootThumb3TPlugOperator(
    CompoundPlugOperator["RightFootThumb3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb3Tx", "RightFootThumb3Tx"),
        ("RightFootThumb3Ty", "RightFootThumb3Ty"),
        ("RightFootThumb3Tz", "RightFootThumb3Tz"),
    )

    RightFootThumb3Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb3Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb3Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb3TAttrOperator(
    CompoundAttrOperator[RightFootThumb3TPlugOperator]
):
    __slots__ = ()

    RightFootThumb3Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb3Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb3Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb3TField(
    CompoundField[RightFootThumb3TAttrOperator, RightFootThumb3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb3TAttrOperator
    PLUG_CLS = RightFootThumb3TPlugOperator

    RightFootThumb3Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb3Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb3Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb3RPlugOperator(
    CompoundPlugOperator["RightFootThumb3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb3Rx", "RightFootThumb3Rx"),
        ("RightFootThumb3Ry", "RightFootThumb3Ry"),
        ("RightFootThumb3Rz", "RightFootThumb3Rz"),
    )

    RightFootThumb3Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb3Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb3Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb3RAttrOperator(
    CompoundAttrOperator[RightFootThumb3RPlugOperator]
):
    __slots__ = ()

    RightFootThumb3Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb3Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb3Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb3RField(
    CompoundField[RightFootThumb3RAttrOperator, RightFootThumb3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb3RAttrOperator
    PLUG_CLS = RightFootThumb3RPlugOperator

    RightFootThumb3Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb3Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb3Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb3SPlugOperator(
    CompoundPlugOperator["RightFootThumb3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb3Sx", "RightFootThumb3Sx"),
        ("RightFootThumb3Sy", "RightFootThumb3Sy"),
        ("RightFootThumb3Sz", "RightFootThumb3Sz"),
    )

    RightFootThumb3Sx = DoubleField(default_value=1.0)

    RightFootThumb3Sy = DoubleField(default_value=1.0)

    RightFootThumb3Sz = DoubleField(default_value=1.0)


class RightFootThumb3SAttrOperator(
    CompoundAttrOperator[RightFootThumb3SPlugOperator]
):
    __slots__ = ()

    RightFootThumb3Sx = DoubleField(default_value=1.0)

    RightFootThumb3Sy = DoubleField(default_value=1.0)

    RightFootThumb3Sz = DoubleField(default_value=1.0)


class RightFootThumb3SField(
    CompoundField[RightFootThumb3SAttrOperator, RightFootThumb3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb3SAttrOperator
    PLUG_CLS = RightFootThumb3SPlugOperator

    RightFootThumb3Sx = DoubleField(default_value=1.0)

    RightFootThumb3Sy = DoubleField(default_value=1.0)

    RightFootThumb3Sz = DoubleField(default_value=1.0)


class RightFootThumb4TPlugOperator(
    CompoundPlugOperator["RightFootThumb4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb4Tx", "RightFootThumb4Tx"),
        ("RightFootThumb4Ty", "RightFootThumb4Ty"),
        ("RightFootThumb4Tz", "RightFootThumb4Tz"),
    )

    RightFootThumb4Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb4Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb4Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb4TAttrOperator(
    CompoundAttrOperator[RightFootThumb4TPlugOperator]
):
    __slots__ = ()

    RightFootThumb4Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb4Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb4Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb4TField(
    CompoundField[RightFootThumb4TAttrOperator, RightFootThumb4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb4TAttrOperator
    PLUG_CLS = RightFootThumb4TPlugOperator

    RightFootThumb4Tx = DoubleLinearField(default_value=0.0)

    RightFootThumb4Ty = DoubleLinearField(default_value=0.0)

    RightFootThumb4Tz = DoubleLinearField(default_value=0.0)


class RightFootThumb4RPlugOperator(
    CompoundPlugOperator["RightFootThumb4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb4Rx", "RightFootThumb4Rx"),
        ("RightFootThumb4Ry", "RightFootThumb4Ry"),
        ("RightFootThumb4Rz", "RightFootThumb4Rz"),
    )

    RightFootThumb4Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb4Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb4Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb4RAttrOperator(
    CompoundAttrOperator[RightFootThumb4RPlugOperator]
):
    __slots__ = ()

    RightFootThumb4Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb4Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb4Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb4RField(
    CompoundField[RightFootThumb4RAttrOperator, RightFootThumb4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb4RAttrOperator
    PLUG_CLS = RightFootThumb4RPlugOperator

    RightFootThumb4Rx = DoubleAngleField(default_value=0.0)

    RightFootThumb4Ry = DoubleAngleField(default_value=0.0)

    RightFootThumb4Rz = DoubleAngleField(default_value=0.0)


class RightFootThumb4SPlugOperator(
    CompoundPlugOperator["RightFootThumb4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootThumb4Sx", "RightFootThumb4Sx"),
        ("RightFootThumb4Sy", "RightFootThumb4Sy"),
        ("RightFootThumb4Sz", "RightFootThumb4Sz"),
    )

    RightFootThumb4Sx = DoubleField(default_value=1.0)

    RightFootThumb4Sy = DoubleField(default_value=1.0)

    RightFootThumb4Sz = DoubleField(default_value=1.0)


class RightFootThumb4SAttrOperator(
    CompoundAttrOperator[RightFootThumb4SPlugOperator]
):
    __slots__ = ()

    RightFootThumb4Sx = DoubleField(default_value=1.0)

    RightFootThumb4Sy = DoubleField(default_value=1.0)

    RightFootThumb4Sz = DoubleField(default_value=1.0)


class RightFootThumb4SField(
    CompoundField[RightFootThumb4SAttrOperator, RightFootThumb4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootThumb4SAttrOperator
    PLUG_CLS = RightFootThumb4SPlugOperator

    RightFootThumb4Sx = DoubleField(default_value=1.0)

    RightFootThumb4Sy = DoubleField(default_value=1.0)

    RightFootThumb4Sz = DoubleField(default_value=1.0)


class RightFootIndex1TPlugOperator(
    CompoundPlugOperator["RightFootIndex1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex1Tx", "RightFootIndex1Tx"),
        ("RightFootIndex1Ty", "RightFootIndex1Ty"),
        ("RightFootIndex1Tz", "RightFootIndex1Tz"),
    )

    RightFootIndex1Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex1Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex1Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex1TAttrOperator(
    CompoundAttrOperator[RightFootIndex1TPlugOperator]
):
    __slots__ = ()

    RightFootIndex1Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex1Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex1Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex1TField(
    CompoundField[RightFootIndex1TAttrOperator, RightFootIndex1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex1TAttrOperator
    PLUG_CLS = RightFootIndex1TPlugOperator

    RightFootIndex1Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex1Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex1Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex1RPlugOperator(
    CompoundPlugOperator["RightFootIndex1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex1Rx", "RightFootIndex1Rx"),
        ("RightFootIndex1Ry", "RightFootIndex1Ry"),
        ("RightFootIndex1Rz", "RightFootIndex1Rz"),
    )

    RightFootIndex1Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex1Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex1Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex1RAttrOperator(
    CompoundAttrOperator[RightFootIndex1RPlugOperator]
):
    __slots__ = ()

    RightFootIndex1Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex1Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex1Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex1RField(
    CompoundField[RightFootIndex1RAttrOperator, RightFootIndex1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex1RAttrOperator
    PLUG_CLS = RightFootIndex1RPlugOperator

    RightFootIndex1Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex1Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex1Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex1SPlugOperator(
    CompoundPlugOperator["RightFootIndex1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex1Sx", "RightFootIndex1Sx"),
        ("RightFootIndex1Sy", "RightFootIndex1Sy"),
        ("RightFootIndex1Sz", "RightFootIndex1Sz"),
    )

    RightFootIndex1Sx = DoubleField(default_value=1.0)

    RightFootIndex1Sy = DoubleField(default_value=1.0)

    RightFootIndex1Sz = DoubleField(default_value=1.0)


class RightFootIndex1SAttrOperator(
    CompoundAttrOperator[RightFootIndex1SPlugOperator]
):
    __slots__ = ()

    RightFootIndex1Sx = DoubleField(default_value=1.0)

    RightFootIndex1Sy = DoubleField(default_value=1.0)

    RightFootIndex1Sz = DoubleField(default_value=1.0)


class RightFootIndex1SField(
    CompoundField[RightFootIndex1SAttrOperator, RightFootIndex1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex1SAttrOperator
    PLUG_CLS = RightFootIndex1SPlugOperator

    RightFootIndex1Sx = DoubleField(default_value=1.0)

    RightFootIndex1Sy = DoubleField(default_value=1.0)

    RightFootIndex1Sz = DoubleField(default_value=1.0)


class RightFootIndex2TPlugOperator(
    CompoundPlugOperator["RightFootIndex2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex2Tx", "RightFootIndex2Tx"),
        ("RightFootIndex2Ty", "RightFootIndex2Ty"),
        ("RightFootIndex2Tz", "RightFootIndex2Tz"),
    )

    RightFootIndex2Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex2Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex2Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex2TAttrOperator(
    CompoundAttrOperator[RightFootIndex2TPlugOperator]
):
    __slots__ = ()

    RightFootIndex2Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex2Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex2Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex2TField(
    CompoundField[RightFootIndex2TAttrOperator, RightFootIndex2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex2TAttrOperator
    PLUG_CLS = RightFootIndex2TPlugOperator

    RightFootIndex2Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex2Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex2Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex2RPlugOperator(
    CompoundPlugOperator["RightFootIndex2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex2Rx", "RightFootIndex2Rx"),
        ("RightFootIndex2Ry", "RightFootIndex2Ry"),
        ("RightFootIndex2Rz", "RightFootIndex2Rz"),
    )

    RightFootIndex2Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex2Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex2Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex2RAttrOperator(
    CompoundAttrOperator[RightFootIndex2RPlugOperator]
):
    __slots__ = ()

    RightFootIndex2Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex2Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex2Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex2RField(
    CompoundField[RightFootIndex2RAttrOperator, RightFootIndex2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex2RAttrOperator
    PLUG_CLS = RightFootIndex2RPlugOperator

    RightFootIndex2Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex2Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex2Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex2SPlugOperator(
    CompoundPlugOperator["RightFootIndex2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex2Sx", "RightFootIndex2Sx"),
        ("RightFootIndex2Sy", "RightFootIndex2Sy"),
        ("RightFootIndex2Sz", "RightFootIndex2Sz"),
    )

    RightFootIndex2Sx = DoubleField(default_value=1.0)

    RightFootIndex2Sy = DoubleField(default_value=1.0)

    RightFootIndex2Sz = DoubleField(default_value=1.0)


class RightFootIndex2SAttrOperator(
    CompoundAttrOperator[RightFootIndex2SPlugOperator]
):
    __slots__ = ()

    RightFootIndex2Sx = DoubleField(default_value=1.0)

    RightFootIndex2Sy = DoubleField(default_value=1.0)

    RightFootIndex2Sz = DoubleField(default_value=1.0)


class RightFootIndex2SField(
    CompoundField[RightFootIndex2SAttrOperator, RightFootIndex2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex2SAttrOperator
    PLUG_CLS = RightFootIndex2SPlugOperator

    RightFootIndex2Sx = DoubleField(default_value=1.0)

    RightFootIndex2Sy = DoubleField(default_value=1.0)

    RightFootIndex2Sz = DoubleField(default_value=1.0)


class RightFootIndex3TPlugOperator(
    CompoundPlugOperator["RightFootIndex3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex3Tx", "RightFootIndex3Tx"),
        ("RightFootIndex3Ty", "RightFootIndex3Ty"),
        ("RightFootIndex3Tz", "RightFootIndex3Tz"),
    )

    RightFootIndex3Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex3Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex3Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex3TAttrOperator(
    CompoundAttrOperator[RightFootIndex3TPlugOperator]
):
    __slots__ = ()

    RightFootIndex3Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex3Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex3Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex3TField(
    CompoundField[RightFootIndex3TAttrOperator, RightFootIndex3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex3TAttrOperator
    PLUG_CLS = RightFootIndex3TPlugOperator

    RightFootIndex3Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex3Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex3Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex3RPlugOperator(
    CompoundPlugOperator["RightFootIndex3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex3Rx", "RightFootIndex3Rx"),
        ("RightFootIndex3Ry", "RightFootIndex3Ry"),
        ("RightFootIndex3Rz", "RightFootIndex3Rz"),
    )

    RightFootIndex3Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex3Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex3Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex3RAttrOperator(
    CompoundAttrOperator[RightFootIndex3RPlugOperator]
):
    __slots__ = ()

    RightFootIndex3Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex3Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex3Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex3RField(
    CompoundField[RightFootIndex3RAttrOperator, RightFootIndex3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex3RAttrOperator
    PLUG_CLS = RightFootIndex3RPlugOperator

    RightFootIndex3Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex3Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex3Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex3SPlugOperator(
    CompoundPlugOperator["RightFootIndex3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex3Sx", "RightFootIndex3Sx"),
        ("RightFootIndex3Sy", "RightFootIndex3Sy"),
        ("RightFootIndex3Sz", "RightFootIndex3Sz"),
    )

    RightFootIndex3Sx = DoubleField(default_value=1.0)

    RightFootIndex3Sy = DoubleField(default_value=1.0)

    RightFootIndex3Sz = DoubleField(default_value=1.0)


class RightFootIndex3SAttrOperator(
    CompoundAttrOperator[RightFootIndex3SPlugOperator]
):
    __slots__ = ()

    RightFootIndex3Sx = DoubleField(default_value=1.0)

    RightFootIndex3Sy = DoubleField(default_value=1.0)

    RightFootIndex3Sz = DoubleField(default_value=1.0)


class RightFootIndex3SField(
    CompoundField[RightFootIndex3SAttrOperator, RightFootIndex3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex3SAttrOperator
    PLUG_CLS = RightFootIndex3SPlugOperator

    RightFootIndex3Sx = DoubleField(default_value=1.0)

    RightFootIndex3Sy = DoubleField(default_value=1.0)

    RightFootIndex3Sz = DoubleField(default_value=1.0)


class RightFootIndex4TPlugOperator(
    CompoundPlugOperator["RightFootIndex4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex4Tx", "RightFootIndex4Tx"),
        ("RightFootIndex4Ty", "RightFootIndex4Ty"),
        ("RightFootIndex4Tz", "RightFootIndex4Tz"),
    )

    RightFootIndex4Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex4Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex4Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex4TAttrOperator(
    CompoundAttrOperator[RightFootIndex4TPlugOperator]
):
    __slots__ = ()

    RightFootIndex4Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex4Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex4Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex4TField(
    CompoundField[RightFootIndex4TAttrOperator, RightFootIndex4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex4TAttrOperator
    PLUG_CLS = RightFootIndex4TPlugOperator

    RightFootIndex4Tx = DoubleLinearField(default_value=0.0)

    RightFootIndex4Ty = DoubleLinearField(default_value=0.0)

    RightFootIndex4Tz = DoubleLinearField(default_value=0.0)


class RightFootIndex4RPlugOperator(
    CompoundPlugOperator["RightFootIndex4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex4Rx", "RightFootIndex4Rx"),
        ("RightFootIndex4Ry", "RightFootIndex4Ry"),
        ("RightFootIndex4Rz", "RightFootIndex4Rz"),
    )

    RightFootIndex4Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex4Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex4Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex4RAttrOperator(
    CompoundAttrOperator[RightFootIndex4RPlugOperator]
):
    __slots__ = ()

    RightFootIndex4Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex4Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex4Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex4RField(
    CompoundField[RightFootIndex4RAttrOperator, RightFootIndex4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex4RAttrOperator
    PLUG_CLS = RightFootIndex4RPlugOperator

    RightFootIndex4Rx = DoubleAngleField(default_value=0.0)

    RightFootIndex4Ry = DoubleAngleField(default_value=0.0)

    RightFootIndex4Rz = DoubleAngleField(default_value=0.0)


class RightFootIndex4SPlugOperator(
    CompoundPlugOperator["RightFootIndex4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootIndex4Sx", "RightFootIndex4Sx"),
        ("RightFootIndex4Sy", "RightFootIndex4Sy"),
        ("RightFootIndex4Sz", "RightFootIndex4Sz"),
    )

    RightFootIndex4Sx = DoubleField(default_value=1.0)

    RightFootIndex4Sy = DoubleField(default_value=1.0)

    RightFootIndex4Sz = DoubleField(default_value=1.0)


class RightFootIndex4SAttrOperator(
    CompoundAttrOperator[RightFootIndex4SPlugOperator]
):
    __slots__ = ()

    RightFootIndex4Sx = DoubleField(default_value=1.0)

    RightFootIndex4Sy = DoubleField(default_value=1.0)

    RightFootIndex4Sz = DoubleField(default_value=1.0)


class RightFootIndex4SField(
    CompoundField[RightFootIndex4SAttrOperator, RightFootIndex4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootIndex4SAttrOperator
    PLUG_CLS = RightFootIndex4SPlugOperator

    RightFootIndex4Sx = DoubleField(default_value=1.0)

    RightFootIndex4Sy = DoubleField(default_value=1.0)

    RightFootIndex4Sz = DoubleField(default_value=1.0)


class RightFootMiddle1TPlugOperator(
    CompoundPlugOperator["RightFootMiddle1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle1Tx", "RightFootMiddle1Tx"),
        ("RightFootMiddle1Ty", "RightFootMiddle1Ty"),
        ("RightFootMiddle1Tz", "RightFootMiddle1Tz"),
    )

    RightFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle1TAttrOperator(
    CompoundAttrOperator[RightFootMiddle1TPlugOperator]
):
    __slots__ = ()

    RightFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle1TField(
    CompoundField[RightFootMiddle1TAttrOperator, RightFootMiddle1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle1TAttrOperator
    PLUG_CLS = RightFootMiddle1TPlugOperator

    RightFootMiddle1Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle1Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle1RPlugOperator(
    CompoundPlugOperator["RightFootMiddle1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle1Rx", "RightFootMiddle1Rx"),
        ("RightFootMiddle1Ry", "RightFootMiddle1Ry"),
        ("RightFootMiddle1Rz", "RightFootMiddle1Rz"),
    )

    RightFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle1RAttrOperator(
    CompoundAttrOperator[RightFootMiddle1RPlugOperator]
):
    __slots__ = ()

    RightFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle1RField(
    CompoundField[RightFootMiddle1RAttrOperator, RightFootMiddle1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle1RAttrOperator
    PLUG_CLS = RightFootMiddle1RPlugOperator

    RightFootMiddle1Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle1Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle1SPlugOperator(
    CompoundPlugOperator["RightFootMiddle1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle1Sx", "RightFootMiddle1Sx"),
        ("RightFootMiddle1Sy", "RightFootMiddle1Sy"),
        ("RightFootMiddle1Sz", "RightFootMiddle1Sz"),
    )

    RightFootMiddle1Sx = DoubleField(default_value=1.0)

    RightFootMiddle1Sy = DoubleField(default_value=1.0)

    RightFootMiddle1Sz = DoubleField(default_value=1.0)


class RightFootMiddle1SAttrOperator(
    CompoundAttrOperator[RightFootMiddle1SPlugOperator]
):
    __slots__ = ()

    RightFootMiddle1Sx = DoubleField(default_value=1.0)

    RightFootMiddle1Sy = DoubleField(default_value=1.0)

    RightFootMiddle1Sz = DoubleField(default_value=1.0)


class RightFootMiddle1SField(
    CompoundField[RightFootMiddle1SAttrOperator, RightFootMiddle1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle1SAttrOperator
    PLUG_CLS = RightFootMiddle1SPlugOperator

    RightFootMiddle1Sx = DoubleField(default_value=1.0)

    RightFootMiddle1Sy = DoubleField(default_value=1.0)

    RightFootMiddle1Sz = DoubleField(default_value=1.0)


class RightFootMiddle2TPlugOperator(
    CompoundPlugOperator["RightFootMiddle2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle2Tx", "RightFootMiddle2Tx"),
        ("RightFootMiddle2Ty", "RightFootMiddle2Ty"),
        ("RightFootMiddle2Tz", "RightFootMiddle2Tz"),
    )

    RightFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle2TAttrOperator(
    CompoundAttrOperator[RightFootMiddle2TPlugOperator]
):
    __slots__ = ()

    RightFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle2TField(
    CompoundField[RightFootMiddle2TAttrOperator, RightFootMiddle2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle2TAttrOperator
    PLUG_CLS = RightFootMiddle2TPlugOperator

    RightFootMiddle2Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle2Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle2RPlugOperator(
    CompoundPlugOperator["RightFootMiddle2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle2Rx", "RightFootMiddle2Rx"),
        ("RightFootMiddle2Ry", "RightFootMiddle2Ry"),
        ("RightFootMiddle2Rz", "RightFootMiddle2Rz"),
    )

    RightFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle2RAttrOperator(
    CompoundAttrOperator[RightFootMiddle2RPlugOperator]
):
    __slots__ = ()

    RightFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle2RField(
    CompoundField[RightFootMiddle2RAttrOperator, RightFootMiddle2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle2RAttrOperator
    PLUG_CLS = RightFootMiddle2RPlugOperator

    RightFootMiddle2Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle2Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle2SPlugOperator(
    CompoundPlugOperator["RightFootMiddle2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle2Sx", "RightFootMiddle2Sx"),
        ("RightFootMiddle2Sy", "RightFootMiddle2Sy"),
        ("RightFootMiddle2Sz", "RightFootMiddle2Sz"),
    )

    RightFootMiddle2Sx = DoubleField(default_value=1.0)

    RightFootMiddle2Sy = DoubleField(default_value=1.0)

    RightFootMiddle2Sz = DoubleField(default_value=1.0)


class RightFootMiddle2SAttrOperator(
    CompoundAttrOperator[RightFootMiddle2SPlugOperator]
):
    __slots__ = ()

    RightFootMiddle2Sx = DoubleField(default_value=1.0)

    RightFootMiddle2Sy = DoubleField(default_value=1.0)

    RightFootMiddle2Sz = DoubleField(default_value=1.0)


class RightFootMiddle2SField(
    CompoundField[RightFootMiddle2SAttrOperator, RightFootMiddle2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle2SAttrOperator
    PLUG_CLS = RightFootMiddle2SPlugOperator

    RightFootMiddle2Sx = DoubleField(default_value=1.0)

    RightFootMiddle2Sy = DoubleField(default_value=1.0)

    RightFootMiddle2Sz = DoubleField(default_value=1.0)


class RightFootMiddle3TPlugOperator(
    CompoundPlugOperator["RightFootMiddle3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle3Tx", "RightFootMiddle3Tx"),
        ("RightFootMiddle3Ty", "RightFootMiddle3Ty"),
        ("RightFootMiddle3Tz", "RightFootMiddle3Tz"),
    )

    RightFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle3TAttrOperator(
    CompoundAttrOperator[RightFootMiddle3TPlugOperator]
):
    __slots__ = ()

    RightFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle3TField(
    CompoundField[RightFootMiddle3TAttrOperator, RightFootMiddle3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle3TAttrOperator
    PLUG_CLS = RightFootMiddle3TPlugOperator

    RightFootMiddle3Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle3Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle3RPlugOperator(
    CompoundPlugOperator["RightFootMiddle3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle3Rx", "RightFootMiddle3Rx"),
        ("RightFootMiddle3Ry", "RightFootMiddle3Ry"),
        ("RightFootMiddle3Rz", "RightFootMiddle3Rz"),
    )

    RightFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle3RAttrOperator(
    CompoundAttrOperator[RightFootMiddle3RPlugOperator]
):
    __slots__ = ()

    RightFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle3RField(
    CompoundField[RightFootMiddle3RAttrOperator, RightFootMiddle3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle3RAttrOperator
    PLUG_CLS = RightFootMiddle3RPlugOperator

    RightFootMiddle3Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle3Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle3SPlugOperator(
    CompoundPlugOperator["RightFootMiddle3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle3Sx", "RightFootMiddle3Sx"),
        ("RightFootMiddle3Sy", "RightFootMiddle3Sy"),
        ("RightFootMiddle3Sz", "RightFootMiddle3Sz"),
    )

    RightFootMiddle3Sx = DoubleField(default_value=1.0)

    RightFootMiddle3Sy = DoubleField(default_value=1.0)

    RightFootMiddle3Sz = DoubleField(default_value=1.0)


class RightFootMiddle3SAttrOperator(
    CompoundAttrOperator[RightFootMiddle3SPlugOperator]
):
    __slots__ = ()

    RightFootMiddle3Sx = DoubleField(default_value=1.0)

    RightFootMiddle3Sy = DoubleField(default_value=1.0)

    RightFootMiddle3Sz = DoubleField(default_value=1.0)


class RightFootMiddle3SField(
    CompoundField[RightFootMiddle3SAttrOperator, RightFootMiddle3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle3SAttrOperator
    PLUG_CLS = RightFootMiddle3SPlugOperator

    RightFootMiddle3Sx = DoubleField(default_value=1.0)

    RightFootMiddle3Sy = DoubleField(default_value=1.0)

    RightFootMiddle3Sz = DoubleField(default_value=1.0)


class RightFootMiddle4TPlugOperator(
    CompoundPlugOperator["RightFootMiddle4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle4Tx", "RightFootMiddle4Tx"),
        ("RightFootMiddle4Ty", "RightFootMiddle4Ty"),
        ("RightFootMiddle4Tz", "RightFootMiddle4Tz"),
    )

    RightFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle4TAttrOperator(
    CompoundAttrOperator[RightFootMiddle4TPlugOperator]
):
    __slots__ = ()

    RightFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle4TField(
    CompoundField[RightFootMiddle4TAttrOperator, RightFootMiddle4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle4TAttrOperator
    PLUG_CLS = RightFootMiddle4TPlugOperator

    RightFootMiddle4Tx = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Ty = DoubleLinearField(default_value=0.0)

    RightFootMiddle4Tz = DoubleLinearField(default_value=0.0)


class RightFootMiddle4RPlugOperator(
    CompoundPlugOperator["RightFootMiddle4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle4Rx", "RightFootMiddle4Rx"),
        ("RightFootMiddle4Ry", "RightFootMiddle4Ry"),
        ("RightFootMiddle4Rz", "RightFootMiddle4Rz"),
    )

    RightFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle4RAttrOperator(
    CompoundAttrOperator[RightFootMiddle4RPlugOperator]
):
    __slots__ = ()

    RightFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle4RField(
    CompoundField[RightFootMiddle4RAttrOperator, RightFootMiddle4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle4RAttrOperator
    PLUG_CLS = RightFootMiddle4RPlugOperator

    RightFootMiddle4Rx = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Ry = DoubleAngleField(default_value=0.0)

    RightFootMiddle4Rz = DoubleAngleField(default_value=0.0)


class RightFootMiddle4SPlugOperator(
    CompoundPlugOperator["RightFootMiddle4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootMiddle4Sx", "RightFootMiddle4Sx"),
        ("RightFootMiddle4Sy", "RightFootMiddle4Sy"),
        ("RightFootMiddle4Sz", "RightFootMiddle4Sz"),
    )

    RightFootMiddle4Sx = DoubleField(default_value=1.0)

    RightFootMiddle4Sy = DoubleField(default_value=1.0)

    RightFootMiddle4Sz = DoubleField(default_value=1.0)


class RightFootMiddle4SAttrOperator(
    CompoundAttrOperator[RightFootMiddle4SPlugOperator]
):
    __slots__ = ()

    RightFootMiddle4Sx = DoubleField(default_value=1.0)

    RightFootMiddle4Sy = DoubleField(default_value=1.0)

    RightFootMiddle4Sz = DoubleField(default_value=1.0)


class RightFootMiddle4SField(
    CompoundField[RightFootMiddle4SAttrOperator, RightFootMiddle4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootMiddle4SAttrOperator
    PLUG_CLS = RightFootMiddle4SPlugOperator

    RightFootMiddle4Sx = DoubleField(default_value=1.0)

    RightFootMiddle4Sy = DoubleField(default_value=1.0)

    RightFootMiddle4Sz = DoubleField(default_value=1.0)


class RightFootRing1TPlugOperator(
    CompoundPlugOperator["RightFootRing1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing1Tx", "RightFootRing1Tx"),
        ("RightFootRing1Ty", "RightFootRing1Ty"),
        ("RightFootRing1Tz", "RightFootRing1Tz"),
    )

    RightFootRing1Tx = DoubleLinearField(default_value=0.0)

    RightFootRing1Ty = DoubleLinearField(default_value=0.0)

    RightFootRing1Tz = DoubleLinearField(default_value=0.0)


class RightFootRing1TAttrOperator(
    CompoundAttrOperator[RightFootRing1TPlugOperator]
):
    __slots__ = ()

    RightFootRing1Tx = DoubleLinearField(default_value=0.0)

    RightFootRing1Ty = DoubleLinearField(default_value=0.0)

    RightFootRing1Tz = DoubleLinearField(default_value=0.0)


class RightFootRing1TField(
    CompoundField[RightFootRing1TAttrOperator, RightFootRing1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing1TAttrOperator
    PLUG_CLS = RightFootRing1TPlugOperator

    RightFootRing1Tx = DoubleLinearField(default_value=0.0)

    RightFootRing1Ty = DoubleLinearField(default_value=0.0)

    RightFootRing1Tz = DoubleLinearField(default_value=0.0)


class RightFootRing1RPlugOperator(
    CompoundPlugOperator["RightFootRing1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing1Rx", "RightFootRing1Rx"),
        ("RightFootRing1Ry", "RightFootRing1Ry"),
        ("RightFootRing1Rz", "RightFootRing1Rz"),
    )

    RightFootRing1Rx = DoubleAngleField(default_value=0.0)

    RightFootRing1Ry = DoubleAngleField(default_value=0.0)

    RightFootRing1Rz = DoubleAngleField(default_value=0.0)


class RightFootRing1RAttrOperator(
    CompoundAttrOperator[RightFootRing1RPlugOperator]
):
    __slots__ = ()

    RightFootRing1Rx = DoubleAngleField(default_value=0.0)

    RightFootRing1Ry = DoubleAngleField(default_value=0.0)

    RightFootRing1Rz = DoubleAngleField(default_value=0.0)


class RightFootRing1RField(
    CompoundField[RightFootRing1RAttrOperator, RightFootRing1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing1RAttrOperator
    PLUG_CLS = RightFootRing1RPlugOperator

    RightFootRing1Rx = DoubleAngleField(default_value=0.0)

    RightFootRing1Ry = DoubleAngleField(default_value=0.0)

    RightFootRing1Rz = DoubleAngleField(default_value=0.0)


class RightFootRing1SPlugOperator(
    CompoundPlugOperator["RightFootRing1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing1Sx", "RightFootRing1Sx"),
        ("RightFootRing1Sy", "RightFootRing1Sy"),
        ("RightFootRing1Sz", "RightFootRing1Sz"),
    )

    RightFootRing1Sx = DoubleField(default_value=1.0)

    RightFootRing1Sy = DoubleField(default_value=1.0)

    RightFootRing1Sz = DoubleField(default_value=1.0)


class RightFootRing1SAttrOperator(
    CompoundAttrOperator[RightFootRing1SPlugOperator]
):
    __slots__ = ()

    RightFootRing1Sx = DoubleField(default_value=1.0)

    RightFootRing1Sy = DoubleField(default_value=1.0)

    RightFootRing1Sz = DoubleField(default_value=1.0)


class RightFootRing1SField(
    CompoundField[RightFootRing1SAttrOperator, RightFootRing1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing1SAttrOperator
    PLUG_CLS = RightFootRing1SPlugOperator

    RightFootRing1Sx = DoubleField(default_value=1.0)

    RightFootRing1Sy = DoubleField(default_value=1.0)

    RightFootRing1Sz = DoubleField(default_value=1.0)


class RightFootRing2TPlugOperator(
    CompoundPlugOperator["RightFootRing2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing2Tx", "RightFootRing2Tx"),
        ("RightFootRing2Ty", "RightFootRing2Ty"),
        ("RightFootRing2Tz", "RightFootRing2Tz"),
    )

    RightFootRing2Tx = DoubleLinearField(default_value=0.0)

    RightFootRing2Ty = DoubleLinearField(default_value=0.0)

    RightFootRing2Tz = DoubleLinearField(default_value=0.0)


class RightFootRing2TAttrOperator(
    CompoundAttrOperator[RightFootRing2TPlugOperator]
):
    __slots__ = ()

    RightFootRing2Tx = DoubleLinearField(default_value=0.0)

    RightFootRing2Ty = DoubleLinearField(default_value=0.0)

    RightFootRing2Tz = DoubleLinearField(default_value=0.0)


class RightFootRing2TField(
    CompoundField[RightFootRing2TAttrOperator, RightFootRing2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing2TAttrOperator
    PLUG_CLS = RightFootRing2TPlugOperator

    RightFootRing2Tx = DoubleLinearField(default_value=0.0)

    RightFootRing2Ty = DoubleLinearField(default_value=0.0)

    RightFootRing2Tz = DoubleLinearField(default_value=0.0)


class RightFootRing2RPlugOperator(
    CompoundPlugOperator["RightFootRing2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing2Rx", "RightFootRing2Rx"),
        ("RightFootRing2Ry", "RightFootRing2Ry"),
        ("RightFootRing2Rz", "RightFootRing2Rz"),
    )

    RightFootRing2Rx = DoubleAngleField(default_value=0.0)

    RightFootRing2Ry = DoubleAngleField(default_value=0.0)

    RightFootRing2Rz = DoubleAngleField(default_value=0.0)


class RightFootRing2RAttrOperator(
    CompoundAttrOperator[RightFootRing2RPlugOperator]
):
    __slots__ = ()

    RightFootRing2Rx = DoubleAngleField(default_value=0.0)

    RightFootRing2Ry = DoubleAngleField(default_value=0.0)

    RightFootRing2Rz = DoubleAngleField(default_value=0.0)


class RightFootRing2RField(
    CompoundField[RightFootRing2RAttrOperator, RightFootRing2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing2RAttrOperator
    PLUG_CLS = RightFootRing2RPlugOperator

    RightFootRing2Rx = DoubleAngleField(default_value=0.0)

    RightFootRing2Ry = DoubleAngleField(default_value=0.0)

    RightFootRing2Rz = DoubleAngleField(default_value=0.0)


class RightFootRing2SPlugOperator(
    CompoundPlugOperator["RightFootRing2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing2Sx", "RightFootRing2Sx"),
        ("RightFootRing2Sy", "RightFootRing2Sy"),
        ("RightFootRing2Sz", "RightFootRing2Sz"),
    )

    RightFootRing2Sx = DoubleField(default_value=1.0)

    RightFootRing2Sy = DoubleField(default_value=1.0)

    RightFootRing2Sz = DoubleField(default_value=1.0)


class RightFootRing2SAttrOperator(
    CompoundAttrOperator[RightFootRing2SPlugOperator]
):
    __slots__ = ()

    RightFootRing2Sx = DoubleField(default_value=1.0)

    RightFootRing2Sy = DoubleField(default_value=1.0)

    RightFootRing2Sz = DoubleField(default_value=1.0)


class RightFootRing2SField(
    CompoundField[RightFootRing2SAttrOperator, RightFootRing2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing2SAttrOperator
    PLUG_CLS = RightFootRing2SPlugOperator

    RightFootRing2Sx = DoubleField(default_value=1.0)

    RightFootRing2Sy = DoubleField(default_value=1.0)

    RightFootRing2Sz = DoubleField(default_value=1.0)


class RightFootRing3TPlugOperator(
    CompoundPlugOperator["RightFootRing3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing3Tx", "RightFootRing3Tx"),
        ("RightFootRing3Ty", "RightFootRing3Ty"),
        ("RightFootRing3Tz", "RightFootRing3Tz"),
    )

    RightFootRing3Tx = DoubleLinearField(default_value=0.0)

    RightFootRing3Ty = DoubleLinearField(default_value=0.0)

    RightFootRing3Tz = DoubleLinearField(default_value=0.0)


class RightFootRing3TAttrOperator(
    CompoundAttrOperator[RightFootRing3TPlugOperator]
):
    __slots__ = ()

    RightFootRing3Tx = DoubleLinearField(default_value=0.0)

    RightFootRing3Ty = DoubleLinearField(default_value=0.0)

    RightFootRing3Tz = DoubleLinearField(default_value=0.0)


class RightFootRing3TField(
    CompoundField[RightFootRing3TAttrOperator, RightFootRing3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing3TAttrOperator
    PLUG_CLS = RightFootRing3TPlugOperator

    RightFootRing3Tx = DoubleLinearField(default_value=0.0)

    RightFootRing3Ty = DoubleLinearField(default_value=0.0)

    RightFootRing3Tz = DoubleLinearField(default_value=0.0)


class RightFootRing3RPlugOperator(
    CompoundPlugOperator["RightFootRing3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing3Rx", "RightFootRing3Rx"),
        ("RightFootRing3Ry", "RightFootRing3Ry"),
        ("RightFootRing3Rz", "RightFootRing3Rz"),
    )

    RightFootRing3Rx = DoubleAngleField(default_value=0.0)

    RightFootRing3Ry = DoubleAngleField(default_value=0.0)

    RightFootRing3Rz = DoubleAngleField(default_value=0.0)


class RightFootRing3RAttrOperator(
    CompoundAttrOperator[RightFootRing3RPlugOperator]
):
    __slots__ = ()

    RightFootRing3Rx = DoubleAngleField(default_value=0.0)

    RightFootRing3Ry = DoubleAngleField(default_value=0.0)

    RightFootRing3Rz = DoubleAngleField(default_value=0.0)


class RightFootRing3RField(
    CompoundField[RightFootRing3RAttrOperator, RightFootRing3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing3RAttrOperator
    PLUG_CLS = RightFootRing3RPlugOperator

    RightFootRing3Rx = DoubleAngleField(default_value=0.0)

    RightFootRing3Ry = DoubleAngleField(default_value=0.0)

    RightFootRing3Rz = DoubleAngleField(default_value=0.0)


class RightFootRing3SPlugOperator(
    CompoundPlugOperator["RightFootRing3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing3Sx", "RightFootRing3Sx"),
        ("RightFootRing3Sy", "RightFootRing3Sy"),
        ("RightFootRing3Sz", "RightFootRing3Sz"),
    )

    RightFootRing3Sx = DoubleField(default_value=1.0)

    RightFootRing3Sy = DoubleField(default_value=1.0)

    RightFootRing3Sz = DoubleField(default_value=1.0)


class RightFootRing3SAttrOperator(
    CompoundAttrOperator[RightFootRing3SPlugOperator]
):
    __slots__ = ()

    RightFootRing3Sx = DoubleField(default_value=1.0)

    RightFootRing3Sy = DoubleField(default_value=1.0)

    RightFootRing3Sz = DoubleField(default_value=1.0)


class RightFootRing3SField(
    CompoundField[RightFootRing3SAttrOperator, RightFootRing3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing3SAttrOperator
    PLUG_CLS = RightFootRing3SPlugOperator

    RightFootRing3Sx = DoubleField(default_value=1.0)

    RightFootRing3Sy = DoubleField(default_value=1.0)

    RightFootRing3Sz = DoubleField(default_value=1.0)


class RightFootRing4TPlugOperator(
    CompoundPlugOperator["RightFootRing4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing4Tx", "RightFootRing4Tx"),
        ("RightFootRing4Ty", "RightFootRing4Ty"),
        ("RightFootRing4Tz", "RightFootRing4Tz"),
    )

    RightFootRing4Tx = DoubleLinearField(default_value=0.0)

    RightFootRing4Ty = DoubleLinearField(default_value=0.0)

    RightFootRing4Tz = DoubleLinearField(default_value=0.0)


class RightFootRing4TAttrOperator(
    CompoundAttrOperator[RightFootRing4TPlugOperator]
):
    __slots__ = ()

    RightFootRing4Tx = DoubleLinearField(default_value=0.0)

    RightFootRing4Ty = DoubleLinearField(default_value=0.0)

    RightFootRing4Tz = DoubleLinearField(default_value=0.0)


class RightFootRing4TField(
    CompoundField[RightFootRing4TAttrOperator, RightFootRing4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing4TAttrOperator
    PLUG_CLS = RightFootRing4TPlugOperator

    RightFootRing4Tx = DoubleLinearField(default_value=0.0)

    RightFootRing4Ty = DoubleLinearField(default_value=0.0)

    RightFootRing4Tz = DoubleLinearField(default_value=0.0)


class RightFootRing4RPlugOperator(
    CompoundPlugOperator["RightFootRing4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing4Rx", "RightFootRing4Rx"),
        ("RightFootRing4Ry", "RightFootRing4Ry"),
        ("RightFootRing4Rz", "RightFootRing4Rz"),
    )

    RightFootRing4Rx = DoubleAngleField(default_value=0.0)

    RightFootRing4Ry = DoubleAngleField(default_value=0.0)

    RightFootRing4Rz = DoubleAngleField(default_value=0.0)


class RightFootRing4RAttrOperator(
    CompoundAttrOperator[RightFootRing4RPlugOperator]
):
    __slots__ = ()

    RightFootRing4Rx = DoubleAngleField(default_value=0.0)

    RightFootRing4Ry = DoubleAngleField(default_value=0.0)

    RightFootRing4Rz = DoubleAngleField(default_value=0.0)


class RightFootRing4RField(
    CompoundField[RightFootRing4RAttrOperator, RightFootRing4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing4RAttrOperator
    PLUG_CLS = RightFootRing4RPlugOperator

    RightFootRing4Rx = DoubleAngleField(default_value=0.0)

    RightFootRing4Ry = DoubleAngleField(default_value=0.0)

    RightFootRing4Rz = DoubleAngleField(default_value=0.0)


class RightFootRing4SPlugOperator(
    CompoundPlugOperator["RightFootRing4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootRing4Sx", "RightFootRing4Sx"),
        ("RightFootRing4Sy", "RightFootRing4Sy"),
        ("RightFootRing4Sz", "RightFootRing4Sz"),
    )

    RightFootRing4Sx = DoubleField(default_value=1.0)

    RightFootRing4Sy = DoubleField(default_value=1.0)

    RightFootRing4Sz = DoubleField(default_value=1.0)


class RightFootRing4SAttrOperator(
    CompoundAttrOperator[RightFootRing4SPlugOperator]
):
    __slots__ = ()

    RightFootRing4Sx = DoubleField(default_value=1.0)

    RightFootRing4Sy = DoubleField(default_value=1.0)

    RightFootRing4Sz = DoubleField(default_value=1.0)


class RightFootRing4SField(
    CompoundField[RightFootRing4SAttrOperator, RightFootRing4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootRing4SAttrOperator
    PLUG_CLS = RightFootRing4SPlugOperator

    RightFootRing4Sx = DoubleField(default_value=1.0)

    RightFootRing4Sy = DoubleField(default_value=1.0)

    RightFootRing4Sz = DoubleField(default_value=1.0)


class RightFootPinky1TPlugOperator(
    CompoundPlugOperator["RightFootPinky1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky1Tx", "RightFootPinky1Tx"),
        ("RightFootPinky1Ty", "RightFootPinky1Ty"),
        ("RightFootPinky1Tz", "RightFootPinky1Tz"),
    )

    RightFootPinky1Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky1Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky1Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky1TAttrOperator(
    CompoundAttrOperator[RightFootPinky1TPlugOperator]
):
    __slots__ = ()

    RightFootPinky1Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky1Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky1Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky1TField(
    CompoundField[RightFootPinky1TAttrOperator, RightFootPinky1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky1TAttrOperator
    PLUG_CLS = RightFootPinky1TPlugOperator

    RightFootPinky1Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky1Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky1Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky1RPlugOperator(
    CompoundPlugOperator["RightFootPinky1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky1Rx", "RightFootPinky1Rx"),
        ("RightFootPinky1Ry", "RightFootPinky1Ry"),
        ("RightFootPinky1Rz", "RightFootPinky1Rz"),
    )

    RightFootPinky1Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky1Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky1Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky1RAttrOperator(
    CompoundAttrOperator[RightFootPinky1RPlugOperator]
):
    __slots__ = ()

    RightFootPinky1Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky1Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky1Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky1RField(
    CompoundField[RightFootPinky1RAttrOperator, RightFootPinky1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky1RAttrOperator
    PLUG_CLS = RightFootPinky1RPlugOperator

    RightFootPinky1Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky1Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky1Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky1SPlugOperator(
    CompoundPlugOperator["RightFootPinky1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky1Sx", "RightFootPinky1Sx"),
        ("RightFootPinky1Sy", "RightFootPinky1Sy"),
        ("RightFootPinky1Sz", "RightFootPinky1Sz"),
    )

    RightFootPinky1Sx = DoubleField(default_value=1.0)

    RightFootPinky1Sy = DoubleField(default_value=1.0)

    RightFootPinky1Sz = DoubleField(default_value=1.0)


class RightFootPinky1SAttrOperator(
    CompoundAttrOperator[RightFootPinky1SPlugOperator]
):
    __slots__ = ()

    RightFootPinky1Sx = DoubleField(default_value=1.0)

    RightFootPinky1Sy = DoubleField(default_value=1.0)

    RightFootPinky1Sz = DoubleField(default_value=1.0)


class RightFootPinky1SField(
    CompoundField[RightFootPinky1SAttrOperator, RightFootPinky1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky1SAttrOperator
    PLUG_CLS = RightFootPinky1SPlugOperator

    RightFootPinky1Sx = DoubleField(default_value=1.0)

    RightFootPinky1Sy = DoubleField(default_value=1.0)

    RightFootPinky1Sz = DoubleField(default_value=1.0)


class RightFootPinky2TPlugOperator(
    CompoundPlugOperator["RightFootPinky2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky2Tx", "RightFootPinky2Tx"),
        ("RightFootPinky2Ty", "RightFootPinky2Ty"),
        ("RightFootPinky2Tz", "RightFootPinky2Tz"),
    )

    RightFootPinky2Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky2Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky2Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky2TAttrOperator(
    CompoundAttrOperator[RightFootPinky2TPlugOperator]
):
    __slots__ = ()

    RightFootPinky2Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky2Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky2Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky2TField(
    CompoundField[RightFootPinky2TAttrOperator, RightFootPinky2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky2TAttrOperator
    PLUG_CLS = RightFootPinky2TPlugOperator

    RightFootPinky2Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky2Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky2Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky2RPlugOperator(
    CompoundPlugOperator["RightFootPinky2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky2Rx", "RightFootPinky2Rx"),
        ("RightFootPinky2Ry", "RightFootPinky2Ry"),
        ("RightFootPinky2Rz", "RightFootPinky2Rz"),
    )

    RightFootPinky2Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky2Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky2Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky2RAttrOperator(
    CompoundAttrOperator[RightFootPinky2RPlugOperator]
):
    __slots__ = ()

    RightFootPinky2Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky2Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky2Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky2RField(
    CompoundField[RightFootPinky2RAttrOperator, RightFootPinky2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky2RAttrOperator
    PLUG_CLS = RightFootPinky2RPlugOperator

    RightFootPinky2Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky2Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky2Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky2SPlugOperator(
    CompoundPlugOperator["RightFootPinky2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky2Sx", "RightFootPinky2Sx"),
        ("RightFootPinky2Sy", "RightFootPinky2Sy"),
        ("RightFootPinky2Sz", "RightFootPinky2Sz"),
    )

    RightFootPinky2Sx = DoubleField(default_value=1.0)

    RightFootPinky2Sy = DoubleField(default_value=1.0)

    RightFootPinky2Sz = DoubleField(default_value=1.0)


class RightFootPinky2SAttrOperator(
    CompoundAttrOperator[RightFootPinky2SPlugOperator]
):
    __slots__ = ()

    RightFootPinky2Sx = DoubleField(default_value=1.0)

    RightFootPinky2Sy = DoubleField(default_value=1.0)

    RightFootPinky2Sz = DoubleField(default_value=1.0)


class RightFootPinky2SField(
    CompoundField[RightFootPinky2SAttrOperator, RightFootPinky2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky2SAttrOperator
    PLUG_CLS = RightFootPinky2SPlugOperator

    RightFootPinky2Sx = DoubleField(default_value=1.0)

    RightFootPinky2Sy = DoubleField(default_value=1.0)

    RightFootPinky2Sz = DoubleField(default_value=1.0)


class RightFootPinky3TPlugOperator(
    CompoundPlugOperator["RightFootPinky3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky3Tx", "RightFootPinky3Tx"),
        ("RightFootPinky3Ty", "RightFootPinky3Ty"),
        ("RightFootPinky3Tz", "RightFootPinky3Tz"),
    )

    RightFootPinky3Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky3Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky3Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky3TAttrOperator(
    CompoundAttrOperator[RightFootPinky3TPlugOperator]
):
    __slots__ = ()

    RightFootPinky3Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky3Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky3Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky3TField(
    CompoundField[RightFootPinky3TAttrOperator, RightFootPinky3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky3TAttrOperator
    PLUG_CLS = RightFootPinky3TPlugOperator

    RightFootPinky3Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky3Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky3Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky3RPlugOperator(
    CompoundPlugOperator["RightFootPinky3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky3Rx", "RightFootPinky3Rx"),
        ("RightFootPinky3Ry", "RightFootPinky3Ry"),
        ("RightFootPinky3Rz", "RightFootPinky3Rz"),
    )

    RightFootPinky3Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky3Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky3Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky3RAttrOperator(
    CompoundAttrOperator[RightFootPinky3RPlugOperator]
):
    __slots__ = ()

    RightFootPinky3Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky3Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky3Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky3RField(
    CompoundField[RightFootPinky3RAttrOperator, RightFootPinky3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky3RAttrOperator
    PLUG_CLS = RightFootPinky3RPlugOperator

    RightFootPinky3Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky3Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky3Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky3SPlugOperator(
    CompoundPlugOperator["RightFootPinky3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky3Sx", "RightFootPinky3Sx"),
        ("RightFootPinky3Sy", "RightFootPinky3Sy"),
        ("RightFootPinky3Sz", "RightFootPinky3Sz"),
    )

    RightFootPinky3Sx = DoubleField(default_value=1.0)

    RightFootPinky3Sy = DoubleField(default_value=1.0)

    RightFootPinky3Sz = DoubleField(default_value=1.0)


class RightFootPinky3SAttrOperator(
    CompoundAttrOperator[RightFootPinky3SPlugOperator]
):
    __slots__ = ()

    RightFootPinky3Sx = DoubleField(default_value=1.0)

    RightFootPinky3Sy = DoubleField(default_value=1.0)

    RightFootPinky3Sz = DoubleField(default_value=1.0)


class RightFootPinky3SField(
    CompoundField[RightFootPinky3SAttrOperator, RightFootPinky3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky3SAttrOperator
    PLUG_CLS = RightFootPinky3SPlugOperator

    RightFootPinky3Sx = DoubleField(default_value=1.0)

    RightFootPinky3Sy = DoubleField(default_value=1.0)

    RightFootPinky3Sz = DoubleField(default_value=1.0)


class RightFootPinky4TPlugOperator(
    CompoundPlugOperator["RightFootPinky4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky4Tx", "RightFootPinky4Tx"),
        ("RightFootPinky4Ty", "RightFootPinky4Ty"),
        ("RightFootPinky4Tz", "RightFootPinky4Tz"),
    )

    RightFootPinky4Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky4Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky4Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky4TAttrOperator(
    CompoundAttrOperator[RightFootPinky4TPlugOperator]
):
    __slots__ = ()

    RightFootPinky4Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky4Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky4Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky4TField(
    CompoundField[RightFootPinky4TAttrOperator, RightFootPinky4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky4TAttrOperator
    PLUG_CLS = RightFootPinky4TPlugOperator

    RightFootPinky4Tx = DoubleLinearField(default_value=0.0)

    RightFootPinky4Ty = DoubleLinearField(default_value=0.0)

    RightFootPinky4Tz = DoubleLinearField(default_value=0.0)


class RightFootPinky4RPlugOperator(
    CompoundPlugOperator["RightFootPinky4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky4Rx", "RightFootPinky4Rx"),
        ("RightFootPinky4Ry", "RightFootPinky4Ry"),
        ("RightFootPinky4Rz", "RightFootPinky4Rz"),
    )

    RightFootPinky4Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky4Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky4Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky4RAttrOperator(
    CompoundAttrOperator[RightFootPinky4RPlugOperator]
):
    __slots__ = ()

    RightFootPinky4Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky4Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky4Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky4RField(
    CompoundField[RightFootPinky4RAttrOperator, RightFootPinky4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky4RAttrOperator
    PLUG_CLS = RightFootPinky4RPlugOperator

    RightFootPinky4Rx = DoubleAngleField(default_value=0.0)

    RightFootPinky4Ry = DoubleAngleField(default_value=0.0)

    RightFootPinky4Rz = DoubleAngleField(default_value=0.0)


class RightFootPinky4SPlugOperator(
    CompoundPlugOperator["RightFootPinky4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootPinky4Sx", "RightFootPinky4Sx"),
        ("RightFootPinky4Sy", "RightFootPinky4Sy"),
        ("RightFootPinky4Sz", "RightFootPinky4Sz"),
    )

    RightFootPinky4Sx = DoubleField(default_value=1.0)

    RightFootPinky4Sy = DoubleField(default_value=1.0)

    RightFootPinky4Sz = DoubleField(default_value=1.0)


class RightFootPinky4SAttrOperator(
    CompoundAttrOperator[RightFootPinky4SPlugOperator]
):
    __slots__ = ()

    RightFootPinky4Sx = DoubleField(default_value=1.0)

    RightFootPinky4Sy = DoubleField(default_value=1.0)

    RightFootPinky4Sz = DoubleField(default_value=1.0)


class RightFootPinky4SField(
    CompoundField[RightFootPinky4SAttrOperator, RightFootPinky4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootPinky4SAttrOperator
    PLUG_CLS = RightFootPinky4SPlugOperator

    RightFootPinky4Sx = DoubleField(default_value=1.0)

    RightFootPinky4Sy = DoubleField(default_value=1.0)

    RightFootPinky4Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger1TPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger1Tx", "RightFootExtraFinger1Tx"),
        ("RightFootExtraFinger1Ty", "RightFootExtraFinger1Ty"),
        ("RightFootExtraFinger1Tz", "RightFootExtraFinger1Tz"),
    )

    RightFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger1TAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger1TPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger1TField(
    CompoundField[RightFootExtraFinger1TAttrOperator, RightFootExtraFinger1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger1TAttrOperator
    PLUG_CLS = RightFootExtraFinger1TPlugOperator

    RightFootExtraFinger1Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger1Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger1RPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger1Rx", "RightFootExtraFinger1Rx"),
        ("RightFootExtraFinger1Ry", "RightFootExtraFinger1Ry"),
        ("RightFootExtraFinger1Rz", "RightFootExtraFinger1Rz"),
    )

    RightFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger1RAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger1RPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger1RField(
    CompoundField[RightFootExtraFinger1RAttrOperator, RightFootExtraFinger1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger1RAttrOperator
    PLUG_CLS = RightFootExtraFinger1RPlugOperator

    RightFootExtraFinger1Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger1Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger1SPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger1Sx", "RightFootExtraFinger1Sx"),
        ("RightFootExtraFinger1Sy", "RightFootExtraFinger1Sy"),
        ("RightFootExtraFinger1Sz", "RightFootExtraFinger1Sz"),
    )

    RightFootExtraFinger1Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger1SAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger1SPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger1Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger1SField(
    CompoundField[RightFootExtraFinger1SAttrOperator, RightFootExtraFinger1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger1SAttrOperator
    PLUG_CLS = RightFootExtraFinger1SPlugOperator

    RightFootExtraFinger1Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger1Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger2TPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger2Tx", "RightFootExtraFinger2Tx"),
        ("RightFootExtraFinger2Ty", "RightFootExtraFinger2Ty"),
        ("RightFootExtraFinger2Tz", "RightFootExtraFinger2Tz"),
    )

    RightFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger2TAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger2TPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger2TField(
    CompoundField[RightFootExtraFinger2TAttrOperator, RightFootExtraFinger2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger2TAttrOperator
    PLUG_CLS = RightFootExtraFinger2TPlugOperator

    RightFootExtraFinger2Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger2Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger2RPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger2Rx", "RightFootExtraFinger2Rx"),
        ("RightFootExtraFinger2Ry", "RightFootExtraFinger2Ry"),
        ("RightFootExtraFinger2Rz", "RightFootExtraFinger2Rz"),
    )

    RightFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger2RAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger2RPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger2RField(
    CompoundField[RightFootExtraFinger2RAttrOperator, RightFootExtraFinger2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger2RAttrOperator
    PLUG_CLS = RightFootExtraFinger2RPlugOperator

    RightFootExtraFinger2Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger2Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger2SPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger2Sx", "RightFootExtraFinger2Sx"),
        ("RightFootExtraFinger2Sy", "RightFootExtraFinger2Sy"),
        ("RightFootExtraFinger2Sz", "RightFootExtraFinger2Sz"),
    )

    RightFootExtraFinger2Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger2SAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger2SPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger2Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger2SField(
    CompoundField[RightFootExtraFinger2SAttrOperator, RightFootExtraFinger2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger2SAttrOperator
    PLUG_CLS = RightFootExtraFinger2SPlugOperator

    RightFootExtraFinger2Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger2Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger3TPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger3Tx", "RightFootExtraFinger3Tx"),
        ("RightFootExtraFinger3Ty", "RightFootExtraFinger3Ty"),
        ("RightFootExtraFinger3Tz", "RightFootExtraFinger3Tz"),
    )

    RightFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger3TAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger3TPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger3TField(
    CompoundField[RightFootExtraFinger3TAttrOperator, RightFootExtraFinger3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger3TAttrOperator
    PLUG_CLS = RightFootExtraFinger3TPlugOperator

    RightFootExtraFinger3Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger3Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger3RPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger3Rx", "RightFootExtraFinger3Rx"),
        ("RightFootExtraFinger3Ry", "RightFootExtraFinger3Ry"),
        ("RightFootExtraFinger3Rz", "RightFootExtraFinger3Rz"),
    )

    RightFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger3RAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger3RPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger3RField(
    CompoundField[RightFootExtraFinger3RAttrOperator, RightFootExtraFinger3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger3RAttrOperator
    PLUG_CLS = RightFootExtraFinger3RPlugOperator

    RightFootExtraFinger3Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger3Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger3SPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger3Sx", "RightFootExtraFinger3Sx"),
        ("RightFootExtraFinger3Sy", "RightFootExtraFinger3Sy"),
        ("RightFootExtraFinger3Sz", "RightFootExtraFinger3Sz"),
    )

    RightFootExtraFinger3Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger3SAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger3SPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger3Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger3SField(
    CompoundField[RightFootExtraFinger3SAttrOperator, RightFootExtraFinger3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger3SAttrOperator
    PLUG_CLS = RightFootExtraFinger3SPlugOperator

    RightFootExtraFinger3Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger3Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger4TPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger4Tx", "RightFootExtraFinger4Tx"),
        ("RightFootExtraFinger4Ty", "RightFootExtraFinger4Ty"),
        ("RightFootExtraFinger4Tz", "RightFootExtraFinger4Tz"),
    )

    RightFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger4TAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger4TPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger4TField(
    CompoundField[RightFootExtraFinger4TAttrOperator, RightFootExtraFinger4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger4TAttrOperator
    PLUG_CLS = RightFootExtraFinger4TPlugOperator

    RightFootExtraFinger4Tx = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Ty = DoubleLinearField(default_value=0.0)

    RightFootExtraFinger4Tz = DoubleLinearField(default_value=0.0)


class RightFootExtraFinger4RPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger4Rx", "RightFootExtraFinger4Rx"),
        ("RightFootExtraFinger4Ry", "RightFootExtraFinger4Ry"),
        ("RightFootExtraFinger4Rz", "RightFootExtraFinger4Rz"),
    )

    RightFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger4RAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger4RPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger4RField(
    CompoundField[RightFootExtraFinger4RAttrOperator, RightFootExtraFinger4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger4RAttrOperator
    PLUG_CLS = RightFootExtraFinger4RPlugOperator

    RightFootExtraFinger4Rx = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Ry = DoubleAngleField(default_value=0.0)

    RightFootExtraFinger4Rz = DoubleAngleField(default_value=0.0)


class RightFootExtraFinger4SPlugOperator(
    CompoundPlugOperator["RightFootExtraFinger4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightFootExtraFinger4Sx", "RightFootExtraFinger4Sx"),
        ("RightFootExtraFinger4Sy", "RightFootExtraFinger4Sy"),
        ("RightFootExtraFinger4Sz", "RightFootExtraFinger4Sz"),
    )

    RightFootExtraFinger4Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger4SAttrOperator(
    CompoundAttrOperator[RightFootExtraFinger4SPlugOperator]
):
    __slots__ = ()

    RightFootExtraFinger4Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sz = DoubleField(default_value=1.0)


class RightFootExtraFinger4SField(
    CompoundField[RightFootExtraFinger4SAttrOperator, RightFootExtraFinger4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightFootExtraFinger4SAttrOperator
    PLUG_CLS = RightFootExtraFinger4SPlugOperator

    RightFootExtraFinger4Sx = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sy = DoubleField(default_value=1.0)

    RightFootExtraFinger4Sz = DoubleField(default_value=1.0)


class LeftInHandThumbTPlugOperator(
    CompoundPlugOperator["LeftInHandThumbTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandThumbTx", "LeftInHandThumbTx"),
        ("LeftInHandThumbTy", "LeftInHandThumbTy"),
        ("LeftInHandThumbTz", "LeftInHandThumbTz"),
    )

    LeftInHandThumbTx = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTy = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTz = DoubleLinearField(default_value=0.0)


class LeftInHandThumbTAttrOperator(
    CompoundAttrOperator[LeftInHandThumbTPlugOperator]
):
    __slots__ = ()

    LeftInHandThumbTx = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTy = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTz = DoubleLinearField(default_value=0.0)


class LeftInHandThumbTField(
    CompoundField[LeftInHandThumbTAttrOperator, LeftInHandThumbTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandThumbTAttrOperator
    PLUG_CLS = LeftInHandThumbTPlugOperator

    LeftInHandThumbTx = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTy = DoubleLinearField(default_value=0.0)

    LeftInHandThumbTz = DoubleLinearField(default_value=0.0)


class LeftInHandThumbRPlugOperator(
    CompoundPlugOperator["LeftInHandThumbRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandThumbRx", "LeftInHandThumbRx"),
        ("LeftInHandThumbRy", "LeftInHandThumbRy"),
        ("LeftInHandThumbRz", "LeftInHandThumbRz"),
    )

    LeftInHandThumbRx = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRy = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRz = DoubleAngleField(default_value=0.0)


class LeftInHandThumbRAttrOperator(
    CompoundAttrOperator[LeftInHandThumbRPlugOperator]
):
    __slots__ = ()

    LeftInHandThumbRx = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRy = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRz = DoubleAngleField(default_value=0.0)


class LeftInHandThumbRField(
    CompoundField[LeftInHandThumbRAttrOperator, LeftInHandThumbRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandThumbRAttrOperator
    PLUG_CLS = LeftInHandThumbRPlugOperator

    LeftInHandThumbRx = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRy = DoubleAngleField(default_value=0.0)

    LeftInHandThumbRz = DoubleAngleField(default_value=0.0)


class LeftInHandThumbSPlugOperator(
    CompoundPlugOperator["LeftInHandThumbSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandThumbSx", "LeftInHandThumbSx"),
        ("LeftInHandThumbSy", "LeftInHandThumbSy"),
        ("LeftInHandThumbSz", "LeftInHandThumbSz"),
    )

    LeftInHandThumbSx = DoubleField(default_value=1.0)

    LeftInHandThumbSy = DoubleField(default_value=1.0)

    LeftInHandThumbSz = DoubleField(default_value=1.0)


class LeftInHandThumbSAttrOperator(
    CompoundAttrOperator[LeftInHandThumbSPlugOperator]
):
    __slots__ = ()

    LeftInHandThumbSx = DoubleField(default_value=1.0)

    LeftInHandThumbSy = DoubleField(default_value=1.0)

    LeftInHandThumbSz = DoubleField(default_value=1.0)


class LeftInHandThumbSField(
    CompoundField[LeftInHandThumbSAttrOperator, LeftInHandThumbSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandThumbSAttrOperator
    PLUG_CLS = LeftInHandThumbSPlugOperator

    LeftInHandThumbSx = DoubleField(default_value=1.0)

    LeftInHandThumbSy = DoubleField(default_value=1.0)

    LeftInHandThumbSz = DoubleField(default_value=1.0)


class LeftInHandIndexTPlugOperator(
    CompoundPlugOperator["LeftInHandIndexTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandIndexTx", "LeftInHandIndexTx"),
        ("LeftInHandIndexTy", "LeftInHandIndexTy"),
        ("LeftInHandIndexTz", "LeftInHandIndexTz"),
    )

    LeftInHandIndexTx = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTy = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTz = DoubleLinearField(default_value=0.0)


class LeftInHandIndexTAttrOperator(
    CompoundAttrOperator[LeftInHandIndexTPlugOperator]
):
    __slots__ = ()

    LeftInHandIndexTx = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTy = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTz = DoubleLinearField(default_value=0.0)


class LeftInHandIndexTField(
    CompoundField[LeftInHandIndexTAttrOperator, LeftInHandIndexTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandIndexTAttrOperator
    PLUG_CLS = LeftInHandIndexTPlugOperator

    LeftInHandIndexTx = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTy = DoubleLinearField(default_value=0.0)

    LeftInHandIndexTz = DoubleLinearField(default_value=0.0)


class LeftInHandIndexRPlugOperator(
    CompoundPlugOperator["LeftInHandIndexRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandIndexRx", "LeftInHandIndexRx"),
        ("LeftInHandIndexRy", "LeftInHandIndexRy"),
        ("LeftInHandIndexRz", "LeftInHandIndexRz"),
    )

    LeftInHandIndexRx = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRy = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRz = DoubleAngleField(default_value=0.0)


class LeftInHandIndexRAttrOperator(
    CompoundAttrOperator[LeftInHandIndexRPlugOperator]
):
    __slots__ = ()

    LeftInHandIndexRx = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRy = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRz = DoubleAngleField(default_value=0.0)


class LeftInHandIndexRField(
    CompoundField[LeftInHandIndexRAttrOperator, LeftInHandIndexRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandIndexRAttrOperator
    PLUG_CLS = LeftInHandIndexRPlugOperator

    LeftInHandIndexRx = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRy = DoubleAngleField(default_value=0.0)

    LeftInHandIndexRz = DoubleAngleField(default_value=0.0)


class LeftInHandIndexSPlugOperator(
    CompoundPlugOperator["LeftInHandIndexSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandIndexSx", "LeftInHandIndexSx"),
        ("LeftInHandIndexSy", "LeftInHandIndexSy"),
        ("LeftInHandIndexSz", "LeftInHandIndexSz"),
    )

    LeftInHandIndexSx = DoubleField(default_value=1.0)

    LeftInHandIndexSy = DoubleField(default_value=1.0)

    LeftInHandIndexSz = DoubleField(default_value=1.0)


class LeftInHandIndexSAttrOperator(
    CompoundAttrOperator[LeftInHandIndexSPlugOperator]
):
    __slots__ = ()

    LeftInHandIndexSx = DoubleField(default_value=1.0)

    LeftInHandIndexSy = DoubleField(default_value=1.0)

    LeftInHandIndexSz = DoubleField(default_value=1.0)


class LeftInHandIndexSField(
    CompoundField[LeftInHandIndexSAttrOperator, LeftInHandIndexSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandIndexSAttrOperator
    PLUG_CLS = LeftInHandIndexSPlugOperator

    LeftInHandIndexSx = DoubleField(default_value=1.0)

    LeftInHandIndexSy = DoubleField(default_value=1.0)

    LeftInHandIndexSz = DoubleField(default_value=1.0)


class LeftInHandMiddleTPlugOperator(
    CompoundPlugOperator["LeftInHandMiddleTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandMiddleTx", "LeftInHandMiddleTx"),
        ("LeftInHandMiddleTy", "LeftInHandMiddleTy"),
        ("LeftInHandMiddleTz", "LeftInHandMiddleTz"),
    )

    LeftInHandMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInHandMiddleTAttrOperator(
    CompoundAttrOperator[LeftInHandMiddleTPlugOperator]
):
    __slots__ = ()

    LeftInHandMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInHandMiddleTField(
    CompoundField[LeftInHandMiddleTAttrOperator, LeftInHandMiddleTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandMiddleTAttrOperator
    PLUG_CLS = LeftInHandMiddleTPlugOperator

    LeftInHandMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInHandMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInHandMiddleRPlugOperator(
    CompoundPlugOperator["LeftInHandMiddleRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandMiddleRx", "LeftInHandMiddleRx"),
        ("LeftInHandMiddleRy", "LeftInHandMiddleRy"),
        ("LeftInHandMiddleRz", "LeftInHandMiddleRz"),
    )

    LeftInHandMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInHandMiddleRAttrOperator(
    CompoundAttrOperator[LeftInHandMiddleRPlugOperator]
):
    __slots__ = ()

    LeftInHandMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInHandMiddleRField(
    CompoundField[LeftInHandMiddleRAttrOperator, LeftInHandMiddleRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandMiddleRAttrOperator
    PLUG_CLS = LeftInHandMiddleRPlugOperator

    LeftInHandMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInHandMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInHandMiddleSPlugOperator(
    CompoundPlugOperator["LeftInHandMiddleSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandMiddleSx", "LeftInHandMiddleSx"),
        ("LeftInHandMiddleSy", "LeftInHandMiddleSy"),
        ("LeftInHandMiddleSz", "LeftInHandMiddleSz"),
    )

    LeftInHandMiddleSx = DoubleField(default_value=1.0)

    LeftInHandMiddleSy = DoubleField(default_value=1.0)

    LeftInHandMiddleSz = DoubleField(default_value=1.0)


class LeftInHandMiddleSAttrOperator(
    CompoundAttrOperator[LeftInHandMiddleSPlugOperator]
):
    __slots__ = ()

    LeftInHandMiddleSx = DoubleField(default_value=1.0)

    LeftInHandMiddleSy = DoubleField(default_value=1.0)

    LeftInHandMiddleSz = DoubleField(default_value=1.0)


class LeftInHandMiddleSField(
    CompoundField[LeftInHandMiddleSAttrOperator, LeftInHandMiddleSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandMiddleSAttrOperator
    PLUG_CLS = LeftInHandMiddleSPlugOperator

    LeftInHandMiddleSx = DoubleField(default_value=1.0)

    LeftInHandMiddleSy = DoubleField(default_value=1.0)

    LeftInHandMiddleSz = DoubleField(default_value=1.0)


class LeftInHandRingTPlugOperator(
    CompoundPlugOperator["LeftInHandRingTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandRingTx", "LeftInHandRingTx"),
        ("LeftInHandRingTy", "LeftInHandRingTy"),
        ("LeftInHandRingTz", "LeftInHandRingTz"),
    )

    LeftInHandRingTx = DoubleLinearField(default_value=0.0)

    LeftInHandRingTy = DoubleLinearField(default_value=0.0)

    LeftInHandRingTz = DoubleLinearField(default_value=0.0)


class LeftInHandRingTAttrOperator(
    CompoundAttrOperator[LeftInHandRingTPlugOperator]
):
    __slots__ = ()

    LeftInHandRingTx = DoubleLinearField(default_value=0.0)

    LeftInHandRingTy = DoubleLinearField(default_value=0.0)

    LeftInHandRingTz = DoubleLinearField(default_value=0.0)


class LeftInHandRingTField(
    CompoundField[LeftInHandRingTAttrOperator, LeftInHandRingTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandRingTAttrOperator
    PLUG_CLS = LeftInHandRingTPlugOperator

    LeftInHandRingTx = DoubleLinearField(default_value=0.0)

    LeftInHandRingTy = DoubleLinearField(default_value=0.0)

    LeftInHandRingTz = DoubleLinearField(default_value=0.0)


class LeftInHandRingRPlugOperator(
    CompoundPlugOperator["LeftInHandRingRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandRingRx", "LeftInHandRingRx"),
        ("LeftInHandRingRy", "LeftInHandRingRy"),
        ("LeftInHandRingRz", "LeftInHandRingRz"),
    )

    LeftInHandRingRx = DoubleAngleField(default_value=0.0)

    LeftInHandRingRy = DoubleAngleField(default_value=0.0)

    LeftInHandRingRz = DoubleAngleField(default_value=0.0)


class LeftInHandRingRAttrOperator(
    CompoundAttrOperator[LeftInHandRingRPlugOperator]
):
    __slots__ = ()

    LeftInHandRingRx = DoubleAngleField(default_value=0.0)

    LeftInHandRingRy = DoubleAngleField(default_value=0.0)

    LeftInHandRingRz = DoubleAngleField(default_value=0.0)


class LeftInHandRingRField(
    CompoundField[LeftInHandRingRAttrOperator, LeftInHandRingRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandRingRAttrOperator
    PLUG_CLS = LeftInHandRingRPlugOperator

    LeftInHandRingRx = DoubleAngleField(default_value=0.0)

    LeftInHandRingRy = DoubleAngleField(default_value=0.0)

    LeftInHandRingRz = DoubleAngleField(default_value=0.0)


class LeftInHandRingSPlugOperator(
    CompoundPlugOperator["LeftInHandRingSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandRingSx", "LeftInHandRingSx"),
        ("LeftInHandRingSy", "LeftInHandRingSy"),
        ("LeftInHandRingSz", "LeftInHandRingSz"),
    )

    LeftInHandRingSx = DoubleField(default_value=1.0)

    LeftInHandRingSy = DoubleField(default_value=1.0)

    LeftInHandRingSz = DoubleField(default_value=1.0)


class LeftInHandRingSAttrOperator(
    CompoundAttrOperator[LeftInHandRingSPlugOperator]
):
    __slots__ = ()

    LeftInHandRingSx = DoubleField(default_value=1.0)

    LeftInHandRingSy = DoubleField(default_value=1.0)

    LeftInHandRingSz = DoubleField(default_value=1.0)


class LeftInHandRingSField(
    CompoundField[LeftInHandRingSAttrOperator, LeftInHandRingSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandRingSAttrOperator
    PLUG_CLS = LeftInHandRingSPlugOperator

    LeftInHandRingSx = DoubleField(default_value=1.0)

    LeftInHandRingSy = DoubleField(default_value=1.0)

    LeftInHandRingSz = DoubleField(default_value=1.0)


class LeftInHandPinkyTPlugOperator(
    CompoundPlugOperator["LeftInHandPinkyTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandPinkyTx", "LeftInHandPinkyTx"),
        ("LeftInHandPinkyTy", "LeftInHandPinkyTy"),
        ("LeftInHandPinkyTz", "LeftInHandPinkyTz"),
    )

    LeftInHandPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInHandPinkyTAttrOperator(
    CompoundAttrOperator[LeftInHandPinkyTPlugOperator]
):
    __slots__ = ()

    LeftInHandPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInHandPinkyTField(
    CompoundField[LeftInHandPinkyTAttrOperator, LeftInHandPinkyTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandPinkyTAttrOperator
    PLUG_CLS = LeftInHandPinkyTPlugOperator

    LeftInHandPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInHandPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInHandPinkyRPlugOperator(
    CompoundPlugOperator["LeftInHandPinkyRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandPinkyRx", "LeftInHandPinkyRx"),
        ("LeftInHandPinkyRy", "LeftInHandPinkyRy"),
        ("LeftInHandPinkyRz", "LeftInHandPinkyRz"),
    )

    LeftInHandPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInHandPinkyRAttrOperator(
    CompoundAttrOperator[LeftInHandPinkyRPlugOperator]
):
    __slots__ = ()

    LeftInHandPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInHandPinkyRField(
    CompoundField[LeftInHandPinkyRAttrOperator, LeftInHandPinkyRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandPinkyRAttrOperator
    PLUG_CLS = LeftInHandPinkyRPlugOperator

    LeftInHandPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInHandPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInHandPinkySPlugOperator(
    CompoundPlugOperator["LeftInHandPinkySAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandPinkySx", "LeftInHandPinkySx"),
        ("LeftInHandPinkySy", "LeftInHandPinkySy"),
        ("LeftInHandPinkySz", "LeftInHandPinkySz"),
    )

    LeftInHandPinkySx = DoubleField(default_value=1.0)

    LeftInHandPinkySy = DoubleField(default_value=1.0)

    LeftInHandPinkySz = DoubleField(default_value=1.0)


class LeftInHandPinkySAttrOperator(
    CompoundAttrOperator[LeftInHandPinkySPlugOperator]
):
    __slots__ = ()

    LeftInHandPinkySx = DoubleField(default_value=1.0)

    LeftInHandPinkySy = DoubleField(default_value=1.0)

    LeftInHandPinkySz = DoubleField(default_value=1.0)


class LeftInHandPinkySField(
    CompoundField[LeftInHandPinkySAttrOperator, LeftInHandPinkySPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandPinkySAttrOperator
    PLUG_CLS = LeftInHandPinkySPlugOperator

    LeftInHandPinkySx = DoubleField(default_value=1.0)

    LeftInHandPinkySy = DoubleField(default_value=1.0)

    LeftInHandPinkySz = DoubleField(default_value=1.0)


class LeftInHandExtraFingerTPlugOperator(
    CompoundPlugOperator["LeftInHandExtraFingerTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandExtraFingerTx", "LeftInHandExtraFingerTx"),
        ("LeftInHandExtraFingerTy", "LeftInHandExtraFingerTy"),
        ("LeftInHandExtraFingerTz", "LeftInHandExtraFingerTz"),
    )

    LeftInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInHandExtraFingerTAttrOperator(
    CompoundAttrOperator[LeftInHandExtraFingerTPlugOperator]
):
    __slots__ = ()

    LeftInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInHandExtraFingerTField(
    CompoundField[LeftInHandExtraFingerTAttrOperator, LeftInHandExtraFingerTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandExtraFingerTAttrOperator
    PLUG_CLS = LeftInHandExtraFingerTPlugOperator

    LeftInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInHandExtraFingerRPlugOperator(
    CompoundPlugOperator["LeftInHandExtraFingerRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandExtraFingerRx", "LeftInHandExtraFingerRx"),
        ("LeftInHandExtraFingerRy", "LeftInHandExtraFingerRy"),
        ("LeftInHandExtraFingerRz", "LeftInHandExtraFingerRz"),
    )

    LeftInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInHandExtraFingerRAttrOperator(
    CompoundAttrOperator[LeftInHandExtraFingerRPlugOperator]
):
    __slots__ = ()

    LeftInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInHandExtraFingerRField(
    CompoundField[LeftInHandExtraFingerRAttrOperator, LeftInHandExtraFingerRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandExtraFingerRAttrOperator
    PLUG_CLS = LeftInHandExtraFingerRPlugOperator

    LeftInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInHandExtraFingerSPlugOperator(
    CompoundPlugOperator["LeftInHandExtraFingerSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInHandExtraFingerSx", "LeftInHandExtraFingerSx"),
        ("LeftInHandExtraFingerSy", "LeftInHandExtraFingerSy"),
        ("LeftInHandExtraFingerSz", "LeftInHandExtraFingerSz"),
    )

    LeftInHandExtraFingerSx = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSy = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSz = DoubleField(default_value=1.0)


class LeftInHandExtraFingerSAttrOperator(
    CompoundAttrOperator[LeftInHandExtraFingerSPlugOperator]
):
    __slots__ = ()

    LeftInHandExtraFingerSx = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSy = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSz = DoubleField(default_value=1.0)


class LeftInHandExtraFingerSField(
    CompoundField[LeftInHandExtraFingerSAttrOperator, LeftInHandExtraFingerSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInHandExtraFingerSAttrOperator
    PLUG_CLS = LeftInHandExtraFingerSPlugOperator

    LeftInHandExtraFingerSx = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSy = DoubleField(default_value=1.0)

    LeftInHandExtraFingerSz = DoubleField(default_value=1.0)


class RightInHandThumbTPlugOperator(
    CompoundPlugOperator["RightInHandThumbTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandThumbTx", "RightInHandThumbTx"),
        ("RightInHandThumbTy", "RightInHandThumbTy"),
        ("RightInHandThumbTz", "RightInHandThumbTz"),
    )

    RightInHandThumbTx = DoubleLinearField(default_value=0.0)

    RightInHandThumbTy = DoubleLinearField(default_value=0.0)

    RightInHandThumbTz = DoubleLinearField(default_value=0.0)


class RightInHandThumbTAttrOperator(
    CompoundAttrOperator[RightInHandThumbTPlugOperator]
):
    __slots__ = ()

    RightInHandThumbTx = DoubleLinearField(default_value=0.0)

    RightInHandThumbTy = DoubleLinearField(default_value=0.0)

    RightInHandThumbTz = DoubleLinearField(default_value=0.0)


class RightInHandThumbTField(
    CompoundField[RightInHandThumbTAttrOperator, RightInHandThumbTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandThumbTAttrOperator
    PLUG_CLS = RightInHandThumbTPlugOperator

    RightInHandThumbTx = DoubleLinearField(default_value=0.0)

    RightInHandThumbTy = DoubleLinearField(default_value=0.0)

    RightInHandThumbTz = DoubleLinearField(default_value=0.0)


class RightInHandThumbRPlugOperator(
    CompoundPlugOperator["RightInHandThumbRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandThumbRx", "RightInHandThumbRx"),
        ("RightInHandThumbRy", "RightInHandThumbRy"),
        ("RightInHandThumbRz", "RightInHandThumbRz"),
    )

    RightInHandThumbRx = DoubleAngleField(default_value=0.0)

    RightInHandThumbRy = DoubleAngleField(default_value=0.0)

    RightInHandThumbRz = DoubleAngleField(default_value=0.0)


class RightInHandThumbRAttrOperator(
    CompoundAttrOperator[RightInHandThumbRPlugOperator]
):
    __slots__ = ()

    RightInHandThumbRx = DoubleAngleField(default_value=0.0)

    RightInHandThumbRy = DoubleAngleField(default_value=0.0)

    RightInHandThumbRz = DoubleAngleField(default_value=0.0)


class RightInHandThumbRField(
    CompoundField[RightInHandThumbRAttrOperator, RightInHandThumbRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandThumbRAttrOperator
    PLUG_CLS = RightInHandThumbRPlugOperator

    RightInHandThumbRx = DoubleAngleField(default_value=0.0)

    RightInHandThumbRy = DoubleAngleField(default_value=0.0)

    RightInHandThumbRz = DoubleAngleField(default_value=0.0)


class RightInHandThumbSPlugOperator(
    CompoundPlugOperator["RightInHandThumbSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandThumbSx", "RightInHandThumbSx"),
        ("RightInHandThumbSy", "RightInHandThumbSy"),
        ("RightInHandThumbSz", "RightInHandThumbSz"),
    )

    RightInHandThumbSx = DoubleField(default_value=1.0)

    RightInHandThumbSy = DoubleField(default_value=1.0)

    RightInHandThumbSz = DoubleField(default_value=1.0)


class RightInHandThumbSAttrOperator(
    CompoundAttrOperator[RightInHandThumbSPlugOperator]
):
    __slots__ = ()

    RightInHandThumbSx = DoubleField(default_value=1.0)

    RightInHandThumbSy = DoubleField(default_value=1.0)

    RightInHandThumbSz = DoubleField(default_value=1.0)


class RightInHandThumbSField(
    CompoundField[RightInHandThumbSAttrOperator, RightInHandThumbSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandThumbSAttrOperator
    PLUG_CLS = RightInHandThumbSPlugOperator

    RightInHandThumbSx = DoubleField(default_value=1.0)

    RightInHandThumbSy = DoubleField(default_value=1.0)

    RightInHandThumbSz = DoubleField(default_value=1.0)


class RightInHandIndexTPlugOperator(
    CompoundPlugOperator["RightInHandIndexTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandIndexTx", "RightInHandIndexTx"),
        ("RightInHandIndexTy", "RightInHandIndexTy"),
        ("RightInHandIndexTz", "RightInHandIndexTz"),
    )

    RightInHandIndexTx = DoubleLinearField(default_value=0.0)

    RightInHandIndexTy = DoubleLinearField(default_value=0.0)

    RightInHandIndexTz = DoubleLinearField(default_value=0.0)


class RightInHandIndexTAttrOperator(
    CompoundAttrOperator[RightInHandIndexTPlugOperator]
):
    __slots__ = ()

    RightInHandIndexTx = DoubleLinearField(default_value=0.0)

    RightInHandIndexTy = DoubleLinearField(default_value=0.0)

    RightInHandIndexTz = DoubleLinearField(default_value=0.0)


class RightInHandIndexTField(
    CompoundField[RightInHandIndexTAttrOperator, RightInHandIndexTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandIndexTAttrOperator
    PLUG_CLS = RightInHandIndexTPlugOperator

    RightInHandIndexTx = DoubleLinearField(default_value=0.0)

    RightInHandIndexTy = DoubleLinearField(default_value=0.0)

    RightInHandIndexTz = DoubleLinearField(default_value=0.0)


class RightInHandIndexRPlugOperator(
    CompoundPlugOperator["RightInHandIndexRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandIndexRx", "RightInHandIndexRx"),
        ("RightInHandIndexRy", "RightInHandIndexRy"),
        ("RightInHandIndexRz", "RightInHandIndexRz"),
    )

    RightInHandIndexRx = DoubleAngleField(default_value=0.0)

    RightInHandIndexRy = DoubleAngleField(default_value=0.0)

    RightInHandIndexRz = DoubleAngleField(default_value=0.0)


class RightInHandIndexRAttrOperator(
    CompoundAttrOperator[RightInHandIndexRPlugOperator]
):
    __slots__ = ()

    RightInHandIndexRx = DoubleAngleField(default_value=0.0)

    RightInHandIndexRy = DoubleAngleField(default_value=0.0)

    RightInHandIndexRz = DoubleAngleField(default_value=0.0)


class RightInHandIndexRField(
    CompoundField[RightInHandIndexRAttrOperator, RightInHandIndexRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandIndexRAttrOperator
    PLUG_CLS = RightInHandIndexRPlugOperator

    RightInHandIndexRx = DoubleAngleField(default_value=0.0)

    RightInHandIndexRy = DoubleAngleField(default_value=0.0)

    RightInHandIndexRz = DoubleAngleField(default_value=0.0)


class RightInHandIndexSPlugOperator(
    CompoundPlugOperator["RightInHandIndexSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandIndexSx", "RightInHandIndexSx"),
        ("RightInHandIndexSy", "RightInHandIndexSy"),
        ("RightInHandIndexSz", "RightInHandIndexSz"),
    )

    RightInHandIndexSx = DoubleField(default_value=1.0)

    RightInHandIndexSy = DoubleField(default_value=1.0)

    RightInHandIndexSz = DoubleField(default_value=1.0)


class RightInHandIndexSAttrOperator(
    CompoundAttrOperator[RightInHandIndexSPlugOperator]
):
    __slots__ = ()

    RightInHandIndexSx = DoubleField(default_value=1.0)

    RightInHandIndexSy = DoubleField(default_value=1.0)

    RightInHandIndexSz = DoubleField(default_value=1.0)


class RightInHandIndexSField(
    CompoundField[RightInHandIndexSAttrOperator, RightInHandIndexSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandIndexSAttrOperator
    PLUG_CLS = RightInHandIndexSPlugOperator

    RightInHandIndexSx = DoubleField(default_value=1.0)

    RightInHandIndexSy = DoubleField(default_value=1.0)

    RightInHandIndexSz = DoubleField(default_value=1.0)


class RightInHandMiddleTPlugOperator(
    CompoundPlugOperator["RightInHandMiddleTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandMiddleTx", "RightInHandMiddleTx"),
        ("RightInHandMiddleTy", "RightInHandMiddleTy"),
        ("RightInHandMiddleTz", "RightInHandMiddleTz"),
    )

    RightInHandMiddleTx = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTy = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTz = DoubleLinearField(default_value=0.0)


class RightInHandMiddleTAttrOperator(
    CompoundAttrOperator[RightInHandMiddleTPlugOperator]
):
    __slots__ = ()

    RightInHandMiddleTx = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTy = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTz = DoubleLinearField(default_value=0.0)


class RightInHandMiddleTField(
    CompoundField[RightInHandMiddleTAttrOperator, RightInHandMiddleTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandMiddleTAttrOperator
    PLUG_CLS = RightInHandMiddleTPlugOperator

    RightInHandMiddleTx = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTy = DoubleLinearField(default_value=0.0)

    RightInHandMiddleTz = DoubleLinearField(default_value=0.0)


class RightInHandMiddleRPlugOperator(
    CompoundPlugOperator["RightInHandMiddleRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandMiddleRx", "RightInHandMiddleRx"),
        ("RightInHandMiddleRy", "RightInHandMiddleRy"),
        ("RightInHandMiddleRz", "RightInHandMiddleRz"),
    )

    RightInHandMiddleRx = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRy = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRz = DoubleAngleField(default_value=0.0)


class RightInHandMiddleRAttrOperator(
    CompoundAttrOperator[RightInHandMiddleRPlugOperator]
):
    __slots__ = ()

    RightInHandMiddleRx = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRy = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRz = DoubleAngleField(default_value=0.0)


class RightInHandMiddleRField(
    CompoundField[RightInHandMiddleRAttrOperator, RightInHandMiddleRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandMiddleRAttrOperator
    PLUG_CLS = RightInHandMiddleRPlugOperator

    RightInHandMiddleRx = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRy = DoubleAngleField(default_value=0.0)

    RightInHandMiddleRz = DoubleAngleField(default_value=0.0)


class RightInHandMiddleSPlugOperator(
    CompoundPlugOperator["RightInHandMiddleSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandMiddleSx", "RightInHandMiddleSx"),
        ("RightInHandMiddleSy", "RightInHandMiddleSy"),
        ("RightInHandMiddleSz", "RightInHandMiddleSz"),
    )

    RightInHandMiddleSx = DoubleField(default_value=1.0)

    RightInHandMiddleSy = DoubleField(default_value=1.0)

    RightInHandMiddleSz = DoubleField(default_value=1.0)


class RightInHandMiddleSAttrOperator(
    CompoundAttrOperator[RightInHandMiddleSPlugOperator]
):
    __slots__ = ()

    RightInHandMiddleSx = DoubleField(default_value=1.0)

    RightInHandMiddleSy = DoubleField(default_value=1.0)

    RightInHandMiddleSz = DoubleField(default_value=1.0)


class RightInHandMiddleSField(
    CompoundField[RightInHandMiddleSAttrOperator, RightInHandMiddleSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandMiddleSAttrOperator
    PLUG_CLS = RightInHandMiddleSPlugOperator

    RightInHandMiddleSx = DoubleField(default_value=1.0)

    RightInHandMiddleSy = DoubleField(default_value=1.0)

    RightInHandMiddleSz = DoubleField(default_value=1.0)


class RightInHandRingTPlugOperator(
    CompoundPlugOperator["RightInHandRingTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandRingTx", "RightInHandRingTx"),
        ("RightInHandRingTy", "RightInHandRingTy"),
        ("RightInHandRingTz", "RightInHandRingTz"),
    )

    RightInHandRingTx = DoubleLinearField(default_value=0.0)

    RightInHandRingTy = DoubleLinearField(default_value=0.0)

    RightInHandRingTz = DoubleLinearField(default_value=0.0)


class RightInHandRingTAttrOperator(
    CompoundAttrOperator[RightInHandRingTPlugOperator]
):
    __slots__ = ()

    RightInHandRingTx = DoubleLinearField(default_value=0.0)

    RightInHandRingTy = DoubleLinearField(default_value=0.0)

    RightInHandRingTz = DoubleLinearField(default_value=0.0)


class RightInHandRingTField(
    CompoundField[RightInHandRingTAttrOperator, RightInHandRingTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandRingTAttrOperator
    PLUG_CLS = RightInHandRingTPlugOperator

    RightInHandRingTx = DoubleLinearField(default_value=0.0)

    RightInHandRingTy = DoubleLinearField(default_value=0.0)

    RightInHandRingTz = DoubleLinearField(default_value=0.0)


class RightInHandRingRPlugOperator(
    CompoundPlugOperator["RightInHandRingRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandRingRx", "RightInHandRingRx"),
        ("RightInHandRingRy", "RightInHandRingRy"),
        ("RightInHandRingRz", "RightInHandRingRz"),
    )

    RightInHandRingRx = DoubleAngleField(default_value=0.0)

    RightInHandRingRy = DoubleAngleField(default_value=0.0)

    RightInHandRingRz = DoubleAngleField(default_value=0.0)


class RightInHandRingRAttrOperator(
    CompoundAttrOperator[RightInHandRingRPlugOperator]
):
    __slots__ = ()

    RightInHandRingRx = DoubleAngleField(default_value=0.0)

    RightInHandRingRy = DoubleAngleField(default_value=0.0)

    RightInHandRingRz = DoubleAngleField(default_value=0.0)


class RightInHandRingRField(
    CompoundField[RightInHandRingRAttrOperator, RightInHandRingRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandRingRAttrOperator
    PLUG_CLS = RightInHandRingRPlugOperator

    RightInHandRingRx = DoubleAngleField(default_value=0.0)

    RightInHandRingRy = DoubleAngleField(default_value=0.0)

    RightInHandRingRz = DoubleAngleField(default_value=0.0)


class RightInHandRingSPlugOperator(
    CompoundPlugOperator["RightInHandRingSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandRingSx", "RightInHandRingSx"),
        ("RightInHandRingSy", "RightInHandRingSy"),
        ("RightInHandRingSz", "RightInHandRingSz"),
    )

    RightInHandRingSx = DoubleField(default_value=1.0)

    RightInHandRingSy = DoubleField(default_value=1.0)

    RightInHandRingSz = DoubleField(default_value=1.0)


class RightInHandRingSAttrOperator(
    CompoundAttrOperator[RightInHandRingSPlugOperator]
):
    __slots__ = ()

    RightInHandRingSx = DoubleField(default_value=1.0)

    RightInHandRingSy = DoubleField(default_value=1.0)

    RightInHandRingSz = DoubleField(default_value=1.0)


class RightInHandRingSField(
    CompoundField[RightInHandRingSAttrOperator, RightInHandRingSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandRingSAttrOperator
    PLUG_CLS = RightInHandRingSPlugOperator

    RightInHandRingSx = DoubleField(default_value=1.0)

    RightInHandRingSy = DoubleField(default_value=1.0)

    RightInHandRingSz = DoubleField(default_value=1.0)


class RightInHandPinkyTPlugOperator(
    CompoundPlugOperator["RightInHandPinkyTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandPinkyTx", "RightInHandPinkyTx"),
        ("RightInHandPinkyTy", "RightInHandPinkyTy"),
        ("RightInHandPinkyTz", "RightInHandPinkyTz"),
    )

    RightInHandPinkyTx = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTy = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTz = DoubleLinearField(default_value=0.0)


class RightInHandPinkyTAttrOperator(
    CompoundAttrOperator[RightInHandPinkyTPlugOperator]
):
    __slots__ = ()

    RightInHandPinkyTx = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTy = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTz = DoubleLinearField(default_value=0.0)


class RightInHandPinkyTField(
    CompoundField[RightInHandPinkyTAttrOperator, RightInHandPinkyTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandPinkyTAttrOperator
    PLUG_CLS = RightInHandPinkyTPlugOperator

    RightInHandPinkyTx = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTy = DoubleLinearField(default_value=0.0)

    RightInHandPinkyTz = DoubleLinearField(default_value=0.0)


class RightInHandPinkyRPlugOperator(
    CompoundPlugOperator["RightInHandPinkyRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandPinkyRx", "RightInHandPinkyRx"),
        ("RightInHandPinkyRy", "RightInHandPinkyRy"),
        ("RightInHandPinkyRz", "RightInHandPinkyRz"),
    )

    RightInHandPinkyRx = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRy = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRz = DoubleAngleField(default_value=0.0)


class RightInHandPinkyRAttrOperator(
    CompoundAttrOperator[RightInHandPinkyRPlugOperator]
):
    __slots__ = ()

    RightInHandPinkyRx = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRy = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRz = DoubleAngleField(default_value=0.0)


class RightInHandPinkyRField(
    CompoundField[RightInHandPinkyRAttrOperator, RightInHandPinkyRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandPinkyRAttrOperator
    PLUG_CLS = RightInHandPinkyRPlugOperator

    RightInHandPinkyRx = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRy = DoubleAngleField(default_value=0.0)

    RightInHandPinkyRz = DoubleAngleField(default_value=0.0)


class RightInHandPinkySPlugOperator(
    CompoundPlugOperator["RightInHandPinkySAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandPinkySx", "RightInHandPinkySx"),
        ("RightInHandPinkySy", "RightInHandPinkySy"),
        ("RightInHandPinkySz", "RightInHandPinkySz"),
    )

    RightInHandPinkySx = DoubleField(default_value=1.0)

    RightInHandPinkySy = DoubleField(default_value=1.0)

    RightInHandPinkySz = DoubleField(default_value=1.0)


class RightInHandPinkySAttrOperator(
    CompoundAttrOperator[RightInHandPinkySPlugOperator]
):
    __slots__ = ()

    RightInHandPinkySx = DoubleField(default_value=1.0)

    RightInHandPinkySy = DoubleField(default_value=1.0)

    RightInHandPinkySz = DoubleField(default_value=1.0)


class RightInHandPinkySField(
    CompoundField[RightInHandPinkySAttrOperator, RightInHandPinkySPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandPinkySAttrOperator
    PLUG_CLS = RightInHandPinkySPlugOperator

    RightInHandPinkySx = DoubleField(default_value=1.0)

    RightInHandPinkySy = DoubleField(default_value=1.0)

    RightInHandPinkySz = DoubleField(default_value=1.0)


class RightInHandExtraFingerTPlugOperator(
    CompoundPlugOperator["RightInHandExtraFingerTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandExtraFingerTx", "RightInHandExtraFingerTx"),
        ("RightInHandExtraFingerTy", "RightInHandExtraFingerTy"),
        ("RightInHandExtraFingerTz", "RightInHandExtraFingerTz"),
    )

    RightInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInHandExtraFingerTAttrOperator(
    CompoundAttrOperator[RightInHandExtraFingerTPlugOperator]
):
    __slots__ = ()

    RightInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInHandExtraFingerTField(
    CompoundField[RightInHandExtraFingerTAttrOperator, RightInHandExtraFingerTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandExtraFingerTAttrOperator
    PLUG_CLS = RightInHandExtraFingerTPlugOperator

    RightInHandExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInHandExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInHandExtraFingerRPlugOperator(
    CompoundPlugOperator["RightInHandExtraFingerRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandExtraFingerRx", "RightInHandExtraFingerRx"),
        ("RightInHandExtraFingerRy", "RightInHandExtraFingerRy"),
        ("RightInHandExtraFingerRz", "RightInHandExtraFingerRz"),
    )

    RightInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInHandExtraFingerRAttrOperator(
    CompoundAttrOperator[RightInHandExtraFingerRPlugOperator]
):
    __slots__ = ()

    RightInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInHandExtraFingerRField(
    CompoundField[RightInHandExtraFingerRAttrOperator, RightInHandExtraFingerRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandExtraFingerRAttrOperator
    PLUG_CLS = RightInHandExtraFingerRPlugOperator

    RightInHandExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInHandExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInHandExtraFingerSPlugOperator(
    CompoundPlugOperator["RightInHandExtraFingerSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInHandExtraFingerSx", "RightInHandExtraFingerSx"),
        ("RightInHandExtraFingerSy", "RightInHandExtraFingerSy"),
        ("RightInHandExtraFingerSz", "RightInHandExtraFingerSz"),
    )

    RightInHandExtraFingerSx = DoubleField(default_value=1.0)

    RightInHandExtraFingerSy = DoubleField(default_value=1.0)

    RightInHandExtraFingerSz = DoubleField(default_value=1.0)


class RightInHandExtraFingerSAttrOperator(
    CompoundAttrOperator[RightInHandExtraFingerSPlugOperator]
):
    __slots__ = ()

    RightInHandExtraFingerSx = DoubleField(default_value=1.0)

    RightInHandExtraFingerSy = DoubleField(default_value=1.0)

    RightInHandExtraFingerSz = DoubleField(default_value=1.0)


class RightInHandExtraFingerSField(
    CompoundField[RightInHandExtraFingerSAttrOperator, RightInHandExtraFingerSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInHandExtraFingerSAttrOperator
    PLUG_CLS = RightInHandExtraFingerSPlugOperator

    RightInHandExtraFingerSx = DoubleField(default_value=1.0)

    RightInHandExtraFingerSy = DoubleField(default_value=1.0)

    RightInHandExtraFingerSz = DoubleField(default_value=1.0)


class LeftInFootThumbTPlugOperator(
    CompoundPlugOperator["LeftInFootThumbTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootThumbTx", "LeftInFootThumbTx"),
        ("LeftInFootThumbTy", "LeftInFootThumbTy"),
        ("LeftInFootThumbTz", "LeftInFootThumbTz"),
    )

    LeftInFootThumbTx = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTy = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTz = DoubleLinearField(default_value=0.0)


class LeftInFootThumbTAttrOperator(
    CompoundAttrOperator[LeftInFootThumbTPlugOperator]
):
    __slots__ = ()

    LeftInFootThumbTx = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTy = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTz = DoubleLinearField(default_value=0.0)


class LeftInFootThumbTField(
    CompoundField[LeftInFootThumbTAttrOperator, LeftInFootThumbTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootThumbTAttrOperator
    PLUG_CLS = LeftInFootThumbTPlugOperator

    LeftInFootThumbTx = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTy = DoubleLinearField(default_value=0.0)

    LeftInFootThumbTz = DoubleLinearField(default_value=0.0)


class LeftInFootThumbRPlugOperator(
    CompoundPlugOperator["LeftInFootThumbRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootThumbRx", "LeftInFootThumbRx"),
        ("LeftInFootThumbRy", "LeftInFootThumbRy"),
        ("LeftInFootThumbRz", "LeftInFootThumbRz"),
    )

    LeftInFootThumbRx = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRy = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRz = DoubleAngleField(default_value=0.0)


class LeftInFootThumbRAttrOperator(
    CompoundAttrOperator[LeftInFootThumbRPlugOperator]
):
    __slots__ = ()

    LeftInFootThumbRx = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRy = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRz = DoubleAngleField(default_value=0.0)


class LeftInFootThumbRField(
    CompoundField[LeftInFootThumbRAttrOperator, LeftInFootThumbRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootThumbRAttrOperator
    PLUG_CLS = LeftInFootThumbRPlugOperator

    LeftInFootThumbRx = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRy = DoubleAngleField(default_value=0.0)

    LeftInFootThumbRz = DoubleAngleField(default_value=0.0)


class LeftInFootThumbSPlugOperator(
    CompoundPlugOperator["LeftInFootThumbSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootThumbSx", "LeftInFootThumbSx"),
        ("LeftInFootThumbSy", "LeftInFootThumbSy"),
        ("LeftInFootThumbSz", "LeftInFootThumbSz"),
    )

    LeftInFootThumbSx = DoubleField(default_value=1.0)

    LeftInFootThumbSy = DoubleField(default_value=1.0)

    LeftInFootThumbSz = DoubleField(default_value=1.0)


class LeftInFootThumbSAttrOperator(
    CompoundAttrOperator[LeftInFootThumbSPlugOperator]
):
    __slots__ = ()

    LeftInFootThumbSx = DoubleField(default_value=1.0)

    LeftInFootThumbSy = DoubleField(default_value=1.0)

    LeftInFootThumbSz = DoubleField(default_value=1.0)


class LeftInFootThumbSField(
    CompoundField[LeftInFootThumbSAttrOperator, LeftInFootThumbSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootThumbSAttrOperator
    PLUG_CLS = LeftInFootThumbSPlugOperator

    LeftInFootThumbSx = DoubleField(default_value=1.0)

    LeftInFootThumbSy = DoubleField(default_value=1.0)

    LeftInFootThumbSz = DoubleField(default_value=1.0)


class LeftInFootIndexTPlugOperator(
    CompoundPlugOperator["LeftInFootIndexTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootIndexTx", "LeftInFootIndexTx"),
        ("LeftInFootIndexTy", "LeftInFootIndexTy"),
        ("LeftInFootIndexTz", "LeftInFootIndexTz"),
    )

    LeftInFootIndexTx = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTy = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTz = DoubleLinearField(default_value=0.0)


class LeftInFootIndexTAttrOperator(
    CompoundAttrOperator[LeftInFootIndexTPlugOperator]
):
    __slots__ = ()

    LeftInFootIndexTx = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTy = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTz = DoubleLinearField(default_value=0.0)


class LeftInFootIndexTField(
    CompoundField[LeftInFootIndexTAttrOperator, LeftInFootIndexTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootIndexTAttrOperator
    PLUG_CLS = LeftInFootIndexTPlugOperator

    LeftInFootIndexTx = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTy = DoubleLinearField(default_value=0.0)

    LeftInFootIndexTz = DoubleLinearField(default_value=0.0)


class LeftInFootIndexRPlugOperator(
    CompoundPlugOperator["LeftInFootIndexRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootIndexRx", "LeftInFootIndexRx"),
        ("LeftInFootIndexRy", "LeftInFootIndexRy"),
        ("LeftInFootIndexRz", "LeftInFootIndexRz"),
    )

    LeftInFootIndexRx = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRy = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRz = DoubleAngleField(default_value=0.0)


class LeftInFootIndexRAttrOperator(
    CompoundAttrOperator[LeftInFootIndexRPlugOperator]
):
    __slots__ = ()

    LeftInFootIndexRx = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRy = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRz = DoubleAngleField(default_value=0.0)


class LeftInFootIndexRField(
    CompoundField[LeftInFootIndexRAttrOperator, LeftInFootIndexRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootIndexRAttrOperator
    PLUG_CLS = LeftInFootIndexRPlugOperator

    LeftInFootIndexRx = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRy = DoubleAngleField(default_value=0.0)

    LeftInFootIndexRz = DoubleAngleField(default_value=0.0)


class LeftInFootIndexSPlugOperator(
    CompoundPlugOperator["LeftInFootIndexSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootIndexSx", "LeftInFootIndexSx"),
        ("LeftInFootIndexSy", "LeftInFootIndexSy"),
        ("LeftInFootIndexSz", "LeftInFootIndexSz"),
    )

    LeftInFootIndexSx = DoubleField(default_value=1.0)

    LeftInFootIndexSy = DoubleField(default_value=1.0)

    LeftInFootIndexSz = DoubleField(default_value=1.0)


class LeftInFootIndexSAttrOperator(
    CompoundAttrOperator[LeftInFootIndexSPlugOperator]
):
    __slots__ = ()

    LeftInFootIndexSx = DoubleField(default_value=1.0)

    LeftInFootIndexSy = DoubleField(default_value=1.0)

    LeftInFootIndexSz = DoubleField(default_value=1.0)


class LeftInFootIndexSField(
    CompoundField[LeftInFootIndexSAttrOperator, LeftInFootIndexSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootIndexSAttrOperator
    PLUG_CLS = LeftInFootIndexSPlugOperator

    LeftInFootIndexSx = DoubleField(default_value=1.0)

    LeftInFootIndexSy = DoubleField(default_value=1.0)

    LeftInFootIndexSz = DoubleField(default_value=1.0)


class LeftInFootMiddleTPlugOperator(
    CompoundPlugOperator["LeftInFootMiddleTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootMiddleTx", "LeftInFootMiddleTx"),
        ("LeftInFootMiddleTy", "LeftInFootMiddleTy"),
        ("LeftInFootMiddleTz", "LeftInFootMiddleTz"),
    )

    LeftInFootMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInFootMiddleTAttrOperator(
    CompoundAttrOperator[LeftInFootMiddleTPlugOperator]
):
    __slots__ = ()

    LeftInFootMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInFootMiddleTField(
    CompoundField[LeftInFootMiddleTAttrOperator, LeftInFootMiddleTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootMiddleTAttrOperator
    PLUG_CLS = LeftInFootMiddleTPlugOperator

    LeftInFootMiddleTx = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTy = DoubleLinearField(default_value=0.0)

    LeftInFootMiddleTz = DoubleLinearField(default_value=0.0)


class LeftInFootMiddleRPlugOperator(
    CompoundPlugOperator["LeftInFootMiddleRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootMiddleRx", "LeftInFootMiddleRx"),
        ("LeftInFootMiddleRy", "LeftInFootMiddleRy"),
        ("LeftInFootMiddleRz", "LeftInFootMiddleRz"),
    )

    LeftInFootMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInFootMiddleRAttrOperator(
    CompoundAttrOperator[LeftInFootMiddleRPlugOperator]
):
    __slots__ = ()

    LeftInFootMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInFootMiddleRField(
    CompoundField[LeftInFootMiddleRAttrOperator, LeftInFootMiddleRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootMiddleRAttrOperator
    PLUG_CLS = LeftInFootMiddleRPlugOperator

    LeftInFootMiddleRx = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRy = DoubleAngleField(default_value=0.0)

    LeftInFootMiddleRz = DoubleAngleField(default_value=0.0)


class LeftInFootMiddleSPlugOperator(
    CompoundPlugOperator["LeftInFootMiddleSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootMiddleSx", "LeftInFootMiddleSx"),
        ("LeftInFootMiddleSy", "LeftInFootMiddleSy"),
        ("LeftInFootMiddleSz", "LeftInFootMiddleSz"),
    )

    LeftInFootMiddleSx = DoubleField(default_value=1.0)

    LeftInFootMiddleSy = DoubleField(default_value=1.0)

    LeftInFootMiddleSz = DoubleField(default_value=1.0)


class LeftInFootMiddleSAttrOperator(
    CompoundAttrOperator[LeftInFootMiddleSPlugOperator]
):
    __slots__ = ()

    LeftInFootMiddleSx = DoubleField(default_value=1.0)

    LeftInFootMiddleSy = DoubleField(default_value=1.0)

    LeftInFootMiddleSz = DoubleField(default_value=1.0)


class LeftInFootMiddleSField(
    CompoundField[LeftInFootMiddleSAttrOperator, LeftInFootMiddleSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootMiddleSAttrOperator
    PLUG_CLS = LeftInFootMiddleSPlugOperator

    LeftInFootMiddleSx = DoubleField(default_value=1.0)

    LeftInFootMiddleSy = DoubleField(default_value=1.0)

    LeftInFootMiddleSz = DoubleField(default_value=1.0)


class LeftInFootRingTPlugOperator(
    CompoundPlugOperator["LeftInFootRingTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootRingTx", "LeftInFootRingTx"),
        ("LeftInFootRingTy", "LeftInFootRingTy"),
        ("LeftInFootRingTz", "LeftInFootRingTz"),
    )

    LeftInFootRingTx = DoubleLinearField(default_value=0.0)

    LeftInFootRingTy = DoubleLinearField(default_value=0.0)

    LeftInFootRingTz = DoubleLinearField(default_value=0.0)


class LeftInFootRingTAttrOperator(
    CompoundAttrOperator[LeftInFootRingTPlugOperator]
):
    __slots__ = ()

    LeftInFootRingTx = DoubleLinearField(default_value=0.0)

    LeftInFootRingTy = DoubleLinearField(default_value=0.0)

    LeftInFootRingTz = DoubleLinearField(default_value=0.0)


class LeftInFootRingTField(
    CompoundField[LeftInFootRingTAttrOperator, LeftInFootRingTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootRingTAttrOperator
    PLUG_CLS = LeftInFootRingTPlugOperator

    LeftInFootRingTx = DoubleLinearField(default_value=0.0)

    LeftInFootRingTy = DoubleLinearField(default_value=0.0)

    LeftInFootRingTz = DoubleLinearField(default_value=0.0)


class LeftInFootRingRPlugOperator(
    CompoundPlugOperator["LeftInFootRingRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootRingRx", "LeftInFootRingRx"),
        ("LeftInFootRingRy", "LeftInFootRingRy"),
        ("LeftInFootRingRz", "LeftInFootRingRz"),
    )

    LeftInFootRingRx = DoubleAngleField(default_value=0.0)

    LeftInFootRingRy = DoubleAngleField(default_value=0.0)

    LeftInFootRingRz = DoubleAngleField(default_value=0.0)


class LeftInFootRingRAttrOperator(
    CompoundAttrOperator[LeftInFootRingRPlugOperator]
):
    __slots__ = ()

    LeftInFootRingRx = DoubleAngleField(default_value=0.0)

    LeftInFootRingRy = DoubleAngleField(default_value=0.0)

    LeftInFootRingRz = DoubleAngleField(default_value=0.0)


class LeftInFootRingRField(
    CompoundField[LeftInFootRingRAttrOperator, LeftInFootRingRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootRingRAttrOperator
    PLUG_CLS = LeftInFootRingRPlugOperator

    LeftInFootRingRx = DoubleAngleField(default_value=0.0)

    LeftInFootRingRy = DoubleAngleField(default_value=0.0)

    LeftInFootRingRz = DoubleAngleField(default_value=0.0)


class LeftInFootRingSPlugOperator(
    CompoundPlugOperator["LeftInFootRingSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootRingSx", "LeftInFootRingSx"),
        ("LeftInFootRingSy", "LeftInFootRingSy"),
        ("LeftInFootRingSz", "LeftInFootRingSz"),
    )

    LeftInFootRingSx = DoubleField(default_value=1.0)

    LeftInFootRingSy = DoubleField(default_value=1.0)

    LeftInFootRingSz = DoubleField(default_value=1.0)


class LeftInFootRingSAttrOperator(
    CompoundAttrOperator[LeftInFootRingSPlugOperator]
):
    __slots__ = ()

    LeftInFootRingSx = DoubleField(default_value=1.0)

    LeftInFootRingSy = DoubleField(default_value=1.0)

    LeftInFootRingSz = DoubleField(default_value=1.0)


class LeftInFootRingSField(
    CompoundField[LeftInFootRingSAttrOperator, LeftInFootRingSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootRingSAttrOperator
    PLUG_CLS = LeftInFootRingSPlugOperator

    LeftInFootRingSx = DoubleField(default_value=1.0)

    LeftInFootRingSy = DoubleField(default_value=1.0)

    LeftInFootRingSz = DoubleField(default_value=1.0)


class LeftInFootPinkyTPlugOperator(
    CompoundPlugOperator["LeftInFootPinkyTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootPinkyTx", "LeftInFootPinkyTx"),
        ("LeftInFootPinkyTy", "LeftInFootPinkyTy"),
        ("LeftInFootPinkyTz", "LeftInFootPinkyTz"),
    )

    LeftInFootPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInFootPinkyTAttrOperator(
    CompoundAttrOperator[LeftInFootPinkyTPlugOperator]
):
    __slots__ = ()

    LeftInFootPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInFootPinkyTField(
    CompoundField[LeftInFootPinkyTAttrOperator, LeftInFootPinkyTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootPinkyTAttrOperator
    PLUG_CLS = LeftInFootPinkyTPlugOperator

    LeftInFootPinkyTx = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTy = DoubleLinearField(default_value=0.0)

    LeftInFootPinkyTz = DoubleLinearField(default_value=0.0)


class LeftInFootPinkyRPlugOperator(
    CompoundPlugOperator["LeftInFootPinkyRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootPinkyRx", "LeftInFootPinkyRx"),
        ("LeftInFootPinkyRy", "LeftInFootPinkyRy"),
        ("LeftInFootPinkyRz", "LeftInFootPinkyRz"),
    )

    LeftInFootPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInFootPinkyRAttrOperator(
    CompoundAttrOperator[LeftInFootPinkyRPlugOperator]
):
    __slots__ = ()

    LeftInFootPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInFootPinkyRField(
    CompoundField[LeftInFootPinkyRAttrOperator, LeftInFootPinkyRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootPinkyRAttrOperator
    PLUG_CLS = LeftInFootPinkyRPlugOperator

    LeftInFootPinkyRx = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRy = DoubleAngleField(default_value=0.0)

    LeftInFootPinkyRz = DoubleAngleField(default_value=0.0)


class LeftInFootPinkySPlugOperator(
    CompoundPlugOperator["LeftInFootPinkySAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootPinkySx", "LeftInFootPinkySx"),
        ("LeftInFootPinkySy", "LeftInFootPinkySy"),
        ("LeftInFootPinkySz", "LeftInFootPinkySz"),
    )

    LeftInFootPinkySx = DoubleField(default_value=1.0)

    LeftInFootPinkySy = DoubleField(default_value=1.0)

    LeftInFootPinkySz = DoubleField(default_value=1.0)


class LeftInFootPinkySAttrOperator(
    CompoundAttrOperator[LeftInFootPinkySPlugOperator]
):
    __slots__ = ()

    LeftInFootPinkySx = DoubleField(default_value=1.0)

    LeftInFootPinkySy = DoubleField(default_value=1.0)

    LeftInFootPinkySz = DoubleField(default_value=1.0)


class LeftInFootPinkySField(
    CompoundField[LeftInFootPinkySAttrOperator, LeftInFootPinkySPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootPinkySAttrOperator
    PLUG_CLS = LeftInFootPinkySPlugOperator

    LeftInFootPinkySx = DoubleField(default_value=1.0)

    LeftInFootPinkySy = DoubleField(default_value=1.0)

    LeftInFootPinkySz = DoubleField(default_value=1.0)


class LeftInFootExtraFingerTPlugOperator(
    CompoundPlugOperator["LeftInFootExtraFingerTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootExtraFingerTx", "LeftInFootExtraFingerTx"),
        ("LeftInFootExtraFingerTy", "LeftInFootExtraFingerTy"),
        ("LeftInFootExtraFingerTz", "LeftInFootExtraFingerTz"),
    )

    LeftInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInFootExtraFingerTAttrOperator(
    CompoundAttrOperator[LeftInFootExtraFingerTPlugOperator]
):
    __slots__ = ()

    LeftInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInFootExtraFingerTField(
    CompoundField[LeftInFootExtraFingerTAttrOperator, LeftInFootExtraFingerTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootExtraFingerTAttrOperator
    PLUG_CLS = LeftInFootExtraFingerTPlugOperator

    LeftInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    LeftInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class LeftInFootExtraFingerRPlugOperator(
    CompoundPlugOperator["LeftInFootExtraFingerRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootExtraFingerRx", "LeftInFootExtraFingerRx"),
        ("LeftInFootExtraFingerRy", "LeftInFootExtraFingerRy"),
        ("LeftInFootExtraFingerRz", "LeftInFootExtraFingerRz"),
    )

    LeftInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInFootExtraFingerRAttrOperator(
    CompoundAttrOperator[LeftInFootExtraFingerRPlugOperator]
):
    __slots__ = ()

    LeftInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInFootExtraFingerRField(
    CompoundField[LeftInFootExtraFingerRAttrOperator, LeftInFootExtraFingerRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootExtraFingerRAttrOperator
    PLUG_CLS = LeftInFootExtraFingerRPlugOperator

    LeftInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    LeftInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class LeftInFootExtraFingerSPlugOperator(
    CompoundPlugOperator["LeftInFootExtraFingerSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftInFootExtraFingerSx", "LeftInFootExtraFingerSx"),
        ("LeftInFootExtraFingerSy", "LeftInFootExtraFingerSy"),
        ("LeftInFootExtraFingerSz", "LeftInFootExtraFingerSz"),
    )

    LeftInFootExtraFingerSx = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSy = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSz = DoubleField(default_value=1.0)


class LeftInFootExtraFingerSAttrOperator(
    CompoundAttrOperator[LeftInFootExtraFingerSPlugOperator]
):
    __slots__ = ()

    LeftInFootExtraFingerSx = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSy = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSz = DoubleField(default_value=1.0)


class LeftInFootExtraFingerSField(
    CompoundField[LeftInFootExtraFingerSAttrOperator, LeftInFootExtraFingerSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftInFootExtraFingerSAttrOperator
    PLUG_CLS = LeftInFootExtraFingerSPlugOperator

    LeftInFootExtraFingerSx = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSy = DoubleField(default_value=1.0)

    LeftInFootExtraFingerSz = DoubleField(default_value=1.0)


class RightInFootThumbTPlugOperator(
    CompoundPlugOperator["RightInFootThumbTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootThumbTx", "RightInFootThumbTx"),
        ("RightInFootThumbTy", "RightInFootThumbTy"),
        ("RightInFootThumbTz", "RightInFootThumbTz"),
    )

    RightInFootThumbTx = DoubleLinearField(default_value=0.0)

    RightInFootThumbTy = DoubleLinearField(default_value=0.0)

    RightInFootThumbTz = DoubleLinearField(default_value=0.0)


class RightInFootThumbTAttrOperator(
    CompoundAttrOperator[RightInFootThumbTPlugOperator]
):
    __slots__ = ()

    RightInFootThumbTx = DoubleLinearField(default_value=0.0)

    RightInFootThumbTy = DoubleLinearField(default_value=0.0)

    RightInFootThumbTz = DoubleLinearField(default_value=0.0)


class RightInFootThumbTField(
    CompoundField[RightInFootThumbTAttrOperator, RightInFootThumbTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootThumbTAttrOperator
    PLUG_CLS = RightInFootThumbTPlugOperator

    RightInFootThumbTx = DoubleLinearField(default_value=0.0)

    RightInFootThumbTy = DoubleLinearField(default_value=0.0)

    RightInFootThumbTz = DoubleLinearField(default_value=0.0)


class RightInFootThumbRPlugOperator(
    CompoundPlugOperator["RightInFootThumbRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootThumbRx", "RightInFootThumbRx"),
        ("RightInFootThumbRy", "RightInFootThumbRy"),
        ("RightInFootThumbRz", "RightInFootThumbRz"),
    )

    RightInFootThumbRx = DoubleAngleField(default_value=0.0)

    RightInFootThumbRy = DoubleAngleField(default_value=0.0)

    RightInFootThumbRz = DoubleAngleField(default_value=0.0)


class RightInFootThumbRAttrOperator(
    CompoundAttrOperator[RightInFootThumbRPlugOperator]
):
    __slots__ = ()

    RightInFootThumbRx = DoubleAngleField(default_value=0.0)

    RightInFootThumbRy = DoubleAngleField(default_value=0.0)

    RightInFootThumbRz = DoubleAngleField(default_value=0.0)


class RightInFootThumbRField(
    CompoundField[RightInFootThumbRAttrOperator, RightInFootThumbRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootThumbRAttrOperator
    PLUG_CLS = RightInFootThumbRPlugOperator

    RightInFootThumbRx = DoubleAngleField(default_value=0.0)

    RightInFootThumbRy = DoubleAngleField(default_value=0.0)

    RightInFootThumbRz = DoubleAngleField(default_value=0.0)


class RightInFootThumbSPlugOperator(
    CompoundPlugOperator["RightInFootThumbSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootThumbSx", "RightInFootThumbSx"),
        ("RightInFootThumbSy", "RightInFootThumbSy"),
        ("RightInFootThumbSz", "RightInFootThumbSz"),
    )

    RightInFootThumbSx = DoubleField(default_value=1.0)

    RightInFootThumbSy = DoubleField(default_value=1.0)

    RightInFootThumbSz = DoubleField(default_value=1.0)


class RightInFootThumbSAttrOperator(
    CompoundAttrOperator[RightInFootThumbSPlugOperator]
):
    __slots__ = ()

    RightInFootThumbSx = DoubleField(default_value=1.0)

    RightInFootThumbSy = DoubleField(default_value=1.0)

    RightInFootThumbSz = DoubleField(default_value=1.0)


class RightInFootThumbSField(
    CompoundField[RightInFootThumbSAttrOperator, RightInFootThumbSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootThumbSAttrOperator
    PLUG_CLS = RightInFootThumbSPlugOperator

    RightInFootThumbSx = DoubleField(default_value=1.0)

    RightInFootThumbSy = DoubleField(default_value=1.0)

    RightInFootThumbSz = DoubleField(default_value=1.0)


class RightInFootIndexTPlugOperator(
    CompoundPlugOperator["RightInFootIndexTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootIndexTx", "RightInFootIndexTx"),
        ("RightInFootIndexTy", "RightInFootIndexTy"),
        ("RightInFootIndexTz", "RightInFootIndexTz"),
    )

    RightInFootIndexTx = DoubleLinearField(default_value=0.0)

    RightInFootIndexTy = DoubleLinearField(default_value=0.0)

    RightInFootIndexTz = DoubleLinearField(default_value=0.0)


class RightInFootIndexTAttrOperator(
    CompoundAttrOperator[RightInFootIndexTPlugOperator]
):
    __slots__ = ()

    RightInFootIndexTx = DoubleLinearField(default_value=0.0)

    RightInFootIndexTy = DoubleLinearField(default_value=0.0)

    RightInFootIndexTz = DoubleLinearField(default_value=0.0)


class RightInFootIndexTField(
    CompoundField[RightInFootIndexTAttrOperator, RightInFootIndexTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootIndexTAttrOperator
    PLUG_CLS = RightInFootIndexTPlugOperator

    RightInFootIndexTx = DoubleLinearField(default_value=0.0)

    RightInFootIndexTy = DoubleLinearField(default_value=0.0)

    RightInFootIndexTz = DoubleLinearField(default_value=0.0)


class RightInFootIndexRPlugOperator(
    CompoundPlugOperator["RightInFootIndexRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootIndexRx", "RightInFootIndexRx"),
        ("RightInFootIndexRy", "RightInFootIndexRy"),
        ("RightInFootIndexRz", "RightInFootIndexRz"),
    )

    RightInFootIndexRx = DoubleAngleField(default_value=0.0)

    RightInFootIndexRy = DoubleAngleField(default_value=0.0)

    RightInFootIndexRz = DoubleAngleField(default_value=0.0)


class RightInFootIndexRAttrOperator(
    CompoundAttrOperator[RightInFootIndexRPlugOperator]
):
    __slots__ = ()

    RightInFootIndexRx = DoubleAngleField(default_value=0.0)

    RightInFootIndexRy = DoubleAngleField(default_value=0.0)

    RightInFootIndexRz = DoubleAngleField(default_value=0.0)


class RightInFootIndexRField(
    CompoundField[RightInFootIndexRAttrOperator, RightInFootIndexRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootIndexRAttrOperator
    PLUG_CLS = RightInFootIndexRPlugOperator

    RightInFootIndexRx = DoubleAngleField(default_value=0.0)

    RightInFootIndexRy = DoubleAngleField(default_value=0.0)

    RightInFootIndexRz = DoubleAngleField(default_value=0.0)


class RightInFootIndexSPlugOperator(
    CompoundPlugOperator["RightInFootIndexSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootIndexSx", "RightInFootIndexSx"),
        ("RightInFootIndexSy", "RightInFootIndexSy"),
        ("RightInFootIndexSz", "RightInFootIndexSz"),
    )

    RightInFootIndexSx = DoubleField(default_value=1.0)

    RightInFootIndexSy = DoubleField(default_value=1.0)

    RightInFootIndexSz = DoubleField(default_value=1.0)


class RightInFootIndexSAttrOperator(
    CompoundAttrOperator[RightInFootIndexSPlugOperator]
):
    __slots__ = ()

    RightInFootIndexSx = DoubleField(default_value=1.0)

    RightInFootIndexSy = DoubleField(default_value=1.0)

    RightInFootIndexSz = DoubleField(default_value=1.0)


class RightInFootIndexSField(
    CompoundField[RightInFootIndexSAttrOperator, RightInFootIndexSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootIndexSAttrOperator
    PLUG_CLS = RightInFootIndexSPlugOperator

    RightInFootIndexSx = DoubleField(default_value=1.0)

    RightInFootIndexSy = DoubleField(default_value=1.0)

    RightInFootIndexSz = DoubleField(default_value=1.0)


class RightInFootMiddleTPlugOperator(
    CompoundPlugOperator["RightInFootMiddleTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootMiddleTx", "RightInFootMiddleTx"),
        ("RightInFootMiddleTy", "RightInFootMiddleTy"),
        ("RightInFootMiddleTz", "RightInFootMiddleTz"),
    )

    RightInFootMiddleTx = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTy = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTz = DoubleLinearField(default_value=0.0)


class RightInFootMiddleTAttrOperator(
    CompoundAttrOperator[RightInFootMiddleTPlugOperator]
):
    __slots__ = ()

    RightInFootMiddleTx = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTy = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTz = DoubleLinearField(default_value=0.0)


class RightInFootMiddleTField(
    CompoundField[RightInFootMiddleTAttrOperator, RightInFootMiddleTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootMiddleTAttrOperator
    PLUG_CLS = RightInFootMiddleTPlugOperator

    RightInFootMiddleTx = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTy = DoubleLinearField(default_value=0.0)

    RightInFootMiddleTz = DoubleLinearField(default_value=0.0)


class RightInFootMiddleRPlugOperator(
    CompoundPlugOperator["RightInFootMiddleRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootMiddleRx", "RightInFootMiddleRx"),
        ("RightInFootMiddleRy", "RightInFootMiddleRy"),
        ("RightInFootMiddleRz", "RightInFootMiddleRz"),
    )

    RightInFootMiddleRx = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRy = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRz = DoubleAngleField(default_value=0.0)


class RightInFootMiddleRAttrOperator(
    CompoundAttrOperator[RightInFootMiddleRPlugOperator]
):
    __slots__ = ()

    RightInFootMiddleRx = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRy = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRz = DoubleAngleField(default_value=0.0)


class RightInFootMiddleRField(
    CompoundField[RightInFootMiddleRAttrOperator, RightInFootMiddleRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootMiddleRAttrOperator
    PLUG_CLS = RightInFootMiddleRPlugOperator

    RightInFootMiddleRx = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRy = DoubleAngleField(default_value=0.0)

    RightInFootMiddleRz = DoubleAngleField(default_value=0.0)


class RightInFootMiddleSPlugOperator(
    CompoundPlugOperator["RightInFootMiddleSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootMiddleSx", "RightInFootMiddleSx"),
        ("RightInFootMiddleSy", "RightInFootMiddleSy"),
        ("RightInFootMiddleSz", "RightInFootMiddleSz"),
    )

    RightInFootMiddleSx = DoubleField(default_value=1.0)

    RightInFootMiddleSy = DoubleField(default_value=1.0)

    RightInFootMiddleSz = DoubleField(default_value=1.0)


class RightInFootMiddleSAttrOperator(
    CompoundAttrOperator[RightInFootMiddleSPlugOperator]
):
    __slots__ = ()

    RightInFootMiddleSx = DoubleField(default_value=1.0)

    RightInFootMiddleSy = DoubleField(default_value=1.0)

    RightInFootMiddleSz = DoubleField(default_value=1.0)


class RightInFootMiddleSField(
    CompoundField[RightInFootMiddleSAttrOperator, RightInFootMiddleSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootMiddleSAttrOperator
    PLUG_CLS = RightInFootMiddleSPlugOperator

    RightInFootMiddleSx = DoubleField(default_value=1.0)

    RightInFootMiddleSy = DoubleField(default_value=1.0)

    RightInFootMiddleSz = DoubleField(default_value=1.0)


class RightInFootRingTPlugOperator(
    CompoundPlugOperator["RightInFootRingTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootRingTx", "RightInFootRingTx"),
        ("RightInFootRingTy", "RightInFootRingTy"),
        ("RightInFootRingTz", "RightInFootRingTz"),
    )

    RightInFootRingTx = DoubleLinearField(default_value=0.0)

    RightInFootRingTy = DoubleLinearField(default_value=0.0)

    RightInFootRingTz = DoubleLinearField(default_value=0.0)


class RightInFootRingTAttrOperator(
    CompoundAttrOperator[RightInFootRingTPlugOperator]
):
    __slots__ = ()

    RightInFootRingTx = DoubleLinearField(default_value=0.0)

    RightInFootRingTy = DoubleLinearField(default_value=0.0)

    RightInFootRingTz = DoubleLinearField(default_value=0.0)


class RightInFootRingTField(
    CompoundField[RightInFootRingTAttrOperator, RightInFootRingTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootRingTAttrOperator
    PLUG_CLS = RightInFootRingTPlugOperator

    RightInFootRingTx = DoubleLinearField(default_value=0.0)

    RightInFootRingTy = DoubleLinearField(default_value=0.0)

    RightInFootRingTz = DoubleLinearField(default_value=0.0)


class RightInFootRingRPlugOperator(
    CompoundPlugOperator["RightInFootRingRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootRingRx", "RightInFootRingRx"),
        ("RightInFootRingRy", "RightInFootRingRy"),
        ("RightInFootRingRz", "RightInFootRingRz"),
    )

    RightInFootRingRx = DoubleAngleField(default_value=0.0)

    RightInFootRingRy = DoubleAngleField(default_value=0.0)

    RightInFootRingRz = DoubleAngleField(default_value=0.0)


class RightInFootRingRAttrOperator(
    CompoundAttrOperator[RightInFootRingRPlugOperator]
):
    __slots__ = ()

    RightInFootRingRx = DoubleAngleField(default_value=0.0)

    RightInFootRingRy = DoubleAngleField(default_value=0.0)

    RightInFootRingRz = DoubleAngleField(default_value=0.0)


class RightInFootRingRField(
    CompoundField[RightInFootRingRAttrOperator, RightInFootRingRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootRingRAttrOperator
    PLUG_CLS = RightInFootRingRPlugOperator

    RightInFootRingRx = DoubleAngleField(default_value=0.0)

    RightInFootRingRy = DoubleAngleField(default_value=0.0)

    RightInFootRingRz = DoubleAngleField(default_value=0.0)


class RightInFootRingSPlugOperator(
    CompoundPlugOperator["RightInFootRingSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootRingSx", "RightInFootRingSx"),
        ("RightInFootRingSy", "RightInFootRingSy"),
        ("RightInFootRingSz", "RightInFootRingSz"),
    )

    RightInFootRingSx = DoubleField(default_value=1.0)

    RightInFootRingSy = DoubleField(default_value=1.0)

    RightInFootRingSz = DoubleField(default_value=1.0)


class RightInFootRingSAttrOperator(
    CompoundAttrOperator[RightInFootRingSPlugOperator]
):
    __slots__ = ()

    RightInFootRingSx = DoubleField(default_value=1.0)

    RightInFootRingSy = DoubleField(default_value=1.0)

    RightInFootRingSz = DoubleField(default_value=1.0)


class RightInFootRingSField(
    CompoundField[RightInFootRingSAttrOperator, RightInFootRingSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootRingSAttrOperator
    PLUG_CLS = RightInFootRingSPlugOperator

    RightInFootRingSx = DoubleField(default_value=1.0)

    RightInFootRingSy = DoubleField(default_value=1.0)

    RightInFootRingSz = DoubleField(default_value=1.0)


class RightInFootPinkyTPlugOperator(
    CompoundPlugOperator["RightInFootPinkyTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootPinkyTx", "RightInFootPinkyTx"),
        ("RightInFootPinkyTy", "RightInFootPinkyTy"),
        ("RightInFootPinkyTz", "RightInFootPinkyTz"),
    )

    RightInFootPinkyTx = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTy = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTz = DoubleLinearField(default_value=0.0)


class RightInFootPinkyTAttrOperator(
    CompoundAttrOperator[RightInFootPinkyTPlugOperator]
):
    __slots__ = ()

    RightInFootPinkyTx = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTy = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTz = DoubleLinearField(default_value=0.0)


class RightInFootPinkyTField(
    CompoundField[RightInFootPinkyTAttrOperator, RightInFootPinkyTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootPinkyTAttrOperator
    PLUG_CLS = RightInFootPinkyTPlugOperator

    RightInFootPinkyTx = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTy = DoubleLinearField(default_value=0.0)

    RightInFootPinkyTz = DoubleLinearField(default_value=0.0)


class RightInFootPinkyRPlugOperator(
    CompoundPlugOperator["RightInFootPinkyRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootPinkyRx", "RightInFootPinkyRx"),
        ("RightInFootPinkyRy", "RightInFootPinkyRy"),
        ("RightInFootPinkyRz", "RightInFootPinkyRz"),
    )

    RightInFootPinkyRx = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRy = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRz = DoubleAngleField(default_value=0.0)


class RightInFootPinkyRAttrOperator(
    CompoundAttrOperator[RightInFootPinkyRPlugOperator]
):
    __slots__ = ()

    RightInFootPinkyRx = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRy = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRz = DoubleAngleField(default_value=0.0)


class RightInFootPinkyRField(
    CompoundField[RightInFootPinkyRAttrOperator, RightInFootPinkyRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootPinkyRAttrOperator
    PLUG_CLS = RightInFootPinkyRPlugOperator

    RightInFootPinkyRx = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRy = DoubleAngleField(default_value=0.0)

    RightInFootPinkyRz = DoubleAngleField(default_value=0.0)


class RightInFootPinkySPlugOperator(
    CompoundPlugOperator["RightInFootPinkySAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootPinkySx", "RightInFootPinkySx"),
        ("RightInFootPinkySy", "RightInFootPinkySy"),
        ("RightInFootPinkySz", "RightInFootPinkySz"),
    )

    RightInFootPinkySx = DoubleField(default_value=1.0)

    RightInFootPinkySy = DoubleField(default_value=1.0)

    RightInFootPinkySz = DoubleField(default_value=1.0)


class RightInFootPinkySAttrOperator(
    CompoundAttrOperator[RightInFootPinkySPlugOperator]
):
    __slots__ = ()

    RightInFootPinkySx = DoubleField(default_value=1.0)

    RightInFootPinkySy = DoubleField(default_value=1.0)

    RightInFootPinkySz = DoubleField(default_value=1.0)


class RightInFootPinkySField(
    CompoundField[RightInFootPinkySAttrOperator, RightInFootPinkySPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootPinkySAttrOperator
    PLUG_CLS = RightInFootPinkySPlugOperator

    RightInFootPinkySx = DoubleField(default_value=1.0)

    RightInFootPinkySy = DoubleField(default_value=1.0)

    RightInFootPinkySz = DoubleField(default_value=1.0)


class RightInFootExtraFingerTPlugOperator(
    CompoundPlugOperator["RightInFootExtraFingerTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootExtraFingerTx", "RightInFootExtraFingerTx"),
        ("RightInFootExtraFingerTy", "RightInFootExtraFingerTy"),
        ("RightInFootExtraFingerTz", "RightInFootExtraFingerTz"),
    )

    RightInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInFootExtraFingerTAttrOperator(
    CompoundAttrOperator[RightInFootExtraFingerTPlugOperator]
):
    __slots__ = ()

    RightInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInFootExtraFingerTField(
    CompoundField[RightInFootExtraFingerTAttrOperator, RightInFootExtraFingerTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootExtraFingerTAttrOperator
    PLUG_CLS = RightInFootExtraFingerTPlugOperator

    RightInFootExtraFingerTx = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTy = DoubleLinearField(default_value=0.0)

    RightInFootExtraFingerTz = DoubleLinearField(default_value=0.0)


class RightInFootExtraFingerRPlugOperator(
    CompoundPlugOperator["RightInFootExtraFingerRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootExtraFingerRx", "RightInFootExtraFingerRx"),
        ("RightInFootExtraFingerRy", "RightInFootExtraFingerRy"),
        ("RightInFootExtraFingerRz", "RightInFootExtraFingerRz"),
    )

    RightInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInFootExtraFingerRAttrOperator(
    CompoundAttrOperator[RightInFootExtraFingerRPlugOperator]
):
    __slots__ = ()

    RightInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInFootExtraFingerRField(
    CompoundField[RightInFootExtraFingerRAttrOperator, RightInFootExtraFingerRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootExtraFingerRAttrOperator
    PLUG_CLS = RightInFootExtraFingerRPlugOperator

    RightInFootExtraFingerRx = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRy = DoubleAngleField(default_value=0.0)

    RightInFootExtraFingerRz = DoubleAngleField(default_value=0.0)


class RightInFootExtraFingerSPlugOperator(
    CompoundPlugOperator["RightInFootExtraFingerSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightInFootExtraFingerSx", "RightInFootExtraFingerSx"),
        ("RightInFootExtraFingerSy", "RightInFootExtraFingerSy"),
        ("RightInFootExtraFingerSz", "RightInFootExtraFingerSz"),
    )

    RightInFootExtraFingerSx = DoubleField(default_value=1.0)

    RightInFootExtraFingerSy = DoubleField(default_value=1.0)

    RightInFootExtraFingerSz = DoubleField(default_value=1.0)


class RightInFootExtraFingerSAttrOperator(
    CompoundAttrOperator[RightInFootExtraFingerSPlugOperator]
):
    __slots__ = ()

    RightInFootExtraFingerSx = DoubleField(default_value=1.0)

    RightInFootExtraFingerSy = DoubleField(default_value=1.0)

    RightInFootExtraFingerSz = DoubleField(default_value=1.0)


class RightInFootExtraFingerSField(
    CompoundField[RightInFootExtraFingerSAttrOperator, RightInFootExtraFingerSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightInFootExtraFingerSAttrOperator
    PLUG_CLS = RightInFootExtraFingerSPlugOperator

    RightInFootExtraFingerSx = DoubleField(default_value=1.0)

    RightInFootExtraFingerSy = DoubleField(default_value=1.0)

    RightInFootExtraFingerSz = DoubleField(default_value=1.0)


class LeftShoulderExtraTPlugOperator(
    CompoundPlugOperator["LeftShoulderExtraTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderExtraTx", "LeftShoulderExtraTx"),
        ("LeftShoulderExtraTy", "LeftShoulderExtraTy"),
        ("LeftShoulderExtraTz", "LeftShoulderExtraTz"),
    )

    LeftShoulderExtraTx = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTy = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTz = DoubleLinearField(default_value=0.0)


class LeftShoulderExtraTAttrOperator(
    CompoundAttrOperator[LeftShoulderExtraTPlugOperator]
):
    __slots__ = ()

    LeftShoulderExtraTx = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTy = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTz = DoubleLinearField(default_value=0.0)


class LeftShoulderExtraTField(
    CompoundField[LeftShoulderExtraTAttrOperator, LeftShoulderExtraTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderExtraTAttrOperator
    PLUG_CLS = LeftShoulderExtraTPlugOperator

    LeftShoulderExtraTx = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTy = DoubleLinearField(default_value=0.0)

    LeftShoulderExtraTz = DoubleLinearField(default_value=0.0)


class LeftShoulderExtraRPlugOperator(
    CompoundPlugOperator["LeftShoulderExtraRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderExtraRx", "LeftShoulderExtraRx"),
        ("LeftShoulderExtraRy", "LeftShoulderExtraRy"),
        ("LeftShoulderExtraRz", "LeftShoulderExtraRz"),
    )

    LeftShoulderExtraRx = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRy = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRz = DoubleAngleField(default_value=0.0)


class LeftShoulderExtraRAttrOperator(
    CompoundAttrOperator[LeftShoulderExtraRPlugOperator]
):
    __slots__ = ()

    LeftShoulderExtraRx = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRy = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRz = DoubleAngleField(default_value=0.0)


class LeftShoulderExtraRField(
    CompoundField[LeftShoulderExtraRAttrOperator, LeftShoulderExtraRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderExtraRAttrOperator
    PLUG_CLS = LeftShoulderExtraRPlugOperator

    LeftShoulderExtraRx = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRy = DoubleAngleField(default_value=0.0)

    LeftShoulderExtraRz = DoubleAngleField(default_value=0.0)


class LeftShoulderExtraSPlugOperator(
    CompoundPlugOperator["LeftShoulderExtraSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeftShoulderExtraSx", "LeftShoulderExtraSx"),
        ("LeftShoulderExtraSy", "LeftShoulderExtraSy"),
        ("LeftShoulderExtraSz", "LeftShoulderExtraSz"),
    )

    LeftShoulderExtraSx = DoubleField(default_value=1.0)

    LeftShoulderExtraSy = DoubleField(default_value=1.0)

    LeftShoulderExtraSz = DoubleField(default_value=1.0)


class LeftShoulderExtraSAttrOperator(
    CompoundAttrOperator[LeftShoulderExtraSPlugOperator]
):
    __slots__ = ()

    LeftShoulderExtraSx = DoubleField(default_value=1.0)

    LeftShoulderExtraSy = DoubleField(default_value=1.0)

    LeftShoulderExtraSz = DoubleField(default_value=1.0)


class LeftShoulderExtraSField(
    CompoundField[LeftShoulderExtraSAttrOperator, LeftShoulderExtraSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftShoulderExtraSAttrOperator
    PLUG_CLS = LeftShoulderExtraSPlugOperator

    LeftShoulderExtraSx = DoubleField(default_value=1.0)

    LeftShoulderExtraSy = DoubleField(default_value=1.0)

    LeftShoulderExtraSz = DoubleField(default_value=1.0)


class RightShoulderExtraTPlugOperator(
    CompoundPlugOperator["RightShoulderExtraTAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderExtraTx", "RightShoulderExtraTx"),
        ("RightShoulderExtraTy", "RightShoulderExtraTy"),
        ("RightShoulderExtraTz", "RightShoulderExtraTz"),
    )

    RightShoulderExtraTx = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTy = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTz = DoubleLinearField(default_value=0.0)


class RightShoulderExtraTAttrOperator(
    CompoundAttrOperator[RightShoulderExtraTPlugOperator]
):
    __slots__ = ()

    RightShoulderExtraTx = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTy = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTz = DoubleLinearField(default_value=0.0)


class RightShoulderExtraTField(
    CompoundField[RightShoulderExtraTAttrOperator, RightShoulderExtraTPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderExtraTAttrOperator
    PLUG_CLS = RightShoulderExtraTPlugOperator

    RightShoulderExtraTx = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTy = DoubleLinearField(default_value=0.0)

    RightShoulderExtraTz = DoubleLinearField(default_value=0.0)


class RightShoulderExtraRPlugOperator(
    CompoundPlugOperator["RightShoulderExtraRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderExtraRx", "RightShoulderExtraRx"),
        ("RightShoulderExtraRy", "RightShoulderExtraRy"),
        ("RightShoulderExtraRz", "RightShoulderExtraRz"),
    )

    RightShoulderExtraRx = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRy = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRz = DoubleAngleField(default_value=0.0)


class RightShoulderExtraRAttrOperator(
    CompoundAttrOperator[RightShoulderExtraRPlugOperator]
):
    __slots__ = ()

    RightShoulderExtraRx = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRy = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRz = DoubleAngleField(default_value=0.0)


class RightShoulderExtraRField(
    CompoundField[RightShoulderExtraRAttrOperator, RightShoulderExtraRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderExtraRAttrOperator
    PLUG_CLS = RightShoulderExtraRPlugOperator

    RightShoulderExtraRx = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRy = DoubleAngleField(default_value=0.0)

    RightShoulderExtraRz = DoubleAngleField(default_value=0.0)


class RightShoulderExtraSPlugOperator(
    CompoundPlugOperator["RightShoulderExtraSAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RightShoulderExtraSx", "RightShoulderExtraSx"),
        ("RightShoulderExtraSy", "RightShoulderExtraSy"),
        ("RightShoulderExtraSz", "RightShoulderExtraSz"),
    )

    RightShoulderExtraSx = DoubleField(default_value=1.0)

    RightShoulderExtraSy = DoubleField(default_value=1.0)

    RightShoulderExtraSz = DoubleField(default_value=1.0)


class RightShoulderExtraSAttrOperator(
    CompoundAttrOperator[RightShoulderExtraSPlugOperator]
):
    __slots__ = ()

    RightShoulderExtraSx = DoubleField(default_value=1.0)

    RightShoulderExtraSy = DoubleField(default_value=1.0)

    RightShoulderExtraSz = DoubleField(default_value=1.0)


class RightShoulderExtraSField(
    CompoundField[RightShoulderExtraSAttrOperator, RightShoulderExtraSPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightShoulderExtraSAttrOperator
    PLUG_CLS = RightShoulderExtraSPlugOperator

    RightShoulderExtraSx = DoubleField(default_value=1.0)

    RightShoulderExtraSy = DoubleField(default_value=1.0)

    RightShoulderExtraSz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll1TPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll1Tx", "LeafLeftUpLegRoll1Tx"),
        ("LeafLeftUpLegRoll1Ty", "LeafLeftUpLegRoll1Ty"),
        ("LeafLeftUpLegRoll1Tz", "LeafLeftUpLegRoll1Tz"),
    )

    LeafLeftUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll1TAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll1TPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll1TField(
    CompoundField[LeafLeftUpLegRoll1TAttrOperator, LeafLeftUpLegRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll1TAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll1TPlugOperator

    LeafLeftUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll1RPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll1Rx", "LeafLeftUpLegRoll1Rx"),
        ("LeafLeftUpLegRoll1Ry", "LeafLeftUpLegRoll1Ry"),
        ("LeafLeftUpLegRoll1Rz", "LeafLeftUpLegRoll1Rz"),
    )

    LeafLeftUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll1RAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll1RPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll1RField(
    CompoundField[LeafLeftUpLegRoll1RAttrOperator, LeafLeftUpLegRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll1RAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll1RPlugOperator

    LeafLeftUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll1SPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll1Sx", "LeafLeftUpLegRoll1Sx"),
        ("LeafLeftUpLegRoll1Sy", "LeafLeftUpLegRoll1Sy"),
        ("LeafLeftUpLegRoll1Sz", "LeafLeftUpLegRoll1Sz"),
    )

    LeafLeftUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll1SAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll1SPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll1SField(
    CompoundField[LeafLeftUpLegRoll1SAttrOperator, LeafLeftUpLegRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll1SAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll1SPlugOperator

    LeafLeftUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll1TPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll1Tx", "LeafLeftLegRoll1Tx"),
        ("LeafLeftLegRoll1Ty", "LeafLeftLegRoll1Ty"),
        ("LeafLeftLegRoll1Tz", "LeafLeftLegRoll1Tz"),
    )

    LeafLeftLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll1TAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll1TPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll1TField(
    CompoundField[LeafLeftLegRoll1TAttrOperator, LeafLeftLegRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll1TAttrOperator
    PLUG_CLS = LeafLeftLegRoll1TPlugOperator

    LeafLeftLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll1RPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll1Rx", "LeafLeftLegRoll1Rx"),
        ("LeafLeftLegRoll1Ry", "LeafLeftLegRoll1Ry"),
        ("LeafLeftLegRoll1Rz", "LeafLeftLegRoll1Rz"),
    )

    LeafLeftLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll1RAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll1RPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll1RField(
    CompoundField[LeafLeftLegRoll1RAttrOperator, LeafLeftLegRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll1RAttrOperator
    PLUG_CLS = LeafLeftLegRoll1RPlugOperator

    LeafLeftLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll1SPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll1Sx", "LeafLeftLegRoll1Sx"),
        ("LeafLeftLegRoll1Sy", "LeafLeftLegRoll1Sy"),
        ("LeafLeftLegRoll1Sz", "LeafLeftLegRoll1Sz"),
    )

    LeafLeftLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll1SAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll1SPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll1SField(
    CompoundField[LeafLeftLegRoll1SAttrOperator, LeafLeftLegRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll1SAttrOperator
    PLUG_CLS = LeafLeftLegRoll1SPlugOperator

    LeafLeftLegRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll1TPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll1Tx", "LeafRightUpLegRoll1Tx"),
        ("LeafRightUpLegRoll1Ty", "LeafRightUpLegRoll1Ty"),
        ("LeafRightUpLegRoll1Tz", "LeafRightUpLegRoll1Tz"),
    )

    LeafRightUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll1TAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll1TPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll1TField(
    CompoundField[LeafRightUpLegRoll1TAttrOperator, LeafRightUpLegRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll1TAttrOperator
    PLUG_CLS = LeafRightUpLegRoll1TPlugOperator

    LeafRightUpLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll1RPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll1Rx", "LeafRightUpLegRoll1Rx"),
        ("LeafRightUpLegRoll1Ry", "LeafRightUpLegRoll1Ry"),
        ("LeafRightUpLegRoll1Rz", "LeafRightUpLegRoll1Rz"),
    )

    LeafRightUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll1RAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll1RPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll1RField(
    CompoundField[LeafRightUpLegRoll1RAttrOperator, LeafRightUpLegRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll1RAttrOperator
    PLUG_CLS = LeafRightUpLegRoll1RPlugOperator

    LeafRightUpLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll1SPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll1Sx", "LeafRightUpLegRoll1Sx"),
        ("LeafRightUpLegRoll1Sy", "LeafRightUpLegRoll1Sy"),
        ("LeafRightUpLegRoll1Sz", "LeafRightUpLegRoll1Sz"),
    )

    LeafRightUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll1SAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll1SPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll1SField(
    CompoundField[LeafRightUpLegRoll1SAttrOperator, LeafRightUpLegRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll1SAttrOperator
    PLUG_CLS = LeafRightUpLegRoll1SPlugOperator

    LeafRightUpLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll1TPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll1Tx", "LeafRightLegRoll1Tx"),
        ("LeafRightLegRoll1Ty", "LeafRightLegRoll1Ty"),
        ("LeafRightLegRoll1Tz", "LeafRightLegRoll1Tz"),
    )

    LeafRightLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll1TAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll1TPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll1TField(
    CompoundField[LeafRightLegRoll1TAttrOperator, LeafRightLegRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll1TAttrOperator
    PLUG_CLS = LeafRightLegRoll1TPlugOperator

    LeafRightLegRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll1RPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll1Rx", "LeafRightLegRoll1Rx"),
        ("LeafRightLegRoll1Ry", "LeafRightLegRoll1Ry"),
        ("LeafRightLegRoll1Rz", "LeafRightLegRoll1Rz"),
    )

    LeafRightLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll1RAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll1RPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll1RField(
    CompoundField[LeafRightLegRoll1RAttrOperator, LeafRightLegRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll1RAttrOperator
    PLUG_CLS = LeafRightLegRoll1RPlugOperator

    LeafRightLegRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll1SPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll1Sx", "LeafRightLegRoll1Sx"),
        ("LeafRightLegRoll1Sy", "LeafRightLegRoll1Sy"),
        ("LeafRightLegRoll1Sz", "LeafRightLegRoll1Sz"),
    )

    LeafRightLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll1SAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll1SPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll1SField(
    CompoundField[LeafRightLegRoll1SAttrOperator, LeafRightLegRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll1SAttrOperator
    PLUG_CLS = LeafRightLegRoll1SPlugOperator

    LeafRightLegRoll1Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll1TPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll1Tx", "LeafLeftArmRoll1Tx"),
        ("LeafLeftArmRoll1Ty", "LeafLeftArmRoll1Ty"),
        ("LeafLeftArmRoll1Tz", "LeafLeftArmRoll1Tz"),
    )

    LeafLeftArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll1TAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll1TPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll1TField(
    CompoundField[LeafLeftArmRoll1TAttrOperator, LeafLeftArmRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll1TAttrOperator
    PLUG_CLS = LeafLeftArmRoll1TPlugOperator

    LeafLeftArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll1RPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll1Rx", "LeafLeftArmRoll1Rx"),
        ("LeafLeftArmRoll1Ry", "LeafLeftArmRoll1Ry"),
        ("LeafLeftArmRoll1Rz", "LeafLeftArmRoll1Rz"),
    )

    LeafLeftArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll1RAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll1RPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll1RField(
    CompoundField[LeafLeftArmRoll1RAttrOperator, LeafLeftArmRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll1RAttrOperator
    PLUG_CLS = LeafLeftArmRoll1RPlugOperator

    LeafLeftArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll1SPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll1Sx", "LeafLeftArmRoll1Sx"),
        ("LeafLeftArmRoll1Sy", "LeafLeftArmRoll1Sy"),
        ("LeafLeftArmRoll1Sz", "LeafLeftArmRoll1Sz"),
    )

    LeafLeftArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll1SAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll1SPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll1SField(
    CompoundField[LeafLeftArmRoll1SAttrOperator, LeafLeftArmRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll1SAttrOperator
    PLUG_CLS = LeafLeftArmRoll1SPlugOperator

    LeafLeftArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll1TPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll1Tx", "LeafLeftForeArmRoll1Tx"),
        ("LeafLeftForeArmRoll1Ty", "LeafLeftForeArmRoll1Ty"),
        ("LeafLeftForeArmRoll1Tz", "LeafLeftForeArmRoll1Tz"),
    )

    LeafLeftForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll1TAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll1TPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll1TField(
    CompoundField[LeafLeftForeArmRoll1TAttrOperator, LeafLeftForeArmRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll1TAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll1TPlugOperator

    LeafLeftForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll1RPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll1Rx", "LeafLeftForeArmRoll1Rx"),
        ("LeafLeftForeArmRoll1Ry", "LeafLeftForeArmRoll1Ry"),
        ("LeafLeftForeArmRoll1Rz", "LeafLeftForeArmRoll1Rz"),
    )

    LeafLeftForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll1RAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll1RPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll1RField(
    CompoundField[LeafLeftForeArmRoll1RAttrOperator, LeafLeftForeArmRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll1RAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll1RPlugOperator

    LeafLeftForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll1SPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll1Sx", "LeafLeftForeArmRoll1Sx"),
        ("LeafLeftForeArmRoll1Sy", "LeafLeftForeArmRoll1Sy"),
        ("LeafLeftForeArmRoll1Sz", "LeafLeftForeArmRoll1Sz"),
    )

    LeafLeftForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll1SAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll1SPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll1SField(
    CompoundField[LeafLeftForeArmRoll1SAttrOperator, LeafLeftForeArmRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll1SAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll1SPlugOperator

    LeafLeftForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll1TPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll1Tx", "LeafRightArmRoll1Tx"),
        ("LeafRightArmRoll1Ty", "LeafRightArmRoll1Ty"),
        ("LeafRightArmRoll1Tz", "LeafRightArmRoll1Tz"),
    )

    LeafRightArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll1TAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll1TPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll1TField(
    CompoundField[LeafRightArmRoll1TAttrOperator, LeafRightArmRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll1TAttrOperator
    PLUG_CLS = LeafRightArmRoll1TPlugOperator

    LeafRightArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll1RPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll1Rx", "LeafRightArmRoll1Rx"),
        ("LeafRightArmRoll1Ry", "LeafRightArmRoll1Ry"),
        ("LeafRightArmRoll1Rz", "LeafRightArmRoll1Rz"),
    )

    LeafRightArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll1RAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll1RPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll1RField(
    CompoundField[LeafRightArmRoll1RAttrOperator, LeafRightArmRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll1RAttrOperator
    PLUG_CLS = LeafRightArmRoll1RPlugOperator

    LeafRightArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll1SPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll1Sx", "LeafRightArmRoll1Sx"),
        ("LeafRightArmRoll1Sy", "LeafRightArmRoll1Sy"),
        ("LeafRightArmRoll1Sz", "LeafRightArmRoll1Sz"),
    )

    LeafRightArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll1SAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll1SPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll1SField(
    CompoundField[LeafRightArmRoll1SAttrOperator, LeafRightArmRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll1SAttrOperator
    PLUG_CLS = LeafRightArmRoll1SPlugOperator

    LeafRightArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll1TPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll1TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll1Tx", "LeafRightForeArmRoll1Tx"),
        ("LeafRightForeArmRoll1Ty", "LeafRightForeArmRoll1Ty"),
        ("LeafRightForeArmRoll1Tz", "LeafRightForeArmRoll1Tz"),
    )

    LeafRightForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll1TAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll1TPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll1TField(
    CompoundField[LeafRightForeArmRoll1TAttrOperator, LeafRightForeArmRoll1TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll1TAttrOperator
    PLUG_CLS = LeafRightForeArmRoll1TPlugOperator

    LeafRightForeArmRoll1Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll1Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll1RPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll1RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll1Rx", "LeafRightForeArmRoll1Rx"),
        ("LeafRightForeArmRoll1Ry", "LeafRightForeArmRoll1Ry"),
        ("LeafRightForeArmRoll1Rz", "LeafRightForeArmRoll1Rz"),
    )

    LeafRightForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll1RAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll1RPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll1RField(
    CompoundField[LeafRightForeArmRoll1RAttrOperator, LeafRightForeArmRoll1RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll1RAttrOperator
    PLUG_CLS = LeafRightForeArmRoll1RPlugOperator

    LeafRightForeArmRoll1Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll1Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll1SPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll1SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll1Sx", "LeafRightForeArmRoll1Sx"),
        ("LeafRightForeArmRoll1Sy", "LeafRightForeArmRoll1Sy"),
        ("LeafRightForeArmRoll1Sz", "LeafRightForeArmRoll1Sz"),
    )

    LeafRightForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll1SAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll1SPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll1SField(
    CompoundField[LeafRightForeArmRoll1SAttrOperator, LeafRightForeArmRoll1SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll1SAttrOperator
    PLUG_CLS = LeafRightForeArmRoll1SPlugOperator

    LeafRightForeArmRoll1Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll1Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll2TPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll2Tx", "LeafLeftUpLegRoll2Tx"),
        ("LeafLeftUpLegRoll2Ty", "LeafLeftUpLegRoll2Ty"),
        ("LeafLeftUpLegRoll2Tz", "LeafLeftUpLegRoll2Tz"),
    )

    LeafLeftUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll2TAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll2TPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll2TField(
    CompoundField[LeafLeftUpLegRoll2TAttrOperator, LeafLeftUpLegRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll2TAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll2TPlugOperator

    LeafLeftUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll2RPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll2Rx", "LeafLeftUpLegRoll2Rx"),
        ("LeafLeftUpLegRoll2Ry", "LeafLeftUpLegRoll2Ry"),
        ("LeafLeftUpLegRoll2Rz", "LeafLeftUpLegRoll2Rz"),
    )

    LeafLeftUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll2RAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll2RPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll2RField(
    CompoundField[LeafLeftUpLegRoll2RAttrOperator, LeafLeftUpLegRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll2RAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll2RPlugOperator

    LeafLeftUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll2SPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll2Sx", "LeafLeftUpLegRoll2Sx"),
        ("LeafLeftUpLegRoll2Sy", "LeafLeftUpLegRoll2Sy"),
        ("LeafLeftUpLegRoll2Sz", "LeafLeftUpLegRoll2Sz"),
    )

    LeafLeftUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll2SAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll2SPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll2SField(
    CompoundField[LeafLeftUpLegRoll2SAttrOperator, LeafLeftUpLegRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll2SAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll2SPlugOperator

    LeafLeftUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll2TPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll2Tx", "LeafLeftLegRoll2Tx"),
        ("LeafLeftLegRoll2Ty", "LeafLeftLegRoll2Ty"),
        ("LeafLeftLegRoll2Tz", "LeafLeftLegRoll2Tz"),
    )

    LeafLeftLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll2TAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll2TPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll2TField(
    CompoundField[LeafLeftLegRoll2TAttrOperator, LeafLeftLegRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll2TAttrOperator
    PLUG_CLS = LeafLeftLegRoll2TPlugOperator

    LeafLeftLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll2RPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll2Rx", "LeafLeftLegRoll2Rx"),
        ("LeafLeftLegRoll2Ry", "LeafLeftLegRoll2Ry"),
        ("LeafLeftLegRoll2Rz", "LeafLeftLegRoll2Rz"),
    )

    LeafLeftLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll2RAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll2RPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll2RField(
    CompoundField[LeafLeftLegRoll2RAttrOperator, LeafLeftLegRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll2RAttrOperator
    PLUG_CLS = LeafLeftLegRoll2RPlugOperator

    LeafLeftLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll2SPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll2Sx", "LeafLeftLegRoll2Sx"),
        ("LeafLeftLegRoll2Sy", "LeafLeftLegRoll2Sy"),
        ("LeafLeftLegRoll2Sz", "LeafLeftLegRoll2Sz"),
    )

    LeafLeftLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll2SAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll2SPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll2SField(
    CompoundField[LeafLeftLegRoll2SAttrOperator, LeafLeftLegRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll2SAttrOperator
    PLUG_CLS = LeafLeftLegRoll2SPlugOperator

    LeafLeftLegRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll2TPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll2Tx", "LeafRightUpLegRoll2Tx"),
        ("LeafRightUpLegRoll2Ty", "LeafRightUpLegRoll2Ty"),
        ("LeafRightUpLegRoll2Tz", "LeafRightUpLegRoll2Tz"),
    )

    LeafRightUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll2TAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll2TPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll2TField(
    CompoundField[LeafRightUpLegRoll2TAttrOperator, LeafRightUpLegRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll2TAttrOperator
    PLUG_CLS = LeafRightUpLegRoll2TPlugOperator

    LeafRightUpLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll2RPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll2Rx", "LeafRightUpLegRoll2Rx"),
        ("LeafRightUpLegRoll2Ry", "LeafRightUpLegRoll2Ry"),
        ("LeafRightUpLegRoll2Rz", "LeafRightUpLegRoll2Rz"),
    )

    LeafRightUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll2RAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll2RPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll2RField(
    CompoundField[LeafRightUpLegRoll2RAttrOperator, LeafRightUpLegRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll2RAttrOperator
    PLUG_CLS = LeafRightUpLegRoll2RPlugOperator

    LeafRightUpLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll2SPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll2Sx", "LeafRightUpLegRoll2Sx"),
        ("LeafRightUpLegRoll2Sy", "LeafRightUpLegRoll2Sy"),
        ("LeafRightUpLegRoll2Sz", "LeafRightUpLegRoll2Sz"),
    )

    LeafRightUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll2SAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll2SPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll2SField(
    CompoundField[LeafRightUpLegRoll2SAttrOperator, LeafRightUpLegRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll2SAttrOperator
    PLUG_CLS = LeafRightUpLegRoll2SPlugOperator

    LeafRightUpLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll2TPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll2Tx", "LeafRightLegRoll2Tx"),
        ("LeafRightLegRoll2Ty", "LeafRightLegRoll2Ty"),
        ("LeafRightLegRoll2Tz", "LeafRightLegRoll2Tz"),
    )

    LeafRightLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll2TAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll2TPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll2TField(
    CompoundField[LeafRightLegRoll2TAttrOperator, LeafRightLegRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll2TAttrOperator
    PLUG_CLS = LeafRightLegRoll2TPlugOperator

    LeafRightLegRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll2RPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll2Rx", "LeafRightLegRoll2Rx"),
        ("LeafRightLegRoll2Ry", "LeafRightLegRoll2Ry"),
        ("LeafRightLegRoll2Rz", "LeafRightLegRoll2Rz"),
    )

    LeafRightLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll2RAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll2RPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll2RField(
    CompoundField[LeafRightLegRoll2RAttrOperator, LeafRightLegRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll2RAttrOperator
    PLUG_CLS = LeafRightLegRoll2RPlugOperator

    LeafRightLegRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll2SPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll2Sx", "LeafRightLegRoll2Sx"),
        ("LeafRightLegRoll2Sy", "LeafRightLegRoll2Sy"),
        ("LeafRightLegRoll2Sz", "LeafRightLegRoll2Sz"),
    )

    LeafRightLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll2SAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll2SPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll2SField(
    CompoundField[LeafRightLegRoll2SAttrOperator, LeafRightLegRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll2SAttrOperator
    PLUG_CLS = LeafRightLegRoll2SPlugOperator

    LeafRightLegRoll2Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll2TPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll2Tx", "LeafLeftArmRoll2Tx"),
        ("LeafLeftArmRoll2Ty", "LeafLeftArmRoll2Ty"),
        ("LeafLeftArmRoll2Tz", "LeafLeftArmRoll2Tz"),
    )

    LeafLeftArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll2TAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll2TPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll2TField(
    CompoundField[LeafLeftArmRoll2TAttrOperator, LeafLeftArmRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll2TAttrOperator
    PLUG_CLS = LeafLeftArmRoll2TPlugOperator

    LeafLeftArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll2RPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll2Rx", "LeafLeftArmRoll2Rx"),
        ("LeafLeftArmRoll2Ry", "LeafLeftArmRoll2Ry"),
        ("LeafLeftArmRoll2Rz", "LeafLeftArmRoll2Rz"),
    )

    LeafLeftArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll2RAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll2RPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll2RField(
    CompoundField[LeafLeftArmRoll2RAttrOperator, LeafLeftArmRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll2RAttrOperator
    PLUG_CLS = LeafLeftArmRoll2RPlugOperator

    LeafLeftArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll2SPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll2Sx", "LeafLeftArmRoll2Sx"),
        ("LeafLeftArmRoll2Sy", "LeafLeftArmRoll2Sy"),
        ("LeafLeftArmRoll2Sz", "LeafLeftArmRoll2Sz"),
    )

    LeafLeftArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll2SAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll2SPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll2SField(
    CompoundField[LeafLeftArmRoll2SAttrOperator, LeafLeftArmRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll2SAttrOperator
    PLUG_CLS = LeafLeftArmRoll2SPlugOperator

    LeafLeftArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll2TPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll2Tx", "LeafLeftForeArmRoll2Tx"),
        ("LeafLeftForeArmRoll2Ty", "LeafLeftForeArmRoll2Ty"),
        ("LeafLeftForeArmRoll2Tz", "LeafLeftForeArmRoll2Tz"),
    )

    LeafLeftForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll2TAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll2TPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll2TField(
    CompoundField[LeafLeftForeArmRoll2TAttrOperator, LeafLeftForeArmRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll2TAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll2TPlugOperator

    LeafLeftForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll2RPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll2Rx", "LeafLeftForeArmRoll2Rx"),
        ("LeafLeftForeArmRoll2Ry", "LeafLeftForeArmRoll2Ry"),
        ("LeafLeftForeArmRoll2Rz", "LeafLeftForeArmRoll2Rz"),
    )

    LeafLeftForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll2RAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll2RPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll2RField(
    CompoundField[LeafLeftForeArmRoll2RAttrOperator, LeafLeftForeArmRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll2RAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll2RPlugOperator

    LeafLeftForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll2SPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll2Sx", "LeafLeftForeArmRoll2Sx"),
        ("LeafLeftForeArmRoll2Sy", "LeafLeftForeArmRoll2Sy"),
        ("LeafLeftForeArmRoll2Sz", "LeafLeftForeArmRoll2Sz"),
    )

    LeafLeftForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll2SAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll2SPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll2SField(
    CompoundField[LeafLeftForeArmRoll2SAttrOperator, LeafLeftForeArmRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll2SAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll2SPlugOperator

    LeafLeftForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll2TPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll2Tx", "LeafRightArmRoll2Tx"),
        ("LeafRightArmRoll2Ty", "LeafRightArmRoll2Ty"),
        ("LeafRightArmRoll2Tz", "LeafRightArmRoll2Tz"),
    )

    LeafRightArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll2TAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll2TPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll2TField(
    CompoundField[LeafRightArmRoll2TAttrOperator, LeafRightArmRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll2TAttrOperator
    PLUG_CLS = LeafRightArmRoll2TPlugOperator

    LeafRightArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll2RPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll2Rx", "LeafRightArmRoll2Rx"),
        ("LeafRightArmRoll2Ry", "LeafRightArmRoll2Ry"),
        ("LeafRightArmRoll2Rz", "LeafRightArmRoll2Rz"),
    )

    LeafRightArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll2RAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll2RPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll2RField(
    CompoundField[LeafRightArmRoll2RAttrOperator, LeafRightArmRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll2RAttrOperator
    PLUG_CLS = LeafRightArmRoll2RPlugOperator

    LeafRightArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll2SPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll2Sx", "LeafRightArmRoll2Sx"),
        ("LeafRightArmRoll2Sy", "LeafRightArmRoll2Sy"),
        ("LeafRightArmRoll2Sz", "LeafRightArmRoll2Sz"),
    )

    LeafRightArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll2SAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll2SPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll2SField(
    CompoundField[LeafRightArmRoll2SAttrOperator, LeafRightArmRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll2SAttrOperator
    PLUG_CLS = LeafRightArmRoll2SPlugOperator

    LeafRightArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll2TPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll2TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll2Tx", "LeafRightForeArmRoll2Tx"),
        ("LeafRightForeArmRoll2Ty", "LeafRightForeArmRoll2Ty"),
        ("LeafRightForeArmRoll2Tz", "LeafRightForeArmRoll2Tz"),
    )

    LeafRightForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll2TAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll2TPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll2TField(
    CompoundField[LeafRightForeArmRoll2TAttrOperator, LeafRightForeArmRoll2TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll2TAttrOperator
    PLUG_CLS = LeafRightForeArmRoll2TPlugOperator

    LeafRightForeArmRoll2Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll2Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll2RPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll2RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll2Rx", "LeafRightForeArmRoll2Rx"),
        ("LeafRightForeArmRoll2Ry", "LeafRightForeArmRoll2Ry"),
        ("LeafRightForeArmRoll2Rz", "LeafRightForeArmRoll2Rz"),
    )

    LeafRightForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll2RAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll2RPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll2RField(
    CompoundField[LeafRightForeArmRoll2RAttrOperator, LeafRightForeArmRoll2RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll2RAttrOperator
    PLUG_CLS = LeafRightForeArmRoll2RPlugOperator

    LeafRightForeArmRoll2Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll2Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll2SPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll2SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll2Sx", "LeafRightForeArmRoll2Sx"),
        ("LeafRightForeArmRoll2Sy", "LeafRightForeArmRoll2Sy"),
        ("LeafRightForeArmRoll2Sz", "LeafRightForeArmRoll2Sz"),
    )

    LeafRightForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll2SAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll2SPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll2SField(
    CompoundField[LeafRightForeArmRoll2SAttrOperator, LeafRightForeArmRoll2SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll2SAttrOperator
    PLUG_CLS = LeafRightForeArmRoll2SPlugOperator

    LeafRightForeArmRoll2Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll2Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll3TPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll3Tx", "LeafLeftUpLegRoll3Tx"),
        ("LeafLeftUpLegRoll3Ty", "LeafLeftUpLegRoll3Ty"),
        ("LeafLeftUpLegRoll3Tz", "LeafLeftUpLegRoll3Tz"),
    )

    LeafLeftUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll3TAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll3TPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll3TField(
    CompoundField[LeafLeftUpLegRoll3TAttrOperator, LeafLeftUpLegRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll3TAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll3TPlugOperator

    LeafLeftUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll3RPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll3Rx", "LeafLeftUpLegRoll3Rx"),
        ("LeafLeftUpLegRoll3Ry", "LeafLeftUpLegRoll3Ry"),
        ("LeafLeftUpLegRoll3Rz", "LeafLeftUpLegRoll3Rz"),
    )

    LeafLeftUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll3RAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll3RPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll3RField(
    CompoundField[LeafLeftUpLegRoll3RAttrOperator, LeafLeftUpLegRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll3RAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll3RPlugOperator

    LeafLeftUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll3SPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll3Sx", "LeafLeftUpLegRoll3Sx"),
        ("LeafLeftUpLegRoll3Sy", "LeafLeftUpLegRoll3Sy"),
        ("LeafLeftUpLegRoll3Sz", "LeafLeftUpLegRoll3Sz"),
    )

    LeafLeftUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll3SAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll3SPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll3SField(
    CompoundField[LeafLeftUpLegRoll3SAttrOperator, LeafLeftUpLegRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll3SAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll3SPlugOperator

    LeafLeftUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll3TPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll3Tx", "LeafLeftLegRoll3Tx"),
        ("LeafLeftLegRoll3Ty", "LeafLeftLegRoll3Ty"),
        ("LeafLeftLegRoll3Tz", "LeafLeftLegRoll3Tz"),
    )

    LeafLeftLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll3TAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll3TPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll3TField(
    CompoundField[LeafLeftLegRoll3TAttrOperator, LeafLeftLegRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll3TAttrOperator
    PLUG_CLS = LeafLeftLegRoll3TPlugOperator

    LeafLeftLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll3RPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll3Rx", "LeafLeftLegRoll3Rx"),
        ("LeafLeftLegRoll3Ry", "LeafLeftLegRoll3Ry"),
        ("LeafLeftLegRoll3Rz", "LeafLeftLegRoll3Rz"),
    )

    LeafLeftLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll3RAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll3RPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll3RField(
    CompoundField[LeafLeftLegRoll3RAttrOperator, LeafLeftLegRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll3RAttrOperator
    PLUG_CLS = LeafLeftLegRoll3RPlugOperator

    LeafLeftLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll3SPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll3Sx", "LeafLeftLegRoll3Sx"),
        ("LeafLeftLegRoll3Sy", "LeafLeftLegRoll3Sy"),
        ("LeafLeftLegRoll3Sz", "LeafLeftLegRoll3Sz"),
    )

    LeafLeftLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll3SAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll3SPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll3SField(
    CompoundField[LeafLeftLegRoll3SAttrOperator, LeafLeftLegRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll3SAttrOperator
    PLUG_CLS = LeafLeftLegRoll3SPlugOperator

    LeafLeftLegRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll3TPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll3Tx", "LeafRightUpLegRoll3Tx"),
        ("LeafRightUpLegRoll3Ty", "LeafRightUpLegRoll3Ty"),
        ("LeafRightUpLegRoll3Tz", "LeafRightUpLegRoll3Tz"),
    )

    LeafRightUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll3TAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll3TPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll3TField(
    CompoundField[LeafRightUpLegRoll3TAttrOperator, LeafRightUpLegRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll3TAttrOperator
    PLUG_CLS = LeafRightUpLegRoll3TPlugOperator

    LeafRightUpLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll3RPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll3Rx", "LeafRightUpLegRoll3Rx"),
        ("LeafRightUpLegRoll3Ry", "LeafRightUpLegRoll3Ry"),
        ("LeafRightUpLegRoll3Rz", "LeafRightUpLegRoll3Rz"),
    )

    LeafRightUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll3RAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll3RPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll3RField(
    CompoundField[LeafRightUpLegRoll3RAttrOperator, LeafRightUpLegRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll3RAttrOperator
    PLUG_CLS = LeafRightUpLegRoll3RPlugOperator

    LeafRightUpLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll3SPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll3Sx", "LeafRightUpLegRoll3Sx"),
        ("LeafRightUpLegRoll3Sy", "LeafRightUpLegRoll3Sy"),
        ("LeafRightUpLegRoll3Sz", "LeafRightUpLegRoll3Sz"),
    )

    LeafRightUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll3SAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll3SPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll3SField(
    CompoundField[LeafRightUpLegRoll3SAttrOperator, LeafRightUpLegRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll3SAttrOperator
    PLUG_CLS = LeafRightUpLegRoll3SPlugOperator

    LeafRightUpLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll3TPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll3Tx", "LeafRightLegRoll3Tx"),
        ("LeafRightLegRoll3Ty", "LeafRightLegRoll3Ty"),
        ("LeafRightLegRoll3Tz", "LeafRightLegRoll3Tz"),
    )

    LeafRightLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll3TAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll3TPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll3TField(
    CompoundField[LeafRightLegRoll3TAttrOperator, LeafRightLegRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll3TAttrOperator
    PLUG_CLS = LeafRightLegRoll3TPlugOperator

    LeafRightLegRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll3RPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll3Rx", "LeafRightLegRoll3Rx"),
        ("LeafRightLegRoll3Ry", "LeafRightLegRoll3Ry"),
        ("LeafRightLegRoll3Rz", "LeafRightLegRoll3Rz"),
    )

    LeafRightLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll3RAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll3RPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll3RField(
    CompoundField[LeafRightLegRoll3RAttrOperator, LeafRightLegRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll3RAttrOperator
    PLUG_CLS = LeafRightLegRoll3RPlugOperator

    LeafRightLegRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll3SPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll3Sx", "LeafRightLegRoll3Sx"),
        ("LeafRightLegRoll3Sy", "LeafRightLegRoll3Sy"),
        ("LeafRightLegRoll3Sz", "LeafRightLegRoll3Sz"),
    )

    LeafRightLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll3SAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll3SPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll3SField(
    CompoundField[LeafRightLegRoll3SAttrOperator, LeafRightLegRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll3SAttrOperator
    PLUG_CLS = LeafRightLegRoll3SPlugOperator

    LeafRightLegRoll3Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll3TPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll3Tx", "LeafLeftArmRoll3Tx"),
        ("LeafLeftArmRoll3Ty", "LeafLeftArmRoll3Ty"),
        ("LeafLeftArmRoll3Tz", "LeafLeftArmRoll3Tz"),
    )

    LeafLeftArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll3TAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll3TPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll3TField(
    CompoundField[LeafLeftArmRoll3TAttrOperator, LeafLeftArmRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll3TAttrOperator
    PLUG_CLS = LeafLeftArmRoll3TPlugOperator

    LeafLeftArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll3RPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll3Rx", "LeafLeftArmRoll3Rx"),
        ("LeafLeftArmRoll3Ry", "LeafLeftArmRoll3Ry"),
        ("LeafLeftArmRoll3Rz", "LeafLeftArmRoll3Rz"),
    )

    LeafLeftArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll3RAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll3RPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll3RField(
    CompoundField[LeafLeftArmRoll3RAttrOperator, LeafLeftArmRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll3RAttrOperator
    PLUG_CLS = LeafLeftArmRoll3RPlugOperator

    LeafLeftArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll3SPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll3Sx", "LeafLeftArmRoll3Sx"),
        ("LeafLeftArmRoll3Sy", "LeafLeftArmRoll3Sy"),
        ("LeafLeftArmRoll3Sz", "LeafLeftArmRoll3Sz"),
    )

    LeafLeftArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll3SAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll3SPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll3SField(
    CompoundField[LeafLeftArmRoll3SAttrOperator, LeafLeftArmRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll3SAttrOperator
    PLUG_CLS = LeafLeftArmRoll3SPlugOperator

    LeafLeftArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll3TPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll3Tx", "LeafLeftForeArmRoll3Tx"),
        ("LeafLeftForeArmRoll3Ty", "LeafLeftForeArmRoll3Ty"),
        ("LeafLeftForeArmRoll3Tz", "LeafLeftForeArmRoll3Tz"),
    )

    LeafLeftForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll3TAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll3TPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll3TField(
    CompoundField[LeafLeftForeArmRoll3TAttrOperator, LeafLeftForeArmRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll3TAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll3TPlugOperator

    LeafLeftForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll3RPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll3Rx", "LeafLeftForeArmRoll3Rx"),
        ("LeafLeftForeArmRoll3Ry", "LeafLeftForeArmRoll3Ry"),
        ("LeafLeftForeArmRoll3Rz", "LeafLeftForeArmRoll3Rz"),
    )

    LeafLeftForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll3RAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll3RPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll3RField(
    CompoundField[LeafLeftForeArmRoll3RAttrOperator, LeafLeftForeArmRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll3RAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll3RPlugOperator

    LeafLeftForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll3SPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll3Sx", "LeafLeftForeArmRoll3Sx"),
        ("LeafLeftForeArmRoll3Sy", "LeafLeftForeArmRoll3Sy"),
        ("LeafLeftForeArmRoll3Sz", "LeafLeftForeArmRoll3Sz"),
    )

    LeafLeftForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll3SAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll3SPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll3SField(
    CompoundField[LeafLeftForeArmRoll3SAttrOperator, LeafLeftForeArmRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll3SAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll3SPlugOperator

    LeafLeftForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll3TPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll3Tx", "LeafRightArmRoll3Tx"),
        ("LeafRightArmRoll3Ty", "LeafRightArmRoll3Ty"),
        ("LeafRightArmRoll3Tz", "LeafRightArmRoll3Tz"),
    )

    LeafRightArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll3TAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll3TPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll3TField(
    CompoundField[LeafRightArmRoll3TAttrOperator, LeafRightArmRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll3TAttrOperator
    PLUG_CLS = LeafRightArmRoll3TPlugOperator

    LeafRightArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll3RPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll3Rx", "LeafRightArmRoll3Rx"),
        ("LeafRightArmRoll3Ry", "LeafRightArmRoll3Ry"),
        ("LeafRightArmRoll3Rz", "LeafRightArmRoll3Rz"),
    )

    LeafRightArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll3RAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll3RPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll3RField(
    CompoundField[LeafRightArmRoll3RAttrOperator, LeafRightArmRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll3RAttrOperator
    PLUG_CLS = LeafRightArmRoll3RPlugOperator

    LeafRightArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll3SPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll3Sx", "LeafRightArmRoll3Sx"),
        ("LeafRightArmRoll3Sy", "LeafRightArmRoll3Sy"),
        ("LeafRightArmRoll3Sz", "LeafRightArmRoll3Sz"),
    )

    LeafRightArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll3SAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll3SPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll3SField(
    CompoundField[LeafRightArmRoll3SAttrOperator, LeafRightArmRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll3SAttrOperator
    PLUG_CLS = LeafRightArmRoll3SPlugOperator

    LeafRightArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll3TPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll3TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll3Tx", "LeafRightForeArmRoll3Tx"),
        ("LeafRightForeArmRoll3Ty", "LeafRightForeArmRoll3Ty"),
        ("LeafRightForeArmRoll3Tz", "LeafRightForeArmRoll3Tz"),
    )

    LeafRightForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll3TAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll3TPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll3TField(
    CompoundField[LeafRightForeArmRoll3TAttrOperator, LeafRightForeArmRoll3TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll3TAttrOperator
    PLUG_CLS = LeafRightForeArmRoll3TPlugOperator

    LeafRightForeArmRoll3Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll3Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll3RPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll3RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll3Rx", "LeafRightForeArmRoll3Rx"),
        ("LeafRightForeArmRoll3Ry", "LeafRightForeArmRoll3Ry"),
        ("LeafRightForeArmRoll3Rz", "LeafRightForeArmRoll3Rz"),
    )

    LeafRightForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll3RAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll3RPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll3RField(
    CompoundField[LeafRightForeArmRoll3RAttrOperator, LeafRightForeArmRoll3RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll3RAttrOperator
    PLUG_CLS = LeafRightForeArmRoll3RPlugOperator

    LeafRightForeArmRoll3Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll3Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll3SPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll3SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll3Sx", "LeafRightForeArmRoll3Sx"),
        ("LeafRightForeArmRoll3Sy", "LeafRightForeArmRoll3Sy"),
        ("LeafRightForeArmRoll3Sz", "LeafRightForeArmRoll3Sz"),
    )

    LeafRightForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll3SAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll3SPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll3SField(
    CompoundField[LeafRightForeArmRoll3SAttrOperator, LeafRightForeArmRoll3SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll3SAttrOperator
    PLUG_CLS = LeafRightForeArmRoll3SPlugOperator

    LeafRightForeArmRoll3Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll3Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll4TPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll4Tx", "LeafLeftUpLegRoll4Tx"),
        ("LeafLeftUpLegRoll4Ty", "LeafLeftUpLegRoll4Ty"),
        ("LeafLeftUpLegRoll4Tz", "LeafLeftUpLegRoll4Tz"),
    )

    LeafLeftUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll4TAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll4TPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll4TField(
    CompoundField[LeafLeftUpLegRoll4TAttrOperator, LeafLeftUpLegRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll4TAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll4TPlugOperator

    LeafLeftUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll4RPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll4Rx", "LeafLeftUpLegRoll4Rx"),
        ("LeafLeftUpLegRoll4Ry", "LeafLeftUpLegRoll4Ry"),
        ("LeafLeftUpLegRoll4Rz", "LeafLeftUpLegRoll4Rz"),
    )

    LeafLeftUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll4RAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll4RPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll4RField(
    CompoundField[LeafLeftUpLegRoll4RAttrOperator, LeafLeftUpLegRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll4RAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll4RPlugOperator

    LeafLeftUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll4SPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll4Sx", "LeafLeftUpLegRoll4Sx"),
        ("LeafLeftUpLegRoll4Sy", "LeafLeftUpLegRoll4Sy"),
        ("LeafLeftUpLegRoll4Sz", "LeafLeftUpLegRoll4Sz"),
    )

    LeafLeftUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll4SAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll4SPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll4SField(
    CompoundField[LeafLeftUpLegRoll4SAttrOperator, LeafLeftUpLegRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll4SAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll4SPlugOperator

    LeafLeftUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll4TPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll4Tx", "LeafLeftLegRoll4Tx"),
        ("LeafLeftLegRoll4Ty", "LeafLeftLegRoll4Ty"),
        ("LeafLeftLegRoll4Tz", "LeafLeftLegRoll4Tz"),
    )

    LeafLeftLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll4TAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll4TPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll4TField(
    CompoundField[LeafLeftLegRoll4TAttrOperator, LeafLeftLegRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll4TAttrOperator
    PLUG_CLS = LeafLeftLegRoll4TPlugOperator

    LeafLeftLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll4RPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll4Rx", "LeafLeftLegRoll4Rx"),
        ("LeafLeftLegRoll4Ry", "LeafLeftLegRoll4Ry"),
        ("LeafLeftLegRoll4Rz", "LeafLeftLegRoll4Rz"),
    )

    LeafLeftLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll4RAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll4RPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll4RField(
    CompoundField[LeafLeftLegRoll4RAttrOperator, LeafLeftLegRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll4RAttrOperator
    PLUG_CLS = LeafLeftLegRoll4RPlugOperator

    LeafLeftLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll4SPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll4Sx", "LeafLeftLegRoll4Sx"),
        ("LeafLeftLegRoll4Sy", "LeafLeftLegRoll4Sy"),
        ("LeafLeftLegRoll4Sz", "LeafLeftLegRoll4Sz"),
    )

    LeafLeftLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll4SAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll4SPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll4SField(
    CompoundField[LeafLeftLegRoll4SAttrOperator, LeafLeftLegRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll4SAttrOperator
    PLUG_CLS = LeafLeftLegRoll4SPlugOperator

    LeafLeftLegRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll4TPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll4Tx", "LeafRightUpLegRoll4Tx"),
        ("LeafRightUpLegRoll4Ty", "LeafRightUpLegRoll4Ty"),
        ("LeafRightUpLegRoll4Tz", "LeafRightUpLegRoll4Tz"),
    )

    LeafRightUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll4TAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll4TPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll4TField(
    CompoundField[LeafRightUpLegRoll4TAttrOperator, LeafRightUpLegRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll4TAttrOperator
    PLUG_CLS = LeafRightUpLegRoll4TPlugOperator

    LeafRightUpLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll4RPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll4Rx", "LeafRightUpLegRoll4Rx"),
        ("LeafRightUpLegRoll4Ry", "LeafRightUpLegRoll4Ry"),
        ("LeafRightUpLegRoll4Rz", "LeafRightUpLegRoll4Rz"),
    )

    LeafRightUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll4RAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll4RPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll4RField(
    CompoundField[LeafRightUpLegRoll4RAttrOperator, LeafRightUpLegRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll4RAttrOperator
    PLUG_CLS = LeafRightUpLegRoll4RPlugOperator

    LeafRightUpLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll4SPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll4Sx", "LeafRightUpLegRoll4Sx"),
        ("LeafRightUpLegRoll4Sy", "LeafRightUpLegRoll4Sy"),
        ("LeafRightUpLegRoll4Sz", "LeafRightUpLegRoll4Sz"),
    )

    LeafRightUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll4SAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll4SPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll4SField(
    CompoundField[LeafRightUpLegRoll4SAttrOperator, LeafRightUpLegRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll4SAttrOperator
    PLUG_CLS = LeafRightUpLegRoll4SPlugOperator

    LeafRightUpLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll4TPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll4Tx", "LeafRightLegRoll4Tx"),
        ("LeafRightLegRoll4Ty", "LeafRightLegRoll4Ty"),
        ("LeafRightLegRoll4Tz", "LeafRightLegRoll4Tz"),
    )

    LeafRightLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll4TAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll4TPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll4TField(
    CompoundField[LeafRightLegRoll4TAttrOperator, LeafRightLegRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll4TAttrOperator
    PLUG_CLS = LeafRightLegRoll4TPlugOperator

    LeafRightLegRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll4RPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll4Rx", "LeafRightLegRoll4Rx"),
        ("LeafRightLegRoll4Ry", "LeafRightLegRoll4Ry"),
        ("LeafRightLegRoll4Rz", "LeafRightLegRoll4Rz"),
    )

    LeafRightLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll4RAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll4RPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll4RField(
    CompoundField[LeafRightLegRoll4RAttrOperator, LeafRightLegRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll4RAttrOperator
    PLUG_CLS = LeafRightLegRoll4RPlugOperator

    LeafRightLegRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll4SPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll4Sx", "LeafRightLegRoll4Sx"),
        ("LeafRightLegRoll4Sy", "LeafRightLegRoll4Sy"),
        ("LeafRightLegRoll4Sz", "LeafRightLegRoll4Sz"),
    )

    LeafRightLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll4SAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll4SPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll4SField(
    CompoundField[LeafRightLegRoll4SAttrOperator, LeafRightLegRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll4SAttrOperator
    PLUG_CLS = LeafRightLegRoll4SPlugOperator

    LeafRightLegRoll4Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll4TPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll4Tx", "LeafLeftArmRoll4Tx"),
        ("LeafLeftArmRoll4Ty", "LeafLeftArmRoll4Ty"),
        ("LeafLeftArmRoll4Tz", "LeafLeftArmRoll4Tz"),
    )

    LeafLeftArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll4TAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll4TPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll4TField(
    CompoundField[LeafLeftArmRoll4TAttrOperator, LeafLeftArmRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll4TAttrOperator
    PLUG_CLS = LeafLeftArmRoll4TPlugOperator

    LeafLeftArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll4RPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll4Rx", "LeafLeftArmRoll4Rx"),
        ("LeafLeftArmRoll4Ry", "LeafLeftArmRoll4Ry"),
        ("LeafLeftArmRoll4Rz", "LeafLeftArmRoll4Rz"),
    )

    LeafLeftArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll4RAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll4RPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll4RField(
    CompoundField[LeafLeftArmRoll4RAttrOperator, LeafLeftArmRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll4RAttrOperator
    PLUG_CLS = LeafLeftArmRoll4RPlugOperator

    LeafLeftArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll4SPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll4Sx", "LeafLeftArmRoll4Sx"),
        ("LeafLeftArmRoll4Sy", "LeafLeftArmRoll4Sy"),
        ("LeafLeftArmRoll4Sz", "LeafLeftArmRoll4Sz"),
    )

    LeafLeftArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll4SAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll4SPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll4SField(
    CompoundField[LeafLeftArmRoll4SAttrOperator, LeafLeftArmRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll4SAttrOperator
    PLUG_CLS = LeafLeftArmRoll4SPlugOperator

    LeafLeftArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll4TPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll4Tx", "LeafLeftForeArmRoll4Tx"),
        ("LeafLeftForeArmRoll4Ty", "LeafLeftForeArmRoll4Ty"),
        ("LeafLeftForeArmRoll4Tz", "LeafLeftForeArmRoll4Tz"),
    )

    LeafLeftForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll4TAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll4TPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll4TField(
    CompoundField[LeafLeftForeArmRoll4TAttrOperator, LeafLeftForeArmRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll4TAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll4TPlugOperator

    LeafLeftForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll4RPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll4Rx", "LeafLeftForeArmRoll4Rx"),
        ("LeafLeftForeArmRoll4Ry", "LeafLeftForeArmRoll4Ry"),
        ("LeafLeftForeArmRoll4Rz", "LeafLeftForeArmRoll4Rz"),
    )

    LeafLeftForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll4RAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll4RPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll4RField(
    CompoundField[LeafLeftForeArmRoll4RAttrOperator, LeafLeftForeArmRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll4RAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll4RPlugOperator

    LeafLeftForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll4SPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll4Sx", "LeafLeftForeArmRoll4Sx"),
        ("LeafLeftForeArmRoll4Sy", "LeafLeftForeArmRoll4Sy"),
        ("LeafLeftForeArmRoll4Sz", "LeafLeftForeArmRoll4Sz"),
    )

    LeafLeftForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll4SAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll4SPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll4SField(
    CompoundField[LeafLeftForeArmRoll4SAttrOperator, LeafLeftForeArmRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll4SAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll4SPlugOperator

    LeafLeftForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll4TPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll4Tx", "LeafRightArmRoll4Tx"),
        ("LeafRightArmRoll4Ty", "LeafRightArmRoll4Ty"),
        ("LeafRightArmRoll4Tz", "LeafRightArmRoll4Tz"),
    )

    LeafRightArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll4TAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll4TPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll4TField(
    CompoundField[LeafRightArmRoll4TAttrOperator, LeafRightArmRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll4TAttrOperator
    PLUG_CLS = LeafRightArmRoll4TPlugOperator

    LeafRightArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll4RPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll4Rx", "LeafRightArmRoll4Rx"),
        ("LeafRightArmRoll4Ry", "LeafRightArmRoll4Ry"),
        ("LeafRightArmRoll4Rz", "LeafRightArmRoll4Rz"),
    )

    LeafRightArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll4RAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll4RPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll4RField(
    CompoundField[LeafRightArmRoll4RAttrOperator, LeafRightArmRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll4RAttrOperator
    PLUG_CLS = LeafRightArmRoll4RPlugOperator

    LeafRightArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll4SPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll4Sx", "LeafRightArmRoll4Sx"),
        ("LeafRightArmRoll4Sy", "LeafRightArmRoll4Sy"),
        ("LeafRightArmRoll4Sz", "LeafRightArmRoll4Sz"),
    )

    LeafRightArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll4SAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll4SPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll4SField(
    CompoundField[LeafRightArmRoll4SAttrOperator, LeafRightArmRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll4SAttrOperator
    PLUG_CLS = LeafRightArmRoll4SPlugOperator

    LeafRightArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll4TPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll4TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll4Tx", "LeafRightForeArmRoll4Tx"),
        ("LeafRightForeArmRoll4Ty", "LeafRightForeArmRoll4Ty"),
        ("LeafRightForeArmRoll4Tz", "LeafRightForeArmRoll4Tz"),
    )

    LeafRightForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll4TAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll4TPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll4TField(
    CompoundField[LeafRightForeArmRoll4TAttrOperator, LeafRightForeArmRoll4TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll4TAttrOperator
    PLUG_CLS = LeafRightForeArmRoll4TPlugOperator

    LeafRightForeArmRoll4Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll4Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll4RPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll4RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll4Rx", "LeafRightForeArmRoll4Rx"),
        ("LeafRightForeArmRoll4Ry", "LeafRightForeArmRoll4Ry"),
        ("LeafRightForeArmRoll4Rz", "LeafRightForeArmRoll4Rz"),
    )

    LeafRightForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll4RAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll4RPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll4RField(
    CompoundField[LeafRightForeArmRoll4RAttrOperator, LeafRightForeArmRoll4RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll4RAttrOperator
    PLUG_CLS = LeafRightForeArmRoll4RPlugOperator

    LeafRightForeArmRoll4Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll4Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll4SPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll4SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll4Sx", "LeafRightForeArmRoll4Sx"),
        ("LeafRightForeArmRoll4Sy", "LeafRightForeArmRoll4Sy"),
        ("LeafRightForeArmRoll4Sz", "LeafRightForeArmRoll4Sz"),
    )

    LeafRightForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll4SAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll4SPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll4SField(
    CompoundField[LeafRightForeArmRoll4SAttrOperator, LeafRightForeArmRoll4SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll4SAttrOperator
    PLUG_CLS = LeafRightForeArmRoll4SPlugOperator

    LeafRightForeArmRoll4Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll4Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll5TPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll5Tx", "LeafLeftUpLegRoll5Tx"),
        ("LeafLeftUpLegRoll5Ty", "LeafLeftUpLegRoll5Ty"),
        ("LeafLeftUpLegRoll5Tz", "LeafLeftUpLegRoll5Tz"),
    )

    LeafLeftUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll5TAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll5TPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll5TField(
    CompoundField[LeafLeftUpLegRoll5TAttrOperator, LeafLeftUpLegRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll5TAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll5TPlugOperator

    LeafLeftUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftUpLegRoll5RPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll5Rx", "LeafLeftUpLegRoll5Rx"),
        ("LeafLeftUpLegRoll5Ry", "LeafLeftUpLegRoll5Ry"),
        ("LeafLeftUpLegRoll5Rz", "LeafLeftUpLegRoll5Rz"),
    )

    LeafLeftUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll5RAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll5RPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll5RField(
    CompoundField[LeafLeftUpLegRoll5RAttrOperator, LeafLeftUpLegRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll5RAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll5RPlugOperator

    LeafLeftUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftUpLegRoll5SPlugOperator(
    CompoundPlugOperator["LeafLeftUpLegRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftUpLegRoll5Sx", "LeafLeftUpLegRoll5Sx"),
        ("LeafLeftUpLegRoll5Sy", "LeafLeftUpLegRoll5Sy"),
        ("LeafLeftUpLegRoll5Sz", "LeafLeftUpLegRoll5Sz"),
    )

    LeafLeftUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll5SAttrOperator(
    CompoundAttrOperator[LeafLeftUpLegRoll5SPlugOperator]
):
    __slots__ = ()

    LeafLeftUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftUpLegRoll5SField(
    CompoundField[LeafLeftUpLegRoll5SAttrOperator, LeafLeftUpLegRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftUpLegRoll5SAttrOperator
    PLUG_CLS = LeafLeftUpLegRoll5SPlugOperator

    LeafLeftUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll5TPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll5Tx", "LeafLeftLegRoll5Tx"),
        ("LeafLeftLegRoll5Ty", "LeafLeftLegRoll5Ty"),
        ("LeafLeftLegRoll5Tz", "LeafLeftLegRoll5Tz"),
    )

    LeafLeftLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll5TAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll5TPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll5TField(
    CompoundField[LeafLeftLegRoll5TAttrOperator, LeafLeftLegRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll5TAttrOperator
    PLUG_CLS = LeafLeftLegRoll5TPlugOperator

    LeafLeftLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftLegRoll5RPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll5Rx", "LeafLeftLegRoll5Rx"),
        ("LeafLeftLegRoll5Ry", "LeafLeftLegRoll5Ry"),
        ("LeafLeftLegRoll5Rz", "LeafLeftLegRoll5Rz"),
    )

    LeafLeftLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll5RAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll5RPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll5RField(
    CompoundField[LeafLeftLegRoll5RAttrOperator, LeafLeftLegRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll5RAttrOperator
    PLUG_CLS = LeafLeftLegRoll5RPlugOperator

    LeafLeftLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftLegRoll5SPlugOperator(
    CompoundPlugOperator["LeafLeftLegRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftLegRoll5Sx", "LeafLeftLegRoll5Sx"),
        ("LeafLeftLegRoll5Sy", "LeafLeftLegRoll5Sy"),
        ("LeafLeftLegRoll5Sz", "LeafLeftLegRoll5Sz"),
    )

    LeafLeftLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll5SAttrOperator(
    CompoundAttrOperator[LeafLeftLegRoll5SPlugOperator]
):
    __slots__ = ()

    LeafLeftLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftLegRoll5SField(
    CompoundField[LeafLeftLegRoll5SAttrOperator, LeafLeftLegRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftLegRoll5SAttrOperator
    PLUG_CLS = LeafLeftLegRoll5SPlugOperator

    LeafLeftLegRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll5TPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll5Tx", "LeafRightUpLegRoll5Tx"),
        ("LeafRightUpLegRoll5Ty", "LeafRightUpLegRoll5Ty"),
        ("LeafRightUpLegRoll5Tz", "LeafRightUpLegRoll5Tz"),
    )

    LeafRightUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll5TAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll5TPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll5TField(
    CompoundField[LeafRightUpLegRoll5TAttrOperator, LeafRightUpLegRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll5TAttrOperator
    PLUG_CLS = LeafRightUpLegRoll5TPlugOperator

    LeafRightUpLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightUpLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightUpLegRoll5RPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll5Rx", "LeafRightUpLegRoll5Rx"),
        ("LeafRightUpLegRoll5Ry", "LeafRightUpLegRoll5Ry"),
        ("LeafRightUpLegRoll5Rz", "LeafRightUpLegRoll5Rz"),
    )

    LeafRightUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll5RAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll5RPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll5RField(
    CompoundField[LeafRightUpLegRoll5RAttrOperator, LeafRightUpLegRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll5RAttrOperator
    PLUG_CLS = LeafRightUpLegRoll5RPlugOperator

    LeafRightUpLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightUpLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightUpLegRoll5SPlugOperator(
    CompoundPlugOperator["LeafRightUpLegRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightUpLegRoll5Sx", "LeafRightUpLegRoll5Sx"),
        ("LeafRightUpLegRoll5Sy", "LeafRightUpLegRoll5Sy"),
        ("LeafRightUpLegRoll5Sz", "LeafRightUpLegRoll5Sz"),
    )

    LeafRightUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll5SAttrOperator(
    CompoundAttrOperator[LeafRightUpLegRoll5SPlugOperator]
):
    __slots__ = ()

    LeafRightUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightUpLegRoll5SField(
    CompoundField[LeafRightUpLegRoll5SAttrOperator, LeafRightUpLegRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightUpLegRoll5SAttrOperator
    PLUG_CLS = LeafRightUpLegRoll5SPlugOperator

    LeafRightUpLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightUpLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll5TPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll5Tx", "LeafRightLegRoll5Tx"),
        ("LeafRightLegRoll5Ty", "LeafRightLegRoll5Ty"),
        ("LeafRightLegRoll5Tz", "LeafRightLegRoll5Tz"),
    )

    LeafRightLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll5TAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll5TPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll5TField(
    CompoundField[LeafRightLegRoll5TAttrOperator, LeafRightLegRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll5TAttrOperator
    PLUG_CLS = LeafRightLegRoll5TPlugOperator

    LeafRightLegRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightLegRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightLegRoll5RPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll5Rx", "LeafRightLegRoll5Rx"),
        ("LeafRightLegRoll5Ry", "LeafRightLegRoll5Ry"),
        ("LeafRightLegRoll5Rz", "LeafRightLegRoll5Rz"),
    )

    LeafRightLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll5RAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll5RPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll5RField(
    CompoundField[LeafRightLegRoll5RAttrOperator, LeafRightLegRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll5RAttrOperator
    PLUG_CLS = LeafRightLegRoll5RPlugOperator

    LeafRightLegRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightLegRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightLegRoll5SPlugOperator(
    CompoundPlugOperator["LeafRightLegRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightLegRoll5Sx", "LeafRightLegRoll5Sx"),
        ("LeafRightLegRoll5Sy", "LeafRightLegRoll5Sy"),
        ("LeafRightLegRoll5Sz", "LeafRightLegRoll5Sz"),
    )

    LeafRightLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll5SAttrOperator(
    CompoundAttrOperator[LeafRightLegRoll5SPlugOperator]
):
    __slots__ = ()

    LeafRightLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sz = DoubleField(default_value=1.0)


class LeafRightLegRoll5SField(
    CompoundField[LeafRightLegRoll5SAttrOperator, LeafRightLegRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightLegRoll5SAttrOperator
    PLUG_CLS = LeafRightLegRoll5SPlugOperator

    LeafRightLegRoll5Sx = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sy = DoubleField(default_value=1.0)

    LeafRightLegRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll5TPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll5Tx", "LeafLeftArmRoll5Tx"),
        ("LeafLeftArmRoll5Ty", "LeafLeftArmRoll5Ty"),
        ("LeafLeftArmRoll5Tz", "LeafLeftArmRoll5Tz"),
    )

    LeafLeftArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll5TAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll5TPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll5TField(
    CompoundField[LeafLeftArmRoll5TAttrOperator, LeafLeftArmRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll5TAttrOperator
    PLUG_CLS = LeafLeftArmRoll5TPlugOperator

    LeafLeftArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftArmRoll5RPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll5Rx", "LeafLeftArmRoll5Rx"),
        ("LeafLeftArmRoll5Ry", "LeafLeftArmRoll5Ry"),
        ("LeafLeftArmRoll5Rz", "LeafLeftArmRoll5Rz"),
    )

    LeafLeftArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll5RAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll5RPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll5RField(
    CompoundField[LeafLeftArmRoll5RAttrOperator, LeafLeftArmRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll5RAttrOperator
    PLUG_CLS = LeafLeftArmRoll5RPlugOperator

    LeafLeftArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftArmRoll5SPlugOperator(
    CompoundPlugOperator["LeafLeftArmRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftArmRoll5Sx", "LeafLeftArmRoll5Sx"),
        ("LeafLeftArmRoll5Sy", "LeafLeftArmRoll5Sy"),
        ("LeafLeftArmRoll5Sz", "LeafLeftArmRoll5Sz"),
    )

    LeafLeftArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll5SAttrOperator(
    CompoundAttrOperator[LeafLeftArmRoll5SPlugOperator]
):
    __slots__ = ()

    LeafLeftArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftArmRoll5SField(
    CompoundField[LeafLeftArmRoll5SAttrOperator, LeafLeftArmRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftArmRoll5SAttrOperator
    PLUG_CLS = LeafLeftArmRoll5SPlugOperator

    LeafLeftArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftArmRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll5TPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll5Tx", "LeafLeftForeArmRoll5Tx"),
        ("LeafLeftForeArmRoll5Ty", "LeafLeftForeArmRoll5Ty"),
        ("LeafLeftForeArmRoll5Tz", "LeafLeftForeArmRoll5Tz"),
    )

    LeafLeftForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll5TAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll5TPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll5TField(
    CompoundField[LeafLeftForeArmRoll5TAttrOperator, LeafLeftForeArmRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll5TAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll5TPlugOperator

    LeafLeftForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafLeftForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafLeftForeArmRoll5RPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll5Rx", "LeafLeftForeArmRoll5Rx"),
        ("LeafLeftForeArmRoll5Ry", "LeafLeftForeArmRoll5Ry"),
        ("LeafLeftForeArmRoll5Rz", "LeafLeftForeArmRoll5Rz"),
    )

    LeafLeftForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll5RAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll5RPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll5RField(
    CompoundField[LeafLeftForeArmRoll5RAttrOperator, LeafLeftForeArmRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll5RAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll5RPlugOperator

    LeafLeftForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafLeftForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafLeftForeArmRoll5SPlugOperator(
    CompoundPlugOperator["LeafLeftForeArmRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafLeftForeArmRoll5Sx", "LeafLeftForeArmRoll5Sx"),
        ("LeafLeftForeArmRoll5Sy", "LeafLeftForeArmRoll5Sy"),
        ("LeafLeftForeArmRoll5Sz", "LeafLeftForeArmRoll5Sz"),
    )

    LeafLeftForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll5SAttrOperator(
    CompoundAttrOperator[LeafLeftForeArmRoll5SPlugOperator]
):
    __slots__ = ()

    LeafLeftForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sz = DoubleField(default_value=1.0)


class LeafLeftForeArmRoll5SField(
    CompoundField[LeafLeftForeArmRoll5SAttrOperator, LeafLeftForeArmRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafLeftForeArmRoll5SAttrOperator
    PLUG_CLS = LeafLeftForeArmRoll5SPlugOperator

    LeafLeftForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafLeftForeArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll5TPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll5Tx", "LeafRightArmRoll5Tx"),
        ("LeafRightArmRoll5Ty", "LeafRightArmRoll5Ty"),
        ("LeafRightArmRoll5Tz", "LeafRightArmRoll5Tz"),
    )

    LeafRightArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll5TAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll5TPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll5TField(
    CompoundField[LeafRightArmRoll5TAttrOperator, LeafRightArmRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll5TAttrOperator
    PLUG_CLS = LeafRightArmRoll5TPlugOperator

    LeafRightArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightArmRoll5RPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll5Rx", "LeafRightArmRoll5Rx"),
        ("LeafRightArmRoll5Ry", "LeafRightArmRoll5Ry"),
        ("LeafRightArmRoll5Rz", "LeafRightArmRoll5Rz"),
    )

    LeafRightArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll5RAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll5RPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll5RField(
    CompoundField[LeafRightArmRoll5RAttrOperator, LeafRightArmRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll5RAttrOperator
    PLUG_CLS = LeafRightArmRoll5RPlugOperator

    LeafRightArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightArmRoll5SPlugOperator(
    CompoundPlugOperator["LeafRightArmRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightArmRoll5Sx", "LeafRightArmRoll5Sx"),
        ("LeafRightArmRoll5Sy", "LeafRightArmRoll5Sy"),
        ("LeafRightArmRoll5Sz", "LeafRightArmRoll5Sz"),
    )

    LeafRightArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll5SAttrOperator(
    CompoundAttrOperator[LeafRightArmRoll5SPlugOperator]
):
    __slots__ = ()

    LeafRightArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightArmRoll5SField(
    CompoundField[LeafRightArmRoll5SAttrOperator, LeafRightArmRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightArmRoll5SAttrOperator
    PLUG_CLS = LeafRightArmRoll5SPlugOperator

    LeafRightArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll5TPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll5TAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll5Tx", "LeafRightForeArmRoll5Tx"),
        ("LeafRightForeArmRoll5Ty", "LeafRightForeArmRoll5Ty"),
        ("LeafRightForeArmRoll5Tz", "LeafRightForeArmRoll5Tz"),
    )

    LeafRightForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll5TAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll5TPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll5TField(
    CompoundField[LeafRightForeArmRoll5TAttrOperator, LeafRightForeArmRoll5TPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll5TAttrOperator
    PLUG_CLS = LeafRightForeArmRoll5TPlugOperator

    LeafRightForeArmRoll5Tx = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Ty = DoubleLinearField(default_value=0.0)

    LeafRightForeArmRoll5Tz = DoubleLinearField(default_value=0.0)


class LeafRightForeArmRoll5RPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll5RAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll5Rx", "LeafRightForeArmRoll5Rx"),
        ("LeafRightForeArmRoll5Ry", "LeafRightForeArmRoll5Ry"),
        ("LeafRightForeArmRoll5Rz", "LeafRightForeArmRoll5Rz"),
    )

    LeafRightForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll5RAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll5RPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll5RField(
    CompoundField[LeafRightForeArmRoll5RAttrOperator, LeafRightForeArmRoll5RPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll5RAttrOperator
    PLUG_CLS = LeafRightForeArmRoll5RPlugOperator

    LeafRightForeArmRoll5Rx = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Ry = DoubleAngleField(default_value=0.0)

    LeafRightForeArmRoll5Rz = DoubleAngleField(default_value=0.0)


class LeafRightForeArmRoll5SPlugOperator(
    CompoundPlugOperator["LeafRightForeArmRoll5SAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("LeafRightForeArmRoll5Sx", "LeafRightForeArmRoll5Sx"),
        ("LeafRightForeArmRoll5Sy", "LeafRightForeArmRoll5Sy"),
        ("LeafRightForeArmRoll5Sz", "LeafRightForeArmRoll5Sz"),
    )

    LeafRightForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll5SAttrOperator(
    CompoundAttrOperator[LeafRightForeArmRoll5SPlugOperator]
):
    __slots__ = ()

    LeafRightForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sz = DoubleField(default_value=1.0)


class LeafRightForeArmRoll5SField(
    CompoundField[LeafRightForeArmRoll5SAttrOperator, LeafRightForeArmRoll5SPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeafRightForeArmRoll5SAttrOperator
    PLUG_CLS = LeafRightForeArmRoll5SPlugOperator

    LeafRightForeArmRoll5Sx = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sy = DoubleField(default_value=1.0)

    LeafRightForeArmRoll5Sz = DoubleField(default_value=1.0)
