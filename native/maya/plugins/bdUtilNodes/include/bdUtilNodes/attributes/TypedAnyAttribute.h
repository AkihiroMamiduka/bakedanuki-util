#pragma once

#include <maya/MStatus.h>

class MFnTypedAttribute;
class MObject;

namespace bd_util_nodes {

MStatus createTypedAnyAttribute(
    MFnTypedAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName
);

MStatus configureInputTypedAttribute(MFnTypedAttribute& attributeFn);

MStatus configureOutputTypedAttribute(MFnTypedAttribute& attributeFn);

}  // namespace bd_util_nodes
