from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PaymentNotice(domainresource.DomainResource):
    __resource_type__: str
    amount: fhirtypes.MoneyType
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    payee: fhirtypes.ReferenceType | None
    payment: fhirtypes.ReferenceType | None
    paymentDate: fhirtypes.DateType | None
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentStatus: fhirtypes.CodeableConceptType | None
    recipient: fhirtypes.ReferenceType
    reporter: fhirtypes.ReferenceType | None
    request: fhirtypes.ReferenceType | None
    response: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
