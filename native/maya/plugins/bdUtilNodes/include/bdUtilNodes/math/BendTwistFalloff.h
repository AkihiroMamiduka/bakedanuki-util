#pragma once

#include <array>
#include <memory>
#include <vector>

#include "bdUtilNodes/math/BendTwist.h"
#include "bdUtilNodes/math/Falloff.h"
#include "bdUtilNodes/math/RbfInterpolator.h"

namespace bd_util_nodes {

enum class BendTwistFalloffMode : short {
    kBendTwist = 0,
    kBendOnly = 1,
};

enum class BendTwistFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kUnsupportedMode = 5,
    kUnsupportedOrder = 6,
    kNumericalFailure = 7,
};

struct BendTwistFalloffSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 0.0};
    double bendInnerRadiusRadians = 0.0;
    double bendOuterRadiusRadians = 1.0;
    double twistInnerRadiusRadians = 0.0;
    double twistOuterRadiusRadians = 1.0;
};

struct BendTwistFalloffWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

BendTwistFalloffStatus evaluateBendTwistFalloff(
    const std::array<double, 4>& inputQuaternion,
    const std::array<double, 4>& axisQuaternion,
    const std::vector<BendTwistFalloffSample>& samples,
    BendTwistOrder order,
    BendTwistFalloffMode mode,
    Falloff falloff,
    std::vector<BendTwistFalloffWeight>& outputWeights
);

enum class MultiBendTwistFalloffStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidQuaternion = 3,
    kUnsupportedFalloff = 4,
    kUnsupportedMode = 5,
    kUnsupportedOrder = 6,
    kNumericalFailure = 7,
    kNoSources = 8,
    kInvalidInfluence = 9,
    kIncompletePose = 10,
};

struct MultiBendTwistFalloffSourceDefinition {
    unsigned int logicalIndex = 0;
    std::array<double, 4> axisQuaternion = {0.0, 0.0, 0.0, 1.0};
    BendTwistOrder order = BendTwistOrder::kTwistBend;
    double influence = 1.0;
};

struct MultiBendTwistFalloffSample {
    unsigned int logicalIndex = 0;
    std::vector<IndexedQuaternion> sourceQuaternions;
    double bendInnerRadiusRadians = 0.0;
    double bendOuterRadiusRadians = 1.0;
    double twistInnerRadiusRadians = 0.0;
    double twistOuterRadiusRadians = 1.0;
};

class MultiBendTwistFalloffEvaluator final {
public:
    MultiBendTwistFalloffEvaluator();
    ~MultiBendTwistFalloffEvaluator();

    MultiBendTwistFalloffEvaluator(
        MultiBendTwistFalloffEvaluator&&
    ) noexcept;
    MultiBendTwistFalloffEvaluator& operator=(
        MultiBendTwistFalloffEvaluator&&
    ) noexcept;

    MultiBendTwistFalloffEvaluator(
        const MultiBendTwistFalloffEvaluator&
    ) = delete;
    MultiBendTwistFalloffEvaluator& operator=(
        const MultiBendTwistFalloffEvaluator&
    ) = delete;

    MultiBendTwistFalloffStatus configure(
        const std::vector<MultiBendTwistFalloffSourceDefinition>& sources,
        const std::vector<MultiBendTwistFalloffSample>& samples,
        BendTwistFalloffMode mode,
        Falloff falloff
    );

    MultiBendTwistFalloffStatus evaluate(
        const std::vector<IndexedQuaternion>& inputQuaternions,
        std::vector<BendTwistFalloffWeight>& outputWeights
    ) const;

    MultiBendTwistFalloffStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace bd_util_nodes
