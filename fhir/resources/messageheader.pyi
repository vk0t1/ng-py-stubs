from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MessageHeader(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    definition: fhirtypes.CanonicalType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    destination: list[fhirtypes.MessageHeaderDestinationType] | None
    eventCanonical: fhirtypes.CanonicalType | None
    eventCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventCoding: fhirtypes.CodingType | None
    focus: list[fhirtypes.ReferenceType] | None
    reason: fhirtypes.CodeableConceptType | None
    response: fhirtypes.MessageHeaderResponseType | None
    responsible: fhirtypes.ReferenceType | None
    sender: fhirtypes.ReferenceType | None
    source: fhirtypes.MessageHeaderSourceType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MessageHeaderDestination(backboneelement.BackboneElement):
    __resource_type__: str
    endpointReference: fhirtypes.ReferenceType | None
    endpointUrl: fhirtypes.UrlType | None
    endpointUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    receiver: fhirtypes.ReferenceType | None
    target: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MessageHeaderResponse(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    details: fhirtypes.ReferenceType | None
    identifier: fhirtypes.IdentifierType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MessageHeaderSource(backboneelement.BackboneElement):
    __resource_type__: str
    contact: fhirtypes.ContactPointType | None
    endpointReference: fhirtypes.ReferenceType | None
    endpointUrl: fhirtypes.UrlType | None
    endpointUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    software: fhirtypes.StringType | None
    software__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
