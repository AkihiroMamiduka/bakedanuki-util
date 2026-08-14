#pragma once

#include <array>
#include <memory>
#include <vector>

#include "bdUtilNodes/math/Falloff.h"
#include "bdUtilNodes/math/RbfInterpolator.h"

namespace bd_util_nodes {

enum class OrientationFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
};

struct OrientationFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 0.0};
    double innerRadiusRadians = 0.0;
    double outerRadiusRadians = 1.0;
};

struct OrientationFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

OrientationFalloffStatus evaluateOrientationFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::vector<OrientationFalloffSample>& samples,
    Falloff falloff,
    std::vector<OrientationFalloffWeight>& outputWeights
);

enum class MultiOrientationFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kNumericalFailure = 5,
    kNoSources = 6,
    kInvalidInfluence = 7,
    kIncompletePose = 8,
};

struct MultiOrientationFalloffSample {
    unsigned int logicalIndex = 0;
    std::vector<IndexedQuaternion> sourceQuaternions;
    double innerRadiusRadians = 0.0;
    double outerRadiusRadians = 1.0;
};

class MultiOrientationFalloffEvaluator final {
public:
    MultiOrientationFalloffEvaluator();
    ~MultiOrientationFalloffEvaluator();

    MultiOrientationFalloffEvaluator(
        MultiOrientationFalloffEvaluator&&
    ) noexcept;
    MultiOrientationFalloffEvaluator& operator=(
        MultiOrientationFalloffEvaluator&&
    ) noexcept;

    MultiOrientationFalloffEvaluator(
        const MultiOrientationFalloffEvaluator&
    ) = delete;
    MultiOrientationFalloffEvaluator& operator=(
        const MultiOrientationFalloffEvaluator&
    ) = delete;

    MultiOrientationFalloffStatus configure(
        const std::vector<QuaternionSourceDefinition>& sources,
        const std::vector<MultiOrientationFalloffSample>& samples,
        Falloff falloff
    );

    MultiOrientationFalloffStatus evaluate(
        const std::vector<IndexedQuaternion>& inputQuaternions,
        std::vector<OrientationFalloffWeight>& outputWeights
    ) const;

    MultiOrientationFalloffStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace bd_util_nodes
