from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AdverseEvent(domainresource.DomainResource):
    __resource_type__: str
    actuality: fhirtypes.CodeType | None
    actuality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    category: list[fhirtypes.CodeableConceptType] | None
    contributor: list[fhirtypes.ReferenceType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detected: fhirtypes.DateTimeType | None
    detected__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    event: fhirtypes.CodeableConceptType | None
    identifier: fhirtypes.IdentifierType | None
    location: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeableConceptType | None
    recordedDate: fhirtypes.DateTimeType | None
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recorder: fhirtypes.ReferenceType | None
    referenceDocument: list[fhirtypes.ReferenceType] | None
    resultingCondition: list[fhirtypes.ReferenceType] | None
    seriousness: fhirtypes.CodeableConceptType | None
    severity: fhirtypes.CodeableConceptType | None
    study: list[fhirtypes.ReferenceType] | None
    subject: fhirtypes.ReferenceType
    subjectMedicalHistory: list[fhirtypes.ReferenceType] | None
    suspectEntity: list[fhirtypes.AdverseEventSuspectEntityType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    __resource_type__: str
    causality: list[fhirtypes.AdverseEventSuspectEntityCausalityType] | None
    instance: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    __resource_type__: str
    assessment: fhirtypes.CodeableConceptType | None
    author: fhirtypes.ReferenceType | None
    method: fhirtypes.CodeableConceptType | None
    productRelatedness: fhirtypes.StringType | None
    productRelatedness__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
