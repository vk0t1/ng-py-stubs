from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationAdministration(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    device: list[fhirtypes.CodeableReferenceType] | None
    dosage: fhirtypes.MedicationAdministrationDosageType | None
    encounter: fhirtypes.ReferenceType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    isSubPotent: bool | None
    isSubPotent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    medication: fhirtypes.CodeableReferenceType
    note: list[fhirtypes.AnnotationType] | None
    occurenceDateTime: fhirtypes.DateTimeType | None
    occurenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurencePeriod: fhirtypes.PeriodType | None
    occurenceTiming: fhirtypes.TimingType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.MedicationAdministrationPerformerType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    recorded: fhirtypes.DateTimeType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: list[fhirtypes.CodeableConceptType] | None
    subPotentReason: list[fhirtypes.CodeableConceptType] | None
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
    actor: fhirtypes.CodeableReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
