#include "bdUtilNodes/nodes/BdRbfPositionFalloffWeightNode.h"

#include <algorithm>
#include <array>
#include <unordered_map>
#include <vector>

#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MDistance.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/PositionFalloff.h"

const MString BdRbfPositionFalloffWeightNode::typeName(
    "bdRbf_PositionFalloffWeight"
);
const MTypeId BdRbfPositionFalloffWeightNode::typeId(0x00142716);

MObject BdRbfPositionFalloffWeightNode::inputPosition;
MObject BdRbfPositionFalloffWeightNode::inputPositionX;
MObject BdRbfPositionFalloffWeightNode::inputPositionY;
MObject BdRbfPositionFalloffWeightNode::inputPositionZ;

MObject BdRbfPositionFalloffWeightNode::innerRadius;
MObject BdRbfPositionFalloffWeightNode::outerRadius;
MObject BdRbfPositionFalloffWeightNode::falloff;

MObject BdRbfPositionFalloffWeightNode::pose;
MObject BdRbfPositionFalloffWeightNode::posePosition;
MObject BdRbfPositionFalloffWeightNode::posePositionX;
MObject BdRbfPositionFalloffWeightNode::posePositionY;
MObject BdRbfPositionFalloffWeightNode::posePositionZ;
MObject BdRbfPositionFalloffWeightNode::enabled;
MObject BdRbfPositionFalloffWeightNode::useRadiusOverride;
MObject BdRbfPositionFalloffWeightNode::innerRadiusOverride;
MObject BdRbfPositionFalloffWeightNode::outerRadiusOverride;

MObject BdRbfPositionFalloffWeightNode::outputWeight;
MObject BdRbfPositionFalloffWeightNode::isValid;
MObject BdRbfPositionFalloffWeightNode::falloffStatus;

namespace {

MStatus configureInputEnumAttribute(MFnEnumAttribute& attributeFn) {
    MStatus status = attributeFn.setReadable(true);
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

MStatus configureOutputEnumAttribute(MFnEnumAttribute& attributeFn) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = attributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    return attributeFn.setKeyable(false);
}

}  // namespace

void* BdRbfPositionFalloffWeightNode::creator() {
    return new BdRbfPositionFalloffWeightNode();
}

MStatus BdRbfPositionFalloffWeightNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        "inputPosition",
        "ip",
        "inputPositionX",
        "ipx",
        "inputPositionY",
        "ipy",
        "inputPositionZ",
        "ipz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(inputPosition);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        innerRadius,
        "innerRadius",
        "inr",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = addAttribute(innerRadius);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        outerRadius,
        "outerRadius",
        "outr",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = addAttribute(outerRadius);
    if (!status) {
        return status;
    }

    falloff = enumAttributeFn.create("falloff", "fo", 2, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 3>{
             {{"Linear", static_cast<short>(0)},
              {"CompactCubic", static_cast<short>(1)},
              {"CompactQuintic", static_cast<short>(2)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureInputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(falloff);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        posePosition,
        posePositionX,
        posePositionY,
        posePositionZ,
        "position",
        "pp",
        "positionX",
        "ppx",
        "positionY",
        "ppy",
        "positionZ",
        "ppz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        enabled,
        "enabled",
        "en",
        true
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        useRadiusOverride,
        "useRadiusOverride",
        "uro",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        innerRadiusOverride,
        "innerRadiusOverride",
        "iro",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        outerRadiusOverride,
        "outerRadiusOverride",
        "oro",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    MFnCompoundAttribute compoundAttributeFn;
    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             posePosition,
             enabled,
             useRadiusOverride,
             innerRadiusOverride,
             outerRadiusOverride,
         }) {
        status = compoundAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
    }
    status = compoundAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    status = addAttribute(pose);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        outputWeight,
        "outputWeight",
        "ow",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setUsesArrayDataBuilder(true);
    if (!status) {
        return status;
    }
    status = addAttribute(outputWeight);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        isValid,
        "isValid",
        "iv",
        false
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(isValid);
    if (!status) {
        return status;
    }

    falloffStatus = enumAttributeFn.create(
        "falloffStatus",
        "fs",
        1,
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 6>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidPosition", static_cast<short>(3)},
              {"UnsupportedFalloff", static_cast<short>(4)},
              {"NumericalFailure", static_cast<short>(5)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureOutputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(falloffStatus);
    if (!status) {
        return status;
    }

    const std::array<MObject, 16> inputs = {
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        innerRadius,
        outerRadius,
        falloff,
        pose,
        posePosition,
        posePositionX,
        posePositionY,
        posePositionZ,
        enabled,
        useRadiusOverride,
        innerRadiusOverride,
        outerRadiusOverride,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {
                 outputWeight,
                 isValid,
                 falloffStatus,
             }) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdRbfPositionFalloffWeightNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputWeight
        && requestedAttribute != isValid
        && requestedAttribute != falloffStatus
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(inputPosition, &status);
    if (!status) {
        return status;
    }
    const double3& inputValue = inputHandle.asDouble3();
    const std::array<double, 3> input = {
        inputValue[0],
        inputValue[1],
        inputValue[2],
    };

    const double defaultInnerRadius = dataBlock.inputValue(
        innerRadius,
        &status
    ).asDistance().asCentimeters();
    if (!status) {
        return status;
    }
    const double defaultOuterRadius = dataBlock.inputValue(
        outerRadius,
        &status
    ).asDistance().asCentimeters();
    if (!status) {
        return status;
    }
    const short falloffValue = dataBlock.inputValue(
        falloff,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::PositionFalloffSample> enabledSamples;
    MArrayDataHandle poseHandles = dataBlock.inputArrayValue(pose, &status);
    if (!status) {
        return status;
    }
    const unsigned int poseCount = poseHandles.elementCount(&status);
    if (!status) {
        return status;
    }
    poseIndices.reserve(poseCount);
    enabledSamples.reserve(poseCount);
    for (unsigned int index = 0; index < poseCount; ++index) {
        const unsigned int logicalIndex = poseHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        poseIndices.push_back(logicalIndex);

        MDataHandle poseHandle = poseHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        if (poseHandle.child(enabled).asBool()) {
            const double3& poseValue = poseHandle.child(
                posePosition
            ).asDouble3();
            const bool useOverride = poseHandle.child(
                useRadiusOverride
            ).asBool();
            double resolvedInnerRadius = defaultInnerRadius;
            double resolvedOuterRadius = defaultOuterRadius;
            if (useOverride) {
                resolvedInnerRadius = poseHandle.child(
                    innerRadiusOverride
                ).asDistance().asCentimeters();
                resolvedOuterRadius = poseHandle.child(
                    outerRadiusOverride
                ).asDistance().asCentimeters();
            }
            enabledSamples.push_back({
                logicalIndex,
                {poseValue[0], poseValue[1], poseValue[2]},
                resolvedInnerRadius,
                resolvedOuterRadius,
            });
        }

        if (index + 1 < poseCount) {
            status = poseHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(poseIndices.begin(), poseIndices.end());
    std::sort(
        enabledSamples.begin(),
        enabledSamples.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

    std::vector<bd_util_nodes::PositionFalloffWeight> falloffWeights;
    const bd_util_nodes::PositionFalloffStatus resultStatus =
        bd_util_nodes::evaluatePositionFalloff(
            input,
            enabledSamples,
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (resultStatus == bd_util_nodes::PositionFalloffStatus::kSuccess) {
        weightByIndex.reserve(falloffWeights.size());
        for (const auto& falloffWeight : falloffWeights) {
            weightByIndex.emplace(
                falloffWeight.logicalIndex,
                falloffWeight.weight
            );
        }
    }

    MArrayDataHandle outputHandles = dataBlock.outputArrayValue(
        outputWeight,
        &status
    );
    if (!status) {
        return status;
    }
    MArrayDataBuilder outputBuilder(
        &dataBlock,
        outputWeight,
        static_cast<unsigned int>(poseIndices.size()),
        &status
    );
    if (!status) {
        return status;
    }
    for (const unsigned int logicalIndex : poseIndices) {
        MDataHandle outputHandle = outputBuilder.addElement(
            logicalIndex,
            &status
        );
        if (!status) {
            return status;
        }
        const auto foundWeight = weightByIndex.find(logicalIndex);
        outputHandle.setDouble(
            foundWeight == weightByIndex.end() ? 0.0 : foundWeight->second
        );
    }
    status = outputHandles.set(outputBuilder);
    if (!status) {
        return status;
    }
    status = outputHandles.setAllClean();
    if (!status) {
        return status;
    }

    MDataHandle isValidHandle = dataBlock.outputValue(isValid, &status);
    if (!status) {
        return status;
    }
    isValidHandle.setBool(
        resultStatus == bd_util_nodes::PositionFalloffStatus::kSuccess
    );
    isValidHandle.setClean();

    MDataHandle statusHandle = dataBlock.outputValue(falloffStatus, &status);
    if (!status) {
        return status;
    }
    statusHandle.setShort(static_cast<short>(resultStatus));
    statusHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdRbfPositionFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
