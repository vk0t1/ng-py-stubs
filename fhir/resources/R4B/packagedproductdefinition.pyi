from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PackagedProductDefinition(domainresource.DomainResource):
    __resource_type__: str
    characteristic: list[fhirtypes.CodeableConceptType] | None
    containedItemQuantity: list[fhirtypes.QuantityType] | None
    copackagedIndicator: bool | None
    copackagedIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    legalStatusOfSupply: list[fhirtypes.PackagedProductDefinitionLegalStatusOfSupplyType] | None
    manufacturer: list[fhirtypes.ReferenceType] | None
    marketingStatus: list[fhirtypes.MarketingStatusType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    package: fhirtypes.PackagedProductDefinitionPackageType | None
    packageFor: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeableConceptType | None
    statusDate: fhirtypes.DateTimeType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionLegalStatusOfSupply(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    jurisdiction: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionPackage(backboneelement.BackboneElement):
    __resource_type__: str
    alternateMaterial: list[fhirtypes.CodeableConceptType] | None
    containedItem: list[fhirtypes.PackagedProductDefinitionPackageContainedItemType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    manufacturer: list[fhirtypes.ReferenceType] | None
    material: list[fhirtypes.CodeableConceptType] | None
    package: list[fhirtypes.PackagedProductDefinitionPackageType] | None
    property: list[fhirtypes.PackagedProductDefinitionPackagePropertyType] | None
    quantity: fhirtypes.IntegerType | None
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    shelfLifeStorage: list[fhirtypes.PackagedProductDefinitionPackageShelfLifeStorageType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionPackageContainedItem(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    item: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionPackageProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PackagedProductDefinitionPackageShelfLifeStorage(backboneelement.BackboneElement):
    __resource_type__: str
    periodDuration: fhirtypes.DurationType | None
    periodString: fhirtypes.StringType | None
    periodString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    specialPrecautionsForStorage: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
