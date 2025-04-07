from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Invoice(domainresource.DomainResource):
    __resource_type__: str
    account: fhirtypes.ReferenceType | None
    cancelledReason: fhirtypes.StringType | None
    cancelledReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    issuer: fhirtypes.ReferenceType | None
    lineItem: list[fhirtypes.InvoiceLineItemType] | None
    note: list[fhirtypes.AnnotationType] | None
    participant: list[fhirtypes.InvoiceParticipantType] | None
    paymentTerms: fhirtypes.MarkdownType | None
    paymentTerms__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recipient: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    totalGross: fhirtypes.MoneyType | None
    totalNet: fhirtypes.MoneyType | None
    totalPriceComponent: list[fhirtypes.InvoiceLineItemPriceComponentType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class InvoiceLineItem(backboneelement.BackboneElement):
    __resource_type__: str
    chargeItemCodeableConcept: fhirtypes.CodeableConceptType | None
    chargeItemReference: fhirtypes.ReferenceType | None
    priceComponent: list[fhirtypes.InvoiceLineItemPriceComponentType] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    code: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class InvoiceParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
