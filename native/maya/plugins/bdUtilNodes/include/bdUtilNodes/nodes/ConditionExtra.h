#pragma once

#include <algorithm>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataHandle.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

#include "bdUtilNodes/math/Comparison.h"
#include "bdUtilNodes/math/Logic.h"

namespace bd_util_nodes {

inline MStatus evaluateExtraConditions(
    MArrayDataHandle& extraHandles,
    double inputValue,
    const MObject& logicAttribute,
    const MObject& comparisonAttribute,
    const MObject& compareValueAttribute,
    bool& result
) {
    MStatus status;
    const unsigned int elementCount = extraHandles.elementCount(&status);
    if (!status) {
        return status;
    }

    std::vector<unsigned int> logicalIndices;
    logicalIndices.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        logicalIndices.push_back(extraHandles.elementIndex(&status));
        if (!status) {
            return status;
        }

        if (index + 1 < elementCount) {
            status = extraHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(logicalIndices.begin(), logicalIndices.end());

    for (const unsigned int logicalIndex : logicalIndices) {
        status = extraHandles.jumpToElement(logicalIndex);
        if (!status) {
            return status;
        }
        MDataHandle extraHandle = extraHandles.inputValue(&status);
        if (!status) {
            return status;
        }

        const bool current = evaluateComparison(
            inputValue,
            extraHandle.child(comparisonAttribute).asShort(),
            extraHandle.child(compareValueAttribute).asDouble()
        );
        result = evaluateLogic(
            result,
            extraHandle.child(logicAttribute).asShort(),
            current
        );
    }
    return MS::kSuccess;
}

}  // namespace bd_util_nodes
