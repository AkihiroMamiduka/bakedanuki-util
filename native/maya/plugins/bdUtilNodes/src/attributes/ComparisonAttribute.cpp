#include "bdUtilNodes/attributes/ComparisonAttribute.h"

#include <maya/MFnEnumAttribute.h>
#include <maya/MString.h>

#include "bdUtilNodes/math/Comparison.h"

namespace bd_util_nodes {

MStatus createComparisonOperationAttribute(
    MFnEnumAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    attribute = attributeFn.create(
        MString(longName),
        MString(shortName),
        static_cast<short>(ComparisonOperation::kEqual),
        &status
    );
    if (!status) {
        return status;
    }

    const struct {
        const char* label;
        ComparisonOperation operation;
    } fields[] = {
        {"Equal", ComparisonOperation::kEqual},
        {"Not Equal", ComparisonOperation::kNotEqual},
        {"Greater Than", ComparisonOperation::kGreaterThan},
        {"Greater or Equal", ComparisonOperation::kGreaterOrEqual},
        {"Less Than", ComparisonOperation::kLessThan},
        {"Less or Equal", ComparisonOperation::kLessOrEqual},
    };

    for (const auto& field : fields) {
        status = attributeFn.addField(
            MString(field.label),
            static_cast<short>(field.operation)
        );
        if (!status) {
            return status;
        }
    }

    status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    return attributeFn.setKeyable(true);
}

}  // namespace bd_util_nodes
