#pragma once

#include <maya/MQuaternion.h>

namespace bd_util_nodes {

enum class BendTwistOrder : short {
    kTwistBend = 0,
    kBendTwist = 1,
};

struct BendTwistComponents {
    double twist;
    double bendHorizontal;
    double bendVertical;
    double bendRatio;
};

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
