from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MessageHeader(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    destination: list[fhirtypes.MessageHeaderDestinationType] | None
    enterer: fhirtypes.ReferenceType | None
    event: fhirtypes.CodingType
    focus: list[fhirtypes.ReferenceType] | None
    reason: fhirtypes.CodeableConceptType | None
    receiver: fhirtypes.ReferenceType | None
    response: fhirtypes.MessageHeaderResponseType | None
    responsible: fhirtypes.ReferenceType | None
    sender: fhirtypes.ReferenceType | None
    source: fhirtypes.MessageHeaderSourceType
    timestamp: fhirtypes.InstantType | None
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MessageHeaderDestination(backboneelement.BackboneElement):
    __resource_type__: str
    endpoint: fhirtypes.UriType | None
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MessageHeaderResponse(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    details: fhirtypes.ReferenceType | None
    identifier: fhirtypes.IdType | None
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MessageHeaderSource(backboneelement.BackboneElement):
    __resource_type__: str
    contact: fhirtypes.ContactPointType | None
    endpoint: fhirtypes.UriType | None
    endpoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    software: fhirtypes.StringType | None
    software__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
