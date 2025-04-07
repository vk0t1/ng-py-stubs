from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PaymentReconciliation(domainresource.DomainResource):
    __resource_type__: str
    accountNumber: fhirtypes.StringType | None
    accountNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    allocation: list[fhirtypes.PaymentReconciliationAllocationType] | None
    amount: fhirtypes.MoneyType
    authorization: fhirtypes.StringType | None
    authorization__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    cardBrand: fhirtypes.StringType | None
    cardBrand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enterer: fhirtypes.ReferenceType | None
    expirationDate: fhirtypes.DateType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    formCode: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    issuerType: fhirtypes.CodeableConceptType | None
    kind: fhirtypes.CodeableConceptType | None
    location: fhirtypes.ReferenceType | None
    method: fhirtypes.CodeableConceptType | None
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentIdentifier: fhirtypes.IdentifierType | None
    paymentIssuer: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    processNote: list[fhirtypes.PaymentReconciliationProcessNoteType] | None
    processor: fhirtypes.StringType | None
    processor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceNumber: fhirtypes.StringType | None
    referenceNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ReferenceType | None
    requestor: fhirtypes.ReferenceType | None
    returnedAmount: fhirtypes.MoneyType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tenderedAmount: fhirtypes.MoneyType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class PaymentReconciliationAllocation(backboneelement.BackboneElement):
    __resource_type__: str
    account: fhirtypes.ReferenceType | None
    amount: fhirtypes.MoneyType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: fhirtypes.IdentifierType | None
    payee: fhirtypes.ReferenceType | None
    predecessor: fhirtypes.IdentifierType | None
    response: fhirtypes.ReferenceType | None
    responsible: fhirtypes.ReferenceType | None
    submitter: fhirtypes.ReferenceType | None
    target: fhirtypes.ReferenceType | None
    targetItemIdentifier: fhirtypes.IdentifierType | None
    targetItemPositiveInt: fhirtypes.PositiveIntType | None
    targetItemPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetItemString: fhirtypes.StringType | None
    targetItemString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
