#pragma once

namespace bd_util_nodes {

enum class ComparisonOperation : short {
    kEqual = 0,
    kNotEqual = 1,
    kGreaterThan = 2,
    kGreaterOrEqual = 3,
    kLessThan = 4,
    kLessOrEqual = 5,
};

inline bool evaluateComparison(
    double input,
    short operation,
    double compare
) noexcept {
    switch (static_cast<ComparisonOperation>(operation)) {
        case ComparisonOperation::kEqual:
            return input == compare;
        case ComparisonOperation::kNotEqual:
            return input != compare;
        case ComparisonOperation::kGreaterThan:
            return input > compare;
        case ComparisonOperation::kGreaterOrEqual:
            return input >= compare;
        case ComparisonOperation::kLessThan:
            return input < compare;
        case ComparisonOperation::kLessOrEqual:
            return input <= compare;
    }
    return false;
}

}  // namespace bd_util_nodes
