from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Invoice(domainresource.DomainResource):
    __resource_type__: str
    account: fhirtypes.ReferenceType | None
    cancelledReason: fhirtypes.StringType | None
    cancelledReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    creation: fhirtypes.DateTimeType | None
    creation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    issuer: fhirtypes.ReferenceType | None
    lineItem: list[fhirtypes.InvoiceLineItemType] | None
    note: list[fhirtypes.AnnotationType] | None
    participant: list[fhirtypes.InvoiceParticipantType] | None
    paymentTerms: fhirtypes.MarkdownType | None
    paymentTerms__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    periodDate: fhirtypes.DateType | None
    periodDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    periodPeriod: fhirtypes.PeriodType | None
    recipient: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    totalGross: fhirtypes.MoneyType | None
    totalNet: fhirtypes.MoneyType | None
    totalPriceComponent: list[fhirtypes.MonetaryComponentType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class InvoiceLineItem(backboneelement.BackboneElement):
    __resource_type__: str
    chargeItemCodeableConcept: fhirtypes.CodeableConceptType | None
    chargeItemReference: fhirtypes.ReferenceType | None
    priceComponent: list[fhirtypes.MonetaryComponentType] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class InvoiceParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
