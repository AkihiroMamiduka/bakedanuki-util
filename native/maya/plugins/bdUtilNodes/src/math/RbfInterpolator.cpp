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

double quaternionDistance(const Quaternion& first, const Quaternion& second) {
    const double dot = std::abs(
        first[0] * second[0] + first[1] * second[1]
        + first[2] * second[2] + first[3] * second[3]
    );
    return 2.0 * std::acos(std::clamp(dot, 0.0, 1.0));
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

}  // namespace bd_util_nodes

