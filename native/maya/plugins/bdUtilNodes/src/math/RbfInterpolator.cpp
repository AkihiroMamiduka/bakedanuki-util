#include "bdUtilNodes/math/RbfInterpolator.h"

#include <algorithm>
#include <cmath>
#include <limits>
#include <utility>

#include <Eigen/Core>
#include <Eigen/QR>

namespace {

constexpr double kQuaternionEpsilon = 1.0e-12;
constexpr double kDuplicateAngleEpsilon = 1.0e-8;
constexpr double kDuplicatePositionEpsilon = 1.0e-10;

using Quaternion = std::array<double, 4>;
using Position = std::array<double, 3>;

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

double quaternionDistance(const Quaternion& first, const Quaternion& second) {
    const double dot = std::abs(
        first[0] * second[0] + first[1] * second[1]
        + first[2] * second[2] + first[3] * second[3]
    );
    return 2.0 * std::acos(std::clamp(dot, 0.0, 1.0));
}

bool isFinitePosition(const Position& position) {
    return std::isfinite(position[0]) && std::isfinite(position[1])
        && std::isfinite(position[2]);
}

double positionDistance(const Position& first, const Position& second) {
    return std::hypot(
        first[0] - second[0],
        first[1] - second[1],
        first[2] - second[2]
    );
}

bool isSupportedKernel(bd_util_nodes::RbfKernel kernel) {
    using bd_util_nodes::RbfKernel;
    return kernel == RbfKernel::kGaussian
        || kernel == RbfKernel::kExponential
        || kernel == RbfKernel::kLinear
        || kernel == RbfKernel::kCubic
        || kernel == RbfKernel::kQuintic;
}

double evaluateKernel(bd_util_nodes::RbfKernel kernel, double value) {
    using bd_util_nodes::RbfKernel;
    switch (kernel) {
        case RbfKernel::kGaussian:
            return std::exp(-(value * value));
        case RbfKernel::kExponential:
            return std::exp(-value);
        case RbfKernel::kLinear:
            return value < 1.0 ? 1.0 - value : 0.0;
        case RbfKernel::kCubic:
            if (value >= 1.0) {
                return 0.0;
            }
            return 1.0 - 3.0 * value * value
                + 2.0 * value * value * value;
        case RbfKernel::kQuintic:
            if (value >= 1.0) {
                return 0.0;
            }
            return 1.0 - 10.0 * std::pow(value, 3.0)
                + 15.0 * std::pow(value, 4.0)
                - 6.0 * std::pow(value, 5.0);
    }
    return std::numeric_limits<double>::quiet_NaN();
}

}  // namespace

namespace bd_util_nodes {

struct QuaternionRbfInterpolator::Impl {
    std::vector<QuaternionPoseSample> samples;
    std::vector<Quaternion> normalizedQuaternions;
    RbfKernel kernel = RbfKernel::kGaussian;
    double radiusRadians = 1.0;
    Eigen::ColPivHouseholderQR<Eigen::MatrixXd> decomposition;
    RbfSolveStatus solveStatus = RbfSolveStatus::kNoPoses;
};

QuaternionRbfInterpolator::QuaternionRbfInterpolator()
    : impl_(std::make_unique<Impl>()) {}

QuaternionRbfInterpolator::~QuaternionRbfInterpolator() = default;

QuaternionRbfInterpolator::QuaternionRbfInterpolator(
    QuaternionRbfInterpolator&&
) noexcept = default;

QuaternionRbfInterpolator& QuaternionRbfInterpolator::operator=(
    QuaternionRbfInterpolator&&
) noexcept = default;

RbfSolveStatus QuaternionRbfInterpolator::configure(
    const std::vector<QuaternionPoseSample>& samples,
    RbfKernel kernel,
    double radiusRadians,
    double regularization
) {
    impl_->samples.clear();
    impl_->normalizedQuaternions.clear();

    if (samples.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoPoses;
        return impl_->solveStatus;
    }
    if (!isSupportedKernel(kernel)) {
        impl_->solveStatus = RbfSolveStatus::kUnsupportedKernel;
        return impl_->solveStatus;
    }
    if (!std::isfinite(radiusRadians) || radiusRadians <= 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRadius;
        return impl_->solveStatus;
    }
    if (!std::isfinite(regularization) || regularization < 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRegularization;
        return impl_->solveStatus;
    }

    impl_->samples = samples;
    impl_->normalizedQuaternions.reserve(samples.size());
    for (const QuaternionPoseSample& sample : samples) {
        Quaternion normalized;
        if (!normalizeQuaternion(sample.quaternion, normalized)) {
            impl_->samples.clear();
            impl_->normalizedQuaternions.clear();
            impl_->solveStatus = RbfSolveStatus::kInvalidQuaternion;
            return impl_->solveStatus;
        }
        impl_->normalizedQuaternions.push_back(normalized);
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(samples.size());
    Eigen::MatrixXd matrix(sampleCount, sampleCount);
    for (Eigen::Index row = 0; row < sampleCount; ++row) {
        for (Eigen::Index column = 0; column < sampleCount; ++column) {
            const double distance = quaternionDistance(
                impl_->normalizedQuaternions[static_cast<std::size_t>(row)],
                impl_->normalizedQuaternions[static_cast<std::size_t>(column)]
            );
            if (row != column && distance <= kDuplicateAngleEpsilon) {
                impl_->samples.clear();
                impl_->normalizedQuaternions.clear();
                impl_->solveStatus = RbfSolveStatus::kDuplicatePose;
                return impl_->solveStatus;
            }
            matrix(row, column) = evaluateKernel(kernel, distance / radiusRadians);
        }
        matrix(row, row) += regularization;
    }

    if (!matrix.allFinite()) {
        impl_->samples.clear();
        impl_->normalizedQuaternions.clear();
        impl_->solveStatus = RbfSolveStatus::kNumericalFailure;
        return impl_->solveStatus;
    }

    impl_->decomposition.compute(matrix);
    if (impl_->decomposition.rank() != sampleCount) {
        impl_->samples.clear();
        impl_->normalizedQuaternions.clear();
        impl_->solveStatus = RbfSolveStatus::kRankDeficient;
        return impl_->solveStatus;
    }

    impl_->kernel = kernel;
    impl_->radiusRadians = radiusRadians;
    impl_->solveStatus = RbfSolveStatus::kSuccess;
    return impl_->solveStatus;
}

RbfSolveStatus QuaternionRbfInterpolator::evaluate(
    const std::array<double, 4>& inputQuaternion,
    std::vector<IndexedWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->solveStatus != RbfSolveStatus::kSuccess) {
        return impl_->solveStatus;
    }

    Quaternion normalizedInput;
    if (!normalizeQuaternion(inputQuaternion, normalizedInput)) {
        return RbfSolveStatus::kInvalidQuaternion;
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(
        impl_->samples.size()
    );
    Eigen::VectorXd kernelVector(sampleCount);
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        const double distance = quaternionDistance(
            normalizedInput,
            impl_->normalizedQuaternions[static_cast<std::size_t>(index)]
        );
        kernelVector(index) = evaluateKernel(
            impl_->kernel,
            distance / impl_->radiusRadians
        );
    }

    if (!kernelVector.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }
    const Eigen::VectorXd weights = impl_->decomposition.solve(kernelVector);
    if (!weights.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }

    outputWeights.reserve(impl_->samples.size());
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        outputWeights.push_back({
            impl_->samples[static_cast<std::size_t>(index)].logicalIndex,
            weights(index),
        });
    }
    return RbfSolveStatus::kSuccess;
}

RbfSolveStatus QuaternionRbfInterpolator::status() const {
    return impl_->solveStatus;
}

struct MultiQuaternionRbfInterpolator::Impl {
    std::vector<QuaternionSourceDefinition> sources;
    std::vector<MultiQuaternionPoseSample> samples;
    std::vector<std::vector<Quaternion>> normalizedPoseQuaternions;
    RbfKernel kernel = RbfKernel::kGaussian;
    double radiusRadians = 1.0;
    double influenceSum = 0.0;
    Eigen::ColPivHouseholderQR<Eigen::MatrixXd> decomposition;
    RbfSolveStatus solveStatus = RbfSolveStatus::kNoSources;
};

namespace {

bool sourceDefinitionsAreValid(
    const std::vector<QuaternionSourceDefinition>& sources,
    double& influenceSum
) {
    influenceSum = 0.0;
    for (std::size_t index = 0; index < sources.size(); ++index) {
        const QuaternionSourceDefinition& source = sources[index];
        if (
            !std::isfinite(source.influence) || source.influence < 0.0
            || (
                index > 0
                && sources[index - 1].logicalIndex >= source.logicalIndex
            )
        ) {
            return false;
        }
        influenceSum += source.influence;
    }
    return std::isfinite(influenceSum) && influenceSum > 0.0;
}

bool normalizeMultiQuaternionPose(
    const MultiQuaternionPoseSample& sample,
    const std::vector<QuaternionSourceDefinition>& sources,
    std::vector<Quaternion>& normalizedQuaternions,
    RbfSolveStatus& status
) {
    if (sample.sourceQuaternions.size() != sources.size()) {
        status = RbfSolveStatus::kIncompletePose;
        return false;
    }

    normalizedQuaternions.clear();
    normalizedQuaternions.reserve(sources.size());
    for (std::size_t index = 0; index < sources.size(); ++index) {
        if (
            sample.sourceQuaternions[index].logicalIndex
            != sources[index].logicalIndex
        ) {
            status = RbfSolveStatus::kIncompletePose;
            return false;
        }
        Quaternion normalized = {0.0, 0.0, 0.0, 1.0};
        if (
            sources[index].influence > 0.0
            && !normalizeQuaternion(
                sample.sourceQuaternions[index].quaternion,
                normalized
            )
        ) {
            status = RbfSolveStatus::kInvalidQuaternion;
            return false;
        }
        normalizedQuaternions.push_back(normalized);
    }
    return true;
}

double multiQuaternionDistance(
    const std::vector<Quaternion>& first,
    const std::vector<Quaternion>& second,
    const std::vector<QuaternionSourceDefinition>& sources,
    double influenceSum
) {
    double weightedSquaredDistance = 0.0;
    for (std::size_t index = 0; index < sources.size(); ++index) {
        if (sources[index].influence <= 0.0) {
            continue;
        }
        const double distance = quaternionDistance(
            first[index],
            second[index]
        );
        weightedSquaredDistance += sources[index].influence
            * distance * distance;
    }
    return std::sqrt(weightedSquaredDistance / influenceSum);
}

}  // namespace

MultiQuaternionRbfInterpolator::MultiQuaternionRbfInterpolator()
    : impl_(std::make_unique<Impl>()) {}

MultiQuaternionRbfInterpolator::~MultiQuaternionRbfInterpolator() = default;

MultiQuaternionRbfInterpolator::MultiQuaternionRbfInterpolator(
    MultiQuaternionRbfInterpolator&&
) noexcept = default;

MultiQuaternionRbfInterpolator&
MultiQuaternionRbfInterpolator::operator=(
    MultiQuaternionRbfInterpolator&&
) noexcept = default;

RbfSolveStatus MultiQuaternionRbfInterpolator::configure(
    const std::vector<QuaternionSourceDefinition>& sources,
    const std::vector<MultiQuaternionPoseSample>& samples,
    RbfKernel kernel,
    double radiusRadians,
    double regularization
) {
    impl_->sources.clear();
    impl_->samples.clear();
    impl_->normalizedPoseQuaternions.clear();

    if (sources.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoSources;
        return impl_->solveStatus;
    }
    if (samples.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoPoses;
        return impl_->solveStatus;
    }
    if (!isSupportedKernel(kernel)) {
        impl_->solveStatus = RbfSolveStatus::kUnsupportedKernel;
        return impl_->solveStatus;
    }
    if (!std::isfinite(radiusRadians) || radiusRadians <= 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRadius;
        return impl_->solveStatus;
    }
    if (!std::isfinite(regularization) || regularization < 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRegularization;
        return impl_->solveStatus;
    }

    impl_->sources = sources;
    if (!sourceDefinitionsAreValid(
            impl_->sources,
            impl_->influenceSum
        )) {
        impl_->sources.clear();
        impl_->solveStatus = RbfSolveStatus::kInvalidInfluence;
        return impl_->solveStatus;
    }

    impl_->samples = samples;
    impl_->normalizedPoseQuaternions.reserve(samples.size());
    for (const MultiQuaternionPoseSample& sample : samples) {
        std::vector<Quaternion> normalizedQuaternions;
        RbfSolveStatus sampleStatus = RbfSolveStatus::kSuccess;
        if (!normalizeMultiQuaternionPose(
                sample,
                impl_->sources,
                normalizedQuaternions,
                sampleStatus
            )) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->normalizedPoseQuaternions.clear();
            impl_->solveStatus = sampleStatus;
            return impl_->solveStatus;
        }
        impl_->normalizedPoseQuaternions.push_back(
            std::move(normalizedQuaternions)
        );
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(samples.size());
    Eigen::MatrixXd matrix(sampleCount, sampleCount);
    for (Eigen::Index row = 0; row < sampleCount; ++row) {
        for (Eigen::Index column = 0; column < sampleCount; ++column) {
            const double distance = multiQuaternionDistance(
                impl_->normalizedPoseQuaternions[
                    static_cast<std::size_t>(row)
                ],
                impl_->normalizedPoseQuaternions[
                    static_cast<std::size_t>(column)
                ],
                impl_->sources,
                impl_->influenceSum
            );
            if (row != column && distance <= kDuplicateAngleEpsilon) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->normalizedPoseQuaternions.clear();
                impl_->solveStatus = RbfSolveStatus::kDuplicatePose;
                return impl_->solveStatus;
            }
            matrix(row, column) = evaluateKernel(
                kernel,
                distance / radiusRadians
            );
        }
        matrix(row, row) += regularization;
    }

    if (!matrix.allFinite()) {
        impl_->sources.clear();
        impl_->samples.clear();
        impl_->normalizedPoseQuaternions.clear();
        impl_->solveStatus = RbfSolveStatus::kNumericalFailure;
        return impl_->solveStatus;
    }

    impl_->decomposition.compute(matrix);
    if (impl_->decomposition.rank() != sampleCount) {
        impl_->sources.clear();
        impl_->samples.clear();
        impl_->normalizedPoseQuaternions.clear();
        impl_->solveStatus = RbfSolveStatus::kRankDeficient;
        return impl_->solveStatus;
    }

    impl_->kernel = kernel;
    impl_->radiusRadians = radiusRadians;
    impl_->solveStatus = RbfSolveStatus::kSuccess;
    return impl_->solveStatus;
}

RbfSolveStatus MultiQuaternionRbfInterpolator::evaluate(
    const std::vector<IndexedQuaternion>& inputQuaternions,
    std::vector<IndexedWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->solveStatus != RbfSolveStatus::kSuccess) {
        return impl_->solveStatus;
    }
    if (inputQuaternions.size() != impl_->sources.size()) {
        return RbfSolveStatus::kIncompletePose;
    }

    std::vector<Quaternion> normalizedInputs;
    normalizedInputs.reserve(inputQuaternions.size());
    for (std::size_t index = 0; index < inputQuaternions.size(); ++index) {
        if (
            inputQuaternions[index].logicalIndex
            != impl_->sources[index].logicalIndex
        ) {
            return RbfSolveStatus::kIncompletePose;
        }
        Quaternion normalized = {0.0, 0.0, 0.0, 1.0};
        if (
            impl_->sources[index].influence > 0.0
            && !normalizeQuaternion(
                inputQuaternions[index].quaternion,
                normalized
            )
        ) {
            return RbfSolveStatus::kInvalidQuaternion;
        }
        normalizedInputs.push_back(normalized);
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(
        impl_->samples.size()
    );
    Eigen::VectorXd kernelVector(sampleCount);
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        const double distance = multiQuaternionDistance(
            normalizedInputs,
            impl_->normalizedPoseQuaternions[
                static_cast<std::size_t>(index)
            ],
            impl_->sources,
            impl_->influenceSum
        );
        kernelVector(index) = evaluateKernel(
            impl_->kernel,
            distance / impl_->radiusRadians
        );
    }

    if (!kernelVector.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }
    const Eigen::VectorXd weights = impl_->decomposition.solve(kernelVector);
    if (!weights.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }

    outputWeights.reserve(impl_->samples.size());
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        outputWeights.push_back({
            impl_->samples[static_cast<std::size_t>(index)].logicalIndex,
            weights(index),
        });
    }
    return RbfSolveStatus::kSuccess;
}

RbfSolveStatus MultiQuaternionRbfInterpolator::status() const {
    return impl_->solveStatus;
}

struct PositionRbfInterpolator::Impl {
    std::vector<PositionPoseSample> samples;
    RbfKernel kernel = RbfKernel::kGaussian;
    double radius = 1.0;
    Eigen::ColPivHouseholderQR<Eigen::MatrixXd> decomposition;
    RbfSolveStatus solveStatus = RbfSolveStatus::kNoPoses;
};

PositionRbfInterpolator::PositionRbfInterpolator()
    : impl_(std::make_unique<Impl>()) {}

PositionRbfInterpolator::~PositionRbfInterpolator() = default;

PositionRbfInterpolator::PositionRbfInterpolator(
    PositionRbfInterpolator&&
) noexcept = default;

PositionRbfInterpolator& PositionRbfInterpolator::operator=(
    PositionRbfInterpolator&&
) noexcept = default;

RbfSolveStatus PositionRbfInterpolator::configure(
    const std::vector<PositionPoseSample>& samples,
    RbfKernel kernel,
    double radius,
    double regularization
) {
    impl_->samples.clear();

    if (samples.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoPoses;
        return impl_->solveStatus;
    }
    if (!isSupportedKernel(kernel)) {
        impl_->solveStatus = RbfSolveStatus::kUnsupportedKernel;
        return impl_->solveStatus;
    }
    if (!std::isfinite(radius) || radius <= 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRadius;
        return impl_->solveStatus;
    }
    if (!std::isfinite(regularization) || regularization < 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRegularization;
        return impl_->solveStatus;
    }

    impl_->samples = samples;
    for (const PositionPoseSample& sample : samples) {
        if (!isFinitePosition(sample.position)) {
            impl_->samples.clear();
            impl_->solveStatus = RbfSolveStatus::kInvalidPosition;
            return impl_->solveStatus;
        }
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(samples.size());
    Eigen::MatrixXd matrix(sampleCount, sampleCount);
    for (Eigen::Index row = 0; row < sampleCount; ++row) {
        for (Eigen::Index column = 0; column < sampleCount; ++column) {
            const double distance = positionDistance(
                samples[static_cast<std::size_t>(row)].position,
                samples[static_cast<std::size_t>(column)].position
            );
            if (row != column && distance <= kDuplicatePositionEpsilon) {
                impl_->samples.clear();
                impl_->solveStatus = RbfSolveStatus::kDuplicatePose;
                return impl_->solveStatus;
            }
            matrix(row, column) = evaluateKernel(kernel, distance / radius);
        }
        matrix(row, row) += regularization;
    }

    if (!matrix.allFinite()) {
        impl_->samples.clear();
        impl_->solveStatus = RbfSolveStatus::kNumericalFailure;
        return impl_->solveStatus;
    }

    impl_->decomposition.compute(matrix);
    if (impl_->decomposition.rank() != sampleCount) {
        impl_->samples.clear();
        impl_->solveStatus = RbfSolveStatus::kRankDeficient;
        return impl_->solveStatus;
    }

    impl_->kernel = kernel;
    impl_->radius = radius;
    impl_->solveStatus = RbfSolveStatus::kSuccess;
    return impl_->solveStatus;
}

RbfSolveStatus PositionRbfInterpolator::evaluate(
    const std::array<double, 3>& inputPosition,
    std::vector<IndexedWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->solveStatus != RbfSolveStatus::kSuccess) {
        return impl_->solveStatus;
    }
    if (!isFinitePosition(inputPosition)) {
        return RbfSolveStatus::kInvalidPosition;
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(
        impl_->samples.size()
    );
    Eigen::VectorXd kernelVector(sampleCount);
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        const double distance = positionDistance(
            inputPosition,
            impl_->samples[static_cast<std::size_t>(index)].position
        );
        kernelVector(index) = evaluateKernel(
            impl_->kernel,
            distance / impl_->radius
        );
    }

    if (!kernelVector.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }
    const Eigen::VectorXd weights = impl_->decomposition.solve(kernelVector);
    if (!weights.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }

    outputWeights.reserve(impl_->samples.size());
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        outputWeights.push_back({
            impl_->samples[static_cast<std::size_t>(index)].logicalIndex,
            weights(index),
        });
    }
    return RbfSolveStatus::kSuccess;
}

RbfSolveStatus PositionRbfInterpolator::status() const {
    return impl_->solveStatus;
}

struct MultiPositionRbfInterpolator::Impl {
    std::vector<PositionSourceDefinition> sources;
    std::vector<MultiPositionPoseSample> samples;
    std::vector<std::vector<std::array<double, 3>>> posePositions;
    RbfKernel kernel = RbfKernel::kGaussian;
    double radius = 1.0;
    double influenceSum = 0.0;
    Eigen::ColPivHouseholderQR<Eigen::MatrixXd> decomposition;
    RbfSolveStatus solveStatus = RbfSolveStatus::kNoSources;
};

namespace {

bool positionSourceDefinitionsAreValid(
    const std::vector<PositionSourceDefinition>& sources,
    double& influenceSum
) {
    influenceSum = 0.0;
    for (std::size_t index = 0; index < sources.size(); ++index) {
        const PositionSourceDefinition& source = sources[index];
        if (
            !std::isfinite(source.influence) || source.influence < 0.0
            || (
                index > 0
                && sources[index - 1].logicalIndex >= source.logicalIndex
            )
        ) {
            return false;
        }
        influenceSum += source.influence;
    }
    return std::isfinite(influenceSum) && influenceSum > 0.0;
}

bool validateMultiPositionPose(
    const MultiPositionPoseSample& sample,
    const std::vector<PositionSourceDefinition>& sources,
    std::vector<std::array<double, 3>>& positions,
    RbfSolveStatus& status
) {
    if (sample.sourcePositions.size() != sources.size()) {
        status = RbfSolveStatus::kIncompletePose;
        return false;
    }

    positions.clear();
    positions.reserve(sources.size());
    for (std::size_t index = 0; index < sources.size(); ++index) {
        if (
            sample.sourcePositions[index].logicalIndex
            != sources[index].logicalIndex
        ) {
            status = RbfSolveStatus::kIncompletePose;
            return false;
        }
        std::array<double, 3> position = {0.0, 0.0, 0.0};
        if (sources[index].influence > 0.0) {
            position = sample.sourcePositions[index].position;
            if (!isFinitePosition(position)) {
                status = RbfSolveStatus::kInvalidPosition;
                return false;
            }
        }
        positions.push_back(position);
    }
    return true;
}

double multiPositionDistance(
    const std::vector<std::array<double, 3>>& first,
    const std::vector<std::array<double, 3>>& second,
    const std::vector<PositionSourceDefinition>& sources,
    double influenceSum
) {
    double weightedSquaredDistance = 0.0;
    for (std::size_t index = 0; index < sources.size(); ++index) {
        if (sources[index].influence <= 0.0) {
            continue;
        }
        const double distance = positionDistance(first[index], second[index]);
        weightedSquaredDistance += sources[index].influence
            * distance * distance;
    }
    return std::sqrt(weightedSquaredDistance / influenceSum);
}

}  // namespace

MultiPositionRbfInterpolator::MultiPositionRbfInterpolator()
    : impl_(std::make_unique<Impl>()) {}

MultiPositionRbfInterpolator::~MultiPositionRbfInterpolator() = default;

MultiPositionRbfInterpolator::MultiPositionRbfInterpolator(
    MultiPositionRbfInterpolator&&
) noexcept = default;

MultiPositionRbfInterpolator& MultiPositionRbfInterpolator::operator=(
    MultiPositionRbfInterpolator&&
) noexcept = default;

RbfSolveStatus MultiPositionRbfInterpolator::configure(
    const std::vector<PositionSourceDefinition>& sources,
    const std::vector<MultiPositionPoseSample>& samples,
    RbfKernel kernel,
    double radius,
    double regularization
) {
    impl_->sources.clear();
    impl_->samples.clear();
    impl_->posePositions.clear();

    if (sources.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoSources;
        return impl_->solveStatus;
    }
    if (samples.empty()) {
        impl_->solveStatus = RbfSolveStatus::kNoPoses;
        return impl_->solveStatus;
    }
    if (!isSupportedKernel(kernel)) {
        impl_->solveStatus = RbfSolveStatus::kUnsupportedKernel;
        return impl_->solveStatus;
    }
    if (!std::isfinite(radius) || radius <= 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRadius;
        return impl_->solveStatus;
    }
    if (!std::isfinite(regularization) || regularization < 0.0) {
        impl_->solveStatus = RbfSolveStatus::kInvalidRegularization;
        return impl_->solveStatus;
    }

    impl_->sources = sources;
    if (!positionSourceDefinitionsAreValid(
            impl_->sources,
            impl_->influenceSum
        )) {
        impl_->sources.clear();
        impl_->solveStatus = RbfSolveStatus::kInvalidInfluence;
        return impl_->solveStatus;
    }

    impl_->samples = samples;
    impl_->posePositions.reserve(samples.size());
    for (const MultiPositionPoseSample& sample : samples) {
        std::vector<std::array<double, 3>> positions;
        RbfSolveStatus sampleStatus = RbfSolveStatus::kSuccess;
        if (!validateMultiPositionPose(
                sample,
                impl_->sources,
                positions,
                sampleStatus
            )) {
            impl_->sources.clear();
            impl_->samples.clear();
            impl_->posePositions.clear();
            impl_->solveStatus = sampleStatus;
            return impl_->solveStatus;
        }
        impl_->posePositions.push_back(std::move(positions));
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(samples.size());
    Eigen::MatrixXd matrix(sampleCount, sampleCount);
    for (Eigen::Index row = 0; row < sampleCount; ++row) {
        for (Eigen::Index column = 0; column < sampleCount; ++column) {
            const double distance = multiPositionDistance(
                impl_->posePositions[static_cast<std::size_t>(row)],
                impl_->posePositions[static_cast<std::size_t>(column)],
                impl_->sources,
                impl_->influenceSum
            );
            if (row != column && distance <= kDuplicatePositionEpsilon) {
                impl_->sources.clear();
                impl_->samples.clear();
                impl_->posePositions.clear();
                impl_->solveStatus = RbfSolveStatus::kDuplicatePose;
                return impl_->solveStatus;
            }
            matrix(row, column) = evaluateKernel(kernel, distance / radius);
        }
        matrix(row, row) += regularization;
    }

    if (!matrix.allFinite()) {
        impl_->sources.clear();
        impl_->samples.clear();
        impl_->posePositions.clear();
        impl_->solveStatus = RbfSolveStatus::kNumericalFailure;
        return impl_->solveStatus;
    }

    impl_->decomposition.compute(matrix);
    if (impl_->decomposition.rank() != sampleCount) {
        impl_->sources.clear();
        impl_->samples.clear();
        impl_->posePositions.clear();
        impl_->solveStatus = RbfSolveStatus::kRankDeficient;
        return impl_->solveStatus;
    }

    impl_->kernel = kernel;
    impl_->radius = radius;
    impl_->solveStatus = RbfSolveStatus::kSuccess;
    return impl_->solveStatus;
}

RbfSolveStatus MultiPositionRbfInterpolator::evaluate(
    const std::vector<IndexedPosition>& inputPositions,
    std::vector<IndexedWeight>& outputWeights
) const {
    outputWeights.clear();
    if (impl_->solveStatus != RbfSolveStatus::kSuccess) {
        return impl_->solveStatus;
    }
    if (inputPositions.size() != impl_->sources.size()) {
        return RbfSolveStatus::kIncompletePose;
    }

    std::vector<std::array<double, 3>> validatedInputs;
    validatedInputs.reserve(inputPositions.size());
    for (std::size_t index = 0; index < inputPositions.size(); ++index) {
        if (
            inputPositions[index].logicalIndex
            != impl_->sources[index].logicalIndex
        ) {
            return RbfSolveStatus::kIncompletePose;
        }
        std::array<double, 3> position = {0.0, 0.0, 0.0};
        if (impl_->sources[index].influence > 0.0) {
            position = inputPositions[index].position;
            if (!isFinitePosition(position)) {
                return RbfSolveStatus::kInvalidPosition;
            }
        }
        validatedInputs.push_back(position);
    }

    const Eigen::Index sampleCount = static_cast<Eigen::Index>(
        impl_->samples.size()
    );
    Eigen::VectorXd kernelVector(sampleCount);
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        const double distance = multiPositionDistance(
            validatedInputs,
            impl_->posePositions[static_cast<std::size_t>(index)],
            impl_->sources,
            impl_->influenceSum
        );
        kernelVector(index) = evaluateKernel(
            impl_->kernel,
            distance / impl_->radius
        );
    }

    if (!kernelVector.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }
    const Eigen::VectorXd weights = impl_->decomposition.solve(kernelVector);
    if (!weights.allFinite()) {
        return RbfSolveStatus::kNumericalFailure;
    }

    outputWeights.reserve(impl_->samples.size());
    for (Eigen::Index index = 0; index < sampleCount; ++index) {
        outputWeights.push_back({
            impl_->samples[static_cast<std::size_t>(index)].logicalIndex,
            weights(index),
        });
    }
    return RbfSolveStatus::kSuccess;
}

RbfSolveStatus MultiPositionRbfInterpolator::status() const {
    return impl_->solveStatus;
}

}  // namespace bd_util_nodes
