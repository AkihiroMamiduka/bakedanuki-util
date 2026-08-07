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
    return {0.0, 0.0, 0.0, 0.0};
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
    if (transverseLength <= kBendTwistEpsilon) {
        return {twist, 0.0, 0.0, 0.0};
    }

    const double bendAngle = 2.0 * std::atan2(
        transverseLength,
        std::max(0.0, normalizedBend.w)
    );
    return {
        twist,
        bendAngle * normalizedBend.y / transverseLength,
        bendAngle * normalizedBend.z / transverseLength,
        std::clamp(bendAngle / bd_util_nodes::kPiRadians, 0.0, 1.0),
    };
}

}  // namespace

namespace bd_util_nodes {

BendTwistComponents decomposeBendTwist(
    const MQuaternion& input,
    const MQuaternion& axisOrientation,
    BendTwistOrder order
) {
    if (!isSupportedOrder(order)) {
        return invalidComponents();
    }

    MQuaternion normalizedInput;
    MQuaternion normalizedAxisOrientation;
    if (
        !normalizeQuaternion(input, normalizedInput)
        || !normalizeQuaternion(
            axisOrientation,
            normalizedAxisOrientation
        )
    ) {
        return invalidComponents();
    }

    MQuaternion canonical = normalizedAxisOrientation * normalizedInput
        * conjugate(normalizedAxisOrientation);
    if (!normalizeQuaternion(canonical, canonical)) {
        return invalidComponents();
    }

    const double twistProjectionLength = std::hypot(
        canonical.x,
        canonical.w
    );
    if (!std::isfinite(twistProjectionLength)) {
        return invalidComponents();
    }
    if (twistProjectionLength <= kBendTwistEpsilon) {
        return bendToComponents(canonicalizeBend(canonical), 0.0);
    }

    MQuaternion twistQuaternion(
        canonical.x / twistProjectionLength,
        0.0,
        0.0,
        canonical.w / twistProjectionLength
    );
    twistQuaternion = canonicalizeTwist(twistQuaternion);

    const MQuaternion inverseTwist = conjugate(twistQuaternion);
    const MQuaternion bendQuaternion =
        order == BendTwistOrder::kTwistBend
        ? inverseTwist * canonical
        : canonical * inverseTwist;

    const double twist = wrapAngle(
        2.0 * std::atan2(twistQuaternion.x, twistQuaternion.w),
        -kPiRadians,
        kPiRadians
    );
    return bendToComponents(bendQuaternion, twist);
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
