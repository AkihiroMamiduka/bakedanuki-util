#pragma once

#include <maya/MQuaternion.h>

namespace bd_util_nodes {

enum class BendTwistOrder : short {
    kTwistBend = 0,
    kBendTwist = 1,
};

struct BendTwistComponents {
    double twist = 0.0;
    double bendHorizontal = 0.0;
    double bendVertical = 0.0;
    double bendRatio = 0.0;
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

}  // namespace bd_util_nodes
