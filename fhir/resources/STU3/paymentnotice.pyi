from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PaymentNotice(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    organization: fhirtypes.ReferenceType | None
    paymentStatus: fhirtypes.CodeableConceptType | None
    provider: fhirtypes.ReferenceType | None
    request: fhirtypes.ReferenceType | None
    response: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusDate: fhirtypes.DateType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
