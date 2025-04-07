from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Substance(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    ingredient: list[fhirtypes.SubstanceIngredientType] | None
    instance: list[fhirtypes.SubstanceInstanceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    quantity: fhirtypes.RatioType | None
    substanceCodeableConcept: fhirtypes.CodeableConceptType | None
    substanceReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SubstanceInstance(backboneelement.BackboneElement):
    __resource_type__: str
    expiry: fhirtypes.DateTimeType | None
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    quantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
