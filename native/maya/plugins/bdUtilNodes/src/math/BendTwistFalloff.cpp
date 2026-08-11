#include "bdUtilNodes/math/BendTwistFalloff.h"

#include <algorithm>
#include <cmath>

#include <maya/MQuaternion.h>
#include <maya/MVector.h>

#include "bdUtilNodes/math/Angle.h"

namespace {

constexpr double kNormalizationEpsilon = 1.0e-12;
using Quaternion = std::array<double, 4>;

bool normalizeQuaternion(
    const Quaternion& input,
    MQuaternion& output
) {
    const double maximum = std::max({
        std::abs(input[0]),
        std::abs(input[1]),
        std::abs(input[2]),
        std::abs(input[3]),
    });
    if (!std::isfinite(maximum) || maximum <= kNormalizationEpsilon) {
        return false;
    }

    const double x = input[0] / maximum;
    const double y = input[1] / maximum;
    const double z = input[2] / maximum;
    const double w = input[3] / maximum;
    const double length = std::sqrt(x * x + y * y + z * z + w * w);
    if (!std::isfinite(length) || length <= 0.0) {
        return false;
    }

    output = MQuaternion(x / length, y / length, z / length, w / length);
    return true;
}

bool areFinite(const bd_util_nodes::BendTwistComponents& components) {
    return std::isfinite(components.twist)
        && std::isfinite(components.bendHorizontal)
        && std::isfinite(components.bendVertical);
}

bool bendDirection(
    const bd_util_nodes::BendTwistComponents& components,
    MVector& direction
) {
    const MQuaternion bend = bd_util_nodes::composeBendTwist(
        0.0,
        components.bendHorizontal,
        components.bendVertical,
        MQuaternion(),
        bd_util_nodes::BendTwistOrder::kTwistBend
    );
    direction = MVector(1.0, 0.0, 0.0).rotateBy(bend);
    const double length = direction.length();
    if (!std::isfinite(length) || length <= 0.0) {
        return false;
    }
    direction /= length;
    return std::isfinite(direction.x) && std::isfinite(direction.y)
        && std::isfinite(direction.z);
}

double directionDistance(const MVector& first, const MVector& second) {
    return std::acos(std::clamp(first * second, -1.0, 1.0));
}

bool isSupportedMode(bd_util_nodes::BendTwistFalloffMode mode) {
    return mode == bd_util_nodes::BendTwistFalloffMode::kBendTwist
        || mode == bd_util_nodes::BendTwistFalloffMode::kBendOnly;
}

bool isSupportedOrder(bd_util_nodes::BendTwistOrder order) {
    return order == bd_util_nodes::BendTwistOrder::kTwistBend
        || order == bd_util_nodes::BendTwistOrder::kBendTwist;
}

}  // namespace

namespace bd_util_nodes {

BendTwistFalloffStatus evaluateBendTwistFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::array<double, 4>& axisQuaternion,
    const std::vector<BendTwistFalloffSample>& samples,
    BendTwistOrder order,
    BendTwistFalloffMode mode,
    Falloff falloff,
    std::vector<BendTwistFalloffWeight>& outputWeights
) {
    outputWeights.clear();
    if (samples.empty()) {
        return BendTwistFalloffStatus::kNoPoses;
    }
    if (!isSupportedFalloff(falloff)) {
        return BendTwistFalloffStatus::kUnsupportedFalloff;
    }
    if (!isSupportedMode(mode)) {
        return BendTwistFalloffStatus::kUnsupportedMode;
    }
    if (!isSupportedOrder(order)) {
        return BendTwistFalloffStatus::kUnsupportedOrder;
    }

    MQuaternion normalizedInput;
    MQuaternion normalizedAxis;
    if (
        !normalizeQuaternion(inputQuaternion, normalizedInput)
        || !normalizeQuaternion(axisQuaternion, normalizedAxis)
    ) {
        return BendTwistFalloffStatus::kInvalidQuaternion;
    }

    const BendTwistComponents inputComponents = decomposeBendTwist(
        normalizedInput,
        normalizedAxis,
        order
    );
    MVector inputDirection;
    if (!areFinite(inputComponents) || !bendDirection(
            inputComponents,
            inputDirection
        )) {
        return BendTwistFalloffStatus::kNumericalFailure;
    }

    outputWeights.reserve(samples.size());
    for (const BendTwistFalloffSample& sample : samples) {
        if (!isValidFalloffRadius(
                sample.bendInnerRadiusRadians,
                sample.bendOuterRadiusRadians
            ) || (
                mode == BendTwistFalloffMode::kBendTwist
                && !isValidFalloffRadius(
                    sample.twistInnerRadiusRadians,
                    sample.twistOuterRadiusRadians
                )
            )) {
            outputWeights.clear();
            return BendTwistFalloffStatus::kInvalidRadius;
        }

        MQuaternion normalizedPose;
        if (!normalizeQuaternion(sample.quaternion, normalizedPose)) {
            outputWeights.clear();
            return BendTwistFalloffStatus::kInvalidQuaternion;
        }
        const BendTwistComponents poseComponents = decomposeBendTwist(
            normalizedPose,
            normalizedAxis,
            order
        );
        MVector poseDirection;
        if (!areFinite(poseComponents) || !bendDirection(
                poseComponents,
                poseDirection
            )) {
            outputWeights.clear();
            return BendTwistFalloffStatus::kNumericalFailure;
        }

        const double bendDistance = directionDistance(
            inputDirection,
            poseDirection
        );
        if (!std::isfinite(bendDistance)) {
            outputWeights.clear();
            return BendTwistFalloffStatus::kNumericalFailure;
        }
        double weight = evaluateFalloffWeight(
            falloff,
            bendDistance,
            sample.bendInnerRadiusRadians,
            sample.bendOuterRadiusRadians
        );

        if (mode == BendTwistFalloffMode::kBendTwist) {
            const double twistDistance = std::abs(shortestAngleDelta(
                inputComponents.twist,
                poseComponents.twist
            ));
            if (!std::isfinite(twistDistance)) {
                outputWeights.clear();
                return BendTwistFalloffStatus::kNumericalFailure;
            }
            weight *= evaluateFalloffWeight(
                falloff,
                twistDistance,
                sample.twistInnerRadiusRadians,
                sample.twistOuterRadiusRadians
            );
        }

        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return BendTwistFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return BendTwistFalloffStatus::kSuccess;
}

}  // namespace bd_util_nodes
