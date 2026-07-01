# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutValuePlugOperator(
    Float3CompoundBasePlugOperator["OutValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outValueX", "outx"),
        ("outValueY", "outy"),
        ("outValueZ", "outz"),
    )

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


class OutValueAttrOperator(
    Float3CompoundBaseAttrOperator[OutValuePlugOperator]
):
    __slots__ = ()

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


class OutValueField(
    Float3CompoundBaseField[OutValueAttrOperator, OutValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutValueAttrOperator
    PLUG_CLS = OutValuePlugOperator

    outValueX = FloatField()
    outx = outValueX

    outValueY = FloatField()
    outy = outValueY

    outValueZ = FloatField()
    outz = outValueZ


class RoPlugOperator(
    Float3CompoundBasePlugOperator["RoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RoX", "Rox"),
        ("RoY", "Roy"),
        ("RoZ", "Roz"),
    )

    RoX = FloatField()
    Rox = RoX

    RoY = FloatField()
    Roy = RoY

    RoZ = FloatField()
    Roz = RoZ


class RoAttrOperator(
    Float3CompoundBaseAttrOperator[RoPlugOperator]
):
    __slots__ = ()

    RoX = FloatField()
    Rox = RoX

    RoY = FloatField()
    Roy = RoY

    RoZ = FloatField()
    Roz = RoZ


class RoField(
    Float3CompoundBaseField[RoAttrOperator, RoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RoAttrOperator
    PLUG_CLS = RoPlugOperator

    RoX = FloatField()
    Rox = RoX

    RoY = FloatField()
    Roy = RoY

    RoZ = FloatField()
    Roz = RoZ


class RdPlugOperator(
    Float3CompoundBasePlugOperator["RdAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("RdX", "Rdx"),
        ("RdY", "Rdy"),
        ("RdZ", "Rdz"),
    )

    RdX = FloatField()
    Rdx = RdX

    RdY = FloatField()
    Rdy = RdY

    RdZ = FloatField()
    Rdz = RdZ


class RdAttrOperator(
    Float3CompoundBaseAttrOperator[RdPlugOperator]
):
    __slots__ = ()

    RdX = FloatField()
    Rdx = RdX

    RdY = FloatField()
    Rdy = RdY

    RdZ = FloatField()
    Rdz = RdZ


class RdField(
    Float3CompoundBaseField[RdAttrOperator, RdPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RdAttrOperator
    PLUG_CLS = RdPlugOperator

    RdX = FloatField()
    Rdx = RdX

    RdY = FloatField()
    Rdy = RdY

    RdZ = FloatField()
    Rdz = RdZ


class PoPlugOperator(
    Float3CompoundBasePlugOperator["PoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PoX", "Pox"),
        ("PoY", "Poy"),
        ("PoZ", "Poz"),
    )

    PoX = FloatField()
    Pox = PoX

    PoY = FloatField()
    Poy = PoY

    PoZ = FloatField()
    Poz = PoZ


class PoAttrOperator(
    Float3CompoundBaseAttrOperator[PoPlugOperator]
):
    __slots__ = ()

    PoX = FloatField()
    Pox = PoX

    PoY = FloatField()
    Poy = PoY

    PoZ = FloatField()
    Poz = PoZ


class PoField(
    Float3CompoundBaseField[PoAttrOperator, PoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PoAttrOperator
    PLUG_CLS = PoPlugOperator

    PoX = FloatField()
    Pox = PoX

    PoY = FloatField()
    Poy = PoY

    PoZ = FloatField()
    Poz = PoZ


class PPlugOperator(
    Float3CompoundBasePlugOperator["PAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PX", "Px"),
        ("PY", "Py"),
        ("PZ", "Pz"),
    )

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PAttrOperator(
    Float3CompoundBaseAttrOperator[PPlugOperator]
):
    __slots__ = ()

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class PField(
    Float3CompoundBaseField[PAttrOperator, PPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PAttrOperator
    PLUG_CLS = PPlugOperator

    PX = FloatField()
    Px = PX

    PY = FloatField()
    Py = PY

    PZ = FloatField()
    Pz = PZ


class DPdxPlugOperator(
    Float3CompoundBasePlugOperator["DPdxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdxX", "dPdxx"),
        ("dPdxY", "dPdxy"),
        ("dPdxZ", "dPdxz"),
    )

    dPdxX = FloatField()
    dPdxx = dPdxX

    dPdxY = FloatField()
    dPdxy = dPdxY

    dPdxZ = FloatField()
    dPdxz = dPdxZ


class DPdxAttrOperator(
    Float3CompoundBaseAttrOperator[DPdxPlugOperator]
):
    __slots__ = ()

    dPdxX = FloatField()
    dPdxx = dPdxX

    dPdxY = FloatField()
    dPdxy = dPdxY

    dPdxZ = FloatField()
    dPdxz = dPdxZ


class DPdxField(
    Float3CompoundBaseField[DPdxAttrOperator, DPdxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DPdxAttrOperator
    PLUG_CLS = DPdxPlugOperator

    dPdxX = FloatField()
    dPdxx = dPdxX

    dPdxY = FloatField()
    dPdxy = dPdxY

    dPdxZ = FloatField()
    dPdxz = dPdxZ


class DPdyPlugOperator(
    Float3CompoundBasePlugOperator["DPdyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdyX", "dPdyx"),
        ("dPdyY", "dPdyy"),
        ("dPdyZ", "dPdyz"),
    )

    dPdyX = FloatField()
    dPdyx = dPdyX

    dPdyY = FloatField()
    dPdyy = dPdyY

    dPdyZ = FloatField()
    dPdyz = dPdyZ


class DPdyAttrOperator(
    Float3CompoundBaseAttrOperator[DPdyPlugOperator]
):
    __slots__ = ()

    dPdyX = FloatField()
    dPdyx = dPdyX

    dPdyY = FloatField()
    dPdyy = dPdyY

    dPdyZ = FloatField()
    dPdyz = dPdyZ


class DPdyField(
    Float3CompoundBaseField[DPdyAttrOperator, DPdyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DPdyAttrOperator
    PLUG_CLS = DPdyPlugOperator

    dPdyX = FloatField()
    dPdyx = dPdyX

    dPdyY = FloatField()
    dPdyy = dPdyY

    dPdyZ = FloatField()
    dPdyz = dPdyZ


class NPlugOperator(
    Float3CompoundBasePlugOperator["NAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NX", "Nx"),
        ("NY", "Ny"),
        ("NZ", "Nz"),
    )

    NX = FloatField()
    Nx = NX

    NY = FloatField()
    Ny = NY

    NZ = FloatField()
    Nz = NZ


class NAttrOperator(
    Float3CompoundBaseAttrOperator[NPlugOperator]
):
    __slots__ = ()

    NX = FloatField()
    Nx = NX

    NY = FloatField()
    Ny = NY

    NZ = FloatField()
    Nz = NZ


class NField(
    Float3CompoundBaseField[NAttrOperator, NPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NAttrOperator
    PLUG_CLS = NPlugOperator

    NX = FloatField()
    Nx = NX

    NY = FloatField()
    Ny = NY

    NZ = FloatField()
    Nz = NZ


class NfPlugOperator(
    Float3CompoundBasePlugOperator["NfAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NfX", "Nfx"),
        ("NfY", "Nfy"),
        ("NfZ", "Nfz"),
    )

    NfX = FloatField()
    Nfx = NfX

    NfY = FloatField()
    Nfy = NfY

    NfZ = FloatField()
    Nfz = NfZ


class NfAttrOperator(
    Float3CompoundBaseAttrOperator[NfPlugOperator]
):
    __slots__ = ()

    NfX = FloatField()
    Nfx = NfX

    NfY = FloatField()
    Nfy = NfY

    NfZ = FloatField()
    Nfz = NfZ


class NfField(
    Float3CompoundBaseField[NfAttrOperator, NfPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NfAttrOperator
    PLUG_CLS = NfPlugOperator

    NfX = FloatField()
    Nfx = NfX

    NfY = FloatField()
    Nfy = NfY

    NfZ = FloatField()
    Nfz = NfZ


class NgPlugOperator(
    Float3CompoundBasePlugOperator["NgAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NgX", "Ngx"),
        ("NgY", "Ngy"),
        ("NgZ", "Ngz"),
    )

    NgX = FloatField()
    Ngx = NgX

    NgY = FloatField()
    Ngy = NgY

    NgZ = FloatField()
    Ngz = NgZ


class NgAttrOperator(
    Float3CompoundBaseAttrOperator[NgPlugOperator]
):
    __slots__ = ()

    NgX = FloatField()
    Ngx = NgX

    NgY = FloatField()
    Ngy = NgY

    NgZ = FloatField()
    Ngz = NgZ


class NgField(
    Float3CompoundBaseField[NgAttrOperator, NgPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NgAttrOperator
    PLUG_CLS = NgPlugOperator

    NgX = FloatField()
    Ngx = NgX

    NgY = FloatField()
    Ngy = NgY

    NgZ = FloatField()
    Ngz = NgZ


class NgfPlugOperator(
    Float3CompoundBasePlugOperator["NgfAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NgfX", "Ngfx"),
        ("NgfY", "Ngfy"),
        ("NgfZ", "Ngfz"),
    )

    NgfX = FloatField()
    Ngfx = NgfX

    NgfY = FloatField()
    Ngfy = NgfY

    NgfZ = FloatField()
    Ngfz = NgfZ


class NgfAttrOperator(
    Float3CompoundBaseAttrOperator[NgfPlugOperator]
):
    __slots__ = ()

    NgfX = FloatField()
    Ngfx = NgfX

    NgfY = FloatField()
    Ngfy = NgfY

    NgfZ = FloatField()
    Ngfz = NgfZ


class NgfField(
    Float3CompoundBaseField[NgfAttrOperator, NgfPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NgfAttrOperator
    PLUG_CLS = NgfPlugOperator

    NgfX = FloatField()
    Ngfx = NgfX

    NgfY = FloatField()
    Ngfy = NgfY

    NgfZ = FloatField()
    Ngfz = NgfZ


class NsPlugOperator(
    Float3CompoundBasePlugOperator["NsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("NsX", "Nsx"),
        ("NsY", "Nsy"),
        ("NsZ", "Nsz"),
    )

    NsX = FloatField()
    Nsx = NsX

    NsY = FloatField()
    Nsy = NsY

    NsZ = FloatField()
    Nsz = NsZ


class NsAttrOperator(
    Float3CompoundBaseAttrOperator[NsPlugOperator]
):
    __slots__ = ()

    NsX = FloatField()
    Nsx = NsX

    NsY = FloatField()
    Nsy = NsY

    NsZ = FloatField()
    Nsz = NsZ


class NsField(
    Float3CompoundBaseField[NsAttrOperator, NsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NsAttrOperator
    PLUG_CLS = NsPlugOperator

    NsX = FloatField()
    Nsx = NsX

    NsY = FloatField()
    Nsy = NsY

    NsZ = FloatField()
    Nsz = NsZ


class DPduPlugOperator(
    Float3CompoundBasePlugOperator["DPduAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPduX", "dPdux"),
        ("dPduY", "dPduy"),
        ("dPduZ", "dPduz"),
    )

    dPduX = FloatField()
    dPdux = dPduX

    dPduY = FloatField()
    dPduy = dPduY

    dPduZ = FloatField()
    dPduz = dPduZ


class DPduAttrOperator(
    Float3CompoundBaseAttrOperator[DPduPlugOperator]
):
    __slots__ = ()

    dPduX = FloatField()
    dPdux = dPduX

    dPduY = FloatField()
    dPduy = dPduY

    dPduZ = FloatField()
    dPduz = dPduZ


class DPduField(
    Float3CompoundBaseField[DPduAttrOperator, DPduPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DPduAttrOperator
    PLUG_CLS = DPduPlugOperator

    dPduX = FloatField()
    dPdux = dPduX

    dPduY = FloatField()
    dPduy = dPduY

    dPduZ = FloatField()
    dPduz = dPduZ


class DPdvPlugOperator(
    Float3CompoundBasePlugOperator["DPdvAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dPdvX", "dPdvx"),
        ("dPdvY", "dPdvy"),
        ("dPdvZ", "dPdvz"),
    )

    dPdvX = FloatField()
    dPdvx = dPdvX

    dPdvY = FloatField()
    dPdvy = dPdvY

    dPdvZ = FloatField()
    dPdvz = dPdvZ


class DPdvAttrOperator(
    Float3CompoundBaseAttrOperator[DPdvPlugOperator]
):
    __slots__ = ()

    dPdvX = FloatField()
    dPdvx = dPdvX

    dPdvY = FloatField()
    dPdvy = dPdvY

    dPdvZ = FloatField()
    dPdvz = dPdvZ


class DPdvField(
    Float3CompoundBaseField[DPdvAttrOperator, DPdvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DPdvAttrOperator
    PLUG_CLS = DPdvPlugOperator

    dPdvX = FloatField()
    dPdvx = dPdvX

    dPdvY = FloatField()
    dPdvy = dPdvY

    dPdvZ = FloatField()
    dPdvz = dPdvZ


class DDdxPlugOperator(
    Float3CompoundBasePlugOperator["DDdxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dDdxX", "dDdxx"),
        ("dDdxY", "dDdxy"),
        ("dDdxZ", "dDdxz"),
    )

    dDdxX = FloatField()
    dDdxx = dDdxX

    dDdxY = FloatField()
    dDdxy = dDdxY

    dDdxZ = FloatField()
    dDdxz = dDdxZ


class DDdxAttrOperator(
    Float3CompoundBaseAttrOperator[DDdxPlugOperator]
):
    __slots__ = ()

    dDdxX = FloatField()
    dDdxx = dDdxX

    dDdxY = FloatField()
    dDdxy = dDdxY

    dDdxZ = FloatField()
    dDdxz = dDdxZ


class DDdxField(
    Float3CompoundBaseField[DDdxAttrOperator, DDdxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DDdxAttrOperator
    PLUG_CLS = DDdxPlugOperator

    dDdxX = FloatField()
    dDdxx = dDdxX

    dDdxY = FloatField()
    dDdxy = dDdxY

    dDdxZ = FloatField()
    dDdxz = dDdxZ


class DDdyPlugOperator(
    Float3CompoundBasePlugOperator["DDdyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dDdyX", "dDdyx"),
        ("dDdyY", "dDdyy"),
        ("dDdyZ", "dDdyz"),
    )

    dDdyX = FloatField()
    dDdyx = dDdyX

    dDdyY = FloatField()
    dDdyy = dDdyY

    dDdyZ = FloatField()
    dDdyz = dDdyZ


class DDdyAttrOperator(
    Float3CompoundBaseAttrOperator[DDdyPlugOperator]
):
    __slots__ = ()

    dDdyX = FloatField()
    dDdyx = dDdyX

    dDdyY = FloatField()
    dDdyy = dDdyY

    dDdyZ = FloatField()
    dDdyz = dDdyZ


class DDdyField(
    Float3CompoundBaseField[DDdyAttrOperator, DDdyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DDdyAttrOperator
    PLUG_CLS = DDdyPlugOperator

    dDdyX = FloatField()
    dDdyx = dDdyX

    dDdyY = FloatField()
    dDdyy = dDdyY

    dDdyZ = FloatField()
    dDdyz = dDdyZ


class DNdxPlugOperator(
    Float3CompoundBasePlugOperator["DNdxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dNdxX", "dNdxx"),
        ("dNdxY", "dNdxy"),
        ("dNdxZ", "dNdxz"),
    )

    dNdxX = FloatField()
    dNdxx = dNdxX

    dNdxY = FloatField()
    dNdxy = dNdxY

    dNdxZ = FloatField()
    dNdxz = dNdxZ


class DNdxAttrOperator(
    Float3CompoundBaseAttrOperator[DNdxPlugOperator]
):
    __slots__ = ()

    dNdxX = FloatField()
    dNdxx = dNdxX

    dNdxY = FloatField()
    dNdxy = dNdxY

    dNdxZ = FloatField()
    dNdxz = dNdxZ


class DNdxField(
    Float3CompoundBaseField[DNdxAttrOperator, DNdxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DNdxAttrOperator
    PLUG_CLS = DNdxPlugOperator

    dNdxX = FloatField()
    dNdxx = dNdxX

    dNdxY = FloatField()
    dNdxy = dNdxY

    dNdxZ = FloatField()
    dNdxz = dNdxZ


class DNdyPlugOperator(
    Float3CompoundBasePlugOperator["DNdyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("dNdyX", "dNdyx"),
        ("dNdyY", "dNdyy"),
        ("dNdyZ", "dNdyz"),
    )

    dNdyX = FloatField()
    dNdyx = dNdyX

    dNdyY = FloatField()
    dNdyy = dNdyY

    dNdyZ = FloatField()
    dNdyz = dNdyZ


class DNdyAttrOperator(
    Float3CompoundBaseAttrOperator[DNdyPlugOperator]
):
    __slots__ = ()

    dNdyX = FloatField()
    dNdyx = dNdyX

    dNdyY = FloatField()
    dNdyy = dNdyY

    dNdyZ = FloatField()
    dNdyz = dNdyZ


class DNdyField(
    Float3CompoundBaseField[DNdyAttrOperator, DNdyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DNdyAttrOperator
    PLUG_CLS = DNdyPlugOperator

    dNdyX = FloatField()
    dNdyx = dNdyX

    dNdyY = FloatField()
    dNdyy = dNdyY

    dNdyZ = FloatField()
    dNdyz = dNdyZ
