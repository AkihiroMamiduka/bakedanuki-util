#include "bdUtilNodes/nodes/BdRbfPositionWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
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
#include "bdUtilNodes/math/RbfInterpolator.h"

const MString BdRbfPositionWeightNode::typeName("bdRbf_PositionWeight");
const MTypeId BdRbfPositionWeightNode::typeId(0x00142715);

MObject BdRbfPositionWeightNode::inputPosition;
MObject BdRbfPositionWeightNode::inputPositionX;
MObject BdRbfPositionWeightNode::inputPositionY;
MObject BdRbfPositionWeightNode::inputPositionZ;

MObject BdRbfPositionWeightNode::pose;
MObject BdRbfPositionWeightNode::posePosition;
MObject BdRbfPositionWeightNode::posePositionX;
MObject BdRbfPositionWeightNode::posePositionY;
MObject BdRbfPositionWeightNode::posePositionZ;
MObject BdRbfPositionWeightNode::enabled;

MObject BdRbfPositionWeightNode::kernel;
MObject BdRbfPositionWeightNode::radius;
MObject BdRbfPositionWeightNode::regularization;
MObject BdRbfPositionWeightNode::allowNegativeWeights;

MObject BdRbfPositionWeightNode::outputWeight;
MObject BdRbfPositionWeightNode::isValid;
MObject BdRbfPositionWeightNode::solveStatus;

namespace {

bool haveSameSamples(
    const std::vector<bd_util_nodes::PositionPoseSample>& first,
    const std::vector<bd_util_nodes::PositionPoseSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t index = 0; index < first.size(); ++index) {
        if (
            first[index].logicalIndex != second[index].logicalIndex
            || first[index].position != second[index].position
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

short positionSolveStatusValue(bd_util_nodes::RbfSolveStatus status) {
    if (status == bd_util_nodes::RbfSolveStatus::kInvalidPosition) {
        return 4;
    }
    return static_cast<short>(status);
}

}  // namespace

struct BdRbfPositionWeightNode::Cache {
    bd_util_nodes::RbfSolveStatus evaluate(
        const std::vector<bd_util_nodes::PositionPoseSample>& samples,
        bd_util_nodes::RbfKernel requestedKernel,
        double requestedRadius,
        double requestedRegularization,
        const std::array<double, 3>& currentPosition,
        std::vector<bd_util_nodes::IndexedWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSamples(configuredSamples, samples)
            || kernel != requestedKernel || radius != requestedRadius
            || regularization != requestedRegularization
        ) {
            configuredSamples = samples;
            kernel = requestedKernel;
            radius = requestedRadius;
            regularization = requestedRegularization;
            configureStatus = interpolator.configure(
                configuredSamples,
                kernel,
                radius,
                regularization
            );
            configured = true;
        }

        outputWeights.clear();
        if (configureStatus != bd_util_nodes::RbfSolveStatus::kSuccess) {
            return configureStatus;
        }
        return interpolator.evaluate(currentPosition, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::PositionPoseSample> configuredSamples;
    bd_util_nodes::RbfKernel kernel = bd_util_nodes::RbfKernel::kQuintic;
    double radius = 0.0;
    double regularization = 1.0e-8;
    bd_util_nodes::RbfSolveStatus configureStatus =
        bd_util_nodes::RbfSolveStatus::kNoPoses;
    bd_util_nodes::PositionRbfInterpolator interpolator;
};

BdRbfPositionWeightNode::BdRbfPositionWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfPositionWeightNode::~BdRbfPositionWeightNode() = default;

void* BdRbfPositionWeightNode::creator() {
    return new BdRbfPositionWeightNode();
}

MStatus BdRbfPositionWeightNode::initialize() {
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

    MFnCompoundAttribute compoundAttributeFn;
    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {posePosition, enabled}) {
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        radius,
        "radius",
        "rad",
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
              {"InvalidPosition", static_cast<short>(4)},
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

    const std::array<MObject, 14> inputs = {
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        pose,
        posePosition,
        posePositionX,
        posePositionY,
        posePositionZ,
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

MStatus BdRbfPositionWeightNode::compute(
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

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::PositionPoseSample> enabledSamples;
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
            enabledSamples.push_back({
                logicalIndex,
                {poseValue[0], poseValue[1], poseValue[2]},
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
    const double radiusValue = dataBlock.inputValue(radius, &status)
        .asDistance()
        .asCentimeters();
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
        radiusValue,
        regularizationValue,
        input,
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
    solveStatusHandle.setShort(positionSolveStatusValue(resultStatus));
    solveStatusHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdRbfPositionWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
