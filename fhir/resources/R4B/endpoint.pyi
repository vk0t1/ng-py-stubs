from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Endpoint(domainresource.DomainResource):
    __resource_type__: str
    address: fhirtypes.UrlType | None
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    connectionType: fhirtypes.CodingType
    contact: list[fhirtypes.ContactPointType] | None
    header: list[fhirtypes.StringType | None] | None
    header__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    payloadMimeType: list[fhirtypes.CodeType | None] | None
    payloadMimeType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    payloadType: list[fhirtypes.CodeableConceptType]
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
