#include "bdUtilNodes/nodes/BdRbfOrientationWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
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
#include "bdUtilNodes/math/RbfInterpolator.h"

const MString BdRbfOrientationWeightNode::typeName("bdRbf_OrientationWeight");
const MTypeId BdRbfOrientationWeightNode::typeId(0x00142713);

MObject BdRbfOrientationWeightNode::inputQuat;
MObject BdRbfOrientationWeightNode::inputQuatX;
MObject BdRbfOrientationWeightNode::inputQuatY;
MObject BdRbfOrientationWeightNode::inputQuatZ;
MObject BdRbfOrientationWeightNode::inputQuatW;

MObject BdRbfOrientationWeightNode::pose;
MObject BdRbfOrientationWeightNode::poseQuat;
MObject BdRbfOrientationWeightNode::poseQuatX;
MObject BdRbfOrientationWeightNode::poseQuatY;
MObject BdRbfOrientationWeightNode::poseQuatZ;
MObject BdRbfOrientationWeightNode::poseQuatW;
MObject BdRbfOrientationWeightNode::enabled;

MObject BdRbfOrientationWeightNode::kernel;
MObject BdRbfOrientationWeightNode::radius;
MObject BdRbfOrientationWeightNode::regularization;
MObject BdRbfOrientationWeightNode::allowNegativeWeights;

MObject BdRbfOrientationWeightNode::outputWeight;
MObject BdRbfOrientationWeightNode::isValid;
MObject BdRbfOrientationWeightNode::solveStatus;

namespace {

bool haveSameSamples(
    const std::vector<bd_util_nodes::QuaternionPoseSample>& first,
    const std::vector<bd_util_nodes::QuaternionPoseSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t index = 0; index < first.size(); ++index) {
        if (
            first[index].logicalIndex != second[index].logicalIndex
            || first[index].quaternion != second[index].quaternion
        ) {
            return false;
        }
    }
    return true;
}

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

struct BdRbfOrientationWeightNode::Cache {
    bd_util_nodes::RbfSolveStatus evaluate(
        const std::vector<bd_util_nodes::QuaternionPoseSample>& samples,
        bd_util_nodes::RbfKernel requestedKernel,
        double requestedRadiusRadians,
        double requestedRegularization,
        const std::array<double, 4>& inputQuaternion,
        std::vector<bd_util_nodes::IndexedWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSamples(configuredSamples, samples)
            || kernel != requestedKernel
            || radiusRadians != requestedRadiusRadians
            || regularization != requestedRegularization
        ) {
            configuredSamples = samples;
            kernel = requestedKernel;
            radiusRadians = requestedRadiusRadians;
            regularization = requestedRegularization;
            configureStatus = interpolator.configure(
                configuredSamples,
                kernel,
                radiusRadians,
                regularization
            );
            configured = true;
        }

        outputWeights.clear();
        if (configureStatus != bd_util_nodes::RbfSolveStatus::kSuccess) {
            return configureStatus;
        }
        return interpolator.evaluate(inputQuaternion, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::QuaternionPoseSample> configuredSamples;
    bd_util_nodes::RbfKernel kernel = bd_util_nodes::RbfKernel::kQuintic;
    double radiusRadians = 0.0;
    double regularization = 1.0e-8;
    bd_util_nodes::RbfSolveStatus configureStatus =
        bd_util_nodes::RbfSolveStatus::kNoPoses;
    bd_util_nodes::QuaternionRbfInterpolator interpolator;
};

BdRbfOrientationWeightNode::BdRbfOrientationWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfOrientationWeightNode::~BdRbfOrientationWeightNode() = default;

void* BdRbfOrientationWeightNode::creator() {
    return new BdRbfOrientationWeightNode();
}

MStatus BdRbfOrientationWeightNode::initialize() {
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

    MFnCompoundAttribute compoundAttributeFn;
    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {poseQuat, enabled}) {
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

    kernel = enumAttributeFn.create("kernel", "k", 4, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 5>{
             {{"Gaussian", static_cast<short>(0)},
              {"Exponential", static_cast<short>(1)},
              {"Linear", static_cast<short>(2)},
              {"CompactCubic", static_cast<short>(3)},
              {"CompactQuintic", static_cast<short>(4)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureInputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(kernel);
    if (!status) {
        return status;
    }

    const double defaultRadius = MAngle(60.0, MAngle::kDegrees).asRadians();
    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        radius,
        "radius",
        "rad",
        defaultRadius
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(radius);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        regularization,
        "regularization",
        "reg",
        1.0e-8
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
    status = numericAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = addAttribute(regularization);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        allowNegativeWeights,
        "allowNegativeWeights",
        "anw",
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
    status = addAttribute(allowNegativeWeights);
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

    solveStatus = enumAttributeFn.create("solveStatus", "ss", 1, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 9>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidRegularization", static_cast<short>(3)},
              {"InvalidQuaternion", static_cast<short>(4)},
              {"DuplicatePose", static_cast<short>(5)},
              {"RankDeficient", static_cast<short>(6)},
              {"NumericalFailure", static_cast<short>(7)},
              {"UnsupportedKernel", static_cast<short>(8)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureOutputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(solveStatus);
    if (!status) {
        return status;
    }

    const std::array<MObject, 16> inputs = {
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        pose,
        poseQuat,
        poseQuatX,
        poseQuatY,
        poseQuatZ,
        poseQuatW,
        enabled,
        kernel,
        radius,
        regularization,
        allowNegativeWeights,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {
                 outputWeight,
                 isValid,
                 solveStatus,
             }) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdRbfOrientationWeightNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputWeight
        && requestedAttribute != isValid
        && requestedAttribute != solveStatus
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(inputQuat, &status);
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();
    const std::array<double, 4> inputQuaternion = {
        inputValue[0],
        inputValue[1],
        inputValue[2],
        inputValue[3],
    };

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::QuaternionPoseSample> enabledSamples;
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
            const double4& poseValue = poseHandle.child(poseQuat).asDouble4();
            enabledSamples.push_back({
                logicalIndex,
                {
                    poseValue[0],
                    poseValue[1],
                    poseValue[2],
                    poseValue[3],
                },
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

    const short kernelValue = dataBlock.inputValue(kernel, &status).asShort();
    if (!status) {
        return status;
    }
    const double radiusRadians = dataBlock.inputValue(radius, &status)
        .asAngle()
        .asRadians();
    if (!status) {
        return status;
    }
    const double regularizationValue = dataBlock.inputValue(
        regularization,
        &status
    ).asDouble();
    if (!status) {
        return status;
    }
    const bool allowNegative = dataBlock.inputValue(
        allowNegativeWeights,
        &status
    ).asBool();
    if (!status) {
        return status;
    }

    std::vector<bd_util_nodes::IndexedWeight> solvedWeights;
    const bd_util_nodes::RbfSolveStatus resultStatus = cache_->evaluate(
        enabledSamples,
        static_cast<bd_util_nodes::RbfKernel>(kernelValue),
        radiusRadians,
        regularizationValue,
        inputQuaternion,
        solvedWeights
    );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (resultStatus == bd_util_nodes::RbfSolveStatus::kSuccess) {
        weightByIndex.reserve(solvedWeights.size());
        for (const bd_util_nodes::IndexedWeight& solvedWeight : solvedWeights) {
            weightByIndex.emplace(
                solvedWeight.logicalIndex,
                allowNegative
                    ? solvedWeight.weight
                    : std::max(0.0, solvedWeight.weight)
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
        resultStatus == bd_util_nodes::RbfSolveStatus::kSuccess
    );
    isValidHandle.setClean();

    MDataHandle solveStatusHandle = dataBlock.outputValue(
        solveStatus,
        &status
    );
    if (!status) {
        return status;
    }
    solveStatusHandle.setShort(static_cast<short>(resultStatus));
    solveStatusHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdRbfOrientationWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
