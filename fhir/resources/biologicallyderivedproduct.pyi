from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BiologicallyDerivedProduct(domainresource.DomainResource):
    __resource_type__: str
    biologicalSourceEvent: fhirtypes.IdentifierType | None
    collection: fhirtypes.BiologicallyDerivedProductCollectionType | None
    division: fhirtypes.StringType | None
    division__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expirationDate: fhirtypes.DateTimeType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    parent: list[fhirtypes.ReferenceType] | None
    processingFacility: list[fhirtypes.ReferenceType] | None
    productCategory: fhirtypes.CodingType | None
    productCode: fhirtypes.CodeableConceptType | None
    productStatus: fhirtypes.CodingType | None
    property: list[fhirtypes.BiologicallyDerivedProductPropertyType] | None
    request: list[fhirtypes.ReferenceType] | None
    storageTempRequirements: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    __resource_type__: str
    collectedDateTime: fhirtypes.DateTimeType | None
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    collectedPeriod: fhirtypes.PeriodType | None
    collector: fhirtypes.ReferenceType | None
    source: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class BiologicallyDerivedProductProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
