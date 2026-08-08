#pragma once

#include <maya/MQuaternion.h>

namespace bd_util_nodes {

enum class BendTwistOrder : short {
    kTwistBend = 0,
    kBendTwist = 1,
};

enum class BendLimitMode : short {
    kBox = 0,
    kEllipse = 1,
};

struct BendTwistComponents {
    double twist = 0.0;
    double bendHorizontal = 0.0;
    double bendVertical = 0.0;
    double bendRatio = 0.0;
};

struct BendTwistLimits {
    double minTwist = 0.0;
    double minBendHorizontal = 0.0;
    double minBendVertical = 0.0;
    double maxTwist = 0.0;
    double maxBendHorizontal = 0.0;
    double maxBendVertical = 0.0;
};

struct BendTwistLimitResult {
    BendTwistComponents components;
    MQuaternion quaternion;
};

double decomposeTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation
);

BendTwistComponents decomposeBendTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation,
    BendTwistOrder order
);

MQuaternion composeBendTwist(
    double twist,
    double bendHorizontal,
    double bendVertical,
    const MQuaternion& axisOrientation,
    BendTwistOrder order
);

BendTwistLimitResult limitBendTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation,
    BendTwistOrder order,
    BendLimitMode mode,
    const BendTwistLimits& limits
);

}  // namespace bd_util_nodes
