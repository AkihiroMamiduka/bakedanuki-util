#include "bdUtilNodes/math/OrientationFalloff.h"

#include <algorithm>
#include <cmath>

namespace {

constexpr double kQuaternionEpsilon = 1.0e-12;
using Quaternion = std::array<double, 4>;

bool normalizeQuaternion(const Quaternion& input, Quaternion& output) {
    const double maximum = std::max({
        std::abs(input[0]),
        std::abs(input[1]),
        std::abs(input[2]),
        std::abs(input[3]),
    });
    if (!std::isfinite(maximum) || maximum <= kQuaternionEpsilon) {
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

    output = {x / length, y / length, z / length, w / length};
    return true;
}

double quaternionDistance(
    const Quaternion& first,
    const Quaternion& second
) {
    const double dot = std::abs(
        first[0] * second[0] + first[1] * second[1]
        + first[2] * second[2] + first[3] * second[3]
    );
    return 2.0 * std::acos(std::clamp(dot, 0.0, 1.0));
}

}  // namespace

namespace bd_util_nodes {

OrientationFalloffStatus evaluateOrientationFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::vector<OrientationFalloffSample>& samples,
    Falloff falloff,
    std::vector<OrientationFalloffWeight>& outputWeights
) {
    outputWeights.clear();
    if (samples.empty()) {
        return OrientationFalloffStatus::kNoPoses;
    }
    if (!isSupportedFalloff(falloff)) {
        return OrientationFalloffStatus::kUnsupportedFalloff;
    }

    Quaternion normalizedInput;
    if (!normalizeQuaternion(inputQuaternion, normalizedInput)) {
        return OrientationFalloffStatus::kInvalidQuaternion;
    }

    outputWeights.reserve(samples.size());
    for (const OrientationFalloffSample& sample : samples) {
        if (!isValidFalloffRadius(
                sample.innerRadiusRadians,
                sample.outerRadiusRadians
            )) {
            outputWeights.clear();
            return OrientationFalloffStatus::kInvalidRadius;
        }

        Quaternion normalizedPose;
        if (!normalizeQuaternion(sample.quaternion, normalizedPose)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kInvalidQuaternion;
        }

        const double distance = quaternionDistance(
            normalizedInput,
            normalizedPose
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kNumericalFailure;
        }
        const double weight = evaluateFalloffWeight(
            falloff,
            distance,
            sample.innerRadiusRadians,
            sample.outerRadiusRadians
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return OrientationFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return OrientationFalloffStatus::kSuccess;
}

struct MultiOrientationFalloffEvaluator::Impl {
    std::vector<QuaternionSourceDefinition> sources;
    std::vector<MultiOrientationFalloffSample> samples;
    std::vector<std::vector<Quaternion>> normalizedPoseQuaternions;
    Falloff falloff = Falloff::kQuintic;
    double influenceSum = 0.0;
    MultiOrientationFalloffStatus evaluationStatus =
        MultiOrientationFalloffStatus::kNoSources;
};

MultiOrientationFalloffEvaluator::MultiOrientationFalloffEvaluator()
    : impl_(std::make_unique<Impl>()) {}

MultiOrientationFalloffEvaluator::~MultiOrientationFalloffEvaluator() =
    default;

MultiOrientationFalloffEvaluator::MultiOrientationFalloffEvaluator(
    MultiOrientationFalloffEvaluator&&
) noexcept = default;

MultiOrientationFalloffEvaluator&
MultiOrientationFalloffEvaluator::operator=(
    MultiOrientationFalloffEvaluator&&
) noexcept = default;

MultiOrientationFalloffStatus MultiOrientationFalloffEvaluator::configure(
    const std::vector<QuaternionSourceDefinition>& sources,
    const std::vector<MultiOrientationFalloffSample>& samples,
    Falloff falloff
) {
    impl_->sources.clear();
    impl_->samples.clear();
    impl_->normalizedPoseQuaternions.clear();
    impl_->influenceSum = 0.0;

    if (sources.empty()) {
        impl_->evaluationStatus = MultiOrientationFalloffStatus::kNoSources;
        return impl_->evaluationStatus;
    }
    if (samples.empty()) {
        impl_->evaluationStatus = MultiOrientationFalloffStatus::kNoPoses;
        return impl_->evaluationStatus;
    }
    if (!isSupportedFalloff(falloff)) {
        impl_->evaluationStatus =
            MultiOrientationFalloffStatus::kUnsupportedFalloff;
        return impl_->evaluationStatus;
    }

    impl_->sources = sources;
    for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
        const QuaternionSourceDefinition& source = impl_->sources[index];
        if (
            !std::isfinite(source.influence) || source.influence < 0.0
            || (
                index > 0
                && impl_->sources[index - 1].logicalIndex
                    >= source.logicalIndex
            )
        ) {
            impl_->sources.clear();
            impl_->evaluationStatus =
                MultiOrientationFalloffStatus::kInvalidInfluence;
            return impl_->evaluationStatus;
        }
        impl_->influenceSum += source.influence;
    }
    if (!std::isfinite(impl_->influenceSum) || impl_->influenceSum <= 0.0) {
        impl_->sources.clear();
        impl_->evaluationStatus =
            MultiOrientationFalloffStatus::kInvalidInfluence;
        return impl_->evaluationStatus;
    }

    impl_->samples = samples;
    impl_->normalizedPoseQuaternions.reserve(samples.size());
    for (const MultiOrientationFalloffSample& sample : samples) {
        if (!isValidFalloffRadius(
                sample.innerRadiusRadians,
                sample.outerRadiusRadians
            )) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->normalizedPoseQuaternions.clear();
            impl_->evaluationStatus =
                MultiOrientationFalloffStatus::kInvalidRadius;
            return impl_->evaluationStatus;
        }
        if (sample.sourceQuaternions.size() != impl_->sources.size()) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->normalizedPoseQuaternions.clear();
            impl_->evaluationStatus =
                MultiOrientationFalloffStatus::kIncompletePose;
            return impl_->evaluationStatus;
        }

        std::vector<Quaternion> normalizedQuaternions;
        normalizedQuaternions.reserve(impl_->sources.size());
        for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
            if (
                sample.sourceQuaternions[index].logicalIndex
                != impl_->sources[index].logicalIndex
            ) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->normalizedPoseQuaternions.clear();
                impl_->evaluationStatus =
                    MultiOrientationFalloffStatus::kIncompletePose;
                return impl_->evaluationStatus;
            }
            Quaternion normalized = {0.0, 0.0, 0.0, 1.0};
            if (
                impl_->sources[index].influence > 0.0
                && !normalizeQuaternion(
                    sample.sourceQuaternions[index].quaternion,
                    normalized
                )
            ) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->normalizedPoseQuaternions.clear();
                impl_->evaluationStatus =
                    MultiOrientationFalloffStatus::kInvalidQuaternion;
                return impl_->evaluationStatus;
            }
            normalizedQuaternions.push_back(normalized);
        }
        impl_->normalizedPoseQuaternions.push_back(
            std::move(normalizedQuaternions)
        );
    }

    impl_->falloff = falloff;
    impl_->evaluationStatus = MultiOrientationFalloffStatus::kSuccess;
    return impl_->evaluationStatus;
}

MultiOrientationFalloffStatus MultiOrientationFalloffEvaluator::evaluate(
    const std::vector<IndexedQuaternion>& inputQuaternions,
    std::vector<OrientationFalloffWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->evaluationStatus != MultiOrientationFalloffStatus::kSuccess) {
        return impl_->evaluationStatus;
    }
    if (inputQuaternions.size() != impl_->sources.size()) {
        return MultiOrientationFalloffStatus::kIncompletePose;
    }

    std::vector<Quaternion> normalizedInputs;
    normalizedInputs.reserve(inputQuaternions.size());
    for (std::size_t index = 0; index < inputQuaternions.size(); ++index) {
        if (
            inputQuaternions[index].logicalIndex
            != impl_->sources[index].logicalIndex
        ) {
            return MultiOrientationFalloffStatus::kIncompletePose;
        }
        Quaternion normalized = {0.0, 0.0, 0.0, 1.0};
        if (
            impl_->sources[index].influence > 0.0
            && !normalizeQuaternion(
                inputQuaternions[index].quaternion,
                normalized
            )
        ) {
            return MultiOrientationFalloffStatus::kInvalidQuaternion;
        }
        normalizedInputs.push_back(normalized);
    }

    outputWeights.reserve(impl_->samples.size());
    for (std::size_t poseIndex = 0; poseIndex < impl_->samples.size(); ++poseIndex) {
        double weightedSquaredDistance = 0.0;
        for (std::size_t sourceIndex = 0; sourceIndex < impl_->sources.size(); ++sourceIndex) {
            if (impl_->sources[sourceIndex].influence <= 0.0) {
                continue;
            }
            const double distance = quaternionDistance(
                normalizedInputs[sourceIndex],
                impl_->normalizedPoseQuaternions[poseIndex][sourceIndex]
            );
            weightedSquaredDistance +=
                impl_->sources[sourceIndex].influence * distance * distance;
        }
        const double distance = std::sqrt(
            weightedSquaredDistance / impl_->influenceSum
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return MultiOrientationFalloffStatus::kNumericalFailure;
        }
        const MultiOrientationFalloffSample& sample = impl_->samples[poseIndex];
        const double weight = evaluateFalloffWeight(
            impl_->falloff,
            distance,
            sample.innerRadiusRadians,
            sample.outerRadiusRadians
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return MultiOrientationFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return MultiOrientationFalloffStatus::kSuccess;
}

MultiOrientationFalloffStatus MultiOrientationFalloffEvaluator::status() const {
    return impl_->evaluationStatus;
}

}  // namespace bd_util_nodes
