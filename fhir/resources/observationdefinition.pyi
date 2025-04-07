from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ObservationDefinition(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bodySite: fhirtypes.CodeableConceptType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    component: list[fhirtypes.ObservationDefinitionComponentType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFromCanonical: list[fhirtypes.CanonicalType | None] | None
    derivedFromCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    derivedFromUri: list[fhirtypes.UriType | None] | None
    derivedFromUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: list[fhirtypes.ReferenceType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hasMember: list[fhirtypes.ReferenceType] | None
    identifier: fhirtypes.IdentifierType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeableConceptType | None
    multipleResultsAllowed: bool | None
    multipleResultsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performerType: fhirtypes.CodeableConceptType | None
    permittedDataType: list[fhirtypes.CodeType | None] | None
    permittedDataType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    permittedUnit: list[fhirtypes.CodingType] | None
    preferredReportName: fhirtypes.StringType | None
    preferredReportName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    qualifiedValue: list[fhirtypes.ObservationDefinitionQualifiedValueType] | None
    specimen: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: list[fhirtypes.CodeableConceptType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ObservationDefinitionComponent(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    permittedDataType: list[fhirtypes.CodeType | None] | None
    permittedDataType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    permittedUnit: list[fhirtypes.CodingType] | None
    qualifiedValue: list[fhirtypes.ObservationDefinitionQualifiedValueType] | None
    @classmethod
    def elements_sequence(cls): ...

class ObservationDefinitionQualifiedValue(backboneelement.BackboneElement):
    __resource_type__: str
    abnormalCodedValueSet: fhirtypes.CanonicalType | None
    abnormalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    age: fhirtypes.RangeType | None
    appliesTo: list[fhirtypes.CodeableConceptType] | None
    condition: fhirtypes.StringType | None
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    context: fhirtypes.CodeableConceptType | None
    criticalCodedValueSet: fhirtypes.CanonicalType | None
    criticalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gestationalAge: fhirtypes.RangeType | None
    normalCodedValueSet: fhirtypes.CanonicalType | None
    normalCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    range: fhirtypes.RangeType | None
    rangeCategory: fhirtypes.CodeType | None
    rangeCategory__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validCodedValueSet: fhirtypes.CanonicalType | None
    validCodedValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
