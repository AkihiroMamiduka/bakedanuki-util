#include "bdUtilNodes/math/BendTwist.h"

#include <algorithm>
#include <cmath>

#include "bdUtilNodes/math/Angle.h"

namespace {

constexpr double kBendTwistEpsilon = 1.0e-10;

MQuaternion invalidQuaternion() {
    return MQuaternion();
}

bool normalizeQuaternion(
    const MQuaternion& input,
    MQuaternion& output
) {
    const double maximum = std::max({
        std::abs(input.x),
        std::abs(input.y),
        std::abs(input.z),
        std::abs(input.w),
    });
    if (!std::isfinite(maximum) || maximum <= kBendTwistEpsilon) {
        return false;
    }

    const double scaledX = input.x / maximum;
    const double scaledY = input.y / maximum;
    const double scaledZ = input.z / maximum;
    const double scaledW = input.w / maximum;
    const double length = std::sqrt(
        scaledX * scaledX + scaledY * scaledY + scaledZ * scaledZ
        + scaledW * scaledW
    );
    if (!std::isfinite(length) || length <= 0.0) {
        return false;
    }

    output = MQuaternion(
        scaledX / length,
        scaledY / length,
        scaledZ / length,
        scaledW / length
    );
    return true;
}

MQuaternion conjugate(const MQuaternion& value) {
    return MQuaternion(-value.x, -value.y, -value.z, value.w);
}

MQuaternion negate(const MQuaternion& value) {
    return MQuaternion(-value.x, -value.y, -value.z, -value.w);
}

MQuaternion canonicalizeTwist(const MQuaternion& twist) {
    if (
        twist.w < -kBendTwistEpsilon
        || (
            std::abs(twist.w) <= kBendTwistEpsilon
            && twist.x < 0.0
        )
    ) {
        return negate(twist);
    }
    return twist;
}

MQuaternion canonicalizeBend(const MQuaternion& bend) {
    bool shouldNegate = bend.w < -kBendTwistEpsilon;
    if (std::abs(bend.w) <= kBendTwistEpsilon) {
        if (bend.y < -kBendTwistEpsilon) {
            shouldNegate = true;
        } else if (std::abs(bend.y) <= kBendTwistEpsilon) {
            if (bend.z < -kBendTwistEpsilon) {
                shouldNegate = true;
            } else if (
                std::abs(bend.z) <= kBendTwistEpsilon
                && bend.x < 0.0
            ) {
                shouldNegate = true;
            }
        }
    }
    return shouldNegate ? negate(bend) : bend;
}

bool isSupportedOrder(bd_util_nodes::BendTwistOrder order) {
    return order == bd_util_nodes::BendTwistOrder::kTwistBend
        || order == bd_util_nodes::BendTwistOrder::kBendTwist;
}

bd_util_nodes::BendTwistComponents invalidComponents() {
    return {};
}

struct DecompositionFrame {
    MQuaternion canonical;
};

bool prepareDecompositionFrame(
    const MQuaternion& input,
    const MQuaternion& axisOrientation,
    DecompositionFrame& frame
) {
    MQuaternion normalizedInput;
    MQuaternion normalizedAxisOrientation;
    if (
        !normalizeQuaternion(input, normalizedInput)
        || !normalizeQuaternion(
            axisOrientation,
            normalizedAxisOrientation
        )
    ) {
        return false;
    }

    frame.canonical = normalizedAxisOrientation * normalizedInput
        * conjugate(normalizedAxisOrientation);
    return normalizeQuaternion(frame.canonical, frame.canonical);
}

struct TwistProjection {
    double twist = 0.0;
    MQuaternion quaternion;
    bool singular = false;
};

bool projectTwist(
    const DecompositionFrame& frame,
    TwistProjection& projection
) {
    const double projectionLength = std::hypot(
        frame.canonical.x,
        frame.canonical.w
    );
    if (!std::isfinite(projectionLength)) {
        return false;
    }
    if (projectionLength <= kBendTwistEpsilon) {
        projection.singular = true;
        return true;
    }

    projection.quaternion = canonicalizeTwist(MQuaternion(
        frame.canonical.x / projectionLength,
        0.0,
        0.0,
        frame.canonical.w / projectionLength
    ));
    projection.twist = bd_util_nodes::wrapAngle(
        2.0 * std::atan2(
            projection.quaternion.x,
            projection.quaternion.w
        ),
        -bd_util_nodes::kPiRadians,
        bd_util_nodes::kPiRadians
    );
    return true;
}

bd_util_nodes::BendTwistComponents bendToComponents(
    const MQuaternion& bend,
    double twist
) {
    MQuaternion normalizedBend;
    if (!normalizeQuaternion(bend, normalizedBend)) {
        return invalidComponents();
    }
    normalizedBend = canonicalizeBend(normalizedBend);

    const double transverseLength = std::hypot(
        normalizedBend.y,
        normalizedBend.z
    );
    if (!std::isfinite(transverseLength)) {
        return invalidComponents();
    }
    bd_util_nodes::BendTwistComponents result;
    result.twist = twist;
    if (transverseLength <= kBendTwistEpsilon) {
        return result;
    }

    const double bendAngle = 2.0 * std::atan2(
        transverseLength,
        std::max(0.0, normalizedBend.w)
    );
    result.bendHorizontal =
        bendAngle * normalizedBend.y / transverseLength;
    result.bendVertical =
        bendAngle * normalizedBend.z / transverseLength;
    result.bendRatio = std::clamp(
        bendAngle / bd_util_nodes::kPiRadians,
        0.0,
        1.0
    );
    return result;
}

}  // namespace

namespace bd_util_nodes {

double decomposeTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation
) {
    DecompositionFrame frame;
    TwistProjection projection;
    if (
        !prepareDecompositionFrame(input, axisOrientation, frame)
        || !projectTwist(frame, projection)
    ) {
        return 0.0;
    }
    return projection.twist;
}

BendTwistComponents decomposeBendTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation,
    BendTwistOrder order
) {
    if (!isSupportedOrder(order)) {
        return invalidComponents();
    }

    DecompositionFrame frame;
    if (
        !prepareDecompositionFrame(input, axisOrientation, frame)
    ) {
        return invalidComponents();
    }

    TwistProjection projection;
    if (!projectTwist(frame, projection)) {
        return invalidComponents();
    }
    if (projection.singular) {
        return bendToComponents(
            canonicalizeBend(frame.canonical),
            0.0
        );
    }

    const MQuaternion inverseTwist = conjugate(projection.quaternion);
    const MQuaternion bendQuaternion =
        order == BendTwistOrder::kTwistBend
        ? inverseTwist * frame.canonical
        : frame.canonical * inverseTwist;
    return bendToComponents(
        bendQuaternion,
        projection.twist
    );
}

MQuaternion composeBendTwist(
    double twist,
    double bendHorizontal,
    double bendVertical,
    const MQuaternion& axisOrientation,
    BendTwistOrder order
) {
    MQuaternion normalizedAxisOrientation;
    if (
        !isSupportedOrder(order) || !std::isfinite(twist)
        || !std::isfinite(bendHorizontal)
        || !std::isfinite(bendVertical)
        || !normalizeQuaternion(
            axisOrientation,
            normalizedAxisOrientation
        )
    ) {
        return invalidQuaternion();
    }

    const double bendAngle = std::hypot(
        bendHorizontal,
        bendVertical
    );
    if (!std::isfinite(bendAngle)) {
        return invalidQuaternion();
    }

    const double twistHalfAngle = 0.5 * twist;
    const MQuaternion twistQuaternion(
        std::sin(twistHalfAngle),
        0.0,
        0.0,
        std::cos(twistHalfAngle)
    );

    MQuaternion bendQuaternion;
    if (bendAngle > kBendTwistEpsilon) {
        const double bendHalfAngle = 0.5 * bendAngle;
        const double scale = std::sin(bendHalfAngle) / bendAngle;
        bendQuaternion = MQuaternion(
            0.0,
            bendHorizontal * scale,
            bendVertical * scale,
            std::cos(bendHalfAngle)
        );
    }

    const MQuaternion canonical =
        order == BendTwistOrder::kTwistBend
        ? twistQuaternion * bendQuaternion
        : bendQuaternion * twistQuaternion;
    MQuaternion output = conjugate(normalizedAxisOrientation) * canonical
        * normalizedAxisOrientation;
    if (!normalizeQuaternion(output, output)) {
        return invalidQuaternion();
    }
    return output;
}

}  // namespace bd_util_nodes
