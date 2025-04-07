from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class NutritionProduct(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    characteristic: list[fhirtypes.NutritionProductCharacteristicType] | None
    code: fhirtypes.CodeableConceptType | None
    ingredient: list[fhirtypes.NutritionProductIngredientType] | None
    instance: list[fhirtypes.NutritionProductInstanceType] | None
    knownAllergen: list[fhirtypes.CodeableReferenceType] | None
    manufacturer: list[fhirtypes.ReferenceType] | None
    note: list[fhirtypes.AnnotationType] | None
    nutrient: list[fhirtypes.NutritionProductNutrientType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class NutritionProductCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class NutritionProductIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    amount: list[fhirtypes.RatioType] | None
    item: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...

class NutritionProductInstance(backboneelement.BackboneElement):
    __resource_type__: str
    biologicalSourceEvent: fhirtypes.IdentifierType | None
    expiry: fhirtypes.DateTimeType | None
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    useBy: fhirtypes.DateTimeType | None
    useBy__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionProductNutrient(backboneelement.BackboneElement):
    __resource_type__: str
    amount: list[fhirtypes.RatioType] | None
    item: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
