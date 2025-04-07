from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AdverseEvent(domainresource.DomainResource):
    __resource_type__: str
    category: fhirtypes.CodeType | None
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventParticipant: fhirtypes.ReferenceType | None
    identifier: fhirtypes.IdentifierType | None
    location: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeableConceptType | None
    reaction: list[fhirtypes.ReferenceType] | None
    recorder: fhirtypes.ReferenceType | None
    referenceDocument: list[fhirtypes.ReferenceType] | None
    seriousness: fhirtypes.CodeableConceptType | None
    study: list[fhirtypes.ReferenceType] | None
    subject: fhirtypes.ReferenceType | None
    subjectMedicalHistory: list[fhirtypes.ReferenceType] | None
    suspectEntity: list[fhirtypes.AdverseEventSuspectEntityType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    __resource_type__: str
    causality: fhirtypes.CodeType | None
    causality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    causalityAssessment: fhirtypes.CodeableConceptType | None
    causalityAuthor: fhirtypes.ReferenceType | None
    causalityMethod: fhirtypes.CodeableConceptType | None
    causalityProductRelatedness: fhirtypes.StringType | None
    causalityProductRelatedness__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    causalityResult: fhirtypes.CodeableConceptType | None
    instance: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
