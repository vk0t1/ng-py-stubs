from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SpecimenDefinition(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    collection: list[fhirtypes.CodeableConceptType] | None
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
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patientPreparation: list[fhirtypes.CodeableConceptType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    timeAspect: fhirtypes.StringType | None
    timeAspect__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeCollected: fhirtypes.CodeableConceptType | None
    typeTested: list[fhirtypes.SpecimenDefinitionTypeTestedType] | None
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

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    __resource_type__: str
    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType | None
    handling: list[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] | None
    isDerived: bool | None
    isDerived__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preference: fhirtypes.CodeType | None
    preference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rejectionCriterion: list[fhirtypes.CodeableConceptType] | None
    requirement: fhirtypes.MarkdownType | None
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    retentionTime: fhirtypes.DurationType | None
    singleUse: bool | None
    singleUse__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    testingDestination: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    __resource_type__: str
    additive: list[fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType] | None
    cap: fhirtypes.CodeableConceptType | None
    capacity: fhirtypes.QuantityType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    material: fhirtypes.CodeableConceptType | None
    minimumVolumeQuantity: fhirtypes.QuantityType | None
    minimumVolumeString: fhirtypes.StringType | None
    minimumVolumeString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preparation: fhirtypes.MarkdownType | None
    preparation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    __resource_type__: str
    additiveCodeableConcept: fhirtypes.CodeableConceptType | None
    additiveReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    __resource_type__: str
    instruction: fhirtypes.MarkdownType | None
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxDuration: fhirtypes.DurationType | None
    temperatureQualifier: fhirtypes.CodeableConceptType | None
    temperatureRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
