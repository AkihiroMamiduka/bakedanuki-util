#include "bdUtilNodes/nodes/BdRbfMultiPositionWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
#include <unordered_map>
#include <utility>
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

const MString BdRbfMultiPositionWeightNode::typeName(
    "bdRbf_MultiPositionWeight"
);
const MTypeId BdRbfMultiPositionWeightNode::typeId(0x0014271A);

MObject BdRbfMultiPositionWeightNode::source;
MObject BdRbfMultiPositionWeightNode::inputPosition;
MObject BdRbfMultiPositionWeightNode::inputPositionX;
MObject BdRbfMultiPositionWeightNode::inputPositionY;
MObject BdRbfMultiPositionWeightNode::inputPositionZ;
MObject BdRbfMultiPositionWeightNode::influence;

MObject BdRbfMultiPositionWeightNode::pose;
MObject BdRbfMultiPositionWeightNode::sourcePosition;
MObject BdRbfMultiPositionWeightNode::sourcePositionX;
MObject BdRbfMultiPositionWeightNode::sourcePositionY;
MObject BdRbfMultiPositionWeightNode::sourcePositionZ;
MObject BdRbfMultiPositionWeightNode::enabled;

MObject BdRbfMultiPositionWeightNode::kernel;
MObject BdRbfMultiPositionWeightNode::radius;
MObject BdRbfMultiPositionWeightNode::regularization;
MObject BdRbfMultiPositionWeightNode::allowNegativeWeights;

MObject BdRbfMultiPositionWeightNode::outputWeight;
MObject BdRbfMultiPositionWeightNode::isValid;
MObject BdRbfMultiPositionWeightNode::solveStatus;

namespace {

bool haveSameSources(
    const std::vector<bd_util_nodes::PositionSourceDefinition>& first,
    const std::vector<bd_util_nodes::PositionSourceDefinition>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t index = 0; index < first.size(); ++index) {
        if (
            first[index].logicalIndex != second[index].logicalIndex
            || first[index].influence != second[index].influence
        ) {
            return false;
        }
    }
    return true;
}

bool haveSameSamples(
    const std::vector<bd_util_nodes::MultiPositionPoseSample>& first,
    const std::vector<bd_util_nodes::MultiPositionPoseSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t poseIndex = 0; poseIndex < first.size(); ++poseIndex) {
        if (
            first[poseIndex].logicalIndex != second[poseIndex].logicalIndex
            || first[poseIndex].sourcePositions.size()
                != second[poseIndex].sourcePositions.size()
        ) {
            return false;
        }
        for (
            std::size_t sourceIndex = 0;
            sourceIndex < first[poseIndex].sourcePositions.size();
            ++sourceIndex
        ) {
            const bd_util_nodes::IndexedPosition& firstPosition =
                first[poseIndex].sourcePositions[sourceIndex];
            const bd_util_nodes::IndexedPosition& secondPosition =
                second[poseIndex].sourcePositions[sourceIndex];
            if (
                firstPosition.logicalIndex != secondPosition.logicalIndex
                || firstPosition.position != secondPosition.position
            ) {
                return false;
            }
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

struct BdRbfMultiPositionWeightNode::Cache {
    bd_util_nodes::RbfSolveStatus evaluate(
        const std::vector<bd_util_nodes::PositionSourceDefinition>& sources,
        const std::vector<bd_util_nodes::MultiPositionPoseSample>& samples,
        bd_util_nodes::RbfKernel requestedKernel,
        double requestedRadius,
        double requestedRegularization,
        const std::vector<bd_util_nodes::IndexedPosition>& inputPositions,
        std::vector<bd_util_nodes::IndexedWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSources(configuredSources, sources)
            || !haveSameSamples(configuredSamples, samples)
            || kernel != requestedKernel || radius != requestedRadius
            || regularization != requestedRegularization
        ) {
            configuredSources = sources;
            configuredSamples = samples;
            kernel = requestedKernel;
            radius = requestedRadius;
            regularization = requestedRegularization;
            configureStatus = interpolator.configure(
                configuredSources,
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
        return interpolator.evaluate(inputPositions, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::PositionSourceDefinition> configuredSources;
    std::vector<bd_util_nodes::MultiPositionPoseSample> configuredSamples;
    bd_util_nodes::RbfKernel kernel = bd_util_nodes::RbfKernel::kQuintic;
    double radius = 0.0;
    double regularization = 1.0e-8;
    bd_util_nodes::RbfSolveStatus configureStatus =
        bd_util_nodes::RbfSolveStatus::kNoSources;
    bd_util_nodes::MultiPositionRbfInterpolator interpolator;
};

BdRbfMultiPositionWeightNode::BdRbfMultiPositionWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfMultiPositionWeightNode::~BdRbfMultiPositionWeightNode() = default;

void* BdRbfMultiPositionWeightNode::creator() {
    return new BdRbfMultiPositionWeightNode();
}

MStatus BdRbfMultiPositionWeightNode::initialize() {
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

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        influence,
        "influence",
        "inf",
        1.0
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

    MFnCompoundAttribute compoundAttributeFn;
    source = compoundAttributeFn.create("source", "src", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {inputPosition, influence}) {
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
    status = addAttribute(source);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        sourcePosition,
        sourcePositionX,
        sourcePositionY,
        sourcePositionZ,
        "sourcePosition",
        "sp",
        "sourcePositionX",
        "spx",
        "sourcePositionY",
        "spy",
        "sourcePositionZ",
        "spz",
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
    status = numericAttributeFn.setArray(true);
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

    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {sourcePosition, enabled}) {
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

    solveStatus = enumAttributeFn.create("solveStatus", "ss", 10, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 12>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidRegularization", static_cast<short>(3)},
              {"InvalidPosition", static_cast<short>(4)},
              {"DuplicatePose", static_cast<short>(5)},
              {"RankDeficient", static_cast<short>(6)},
              {"NumericalFailure", static_cast<short>(7)},
              {"UnsupportedKernel", static_cast<short>(8)},
              {"NoSources", static_cast<short>(10)},
              {"InvalidInfluence", static_cast<short>(11)},
              {"IncompletePose", static_cast<short>(12)}}}) {
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
        source,
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        influence,
        pose,
        sourcePosition,
        sourcePositionX,
        sourcePositionY,
        sourcePositionZ,
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

MStatus BdRbfMultiPositionWeightNode::compute(
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
    std::vector<bd_util_nodes::PositionSourceDefinition> sources;
    std::vector<bd_util_nodes::IndexedPosition> inputPositions;
    MArrayDataHandle sourceHandles = dataBlock.inputArrayValue(
        source,
        &status
    );
    if (!status) {
        return status;
    }
    const unsigned int sourceCount = sourceHandles.elementCount(&status);
    if (!status) {
        return status;
    }
    sources.reserve(sourceCount);
    inputPositions.reserve(sourceCount);
    for (unsigned int index = 0; index < sourceCount; ++index) {
        const unsigned int logicalIndex = sourceHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        MDataHandle sourceHandle = sourceHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        const double3& inputValue = sourceHandle.child(
            inputPosition
        ).asDouble3();
        sources.push_back({
            logicalIndex,
            sourceHandle.child(influence).asDouble(),
        });
        inputPositions.push_back({
            logicalIndex,
            {inputValue[0], inputValue[1], inputValue[2]},
        });

        if (index + 1 < sourceCount) {
            status = sourceHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(
        sources.begin(),
        sources.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );
    std::sort(
        inputPositions.begin(),
        inputPositions.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::MultiPositionPoseSample> enabledSamples;
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
            bd_util_nodes::MultiPositionPoseSample sample;
            sample.logicalIndex = logicalIndex;
            MArrayDataHandle sourcePositionHandles(
                poseHandle.child(sourcePosition),
                &status
            );
            if (!status) {
                return status;
            }
            const unsigned int poseSourceCount =
                sourcePositionHandles.elementCount(&status);
            if (!status) {
                return status;
            }
            sample.sourcePositions.reserve(poseSourceCount);
            for (
                unsigned int sourceIndex = 0;
                sourceIndex < poseSourceCount;
                ++sourceIndex
            ) {
                const unsigned int sourceLogicalIndex =
                    sourcePositionHandles.elementIndex(&status);
                if (!status) {
                    return status;
                }
                MDataHandle sourcePositionHandle =
                    sourcePositionHandles.inputValue(&status);
                if (!status) {
                    return status;
                }
                const double3& positionValue =
                    sourcePositionHandle.asDouble3();
                sample.sourcePositions.push_back({
                    sourceLogicalIndex,
                    {
                        positionValue[0],
                        positionValue[1],
                        positionValue[2],
                    },
                });
                if (sourceIndex + 1 < poseSourceCount) {
                    status = sourcePositionHandles.next();
                    if (!status) {
                        return status;
                    }
                }
            }
            std::sort(
                sample.sourcePositions.begin(),
                sample.sourcePositions.end(),
                [](const auto& first, const auto& second) {
                    return first.logicalIndex < second.logicalIndex;
                }
            );
            enabledSamples.push_back(std::move(sample));
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
        sources,
        enabledSamples,
        static_cast<bd_util_nodes::RbfKernel>(kernelValue),
        radiusValue,
        regularizationValue,
        inputPositions,
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

MPxNode::SchedulingType BdRbfMultiPositionWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
