from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ManufacturedItemDefinition(domainresource.DomainResource):
    __resource_type__: str
    component: list[fhirtypes.ManufacturedItemDefinitionComponentType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    ingredient: list[fhirtypes.CodeableConceptType] | None
    manufacturedDoseForm: fhirtypes.CodeableConceptType
    manufacturer: list[fhirtypes.ReferenceType] | None
    marketingStatus: list[fhirtypes.MarketingStatusType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: list[fhirtypes.ManufacturedItemDefinitionPropertyType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unitOfPresentation: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ManufacturedItemDefinitionComponent(backboneelement.BackboneElement):
    __resource_type__: str
    amount: list[fhirtypes.QuantityType] | None
    component: list[fhirtypes.ManufacturedItemDefinitionComponentType] | None
    constituent: list[fhirtypes.ManufacturedItemDefinitionComponentConstituentType] | None
    function: list[fhirtypes.CodeableConceptType] | None
    property: list[fhirtypes.ManufacturedItemDefinitionPropertyType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ManufacturedItemDefinitionComponentConstituent(backboneelement.BackboneElement):
    __resource_type__: str
    amount: list[fhirtypes.QuantityType] | None
    function: list[fhirtypes.CodeableConceptType] | None
    hasIngredient: list[fhirtypes.CodeableReferenceType] | None
    location: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ManufacturedItemDefinitionProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
