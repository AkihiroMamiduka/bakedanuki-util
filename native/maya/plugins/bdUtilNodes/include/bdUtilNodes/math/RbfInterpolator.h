#pragma once

#include <array>
#include <memory>
#include <vector>

namespace bd_util_nodes {

enum class RbfKernel : short {
    kGaussian = 0,
    kExponential = 1,
    kLinear = 2,
    kCubic = 3,
    kQuintic = 4,
};

enum class RbfSolveStatus : short {
    kSuccess = 0,
    kNoPoses = 1,
    kInvalidRadius = 2,
    kInvalidRegularization = 3,
    kInvalidQuaternion = 4,
    kDuplicatePose = 5,
    kRankDeficient = 6,
    kNumericalFailure = 7,
    kUnsupportedKernel = 8,
    kInvalidPosition = 9,
    kNoSources = 10,
    kInvalidInfluence = 11,
    kIncompletePose = 12,
};

struct QuaternionPoseSample {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 1.0};
};

struct PositionPoseSample {
    unsigned int logicalIndex = 0;
    std::array<double, 3> position = {0.0, 0.0, 0.0};
};

struct QuaternionSourceDefinition {
    unsigned int logicalIndex = 0;
    double influence = 1.0;
};

struct IndexedQuaternion {
    unsigned int logicalIndex = 0;
    std::array<double, 4> quaternion = {0.0, 0.0, 0.0, 1.0};
};

struct MultiQuaternionPoseSample {
    unsigned int logicalIndex = 0;
    std::vector<IndexedQuaternion> sourceQuaternions;
};

struct IndexedWeight {
    unsigned int logicalIndex = 0;
    double weight = 0.0;
};

class QuaternionRbfInterpolator final {
public:
    QuaternionRbfInterpolator();
    ~QuaternionRbfInterpolator();

    QuaternionRbfInterpolator(QuaternionRbfInterpolator&&) noexcept;
    QuaternionRbfInterpolator& operator=(
        QuaternionRbfInterpolator&&
    ) noexcept;

    QuaternionRbfInterpolator(const QuaternionRbfInterpolator&) = delete;
    QuaternionRbfInterpolator& operator=(
        const QuaternionRbfInterpolator&
    ) = delete;

    RbfSolveStatus configure(
        const std::vector<QuaternionPoseSample>& samples,
        RbfKernel kernel,
        double radiusRadians,
        double regularization
    );

    RbfSolveStatus evaluate(
        const std::array<double, 4>& inputQuaternion,
        std::vector<IndexedWeight>& outputWeights
    ) const;

    RbfSolveStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

class MultiQuaternionRbfInterpolator final {
public:
    MultiQuaternionRbfInterpolator();
    ~MultiQuaternionRbfInterpolator();

    MultiQuaternionRbfInterpolator(
        MultiQuaternionRbfInterpolator&&
    ) noexcept;
    MultiQuaternionRbfInterpolator& operator=(
        MultiQuaternionRbfInterpolator&&
    ) noexcept;

    MultiQuaternionRbfInterpolator(
        const MultiQuaternionRbfInterpolator&
    ) = delete;
    MultiQuaternionRbfInterpolator& operator=(
        const MultiQuaternionRbfInterpolator&
    ) = delete;

    RbfSolveStatus configure(
        const std::vector<QuaternionSourceDefinition>& sources,
        const std::vector<MultiQuaternionPoseSample>& samples,
        RbfKernel kernel,
        double radiusRadians,
        double regularization
    );

    RbfSolveStatus evaluate(
        const std::vector<IndexedQuaternion>& inputQuaternions,
        std::vector<IndexedWeight>& outputWeights
    ) const;

    RbfSolveStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

class PositionRbfInterpolator final {
public:
    PositionRbfInterpolator();
    ~PositionRbfInterpolator();

    PositionRbfInterpolator(PositionRbfInterpolator&&) noexcept;
    PositionRbfInterpolator& operator=(PositionRbfInterpolator&&) noexcept;

    PositionRbfInterpolator(const PositionRbfInterpolator&) = delete;
    PositionRbfInterpolator& operator=(const PositionRbfInterpolator&) =
        delete;

    RbfSolveStatus configure(
        const std::vector<PositionPoseSample>& samples,
        RbfKernel kernel,
        double radius,
        double regularization
    );

    RbfSolveStatus evaluate(
        const std::array<double, 3>& inputPosition,
        std::vector<IndexedWeight>& outputWeights
    ) const;

    RbfSolveStatus status() const;

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace bd_util_nodes
