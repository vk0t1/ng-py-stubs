from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class InventoryItem(domainresource.DomainResource):
    __resource_type__: str
    association: list[fhirtypes.InventoryItemAssociationType] | None
    baseUnit: fhirtypes.CodeableConceptType | None
    category: list[fhirtypes.CodeableConceptType] | None
    characteristic: list[fhirtypes.InventoryItemCharacteristicType] | None
    code: list[fhirtypes.CodeableConceptType] | None
    description: fhirtypes.InventoryItemDescriptionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instance: fhirtypes.InventoryItemInstanceType | None
    inventoryStatus: list[fhirtypes.CodeableConceptType] | None
    name: list[fhirtypes.InventoryItemNameType] | None
    netContent: fhirtypes.QuantityType | None
    productReference: fhirtypes.ReferenceType | None
    responsibleOrganization: list[fhirtypes.InventoryItemResponsibleOrganizationType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class InventoryItemAssociation(backboneelement.BackboneElement):
    __resource_type__: str
    associationType: fhirtypes.CodeableConceptType
    quantity: fhirtypes.RatioType
    relatedItem: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class InventoryItemCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    characteristicType: fhirtypes.CodeableConceptType
    valueAddress: fhirtypes.AddressType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDuration: fhirtypes.DurationType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUrl: fhirtypes.UrlType | None
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class InventoryItemDescription(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class InventoryItemInstance(backboneelement.BackboneElement):
    __resource_type__: str
    expiry: fhirtypes.DateTimeType | None
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class InventoryItemName(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nameType: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class InventoryItemResponsibleOrganization(backboneelement.BackboneElement):
    __resource_type__: str
    organization: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
