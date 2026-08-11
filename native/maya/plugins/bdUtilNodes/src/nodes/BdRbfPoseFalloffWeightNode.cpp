#include "bdUtilNodes/nodes/BdRbfPoseFalloffWeightNode.h"

#include <array>
#include <unordered_map>
#include <vector>

#include <maya/MAngle.h>
#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/PoseFalloff.h"

const MString BdRbfPoseFalloffWeightNode::typeName(
    "bdRbf_PoseFalloffWeight"
);
const MTypeId BdRbfPoseFalloffWeightNode::typeId(0x0007F098);

MObject BdRbfPoseFalloffWeightNode::inputQuat;
MObject BdRbfPoseFalloffWeightNode::inputQuatX;
MObject BdRbfPoseFalloffWeightNode::inputQuatY;
MObject BdRbfPoseFalloffWeightNode::inputQuatZ;
MObject BdRbfPoseFalloffWeightNode::inputQuatW;

MObject BdRbfPoseFalloffWeightNode::innerRadius;
MObject BdRbfPoseFalloffWeightNode::outerRadius;
MObject BdRbfPoseFalloffWeightNode::falloff;

MObject BdRbfPoseFalloffWeightNode::pose;
MObject BdRbfPoseFalloffWeightNode::poseQuat;
MObject BdRbfPoseFalloffWeightNode::poseQuatX;
MObject BdRbfPoseFalloffWeightNode::poseQuatY;
MObject BdRbfPoseFalloffWeightNode::poseQuatZ;
MObject BdRbfPoseFalloffWeightNode::poseQuatW;
MObject BdRbfPoseFalloffWeightNode::enabled;
MObject BdRbfPoseFalloffWeightNode::useRadiusOverride;
MObject BdRbfPoseFalloffWeightNode::innerRadiusOverride;
MObject BdRbfPoseFalloffWeightNode::outerRadiusOverride;

MObject BdRbfPoseFalloffWeightNode::outputWeight;
MObject BdRbfPoseFalloffWeightNode::isValid;
MObject BdRbfPoseFalloffWeightNode::falloffStatus;

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

void* BdRbfPoseFalloffWeightNode::creator() {
    return new BdRbfPoseFalloffWeightNode();
}

MStatus BdRbfPoseFalloffWeightNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        "inputQuat",
        "iq",
        "inputQuatX",
        "iqx",
        "inputQuatY",
        "iqy",
        "inputQuatZ",
        "iqz",
        "inputQuatW",
        "iqw"
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
    status = addAttribute(inputQuat);
    if (!status) {
        return status;
    }

    const double defaultOuterRadius = MAngle(
        60.0,
        MAngle::kDegrees
    ).asRadians();
    status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outerRadius,
        "outerRadius",
        "outr",
        defaultOuterRadius
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

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        poseQuat,
        poseQuatX,
        poseQuatY,
        poseQuatZ,
        poseQuatW,
        "poseQuat",
        "pq",
        "poseQuatX",
        "pqx",
        "poseQuatY",
        "pqy",
        "poseQuatZ",
        "pqz",
        "poseQuatW",
        "pqw",
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

    status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outerRadiusOverride,
        "outerRadiusOverride",
        "oro",
        defaultOuterRadius
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
             poseQuat,
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
              {"InvalidQuaternion", static_cast<short>(3)},
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

    const std::array<MObject, 18> inputs = {
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        innerRadius,
        outerRadius,
        falloff,
        pose,
        poseQuat,
        poseQuatX,
        poseQuatY,
        poseQuatZ,
        poseQuatW,
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

MStatus BdRbfPoseFalloffWeightNode::compute(
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
    MDataHandle inputHandle = dataBlock.inputValue(inputQuat, &status);
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();
    const std::array<double, 4> input = {
        inputValue[0],
        inputValue[1],
        inputValue[2],
        inputValue[3],
    };

    const double defaultInnerRadius = dataBlock.inputValue(
        innerRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }
    const double defaultOuterRadius = dataBlock.inputValue(
        outerRadius,
        &status
    ).asAngle().asRadians();
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
    std::vector<bd_util_nodes::PoseFalloffSample> enabledSamples;
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
            const double4& poseValue = poseHandle.child(
                poseQuat
            ).asDouble4();
            const bool useOverride = poseHandle.child(
                useRadiusOverride
            ).asBool();
            double resolvedInnerRadius = defaultInnerRadius;
            double resolvedOuterRadius = defaultOuterRadius;
            if (useOverride) {
                resolvedInnerRadius = poseHandle.child(
                    innerRadiusOverride
                ).asAngle().asRadians();
                resolvedOuterRadius = poseHandle.child(
                    outerRadiusOverride
                ).asAngle().asRadians();
            }
            enabledSamples.push_back({
                logicalIndex,
                {
                    poseValue[0],
                    poseValue[1],
                    poseValue[2],
                    poseValue[3],
                },
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
    std::vector<bd_util_nodes::PoseFalloffWeight> falloffWeights;
    const bd_util_nodes::PoseFalloffStatus resultStatus =
        bd_util_nodes::evaluatePoseFalloff(
            input,
            enabledSamples,
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (resultStatus == bd_util_nodes::PoseFalloffStatus::kSuccess) {
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
        resultStatus == bd_util_nodes::PoseFalloffStatus::kSuccess
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
BdRbfPoseFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
