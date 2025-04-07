from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AdverseEvent(domainresource.DomainResource):
    __resource_type__: str
    actuality: fhirtypes.CodeType | None
    actuality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType | None
    contributingFactor: list[fhirtypes.AdverseEventContributingFactorType] | None
    detected: fhirtypes.DateTimeType | None
    detected__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    expectedInResearchStudy: bool | None
    expectedInResearchStudy__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    mitigatingAction: list[fhirtypes.AdverseEventMitigatingActionType] | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    outcome: list[fhirtypes.CodeableConceptType] | None
    participant: list[fhirtypes.AdverseEventParticipantType] | None
    preventiveAction: list[fhirtypes.AdverseEventPreventiveActionType] | None
    recordedDate: fhirtypes.DateTimeType | None
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recorder: fhirtypes.ReferenceType | None
    resultingEffect: list[fhirtypes.ReferenceType] | None
    seriousness: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    study: list[fhirtypes.ReferenceType] | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.AdverseEventSupportingInfoType] | None
    suspectEntity: list[fhirtypes.AdverseEventSuspectEntityType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventContributingFactor(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventMitigatingAction(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class AdverseEventPreventiveAction(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventSupportingInfo(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    __resource_type__: str
    causality: fhirtypes.AdverseEventSuspectEntityCausalityType | None
    instanceCodeableConcept: fhirtypes.CodeableConceptType | None
    instanceReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    __resource_type__: str
    assessmentMethod: fhirtypes.CodeableConceptType | None
    author: fhirtypes.ReferenceType | None
    entityRelatedness: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
