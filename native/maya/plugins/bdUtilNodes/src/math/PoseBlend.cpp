#include "bdUtilNodes/math/PoseBlend.h"

#include <algorithm>
#include <array>
#include <cmath>
#include <vector>

namespace {

constexpr double kPoseBlendQuaternionEpsilon = 1.0e-12;

bool areFinite(const std::array<double, 3>& value) {
    return std::isfinite(value[0]) && std::isfinite(value[1])
        && std::isfinite(value[2]);
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
    if (!std::isfinite(maximum) || maximum <= kPoseBlendQuaternionEpsilon) {
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

MQuaternion canonicalizeShortest(const MQuaternion& value) {
    bool shouldNegate = value.w < -kPoseBlendQuaternionEpsilon;
    if (std::abs(value.w) <= kPoseBlendQuaternionEpsilon) {
        for (const double component : {value.x, value.y, value.z}) {
            if (component < -kPoseBlendQuaternionEpsilon) {
                shouldNegate = true;
                break;
            }
            if (component > kPoseBlendQuaternionEpsilon) {
                break;
            }
        }
    }
    return shouldNegate ? negate(value) : value;
}

bool quaternionLogVector(
    const MQuaternion& input,
    std::array<double, 3>& output
) {
    MQuaternion normalized;
    if (!normalizeQuaternion(input, normalized)) {
        return false;
    }
    normalized = canonicalizeShortest(normalized);

    const double vectorLength = std::hypot(
        normalized.x,
        normalized.y,
        normalized.z
    );
    if (!std::isfinite(vectorLength)) {
        return false;
    }

    double scale = 2.0;
    if (vectorLength > kPoseBlendQuaternionEpsilon) {
        const double angle = 2.0 * std::atan2(
            vectorLength,
            std::max(0.0, normalized.w)
        );
        scale = angle / vectorLength;
    }
    output = {
        normalized.x * scale,
        normalized.y * scale,
        normalized.z * scale,
    };
    return areFinite(output);
}

bool quaternionExpVector(
    const std::array<double, 3>& input,
    MQuaternion& output
) {
    if (!areFinite(input)) {
        return false;
    }

    const double angle = std::hypot(input[0], input[1], input[2]);
    if (!std::isfinite(angle)) {
        return false;
    }

    if (angle <= kPoseBlendQuaternionEpsilon) {
        output = MQuaternion(
            0.5 * input[0],
            0.5 * input[1],
            0.5 * input[2],
            1.0
        );
        return normalizeQuaternion(output, output);
    }

    const double halfAngle = 0.5 * angle;
    const double scale = std::sin(halfAngle) / angle;
    output = MQuaternion(
        input[0] * scale,
        input[1] * scale,
        input[2] * scale,
        std::cos(halfAngle)
    );
    return normalizeQuaternion(output, output);
}

}  // namespace

namespace bd_util_nodes {

PoseBlendStatus blendPose(
    const std::array<double, 3>& baseTranslate,
    const MQuaternion& baseRotate,
    const std::array<double, 3>& baseScale,
    const std::vector<WeightedPoseValue>& poses,
    PoseBlendResult& result
) {
    result = {};
    if (!areFinite(baseTranslate)) {
        return PoseBlendStatus::kInvalidTranslate;
    }

    MQuaternion normalizedBaseRotate;
    if (!normalizeQuaternion(baseRotate, normalizedBaseRotate)) {
        return PoseBlendStatus::kInvalidRotate;
    }
    if (!areFinite(baseScale)) {
        return PoseBlendStatus::kInvalidScale;
    }

    result.translate = baseTranslate;
    result.rotate = normalizedBaseRotate;
    result.scale = baseScale;

    std::vector<const WeightedPoseValue*> sortedPoses;
    sortedPoses.reserve(poses.size());
    for (const WeightedPoseValue& pose : poses) {
        sortedPoses.push_back(&pose);
    }
    std::sort(
        sortedPoses.begin(),
        sortedPoses.end(),
        [](const WeightedPoseValue* left, const WeightedPoseValue* right) {
            return left->logicalIndex < right->logicalIndex;
        }
    );

    std::array<double, 3> translateDelta = {0.0, 0.0, 0.0};
    std::array<double, 3> rotateVector = {0.0, 0.0, 0.0};
    std::array<double, 3> scaleDelta = {0.0, 0.0, 0.0};

    for (const WeightedPoseValue* pose : sortedPoses) {
        if (!std::isfinite(pose->weight)) {
            return PoseBlendStatus::kInvalidWeight;
        }
        if (pose->weight == 0.0) {
            continue;
        }
        if (!areFinite(pose->translate)) {
            return PoseBlendStatus::kInvalidTranslate;
        }

        MQuaternion normalizedPoseRotate;
        if (!normalizeQuaternion(pose->rotate, normalizedPoseRotate)) {
            return PoseBlendStatus::kInvalidRotate;
        }
        if (!areFinite(pose->scale)) {
            return PoseBlendStatus::kInvalidScale;
        }

        MQuaternion relativeRotate =
            conjugate(normalizedBaseRotate) * normalizedPoseRotate;
        std::array<double, 3> poseRotateVector;
        if (!quaternionLogVector(relativeRotate, poseRotateVector)) {
            return PoseBlendStatus::kInvalidRotate;
        }

        for (std::size_t index = 0; index < 3; ++index) {
            translateDelta[index] += pose->weight
                * (pose->translate[index] - baseTranslate[index]);
            rotateVector[index] += pose->weight * poseRotateVector[index];
            scaleDelta[index] += pose->weight
                * (pose->scale[index] - baseScale[index]);
        }
        if (
            !areFinite(translateDelta) || !areFinite(rotateVector)
            || !areFinite(scaleDelta)
        ) {
            return PoseBlendStatus::kNumericalFailure;
        }
    }

    for (std::size_t index = 0; index < 3; ++index) {
        result.translate[index] = baseTranslate[index]
            + translateDelta[index];
        result.scale[index] = baseScale[index] + scaleDelta[index];
    }
    if (!areFinite(result.translate) || !areFinite(result.scale)) {
        result.translate = baseTranslate;
        result.scale = baseScale;
        return PoseBlendStatus::kNumericalFailure;
    }

    MQuaternion relativeResult;
    if (!quaternionExpVector(rotateVector, relativeResult)) {
        return PoseBlendStatus::kNumericalFailure;
    }
    MQuaternion blendedRotate = normalizedBaseRotate * relativeResult;
    if (!normalizeQuaternion(blendedRotate, result.rotate)) {
        result.rotate = normalizedBaseRotate;
        return PoseBlendStatus::kNumericalFailure;
    }
    return PoseBlendStatus::kSuccess;
}

}  // namespace bd_util_nodes
