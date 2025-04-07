from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PaymentReconciliation(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detail: list[fhirtypes.PaymentReconciliationDetailType] | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    formCode: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentAmount: fhirtypes.MoneyType
    paymentDate: fhirtypes.DateType | None
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentIdentifier: fhirtypes.IdentifierType | None
    paymentIssuer: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    processNote: list[fhirtypes.PaymentReconciliationProcessNoteType] | None
    request: fhirtypes.ReferenceType | None
    requestor: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    payee: fhirtypes.ReferenceType | None
    predecessor: fhirtypes.IdentifierType | None
    request: fhirtypes.ReferenceType | None
    response: fhirtypes.ReferenceType | None
    responsible: fhirtypes.ReferenceType | None
    submitter: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
