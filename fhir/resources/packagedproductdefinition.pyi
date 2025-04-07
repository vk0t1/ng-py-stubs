from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PackagedProductDefinition(domainresource.DomainResource):
    __resource_type__: str
    attachedDocument: list[fhirtypes.ReferenceType] | None
    characteristic: list[fhirtypes.PackagedProductDefinitionPackagingPropertyType] | None
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
    packageFor: list[fhirtypes.ReferenceType] | None
    packaging: fhirtypes.PackagedProductDefinitionPackagingType | None
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

class PackagedProductDefinitionPackaging(backboneelement.BackboneElement):
    __resource_type__: str
    alternateMaterial: list[fhirtypes.CodeableConceptType] | None
    componentPart: bool | None
    componentPart__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    containedItem: list[fhirtypes.PackagedProductDefinitionPackagingContainedItemType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    manufacturer: list[fhirtypes.ReferenceType] | None
    material: list[fhirtypes.CodeableConceptType] | None
    packaging: list[fhirtypes.PackagedProductDefinitionPackagingType] | None
    property: list[fhirtypes.PackagedProductDefinitionPackagingPropertyType] | None
    quantity: fhirtypes.IntegerType | None
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    shelfLifeStorage: list[fhirtypes.ProductShelfLifeType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionPackagingContainedItem(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    item: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...

class PackagedProductDefinitionPackagingProperty(backboneelement.BackboneElement):
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
