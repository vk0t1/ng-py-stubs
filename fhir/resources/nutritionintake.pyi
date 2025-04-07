from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class NutritionIntake(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    consumedItem: list[fhirtypes.NutritionIntakeConsumedItemType]
    derivedFrom: list[fhirtypes.ReferenceType] | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    ingredientLabel: list[fhirtypes.NutritionIntakeIngredientLabelType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    location: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.NutritionIntakePerformerType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    recorded: fhirtypes.DateTimeType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reportedBoolean: bool | None
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reportedReference: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: list[fhirtypes.CodeableConceptType] | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class NutritionIntakeConsumedItem(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    notConsumed: bool | None
    notConsumed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notConsumedReason: fhirtypes.CodeableConceptType | None
    nutritionProduct: fhirtypes.CodeableReferenceType
    rate: fhirtypes.QuantityType | None
    schedule: fhirtypes.TimingType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class NutritionIntakeIngredientLabel(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType
    nutrient: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...

class NutritionIntakePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
