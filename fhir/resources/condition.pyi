from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Condition(domainresource.DomainResource):
    __resource_type__: str
    abatementAge: fhirtypes.AgeType | None
    abatementDateTime: fhirtypes.DateTimeType | None
    abatementDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    abatementPeriod: fhirtypes.PeriodType | None
    abatementRange: fhirtypes.RangeType | None
    abatementString: fhirtypes.StringType | None
    abatementString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    clinicalStatus: fhirtypes.CodeableConceptType
    code: fhirtypes.CodeableConceptType | None
    encounter: fhirtypes.ReferenceType | None
    evidence: list[fhirtypes.CodeableReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    onsetAge: fhirtypes.AgeType | None
    onsetDateTime: fhirtypes.DateTimeType | None
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onsetPeriod: fhirtypes.PeriodType | None
    onsetRange: fhirtypes.RangeType | None
    onsetString: fhirtypes.StringType | None
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participant: list[fhirtypes.ConditionParticipantType] | None
    recordedDate: fhirtypes.DateTimeType | None
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeableConceptType | None
    stage: list[fhirtypes.ConditionStageType] | None
    subject: fhirtypes.ReferenceType
    verificationStatus: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConditionParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ConditionStage(backboneelement.BackboneElement):
    __resource_type__: str
    assessment: list[fhirtypes.ReferenceType] | None
    summary: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
