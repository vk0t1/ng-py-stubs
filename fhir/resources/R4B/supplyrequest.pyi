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
    identifier: list[fhirtypes.IdentifierType] | None
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    parameter: list[fhirtypes.SupplyRequestParameterType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supplier: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SupplyRequestParameter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
