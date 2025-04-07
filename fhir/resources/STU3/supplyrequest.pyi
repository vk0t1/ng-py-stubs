from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SupplyRequest(domainresource.DomainResource):
    __resource_type__: str
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    category: fhirtypes.CodeableConceptType | None
    deliverFrom: fhirtypes.ReferenceType | None
    deliverTo: fhirtypes.ReferenceType | None
    identifier: fhirtypes.IdentifierType | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    orderedItem: fhirtypes.SupplyRequestOrderedItemType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCodeableConcept: fhirtypes.CodeableConceptType | None
    reasonReference: fhirtypes.ReferenceType | None
    requester: fhirtypes.SupplyRequestRequesterType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supplier: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SupplyRequestOrderedItem(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    quantity: fhirtypes.QuantityType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SupplyRequestRequester(backboneelement.BackboneElement):
    __resource_type__: str
    agent: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
