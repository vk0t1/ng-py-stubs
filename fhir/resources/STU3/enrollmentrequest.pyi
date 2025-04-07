from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EnrollmentRequest(domainresource.DomainResource):
    __resource_type__: str
    coverage: fhirtypes.ReferenceType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurer: fhirtypes.ReferenceType | None
    organization: fhirtypes.ReferenceType | None
    provider: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
