from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CatalogEntry(domainresource.DomainResource):
    __resource_type__: str
    additionalCharacteristic: list[fhirtypes.CodeableConceptType] | None
    additionalClassification: list[fhirtypes.CodeableConceptType] | None
    additionalIdentifier: list[fhirtypes.IdentifierType] | None
    classification: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    lastUpdated: fhirtypes.DateTimeType | None
    lastUpdated__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    orderable: bool | None
    orderable__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referencedItem: fhirtypes.ReferenceType
    relatedEntry: list[fhirtypes.CatalogEntryRelatedEntryType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    validTo: fhirtypes.DateTimeType | None
    validTo__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validityPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    __resource_type__: str
    item: fhirtypes.ReferenceType
    relationtype: fhirtypes.CodeType | None
    relationtype__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
