from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationStatement(domainresource.DomainResource):
    __resource_type__: str
    adherence: fhirtypes.MedicationStatementAdherenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    dateAsserted: fhirtypes.DateTimeType | None
    dateAsserted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.ReferenceType] | None
    dosage: list[fhirtypes.DosageType] | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    effectiveTiming: fhirtypes.TimingType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: list[fhirtypes.ReferenceType] | None
    medication: fhirtypes.CodeableReferenceType
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    relatedClinicalInformation: list[fhirtypes.ReferenceType] | None
    renderedDosageInstruction: fhirtypes.MarkdownType | None
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationStatementAdherence(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    reason: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
