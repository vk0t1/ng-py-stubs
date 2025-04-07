from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Device(domainresource.DomainResource):
    __resource_type__: str
    contact: list[fhirtypes.ContactPointType] | None
    expirationDate: fhirtypes.DateTimeType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufactureDate: fhirtypes.DateTimeType | None
    manufactureDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.StringType | None
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    model: fhirtypes.StringType | None
    model__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    owner: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType | None
    safety: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    udi: fhirtypes.DeviceUdiType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceUdi(backboneelement.BackboneElement):
    __resource_type__: str
    carrierAIDC: fhirtypes.Base64BinaryType | None
    carrierAIDC__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    carrierHRF: fhirtypes.StringType | None
    carrierHRF__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deviceIdentifier: fhirtypes.StringType | None
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    entryType: fhirtypes.CodeType | None
    entryType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    issuer: fhirtypes.UriType | None
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: fhirtypes.UriType | None
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
