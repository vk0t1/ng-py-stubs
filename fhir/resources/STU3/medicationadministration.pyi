from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationAdministration(domainresource.DomainResource):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    device: list[fhirtypes.ReferenceType] | None
    dosage: fhirtypes.MedicationAdministrationDosageType | None
    effectiveDateTime: fhirtypes.DateTimeType | None
    effectiveDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    medicationCodeableConcept: fhirtypes.CodeableConceptType | None
    medicationReference: fhirtypes.ReferenceType | None
    notGiven: bool | None
    notGiven__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.MedicationAdministrationPerformerType] | None
    prescription: fhirtypes.ReferenceType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonNotGiven: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    __resource_type__: str
    dose: fhirtypes.QuantityType | None
    method: fhirtypes.CodeableConceptType | None
    rateQuantity: fhirtypes.QuantityType | None
    rateRatio: fhirtypes.RatioType | None
    route: fhirtypes.CodeableConceptType | None
    site: fhirtypes.CodeableConceptType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
