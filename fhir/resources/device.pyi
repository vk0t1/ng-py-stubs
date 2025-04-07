from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Device(domainresource.DomainResource):
    __resource_type__: str
    availabilityStatus: fhirtypes.CodeableConceptType | None
    biologicalSourceEvent: fhirtypes.IdentifierType | None
    category: list[fhirtypes.CodeableConceptType] | None
    conformsTo: list[fhirtypes.DeviceConformsToType] | None
    contact: list[fhirtypes.ContactPointType] | None
    cycle: fhirtypes.CountType | None
    definition: fhirtypes.CodeableReferenceType | None
    displayName: fhirtypes.StringType | None
    displayName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    duration: fhirtypes.DurationType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    expirationDate: fhirtypes.DateTimeType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gateway: list[fhirtypes.CodeableReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufactureDate: fhirtypes.DateTimeType | None
    manufactureDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.StringType | None
    manufacturer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeableConceptType | None
    modelNumber: fhirtypes.StringType | None
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: list[fhirtypes.DeviceNameType] | None
    note: list[fhirtypes.AnnotationType] | None
    owner: fhirtypes.ReferenceType | None
    parent: fhirtypes.ReferenceType | None
    partNumber: fhirtypes.StringType | None
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: list[fhirtypes.DevicePropertyType] | None
    safety: list[fhirtypes.CodeableConceptType] | None
    serialNumber: fhirtypes.StringType | None
    serialNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    udiCarrier: list[fhirtypes.DeviceUdiCarrierType] | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.DeviceVersionType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceConformsTo(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    specification: fhirtypes.CodeableConceptType
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceName(backboneelement.BackboneElement):
    __resource_type__: str
    display: bool | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

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
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceVersion(backboneelement.BackboneElement):
    __resource_type__: str
    component: fhirtypes.IdentifierType | None
    installDate: fhirtypes.DateTimeType | None
    installDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
