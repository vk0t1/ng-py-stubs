from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class NutritionOrder(domainresource.DomainResource):
    __resource_type__: str
    allergyIntolerance: list[fhirtypes.ReferenceType] | None
    dateTime: fhirtypes.DateTimeType | None
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    enteralFormula: fhirtypes.NutritionOrderEnteralFormulaType | None
    excludeFoodModifier: list[fhirtypes.CodeableConceptType] | None
    foodPreferenceModifier: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    oralDiet: fhirtypes.NutritionOrderOralDietType | None
    orderer: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supplement: list[fhirtypes.NutritionOrderSupplementType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    __resource_type__: str
    additiveProductName: fhirtypes.StringType | None
    additiveProductName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    additiveType: fhirtypes.CodeableConceptType | None
    administration: list[fhirtypes.NutritionOrderEnteralFormulaAdministrationType] | None
    administrationInstruction: fhirtypes.StringType | None
    administrationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    baseFormulaProductName: fhirtypes.StringType | None
    baseFormulaProductName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    baseFormulaType: fhirtypes.CodeableConceptType | None
    caloricDensity: fhirtypes.QuantityType | None
    maxVolumeToDeliver: fhirtypes.QuantityType | None
    routeofAdministration: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    __resource_type__: str
    quantity: fhirtypes.QuantityType | None
    rateQuantity: fhirtypes.QuantityType | None
    rateRatio: fhirtypes.RatioType | None
    schedule: fhirtypes.TimingType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class NutritionOrderOralDiet(backboneelement.BackboneElement):
    __resource_type__: str
    fluidConsistencyType: list[fhirtypes.CodeableConceptType] | None
    instruction: fhirtypes.StringType | None
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nutrient: list[fhirtypes.NutritionOrderOralDietNutrientType] | None
    schedule: list[fhirtypes.TimingType] | None
    texture: list[fhirtypes.NutritionOrderOralDietTextureType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    modifier: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    __resource_type__: str
    foodType: fhirtypes.CodeableConceptType | None
    modifier: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderSupplement(backboneelement.BackboneElement):
    __resource_type__: str
    instruction: fhirtypes.StringType | None
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    productName: fhirtypes.StringType | None
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    schedule: list[fhirtypes.TimingType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
