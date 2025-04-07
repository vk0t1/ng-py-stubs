from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationStatement(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: fhirtypes.CodeableConceptType | None
    context: fhirtypes.ReferenceType | None
    dateAsserted: fhirtypes.DateTimeType | None
    dateAsserted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.ReferenceType] | None
    dosage: list[fhirtypes.DosageType] | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: fhirtypes.ReferenceType | None
    medicationCodeableConcept: fhirtypes.CodeableConceptType | None
    medicationReference: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: list[fhirtypes.CodeableConceptType] | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
