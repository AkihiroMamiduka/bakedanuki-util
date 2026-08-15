# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.dynamic_constraint import (
    ConnectionDensityRangeField,
    StrengthDropoffField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField


class ConstraintMethodEnumPlugOperator(
    EnumPlugOperator["ConstraintMethodEnumAttrOperator"]
):
    __slots__ = ()

    WELD = 0
    SPRING = 1
    RUBBER_BAND = 2


class ConstraintMethodEnumAttrOperator(
    EnumAttrOperator[ConstraintMethodEnumPlugOperator]
):
    __slots__ = ()

    WELD = 0
    SPRING = 1
    RUBBER_BAND = 2

    NAME_MAP = {
        WELD: "Weld",
        SPRING: "Spring",
        RUBBER_BAND: "Rubber Band",
    }


class ConstraintMethodEnumField(
    EnumField[
        ConstraintMethodEnumAttrOperator, ConstraintMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintMethodEnumAttrOperator
    PLUG_CLS = ConstraintMethodEnumPlugOperator


class ConnectionMethodEnumPlugOperator(
    EnumPlugOperator["ConnectionMethodEnumAttrOperator"]
):
    __slots__ = ()

    COMPONENT_ORDER = 0
    WITHIN_MAX_DISTANCE = 1
    NEAREST_PAIRS = 2


class ConnectionMethodEnumAttrOperator(
    EnumAttrOperator[ConnectionMethodEnumPlugOperator]
):
    __slots__ = ()

    COMPONENT_ORDER = 0
    WITHIN_MAX_DISTANCE = 1
    NEAREST_PAIRS = 2

    NAME_MAP = {
        COMPONENT_ORDER: "Component Order",
        WITHIN_MAX_DISTANCE: "Within Max Distance",
        NEAREST_PAIRS: "Nearest Pairs",
    }


class ConnectionMethodEnumField(
    EnumField[
        ConnectionMethodEnumAttrOperator, ConnectionMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConnectionMethodEnumAttrOperator
    PLUG_CLS = ConnectionMethodEnumPlugOperator


class ConstraintRelationEnumPlugOperator(
    EnumPlugOperator["ConstraintRelationEnumAttrOperator"]
):
    __slots__ = ()

    OBJECT_TO_CONSTRAINT = 0
    OBJECT_TO_OBJECT = 1


class ConstraintRelationEnumAttrOperator(
    EnumAttrOperator[ConstraintRelationEnumPlugOperator]
):
    __slots__ = ()

    OBJECT_TO_CONSTRAINT = 0
    OBJECT_TO_OBJECT = 1

    NAME_MAP = {
        OBJECT_TO_CONSTRAINT: "Object to Constraint",
        OBJECT_TO_OBJECT: "Object to Object",
    }


class ConstraintRelationEnumField(
    EnumField[
        ConstraintRelationEnumAttrOperator, ConstraintRelationEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRelationEnumAttrOperator
    PLUG_CLS = ConstraintRelationEnumPlugOperator


class ComponentRelationEnumPlugOperator(
    EnumPlugOperator["ComponentRelationEnumAttrOperator"]
):
    __slots__ = ()

    ALL_TO_FIRST = 0
    ALL_TO_ALL = 1
    CHAIN = 2


class ComponentRelationEnumAttrOperator(
    EnumAttrOperator[ComponentRelationEnumPlugOperator]
):
    __slots__ = ()

    ALL_TO_FIRST = 0
    ALL_TO_ALL = 1
    CHAIN = 2

    NAME_MAP = {
        ALL_TO_FIRST: "All to First",
        ALL_TO_ALL: "All to All",
        CHAIN: "Chain",
    }


class ComponentRelationEnumField(
    EnumField[
        ComponentRelationEnumAttrOperator, ComponentRelationEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ComponentRelationEnumAttrOperator
    PLUG_CLS = ComponentRelationEnumPlugOperator


class ConnectionUpdateEnumPlugOperator(
    EnumPlugOperator["ConnectionUpdateEnumAttrOperator"]
):
    __slots__ = ()

    AT_START = 0
    PER_FRAME = 1


class ConnectionUpdateEnumAttrOperator(
    EnumAttrOperator[ConnectionUpdateEnumPlugOperator]
):
    __slots__ = ()

    AT_START = 0
    PER_FRAME = 1

    NAME_MAP = {
        AT_START: "At Start",
        PER_FRAME: "Per Frame",
    }


class ConnectionUpdateEnumField(
    EnumField[
        ConnectionUpdateEnumAttrOperator, ConnectionUpdateEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ConnectionUpdateEnumAttrOperator
    PLUG_CLS = ConnectionUpdateEnumPlugOperator


class RestLengthMethodEnumPlugOperator(
    EnumPlugOperator["RestLengthMethodEnumAttrOperator"]
):
    __slots__ = ()

    FROM_START_DISTANCE = 0
    CONSTANT = 1


class RestLengthMethodEnumAttrOperator(
    EnumAttrOperator[RestLengthMethodEnumPlugOperator]
):
    __slots__ = ()

    FROM_START_DISTANCE = 0
    CONSTANT = 1

    NAME_MAP = {
        FROM_START_DISTANCE: "From Start Distance",
        CONSTANT: "Constant",
    }


class RestLengthMethodEnumField(
    EnumField[
        RestLengthMethodEnumAttrOperator, RestLengthMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = RestLengthMethodEnumAttrOperator
    PLUG_CLS = RestLengthMethodEnumPlugOperator


class GeneratedDynamicConstraint(Shape):
    __slots__ = ()

    NODE_TYPE = "dynamicConstraint"

    isDynamic = BoolField(default_value=True)
    isd = isDynamic

    enable = BoolField(default_value=True)
    ena = enable

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    componentIds = TypedField(multi=True)
    cid = componentIds

    constraintMethod = ConstraintMethodEnumField(default_value=1)
    cm = constraintMethod

    connectionMethod = ConnectionMethodEnumField(default_value=0)
    cnm = connectionMethod

    constraintRelation = ConstraintRelationEnumField(default_value=1)
    crr = constraintRelation

    componentRelation = ComponentRelationEnumField(default_value=0)
    cmr = componentRelation

    connectionUpdate = ConnectionUpdateEnumField(default_value=0)
    cu = connectionUpdate

    connectWithinComponent = BoolField(default_value=False)
    cwc = connectWithinComponent

    connectionDensity = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    cdn = connectionDensity

    connectionDensityRange = ConnectionDensityRangeField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    cdnr = connectionDensityRange

    displayConnections = BoolField(default_value=True)
    dcn = displayConnections

    strength = DoubleField(
        default_value=20.0, soft_min_value=0.0, soft_max_value=200.0
    )
    str = strength

    restLengthMethod = RestLengthMethodEnumField(default_value=0)
    rlm = restLengthMethod

    restLength = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    rl = restLength

    restLengthScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    rls = restLengthScale

    tangentStrength = DoubleField(
        default_value=10.0, soft_min_value=0.0, soft_max_value=200.0
    )
    tst = tangentStrength

    bend = BoolField(default_value=False)
    bnd = bend

    bendStrength = DoubleField(
        default_value=20.0, soft_min_value=0.0, soft_max_value=200.0
    )
    bns = bendStrength

    bendBreakAngle = DoubleField(
        default_value=360.0, soft_min_value=0.0, soft_max_value=360.0
    )
    bba = bendBreakAngle

    glueStrength = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    gls = glueStrength

    glueStrengthScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    glss = glueStrengthScale

    force = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    for_ = force

    motionDrag = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    mdg = motionDrag

    dropoff = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    drp = dropoff

    dropoffDistance = DoubleField(
        default_value=50.0, soft_min_value=0.0, soft_max_value=100.0
    )
    ddd = dropoffDistance

    strengthDropoff = StrengthDropoffField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    sdp = strengthDropoff

    maxDistance = DoubleField(
        default_value=0.1, soft_min_value=0.0, soft_max_value=1.0
    )
    mds = maxDistance

    damp = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dmp = damp

    friction = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    frc = friction

    localCollide = BoolField(default_value=False)
    lcl = localCollide

    collideWidthScale = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    cws = collideWidthScale

    excludeCollisions = BoolField(default_value=False)
    excs = excludeCollisions

    singleSided = BoolField(default_value=True)
    ssd = singleSided

    maxIterations = LongField(
        default_value=5000, soft_min_value=0, soft_max_value=10000
    )
    mitr = maxIterations

    minIterations = LongField(
        default_value=0, soft_min_value=0, soft_max_value=100
    )
    mini = minIterations

    evalStart = TypedField(multi=True, writable=False)
    evs = evalStart

    evalCurrent = TypedField(multi=True, writable=False)
    evc = evalCurrent

    iterations = LongField(default_value=20)
    itr = iterations

    collide = BoolField(default_value=True)
    cld = collide
