#pragma once

#include <array>
#include <memory>
#include <vector>

#include "bdUtilNodes/math/Falloff.h"
#include "bdUtilNodes/math/RbfInterpolator.h"

namespace bd_util_nodes {

enum class PositionFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidPosition = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
};

struct PositionFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 3> position = {0.0, 0.0, 0.0};
    double innerRadius = 0.0;
    double outerRadius = 1.0;
};

struct PositionFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

PositionFalloffStatus evaluatePositionFalloff(
    const std::array<double, 3>& inputPosition,
    const std::vector<PositionFalloffSample>& samples,
    Falloff falloff,
    std::vector<PositionFalloffWeight>& outputWeights
);

enum class MultiPositionFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidPosition = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
    kNoSources = 6,
    kInvalidInfluence = 7,
    kIncompletePose = 8,
};

struct MultiPositionFalloffSample {
    unsigned int logicalIndex = 0;
    std::vector<IndexedPosition> sourcePositions;
    double innerRadius = 0.0;
    double outerRadius = 1.0;
};

class MultiPositionFalloffEvaluator final {
public:
    MultiPositionFalloffEvaluator();
    ~MultiPositionFalloffEvaluator();

    MultiPositionFalloffEvaluator(MultiPositionFalloffEvaluator&&) noexcept;
    MultiPositionFalloffEvaluator& operator=(
        MultiPositionFalloffEvaluator&&
    ) noexcept;

    MultiPositionFalloffEvaluator(const MultiPositionFalloffEvaluator&) =
        delete;
    MultiPositionFalloffEvaluator& operator=(
        const MultiPositionFalloffEvaluator&
    ) = delete;

    MultiPositionFalloffStatus configure(
        const std::vector<PositionSourceDefinition>& sources,
        const std::vector<MultiPositionFalloffSample>& samples,
        Falloff falloff
    );

    MultiPositionFalloffStatus evaluate(
        const std::vector<IndexedPosition>& inputPositions,
        std::vector<PositionFalloffWeight>& outputWeights
    ) const;

    MultiPositionFalloffStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace bd_util_nodes
