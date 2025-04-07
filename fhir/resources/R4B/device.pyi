from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Device(domainresource.DomainResource):
    __resource_type__: str
    contact: list[fhirtypes.ContactPointType] | None
    definition: fhirtypes.ReferenceType | None
    deviceName: list[fhirtypes.DeviceDeviceNameType] | None
    distinctIdentifier: fhirtypes.StringType | None
    distinctIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    modelNumber: fhirtypes.StringType | None
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    owner: fhirtypes.ReferenceType | None
    parent: fhirtypes.ReferenceType | None
    partNumber: fhirtypes.StringType | None
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType | None
    property: list[fhirtypes.DevicePropertyType] | None
    safety: list[fhirtypes.CodeableConceptType] | None
    serialNumber: fhirtypes.StringType | None
    serialNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    specialization: list[fhirtypes.DeviceSpecializationType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    udiCarrier: list[fhirtypes.DeviceUdiCarrierType] | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.DeviceVersionType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDeviceName(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueCode: list[fhirtypes.CodeableConceptType] | None
    valueQuantity: list[fhirtypes.QuantityType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceSpecialization(backboneelement.BackboneElement):
    __resource_type__: str
    systemType: fhirtypes.CodeableConceptType
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceUdiCarrier(backboneelement.BackboneElement):
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
    @classmethod
    def elements_sequence(cls): ...

class DeviceVersion(backboneelement.BackboneElement):
    __resource_type__: str
    component: fhirtypes.IdentifierType | None
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
