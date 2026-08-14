#include "bdUtilNodes/nodes/BdRbfMultiOrientationWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
#include <unordered_map>
#include <utility>
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

const MString BdRbfMultiOrientationWeightNode::typeName(
    "bdRbf_MultiOrientationWeight"
);
const MTypeId BdRbfMultiOrientationWeightNode::typeId(0x00142719);

MObject BdRbfMultiOrientationWeightNode::source;
MObject BdRbfMultiOrientationWeightNode::inputQuat;
MObject BdRbfMultiOrientationWeightNode::inputQuatX;
MObject BdRbfMultiOrientationWeightNode::inputQuatY;
MObject BdRbfMultiOrientationWeightNode::inputQuatZ;
MObject BdRbfMultiOrientationWeightNode::inputQuatW;
MObject BdRbfMultiOrientationWeightNode::influence;

MObject BdRbfMultiOrientationWeightNode::pose;
MObject BdRbfMultiOrientationWeightNode::sourceQuat;
MObject BdRbfMultiOrientationWeightNode::sourceQuatX;
MObject BdRbfMultiOrientationWeightNode::sourceQuatY;
MObject BdRbfMultiOrientationWeightNode::sourceQuatZ;
MObject BdRbfMultiOrientationWeightNode::sourceQuatW;
MObject BdRbfMultiOrientationWeightNode::enabled;

MObject BdRbfMultiOrientationWeightNode::kernel;
MObject BdRbfMultiOrientationWeightNode::radius;
MObject BdRbfMultiOrientationWeightNode::regularization;
MObject BdRbfMultiOrientationWeightNode::allowNegativeWeights;

MObject BdRbfMultiOrientationWeightNode::outputWeight;
MObject BdRbfMultiOrientationWeightNode::isValid;
MObject BdRbfMultiOrientationWeightNode::solveStatus;

namespace {

bool haveSameSources(
    const std::vector<bd_util_nodes::QuaternionSourceDefinition>& first,
    const std::vector<bd_util_nodes::QuaternionSourceDefinition>& second
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
    const std::vector<bd_util_nodes::MultiQuaternionPoseSample>& first,
    const std::vector<bd_util_nodes::MultiQuaternionPoseSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t poseIndex = 0; poseIndex < first.size(); ++poseIndex) {
        if (
            first[poseIndex].logicalIndex != second[poseIndex].logicalIndex
            || first[poseIndex].sourceQuaternions.size()
                != second[poseIndex].sourceQuaternions.size()
        ) {
            return false;
        }
        for (
            std::size_t sourceIndex = 0;
            sourceIndex < first[poseIndex].sourceQuaternions.size();
            ++sourceIndex
        ) {
            const bd_util_nodes::IndexedQuaternion& firstQuaternion =
                first[poseIndex].sourceQuaternions[sourceIndex];
            const bd_util_nodes::IndexedQuaternion& secondQuaternion =
                second[poseIndex].sourceQuaternions[sourceIndex];
            if (
                firstQuaternion.logicalIndex
                    != secondQuaternion.logicalIndex
                || firstQuaternion.quaternion
                    != secondQuaternion.quaternion
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

}  // namespace

struct BdRbfMultiOrientationWeightNode::Cache {
    bd_util_nodes::RbfSolveStatus evaluate(
        const std::vector<bd_util_nodes::QuaternionSourceDefinition>& sources,
        const std::vector<bd_util_nodes::MultiQuaternionPoseSample>& samples,
        bd_util_nodes::RbfKernel requestedKernel,
        double requestedRadiusRadians,
        double requestedRegularization,
        const std::vector<bd_util_nodes::IndexedQuaternion>& inputQuaternions,
        std::vector<bd_util_nodes::IndexedWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSources(configuredSources, sources)
            || !haveSameSamples(configuredSamples, samples)
            || kernel != requestedKernel
            || radiusRadians != requestedRadiusRadians
            || regularization != requestedRegularization
        ) {
            configuredSources = sources;
            configuredSamples = samples;
            kernel = requestedKernel;
            radiusRadians = requestedRadiusRadians;
            regularization = requestedRegularization;
            configureStatus = interpolator.configure(
                configuredSources,
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
        return interpolator.evaluate(inputQuaternions, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::QuaternionSourceDefinition> configuredSources;
    std::vector<bd_util_nodes::MultiQuaternionPoseSample> configuredSamples;
    bd_util_nodes::RbfKernel kernel = bd_util_nodes::RbfKernel::kQuintic;
    double radiusRadians = 0.0;
    double regularization = 1.0e-8;
    bd_util_nodes::RbfSolveStatus configureStatus =
        bd_util_nodes::RbfSolveStatus::kNoSources;
    bd_util_nodes::MultiQuaternionRbfInterpolator interpolator;
};

BdRbfMultiOrientationWeightNode::BdRbfMultiOrientationWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfMultiOrientationWeightNode::~BdRbfMultiOrientationWeightNode() =
    default;

void* BdRbfMultiOrientationWeightNode::creator() {
    return new BdRbfMultiOrientationWeightNode();
}

MStatus BdRbfMultiOrientationWeightNode::initialize() {
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
    for (const MObject& child : {inputQuat, influence}) {
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

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        sourceQuat,
        sourceQuatX,
        sourceQuatY,
        sourceQuatZ,
        sourceQuatW,
        "sourceQuat",
        "sq",
        "sourceQuatX",
        "sqx",
        "sourceQuatY",
        "sqy",
        "sourceQuatZ",
        "sqz",
        "sourceQuatW",
        "sqw",
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
    for (const MObject& child : {sourceQuat, enabled}) {
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

    solveStatus = enumAttributeFn.create("solveStatus", "ss", 10, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 12>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidRegularization", static_cast<short>(3)},
              {"InvalidQuaternion", static_cast<short>(4)},
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

    const std::array<MObject, 18> inputs = {
        source,
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        influence,
        pose,
        sourceQuat,
        sourceQuatX,
        sourceQuatY,
        sourceQuatZ,
        sourceQuatW,
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

MStatus BdRbfMultiOrientationWeightNode::compute(
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
    std::vector<bd_util_nodes::QuaternionSourceDefinition> sources;
    std::vector<bd_util_nodes::IndexedQuaternion> inputQuaternions;
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
    inputQuaternions.reserve(sourceCount);
    for (unsigned int index = 0; index < sourceCount; ++index) {
        const unsigned int logicalIndex = sourceHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        MDataHandle sourceHandle = sourceHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        const double4& inputValue = sourceHandle.child(inputQuat).asDouble4();
        sources.push_back({
            logicalIndex,
            sourceHandle.child(influence).asDouble(),
        });
        inputQuaternions.push_back({
            logicalIndex,
            {
                inputValue[0],
                inputValue[1],
                inputValue[2],
                inputValue[3],
            },
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
        inputQuaternions.begin(),
        inputQuaternions.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::MultiQuaternionPoseSample> enabledSamples;
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
            bd_util_nodes::MultiQuaternionPoseSample sample;
            sample.logicalIndex = logicalIndex;
            MArrayDataHandle sourceQuatHandles(
                poseHandle.child(sourceQuat),
                &status
            );
            if (!status) {
                return status;
            }
            const unsigned int poseSourceCount =
                sourceQuatHandles.elementCount(&status);
            if (!status) {
                return status;
            }
            sample.sourceQuaternions.reserve(poseSourceCount);
            for (
                unsigned int sourceIndex = 0;
                sourceIndex < poseSourceCount;
                ++sourceIndex
            ) {
                const unsigned int sourceLogicalIndex =
                    sourceQuatHandles.elementIndex(&status);
                if (!status) {
                    return status;
                }
                MDataHandle sourceQuatHandle = sourceQuatHandles.inputValue(
                    &status
                );
                if (!status) {
                    return status;
                }
                const double4& poseValue = sourceQuatHandle.asDouble4();
                sample.sourceQuaternions.push_back({
                    sourceLogicalIndex,
                    {
                        poseValue[0],
                        poseValue[1],
                        poseValue[2],
                        poseValue[3],
                    },
                });
                if (sourceIndex + 1 < poseSourceCount) {
                    status = sourceQuatHandles.next();
                    if (!status) {
                        return status;
                    }
                }
            }
            std::sort(
                sample.sourceQuaternions.begin(),
                sample.sourceQuaternions.end(),
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
        sources,
        enabledSamples,
        static_cast<bd_util_nodes::RbfKernel>(kernelValue),
        radiusRadians,
        regularizationValue,
        inputQuaternions,
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

MPxNode::SchedulingType
BdRbfMultiOrientationWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
