from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class NutritionOrder(domainresource.DomainResource):
    __resource_type__: str
    allergyIntolerance: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    dateTime: fhirtypes.DateTimeType | None
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    enteralFormula: fhirtypes.NutritionOrderEnteralFormulaType | None
    excludeFoodModifier: list[fhirtypes.CodeableConceptType] | None
    foodPreferenceModifier: list[fhirtypes.CodeableConceptType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiates: list[fhirtypes.UriType | None] | None
    instantiates__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    oralDiet: fhirtypes.NutritionOrderOralDietType | None
    orderer: fhirtypes.ReferenceType | None
    outsideFoodAllowed: bool | None
    outsideFoodAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: list[fhirtypes.CodeableReferenceType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supplement: list[fhirtypes.NutritionOrderSupplementType] | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    __resource_type__: str
    additive: list[fhirtypes.NutritionOrderEnteralFormulaAdditiveType] | None
    administration: list[fhirtypes.NutritionOrderEnteralFormulaAdministrationType] | None
    administrationInstruction: fhirtypes.MarkdownType | None
    administrationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    baseFormulaProductName: fhirtypes.StringType | None
    baseFormulaProductName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    baseFormulaType: fhirtypes.CodeableReferenceType | None
    caloricDensity: fhirtypes.QuantityType | None
    deliveryDevice: list[fhirtypes.CodeableReferenceType] | None
    maxVolumeToDeliver: fhirtypes.QuantityType | None
    routeOfAdministration: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderEnteralFormulaAdditive(backboneelement.BackboneElement):
    __resource_type__: str
    productName: fhirtypes.StringType | None
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    type: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    __resource_type__: str
    quantity: fhirtypes.QuantityType | None
    rateQuantity: fhirtypes.QuantityType | None
    rateRatio: fhirtypes.RatioType | None
    schedule: fhirtypes.NutritionOrderEnteralFormulaAdministrationScheduleType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class NutritionOrderEnteralFormulaAdministrationSchedule(backboneelement.BackboneElement):
    __resource_type__: str
    asNeeded: bool | None
    asNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededFor: fhirtypes.CodeableConceptType | None
    timing: list[fhirtypes.TimingType] | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderOralDiet(backboneelement.BackboneElement):
    __resource_type__: str
    fluidConsistencyType: list[fhirtypes.CodeableConceptType] | None
    instruction: fhirtypes.StringType | None
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nutrient: list[fhirtypes.NutritionOrderOralDietNutrientType] | None
    schedule: fhirtypes.NutritionOrderOralDietScheduleType | None
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

class NutritionOrderOralDietSchedule(backboneelement.BackboneElement):
    __resource_type__: str
    asNeeded: bool | None
    asNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededFor: fhirtypes.CodeableConceptType | None
    timing: list[fhirtypes.TimingType] | None
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
    schedule: fhirtypes.NutritionOrderSupplementScheduleType | None
    type: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class NutritionOrderSupplementSchedule(backboneelement.BackboneElement):
    __resource_type__: str
    asNeeded: bool | None
    asNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededFor: fhirtypes.CodeableConceptType | None
    timing: list[fhirtypes.TimingType] | None
    @classmethod
    def elements_sequence(cls): ...
