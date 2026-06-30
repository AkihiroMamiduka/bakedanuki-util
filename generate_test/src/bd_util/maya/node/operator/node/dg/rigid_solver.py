# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.rigid_solver import (
    ConstraintRotateField,
    ConstraintTranslateField,
    GeneralForceField,
    RotateField,
    TranslateField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar.time import TimeField


class SolverMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MIDPOINT = 0
    RUNGE_KUTTA = 1
    RUNGE_KUTTA_ADAPTIVE = 2


class SolverMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MIDPOINT = 0
    RUNGE_KUTTA = 1
    RUNGE_KUTTA_ADAPTIVE = 2

    NAME_MAP = {
        MIDPOINT: "MidPoint",
        RUNGE_KUTTA: "Runge Kutta",
        RUNGE_KUTTA_ADAPTIVE: "Runge Kutta Adaptive",
    }


class SolverMethodEnumField(
    EnumField[SolverMethodEnumAttrOperator, SolverMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverMethodEnumAttrOperator
    PLUG_CLS = SolverMethodEnumPlugOperator


class RigidSolver(DG):
    __slots__ = ()

    NODE_TYPE = "rigidSolver"

    currentTime = TimeField()
    ct = currentTime

    startTime = TimeField()
    stm = startTime

    deltaTime = TimeField()
    dtm = deltaTime

    lastSceneTime = TimeField()
    lst = lastSceneTime

    generalForce = GeneralForceField(multi=True)
    gfr = generalForce

    translate = TranslateField(multi=True)
    t = translate

    rotate = RotateField(multi=True)
    r = rotate

    constraintTranslate = ConstraintTranslateField(multi=True)
    ctr = constraintTranslate

    constraintRotate = ConstraintRotateField(multi=True)
    cr = constraintRotate

    collisionTolerance = DoubleField()
    ctl = collisionTolerance

    stepSize = DoubleField()
    ss = stepSize

    scaleVelocity = DoubleField()
    svv = scaleVelocity

    rigidBodyCount = LongField()
    rbc = rigidBodyCount

    solverMethod = SolverMethodEnumField()
    slm = solverMethod

    friction = BoolField()
    f = friction

    bounciness = BoolField()
    b = bounciness

    dynamics = BoolField()
    dyn = dynamics

    autoSolverTolerances = BoolField()
    ast = autoSolverTolerances

    displayVelocity = BoolField()
    dv = displayVelocity

    displayCenterOfMass = BoolField()
    dcom = displayCenterOfMass

    displayConstraint = BoolField()
    dc = displayConstraint

    displayLabel = BoolField()
    dl = displayLabel

    cacheData = BoolField()
    cd = cacheData

    contactData = BoolField()
    ctd = contactData

    state = BoolField()
    stt = state

    current = BoolField()
    cur = current

    forceDynamics = BoolField()
    fdn = forceDynamics

    allowDisconnection = BoolField()
    ad = allowDisconnection

    solving = BoolField()
    sol = solving

    statistics = BoolField()
    st = statistics
