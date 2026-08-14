#include "bdUtilNodes/math/BendTwistFalloff.h"

#include <algorithm>
#include <cmath>
#include <utility>

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

struct MultiBendTwistFalloffEvaluator::Impl {
    std::vector<MultiBendTwistFalloffSourceDefinition> sources;
    std::vector<MultiBendTwistFalloffSample> samples;
    std::vector<MQuaternion> normalizedAxes;
    std::vector<std::vector<MVector>> poseDirections;
    std::vector<std::vector<double>> poseTwists;
    BendTwistFalloffMode mode = BendTwistFalloffMode::kBendTwist;
    Falloff falloff = Falloff::kQuintic;
    double influenceSum = 0.0;
    MultiBendTwistFalloffStatus evaluationStatus =
        MultiBendTwistFalloffStatus::kNoSources;
};

MultiBendTwistFalloffEvaluator::MultiBendTwistFalloffEvaluator()
    : impl_(std::make_unique<Impl>()) {}

MultiBendTwistFalloffEvaluator::~MultiBendTwistFalloffEvaluator() =
    default;

MultiBendTwistFalloffEvaluator::MultiBendTwistFalloffEvaluator(
    MultiBendTwistFalloffEvaluator&&
) noexcept = default;

MultiBendTwistFalloffEvaluator&
MultiBendTwistFalloffEvaluator::operator=(
    MultiBendTwistFalloffEvaluator&&
) noexcept = default;

MultiBendTwistFalloffStatus MultiBendTwistFalloffEvaluator::configure(
    const std::vector<MultiBendTwistFalloffSourceDefinition>& sources,
    const std::vector<MultiBendTwistFalloffSample>& samples,
    BendTwistFalloffMode mode,
    Falloff falloff
) {
    impl_->sources.clear();
    impl_->samples.clear();
    impl_->normalizedAxes.clear();
    impl_->poseDirections.clear();
    impl_->poseTwists.clear();
    impl_->influenceSum = 0.0;

    if (sources.empty()) {
        impl_->evaluationStatus =
            MultiBendTwistFalloffStatus::kNoSources;
        return impl_->evaluationStatus;
    }
    if (samples.empty()) {
        impl_->evaluationStatus = MultiBendTwistFalloffStatus::kNoPoses;
        return impl_->evaluationStatus;
    }
    if (!isSupportedFalloff(falloff)) {
        impl_->evaluationStatus =
            MultiBendTwistFalloffStatus::kUnsupportedFalloff;
        return impl_->evaluationStatus;
    }
    if (!isSupportedMode(mode)) {
        impl_->evaluationStatus =
            MultiBendTwistFalloffStatus::kUnsupportedMode;
        return impl_->evaluationStatus;
    }

    impl_->sources = sources;
    impl_->normalizedAxes.reserve(sources.size());
    for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
        const MultiBendTwistFalloffSourceDefinition& source =
            impl_->sources[index];
        if (
            !std::isfinite(source.influence) || source.influence < 0.0
            || (
                index > 0
                && impl_->sources[index - 1].logicalIndex
                    >= source.logicalIndex
            )
        ) {
            impl_->sources.clear();
            impl_->normalizedAxes.clear();
            impl_->evaluationStatus =
                MultiBendTwistFalloffStatus::kInvalidInfluence;
            return impl_->evaluationStatus;
        }

        MQuaternion normalizedAxis;
        if (source.influence > 0.0) {
            if (!isSupportedOrder(source.order)) {
                impl_->sources.clear();
                impl_->normalizedAxes.clear();
                impl_->evaluationStatus =
                    MultiBendTwistFalloffStatus::kUnsupportedOrder;
                return impl_->evaluationStatus;
            }
            if (!normalizeQuaternion(
                    source.axisQuaternion,
                    normalizedAxis
                )) {
                impl_->sources.clear();
                impl_->normalizedAxes.clear();
                impl_->evaluationStatus =
                    MultiBendTwistFalloffStatus::kInvalidQuaternion;
                return impl_->evaluationStatus;
            }
        }
        impl_->normalizedAxes.push_back(normalizedAxis);
        impl_->influenceSum += source.influence;
    }
    if (!std::isfinite(impl_->influenceSum) || impl_->influenceSum <= 0.0) {
        impl_->sources.clear();
        impl_->normalizedAxes.clear();
        impl_->evaluationStatus =
            MultiBendTwistFalloffStatus::kInvalidInfluence;
        return impl_->evaluationStatus;
    }

    impl_->samples = samples;
    impl_->poseDirections.reserve(samples.size());
    impl_->poseTwists.reserve(samples.size());
    for (const MultiBendTwistFalloffSample& sample : samples) {
        if (
            !isValidFalloffRadius(
                sample.bendInnerRadiusRadians,
                sample.bendOuterRadiusRadians
            )
            || (
                mode == BendTwistFalloffMode::kBendTwist
                && !isValidFalloffRadius(
                    sample.twistInnerRadiusRadians,
                    sample.twistOuterRadiusRadians
                )
            )
        ) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->normalizedAxes.clear();
            impl_->poseDirections.clear();
            impl_->poseTwists.clear();
            impl_->evaluationStatus =
                MultiBendTwistFalloffStatus::kInvalidRadius;
            return impl_->evaluationStatus;
        }
        if (sample.sourceQuaternions.size() != impl_->sources.size()) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->normalizedAxes.clear();
            impl_->poseDirections.clear();
            impl_->poseTwists.clear();
            impl_->evaluationStatus =
                MultiBendTwistFalloffStatus::kIncompletePose;
            return impl_->evaluationStatus;
        }

        std::vector<MVector> directions;
        std::vector<double> twists;
        directions.reserve(impl_->sources.size());
        twists.reserve(impl_->sources.size());
        for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
            if (
                sample.sourceQuaternions[index].logicalIndex
                != impl_->sources[index].logicalIndex
            ) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->normalizedAxes.clear();
                impl_->poseDirections.clear();
                impl_->poseTwists.clear();
                impl_->evaluationStatus =
                    MultiBendTwistFalloffStatus::kIncompletePose;
                return impl_->evaluationStatus;
            }

            MVector direction(1.0, 0.0, 0.0);
            double twist = 0.0;
            if (impl_->sources[index].influence > 0.0) {
                MQuaternion normalizedPose;
                if (!normalizeQuaternion(
                        sample.sourceQuaternions[index].quaternion,
                        normalizedPose
                    )) {
                    impl_->sources.clear();
                    impl_->samples.clear();
                    impl_->normalizedAxes.clear();
                    impl_->poseDirections.clear();
                    impl_->poseTwists.clear();
                    impl_->evaluationStatus =
                        MultiBendTwistFalloffStatus::kInvalidQuaternion;
                    return impl_->evaluationStatus;
                }
                const BendTwistComponents components = decomposeBendTwist(
                    normalizedPose,
                    impl_->normalizedAxes[index],
                    impl_->sources[index].order
                );
                if (!areFinite(components) || !bendDirection(
                        components,
                        direction
                    )) {
                    impl_->sources.clear();
                    impl_->samples.clear();
                    impl_->normalizedAxes.clear();
                    impl_->poseDirections.clear();
                    impl_->poseTwists.clear();
                    impl_->evaluationStatus =
                        MultiBendTwistFalloffStatus::kNumericalFailure;
                    return impl_->evaluationStatus;
                }
                twist = components.twist;
            }
            directions.push_back(direction);
            twists.push_back(twist);
        }
        impl_->poseDirections.push_back(std::move(directions));
        impl_->poseTwists.push_back(std::move(twists));
    }

    impl_->mode = mode;
    impl_->falloff = falloff;
    impl_->evaluationStatus = MultiBendTwistFalloffStatus::kSuccess;
    return impl_->evaluationStatus;
}

MultiBendTwistFalloffStatus MultiBendTwistFalloffEvaluator::evaluate(
    const std::vector<IndexedQuaternion>& inputQuaternions,
    std::vector<BendTwistFalloffWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->evaluationStatus != MultiBendTwistFalloffStatus::kSuccess) {
        return impl_->evaluationStatus;
    }
    if (inputQuaternions.size() != impl_->sources.size()) {
        return MultiBendTwistFalloffStatus::kIncompletePose;
    }

    std::vector<MVector> inputDirections;
    std::vector<double> inputTwists;
    inputDirections.reserve(inputQuaternions.size());
    inputTwists.reserve(inputQuaternions.size());
    for (std::size_t index = 0; index < inputQuaternions.size(); ++index) {
        if (
            inputQuaternions[index].logicalIndex
            != impl_->sources[index].logicalIndex
        ) {
            return MultiBendTwistFalloffStatus::kIncompletePose;
        }

        MVector direction(1.0, 0.0, 0.0);
        double twist = 0.0;
        if (impl_->sources[index].influence > 0.0) {
            MQuaternion normalizedInput;
            if (!normalizeQuaternion(
                    inputQuaternions[index].quaternion,
                    normalizedInput
                )) {
                return MultiBendTwistFalloffStatus::kInvalidQuaternion;
            }
            const BendTwistComponents components = decomposeBendTwist(
                normalizedInput,
                impl_->normalizedAxes[index],
                impl_->sources[index].order
            );
            if (!areFinite(components) || !bendDirection(
                    components,
                    direction
                )) {
                return MultiBendTwistFalloffStatus::kNumericalFailure;
            }
            twist = components.twist;
        }
        inputDirections.push_back(direction);
        inputTwists.push_back(twist);
    }

    outputWeights.reserve(impl_->samples.size());
    for (std::size_t poseIndex = 0; poseIndex < impl_->samples.size(); ++poseIndex) {
        double weightedSquaredBendDistance = 0.0;
        double weightedSquaredTwistDistance = 0.0;
        for (std::size_t sourceIndex = 0; sourceIndex < impl_->sources.size(); ++sourceIndex) {
            const double sourceInfluence =
                impl_->sources[sourceIndex].influence;
            if (sourceInfluence <= 0.0) {
                continue;
            }

            const double bendDistance = directionDistance(
                inputDirections[sourceIndex],
                impl_->poseDirections[poseIndex][sourceIndex]
            );
            if (!std::isfinite(bendDistance)) {
                outputWeights.clear();
                return MultiBendTwistFalloffStatus::kNumericalFailure;
            }
            weightedSquaredBendDistance +=
                sourceInfluence * bendDistance * bendDistance;

            if (impl_->mode == BendTwistFalloffMode::kBendTwist) {
                const double twistDistance = std::abs(shortestAngleDelta(
                    inputTwists[sourceIndex],
                    impl_->poseTwists[poseIndex][sourceIndex]
                ));
                if (!std::isfinite(twistDistance)) {
                    outputWeights.clear();
                    return MultiBendTwistFalloffStatus::kNumericalFailure;
                }
                weightedSquaredTwistDistance +=
                    sourceInfluence * twistDistance * twistDistance;
            }
        }

        const double bendDistance = std::sqrt(
            weightedSquaredBendDistance / impl_->influenceSum
        );
        if (!std::isfinite(bendDistance)) {
            outputWeights.clear();
            return MultiBendTwistFalloffStatus::kNumericalFailure;
        }
        const MultiBendTwistFalloffSample& sample =
            impl_->samples[poseIndex];
        double weight = evaluateFalloffWeight(
            impl_->falloff,
            bendDistance,
            sample.bendInnerRadiusRadians,
            sample.bendOuterRadiusRadians
        );

        if (impl_->mode == BendTwistFalloffMode::kBendTwist) {
            const double twistDistance = std::sqrt(
                weightedSquaredTwistDistance / impl_->influenceSum
            );
            if (!std::isfinite(twistDistance)) {
                outputWeights.clear();
                return MultiBendTwistFalloffStatus::kNumericalFailure;
            }
            weight *= evaluateFalloffWeight(
                impl_->falloff,
                twistDistance,
                sample.twistInnerRadiusRadians,
                sample.twistOuterRadiusRadians
            );
        }

        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return MultiBendTwistFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return MultiBendTwistFalloffStatus::kSuccess;
}

MultiBendTwistFalloffStatus MultiBendTwistFalloffEvaluator::status() const {
    return impl_->evaluationStatus;
}

}  // namespace bd_util_nodes
