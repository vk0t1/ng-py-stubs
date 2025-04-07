from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Specimen(domainresource.DomainResource):
    __resource_type__: str
    accessionIdentifier: fhirtypes.IdentifierType | None
    collection: fhirtypes.SpecimenCollectionType | None
    combined: fhirtypes.CodeType | None
    combined__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    condition: list[fhirtypes.CodeableConceptType] | None
    container: list[fhirtypes.SpecimenContainerType] | None
    feature: list[fhirtypes.SpecimenFeatureType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    parent: list[fhirtypes.ReferenceType] | None
    processing: list[fhirtypes.SpecimenProcessingType] | None
    receivedTime: fhirtypes.DateTimeType | None
    receivedTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: list[fhirtypes.ReferenceType] | None
    role: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SpecimenCollection(backboneelement.BackboneElement):
    __resource_type__: str
    bodySite: fhirtypes.CodeableReferenceType | None
    collectedDateTime: fhirtypes.DateTimeType | None
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    collectedPeriod: fhirtypes.PeriodType | None
    collector: fhirtypes.ReferenceType | None
    device: fhirtypes.CodeableReferenceType | None
    duration: fhirtypes.DurationType | None
    fastingStatusCodeableConcept: fhirtypes.CodeableConceptType | None
    fastingStatusDuration: fhirtypes.DurationType | None
    method: fhirtypes.CodeableConceptType | None
    procedure: fhirtypes.ReferenceType | None
    quantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenContainer(backboneelement.BackboneElement):
    __resource_type__: str
    device: fhirtypes.ReferenceType
    location: fhirtypes.ReferenceType | None
    specimenQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...

class SpecimenFeature(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SpecimenProcessing(backboneelement.BackboneElement):
    __resource_type__: str
    additive: list[fhirtypes.ReferenceType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeableConceptType | None
    timeDateTime: fhirtypes.DateTimeType | None
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
