from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Specimen(domainresource.DomainResource):
    __resource_type__: str
    accessionIdentifier: fhirtypes.IdentifierType | None
    collection: fhirtypes.SpecimenCollectionType | None
    condition: list[fhirtypes.CodeableConceptType] | None
    container: list[fhirtypes.SpecimenContainerType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    parent: list[fhirtypes.ReferenceType] | None
    processing: list[fhirtypes.SpecimenProcessingType] | None
    receivedTime: fhirtypes.DateTimeType | None
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SpecimenCollection(backboneelement.BackboneElement):
    __resource_type__: str
    bodySite: fhirtypes.CodeableConceptType | None
    collectedDateTime: fhirtypes.DateTimeType | None
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    collectedPeriod: fhirtypes.PeriodType | None
    collector: fhirtypes.ReferenceType | None
    duration: fhirtypes.DurationType | None
    fastingStatusCodeableConcept: fhirtypes.CodeableConceptType | None
    fastingStatusDuration: fhirtypes.DurationType | None
    method: fhirtypes.CodeableConceptType | None
    quantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenContainer(backboneelement.BackboneElement):
    __resource_type__: str
    additiveCodeableConcept: fhirtypes.CodeableConceptType | None
    additiveReference: fhirtypes.ReferenceType | None
    capacity: fhirtypes.QuantityType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    specimenQuantity: fhirtypes.QuantityType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenProcessing(backboneelement.BackboneElement):
    __resource_type__: str
    additive: list[fhirtypes.ReferenceType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    procedure: fhirtypes.CodeableConceptType | None
    timeDateTime: fhirtypes.DateTimeType | None
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
