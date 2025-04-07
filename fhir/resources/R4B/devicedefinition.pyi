from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceDefinition(domainresource.DomainResource):
    __resource_type__: str
    capability: list[fhirtypes.DeviceDefinitionCapabilityType] | None
    contact: list[fhirtypes.ContactPointType] | None
    deviceName: list[fhirtypes.DeviceDefinitionDeviceNameType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    languageCode: list[fhirtypes.CodeableConceptType] | None
    manufacturerReference: fhirtypes.ReferenceType | None
    manufacturerString: fhirtypes.StringType | None
    manufacturerString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    material: list[fhirtypes.DeviceDefinitionMaterialType] | None
    modelNumber: fhirtypes.StringType | None
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    onlineInformation: fhirtypes.UriType | None
    onlineInformation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    owner: fhirtypes.ReferenceType | None
    parentDevice: fhirtypes.ReferenceType | None
    physicalCharacteristics: fhirtypes.ProdCharacteristicType | None
    property: list[fhirtypes.DeviceDefinitionPropertyType] | None
    quantity: fhirtypes.QuantityType | None
    safety: list[fhirtypes.CodeableConceptType] | None
    shelfLifeStorage: list[fhirtypes.ProductShelfLifeType] | None
    specialization: list[fhirtypes.DeviceDefinitionSpecializationType] | None
    type: fhirtypes.CodeableConceptType | None
    udiDeviceIdentifier: list[fhirtypes.DeviceDefinitionUdiDeviceIdentifierType] | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.StringType | None] | None
    version__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DeviceDefinitionCapability(backboneelement.BackboneElement):
    __resource_type__: str
    description: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    __resource_type__: str
    allergenicIndicator: bool | None
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    alternate: bool | None
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    substance: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueCode: list[fhirtypes.CodeableConceptType] | None
    valueQuantity: list[fhirtypes.QuantityType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    __resource_type__: str
    systemType: fhirtypes.StringType | None
    systemType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    __resource_type__: str
    deviceIdentifier: fhirtypes.StringType | None
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    issuer: fhirtypes.UriType | None
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: fhirtypes.UriType | None
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
