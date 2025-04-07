from . import backboneelement as backboneelement
from . import fhirtypes as fhirtypes
from . import resource as resource

class Bundle(resource.Resource):
    __resource_type__: str
    entry: list[fhirtypes.BundleEntryType] | None
    identifier: fhirtypes.IdentifierType | None
    link: list[fhirtypes.BundleLinkType] | None
    signature: fhirtypes.SignatureType | None
    timestamp: fhirtypes.InstantType | None
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    total: fhirtypes.UnsignedIntType | None
    total__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class BundleEntry(backboneelement.BackboneElement):
    __resource_type__: str
    fullUrl: fhirtypes.UriType | None
    fullUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    link: list[fhirtypes.BundleLinkType] | None
    request: fhirtypes.BundleEntryRequestType | None
    resource: fhirtypes.ResourceType | None
    response: fhirtypes.BundleEntryResponseType | None
    search: fhirtypes.BundleEntrySearchType | None
    @classmethod
    def elements_sequence(cls): ...

class BundleEntryRequest(backboneelement.BackboneElement):
    __resource_type__: str
    ifMatch: fhirtypes.StringType | None
    ifMatch__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    ifModifiedSince: fhirtypes.InstantType | None
    ifModifiedSince__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    ifNoneExist: fhirtypes.StringType | None
    ifNoneExist__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    ifNoneMatch: fhirtypes.StringType | None
    ifNoneMatch__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeType | None
    method__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class BundleEntryResponse(backboneelement.BackboneElement):
    __resource_type__: str
    etag: fhirtypes.StringType | None
    etag__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lastModified: fhirtypes.InstantType | None
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.UriType | None
    location__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outcome: fhirtypes.ResourceType | None
    status: fhirtypes.StringType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class BundleEntrySearch(backboneelement.BackboneElement):
    __resource_type__: str
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    score: fhirtypes.DecimalType | None
    score__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class BundleLink(backboneelement.BackboneElement):
    __resource_type__: str
    relation: fhirtypes.StringType | None
    relation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
