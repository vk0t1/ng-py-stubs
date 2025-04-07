from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Condition(domainresource.DomainResource):
    __resource_type__: str
    abatementAge: fhirtypes.AgeType | None
    abatementBoolean: bool | None
    abatementBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    abatementDateTime: fhirtypes.DateTimeType | None
    abatementDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    abatementPeriod: fhirtypes.PeriodType | None
    abatementRange: fhirtypes.RangeType | None
    abatementString: fhirtypes.StringType | None
    abatementString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    assertedDate: fhirtypes.DateTimeType | None
    assertedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asserter: fhirtypes.ReferenceType | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    clinicalStatus: fhirtypes.CodeType | None
    clinicalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeableConceptType | None
    context: fhirtypes.ReferenceType | None
    evidence: list[fhirtypes.ConditionEvidenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    onsetAge: fhirtypes.AgeType | None
    onsetDateTime: fhirtypes.DateTimeType | None
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onsetPeriod: fhirtypes.PeriodType | None
    onsetRange: fhirtypes.RangeType | None
    onsetString: fhirtypes.StringType | None
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeableConceptType | None
    stage: fhirtypes.ConditionStageType | None
    subject: fhirtypes.ReferenceType
    verificationStatus: fhirtypes.CodeType | None
    verificationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConditionEvidence(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodeableConceptType] | None
    detail: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class ConditionStage(backboneelement.BackboneElement):
    __resource_type__: str
    assessment: list[fhirtypes.ReferenceType] | None
    summary: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
