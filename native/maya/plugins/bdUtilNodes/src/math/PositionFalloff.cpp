#include "bdUtilNodes/math/PositionFalloff.h"

#include <cmath>

namespace {

using Position = std::array<double, 3>;

bool isFinitePosition(const Position& position) {
    return std::isfinite(position[0]) && std::isfinite(position[1])
        && std::isfinite(position[2]);
}

}  // namespace

namespace bd_util_nodes {

PositionFalloffStatus evaluatePositionFalloff(
    const std::array<double, 3>& inputPosition,
    const std::vector<PositionFalloffSample>& samples,
    Falloff falloff,
    std::vector<PositionFalloffWeight>& outputWeights
) {
    outputWeights.clear();
    if (samples.empty()) {
        return PositionFalloffStatus::kNoPoses;
    }
    if (!isSupportedFalloff(falloff)) {
        return PositionFalloffStatus::kUnsupportedFalloff;
    }
    if (!isFinitePosition(inputPosition)) {
        return PositionFalloffStatus::kInvalidPosition;
    }

    outputWeights.reserve(samples.size());
    for (const PositionFalloffSample& sample : samples) {
        if (!isFinitePosition(sample.position)) {
            outputWeights.clear();
            return PositionFalloffStatus::kInvalidPosition;
        }
        if (!isValidFalloffRadius(
                sample.innerRadius,
                sample.outerRadius
            )) {
            outputWeights.clear();
            return PositionFalloffStatus::kInvalidRadius;
        }

        const double distance = std::hypot(
            inputPosition[0] - sample.position[0],
            inputPosition[1] - sample.position[1],
            inputPosition[2] - sample.position[2]
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return PositionFalloffStatus::kNumericalFailure;
        }

        const double weight = evaluateFalloffWeight(
            falloff,
            distance,
            sample.innerRadius,
            sample.outerRadius
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return PositionFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return PositionFalloffStatus::kSuccess;
}

struct MultiPositionFalloffEvaluator::Impl {
    std::vector<PositionSourceDefinition> sources;
    std::vector<MultiPositionFalloffSample> samples;
    Falloff falloff = Falloff::kQuintic;
    double influenceSum = 0.0;
    MultiPositionFalloffStatus evaluationStatus =
        MultiPositionFalloffStatus::kNoSources;
};

MultiPositionFalloffEvaluator::MultiPositionFalloffEvaluator()
    : impl_(std::make_unique<Impl>()) {}

MultiPositionFalloffEvaluator::~MultiPositionFalloffEvaluator() = default;

MultiPositionFalloffEvaluator::MultiPositionFalloffEvaluator(
    MultiPositionFalloffEvaluator&&
) noexcept = default;

MultiPositionFalloffEvaluator& MultiPositionFalloffEvaluator::operator=(
    MultiPositionFalloffEvaluator&&
) noexcept = default;

MultiPositionFalloffStatus MultiPositionFalloffEvaluator::configure(
    const std::vector<PositionSourceDefinition>& sources,
    const std::vector<MultiPositionFalloffSample>& samples,
    Falloff falloff
) {
    impl_->sources.clear();
    impl_->samples.clear();
    impl_->influenceSum = 0.0;

    if (sources.empty()) {
        impl_->evaluationStatus = MultiPositionFalloffStatus::kNoSources;
        return impl_->evaluationStatus;
    }
    if (samples.empty()) {
        impl_->evaluationStatus = MultiPositionFalloffStatus::kNoPoses;
        return impl_->evaluationStatus;
    }
    if (!isSupportedFalloff(falloff)) {
        impl_->evaluationStatus =
            MultiPositionFalloffStatus::kUnsupportedFalloff;
        return impl_->evaluationStatus;
    }

    impl_->sources = sources;
    for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
        const PositionSourceDefinition& source = impl_->sources[index];
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
                MultiPositionFalloffStatus::kInvalidInfluence;
            return impl_->evaluationStatus;
        }
        impl_->influenceSum += source.influence;
    }
    if (!std::isfinite(impl_->influenceSum) || impl_->influenceSum <= 0.0) {
        impl_->sources.clear();
        impl_->evaluationStatus =
            MultiPositionFalloffStatus::kInvalidInfluence;
        return impl_->evaluationStatus;
    }

    impl_->samples = samples;
    for (const MultiPositionFalloffSample& sample : samples) {
        if (!isValidFalloffRadius(sample.innerRadius, sample.outerRadius)) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->evaluationStatus =
                MultiPositionFalloffStatus::kInvalidRadius;
            return impl_->evaluationStatus;
        }
        if (sample.sourcePositions.size() != impl_->sources.size()) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->evaluationStatus =
                MultiPositionFalloffStatus::kIncompletePose;
            return impl_->evaluationStatus;
        }
        for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
            if (
                sample.sourcePositions[index].logicalIndex
                != impl_->sources[index].logicalIndex
            ) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->evaluationStatus =
                    MultiPositionFalloffStatus::kIncompletePose;
                return impl_->evaluationStatus;
            }
            if (
                impl_->sources[index].influence > 0.0
                && !isFinitePosition(sample.sourcePositions[index].position)
            ) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->evaluationStatus =
                    MultiPositionFalloffStatus::kInvalidPosition;
                return impl_->evaluationStatus;
            }
        }
    }

    impl_->falloff = falloff;
    impl_->evaluationStatus = MultiPositionFalloffStatus::kSuccess;
    return impl_->evaluationStatus;
}

MultiPositionFalloffStatus MultiPositionFalloffEvaluator::evaluate(
    const std::vector<IndexedPosition>& inputPositions,
    std::vector<PositionFalloffWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->evaluationStatus != MultiPositionFalloffStatus::kSuccess) {
        return impl_->evaluationStatus;
    }
    if (inputPositions.size() != impl_->sources.size()) {
        return MultiPositionFalloffStatus::kIncompletePose;
    }
    for (std::size_t index = 0; index < inputPositions.size(); ++index) {
        if (
            inputPositions[index].logicalIndex
            != impl_->sources[index].logicalIndex
        ) {
            return MultiPositionFalloffStatus::kIncompletePose;
        }
        if (
            impl_->sources[index].influence > 0.0
            && !isFinitePosition(inputPositions[index].position)
        ) {
            return MultiPositionFalloffStatus::kInvalidPosition;
        }
    }

    outputWeights.reserve(impl_->samples.size());
    for (const MultiPositionFalloffSample& sample : impl_->samples) {
        double weightedSquaredDistance = 0.0;
        for (std::size_t index = 0; index < impl_->sources.size(); ++index) {
            if (impl_->sources[index].influence <= 0.0) {
                continue;
            }
            const double distance = std::hypot(
                inputPositions[index].position[0]
                    - sample.sourcePositions[index].position[0],
                inputPositions[index].position[1]
                    - sample.sourcePositions[index].position[1],
                inputPositions[index].position[2]
                    - sample.sourcePositions[index].position[2]
            );
            weightedSquaredDistance +=
                impl_->sources[index].influence * distance * distance;
        }
        const double distance = std::sqrt(
            weightedSquaredDistance / impl_->influenceSum
        );
        if (!std::isfinite(distance)) {
            outputWeights.clear();
            return MultiPositionFalloffStatus::kNumericalFailure;
        }
        const double weight = evaluateFalloffWeight(
            impl_->falloff,
            distance,
            sample.innerRadius,
            sample.outerRadius
        );
        if (!std::isfinite(weight)) {
            outputWeights.clear();
            return MultiPositionFalloffStatus::kNumericalFailure;
        }
        outputWeights.push_back({
            sample.logicalIndex,
            std::clamp(weight, 0.0, 1.0),
        });
    }
    return MultiPositionFalloffStatus::kSuccess;
}

MultiPositionFalloffStatus MultiPositionFalloffEvaluator::status() const {
    return impl_->evaluationStatus;
}

}  // namespace bd_util_nodes
