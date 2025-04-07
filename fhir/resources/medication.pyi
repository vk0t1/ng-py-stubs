from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Medication(domainresource.DomainResource):
    __resource_type__: str
    batch: fhirtypes.MedicationBatchType | None
    code: fhirtypes.CodeableConceptType | None
    definition: fhirtypes.ReferenceType | None
    doseForm: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    ingredient: list[fhirtypes.MedicationIngredientType] | None
    marketingAuthorizationHolder: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    totalVolume: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationBatch(backboneelement.BackboneElement):
    __resource_type__: str
    expirationDate: fhirtypes.DateTimeType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    isActive: bool | None
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    item: fhirtypes.CodeableReferenceType
    strengthCodeableConcept: fhirtypes.CodeableConceptType | None
    strengthQuantity: fhirtypes.QuantityType | None
    strengthRatio: fhirtypes.RatioType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
