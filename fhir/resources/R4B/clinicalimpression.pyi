from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ClinicalImpression(domainresource.DomainResource):
    __resource_type__: str
    assessor: fhirtypes.ReferenceType | None
    code: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    encounter: fhirtypes.ReferenceType | None
    finding: list[fhirtypes.ClinicalImpressionFindingType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    investigation: list[fhirtypes.ClinicalImpressionInvestigationType] | None
    note: list[fhirtypes.AnnotationType] | None
    previous: fhirtypes.ReferenceType | None
    problem: list[fhirtypes.ReferenceType] | None
    prognosisCodeableConcept: list[fhirtypes.CodeableConceptType] | None
    prognosisReference: list[fhirtypes.ReferenceType] | None
    protocol: list[fhirtypes.UriType | None] | None
    protocol__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType
    summary: fhirtypes.StringType | None
    summary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportingInfo: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClinicalImpressionFinding(backboneelement.BackboneElement):
    __resource_type__: str
    basis: fhirtypes.StringType | None
    basis__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    item: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
