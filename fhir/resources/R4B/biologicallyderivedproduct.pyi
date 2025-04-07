from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BiologicallyDerivedProduct(domainresource.DomainResource):
    __resource_type__: str
    collection: fhirtypes.BiologicallyDerivedProductCollectionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    manipulation: fhirtypes.BiologicallyDerivedProductManipulationType | None
    parent: list[fhirtypes.ReferenceType] | None
    processing: list[fhirtypes.BiologicallyDerivedProductProcessingType] | None
    productCategory: fhirtypes.CodeType | None
    productCategory__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    productCode: fhirtypes.CodeableConceptType | None
    quantity: fhirtypes.IntegerType | None
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    storage: list[fhirtypes.BiologicallyDerivedProductStorageType] | None
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

class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timeDateTime: fhirtypes.DateTimeType | None
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    __resource_type__: str
    additive: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    procedure: fhirtypes.CodeableConceptType | None
    timeDateTime: fhirtypes.DateTimeType | None
    timeDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timePeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    duration: fhirtypes.PeriodType | None
    scale: fhirtypes.CodeType | None
    scale__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    temperature: fhirtypes.DecimalType | None
    temperature__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
