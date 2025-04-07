from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Endpoint(domainresource.DomainResource):
    __resource_type__: str
    address: fhirtypes.UrlType | None
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    connectionType: list[fhirtypes.CodeableConceptType]
    contact: list[fhirtypes.ContactPointType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    environmentType: list[fhirtypes.CodeableConceptType] | None
    header: list[fhirtypes.StringType | None] | None
    header__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    payload: list[fhirtypes.EndpointPayloadType] | None
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EndpointPayload(backboneelement.BackboneElement):
    __resource_type__: str
    mimeType: list[fhirtypes.CodeType | None] | None
    mimeType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
