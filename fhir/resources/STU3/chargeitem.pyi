from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ChargeItem(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    bodysite: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.UriType | None] | None
    definition__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    enteredDate: fhirtypes.DateTimeType | None
    enteredDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enterer: fhirtypes.ReferenceType | None
    factorOverride: fhirtypes.DecimalType | None
    factorOverride__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    overrideReason: fhirtypes.StringType | None
    overrideReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    partOf: list[fhirtypes.ReferenceType] | None
    participant: list[fhirtypes.ChargeItemParticipantType] | None
    performingOrganization: fhirtypes.ReferenceType | None
    priceOverride: fhirtypes.MoneyType | None
    quantity: fhirtypes.QuantityType | None
    reason: list[fhirtypes.CodeableConceptType] | None
    requestingOrganization: fhirtypes.ReferenceType | None
    service: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ChargeItemParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
