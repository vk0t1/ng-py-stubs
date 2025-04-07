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
    form: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    organization: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeableConceptType | None
    period: fhirtypes.PeriodType | None
    processNote: list[fhirtypes.PaymentReconciliationProcessNoteType] | None
    request: fhirtypes.ReferenceType | None
    requestOrganization: fhirtypes.ReferenceType | None
    requestProvider: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    total: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    payee: fhirtypes.ReferenceType | None
    request: fhirtypes.ReferenceType | None
    response: fhirtypes.ReferenceType | None
    submitter: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
