#pragma once

#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MObject.h>
#include <maya/MStatus.h>

namespace bd_util_nodes {

inline MStatus copyExtraConditionArray(
    MDataBlock& dataBlock,
    MArrayDataHandle& inputHandles,
    MArrayDataHandle& outputHandles,
    const MObject& inputLogic,
    const MObject& inputComparison,
    const MObject& inputCompareValue,
    const MObject& outputExtra,
    const MObject& outputLogic,
    const MObject& outputComparison,
    const MObject& outputCompareValue
) {
    MStatus status;
    const unsigned int elementCount = inputHandles.elementCount(&status);
    if (!status) {
        return status;
    }

    MArrayDataBuilder outputBuilder(
        &dataBlock,
        outputExtra,
        elementCount,
        &status
    );
    if (!status) {
        return status;
    }

    for (unsigned int index = 0; index < elementCount; ++index) {
        const unsigned int logicalIndex = inputHandles.elementIndex(&status);
        if (!status) {
            return status;
        }

        MDataHandle inputValue = inputHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        MDataHandle outputValue = outputBuilder.addElement(
            logicalIndex,
            &status
        );
        if (!status) {
            return status;
        }

        outputValue.child(outputLogic).setShort(
            inputValue.child(inputLogic).asShort()
        );
        outputValue.child(outputComparison).setShort(
            inputValue.child(inputComparison).asShort()
        );
        outputValue.child(outputCompareValue).setDouble(
            inputValue.child(inputCompareValue).asDouble()
        );

        if (index + 1 < elementCount) {
            status = inputHandles.next();
            if (!status) {
                return status;
            }
        }
    }

    status = outputHandles.set(outputBuilder);
    if (!status) {
        return status;
    }
    return outputHandles.setAllClean();
}

}  // namespace bd_util_nodes
