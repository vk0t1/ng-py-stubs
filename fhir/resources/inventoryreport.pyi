from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class InventoryReport(domainresource.DomainResource):
    __resource_type__: str
    countType: fhirtypes.CodeType | None
    countType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    inventoryListing: list[fhirtypes.InventoryReportInventoryListingType] | None
    note: list[fhirtypes.AnnotationType] | None
    operationType: fhirtypes.CodeableConceptType | None
    operationTypeReason: fhirtypes.CodeableConceptType | None
    reportedDateTime: fhirtypes.DateTimeType | None
    reportedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reporter: fhirtypes.ReferenceType | None
    reportingPeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class InventoryReportInventoryListing(backboneelement.BackboneElement):
    __resource_type__: str
    countingDateTime: fhirtypes.DateTimeType | None
    countingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    item: list[fhirtypes.InventoryReportInventoryListingItemType] | None
    itemStatus: fhirtypes.CodeableConceptType | None
    location: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class InventoryReportInventoryListingItem(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    item: fhirtypes.CodeableReferenceType
    quantity: fhirtypes.QuantityType
    @classmethod
    def elements_sequence(cls): ...
