# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class ForceActorSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ForceActorSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ForceActorSpaceEnumField(
    EnumField[ForceActorSpaceEnumAttrOperator, ForceActorSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceActorSpaceEnumAttrOperator
    PLUG_CLS = ForceActorSpaceEnumPlugOperator


class ScaleCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class ScaleCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class ScaleCompensationModeEnumField(
    EnumField[ScaleCompensationModeEnumAttrOperator, ScaleCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleCompensationModeEnumAttrOperator
    PLUG_CLS = ScaleCompensationModeEnumPlugOperator


class MassCenterCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class MassCenterCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class MassCenterCompensationModeEnumField(
    EnumField[MassCenterCompensationModeEnumAttrOperator, MassCenterCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassCenterCompensationModeEnumAttrOperator
    PLUG_CLS = MassCenterCompensationModeEnumPlugOperator


class AnkleHeightCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class AnkleHeightCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class AnkleHeightCompensationModeEnumField(
    EnumField[AnkleHeightCompensationModeEnumAttrOperator, AnkleHeightCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnkleHeightCompensationModeEnumAttrOperator
    PLUG_CLS = AnkleHeightCompensationModeEnumPlugOperator


class AnkleProximityCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class AnkleProximityCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class AnkleProximityCompensationModeEnumField(
    EnumField[AnkleProximityCompensationModeEnumAttrOperator, AnkleProximityCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnkleProximityCompensationModeEnumAttrOperator
    PLUG_CLS = AnkleProximityCompensationModeEnumPlugOperator


class HipsHeightCompensationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2


class HipsHeightCompensationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AUTO = 1
    USER = 2

    NAME_MAP = {
        OFF: "Off",
        AUTO: "Auto",
        USER: "User",
    }


class HipsHeightCompensationModeEnumField(
    EnumField[HipsHeightCompensationModeEnumAttrOperator, HipsHeightCompensationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsHeightCompensationModeEnumAttrOperator
    PLUG_CLS = HipsHeightCompensationModeEnumPlugOperator


class FloorContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FloorContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FloorContactEnumField(
    EnumField[FloorContactEnumAttrOperator, FloorContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorContactEnumAttrOperator
    PLUG_CLS = FloorContactEnumPlugOperator


class HandFloorContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class HandFloorContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class HandFloorContactEnumField(
    EnumField[HandFloorContactEnumAttrOperator, HandFloorContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFloorContactEnumAttrOperator
    PLUG_CLS = HandFloorContactEnumPlugOperator


class HandContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGERBASE = 2
    HOOF = 3


class HandContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    WRIST = 1
    FINGERBASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "Normal",
        WRIST: "Wrist",
        FINGERBASE: "FingerBase",
        HOOF: "Hoof",
    }


class HandContactTypeEnumField(
    EnumField[HandContactTypeEnumAttrOperator, HandContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandContactTypeEnumAttrOperator
    PLUG_CLS = HandContactTypeEnumPlugOperator


class HandFingerContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class HandFingerContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class HandFingerContactEnumField(
    EnumField[HandFingerContactEnumAttrOperator, HandFingerContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFingerContactEnumAttrOperator
    PLUG_CLS = HandFingerContactEnumPlugOperator


class HandFingerContactModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2


class HandFingerContactModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2

    NAME_MAP = {
        STICKY: "Sticky",
        SPREAD: "Spread",
        STICKY_AMP_SPREAD: "Sticky & Spread",
    }


class HandFingerContactModeEnumField(
    EnumField[HandFingerContactModeEnumAttrOperator, HandFingerContactModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFingerContactModeEnumAttrOperator
    PLUG_CLS = HandFingerContactModeEnumPlugOperator


class FootContactTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOEBASE = 2
    HOOF = 3


class FootContactTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 0
    ANKLE = 1
    TOEBASE = 2
    HOOF = 3

    NAME_MAP = {
        NORMAL: "Normal",
        ANKLE: "Ankle",
        TOEBASE: "ToeBase",
        HOOF: "Hoof",
    }


class FootContactTypeEnumField(
    EnumField[FootContactTypeEnumAttrOperator, FootContactTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootContactTypeEnumAttrOperator
    PLUG_CLS = FootContactTypeEnumPlugOperator


class FootFingerContactEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FootFingerContactEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FootFingerContactEnumField(
    EnumField[FootFingerContactEnumAttrOperator, FootFingerContactEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootFingerContactEnumAttrOperator
    PLUG_CLS = FootFingerContactEnumPlugOperator


class FootFingerContactModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2


class FootFingerContactModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STICKY = 0
    SPREAD = 1
    STICKY_AMP_SPREAD = 2

    NAME_MAP = {
        STICKY: "Sticky",
        SPREAD: "Spread",
        STICKY_AMP_SPREAD: "Sticky & Spread",
    }


class FootFingerContactModeEnumField(
    EnumField[FootFingerContactModeEnumAttrOperator, FootFingerContactModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FootFingerContactModeEnumAttrOperator
    PLUG_CLS = FootFingerContactModeEnumPlugOperator


class LeftUpLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftUpLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftUpLegRollModeEnumField(
    EnumField[LeftUpLegRollModeEnumAttrOperator, LeftUpLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftUpLegRollModeEnumAttrOperator
    PLUG_CLS = LeftUpLegRollModeEnumPlugOperator


class LeftLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftLegRollModeEnumField(
    EnumField[LeftLegRollModeEnumAttrOperator, LeftLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegRollModeEnumAttrOperator
    PLUG_CLS = LeftLegRollModeEnumPlugOperator


class RightUpLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightUpLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightUpLegRollModeEnumField(
    EnumField[RightUpLegRollModeEnumAttrOperator, RightUpLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightUpLegRollModeEnumAttrOperator
    PLUG_CLS = RightUpLegRollModeEnumPlugOperator


class RightLegRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightLegRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightLegRollModeEnumField(
    EnumField[RightLegRollModeEnumAttrOperator, RightLegRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegRollModeEnumAttrOperator
    PLUG_CLS = RightLegRollModeEnumPlugOperator


class LeftArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftArmRollModeEnumField(
    EnumField[LeftArmRollModeEnumAttrOperator, LeftArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmRollModeEnumAttrOperator
    PLUG_CLS = LeftArmRollModeEnumPlugOperator


class LeftForeArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftForeArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftForeArmRollModeEnumField(
    EnumField[LeftForeArmRollModeEnumAttrOperator, LeftForeArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftForeArmRollModeEnumAttrOperator
    PLUG_CLS = LeftForeArmRollModeEnumPlugOperator


class RightArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightArmRollModeEnumField(
    EnumField[RightArmRollModeEnumAttrOperator, RightArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmRollModeEnumAttrOperator
    PLUG_CLS = RightArmRollModeEnumPlugOperator


class RightForeArmRollModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightForeArmRollModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightForeArmRollModeEnumField(
    EnumField[RightForeArmRollModeEnumAttrOperator, RightForeArmRollModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightForeArmRollModeEnumAttrOperator
    PLUG_CLS = RightForeArmRollModeEnumPlugOperator


class MirrorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class MirrorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class MirrorEnumField(
    EnumField[MirrorEnumAttrOperator, MirrorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorEnumAttrOperator
    PLUG_CLS = MirrorEnumPlugOperator


class LeftKneeKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftKneeKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftKneeKillPitchEnumField(
    EnumField[LeftKneeKillPitchEnumAttrOperator, LeftKneeKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftKneeKillPitchEnumAttrOperator
    PLUG_CLS = LeftKneeKillPitchEnumPlugOperator


class RightKneeKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightKneeKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightKneeKillPitchEnumField(
    EnumField[RightKneeKillPitchEnumAttrOperator, RightKneeKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightKneeKillPitchEnumAttrOperator
    PLUG_CLS = RightKneeKillPitchEnumPlugOperator


class LeftElbowKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftElbowKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftElbowKillPitchEnumField(
    EnumField[LeftElbowKillPitchEnumAttrOperator, LeftElbowKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftElbowKillPitchEnumAttrOperator
    PLUG_CLS = LeftElbowKillPitchEnumPlugOperator


class RightElbowKillPitchEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightElbowKillPitchEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightElbowKillPitchEnumField(
    EnumField[RightElbowKillPitchEnumAttrOperator, RightElbowKillPitchEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightElbowKillPitchEnumAttrOperator
    PLUG_CLS = RightElbowKillPitchEnumPlugOperator


class AutomaticToesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class AutomaticToesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class AutomaticToesEnumField(
    EnumField[AutomaticToesEnumAttrOperator, AutomaticToesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AutomaticToesEnumAttrOperator
    PLUG_CLS = AutomaticToesEnumPlugOperator


class FloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2


class FloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    ANKLE = 1
    TOES = 2

    NAME_MAP = {
        AUTO: "Auto",
        ANKLE: "Ankle",
        TOES: "Toes",
    }


class FloorPivotEnumField(
    EnumField[FloorPivotEnumAttrOperator, FloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloorPivotEnumAttrOperator
    PLUG_CLS = FloorPivotEnumPlugOperator


class PostureEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1


class PostureEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BIPED = 0
    QUADRUPED = 1

    NAME_MAP = {
        BIPED: "Biped",
        QUADRUPED: "Quadruped",
    }


class PostureEnumField(
    EnumField[PostureEnumAttrOperator, PostureEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostureEnumAttrOperator
    PLUG_CLS = PostureEnumPlugOperator


class AutomaticFingersEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class AutomaticFingersEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class AutomaticFingersEnumField(
    EnumField[AutomaticFingersEnumAttrOperator, AutomaticFingersEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AutomaticFingersEnumAttrOperator
    PLUG_CLS = AutomaticFingersEnumPlugOperator


class HandFloorPivotEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2


class HandFloorPivotEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTO = 0
    WRIST = 1
    FINGERS = 2

    NAME_MAP = {
        AUTO: "Auto",
        WRIST: "Wrist",
        FINGERS: "Fingers",
    }


class HandFloorPivotEnumField(
    EnumField[HandFloorPivotEnumAttrOperator, HandFloorPivotEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HandFloorPivotEnumAttrOperator
    PLUG_CLS = HandFloorPivotEnumPlugOperator


class HipsTranslationModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1
    TRAJECTORY = 2


class HipsTranslationModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD_RIGID = 0
    BODY_RIGID = 1
    TRAJECTORY = 2

    NAME_MAP = {
        WORLD_RIGID: "World Rigid",
        BODY_RIGID: "Body Rigid",
        TRAJECTORY: "Trajectory",
    }


class HipsTranslationModeEnumField(
    EnumField[HipsTranslationModeEnumAttrOperator, HipsTranslationModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsTranslationModeEnumAttrOperator
    PLUG_CLS = HipsTranslationModeEnumPlugOperator


class FingerSolvingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FingerSolvingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FingerSolvingEnumField(
    EnumField[FingerSolvingEnumAttrOperator, FingerSolvingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerSolvingEnumAttrOperator
    PLUG_CLS = FingerSolvingEnumPlugOperator


class RollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1


class RollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RELATIVE = 0
    ABSOLUTE = 1

    NAME_MAP = {
        RELATIVE: "Relative",
        ABSOLUTE: "Absolute",
    }


class RollExtractionModeEnumField(
    EnumField[RollExtractionModeEnumAttrOperator, RollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RollExtractionModeEnumAttrOperator
    PLUG_CLS = RollExtractionModeEnumPlugOperator


class FingerPropagationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class FingerPropagationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class FingerPropagationEnumField(
    EnumField[FingerPropagationEnumAttrOperator, FingerPropagationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FingerPropagationEnumAttrOperator
    PLUG_CLS = FingerPropagationEnumPlugOperator


class SnSSmoothReachEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class SnSSmoothReachEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class SnSSmoothReachEnumField(
    EnumField[SnSSmoothReachEnumAttrOperator, SnSSmoothReachEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SnSSmoothReachEnumAttrOperator
    PLUG_CLS = SnSSmoothReachEnumPlugOperator


class LockXEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockXEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockXEnumField(
    EnumField[LockXEnumAttrOperator, LockXEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockXEnumAttrOperator
    PLUG_CLS = LockXEnumPlugOperator


class LockYEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockYEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockYEnumField(
    EnumField[LockYEnumAttrOperator, LockYEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockYEnumAttrOperator
    PLUG_CLS = LockYEnumPlugOperator


class LockZEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LockZEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LockZEnumField(
    EnumField[LockZEnumAttrOperator, LockZEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LockZEnumAttrOperator
    PLUG_CLS = LockZEnumPlugOperator


class ParamRealisticArmSolvingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamRealisticArmSolvingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamRealisticArmSolvingEnumField(
    EnumField[ParamRealisticArmSolvingEnumAttrOperator, ParamRealisticArmSolvingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamRealisticArmSolvingEnumAttrOperator
    PLUG_CLS = ParamRealisticArmSolvingEnumPlugOperator


class ParamLeafLeftUpLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll1ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll1ModeEnumAttrOperator, ParamLeafLeftUpLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll1ModeEnumPlugOperator


class ParamLeafLeftLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll1ModeEnumField(
    EnumField[ParamLeafLeftLegRoll1ModeEnumAttrOperator, ParamLeafLeftLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll1ModeEnumPlugOperator


class ParamLeafRightUpLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll1ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll1ModeEnumAttrOperator, ParamLeafRightUpLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll1ModeEnumPlugOperator


class ParamLeafRightLegRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll1ModeEnumField(
    EnumField[ParamLeafRightLegRoll1ModeEnumAttrOperator, ParamLeafRightLegRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll1ModeEnumPlugOperator


class ParamLeafLeftArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll1ModeEnumField(
    EnumField[ParamLeafLeftArmRoll1ModeEnumAttrOperator, ParamLeafLeftArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll1ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll1ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll1ModeEnumAttrOperator, ParamLeafLeftForeArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll1ModeEnumPlugOperator


class ParamLeafRightArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll1ModeEnumField(
    EnumField[ParamLeafRightArmRoll1ModeEnumAttrOperator, ParamLeafRightArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll1ModeEnumPlugOperator


class ParamLeafRightForeArmRoll1ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll1ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll1ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll1ModeEnumAttrOperator, ParamLeafRightForeArmRoll1ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll1ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll1ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll2ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll2ModeEnumAttrOperator, ParamLeafLeftUpLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll2ModeEnumPlugOperator


class ParamLeafLeftLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll2ModeEnumField(
    EnumField[ParamLeafLeftLegRoll2ModeEnumAttrOperator, ParamLeafLeftLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll2ModeEnumPlugOperator


class ParamLeafRightUpLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll2ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll2ModeEnumAttrOperator, ParamLeafRightUpLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll2ModeEnumPlugOperator


class ParamLeafRightLegRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll2ModeEnumField(
    EnumField[ParamLeafRightLegRoll2ModeEnumAttrOperator, ParamLeafRightLegRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll2ModeEnumPlugOperator


class ParamLeafLeftArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll2ModeEnumField(
    EnumField[ParamLeafLeftArmRoll2ModeEnumAttrOperator, ParamLeafLeftArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll2ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll2ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll2ModeEnumAttrOperator, ParamLeafLeftForeArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll2ModeEnumPlugOperator


class ParamLeafRightArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll2ModeEnumField(
    EnumField[ParamLeafRightArmRoll2ModeEnumAttrOperator, ParamLeafRightArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll2ModeEnumPlugOperator


class ParamLeafRightForeArmRoll2ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll2ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll2ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll2ModeEnumAttrOperator, ParamLeafRightForeArmRoll2ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll2ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll2ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll3ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll3ModeEnumAttrOperator, ParamLeafLeftUpLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll3ModeEnumPlugOperator


class ParamLeafLeftLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll3ModeEnumField(
    EnumField[ParamLeafLeftLegRoll3ModeEnumAttrOperator, ParamLeafLeftLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll3ModeEnumPlugOperator


class ParamLeafRightUpLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll3ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll3ModeEnumAttrOperator, ParamLeafRightUpLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll3ModeEnumPlugOperator


class ParamLeafRightLegRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll3ModeEnumField(
    EnumField[ParamLeafRightLegRoll3ModeEnumAttrOperator, ParamLeafRightLegRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll3ModeEnumPlugOperator


class ParamLeafLeftArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll3ModeEnumField(
    EnumField[ParamLeafLeftArmRoll3ModeEnumAttrOperator, ParamLeafLeftArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll3ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll3ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll3ModeEnumAttrOperator, ParamLeafLeftForeArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll3ModeEnumPlugOperator


class ParamLeafRightArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll3ModeEnumField(
    EnumField[ParamLeafRightArmRoll3ModeEnumAttrOperator, ParamLeafRightArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll3ModeEnumPlugOperator


class ParamLeafRightForeArmRoll3ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll3ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll3ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll3ModeEnumAttrOperator, ParamLeafRightForeArmRoll3ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll3ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll3ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll4ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll4ModeEnumAttrOperator, ParamLeafLeftUpLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll4ModeEnumPlugOperator


class ParamLeafLeftLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll4ModeEnumField(
    EnumField[ParamLeafLeftLegRoll4ModeEnumAttrOperator, ParamLeafLeftLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll4ModeEnumPlugOperator


class ParamLeafRightUpLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll4ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll4ModeEnumAttrOperator, ParamLeafRightUpLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll4ModeEnumPlugOperator


class ParamLeafRightLegRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll4ModeEnumField(
    EnumField[ParamLeafRightLegRoll4ModeEnumAttrOperator, ParamLeafRightLegRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll4ModeEnumPlugOperator


class ParamLeafLeftArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll4ModeEnumField(
    EnumField[ParamLeafLeftArmRoll4ModeEnumAttrOperator, ParamLeafLeftArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll4ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll4ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll4ModeEnumAttrOperator, ParamLeafLeftForeArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll4ModeEnumPlugOperator


class ParamLeafRightArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll4ModeEnumField(
    EnumField[ParamLeafRightArmRoll4ModeEnumAttrOperator, ParamLeafRightArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll4ModeEnumPlugOperator


class ParamLeafRightForeArmRoll4ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll4ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll4ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll4ModeEnumAttrOperator, ParamLeafRightForeArmRoll4ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll4ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll4ModeEnumPlugOperator


class ParamLeafLeftUpLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftUpLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftUpLegRoll5ModeEnumField(
    EnumField[ParamLeafLeftUpLegRoll5ModeEnumAttrOperator, ParamLeafLeftUpLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftUpLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftUpLegRoll5ModeEnumPlugOperator


class ParamLeafLeftLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftLegRoll5ModeEnumField(
    EnumField[ParamLeafLeftLegRoll5ModeEnumAttrOperator, ParamLeafLeftLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftLegRoll5ModeEnumPlugOperator


class ParamLeafRightUpLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightUpLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightUpLegRoll5ModeEnumField(
    EnumField[ParamLeafRightUpLegRoll5ModeEnumAttrOperator, ParamLeafRightUpLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightUpLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightUpLegRoll5ModeEnumPlugOperator


class ParamLeafRightLegRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightLegRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightLegRoll5ModeEnumField(
    EnumField[ParamLeafRightLegRoll5ModeEnumAttrOperator, ParamLeafRightLegRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightLegRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightLegRoll5ModeEnumPlugOperator


class ParamLeafLeftArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftArmRoll5ModeEnumField(
    EnumField[ParamLeafLeftArmRoll5ModeEnumAttrOperator, ParamLeafLeftArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftArmRoll5ModeEnumPlugOperator


class ParamLeafLeftForeArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafLeftForeArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafLeftForeArmRoll5ModeEnumField(
    EnumField[ParamLeafLeftForeArmRoll5ModeEnumAttrOperator, ParamLeafLeftForeArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafLeftForeArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafLeftForeArmRoll5ModeEnumPlugOperator


class ParamLeafRightArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightArmRoll5ModeEnumField(
    EnumField[ParamLeafRightArmRoll5ModeEnumAttrOperator, ParamLeafRightArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightArmRoll5ModeEnumPlugOperator


class ParamLeafRightForeArmRoll5ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class ParamLeafRightForeArmRoll5ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class ParamLeafRightForeArmRoll5ModeEnumField(
    EnumField[ParamLeafRightForeArmRoll5ModeEnumAttrOperator, ParamLeafRightForeArmRoll5ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParamLeafRightForeArmRoll5ModeEnumAttrOperator
    PLUG_CLS = ParamLeafRightForeArmRoll5ModeEnumPlugOperator


class LeftLegFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftLegFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftLegFullRollExtractionModeEnumField(
    EnumField[LeftLegFullRollExtractionModeEnumAttrOperator, LeftLegFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftLegFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = LeftLegFullRollExtractionModeEnumPlugOperator


class RightLegFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightLegFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightLegFullRollExtractionModeEnumField(
    EnumField[RightLegFullRollExtractionModeEnumAttrOperator, RightLegFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightLegFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = RightLegFullRollExtractionModeEnumPlugOperator


class LeftArmFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class LeftArmFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class LeftArmFullRollExtractionModeEnumField(
    EnumField[LeftArmFullRollExtractionModeEnumAttrOperator, LeftArmFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LeftArmFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = LeftArmFullRollExtractionModeEnumPlugOperator


class RightArmFullRollExtractionModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ON = 1


class RightArmFullRollExtractionModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    ON = 1

    NAME_MAP = {
        OFF: "Off",
        ON: "On",
    }


class RightArmFullRollExtractionModeEnumField(
    EnumField[RightArmFullRollExtractionModeEnumAttrOperator, RightArmFullRollExtractionModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RightArmFullRollExtractionModeEnumAttrOperator
    PLUG_CLS = RightArmFullRollExtractionModeEnumPlugOperator


class HIKProperty2State(DG):
    __slots__ = ()

    NODE_TYPE = "HIKProperty2State"

    OutputPropertySetState = TypedField()

    rigAlign = BoolField()
    ra = rigAlign

    leftHipRoll = FloatField()
    lhr = leftHipRoll

    leftKneeRoll = FloatField()
    lkr = leftKneeRoll

    rightHipRoll = FloatField()
    rhr = rightHipRoll

    rightKneeRoll = FloatField()
    rkr = rightKneeRoll

    leftShoulderRoll = FloatField()
    lsr = leftShoulderRoll

    leftElbowRoll = FloatField()
    ler = leftElbowRoll

    rightShoulderRoll = FloatField()
    rsr = rightShoulderRoll

    rightElbowRoll = FloatField()
    rer = rightElbowRoll

    ForceActorSpace = ForceActorSpaceEnumField()

    ScaleCompensationMode = ScaleCompensationModeEnumField()

    ScaleCompensation = DoubleField()

    MassCenterCompensationMode = MassCenterCompensationModeEnumField()

    MassCenterCompensation = DoubleField()

    AnkleHeightCompensationMode = AnkleHeightCompensationModeEnumField()

    AnkleHeightCompensation = DoubleField()

    AnkleProximityCompensationMode = AnkleProximityCompensationModeEnumField()

    AnkleProximityCompensation = DoubleField()

    HipsHeightCompensationMode = HipsHeightCompensationModeEnumField()

    HipsHeightCompensation = DoubleField()

    ReachActorLeftAnkle = DoubleField()

    ReachActorRightAnkle = DoubleField()

    ReachActorChest = DoubleField()

    ReachActorLeftWrist = DoubleField()

    ReachActorRightWrist = DoubleField()

    ReachActorLeftKnee = DoubleField()

    ReachActorRightKnee = DoubleField()

    ReachActorHead = DoubleField()

    ReachActorLeftElbow = DoubleField()

    ReachActorRightElbow = DoubleField()

    ReachActorLeftAnkleRotationRotation = DoubleField()

    ReachActorRightAnkleRotation = DoubleField()

    ReachActorHeadRotation = DoubleField()

    ReachActorLeftWristRotation = DoubleField()

    ReachActorRightWristRotation = DoubleField()

    ReachActorLeftFingerBase = DoubleField()

    ReachActorRightFingerBase = DoubleField()

    ReachActorLeftToesBase = DoubleField()

    ReachActorRightToesBase = DoubleField()

    ReachActorLeftFingerBaseRotation = DoubleField()

    ReachActorRightFingerBaseRotation = DoubleField()

    ReachActorLeftToesBaseRotation = DoubleField()

    ReachActorRightToesBaseRotation = DoubleField()

    ReachActorChestRotation = DoubleField()

    ReachActorLowerChestRotation = DoubleField()

    ReachActorLeftHandThumb = DoubleField()

    ReachActorLeftHandIndex = DoubleField()

    ReachActorLeftHandMiddle = DoubleField()

    ReachActorLeftHandRing = DoubleField()

    ReachActorLeftHandPinky = DoubleField()

    ReachActorLeftHandExtraFinger = DoubleField()

    ReachActorRightHandThumb = DoubleField()

    ReachActorRightHandIndex = DoubleField()

    ReachActorRightHandMiddle = DoubleField()

    ReachActorRightHandRing = DoubleField()

    ReachActorRightHandPinky = DoubleField()

    ReachActorRightHandExtraFinger = DoubleField()

    ReachActorLeftFootThumb = DoubleField()

    ReachActorLeftFootIndex = DoubleField()

    ReachActorLeftFootMiddle = DoubleField()

    ReachActorLeftFootRing = DoubleField()

    ReachActorLeftFootPinky = DoubleField()

    ReachActorLeftFootExtraFinger = DoubleField()

    ReachActorRightFootThumb = DoubleField()

    ReachActorRightFootIndex = DoubleField()

    ReachActorRightFootMiddle = DoubleField()

    ReachActorRightFootRing = DoubleField()

    ReachActorRightFootPinky = DoubleField()

    ReachActorRightFootExtraFinger = DoubleField()

    FloorContact = FloorContactEnumField()

    FootBottomToAnkle = DoubleField()

    FootBackToAnkle = DoubleField()

    FootMiddleToAnkle = DoubleField()

    FootFrontToMiddle = DoubleField()

    FootInToAnkle = DoubleField()

    FootOutToAnkle = DoubleField()

    HandFloorContact = HandFloorContactEnumField()

    HandBottomToWrist = DoubleField()

    HandBackToWrist = DoubleField()

    HandMiddleToWrist = DoubleField()

    HandFrontToMiddle = DoubleField()

    HandInToWrist = DoubleField()

    HandOutToWrist = DoubleField()

    HandContactType = HandContactTypeEnumField()

    HandFingerContact = HandFingerContactEnumField()

    HandFingerContactMode = HandFingerContactModeEnumField()

    FootContactType = FootContactTypeEnumField()

    FootFingerContact = FootFingerContactEnumField()

    FootFingerContactMode = FootFingerContactModeEnumField()

    LeftUpLegRollMode = LeftUpLegRollModeEnumField()

    LeftUpLegRoll = DoubleField()

    LeftLegRollMode = LeftLegRollModeEnumField()

    LeftLegRoll = DoubleField()

    RightUpLegRollMode = RightUpLegRollModeEnumField()

    RightUpLegRoll = DoubleField()

    RightLegRollMode = RightLegRollModeEnumField()

    RightLegRoll = DoubleField()

    LeftArmRollMode = LeftArmRollModeEnumField()

    LeftArmRoll = DoubleField()

    LeftForeArmRollMode = LeftForeArmRollModeEnumField()

    LeftForeArmRoll = DoubleField()

    RightArmRollMode = RightArmRollModeEnumField()

    RightArmRoll = DoubleField()

    RightForeArmRollMode = RightForeArmRollModeEnumField()

    RightForeArmRoll = DoubleField()

    Mirror = MirrorEnumField()

    LeftKneeKillPitch = LeftKneeKillPitchEnumField()

    RightKneeKillPitch = RightKneeKillPitchEnumField()

    LeftElbowKillPitch = LeftElbowKillPitchEnumField()

    RightElbowKillPitch = RightElbowKillPitchEnumField()

    CtrlPullLeftFoot = DoubleField()

    CtrlPullRightFoot = DoubleField()

    CtrlPullLeftHand = DoubleField()

    CtrlPullRightHand = DoubleField()

    CtrlPullHead = DoubleField()

    CtrlPullLeftToeBase = DoubleField()

    CtrlPullLeftKnee = DoubleField()

    CtrlPullRightToeBase = DoubleField()

    CtrlPullRightKnee = DoubleField()

    CtrlPullLeftFingerBase = DoubleField()

    CtrlPullLeftElbow = DoubleField()

    CtrlPullRightFingerBase = DoubleField()

    CtrlPullRightElbow = DoubleField()

    CtrlChestPullLeftHand = DoubleField()

    CtrlChestPullRightHand = DoubleField()

    CtrlResistHipsPosition = DoubleField()

    CtrlEnforceGravity = DoubleField()

    CtrlResistHipsOrientation = DoubleField()

    CtrlResistChestPosition = DoubleField()

    CtrlResistChestOrientation = DoubleField()

    CtrlResistLeftCollar = DoubleField()

    CtrlResistRightCollar = DoubleField()

    CtrlResistLeftKnee = DoubleField()

    CtrlResistRightKnee = DoubleField()

    CtrlResistLeftElbow = DoubleField()

    CtrlResistRightElbow = DoubleField()

    ParamCtrlSpineStiffness = DoubleField()

    HipsTOffsetX = DoubleField()

    HipsTOffsetY = DoubleField()

    HipsTOffsetZ = DoubleField()

    ChestTOffsetX = DoubleField()

    ChestTOffsetY = DoubleField()

    ChestTOffsetZ = DoubleField()

    AutomaticToes = AutomaticToesEnumField()

    FloorPivot = FloorPivotEnumField()

    Posture = PostureEnumField()

    AutomaticFingers = AutomaticFingersEnumField()

    HandFloorPivot = HandFloorPivotEnumField()

    ParamCtrlNeckStiffness = DoubleField()

    HipsTranslationMode = HipsTranslationModeEnumField()

    FingerSolving = FingerSolvingEnumField()

    ParamFootContactStiffness = DoubleField()

    CtrlResistMaximumExtensionLeftKnee = DoubleField()

    CtrlResistMaximumExtensionRightKnee = DoubleField()

    CtrlResistMaximumExtensionLeftElbow = DoubleField()

    CtrlResistMaximumExtensionRightElbow = DoubleField()

    CtrlResistCompressionFactorLeftKnee = DoubleField()

    CtrlResistCompressionFactorRightKnee = DoubleField()

    CtrlResistCompressionFactorLeftElbow = DoubleField()

    CtrlResistCompressionFactorRightElbow = DoubleField()

    ParamHandFingerContactRollStiffness = DoubleField()

    ParamFootFingerContactRollStiffness = DoubleField()

    ParamHandContactStiffness = DoubleField()

    RollExtractionMode = RollExtractionModeEnumField()

    PullIterationCount = DoubleField()

    LeftHandThumbTip = DoubleField()

    LeftHandIndexTip = DoubleField()

    LeftHandMiddleTip = DoubleField()

    LeftHandRingTip = DoubleField()

    LeftHandPinkyTip = DoubleField()

    LeftHandExtraFingerTip = DoubleField()

    RightHandThumbTip = DoubleField()

    RightHandIndexTip = DoubleField()

    RightHandMiddleTip = DoubleField()

    RightHandRingTip = DoubleField()

    RightHandPinkyTip = DoubleField()

    RightHandExtraFingerTip = DoubleField()

    LeftFootThumbTip = DoubleField()

    LeftFootIndexTip = DoubleField()

    LeftFootMiddleTip = DoubleField()

    LeftFootRingTip = DoubleField()

    LeftFootPinkyTip = DoubleField()

    LeftFootExtraFingerTip = DoubleField()

    RightFootThumbTip = DoubleField()

    RightFootIndexTip = DoubleField()

    RightFootMiddleTip = DoubleField()

    RightFootRingTip = DoubleField()

    RightFootPinkyTip = DoubleField()

    RightFootExtraFingerTip = DoubleField()

    ShoulderCorrection = DoubleField()

    LeftLegMaxExtensionAngle = DoubleField()

    RightLegMaxExtensionAngle = DoubleField()

    LeftArmMaxExtensionAngle = DoubleField()

    RightArmMaxExtensionAngle = DoubleField()

    ExtraCollarRatio = DoubleField()

    CollarStiffnessX = DoubleField()

    CollarStiffnessY = DoubleField()

    CollarStiffnessZ = DoubleField()

    ReachActorLeftShoulder = DoubleField()

    ReachActorRightShoulder = DoubleField()

    FingerPropagation = FingerPropagationEnumField()

    RealisticLeftKneeSolving = DoubleField()

    RealisticRightKneeSolving = DoubleField()

    SnSScaleArmsAndLegs = DoubleField()

    SnSReachLeftWrist = DoubleField()

    SnSReachRightWrist = DoubleField()

    SnSReachLeftAnkle = DoubleField()

    SnSReachRightAnkle = DoubleField()

    SnSScaleSpine = DoubleField()

    SnSScaleSpineChildren = DoubleField()

    SnSReachChestEnd = DoubleField()

    SnSScaleNeck = DoubleField()

    SnSReachHead = DoubleField()

    LeftUpLegRollEx = DoubleField()

    LeftLegRollEx = DoubleField()

    RightUpLegRollEx = DoubleField()

    RightLegRollEx = DoubleField()

    LeftArmRollEx = DoubleField()

    LeftForeArmRollEx = DoubleField()

    RightArmRollEx = DoubleField()

    RightForeArmRollEx = DoubleField()

    TopSpineCorrection = DoubleField()

    LowerSpineCorrection = DoubleField()

    SnSSmoothReach = SnSSmoothReachEnumField()

    LockX = LockXEnumField()

    LockY = LockYEnumField()

    LockZ = LockZEnumField()

    ParamRealisticArmSolving = ParamRealisticArmSolvingEnumField()

    ParamLeafLeftUpLegRoll1Mode = ParamLeafLeftUpLegRoll1ModeEnumField()

    ParamLeafLeftUpLegRoll1 = DoubleField()

    ParamLeafLeftLegRoll1Mode = ParamLeafLeftLegRoll1ModeEnumField()

    ParamLeafLeftLegRoll1 = DoubleField()

    ParamLeafRightUpLegRoll1Mode = ParamLeafRightUpLegRoll1ModeEnumField()

    ParamLeafRightUpLegRoll1 = DoubleField()

    ParamLeafRightLegRoll1Mode = ParamLeafRightLegRoll1ModeEnumField()

    ParamLeafRightLegRoll1 = DoubleField()

    ParamLeafLeftArmRoll1Mode = ParamLeafLeftArmRoll1ModeEnumField()

    ParamLeafLeftArmRoll1 = DoubleField()

    ParamLeafLeftForeArmRoll1Mode = ParamLeafLeftForeArmRoll1ModeEnumField()

    ParamLeafLeftForeArmRoll1 = DoubleField()

    ParamLeafRightArmRoll1Mode = ParamLeafRightArmRoll1ModeEnumField()

    ParamLeafRightArmRoll1 = DoubleField()

    ParamLeafRightForeArmRoll1Mode = ParamLeafRightForeArmRoll1ModeEnumField()

    ParamLeafRightForeArmRoll1 = DoubleField()

    ParamLeafLeftUpLegRoll2Mode = ParamLeafLeftUpLegRoll2ModeEnumField()

    ParamLeafLeftUpLegRoll2 = DoubleField()

    ParamLeafLeftLegRoll2Mode = ParamLeafLeftLegRoll2ModeEnumField()

    ParamLeafLeftLegRoll2 = DoubleField()

    ParamLeafRightUpLegRoll2Mode = ParamLeafRightUpLegRoll2ModeEnumField()

    ParamLeafRightUpLegRoll2 = DoubleField()

    ParamLeafRightLegRoll2Mode = ParamLeafRightLegRoll2ModeEnumField()

    ParamLeafRightLegRoll2 = DoubleField()

    ParamLeafLeftArmRoll2Mode = ParamLeafLeftArmRoll2ModeEnumField()

    ParamLeafLeftArmRoll2 = DoubleField()

    ParamLeafLeftForeArmRoll2Mode = ParamLeafLeftForeArmRoll2ModeEnumField()

    ParamLeafLeftForeArmRoll2 = DoubleField()

    ParamLeafRightArmRoll2Mode = ParamLeafRightArmRoll2ModeEnumField()

    ParamLeafRightArmRoll2 = DoubleField()

    ParamLeafRightForeArmRoll2Mode = ParamLeafRightForeArmRoll2ModeEnumField()

    ParamLeafRightForeArmRoll2 = DoubleField()

    ParamLeafLeftUpLegRoll3Mode = ParamLeafLeftUpLegRoll3ModeEnumField()

    ParamLeafLeftUpLegRoll3 = DoubleField()

    ParamLeafLeftLegRoll3Mode = ParamLeafLeftLegRoll3ModeEnumField()

    ParamLeafLeftLegRoll3 = DoubleField()

    ParamLeafRightUpLegRoll3Mode = ParamLeafRightUpLegRoll3ModeEnumField()

    ParamLeafRightUpLegRoll3 = DoubleField()

    ParamLeafRightLegRoll3Mode = ParamLeafRightLegRoll3ModeEnumField()

    ParamLeafRightLegRoll3 = DoubleField()

    ParamLeafLeftArmRoll3Mode = ParamLeafLeftArmRoll3ModeEnumField()

    ParamLeafLeftArmRoll3 = DoubleField()

    ParamLeafLeftForeArmRoll3Mode = ParamLeafLeftForeArmRoll3ModeEnumField()

    ParamLeafLeftForeArmRoll3 = DoubleField()

    ParamLeafRightArmRoll3Mode = ParamLeafRightArmRoll3ModeEnumField()

    ParamLeafRightArmRoll3 = DoubleField()

    ParamLeafRightForeArmRoll3Mode = ParamLeafRightForeArmRoll3ModeEnumField()

    ParamLeafRightForeArmRoll3 = DoubleField()

    ParamLeafLeftUpLegRoll4Mode = ParamLeafLeftUpLegRoll4ModeEnumField()

    ParamLeafLeftUpLegRoll4 = DoubleField()

    ParamLeafLeftLegRoll4Mode = ParamLeafLeftLegRoll4ModeEnumField()

    ParamLeafLeftLegRoll4 = DoubleField()

    ParamLeafRightUpLegRoll4Mode = ParamLeafRightUpLegRoll4ModeEnumField()

    ParamLeafRightUpLegRoll4 = DoubleField()

    ParamLeafRightLegRoll4Mode = ParamLeafRightLegRoll4ModeEnumField()

    ParamLeafRightLegRoll4 = DoubleField()

    ParamLeafLeftArmRoll4Mode = ParamLeafLeftArmRoll4ModeEnumField()

    ParamLeafLeftArmRoll4 = DoubleField()

    ParamLeafLeftForeArmRoll4Mode = ParamLeafLeftForeArmRoll4ModeEnumField()

    ParamLeafLeftForeArmRoll4 = DoubleField()

    ParamLeafRightArmRoll4Mode = ParamLeafRightArmRoll4ModeEnumField()

    ParamLeafRightArmRoll4 = DoubleField()

    ParamLeafRightForeArmRoll4Mode = ParamLeafRightForeArmRoll4ModeEnumField()

    ParamLeafRightForeArmRoll4 = DoubleField()

    ParamLeafLeftUpLegRoll5Mode = ParamLeafLeftUpLegRoll5ModeEnumField()

    ParamLeafLeftUpLegRoll5 = DoubleField()

    ParamLeafLeftLegRoll5Mode = ParamLeafLeftLegRoll5ModeEnumField()

    ParamLeafLeftLegRoll5 = DoubleField()

    ParamLeafRightUpLegRoll5Mode = ParamLeafRightUpLegRoll5ModeEnumField()

    ParamLeafRightUpLegRoll5 = DoubleField()

    ParamLeafRightLegRoll5Mode = ParamLeafRightLegRoll5ModeEnumField()

    ParamLeafRightLegRoll5 = DoubleField()

    ParamLeafLeftArmRoll5Mode = ParamLeafLeftArmRoll5ModeEnumField()

    ParamLeafLeftArmRoll5 = DoubleField()

    ParamLeafLeftForeArmRoll5Mode = ParamLeafLeftForeArmRoll5ModeEnumField()

    ParamLeafLeftForeArmRoll5 = DoubleField()

    ParamLeafRightArmRoll5Mode = ParamLeafRightArmRoll5ModeEnumField()

    ParamLeafRightArmRoll5 = DoubleField()

    ParamLeafRightForeArmRoll5Mode = ParamLeafRightForeArmRoll5ModeEnumField()

    ParamLeafRightForeArmRoll5 = DoubleField()

    LeftLegFullRollExtractionMode = LeftLegFullRollExtractionModeEnumField()

    LeftLegFullRollExtraction = DoubleField()

    RightLegFullRollExtractionMode = RightLegFullRollExtractionModeEnumField()

    RightLegFullRollExtraction = DoubleField()

    LeftArmFullRollExtractionMode = LeftArmFullRollExtractionModeEnumField()

    LeftArmFullRollExtraction = DoubleField()

    RightArmFullRollExtractionMode = RightArmFullRollExtractionModeEnumField()

    RightArmFullRollExtraction = DoubleField()

    NeckMotionReduction = DoubleField()
