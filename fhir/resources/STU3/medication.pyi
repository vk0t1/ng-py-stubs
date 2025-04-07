from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Medication(domainresource.DomainResource):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    form: fhirtypes.CodeableConceptType | None
    image: list[fhirtypes.AttachmentType] | None
    ingredient: list[fhirtypes.MedicationIngredientType] | None
    isBrand: bool | None
    isBrand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    isOverTheCounter: bool | None
    isOverTheCounter__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.ReferenceType | None
    package: fhirtypes.MedicationPackageType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.RatioType | None
    isActive: bool | None
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationPackage(backboneelement.BackboneElement):
    __resource_type__: str
    batch: list[fhirtypes.MedicationPackageBatchType] | None
    container: fhirtypes.CodeableConceptType | None
    content: list[fhirtypes.MedicationPackageContentType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationPackageBatch(backboneelement.BackboneElement):
    __resource_type__: str
    expirationDate: fhirtypes.DateTimeType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationPackageContent(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
