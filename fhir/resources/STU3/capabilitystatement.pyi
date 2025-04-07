from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CapabilityStatement(domainresource.DomainResource):
    __resource_type__: str
    acceptUnknown: fhirtypes.CodeType | None
    acceptUnknown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    document: list[fhirtypes.CapabilityStatementDocumentType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fhirVersion: fhirtypes.IdType | None
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    format: list[fhirtypes.CodeType | None] | None
    format__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    implementation: fhirtypes.CapabilityStatementImplementationType | None
    implementationGuide: list[fhirtypes.UriType | None] | None
    implementationGuide__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiates: list[fhirtypes.UriType | None] | None
    instantiates__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    messaging: list[fhirtypes.CapabilityStatementMessagingType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patchFormat: list[fhirtypes.CodeType | None] | None
    patchFormat__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    profile: list[fhirtypes.ReferenceType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rest: list[fhirtypes.CapabilityStatementRestType] | None
    software: fhirtypes.CapabilityStatementSoftwareType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementDocument(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementImplementation(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementMessaging(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.CapabilityStatementMessagingEndpointType] | None
    event: list[fhirtypes.CapabilityStatementMessagingEventType] | None
    reliableCache: fhirtypes.UnsignedIntType | None
    reliableCache__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportedMessage: list[fhirtypes.CapabilityStatementMessagingSupportedMessageType] | None
    @classmethod
    def elements_sequence(cls): ...

class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    __resource_type__: str
    address: fhirtypes.UriType | None
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    protocol: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementMessagingEvent(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeType | None
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodingType
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    focus: fhirtypes.CodeType | None
    focus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ReferenceType
    response: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    __resource_type__: str
    definition: fhirtypes.ReferenceType
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRest(backboneelement.BackboneElement):
    __resource_type__: str
    compartment: list[fhirtypes.UriType | None] | None
    compartment__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    interaction: list[fhirtypes.CapabilityStatementRestInteractionType] | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operation: list[fhirtypes.CapabilityStatementRestOperationType] | None
    resource: list[fhirtypes.CapabilityStatementRestResourceType] | None
    searchParam: list[fhirtypes.CapabilityStatementRestResourceSearchParamType] | None
    security: fhirtypes.CapabilityStatementRestSecurityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestOperation(backboneelement.BackboneElement):
    __resource_type__: str
    definition: fhirtypes.ReferenceType
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestResource(backboneelement.BackboneElement):
    __resource_type__: str
    conditionalCreate: bool | None
    conditionalCreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    conditionalDelete: fhirtypes.CodeType | None
    conditionalDelete__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    conditionalRead: fhirtypes.CodeType | None
    conditionalRead__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    conditionalUpdate: bool | None
    conditionalUpdate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: fhirtypes.MarkdownType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    interaction: list[fhirtypes.CapabilityStatementRestResourceInteractionType]
    profile: fhirtypes.ReferenceType | None
    readHistory: bool | None
    readHistory__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referencePolicy: list[fhirtypes.CodeType | None] | None
    referencePolicy__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    searchInclude: list[fhirtypes.StringType | None] | None
    searchInclude__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    searchParam: list[fhirtypes.CapabilityStatementRestResourceSearchParamType] | None
    searchRevInclude: list[fhirtypes.StringType | None] | None
    searchRevInclude__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    updateCreate: bool | None
    updateCreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versioning: fhirtypes.CodeType | None
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    __resource_type__: str
    definition: fhirtypes.UriType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    __resource_type__: str
    certificate: list[fhirtypes.CapabilityStatementRestSecurityCertificateType] | None
    cors: bool | None
    cors__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    service: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class CapabilityStatementRestSecurityCertificate(backboneelement.BackboneElement):
    __resource_type__: str
    blob: fhirtypes.Base64BinaryType | None
    blob__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CapabilityStatementSoftware(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    releaseDate: fhirtypes.DateTimeType | None
    releaseDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
