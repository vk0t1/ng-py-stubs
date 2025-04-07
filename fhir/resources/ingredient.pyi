from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Ingredient(domainresource.DomainResource):
    __resource_type__: str
    allergenicIndicator: bool | None
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    for_fhir: list[fhirtypes.ReferenceType] | None
    function: list[fhirtypes.CodeableConceptType] | None
    group: fhirtypes.CodeableConceptType | None
    identifier: fhirtypes.IdentifierType | None
    manufacturer: list[fhirtypes.IngredientManufacturerType] | None
    role: fhirtypes.CodeableConceptType
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    substance: fhirtypes.IngredientSubstanceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class IngredientManufacturer(backboneelement.BackboneElement):
    __resource_type__: str
    manufacturer: fhirtypes.ReferenceType
    role: fhirtypes.CodeType | None
    role__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class IngredientSubstance(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableReferenceType
    strength: list[fhirtypes.IngredientSubstanceStrengthType] | None
    @classmethod
    def elements_sequence(cls): ...

class IngredientSubstanceStrength(backboneelement.BackboneElement):
    __resource_type__: str
    basis: fhirtypes.CodeableConceptType | None
    concentrationCodeableConcept: fhirtypes.CodeableConceptType | None
    concentrationQuantity: fhirtypes.QuantityType | None
    concentrationRatio: fhirtypes.RatioType | None
    concentrationRatioRange: fhirtypes.RatioRangeType | None
    country: list[fhirtypes.CodeableConceptType] | None
    measurementPoint: fhirtypes.StringType | None
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    presentationCodeableConcept: fhirtypes.CodeableConceptType | None
    presentationQuantity: fhirtypes.QuantityType | None
    presentationRatio: fhirtypes.RatioType | None
    presentationRatioRange: fhirtypes.RatioRangeType | None
    referenceStrength: list[fhirtypes.IngredientSubstanceStrengthReferenceStrengthType] | None
    textConcentration: fhirtypes.StringType | None
    textConcentration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    textPresentation: fhirtypes.StringType | None
    textPresentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class IngredientSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    __resource_type__: str
    country: list[fhirtypes.CodeableConceptType] | None
    measurementPoint: fhirtypes.StringType | None
    measurementPoint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    strengthQuantity: fhirtypes.QuantityType | None
    strengthRatio: fhirtypes.RatioType | None
    strengthRatioRange: fhirtypes.RatioRangeType | None
    substance: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
